"""Render the reviewed Batch markdown as the source-of-truth report.

The SQLite overlay is useful for filtering and aggregation, but the reviewed
Batch markdown contains the fullest company and idea narrative.  This module
links each curated idea back to that markdown and extracts the company context,
the selected idea, and the shared evidence section.
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


def _source_section(text: str, start: int = 0, end: int | None = None) -> str:
    """Return the final shared/company evidence section when one exists."""
    window_end = len(text) if end is None else end
    matches = list(
        re.finditer(r"^## (?:\d+\. )?주요 근거.*$", text[start:window_end], re.MULTILINE)
    )
    if not matches:
        return ""
    source_start = start + matches[-1].start()
    return text[source_start:window_end].strip()


def _extract_modern_company_report(text: str, date: str) -> str | None:
    """Extract reports from Batch 008-010, which use date-labelled idea H2s."""
    idea_matches = _heading_starts(
        text, rf"^## \d+\. {re.escape(date)}(?:\s|—|-).*$"
    )
    if not idea_matches:
        return None
    selected = idea_matches[0]

    company_heads = _heading_starts(text, r"^# (?!Batch |Part ).+$")
    company_start = 0
    company_end = len(text)
    for idx, head in enumerate(company_heads):
        next_start = company_heads[idx + 1].start() if idx + 1 < len(company_heads) else len(text)
        if head.start() <= selected.start() < next_start:
            company_start = head.start()
            company_end = next_start
            break

    company_ideas = [
        match
        for match in _heading_starts(text, r"^## \d+\. \d{4}-\d{2}-\d{2}(?:\s|—|-).*$")
        if company_start < match.start() < company_end
    ]
    if not company_ideas:
        return None

    intro = text[company_start:company_ideas[0].start()].strip()
    selected_index = next(
        (idx for idx, match in enumerate(company_ideas) if match.start() == selected.start()),
        None,
    )
    if selected_index is None:
        return None

    next_idea_start = (
        company_ideas[selected_index + 1].start()
        if selected_index + 1 < len(company_ideas)
        else company_end
    )
    footer_match = re.search(
        r"^## 2024-01-31 기준 기업 결론.*$",
        text[selected.start():company_end],
        re.MULTILINE,
    )
    footer_start = selected.start() + footer_match.start() if footer_match else company_end
    idea_end = min(next_idea_start, footer_start)
    idea = text[selected.start():idea_end].strip()

    footer = ""
    if footer_match:
        footer = text[footer_start:company_end].strip()
    else:
        footer = _source_section(text, company_start, company_end)

    return "\n\n---\n\n".join(part for part in (intro, idea, footer) if part)


def _extract_legacy_report(text: str, position: int) -> str | None:
    """Extract reports from Batch 001-007, which use Part A/B/C headings."""
    parts = _heading_starts(text, r"^# Part [A-Z]\..*$")
    if not parts or position >= len(parts):
        return None

    intro_candidates = _heading_starts(text, r"^## 1\. .+$")
    intro_start = intro_candidates[0].start() if intro_candidates else 0
    intro = text[intro_start:parts[0].start()].strip()

    part_start = parts[position].start()
    part_end = parts[position + 1].start() if position + 1 < len(parts) else len(text)
    selected_part = text[part_start:part_end].strip()

    sources = _source_section(text, parts[-1].start())
    if sources and sources not in selected_part:
        selected_part = f"{selected_part}\n\n---\n\n{sources}"

    return "\n\n---\n\n".join(part for part in (intro, selected_part) if part)


def _escape_dollar_math(markdown: str) -> str:
    """Prevent Streamlit from interpreting financial dollar values as LaTeX."""
    return re.sub(r"(?<!\\)\$", r"\\$", markdown)


@st.cache_data(show_spinner=False)
def batch_report_for_idea(idea_id: str, date: str) -> dict | None:
    item = _idea_catalog().get(idea_id)
    if not item:
        return None
    text = Path(item["markdown_path"]).read_text(encoding="utf-8")
    if item["batch_name"] in {"Batch 008", "Batch 009", "Batch 010"}:
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
        f"{result['batch_name']} 심층분석 원문에서 선택한 기업과 아이디어를 그대로 표시합니다."
    )
    st.markdown(result["markdown"])
    return True
