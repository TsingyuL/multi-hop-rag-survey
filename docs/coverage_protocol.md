# Coverage and review protocol

## Purpose and claim boundary

This repository supports the evidence map behind *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*. The review is a structured evidence map rather than a registered systematic review or a statistical meta-analysis. Reported counts describe the corpus produced by the declared protocol; they do not imply that no relevant work exists outside the corpus.

The manuscript review cutoff is **2026-08-09**.

## Scope

The current survey defines multi-hop RAG by **dependency among external evidence units**, not by document count, retrieval-call count, or reasoning length.

A work is in the target problem space when at least one of the following holds:

1. **Acquisition dependency:** evidence obtained earlier changes or specifies a later information need, retrieval target, or search action.
2. **Reasoning dependency:** answering requires a substantive operation across multiple external evidence units, such as binding, comparison, conjunction, relational join, aggregation, temporal alignment, or transformation.

Purely parametric chain-of-thought work is outside this scope unless external evidence access is part of the mechanism or task. Reader-only multi-hop systems may still be retained as mechanism evidence for Evidence Composition without being relabeled as end-to-end RAG systems.

## Discovery channels

Candidate discovery uses four complementary channels:

1. consolidation from adjacent surveys;
2. keyword search;
3. backward and forward citation tracing from canonical methods and benchmarks; and
4. a final sweep of recent relevant venues.

The frozen aggregate counts are:

| Discovery channel | Records |
| --- | ---: |
| Adjacent survey consolidation | 171 |
| Keyword search | 123 |
| Citation tracing | 92 |
| Final venue sweep | 66 |
| **Raw source hits** | **452** |

The executable keyword families in [`taxonomy/discovery_queries.csv`](../taxonomy/discovery_queries.csv) use Semantic Scholar as the candidate-discovery service. Those machine-executable strings are a maintenance interface; the manuscript reports the broader conceptual query families used in the review.

Primary-source identity and technical claims are subsequently checked against authoritative landing pages such as ACL Anthology, OpenReview, arXiv, the ACM Digital Library, publisher pages, and official repositories.

## Query families

The review uses query families covering at least the following concepts:

- multi-hop question answering plus retrieval;
- explicit multi-hop retrieval-augmented generation;
- iterative or multi-step retrieval with reasoning;
- multi-hop knowledge-graph question answering;
- evidence-chain retrieval and verification.

Substantial updates should preserve the exact executable query strings and execution dates in the frozen discovery/screening ledger. A search failure or API rate limit is not treated as zero results.

## Venue closure

The final venue sweep covers ACL, EMNLP, NAACL, EACL, COLING, SIGIR, WWW, WSDM, CIKM, ICLR, NeurIPS, ICML, AAAI, and IJCAI. Relevant journal and arXiv records may also enter through keyword search or citation tracing.

The venue sweep is a closure step, not a separate prevalence stratum.

## Screening and canonicalization

The frozen corpus construction flow is:

`452 raw hits -> 342 unique candidates -> 265 primary-source review queue -> 263 resolved sources -> 208 reviewed canonical works`

- Duplicate versions and title variants are merged before challenge statistics are computed.
- 77 unique candidates are excluded at title/metadata screening.
- 2 records remain unresolved and do not enter the reviewed denominator.
- 55 resolved records are excluded after full source review.

The final 208 canonical works are divided into **135 Core, 54 Supporting, and 19 Transfer-relevant**.

## Scope tiers

- **Core:** the central contribution materially depends on evidence dependencies across multiple steps or units. Removing those dependencies would substantially change the research problem or the method's central mechanism.
- **Supporting:** the work remains within retrieval, RAG, or QA system design and provides a mechanism relevant to multi-hop systems, but dependent evidence resolution is not central to its research problem.
- **Transfer-relevant:** the work originates outside the target retrieval/RAG task population and is retained because its mechanism or boundary case clarifies one of the five challenges.

Only the 135 Core works enter the primary challenge-prevalence analysis.

## Challenge coding

The current manuscript uses the five challenge families in [`taxonomy/challenge_codebook_v2.md`](../taxonomy/challenge_codebook_v2.md):

- Next-Hop Discovery
- Path Management
- Evidence Sufficiency
- Error Recovery
- Evidence Composition

Each work-to-challenge relation is coded as Direct, Secondary, or No. Direct prevalence and pairwise overlap are computed only among Core works. Direct+Secondary is reported as a sensitivity analysis for relation strength.

## Independent review and adjudication

The scope and challenge assignments used for manuscript-level quantitative results are independently reviewed by two reviewers under the same codebook. Each reviewer checks the relevant primary technical source before reconciliation. Disagreements are revisited against the source and resolved through explicit adjudication.

The frozen discovery/screening ledger is the source of corpus-construction counts. The adjudicated canonical-work table is the source of challenge prevalence and pairwise overlap.

No inter-coder coefficient should be reported unless the unreconciled reviewer labels required to compute it are preserved and released.

## Artifact status

The manuscript-aligned aggregate snapshot is available in [`taxonomy/audit_v2/`](../taxonomy/audit_v2/) and summarized in [`docs/submission_audit_v2.md`](submission_audit_v2.md).

The legacy 40-record v1 audit is retained for provenance only. It is single-coded and does not support the current manuscript's 208-work counts or independent-review statement.

Before submission, the tagged release should add the row-level frozen screening ledger, canonical 208-work table, 135-Core challenge-relation table, and reviewer/adjudication provenance needed to regenerate the aggregate snapshot independently.

## Update and correction policy

1. Resolve canonical identity before adding a work to the reviewed corpus.
2. Record discovery provenance separately from inclusion and challenge coding.
3. Use primary technical sources for scope and challenge decisions.
4. Preserve exclusion reasons and unresolved-source status rather than silently dropping records.
5. Run structural validators and regenerate aggregate tables after any change to corpus membership or challenge coding.
6. Summarize material corrections in the repository change log or pull request.

This protocol favors inspectable decisions and versioned counts over inflated paper totals.