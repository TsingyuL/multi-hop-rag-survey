# Quantitative Reporting Audit

This audit is tied to the manuscript revision dated July 2026. It uses only
source-verified method records in `taxonomy/methods.csv` and excludes seeded
examples, needs-review entries, and local discovery queues. The denominator is
therefore a conservative reviewed seed, not a frequency estimate over all
multi-hop RAG publications.

## Reviewed Denominator

| Quantity | Count |
| --- | ---: |
| Method records in catalog | 23 |
| Source-verified method records used in audit | 20 |
| Benchmark records in catalog | 6 |
| Intervention mappings in catalog | 27 |

## Primary Target Distribution

| Primary target | Count over reviewed methods |
| --- | ---: |
| Observability | 7 |
| Selection preservation | 3 |
| Evidence exposure | 2 |
| Fusion reliability | 5 |
| Causal faithfulness | 0 |
| Joint or adaptive primary control | 3 |

## Metadata Coverage

| Audit item | Count |
| --- | ---: |
| Reviewed methods with a public code URL recorded | 13 |
| Reviewed benchmark records | 6 |

## Interpretation

The reviewed seed is front-loaded toward acquisition and fusion. Selection
preservation and exposure are present but less often isolated with
chain-preservation or fixed-membership diagnostics. Causal faithfulness is
mostly secondary or evaluation-side in this seed, which is why future catalog
releases should explicitly code deletion, conflict, and counterfactual
evidence-use probes.

Broad discovery is maintained through query templates and local queues rather
than a committed imported-paper dump, so the public repository exposes one
current reviewed version of the taxonomy.
