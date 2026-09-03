"""Render the reviewed Batch markdown as the source-of-truth report.

The SQLite overlay is useful for filtering and aggregation, but the reviewed
Batch markdown contains the fullest company and idea narrative.  This module
links each curated idea back to that markdown. A database row selects a company,
and every reviewed thesis for that company is shown without shortening it.
"""

from __future__ import annotations

import json
import re
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
            catalog[item["idea_id"]] = {
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


def _escape_dollar_math(markdown: str) -> str:
    """Prevent Streamlit from interpreting financial dollar values as LaTeX."""
    return re.sub(r"(?<!\\)\$", r"\\$", markdown)


@st.cache_data(show_spinner=False)
def batch_report_for_idea(idea_id: str, date: str) -> dict | None:
    item = _idea_catalog().get(idea_id)
    if not item:
        return None
    text = Path(item["markdown_path"]).read_text(encoding="utf-8")
    if int(item["batch_name"].split()[-1]) >= 8:
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
