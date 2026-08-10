# Multi-Hop RAG Survey Companion

> Companion repository for **“Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey.”**

[![Manuscript](https://img.shields.io/badge/manuscript-TOIS%20draft-2457C5.svg)](#associated-manuscript)
[![Audit](https://img.shields.io/badge/audit-v2%20aggregate%20snapshot-087E8B.svg)](docs/submission_audit_v2.md)
[![License: MIT](https://img.shields.io/badge/code%20%26%20catalog-MIT-green.svg)](LICENSE)

This repository is the public companion to a survey of multi-hop retrieval-augmented generation defined by **dependency among external evidence units**. The current manuscript organizes the literature around five nonexclusive challenges: **Next-Hop Discovery, Path Management, Evidence Sufficiency, Error Recovery, and Evidence Composition**.

The repository now contains documentation and aggregate audit files aligned with the manuscript review cutoff of **August 9, 2026**. The older 40-record v1 audit is retained for provenance but is not the source of the current manuscript counts.

## Start here

| Need | Open |
| --- | --- |
| Current challenge codebook | [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md) |
| Current audit summary | [`docs/submission_audit_v2.md`](docs/submission_audit_v2.md) |
| Aggregate v2 audit files | [`taxonomy/audit_v2/`](taxonomy/audit_v2/) |
| Discovery and coverage protocol | [`docs/coverage_protocol.md`](docs/coverage_protocol.md) |
| Executable Semantic Scholar query families | [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) |
| Legacy catalog | [`taxonomy/methods.csv`](taxonomy/methods.csv), [`taxonomy/benchmarks.csv`](taxonomy/benchmarks.csv) |
| Legacy 40-record audit | [`taxonomy/audit_records.csv`](taxonomy/audit_records.csv), [`taxonomy/audit_codebook_v1.md`](taxonomy/audit_codebook_v1.md) |

## Current manuscript snapshot

The frozen evidence map contains **208 canonical works**:

- **135 Core**
- **54 Supporting**
- **19 Transfer-relevant**

The corpus construction flow is:

`452 raw hits -> 342 unique candidates -> 265 primary-source review queue -> 263 resolved sources -> 208 reviewed canonical works`

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

## Artifact status

The repository documentation, citation metadata, challenge codebook, and aggregate audit statistics are aligned with the current manuscript. The aggregate files in [`taxonomy/audit_v2/`](taxonomy/audit_v2/) reproduce the manuscript-level counts shown above.

**One release task remains before submission:** publish the row-level frozen discovery/screening ledger, the 208-work canonical table, the 135-Core challenge-relation table, and reviewer/adjudication provenance needed to regenerate the v2 aggregate snapshot independently. Until those files are committed and tagged, the legacy v1 audit must not be used to validate current manuscript counts.

## Legacy v1 catalog and audit

The repository previously organized a 50-record catalog and a 40-record single-coded diagnostic audit around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness. Those files remain available to preserve the project history and should be treated as **legacy v1 artifacts**.

They are not the taxonomy or denominator used by the current challenge-centered manuscript.

## Associated manuscript

- **Title:** Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey
- **Authors:** Yuqing Luo, Kai Zhang, and Heli Yang
- **Affiliation:** University of Science and Technology of China
- **Target venue:** ACM Transactions on Information Systems (TOIS)
- **Review cutoff:** August 9, 2026

The repository does not contain an ACM Version of Record. Publisher DOI, volume, issue, and page metadata should be added only after assignment.

## Citation

Until final publisher metadata exists, cite the manuscript as:

```bibtex
@article{luo2026resolving,
  author = {Yuqing Luo and Kai Zhang and Heli Yang},
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