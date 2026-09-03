#!/usr/bin/env python3
"""Remove every non-reviewed row from the production dashboard database.

The deep-analysis tables are the source of truth. ideas_master retains only the
source metadata needed to display those reviewed ideas. Legacy/automatic tables
keep their schema for compatibility but contain no rows.
"""
from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "processed" / "vic_dashboard.db"
CURATED_TABLES = {
    "ideas_master", "postmortems", "deep_analysis_meta",
    "deep_analysis_claims", "deep_analysis_sections", "deep_analysis_metrics",
    "deep_analysis_timeline", "deep_analysis_sources",
}

def quote(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    with sqlite3.connect(args.db) as conn:
        conn.execute("PRAGMA foreign_keys=OFF")
        reviewed = {r[0] for r in conn.execute("SELECT idea_id FROM deep_analysis_meta")}
        if not reviewed:
            raise SystemExit("refusing to prune: deep_analysis_meta is empty")
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
        with conn:
            conn.execute("CREATE TEMP TABLE keep_idea_ids (idea_id TEXT PRIMARY KEY)")
            conn.executemany("INSERT INTO keep_idea_ids VALUES (?)", ((x,) for x in reviewed))
            for table in tables:
                columns = {r[1] for r in conn.execute(f"PRAGMA table_info({quote(table)})")}
                if table in CURATED_TABLES and "idea_id" in columns:
                    conn.execute(f"DELETE FROM {quote(table)} WHERE idea_id NOT IN (SELECT idea_id FROM keep_idea_ids)")
                elif table not in CURATED_TABLES:
                    conn.execute(f"DELETE FROM {quote(table)}")
        conn.execute("VACUUM")
        integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        counts = {t: conn.execute(f"SELECT COUNT(*) FROM {quote(t)}").fetchone()[0]
                  for t in sorted(CURATED_TABLES)}
        if integrity != "ok" or counts["deep_analysis_meta"] != len(reviewed):
            raise SystemExit(f"curated DB validation failed: {integrity}, {counts}")
        print({"reviewed_ideas": len(reviewed), "integrity": integrity, **counts})

if __name__ == "__main__":
    main()
