"""Validate canonical VIC Batch wrappers and production overlay payloads."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "data" / "curated"
ANALYSIS = ROOT / "analysis"
REQUIRED_ARRAYS = {
    "postmortems",
    "meta",
    "sections",
    "claims",
    "metrics",
    "timeline",
    "sources",
}


def validate_payloads(errors: list[str]) -> tuple[int, int]:
    owners: dict[str, list[str]] = defaultdict(list)
    payload_count = 0
    row_count = 0

    for path in sorted(CURATED.glob("*_deep_v7.json")):
        payload_count += 1
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: JSON parse failure: {exc}")
            continue

        missing = sorted(REQUIRED_ARRAYS - payload.keys())
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing arrays {missing}")
            continue
        non_arrays = sorted(key for key in REQUIRED_ARRAYS if not isinstance(payload[key], list))
        if non_arrays:
            errors.append(f"{path.relative_to(ROOT)}: non-array fields {non_arrays}")
            continue

        postmortem_ids = [row.get("idea_id") for row in payload["postmortems"]]
        if None in postmortem_ids or len(postmortem_ids) != len(set(postmortem_ids)):
            errors.append(f"{path.relative_to(ROOT)}: missing or duplicate postmortem idea_id")
        canonical_ids = {str(idea_id) for idea_id in postmortem_ids}
        for key in ("meta", "sections", "claims", "metrics", "timeline", "sources"):
            detail_ids = [str(row.get("idea_id")) for row in payload[key]]
            missing_ids = sorted(canonical_ids - set(detail_ids))
            extra_ids = sorted(set(detail_ids) - canonical_ids)
            if missing_ids or extra_ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: {key} ID coverage "
                    f"missing={missing_ids}, extra={extra_ids}"
                )
        meta_ids = [str(row.get("idea_id")) for row in payload["meta"]]
        if len(meta_ids) != len(canonical_ids) or len(meta_ids) != len(set(meta_ids)):
            errors.append(
                f"{path.relative_to(ROOT)}: meta must contain exactly one row per idea"
            )

        if "ideas_master" in payload:
            if not isinstance(payload["ideas_master"], list):
                errors.append(f"{path.relative_to(ROOT)}: ideas_master is not an array")
            else:
                idea_master_ids = {row.get("idea_id") for row in payload["ideas_master"]}
                absent = sorted(set(postmortem_ids) - idea_master_ids)
                if absent:
                    errors.append(f"{path.relative_to(ROOT)}: ideas_master missing {absent}")

        weights: dict[str, int] = defaultdict(int)
        for row in payload["claims"]:
            weights[str(row.get("idea_id"))] += int(row.get("thesis_weight_pct") or 0)
        bad_weights = {
            idea_id: weights.get(idea_id, 0)
            for idea_id in canonical_ids
            if weights.get(idea_id, 0) != 100
        }
        if bad_weights:
            errors.append(f"{path.relative_to(ROOT)}: claim weights {bad_weights}")

        for idea_id in postmortem_ids:
            owners[str(idea_id)].append(path.name)
            row_count += 1

    duplicates = {idea_id: paths for idea_id, paths in owners.items() if len(paths) > 1}
    if duplicates:
        errors.append(f"cross-payload duplicate idea_id: {duplicates}")
    return payload_count, row_count


def validate_wrappers(errors: list[str]) -> int:
    source = (ROOT / "app" / "components" / "batch_report.py").read_text(encoding="utf-8")
    entries = re.findall(r'\("([^"]+\.json)","([^"]+\.md)","([^"]+)"\)', source)
    checked = 0

    for json_name, markdown_name, label in entries:
        json_path = CURATED / json_name
        markdown_path = ANALYSIS / markdown_name
        if not json_path.exists():
            errors.append(f"{label}: missing payload {json_path.relative_to(ROOT)}")
            continue
        if not markdown_path.exists():
            errors.append(f"{label}: missing report {markdown_path.relative_to(ROOT)}")
            continue
        checked += 1

        if markdown_name.endswith(".gz"):
            continue
        text = markdown_path.read_text(encoding="utf-8")
        match = re.search(r"<!--\s*batch_parts:\s*(.+?)\s*-->", text, re.DOTALL)
        if not match:
            continue
        for part in (value.strip() for value in match.group(1).split("|")):
            if part and not (ANALYSIS / part).exists():
                errors.append(f"{label}: missing canonical part analysis/{part}")
    return checked


def validate_cleanliness(errors: list[str]) -> None:
    obsolete = [
        *ANALYSIS.glob("batch_*_v2_deep.md"),
        *ANALYSIS.glob("batch_*_part??.md"),
        *ANALYSIS.glob("batch_*_idea??.md"),
        *(ROOT / ".github").glob("batch042_*"),
        *(ROOT / ".github" / "workflows").glob("build_batch_04*.yml"),
    ]
    if obsolete:
        errors.append(
            "obsolete artifacts remain: "
            + ", ".join(str(path.relative_to(ROOT)) for path in sorted(obsolete))
        )


def main() -> int:
    errors: list[str] = []
    payloads, rows = validate_payloads(errors)
    wrappers = validate_wrappers(errors)
    validate_cleanliness(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        f"OK: {payloads} production payloads, {rows} unique ideas, "
        f"{wrappers} report sources, no duplicate idea_id"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
