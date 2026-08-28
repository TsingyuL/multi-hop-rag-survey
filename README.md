# Multi-Hop RAG Research Hub

> Public companion for **“Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment.”**

[![Manuscript](https://img.shields.io/badge/manuscript-TOIS%20draft-2457C5.svg)](#associated-manuscript)
[![Research hub](https://img.shields.io/badge/research%20hub-open-2457C5.svg)](https://tsingyul.github.io/multi-hop-rag-survey/)
[![Corpus](https://img.shields.io/badge/frozen%20corpus-274%20papers-087E8B.svg)](#current-manuscript-snapshot)
[![License: MIT](https://img.shields.io/badge/code%20%26%20catalog-MIT-green.svg)](LICENSE)

This repository is the paper-aligned research hub for a survey of multi-hop retrieval-augmented generation defined by **evidence dependency**. The manuscript uses a layered organization:

1. **Evidence dependency** defines what makes an evidence process genuinely multi-hop.
2. **Process organization** retains established retrieval–reasoning method families.
3. **Knowledge-access conditions** describe the external representation, acquisition interface, and source regime used along dependent hops.
4. **Evaluation alignment** asks whether the resulting intermediate decisions are directly measured.

The current manuscript does **not** claim that prior process taxonomies are obsolete, that heterogeneous/tool-mediated access is dominant, or that the full-corpus percentages are reliability-validated population estimates.

## Start here

| Need | Open |
| --- | --- |
| Paper-to-hub map | [`docs/paper_hub.md`](docs/paper_hub.md) |
| Current submission alignment | [`docs/submission_alignment_v10.md`](docs/submission_alignment_v10.md) |
| Discovery and coverage protocol | [`docs/coverage_protocol.md`](docs/coverage_protocol.md) |
| Executable discovery queries | [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) |
| Adjacent-survey reference library | [`literature/README.md`](literature/README.md) |
| Artifact status and limitations | [`ARTIFACT.md`](ARTIFACT.md) |
| Historical challenge-centered materials | [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md), [`taxonomy/audit_v2/`](taxonomy/audit_v2/) |

## Current manuscript snapshot

The frozen canonical frame contains **274 papers** with review cutoff **August 5, 2026**:

- **149 CORE**
- **57 SUPPORTING**
- **68 TRANSFER**

The current corpus-level analysis is a **structured evidence map**, not a registered systematic review or statistical meta-analysis. The final 274-paper expansion does not have a complete per-database raw-hit ledger that supports a PRISMA-style flow; historical `452 → … → 208` screening counts belong to an earlier challenge-centered snapshot and are retained only as project provenance.

For the revised knowledge-access analysis:

- 170 CORE or SUPPORTING papers are retrieval-bearing;
- 111 have acquisition dependency;
- 139/170 (81.8%) use text-only external evidence;
- 160/170 (94.1%) use fixed/closed sources;
- 99/111 (89.2%) remain access-stable across dependent hops;
- nine papers form the state-dependent routing / transition-capable subset.

A targeted primary-source recheck of those nine routing cases finds that direct intermediate access-decision diagnostics are **uncommon, not absent**: one paper directly evaluates route/program correctness, and two directly evaluate either the route/program or an upstream selector/gating state controlling subsequent access.

## Scope

The survey distinguishes two dependency types:

- **Acquisition dependency:** evidence obtained earlier materially changes a later external acquisition target or action.
- **Reasoning dependency:** answering requires a substantive operation across multiple external evidence units.

Repeated retrieval, multiple documents, or internal search over already supplied context does not by itself establish multi-hop RAG.

## Evidence and reliability boundary

Primary-source coding records source URLs and evidence notes for analytical claims. The broader fine-grained coding schema underwent blinded reliability attempts, but the confirmatory reliability gate did **not** meet the pre-specified threshold. Accordingly:

- full-corpus percentages are reported as **descriptive, evidence-backed mappings** rather than reliability-validated prevalence estimates;
- coarse knowledge-access descriptors are used for the revised synthesis;
- high-leverage routing/evaluation claims are supported by targeted paper-by-paper primary-source rechecking.

This limitation is reported explicitly in the manuscript and should not be replaced by claims of fully adjudicated independent double coding.

## Historical challenge-centered snapshot

Files under `taxonomy/audit_v2/`, the five-challenge codebook, and related challenge-centered documentation describe an **earlier manuscript snapshot** based on 208 works. They remain in the repository for provenance and may support historical comparison, but they are **not** the denominator, taxonomy, or empirical claim set used by the current layered manuscript.

## Public artifact boundary

The submission-ready artifact should freeze the exact 274-paper canonical frame, the coarse knowledge-access mapping, the nine-case routing-evaluation recheck, executable query strings, and scripts or generated outputs used for manuscript tables and figures. See [`ARTIFACT.md`](ARTIFACT.md) for the current completeness statement.

## Associated manuscript

- **Title:** Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment
- **Authors:** Yuqing Luo, Kai Zhang, and Liyang He
- **Affiliation:** University of Science and Technology of China
- **Target venue:** ACM Transactions on Information Systems (TOIS)
- **Review cutoff:** August 5, 2026

The manuscript source is maintained outside this repository. Publisher DOI, volume, issue, and page metadata should be added only after assignment.

## Citation

Until final publisher metadata exists, cite the manuscript as:

```bibtex
@article{luo2026multihoprag,
  author = {Yuqing Luo and Kai Zhang and Liyang He},
  title  = {Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment},
  year   = {2026},
  note   = {Manuscript draft. Companion repository: https://github.com/TsingyuL/multi-hop-rag-survey}
}
```

See [`CITATION.cff`](CITATION.cff) for GitHub citation metadata.

## License and attribution

Repository-authored catalog data, documentation, and utility code are released under the [MIT License](LICENSE). The manuscript and figures remain subject to the authors' publication and publisher terms.
