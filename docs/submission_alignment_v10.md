# Submission alignment snapshot v10

This page is the submission-facing consistency record for the current TOIS draft.

## Manuscript identity

- **Title:** *Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment*
- **Target venue:** ACM Transactions on Information Systems (TOIS)
- **Review cutoff:** **2026-08-05**
- **Canonical frame:** **274 papers**
  - 149 CORE
  - 57 SUPPORTING
  - 68 TRANSFER

## Main analytical story

The manuscript uses four connected layers:

1. **Evidence dependency** — acquisition dependency and reasoning dependency define scope.
2. **Process organization** — established process families are retained as the methodological backbone.
3. **Knowledge-access conditions** — external representation, acquisition interface, source regime, and the derived stable/transitioning relation across dependent hops.
4. **Evaluation alignment** — whether intermediate process/access decisions are directly measured or only reflected in downstream outcomes.

The manuscript does **not** claim a new replacement process taxonomy.

## Current descriptive corpus results

Primary synthesis set: CORE + SUPPORTING.

- Retrieval-bearing: **170** papers.
- Acquisition-dependent: **111** papers.
- Text-only external evidence: **139/170 (81.8%)**.
- Fixed/closed source regime: **160/170 (94.1%)**.
- Access-stable among acquisition-dependent papers: **99/111 (89.2%)**.
- Adaptive routing / transition-capable: **9/111 (8.1%)**.
- Heterogeneous access with transition not established: **3/111 (2.7%)**.

Interpretation: knowledge-access diversity is **complementary rather than dominant**. No monotonic temporal increase in non-default access is claimed.

## Routing-evaluation recheck

The nine state-dependent routing / transition-capable cases received a targeted primary-source recheck.

- Direct route/program correctness: **1/9**.
- Direct route/program or selector/gating diagnostic: **2/9**.
- No direct intermediate access-decision diagnostic under the recheck criterion: **7/9**.

Safe claim: **direct intermediate access-decision diagnostics are uncommon, not absent**.

The earlier `0/9 direct routing evaluation` claim is retired and must not reappear in the manuscript, repository documentation, figures, or supplementary material.

## Reliability and evidence boundary

The broader fine-grained coding scheme underwent blinded confirmatory reliability attempts but did **not** meet the pre-specified threshold. Therefore:

- corpus percentages are descriptive evidence-backed mappings, not reliability-validated prevalence estimates;
- no current artifact should claim fully adjudicated independent double coding for the 274-paper map;
- high-leverage routing/evaluation claims rely on targeted primary-source rechecking.

## Search/reproducibility boundary

The final 274-paper expansion does not have a complete per-database raw-hit ledger that supports a PRISMA-style flow. The auditable denominator is the frozen 274-paper canonical frame. The historical `452 → … → 208` flow belongs to an earlier snapshot and is not the current corpus-construction flow.

Executable Semantic Scholar maintenance-query families remain available in `taxonomy/discovery_queries.csv`.

## Historical materials

The five-challenge taxonomy, 208-work challenge audit, associated challenge counts/overlaps, and earlier manuscript figures are historical project artifacts. They remain public for provenance but are not current submission claims.

## Submission freeze checklist

Before tagging a submission release, verify that all of the following agree with this page:

- `README.md`;
- `ARTIFACT.md`;
- `docs/coverage_protocol.md`;
- `docs/paper_hub.md`;
- `CITATION.cff`;
- manuscript title/abstract/methods/results/limitations;
- row-level canonical frame and knowledge-access mapping;
- nine-case routing-evaluation appendix;
- main-text figures and captions.

A tagged release should identify the exact immutable artifact cited by the paper.
