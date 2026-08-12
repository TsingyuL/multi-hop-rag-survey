# Multi-Hop RAG Research Hub

> Research hub and public companion for **“Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey.”**

[![Manuscript](https://img.shields.io/badge/manuscript-TOIS%20draft-2457C5.svg)](#associated-manuscript)
[![Research hub](https://img.shields.io/badge/research%20hub-open-2457C5.svg)](https://tsingyul.github.io/multi-hop-rag-survey/)
[![Audit](https://img.shields.io/badge/audit-v2%20aggregate%20snapshot-087E8B.svg)](docs/submission_audit_v2.md)
[![Reference library](https://img.shields.io/badge/reference%20library-771%20deduplicated%20papers-6F42C1.svg)](literature/README.md)
[![License: MIT](https://img.shields.io/badge/code%20%26%20catalog-MIT-green.svg)](LICENSE)

This repository is the **paper-aligned research hub** for a survey of multi-hop retrieval-augmented generation defined by **dependency among external evidence units**. It mirrors the paper's conceptual framework, figures, review protocol, aggregate evidence map, and reading paths while keeping the manuscript source outside the repository. See the [paper-to-hub map](docs/paper_hub.md) for the section-by-section correspondence.

The current manuscript organizes the literature around five nonexclusive challenges: **Next-Hop Discovery, Path Management, Evidence Sufficiency, Error Recovery, and Evidence Composition**.

The repository contains documentation and aggregate audit files aligned with the manuscript review cutoff of **August 9, 2026**. The older 40-record v1 audit is retained for provenance but is not the source of the current manuscript counts.

## Start here

| Need | Open |
| --- | --- |
| Web research hub | [GitHub Pages](https://tsingyul.github.io/multi-hop-rag-survey/) |
| Paper section-to-resource map | [`docs/paper_hub.md`](docs/paper_hub.md) |
| Current challenge codebook | [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md) |
| Current audit summary | [`docs/submission_audit_v2.md`](docs/submission_audit_v2.md) |
| Aggregate v2 audit files | [`taxonomy/audit_v2/`](taxonomy/audit_v2/) |
| Seven-survey reference library | [`literature/README.md`](literature/README.md), [`literature/reference_library.xlsx`](literature/reference_library.xlsx) |
| Challenge-centered literature navigator | [`docs/literature_navigator.md`](docs/literature_navigator.md) |
| Current manuscript figures | [`mh_figures/README.md`](mh_figures/README.md) |
| Discovery and coverage protocol | [`docs/coverage_protocol.md`](docs/coverage_protocol.md) |
| Executable Semantic Scholar query families | [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) |
| Legacy catalog | [`taxonomy/methods.csv`](taxonomy/methods.csv), [`taxonomy/benchmarks.csv`](taxonomy/benchmarks.csv) |
| Legacy 40-record audit | [`taxonomy/audit_records.csv`](taxonomy/audit_records.csv), [`taxonomy/audit_codebook_v1.md`](taxonomy/audit_codebook_v1.md) |

## Current manuscript snapshot

The frozen evidence map contains **208 canonical works**:

- **135 Core**
- **54 Supporting**
- **19 Transfer-relevant**

The corpus construction flow reported in the manuscript is:

`452 raw hits -> 342 unique candidates -> 265 primary-source review queue -> 263 resolved sources -> 208 reviewed canonical works`

Candidate-level discovery and screening records are not part of the public release. The current hub reports the aggregate screening counts and protocol. The planned row-level release will begin with the final **208 reviewed canonical works**, but that table and the 135-Core challenge-relation table are not yet public.

The quantitative challenge analysis uses the **135 Core works** as its prevalence denominator.

| Challenge | Direct | Direct+Secondary |
| --- | ---: | ---: |
| Next-Hop Discovery | 84 | 100 |
| Path Management | 41 | 64 |
| Evidence Sufficiency | 24 | 31 |
| Error Recovery | 11 | 15 |
| Evidence Composition | 43 | 98 |

Two overlap results anchor the manuscript findings: 22 of 24 Direct Sufficiency works also instantiate Direct Discovery (**91.7%**), while 5 of 24 instantiate Direct Recovery (**20.8%**). Direct Path Management and Direct Recovery overlap in only **one** Core work.

## Five challenge families

| Challenge | Core question |
| --- | --- |
| **Next-Hop Discovery** | What concrete information should be sought next from the current evidence state? |
| **Path Management** | Which candidate trajectories should be retained, prioritized, merged, or pruned? |
| **Evidence Sufficiency** | Is the current evidence adequate for the remaining task? |
| **Error Recovery** | After a state is diagnosed as invalid or unproductive, how should it be revised or replaced? |
| **Evidence Composition** | Once the required evidence is available, can the system perform the required operation across evidence units? |

The first four challenges control the evolution of the evidence state. Evidence Composition concerns how an assembled support structure is used.

## Review protocol

Candidate discovery combines adjacent-survey consolidation, Semantic Scholar keyword queries, backward and forward citation tracing, and a final venue sweep. Primary-source identity and technical claims are checked against authoritative landing pages such as ACL Anthology, OpenReview, arXiv, the ACM Digital Library, publisher pages, and official repositories.

The scope and challenge assignments used for manuscript-level quantitative results are independently reviewed by two reviewers under the same operational codebook. Disagreements are revisited against the primary technical source and resolved through explicit adjudication.

See [`docs/coverage_protocol.md`](docs/coverage_protocol.md) and [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md) for the operational rules.

## Adjacent-survey reference layer

The research hub also includes a broad reference library reconstructed from
seven adjacent surveys. It contains **886 raw citation records**, **771
deduplicated papers**, **75 papers cited by at least two surveys**, and **16
papers cited by at least three surveys**.

This layer supports discovery and cross-survey comparison. It is deliberately
separate from the frozen **208-work reviewed evidence map**: inclusion in the
reference library does not imply primary-source review, scope inclusion, or
challenge coding. See [`literature/README.md`](literature/README.md) for the
workbook schema and interpretation boundary.

## Public artifact boundary

The current public hub supports inspection of the manuscript's protocol and aggregate **challenge-level quantitative results**. It does not yet support independent regeneration from row-level evidence, and it is not intended to expose the complete candidate discovery queue.

The submission-ready release should additionally contain:

1. the final **208-work canonical evidence map** with scope tier;
2. the **135-Core challenge-relation table** with Direct, Secondary, and No assignments;
3. reviewer and adjudication provenance sufficient to support the manuscript's independent-review wording; and
4. scripts or generated outputs that reproduce the challenge-count table, pairwise overlap table, and empirical landscape figure.

The candidate-level discovery and screening ledger for the 452 raw hits is not part of the public artifact. Aggregate screening counts, search protocol, query families, and venue closure are documented in the manuscript and repository. See [`ARTIFACT.md`](ARTIFACT.md) for the current completeness statement.

## Legacy v1 catalog and audit

The repository previously organized a 50-record catalog and a 40-record single-coded diagnostic audit around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness. Those files remain available to preserve the project history and should be treated as **legacy v1 artifacts**.

They are not the taxonomy or denominator used by the current challenge-centered manuscript.

## Associated manuscript

- **Title:** Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey
- **Authors:** Yuqing Luo, Kai Zhang, and Liyang He
- **Affiliation:** University of Science and Technology of China
- **Target venue:** ACM Transactions on Information Systems (TOIS)
- **Review cutoff:** August 9, 2026

The repository does not contain an ACM Version of Record. Publisher DOI, volume, issue, and page metadata should be added only after assignment. The manuscript source is maintained outside this research hub.

## Citation

Until final publisher metadata exists, cite the manuscript as:

```bibtex
@article{luo2026resolving,
  author = {Yuqing Luo and Kai Zhang and Liyang He},
  title  = {Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey},
  year   = {2026},
  note   = {Manuscript draft. Companion repository: https://github.com/TsingyuL/multi-hop-rag-survey}
}
```

See [`CITATION.cff`](CITATION.cff) for GitHub citation metadata.

## Contributing

Corrections and additions are welcome. New challenge-level coding should follow [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md). The older catalog schema is preserved for backward compatibility; see [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing legacy CSV headers.

## License and attribution

Repository-authored catalog data, documentation, and utility code are released under the [MIT License](LICENSE). The manuscript and figures remain subject to the authors' publication and publisher terms.
