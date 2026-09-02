"""Apply reviewed deep-research payloads to the dashboard database.

The repository keeps the large base SQLite database split into compressed parts.
Small, human-reviewable research batches live as JSON overlays so they can be
audited and deployed without replacing the whole binary database on every batch.
"""

from __future__ import annotations

import json
import sqlite3
from collections import defaultdict
from pathlib import Path


DETAIL_TABLES = {
    "sections": "deep_analysis_sections",
    "claims": "deep_analysis_claims",
    "metrics": "deep_analysis_metrics",
    "timeline": "deep_analysis_timeline",
    "sources": "deep_analysis_sources",
}


def _insert_rows(conn: sqlite3.Connection, table: str, rows: list[dict]) -> None:
    if not rows:
        return
    columns = list(rows[0])
    expected = set(columns)
    if any(set(row) != expected for row in rows):
        raise ValueError(f"{table}: every row must have the same columns")
    known = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
    unknown = expected - known
    if unknown:
        raise ValueError(f"{table}: unknown columns: {sorted(unknown)}")
    placeholders = ",".join("?" for _ in columns)
    names = ",".join(columns)
    sql = f"INSERT OR REPLACE INTO {table} ({names}) VALUES ({placeholders})"
    conn.executemany(sql, ([row[c] for c in columns] for row in rows))


def _validate_payload(conn: sqlite3.Connection, payload: dict) -> list[str]:
    required = {"postmortems", "meta", *DETAIL_TABLES}
    missing = required - set(payload)
    if missing:
        raise ValueError(f"payload keys missing: {sorted(missing)}")

    idea_ids = [row["idea_id"] for row in payload["postmortems"]]
    if len(idea_ids) != len(set(idea_ids)):
        raise ValueError("duplicate idea_id in postmortems")
    found = {
        row[0]
        for row in conn.execute(
            f"SELECT idea_id FROM ideas_master WHERE idea_id IN ({','.join('?' for _ in idea_ids)})",
            idea_ids,
        )
    }
    absent = set(idea_ids) - found
    if absent:
        raise ValueError(f"ideas not found in ideas_master: {sorted(absent)}")

    weights: dict[str, int] = defaultdict(int)
    for claim in payload["claims"]:
        weights[claim["idea_id"]] += int(claim["thesis_weight_pct"])
    bad = {idea_id: total for idea_id, total in weights.items() if total != 100}
    if bad:
        raise ValueError(f"claim weights must sum to 100: {bad}")
    return idea_ids


def _analysis_values(postmortem: dict, claims: list[dict], sections: list[dict]) -> dict:
    claims = sorted(claims, key=lambda row: row["claim_order"])
    sections = sorted(sections, key=lambda row: row["section_order"])
    thesis_points = "\n".join(
        f"{row['claim_order']}. {row['claim_title_ko']}: {row['original_claim_ko']}"
        for row in claims
    )
    assumptions = "\n".join(
        f"{row['claim_order']}. {row['key_assumption_ko']}" for row in claims
    )
    falsifiers = "\n".join(
        f"{row['claim_order']}. {row['ex_ante_falsifier_ko']}" for row in claims
    )
    business_model = sections[0]["section_body_ko"] if sections else postmortem["company_description_ko"]
    return {
        "company_description_ko": postmortem["company_description_ko"],
        "business_model_ko": business_model,
        "thesis_summary_ko": postmortem["original_thesis_ko"],
        "thesis_points_ko": thesis_points,
        "key_assumptions_ko": assumptions,
        "falsifiers_ko": falsifiers,
        "catalyst_outcome_ko": postmortem["catalyst_verdict_ko"],
        "actual_development_ko": postmortem["actual_development_ko"],
        "outcome_thesis_ko": postmortem["thesis_verdict_ko"],
        "outcome_business_ko": postmortem["business_verdict_ko"],
        "outcome_valuation_ko": postmortem["valuation_verdict_ko"],
        "outcome_stock_ko": postmortem["stock_verdict_ko"],
        "outcome_current_ko": postmortem["current_verdict_ko"],
        "overall_verdict_ko": postmortem["overall_verdict_ko"],
        "failure_domain_ko": postmortem["failure_pattern_ko"],
        "failure_mechanism_ko": postmortem["why_ko"],
        "secondary_failure_patterns_ko": postmortem["success_pattern_ko"],
        "root_analytical_error_ko": postmortem["root_error_ko"],
        "transmission_mechanism_ko": postmortem["why_ko"],
        "first_contradictory_signal_ko": postmortem["first_signal_ko"],
        "first_signal_date": postmortem["first_signal_date"],
        "knowable_at_t0_ko": postmortem["knowable_at_t0_ko"],
        "avoidability_ko": postmortem["avoidability_ko"],
        "counterfactual_question_ko": postmortem["counterfactual_question_ko"],
        "research_priority": 5,
        "confidence": postmortem["confidence"],
        "analysis_status_ko": postmortem["research_status_ko"],
        "last_updated": postmortem["research_asof"],
    }


def apply_deep_payload(db_path: Path | str, payload_path: Path | str) -> dict[str, int]:
    """Validate and idempotently apply one reviewed JSON research batch."""
    db_path, payload_path = Path(db_path), Path(payload_path)
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    with sqlite3.connect(db_path) as conn:
        idea_ids = _validate_payload(conn, payload)
        marks = ",".join("?" for _ in idea_ids)

        _insert_rows(conn, "postmortems", payload["postmortems"])
        _insert_rows(conn, "deep_analysis_meta", payload["meta"])
        for payload_key, table in DETAIL_TABLES.items():
            conn.execute(f"DELETE FROM {table} WHERE idea_id IN ({marks})", idea_ids)
            _insert_rows(conn, table, payload[payload_key])

        claims_by_id: dict[str, list[dict]] = defaultdict(list)
        sections_by_id: dict[str, list[dict]] = defaultdict(list)
        for row in payload["claims"]:
            claims_by_id[row["idea_id"]].append(row)
        for row in payload["sections"]:
            sections_by_id[row["idea_id"]].append(row)
        for postmortem in payload["postmortems"]:
            idea_id = postmortem["idea_id"]
            values = _analysis_values(
                postmortem, claims_by_id[idea_id], sections_by_id[idea_id]
            )
            assignments = ",".join(f"{name}=?" for name in values)
            conn.execute(
                f"UPDATE analysis SET {assignments} WHERE idea_id=?",
                [*values.values(), idea_id],
            )

        integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise sqlite3.DatabaseError(f"integrity_check failed: {integrity}")

    return {
        "ideas": len(idea_ids),
        "claims": len(payload["claims"]),
        "sections": len(payload["sections"]),
        "metrics": len(payload["metrics"]),
        "timeline": len(payload["timeline"]),
        "sources": len(payload["sources"]),
    }
