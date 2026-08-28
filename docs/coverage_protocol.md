# Coverage and review protocol

## Purpose and claim boundary

This repository supports the structured evidence map behind *Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment*.

The review is a **structured evidence map**, not a registered systematic review or a statistical meta-analysis. Reported counts describe the frozen corpus produced by the declared protocol and do not imply exhaustive recall.

The auditable manuscript review cutoff is **2026-08-05**.

## Scope

The survey defines multi-hop RAG through **evidence dependency**, not document count, retrieval-call count, or reasoning length.

A work may satisfy one or both of the following:

1. **Acquisition dependency:** evidence obtained earlier materially changes or specifies a later external information need, retrieval target, source choice, or acquisition action.
2. **Reasoning dependency:** answering requires a substantive operation across multiple external evidence units, such as binding, relation composition, comparison, conjunction, aggregation, arithmetic, temporal/schema alignment, cross-source composition, or cross-modal composition.

Repeated retrieval is not sufficient if later acquisition is predetermined or depends only on the original question. Multiple documents do not by themselves establish reasoning dependency. Search or selection performed only inside evidence already supplied to the evaluated model is not treated as external acquisition.

## Discovery channels

Candidate discovery combined complementary channels:

1. consolidation from adjacent surveys;
2. keyword search;
3. backward and forward citation tracing from canonical methods and benchmarks; and
4. venue and recency closure over relevant IR, NLP, ML, and AI venues.

Primary-source identity and technical claims were checked against authoritative sources such as ACL Anthology, OpenReview, arXiv, the ACM Digital Library, publisher/venue proceedings pages, and official repositories. DBLP and Semantic Scholar were additionally useful for discovery, identity resolution, and deduplication.

The repository exposes five executable Semantic Scholar maintenance-query families in [`taxonomy/discovery_queries.csv`](../taxonomy/discovery_queries.csv):

- `multi hop question answering retrieval`;
- `multi hop retrieval augmented generation`;
- `iterative retrieval reasoning question answering`;
- `multi hop knowledge graph question answering`;
- `multi hop evidence chain retrieval`.

These strings are reproducible maintenance queries, not a complete reconstruction of every historical search action. Broader conceptual terms and citation/venue closure were also used because terminology changed substantially across the 2017–2026 literature.

## Temporal window and venue closure

The eligibility/search window begins in **January 2017** and closes on **August 5, 2026**. The final venue sweep includes major venues such as ACL, EMNLP, NAACL, EACL, COLING, SIGIR, WWW, WSDM, CIKM, ICLR, NeurIPS, ICML, AAAI, and IJCAI, with relevant journal and arXiv records entering through search or citation tracing.

The venue sweep is a closure step rather than a prevalence stratum.

## Canonicalization and frozen frame

The counting unit for corpus-level analysis is a **canonical paper identity**. Preprint and archival versions, title variants, and duplicate discovery records are merged when they refer to the same work. A paper is not split merely because it reports multiple datasets, model sizes, hyperparameters, or ordinary ablations.

The current frozen frame contains **274 papers**:

- **149 CORE**;
- **57 SUPPORTING**;
- **68 TRANSFER**.

The exact 274-paper frame is the denominator for manuscript corpus-level counts. The historical challenge-centered flow `452 raw hits → 342 unique candidates → 265 primary-source review queue → 263 resolved sources → 208 reviewed canonical works` belongs to an earlier project snapshot and must not be represented as the construction flow for the current 274-paper corpus.

The final 274-paper expansion does **not** have a complete per-database raw-hit ledger with query execution dates and deduplication counts sufficient to reconstruct a PRISMA-style flow. We therefore report the frozen canonical denominator and protocol rather than retrofitting historical screening counts.

## Scope tiers

- **CORE:** the principal evaluated pipeline is retrieval-bearing and acquisition dependency and/or reasoning dependency is central to the problem or mechanism.
- **SUPPORTING:** the work provides directly relevant evidence on multi-evidence reasoning, integration, evaluation, or scope boundaries without satisfying the full retrieval-bearing CORE gate.
- **TRANSFER:** the work provides adjacent methodological or diagnostic evidence but is not treated as a primary multi-hop RAG study.

## Primary-source coding and evidence provenance

Analytical coding is based on the exact primary technical source rather than titles, secondary surveys, or repository descriptions. The project evidence stores record source URLs, evidence notes, coder/provenance information, and confidence for analytical fields.

The revised manuscript does not elevate the complete legacy fine-grained schema into a new taxonomy. For RQ3 it uses three coarse external-access descriptors:

1. **Knowledge representation** — the form in which externally acquired evidence is exposed;
2. **Acquisition interface** — the external mechanism used to obtain evidence;
3. **Source regime** — fixed/closed versus open/dynamic.

For acquisition-dependent systems, a derived **cross-hop access relation** distinguishes stable access, heterogeneous access without an established state-dependent transition, and adaptive routing/transition-capable access.

Internal graphs, trees, summaries, or triples built solely to organize an otherwise textual evidence source are treated as process/index structures unless the evaluated acquisition action directly exposes graph/structured evidence.

## Reliability and interpretation boundary

The broader fine-grained coding scheme underwent blinded reliability attempts under a frozen manual. The confirmatory reliability gate did **not** meet its pre-specified threshold. Accordingly, the current manuscript does not describe the 274-paper map as a reliability-validated prevalence census and does not claim fully adjudicated independent double coding.

Instead:

- full-corpus percentages are reported as **descriptive, evidence-backed mappings**;
- the revised synthesis relies on coarse access descriptors with explicit boundaries;
- high-leverage claims about the nine state-dependent routing cases are supported by targeted paper-by-paper primary-source rechecking.

The routing recheck also retires the earlier `0/9 direct routing evaluation` claim: direct intermediate diagnostics are uncommon, not absent.

## Public release boundary

The submission-ready tagged artifact should include:

- the exact **274-paper canonical frame** and scope tier;
- the row-level coarse knowledge-access mapping used for RQ3;
- the nine-case routing-evaluation recheck and directness criterion used for RQ4;
- executable discovery queries and the final cutoff statement;
- scripts or generated outputs that reproduce manuscript tables and empirical figures from the same frozen release.

Candidate-level raw-hit reconstruction is not claimed for the final frame because the complete final search ledger is unavailable.

## Update and correction policy

Corrections should identify the affected canonical work, cite the primary technical source, state the proposed revision, and regenerate every manuscript result affected by the change. Any release tag used in the paper should be immutable and internally consistent with the paper's cutoff, corpus size, field definitions, and caveats.
