#!/usr/bin/env python3
"""Load all reviewed V7 deep-research JSON overlays into SQLite."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

from components.curated_overlay import apply_deep_payload  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db",
        type=Path,
        default=ROOT / "data" / "processed" / "vic_dashboard.db",
    )
    parser.add_argument(
        "--payload-glob",
        default="*_deep_v7.json",
        help="filename pattern under data/curated",
    )
    args = parser.parse_args()

    payloads = sorted((ROOT / "data" / "curated").glob(args.payload_glob))
    if not payloads:
        raise SystemExit(f"no payload matched: {args.payload_glob}")
    for payload in payloads:
        counts = apply_deep_payload(args.db, payload)
        print(f"loaded {payload.name}: {counts}")


if __name__ == "__main__":
    main()
