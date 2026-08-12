# Artifact status

This repository is the public companion to *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*. It is a survey artifact, not a benchmark submission and not a claim that all cited experimental results are independently reproduced here.

## Current manuscript-aligned artifacts

| Artifact | Location | Status |
| --- | --- | --- |
| Challenge codebook v2 | [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md) | aligned with current manuscript |
| Submission audit summary | [`docs/submission_audit_v2.md`](docs/submission_audit_v2.md) | aligned aggregate snapshot |
| Search-flow counts | [`taxonomy/audit_v2/search_flow.csv`](taxonomy/audit_v2/search_flow.csv) | aggregate screening counts |
| Challenge counts | [`taxonomy/audit_v2/challenge_counts.csv`](taxonomy/audit_v2/challenge_counts.csv) | current Core counts |
| Direct overlap matrix | [`taxonomy/audit_v2/direct_overlap.csv`](taxonomy/audit_v2/direct_overlap.csv) | current Core overlap |
| Coverage protocol | [`docs/coverage_protocol.md`](docs/coverage_protocol.md) | current discovery and review protocol |
| Executable discovery queries | [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) | Semantic Scholar candidate discovery |
| Seven-survey reference library | [`literature/reference_library.xlsx`](literature/reference_library.xlsx) | broad discovery layer; not an audit denominator |
| Canonical Figure 1 | [`mh_figures/fig1.pdf`](mh_figures/fig1.pdf) | evidence-dependency scope |
| Canonical Figure 2 | [`mh_figures/fig2.pdf`](mh_figures/fig2.pdf) | five-challenge control loop |
| Canonical Figure 3 | [`mh_figures/fig3.pdf`](mh_figures/fig3.pdf) | challenge-mechanism landscape |

The current manuscript snapshot contains 208 reviewed canonical works: 135 Core, 54 Supporting, and 19 Transfer-relevant. Quantitative challenge prevalence uses the 135 Core works.

The separate reference library contains 886 citation records reconstructed from
seven adjacent surveys and 771 deduplicated papers. It supports candidate
discovery and cross-survey comparison; it does not establish scope eligibility,
primary-source review, or challenge coding.

## Public reproducibility boundary

The public artifact is designed to regenerate the manuscript's challenge-level quantitative results from the **final reviewed evidence map**. It does not publish the complete candidate-level discovery and screening ledger.

The tagged submission artifact should contain:

1. the final **208-work canonical evidence map** with scope tier;
2. the **135-Core challenge-relation table** with Direct, Secondary, and No coding;
3. reviewer and adjudication provenance sufficient to support the manuscript's independent-review wording; and
4. scripts or generated outputs that reproduce the challenge-count table, pairwise Direct-overlap table, and empirical landscape figure.

The candidate-level records behind the reported 452 raw hits are outside the public artifact boundary. Their aggregate screening counts, search protocol, query families, and venue closure remain documented in the manuscript and repository.

This boundary means that readers can independently inspect and regenerate the manuscript's quantitative challenge analysis without requiring publication of the full candidate discovery queue.

## Legacy v1 artifact

The following files are preserved for provenance and are not the source of the current manuscript counts:

- `taxonomy/audit_records.csv`
- `taxonomy/audit_codebook_v1.md`
- `docs/quantitative_audit.md`
- the older catalog taxonomy built around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness.

The v1 audit contains 40 single-coded records. It should not be used to validate the v2 208-work manuscript snapshot or to infer the current review reliability protocol.

## Release practice

Create a tagged GitHub release after the final 208-work evidence map, the 135-Core challenge coding, reviewer/adjudication provenance, and regeneration outputs are aligned with the manuscript. Archive the tag through a DOI-minting service if desired. Add a repository DOI to `CITATION.cff` once available; add ACM DOI, volume, issue, and page metadata only after the publisher assigns them.
