# Paper-to-hub map

This repository is the research hub for *Resolving Evidence Chains in
Multi-Hop RAG: A Challenge-Centered Survey*. It mirrors the paper's conceptual
structure and review snapshot without serving as the manuscript-source
repository.

## Hub contract

The current hub is aligned to the manuscript review cutoff of **August 9,
2026**. A resource is described as manuscript-aligned only when its scope,
terminology, counts, and figure role match that snapshot.

The hub has four deliberately separate layers:

1. **Conceptual layer:** the evidence-dependency definition, five challenge
   functions, figures, and literature navigation.
2. **Review layer:** the search protocol, challenge codebook, and aggregate
   evidence-map statistics.
3. **Discovery layer:** the broad seven-survey reference workbook, which is not
   a reviewed-corpus denominator.
4. **Legacy layer:** the older v1 catalog and 40-record audit, retained only for
   provenance.

The LaTeX source and working manuscript remain outside this repository.

## Paper structure and hub entry points

| Paper section or claim | Hub resource | Public status |
| --- | --- | --- |
| Positioning and research questions | [README](../README.md), [challenge-centered literature navigator](literature_navigator.md), and [seven-survey library](../literature/README.md) | Published |
| Evidence dependency as the scope | [Figure 1](../mh_figures/fig1.pdf) and [v2 challenge codebook](../taxonomy/challenge_codebook_v2.md) | Published |
| Five challenges created by evidence dependency | [Figure 2](../mh_figures/fig2.pdf), [v2 challenge codebook](../taxonomy/challenge_codebook_v2.md), and [literature navigator](literature_navigator.md) | Published |
| Review protocol and screening flow | [Coverage protocol](coverage_protocol.md), [submission audit](submission_audit_v2.md), and [aggregate search flow](../taxonomy/audit_v2/search_flow.csv) | Aggregate snapshot published |
| Next-Hop Discovery | [Literature navigator: Next-Hop Discovery](literature_navigator.md#1-next-hop-discovery) | Published |
| Path Management | [Literature navigator: Path Management](literature_navigator.md#2-path-management) | Published |
| Evidence Sufficiency | [Literature navigator: Evidence Sufficiency](literature_navigator.md#3-evidence-sufficiency) | Published |
| Error Recovery | [Literature navigator: Error Recovery](literature_navigator.md#4-error-recovery) | Published |
| Evidence Composition | [Literature navigator: Evidence Composition](literature_navigator.md#5-evidence-composition) | Published |
| From iterative retrieval to evidence-state control | [Figure 3](../mh_figures/fig3.pdf) and the cross-challenge reading paths in the [literature navigator](literature_navigator.md) | Published |
| Benchmarks and evaluation | [Benchmark reading paths](literature_navigator.md#benchmark-reading-paths) and the [five-challenge reporting checklist](reporting_checklist.md) | Published |
| Corpus-level evidence and research agenda | [Challenge counts](../taxonomy/audit_v2/challenge_counts.csv), [Direct overlap matrix](../taxonomy/audit_v2/direct_overlap.csv), [submission audit](submission_audit_v2.md), and [roadmap](roadmap.md) | Aggregate snapshot published |
| Detailed coding and sensitivity rules | [V2 codebook](../taxonomy/challenge_codebook_v2.md) and [audit-v2 README](../taxonomy/audit_v2/README.md) | Published |

## Figure mapping

Repository filenames follow the figures' order in the paper, even though the
working manuscript uses different source filenames:

| Paper figure | Repository asset | Manuscript source asset | Role |
| --- | --- | --- | --- |
| Figure 1 | [`mh_figures/fig1.pdf`](../mh_figures/fig1.pdf) | `figs/2.pdf` | Evidence-dependency scope |
| Figure 2 | [`mh_figures/fig2.pdf`](../mh_figures/fig2.pdf) | `figs/1.pdf` | Five-challenge control loop |
| Figure 3 | [`mh_figures/fig3.pdf`](../mh_figures/fig3.pdf) | `figs/4.pdf` | Challenge-mechanism landscape |

## Evidence and release boundary

The repository currently publishes the aggregate values used by the paper:

- 452 raw hits, 342 unique candidates, 265 works entering primary-source
  review, 263 resolved sources, and 208 reviewed canonical works;
- 135 Core, 54 Supporting, and 19 Transfer-relevant works;
- challenge counts and pairwise Direct overlaps for the 135 Core works.

The final 208-work canonical table, the 135-Core challenge-relation table, and
reviewer/adjudication provenance are **not yet public**. Until those row-level
artifacts and regeneration scripts are released, the hub supports inspection of
the protocol and aggregate manuscript snapshot, but not independent
regeneration of the aggregate results from row-level evidence.

The 771-paper reference workbook is a separate discovery resource. Inclusion
there does not establish primary-source review, scope eligibility, or a
challenge assignment.

## Versioning rule

Each manuscript revision that changes the review cutoff, corpus counts,
challenge coding, figures, or author metadata should update this map, the main
README, `ARTIFACT.md`, and `CITATION.cff` together. A submission-ready snapshot
should be tagged only after the row-level evidence release and regeneration
outputs are synchronized with the paper.
