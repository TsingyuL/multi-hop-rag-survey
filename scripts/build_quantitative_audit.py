#!/usr/bin/env python3
"""Generate the frozen quantitative audit from machine-readable catalog data."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy"
OUTPUT = ROOT / "docs" / "quantitative_audit.md"

STAGE_ORDER = [
    ("observability", "Observability"),
    ("selection_preservation", "Selection preservation"),
    ("exposure", "Evidence exposure"),
    ("fusion", "Fusion reliability"),
    ("faithfulness", "Causal faithfulness"),
]
STRATUM_ORDER = [
    ("existing_seed", "Eligible records retained from the previous seed"),
    ("targeted_observability", "Targeted observability addition"),
    ("targeted_selection", "Targeted selection additions"),
    ("targeted_exposure", "Targeted exposure additions"),
    ("targeted_fusion", "Targeted fusion additions"),
    ("targeted_faithfulness", "Targeted faithfulness additions"),
    ("discretionary_recency", "Declared recency slot"),
    ("discretionary_process", "Declared process-supervision slot"),
]
EVIDENCE_ORDER = [
    ("ev_chain_recall", "Complete-chain or hop-wise recall"),
    ("ev_budget_match", "Matched passage/token/call/latency budget"),
    ("ev_membership", "Selected-set membership"),
    ("ev_ordering", "Fixed-membership ordering/position"),
    ("ev_stage_metric", "Primary-stage-aligned metric"),
    ("ev_fusion_ablation", "Conditional fusion ablation"),
    ("ev_deletion", "Evidence deletion"),
    ("ev_conflict", "Evidence conflict"),
    ("ev_counterfactual", "Counterfactual support"),
    ("ev_cost", "Retrieval-call/token/latency/FLOP cost"),
]


def read_csv(name: str) -> list[dict[str, str]]:
    with (TAXONOMY / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---:" if i else "---" for i in range(len(headers))) + " |",
    ]
    lines.extend("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows)
    return "\n".join(lines)


def main() -> int:
    methods = read_csv("methods.csv")
    benchmarks = read_csv("benchmarks.csv")
    mappings = read_csv("pipeline_mapping.csv")
    audit = read_csv("audit_records.csv")

    reviewed = [row for row in methods if row["status"] == "reviewed"]
    stages = Counter(row["primary_estimand"] for row in audit)
    strata = Counter(row["audit_stratum"] for row in audit)
    years = Counter(row["year"] for row in audit)
    families = Counter(row["architectural_family"] for row in audit)

    evidence_rows: list[list[object]] = []
    for field, label in EVIDENCE_ORDER:
        counts = Counter(row[field] for row in audit)
        evidence_rows.append([
            label,
            counts["yes"],
            counts["partial"],
            counts["unclear"],
            counts["not_reported"],
            counts["not_applicable"],
        ])

    content = f"""# Quantitative Reporting Audit

> **Legacy v1 artifact:** This generated 40-record audit is retained for
> provenance. The current manuscript uses the aggregate v2 snapshot in
> [`submission_audit_v2.md`](submission_audit_v2.md) and
> [`taxonomy/audit_v2/`](../taxonomy/audit_v2/).

This file is generated from `taxonomy/audit_records.csv` by
`python3 scripts/build_quantitative_audit.py`. Do not edit its counts by hand.

The repository separates broad catalog coverage from the frozen comparative
audit. A `reviewed` catalog record has verified metadata and a checked central
taxonomy label. Audit inclusion additionally requires the eligibility and
24-field coding rules in `taxonomy/audit_codebook_v1.md`.

## Frozen denominators

{table(
    ["Quantity", "Count"],
    [
        ["Method records in the broad catalog", len(methods)],
        ["Source-reviewed method records in the broad catalog", len(reviewed)],
        ["Audit-eligible and completed method records", len(audit)],
        ["Reviewed benchmark records", sum(row["status"] == "reviewed" for row in benchmarks)],
        ["Unique intervention mappings", len(mappings)],
    ],
)}

The 40-record audit is not a field-prevalence sample. It is a deliberately
stratified diagnostic sample. The original source-reviewed seed contributed 13
eligible records; 25 targeted records filled stage gaps; and two declared
discretionary records improve recency and process-supervision coverage.

## Audit construction

{table(
    ["Stratum", "Count"],
    [[label, strata[key]] for key, label in STRATUM_ORDER],
)}

## Primary target distribution

`joint` is not permitted as a primary target. Joint systems are assigned to
their earliest active intervention stage and retain `joint` only as a secondary
label.

{table(
    ["Primary target", "Count over audited methods"],
    [[label, stages[key]] for key, label in STAGE_ORDER],
)}

## Verified evidence coverage

Only `yes` is counted as directly verified positive evidence. `partial` is
reported separately. `unclear` is not a negative judgment, and
`not_reported` is permitted only after full-text checking.

{table(
    ["Audit item", "Yes", "Partial", "Unclear", "Not reported", "N/A"],
    evidence_rows,
)}

## Year and architectural-family balance

{table(
    ["Year", "Count"],
    [[year, years[year]] for year in sorted(years)],
)}

{table(
    ["Architectural family", "Count"],
    [[family, count] for family, count in sorted(families.items(), key=lambda item: (-item[1], item[0]))],
)}

## Interpretation boundary

The expanded audit closes the previous denominator problem: taxonomy-level
comparisons now rest on 40 eligible records rather than all 20 records in a
small mixed seed. It does not justify a comprehensive or PRISMA-style coverage
claim.

The audit also exposes a substantive evaluation gap. Stage-aligned metrics and
cost reporting are common, but clean fixed-membership ordering tests remain
rare. No audited record supplies a directly verified evidence-deletion test
under the codebook rule; only one supplies a directly verified conflict test
and one a directly verified counterfactual-support test. Those zeros and ones
describe verified evidence in this stratified audit, not the entire field.

## Reliability boundary

The frozen v1.0 records are single-coded. Independent blind recoding,
disagreement adjudication, and an inter-coder agreement coefficient are not
part of this snapshot. Automated validation establishes structural consistency
and reproducible counts, not semantic correctness. Row-level adjudication notes
and canonical source URLs are exposed so that coding decisions can be checked
and corrected.
"""

    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {len(audit)} audited records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
