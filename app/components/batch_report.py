"""Render the reviewed Batch markdown as the source-of-truth report.

The SQLite overlay is useful for filtering and aggregation, but the reviewed
Batch markdown contains the fullest company and idea narrative.  This module
links each curated idea back to that markdown. A database row selects a company,
and every reviewed thesis for that company is shown without shortening it.
"""

from __future__ import annotations

import json
import re
import gzip
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parents[2]

BATCH_SOURCES = (
    ("farfetch_deep_v7.json", "batch_001_farfetch.md", "Batch 001"),
    ("hawaiian_electric_deep_v7.json", "batch_002_hawaiian_electric.md", "Batch 002"),
    ("american_express_gfc_deep_v7.json", "batch_003_american_express_gfc.md", "Batch 003"),
    ("american_express_costco_antitrust_deep_v7.json", "batch_004_american_express_costco_antitrust.md", "Batch 004"),
    ("american_express_pandemic_rewards_deep_v7.json", "batch_005_american_express_pandemic_rewards.md", "Batch 005"),
    ("western_union_full_history_deep_v7.json", "batch_006_western_union_full_history.md", "Batch 006"),
    ("chesapeake_full_history_deep_v7.json", "batch_007_chesapeake_full_history.md", "Batch 007"),
    ("batch_008_ezpw_lov_nick_cost_deep_v7.json", "batch_008_ezpw_lov_nick_cost_30.md", "Batch 008"),
    ("batch_009_nflx_adt_atvi_baba_deep_v7.json", "batch_009_nflx_adt_atvi_baba_30.md", "Batch 009"),
    ("batch_010_transport_capital_structure_deep_v7.json", "batch_010_transport_capital_structure_30.md", "Batch 010"),
    ("batch_011_apple_google_deep_v7.json", "batch_011_apple_google_10.md", "Batch 011"),
    ("batch_012_alt_managers_deep_v7.json", "batch_012_alt_managers_10.md", "Batch 012"),
    ("batch_013_payments_deep_v7.json", "batch_013_payments_10.md", "Batch 013"),
    ("batch_014_tmus_atus_deep_v7.json", "batch_014_tmus_atus_10.md", "Batch 014"),
    ("batch_015_charter_comcast_deep_v7.json", "batch_015_charter_comcast_10.md", "Batch 015"),
    ("batch_016_cigna_unitedhealth_deep_v7.json", "batch_016_cigna_unitedhealth_10.md", "Batch 016"),
    ("batch_017_sprint_att_deep_v7.json", "batch_017_sprint_att_10.md", "Batch 017"),
    ("batch_018_genworth_assured_guaranty_deep_v7.json", "batch_018_genworth_assured_guaranty_10.md", "Batch 018"),
    ("batch_019_visteon_goodyear_deep_v7.json", "batch_019_visteon_goodyear_10.md", "Batch 019"),
    ("batch_020_fossil_abercrombie_deep_v7.json", "batch_020_fossil_abercrombie_10.md", "Batch 020"),
    ("batch_021_echostar_iridium_deep_v7.json", "batch_021_echostar_iridium_10.md", "Batch 021"),
    ("batch_022_geo_corecivic_deep_v7.json", "batch_022_geo_corecivic_10.md", "Batch 022"),
    ("batch_023_hp_western_digital_deep_v7.json", "batch_023_hp_western_digital_10.md", "Batch 023"),
    ("batch_024_amazon_iac_deep_v7.json", "batch_024_amazon_iac_10.md", "Batch 024"),
    ("batch_025_ibkr_discover_deep_v7.json", "batch_025_ibkr_discover_10.md", "Batch 025"),
    ("batch_026_seritage_gyrodyne_deep_v7.json", "batch_026_seritage_gyrodyne_10.md", "Batch 026"),
    ("all_reviewed_v8_index.json", "all_reviewed_v8.md.gz", "V8 전체 DB"),
)


@st.cache_data(show_spinner=False)
def _idea_catalog() -> dict[str, dict]:
    catalog: dict[str, dict] = {}
    for json_name, markdown_name, batch_name in BATCH_SOURCES:
        json_path = ROOT / "data" / "curated" / json_name
        markdown_path = ROOT / "analysis" / markdown_name
        if not json_path.exists() or not markdown_path.exists():
            continue
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        postmortems = payload.get("postmortems", [])
        for position, item in enumerate(postmortems):
            idea_id = item["idea_id"]
            # Specific reviewed Batch files are the source of truth.
            # The V8 consolidated report is only a fallback for ideas that do
            # not have a dedicated Batch file.  Do not let V8 overwrite the
            # Batch 001+ mapping, otherwise every popup opens all_reviewed_v8.
            if idea_id in catalog:
                continue
            catalog[idea_id] = {
                "batch_name": batch_name,
                "markdown_path": str(markdown_path),
                "position": position,
                "ticker": item.get("ticker", ""),
            }
    return catalog


def _heading_starts(text: str, pattern: str) -> list[re.Match]:
    return list(re.finditer(pattern, text, flags=re.MULTILINE))


