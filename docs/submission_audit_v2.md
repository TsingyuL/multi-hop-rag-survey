# Submission audit snapshot v2

**Manuscript:** *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*  
**Review cutoff:** 2026-08-09  
**Status:** aggregate snapshot aligned with the current manuscript.

This document replaces the legacy 40-record v1 audit as the summary used by the current manuscript. The v1 files remain in the repository for provenance but are not the source of the current 208-work counts.

## Corpus construction

Four discovery channels contribute to the frozen screening flow:

| Discovery channel | Records |
| --- | ---: |
| Adjacent survey consolidation | 171 |
| Keyword search | 123 |
| Backward and forward citation tracing | 92 |
| Final venue sweep | 66 |
| **Raw source hits** | **452** |

After duplicate and version consolidation, the aggregate screening flow is:

`452 raw hits -> 342 unique candidates -> 265 primary-source review queue -> 263 resolved sources -> 208 reviewed canonical works`

Additional bookkeeping:

- 77 unique candidates are excluded at title/metadata screening.
- 2 records remain unresolved and do not enter the denominator.
- 55 resolved records are excluded after full source review.

The 208 reviewed works are divided into:

| Scope tier | Count |
| --- | ---: |
| Core | 135 |
| Supporting | 54 |
| Transfer-relevant | 19 |
| **Total** | **208** |

The candidate-level records behind the 452 raw hits are not part of the public release. The aggregate screening counts and protocol are reported for transparency; the public row-level artifact begins with the final 208 reviewed canonical works.

## Search sources and closure

Executable keyword-query families are maintained in `taxonomy/discovery_queries.csv` and currently use Semantic Scholar. Primary-source identity and technical claims are resolved against authoritative landing pages such as ACL Anthology, OpenReview, arXiv, the ACM Digital Library, publisher pages, and official repositories.

The final venue sweep covers ACL, EMNLP, NAACL, EACL, COLING, SIGIR, WWW, WSDM, CIKM, ICLR, NeurIPS, ICML, AAAI, and IJCAI. The venue sweep is a closure step rather than a separate prevalence stratum.

## Challenge representation in the Core corpus

Relations are nonexclusive. Direct is the primary prevalence criterion; Direct+Secondary is a sensitivity view.

| Challenge | Direct | Direct+Secondary |
| --- | ---: | ---: |
| Next-Hop Discovery | 84 | 100 |
| Path Management | 41 | 64 |
| Evidence Sufficiency | 24 | 31 |
| Error Recovery | 11 | 15 |
| Evidence Composition | 43 | 98 |

## Pairwise Direct overlap

|  | NHD | Path | Suff. | Rec. | Comp. |
| --- | ---: | ---: | ---: | ---: | ---: |
| NHD | 84 | 24 | 22 | 8 | 12 |
| Path | 24 | 41 | 4 | 1 | 6 |
| Suff. | 22 | 4 | 24 | 5 | 3 |
| Rec. | 8 | 1 | 5 | 11 | 2 |
| Comp. | 12 | 6 | 3 | 2 | 43 |

Two manuscript ratios follow directly from this table:

- 22 of 24 Direct Sufficiency works also instantiate Direct Discovery: **91.7%**.
- 5 of 24 Direct Sufficiency works also instantiate Direct Recovery: **20.8%**.

## Review reliability

The scope and challenge assignments used for manuscript-level quantitative results are independently reviewed by two reviewers under the same operational codebook. Reviewers inspect the relevant primary technical source before reconciliation. Disagreements are resolved through source-grounded adjudication.

No inter-coder coefficient is reported unless the unreconciled reviewer labels needed to compute it are preserved in the release.

## Interpretation boundary

These counts describe literature representation under the declared protocol. They do not measure intrinsic challenge importance or absolute system competence.

The current overlap structure supports four manuscript findings:

1. Evidence adequacy and state integrity are distinct control decisions.
2. Insufficiency is coupled far more often with forward Discovery than with Recovery.
3. Direct Path Management and Direct Recovery overlap in only one Core work, indicating that proactive path preservation and reactive repair are rarely unified under the Direct criterion.
4. Acquisition success and evidence use require separate attribution.

## Public artifact completeness

The aggregate files in `taxonomy/audit_v2/` reproduce the counts in this document. The submission release should additionally publish the final **208-work canonical evidence map**, the **135-Core challenge-relation table**, and reviewer/adjudication provenance sufficient to regenerate and inspect the manuscript's quantitative challenge analysis.

The candidate-level discovery and screening ledger is outside the public artifact boundary. Readers can inspect the aggregate screening flow and search protocol without requiring publication of the full candidate queue.

The legacy v1 audit should not be used to validate the current manuscript counts.