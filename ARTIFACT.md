# Artifact status

This repository is the public companion to *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*. It is a survey artifact, not a benchmark submission and not a claim that all cited experimental results are independently reproduced here.

## Current manuscript-aligned artifacts

| Artifact | Location | Status |
| --- | --- | --- |
| Challenge codebook v2 | [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md) | aligned with current manuscript |
| Submission audit summary | [`docs/submission_audit_v2.md`](docs/submission_audit_v2.md) | aligned aggregate snapshot |
| Search-flow counts | [`taxonomy/audit_v2/search_flow.csv`](taxonomy/audit_v2/search_flow.csv) | current aggregate counts |
| Challenge counts | [`taxonomy/audit_v2/challenge_counts.csv`](taxonomy/audit_v2/challenge_counts.csv) | current Core counts |
| Direct overlap matrix | [`taxonomy/audit_v2/direct_overlap.csv`](taxonomy/audit_v2/direct_overlap.csv) | current Core overlap |
| Coverage protocol | [`docs/coverage_protocol.md`](docs/coverage_protocol.md) | current discovery and review protocol |
| Executable discovery queries | [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) | Semantic Scholar candidate discovery |

The current manuscript snapshot contains 208 reviewed canonical works: 135 Core, 54 Supporting, and 19 Transfer-relevant. Quantitative challenge prevalence uses the 135 Core works.

## Reproducibility boundary

The aggregate v2 files reproduce the counts reported by the manuscript, but the public repository does not yet contain the full row-level v2 release.

Before submission, the tagged artifact should additionally contain:

1. the frozen discovery and screening ledger that regenerates the 452 -> 342 -> 265 -> 263 -> 208 corpus flow;
2. the 208-work canonical table with scope tier;
3. the 135-Core challenge-relation table;
4. reviewer and adjudication provenance sufficient to support the manuscript's independent-review wording; and
5. scripts or generated outputs that reproduce the manuscript challenge tables and empirical landscape figure.

Until those row-level files are published, the aggregate snapshot is inspectable but not independently regenerable from raw records in this repository.

## Legacy v1 artifact

The following files are preserved for provenance and are not the source of the current manuscript counts:

- `taxonomy/audit_records.csv`
- `taxonomy/audit_codebook_v1.md`
- `docs/quantitative_audit.md`
- the older catalog taxonomy built around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness.

The v1 audit contains 40 single-coded records. It should not be used to validate the v2 208-work manuscript snapshot or to infer the current review reliability protocol.

## Release practice

Create a tagged GitHub release only after all manuscript-level counts regenerate from the files included in that tag. Archive the tag through a DOI-minting service if desired. Add a repository DOI to `CITATION.cff` once available; add ACM DOI, volume, issue, and page metadata only after the publisher assigns them.