def _extract_modern_company_report(text: str, date: str) -> str | None:
    """Return the Batch intro and the selected company's complete section."""
    idea_matches = _heading_starts(
        text, rf"^## \d+\. {re.escape(date)}(?:\s|—|-).*$"
    )
    if not idea_matches:
        return None
    selected = idea_matches[0]

    all_h1 = _heading_starts(text, r"^# (?!#).+$")
    company_heads = [
        head
        for head in all_h1
        if not re.match(r"^# (?:Batch |Part |배치 )", head.group(0))
    ]
    company_start = None
    company_end = None
    for head in company_heads:
        next_head = next(
            (candidate for candidate in all_h1 if candidate.start() > head.start()),
            None,
        )
        next_start = next_head.start() if next_head else len(text)
        if head.start() <= selected.start() < next_start:
            company_start = head.start()
            company_end = next_start
            break
    if company_start is None or company_end is None:
        return None

    batch_intro_end = company_heads[0].start() if company_heads else company_start
    batch_intro = text[:batch_intro_end].strip()
    company_report = text[company_start:company_end].strip()
    shared_match = re.search(r"^# 배치 공통.*$", text, re.MULTILINE)
    shared = text[shared_match.start():].strip() if shared_match else ""
    return "\n\n---\n\n".join(
        part for part in (batch_intro, company_report, shared) if part
    )


def _extract_legacy_report(text: str, position: int) -> str | None:
    """Batch 001-007 each cover one company, so return the complete file."""
    parts = _heading_starts(text, r"^# Part [A-Z]\..*$")
    if not parts or position >= len(parts):
        return None
    return text.strip()


def _extract_v8_company_report(text: str, idea_id: str) -> str | None:
    """Return the standardised V8 intro and every thesis for one company."""
    marker = re.search(rf"^<!-- idea:{re.escape(idea_id)} -->$", text, re.MULTILINE)
    if not marker:
        return None
    company_heads = _heading_starts(text, r"^# .+ — 기업과 투자 아이디어$")
    company_start = next(
        (head.start() for head in reversed(company_heads) if head.start() < marker.start()),
        None,
    )
    if company_start is None:
        return None
    company_end = next(
        (head.start() for head in company_heads if head.start() > marker.start()),
        len(text),
    )
    intro_end = company_heads[0].start() if company_heads else company_start
    intro = text[:intro_end].strip()
    company = text[company_start:company_end].strip()
    return "\n\n---\n\n".join(part for part in (intro, company) if part)


def _escape_dollar_math(markdown: str) -> str:
    """Prevent Streamlit from interpreting financial dollar values as LaTeX."""
    return re.sub(r"(?<!\\)\$", r"\\$", markdown)


@st.cache_data(show_spinner=False)
def batch_report_for_idea(idea_id: str, date: str) -> dict | None:
    item = _idea_catalog().get(idea_id)
    if not item:
        return None
    markdown_path = Path(item["markdown_path"])
    if markdown_path.suffix == ".gz":
        text = gzip.decompress(markdown_path.read_bytes()).decode("utf-8")
    else:
        text = markdown_path.read_text(encoding="utf-8")
    if item["batch_name"] == "V8 전체 DB":
        report = _extract_v8_company_report(text, idea_id)
    elif int(item["batch_name"].split()[-1]) >= 8:
        report = _extract_modern_company_report(text, date)
    else:
        report = _extract_legacy_report(text, item["position"])
    if not report:
        return None
    return {
        "batch_name": item["batch_name"],
        "markdown": _escape_dollar_math(report),
    }


def render_batch_source_report(idea: dict) -> bool:
    date = str(idea.get("date") or "")[:10]
    result = batch_report_for_idea(str(idea.get("idea_id") or ""), date)
    if not result:
        return False
    st.caption(
        f"{result['batch_name']} 원문 레이아웃입니다. 선택한 기업의 모든 투자논지를 생략 없이 표시합니다."
    )
    st.markdown(result["markdown"])
    return True


def render_batch_popup_button(idea: dict) -> bool:
    """Open the dedicated reviewed Batch markdown directly on GitHub."""
    idea_id = str(idea.get("idea_id") or "")
    item = _idea_catalog().get(idea_id)
    if not item:
        return False

    markdown_path = Path(item["markdown_path"])
    if item["batch_name"] == "V8 전체 DB":
        st.caption(
            "이 항목은 아직 전용 Batch 파일이 없어 V8 통합 보고서에만 포함되어 있습니다."
        )
        return False

    github_url = (
        "https://github.com/horea457/VIC-/blob/main/analysis/"
        + markdown_path.name
    )

    cols = st.columns([1, 3])
    with cols[0]:
        st.link_button(
            "📄 GitHub에서 Batch 원문 열기",
            github_url,
            use_container_width=True,
        )
    with cols[1]:
        st.caption(
            f"{item['batch_name']} · {markdown_path.name} · "
            "상세분석은 GitHub의 Batch markdown 원문을 기준으로 봅니다."
        )
    return True
