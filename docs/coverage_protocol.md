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

Substantial updates should preserve the exact executable query strings and execution dates in the internal frozen discovery/screening ledger. A search failure or API rate limit is not treated as zero results.

## Venue closure

The final venue sweep covers ACL, EMNLP, NAACL, EACL, COLING, SIGIR, WWW, WSDM, CIKM, ICLR, NeurIPS, ICML, AAAI, and IJCAI. Relevant journal and arXiv records may also enter through keyword search or citation tracing.

The venue sweep is a closure step, not a separate prevalence stratum.

## Screening and canonicalization

The aggregate corpus construction flow is:

`452 raw hits -> 342 unique candidates -> 265 primary-source review queue -> 263 resolved sources -> 208 reviewed canonical works`

- 77 unique candidates are excluded at title/metadata screening.
- 2 records remain unresolved and do not enter the reviewed denominator.
- 55 resolved records are excluded after full source review.
- Duplicate versions and title variants are merged before challenge statistics are computed.

The final 208 canonical works are divided into **135 Core, 54 Supporting, and 19 Transfer-relevant**.

## Scope tiers

- **Core:** the central contribution materially depends on evidence dependencies across multiple steps or units. Removing those dependencies would substantially change the research problem or the method's central mechanism.
- **Supporting:** the work remains within retrieval, RAG, or QA system design and provides a mechanism relevant to multi-hop systems, but dependent evidence resolution is not central to its research problem.
- **Transfer-relevant:** the work originates outside the target retrieval/RAG task population and is retained because its mechanism or boundary case clarifies one of the five challenges.

Only the 135 Core works enter the primary challenge-prevalence analysis.

## Challenge coding and adjudication

Challenge relations are coded as Direct, Secondary, or No under [`taxonomy/challenge_codebook_v2.md`](../taxonomy/challenge_codebook_v2.md). The scope and challenge assignments used in the quantitative analysis are independently reviewed by two reviewers under the same codebook. Reviewers inspect the relevant primary technical source before reconciliation. Disagreements are revisited against those sources and resolved through explicit adjudication.

The adjudicated canonical-work table generates challenge prevalence and pairwise overlap. Aggregate corpus-construction counts are generated from the internal frozen discovery and screening ledger.

## Public release boundary

The planned public row-level artifact begins at the final reviewed evidence map. Candidate-level records from the discovery and screening stages are not released. The current repository publishes the aggregate v2 snapshot but not the final row-level evidence map.

The submission-ready release is intended to include:

- the final **208-work canonical evidence map** with scope tier;
- the **135-Core challenge-relation table**;
- reviewer and adjudication provenance needed to support the quantitative coding claims; and
- scripts or generated outputs that reproduce manuscript challenge counts, pairwise overlap, and the empirical landscape figure.

The manuscript and repository report the aggregate screening counts, search protocol, query families, and venue closure so that the construction procedure remains inspectable without publishing the full candidate queue.

## Update and correction policy

Corrections to the final evidence map should identify the affected canonical work, cite the primary technical source, and explain the proposed scope or challenge revision. Any change that affects manuscript counts must regenerate the aggregate tables from the revised adjudicated coding before release.
