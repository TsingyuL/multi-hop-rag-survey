#!/usr/bin/env python3
"""Validate the public survey catalog without third-party dependencies."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy"
ALLOWED_ESTIMANDS = {"observability", "utility", "exposure", "fusion", "faithfulness", "joint"}
ALLOWED_FAMILIES = {
    "retrieval", "graph_kg", "decomposition", "fusion_reader", "llm_reasoning",
    "agentic", "hybrid", "benchmark", "analysis",
}
ALLOWED_SOURCES = {"text", "knowledge_graph", "table", "multimodal", "hybrid"}
ALLOWED_STAGES = {"retrieve", "select", "order", "read_fuse", "verify", "end_to_end"}
ALLOWED_STATUS = {"seeded", "reviewed", "needs_review"}
ALLOWED_LIBRARY_STATES = {"imported", "needs_triage"}


def values(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def read_csv(name: str, required: set[str]) -> list[dict[str, str]]:
    path = TAXONOMY / name
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = set(reader.fieldnames or [])
        missing = required - actual
        if missing:
            raise ValueError(f"{name}: missing headers {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{name}: must contain at least one row")
    return rows


def require_subset(filename: str, row_number: int, field: str, value: str, allowed: set[str]) -> None:
    invalid = values(value) - allowed
    if invalid:
        raise ValueError(f"{filename}: row {row_number} has invalid {field}: {sorted(invalid)}")


def require_choice(filename: str, row_number: int, field: str, value: str, allowed: set[str]) -> None:
    if value not in allowed:
        raise ValueError(f"{filename}: row {row_number} has invalid {field}: {value}")


def require_url(filename: str, row_number: int, field: str, value: str, optional: bool = False) -> None:
    if optional and not value:
        return
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"{filename}: row {row_number} has invalid {field}: {value}")


def main() -> int:
    methods = read_csv(
        "methods.csv",
        {"citation_key", "title", "year", "architectural_family", "primary_estimand",
         "secondary_estimands", "evidence_source", "pipeline_stage", "source_url", "status", "notes",
         "venue", "tasks", "datasets", "code_url"},
    )
    benchmarks = read_csv(
        "benchmarks.csv",
        {"citation_key", "name", "year", "evidence_source", "primary_estimand", "diagnostics",
         "source_url", "status", "caveat", "venue", "task_type", "hops", "data_url"},
    )
    mappings = read_csv(
        "pipeline_mapping.csv",
        {"citation_key", "pipeline_stage", "primary_estimand", "intervention",
         "observable_diagnostic", "common_confounder", "status"},
    )
    library = read_csv(
        "library_papers.csv",
        {"library_id", "title", "authors", "year", "venue", "arxiv_id", "source_url",
         "library_categories", "source_origin", "priority", "notes", "review_state"},
    )
    all_rows = [("methods.csv", row) for row in methods] + [("benchmarks.csv", row) for row in benchmarks]
    keys = [row["citation_key"] for _, row in all_rows]
    if len(keys) != len(set(keys)):
        raise ValueError("citation_key values must be unique across methods.csv and benchmarks.csv")

    for filename, rows in (("methods.csv", methods), ("benchmarks.csv", benchmarks), ("pipeline_mapping.csv", mappings)):
        for number, row in enumerate(rows, start=2):
            require_choice(filename, number, "primary_estimand", row["primary_estimand"], ALLOWED_ESTIMANDS)
            if row["status"] not in ALLOWED_STATUS:
                raise ValueError(f"{filename}: row {number} has invalid status: {row['status']}")
            if not row["citation_key"] or not re.fullmatch(r"[a-z0-9]+", row["citation_key"]):
                raise ValueError(f"{filename}: row {number} has invalid citation_key")
            if filename != "pipeline_mapping.csv":
                if not re.fullmatch(r"\d{4}", row["year"]):
                    raise ValueError(f"{filename}: row {number} has invalid year: {row['year']}")
                require_url(filename, number, "source_url", row["source_url"])

    for filename, rows in (("methods.csv", methods), ("pipeline_mapping.csv", mappings)):
        for number, row in enumerate(rows, start=2):
            require_choice(filename, number, "pipeline_stage", row["pipeline_stage"], ALLOWED_STAGES)

    for number, row in enumerate(methods, start=2):
        require_subset("methods.csv", number, "secondary_estimands", row["secondary_estimands"], ALLOWED_ESTIMANDS)
        if row["architectural_family"] not in ALLOWED_FAMILIES:
            raise ValueError(f"methods.csv: row {number} has invalid architectural_family")
        if row["evidence_source"] not in ALLOWED_SOURCES:
            raise ValueError(f"methods.csv: row {number} has invalid evidence_source")
        for field in ("venue", "tasks", "datasets"):
            if not row[field].strip():
                raise ValueError(f"methods.csv: row {number} has blank {field}")
        require_url("methods.csv", number, "code_url", row["code_url"], optional=True)

    for number, row in enumerate(benchmarks, start=2):
        if row["evidence_source"] not in ALLOWED_SOURCES:
            raise ValueError(f"benchmarks.csv: row {number} has invalid evidence_source")
        for field in ("venue", "task_type", "hops", "data_url"):
            if not row[field].strip():
                raise ValueError(f"benchmarks.csv: row {number} has blank {field}")
        require_url("benchmarks.csv", number, "data_url", row["data_url"])

    library_ids = [row["library_id"] for row in library]
    if len(library_ids) != len(set(library_ids)):
        raise ValueError("library_papers.csv has duplicate library_id values")
    for number, row in enumerate(library, start=2):
        if not re.fullmatch(r"lib_[a-f0-9]{12}", row["library_id"]):
            raise ValueError(f"library_papers.csv: row {number} has invalid library_id")
        if not row["title"].strip() or not row["library_categories"].strip():
            raise ValueError(f"library_papers.csv: row {number} has blank title or library_categories")
        if row["year"] and not re.fullmatch(r"\d{4}", row["year"]):
            raise ValueError(f"library_papers.csv: row {number} has invalid year: {row['year']}")
        require_choice("library_papers.csv", number, "review_state", row["review_state"], ALLOWED_LIBRARY_STATES)
        require_url("library_papers.csv", number, "source_url", row["source_url"], optional=True)

    bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", (TAXONOMY / "reading_list.bib").read_text(encoding="utf-8")))
    missing_bib = set(keys) - bib_keys
    if missing_bib:
        raise ValueError(f"reading_list.bib is missing citation keys: {sorted(missing_bib)}")
    missing_catalog = {row["citation_key"] for row in mappings} - set(keys)
    if missing_catalog:
        raise ValueError(f"pipeline_mapping.csv has unknown citation keys: {sorted(missing_catalog)}")

    unmapped_methods = {row["citation_key"] for row in methods} - {row["citation_key"] for row in mappings}
    if unmapped_methods:
        raise ValueError(f"pipeline_mapping.csv is missing method keys: {sorted(unmapped_methods)}")

    print(f"Catalog valid: {len(methods)} methods, {len(benchmarks)} benchmarks, {len(mappings)} mappings, {len(library)} imported library records.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Catalog validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
