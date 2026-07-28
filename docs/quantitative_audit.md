# Quantitative Reporting Audit

This file is generated from `taxonomy/audit_records.csv` by
`python3 scripts/build_quantitative_audit.py`. Do not edit its counts by hand.

The repository separates broad catalog coverage from the frozen comparative
audit. A `reviewed` catalog record has verified metadata and a checked central
taxonomy label. Audit inclusion additionally requires the eligibility and
24-field coding rules in `taxonomy/audit_codebook_v1.md`.

## Frozen denominators

| Quantity | Count |
| --- | ---: |
| Method records in the broad catalog | 50 |
| Source-reviewed method records in the broad catalog | 47 |
| Audit-eligible and completed method records | 40 |
| Reviewed benchmark records | 6 |
| Unique intervention mappings | 51 |

The 40-record audit is not a field-prevalence sample. It is a deliberately
stratified diagnostic sample. The original source-reviewed seed contributed 13
eligible records; 25 targeted records filled stage gaps; and two declared
discretionary records improve recency and process-supervision coverage.

## Audit construction

| Stratum | Count |
| --- | ---: |
| Eligible records retained from the previous seed | 13 |
| Targeted observability addition | 1 |
| Targeted selection additions | 8 |
| Targeted exposure additions | 5 |
| Targeted fusion additions | 4 |
| Targeted faithfulness additions | 7 |
| Declared recency slot | 1 |
| Declared process-supervision slot | 1 |

## Primary target distribution

`joint` is not permitted as a primary target. Joint systems are assigned to
their earliest active intervention stage and retain `joint` only as a secondary
label.

| Primary target | Count over audited methods |
| --- | ---: |
| Observability | 12 |
| Selection preservation | 8 |
| Evidence exposure | 5 |
| Fusion reliability | 8 |
| Causal faithfulness | 7 |

## Verified evidence coverage

Only `yes` is counted as directly verified positive evidence. `partial` is
reported separately. `unclear` is not a negative judgment, and
`not_reported` is permitted only after full-text checking.

| Audit item | Yes | Partial | Unclear | Not reported | N/A |
| --- | ---: | ---: | ---: | ---: | ---: |
| Complete-chain or hop-wise recall | 8 | 16 | 16 | 0 | 0 |
| Matched passage/token/call/latency budget | 12 | 21 | 7 | 0 | 0 |
| Selected-set membership | 11 | 14 | 15 | 0 | 0 |
| Fixed-membership ordering/position | 3 | 7 | 30 | 0 | 0 |
| Primary-stage-aligned metric | 38 | 2 | 0 | 0 | 0 |
| Conditional fusion ablation | 8 | 14 | 18 | 0 | 0 |
| Evidence deletion | 0 | 5 | 35 | 0 | 0 |
| Evidence conflict | 1 | 7 | 32 | 0 | 0 |
| Counterfactual support | 1 | 1 | 38 | 0 | 0 |
| Retrieval-call/token/latency/FLOP cost | 22 | 18 | 0 | 0 | 0 |

## Year and architectural-family balance

| Year | Count |
| --- | ---: |
| 2019 | 1 |
| 2020 | 3 |
| 2021 | 4 |
| 2022 | 3 |
| 2023 | 8 |
| 2024 | 13 |
| 2025 | 7 |
| 2026 | 1 |

| Architectural family | Count |
| --- | ---: |
| retrieval | 13 |
| agentic | 9 |
| graph_kg | 7 |
| analysis | 5 |
| decomposition | 2 |
| fusion_reader | 2 |
| llm_reasoning | 2 |

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
