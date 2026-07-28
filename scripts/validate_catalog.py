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
ALLOWED_ESTIMANDS = {"observability", "selection_preservation", "exposure", "fusion", "faithfulness", "joint"}
ALLOWED_FAMILIES = {
    "retrieval", "graph_kg", "decomposition", "fusion_reader", "llm_reasoning",
    "agentic", "hybrid", "benchmark", "analysis",
}
ALLOWED_SOURCES = {"text", "knowledge_graph", "table", "multimodal", "hybrid"}
ALLOWED_STAGES = {"retrieve", "select", "order", "read_fuse", "verify", "end_to_end"}
ALLOWED_STATUS = {"seeded", "reviewed", "needs_review"}
ALLOWED_AUDIT_STRATA = {
    "existing_seed", "targeted_observability", "targeted_selection",
    "targeted_exposure", "targeted_fusion", "targeted_faithfulness",
    "discretionary_recency", "discretionary_process",
}
ALLOWED_CLAIM_CODES = {"primary", "secondary", "not_coded", "unclear"}
ALLOWED_EVIDENCE_CODES = {"yes", "partial", "unclear", "not_reported", "not_applicable"}
AUDIT_CLAIM_FIELDS = {
    "claim_observability": "observability",
    "claim_selection": "selection_preservation",
    "claim_exposure": "exposure",
    "claim_fusion": "fusion",
    "claim_faithfulness": "faithfulness",
}
AUDIT_EVIDENCE_FIELDS = {
    "ev_chain_recall", "ev_budget_match", "ev_membership", "ev_ordering",
    "ev_stage_metric", "ev_fusion_ablation", "ev_deletion", "ev_conflict",
    "ev_counterfactual", "ev_cost",
}
EXPECTED_AUDIT_DISTRIBUTION = {
    "observability": 12,
    "selection_preservation": 8,
    "exposure": 5,
    "fusion": 8,
    "faithfulness": 7,
}


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
    audit = read_csv(
        "audit_records.csv",
        {"citation_key", "title", "year", "architectural_family", "primary_estimand",
         "secondary_estimands", "source_url", "audit_stratum", *AUDIT_CLAIM_FIELDS,
         *AUDIT_EVIDENCE_FIELDS, "adjudication_note"},
    )
    all_rows = [("methods.csv", row) for row in methods] + [("benchmarks.csv", row) for row in benchmarks]
    keys = [row["citation_key"] for _, row in all_rows]
    if len(keys) != len(set(keys)):
        raise ValueError("citation_key values must be unique across methods.csv and benchmarks.csv")

    for filename, rows in (("methods.csv", methods), ("benchmarks.csv", benchmarks), ("pipeline_mapping.csv", mappings)):
        for number, row in enumerate(rows, start=2):
            require_choice(filename, number, "primary_estimand", row["primary_estimand"], ALLOWED_ESTIMANDS)
            if filename != "benchmarks.csv" and row["primary_estimand"] == "joint":
                raise ValueError(
                    f"{filename}: row {number} uses joint as a primary estimand; "
                    "code the earliest active stage and keep joint secondary"
                )
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

    mapping_identity = [
        (row["citation_key"], row["pipeline_stage"], row["primary_estimand"], row["intervention"])
        for row in mappings
    ]
    if len(mapping_identity) != len(set(mapping_identity)):
        raise ValueError("pipeline_mapping.csv contains duplicate intervention mappings")

    method_by_key = {row["citation_key"]: row for row in methods}
    for number, row in enumerate(mappings, start=2):
        method = method_by_key[row["citation_key"]]
        if row["status"] != method["status"]:
            raise ValueError(
                f"pipeline_mapping.csv: row {number} status {row['status']} "
                f"does not match methods.csv status {method['status']}"
            )

    audit_keys = [row["citation_key"] for row in audit]
    if len(audit_keys) != len(set(audit_keys)):
        raise ValueError("audit_records.csv citation_key values must be unique")
    if len(audit) != 40:
        raise ValueError(f"audit_records.csv must contain the frozen 40 records, found {len(audit)}")

    audit_distribution: dict[str, int] = {}
    for number, row in enumerate(audit, start=2):
        key = row["citation_key"]
        if key not in method_by_key:
            raise ValueError(f"audit_records.csv: row {number} has unknown method key {key}")
        method = method_by_key[key]
        if method["status"] != "reviewed":
            raise ValueError(f"audit_records.csv: row {number} is not reviewed in methods.csv")
        for field in ("title", "year", "architectural_family", "primary_estimand", "source_url"):
            if row[field] != method[field]:
                raise ValueError(
                    f"audit_records.csv: row {number} field {field} does not match methods.csv"
                )
        require_choice(
            "audit_records.csv", number, "audit_stratum", row["audit_stratum"], ALLOWED_AUDIT_STRATA
        )
        for field in AUDIT_CLAIM_FIELDS:
            require_choice("audit_records.csv", number, field, row[field], ALLOWED_CLAIM_CODES)
        for field in AUDIT_EVIDENCE_FIELDS:
            require_choice("audit_records.csv", number, field, row[field], ALLOWED_EVIDENCE_CODES)
        primary_claim_field = next(
            field for field, estimand in AUDIT_CLAIM_FIELDS.items()
            if estimand == row["primary_estimand"]
        )
        if row[primary_claim_field] != "primary":
            raise ValueError(
                f"audit_records.csv: row {number} must mark {primary_claim_field}=primary"
            )
        if sum(row[field] == "primary" for field in AUDIT_CLAIM_FIELDS) != 1:
            raise ValueError(f"audit_records.csv: row {number} must have exactly one primary claim")
        audit_distribution[row["primary_estimand"]] = (
            audit_distribution.get(row["primary_estimand"], 0) + 1
        )
        if not row["adjudication_note"].strip():
            raise ValueError(f"audit_records.csv: row {number} has a blank adjudication note")

    if audit_distribution != EXPECTED_AUDIT_DISTRIBUTION:
        raise ValueError(
            "audit_records.csv primary distribution changed: "
            f"{audit_distribution} != {EXPECTED_AUDIT_DISTRIBUTION}"
        )

    print(
        f"Catalog valid: {len(methods)} methods, {len(benchmarks)} benchmarks, "
        f"{len(mappings)} unique mappings, {len(audit)} audited methods."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Catalog validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
