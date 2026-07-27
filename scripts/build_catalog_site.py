#!/usr/bin/env python3
"""Build the static JSON payload consumed by the survey catalog page."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy"
OUTPUT = ROOT / "docs" / "data" / "catalog.json"


def read_csv(name: str) -> list[dict[str, str]]:
    with (TAXONOMY / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    payload = {
        "methods": read_csv("methods.csv"),
        "benchmarks": read_csv("benchmarks.csv"),
        "mappings": read_csv("pipeline_mapping.csv"),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for name in ("methods.csv", "benchmarks.csv", "pipeline_mapping.csv", "discovery_queries.csv"):
        shutil.copyfile(TAXONOMY / name, OUTPUT.parent / name)
    print(f"Built {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
