# Artifact status

This repository is the public companion for *Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment*.

## Current manuscript snapshot

The manuscript uses a frozen canonical frame of **274 papers** with review cutoff **2026-08-05**:

- 149 CORE;
- 57 SUPPORTING;
- 68 TRANSFER.

The revised empirical synthesis uses coarse knowledge-access descriptors and a targeted recheck of the state-dependent routing subset. Historical challenge-centered files based on the earlier 208-work snapshot are retained for provenance but are not current manuscript-aligned quantitative artifacts.

## Submission-aligned artifacts

| Artifact | Status |
| --- | --- |
| Frozen 274-paper canonical frame | required for tagged submission release |
| Knowledge-access mapping (representation / interface / regime / cross-hop relation) | current analytical basis; row-level release required before submission freeze |
| Nine-case routing-evaluation recheck | current targeted synthesis; release required before submission freeze |
| Discovery query strings | available in `taxonomy/discovery_queries.csv` |
| Coverage protocol | updated in `docs/coverage_protocol.md` |
| Adjacent-survey reference library | discovery layer only; not a corpus denominator |
| Historical five-challenge audit | legacy/provenance only |

## Public reproducibility boundary

The review is a **structured evidence map**, not a registered systematic review or statistical meta-analysis. The exact 274-paper frame is the auditable denominator for current manuscript counts. However, the final expansion does **not** have a complete per-database raw-hit ledger with execution dates and deduplication counts sufficient to reconstruct a PRISMA-style flow from initial search results to the 274-paper frame. The repository therefore must not reuse the historical `452 → 342 → 265 → 263 → 208` flow as if it generated the current corpus.

The broader fine-grained coding schema underwent blinded reliability attempts, but the confirmatory reliability gate did **not** meet the pre-specified threshold. The submission artifact must therefore preserve the manuscript's interpretation boundary:

- corpus percentages are descriptive, evidence-backed mappings rather than reliability-validated prevalence estimates;
- the revised access synthesis uses coarse, explicitly defined descriptors;
- high-leverage routing/evaluation claims use targeted primary-source rechecks.

## Required tagged submission release

Before submission, the tagged artifact should include:

1. the exact **274-paper canonical frame** and scope tier;
2. the row-level coarse knowledge-access mapping used for RQ3;
3. the **nine-case routing-evaluation recheck** and directness criterion used for RQ4;
4. executable discovery queries and the final **2026-08-05** cutoff statement;
5. scripts or generated outputs that reproduce manuscript tables and empirical figures from the frozen release;
6. a checksum, tag, or immutable commit identifying the exact artifact version cited by the paper.

No artifact should claim fully adjudicated independent double coding for the current 274-paper quantitative map unless a new valid reliability process is completed and released.

## Historical artifacts

The following materials describe earlier project snapshots and remain available only for provenance:

- `taxonomy/audit_v2/` and the five-challenge codebook (208-work challenge-centered manuscript snapshot);
- `taxonomy/audit_records.csv`, `taxonomy/audit_codebook_v1.md`, and `docs/quantitative_audit.md` (older v1 catalog/audit).

Historical counts and challenge prevalence should not be cited as current manuscript results.

## Release practice

Create a tagged GitHub release only after the paper, canonical frame, access mapping, routing recheck, figures, and documentation agree on the same denominator, cutoff, definitions, and caveats. Archive the tag through a DOI-minting service if desired. Add publisher metadata only after assignment.
