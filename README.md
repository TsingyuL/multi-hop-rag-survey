# Multi-Hop RAG Research Hub

> **A curated companion hub for multi-hop retrieval-augmented generation through evidence-chain events.**

[![Catalog](https://img.shields.io/badge/catalog-static%20site-2457C5.svg)](docs/index.html)
[![Artifact](https://img.shields.io/badge/artifact-validated-087E8B.svg)](ARTIFACT.md)
[![License: MIT](https://img.shields.io/badge/code%20%26%20catalog-MIT-green.svg)](LICENSE)

This repository is the public research hub cited by the manuscript **“Multi-Hop Retrieval-Augmented Generation through the Lens of Latent Evidence-Chain Inference: A Diagnostic Survey.”** It keeps the survey's machine-readable taxonomy, reviewed method and benchmark records, quantitative reporting audit, current Figure 1 asset, and validation scripts in one place.

The manuscript source is maintained outside this hub. This repository exists so readers can inspect, reproduce, and extend the evidence-chain catalog behind the survey claims.

## Start here

| Need | Open |
| --- | --- |
| Browse the reviewed catalog | [`docs/index.html`](docs/index.html) |
| Inspect machine-readable records | [`taxonomy/methods.csv`](taxonomy/methods.csv), [`taxonomy/benchmarks.csv`](taxonomy/benchmarks.csv), [`taxonomy/pipeline_mapping.csv`](taxonomy/pipeline_mapping.csv) |
| Inspect the frozen 40-record audit | [`taxonomy/audit_records.csv`](taxonomy/audit_records.csv), [`taxonomy/audit_codebook_v1.md`](taxonomy/audit_codebook_v1.md) |
| Check coding rules | [`docs/taxonomy.md`](docs/taxonomy.md), [`docs/coverage_protocol.md`](docs/coverage_protocol.md) |
| Review frozen audit counts | [`docs/quantitative_audit.md`](docs/quantitative_audit.md) |
| Validate the artifact | `python3 scripts/validate_catalog.py` |

The hub keeps one current catalog instead of conflating discovery breadth with
comparative evidence. The current catalog contains **50 method records**, of
which **47 are source-reviewed**, plus **6 reviewed benchmark records** and
**51 unique intervention mappings**. The frozen comparative audit is stricter:
it contains **40 audit-eligible methods** coded under the 24-field codebook.
This distinction is deliberate: `reviewed` metadata is not automatically
audit-eligible evidence.

The frozen v1.0 audit is single-coded. Its validators reproduce schemas and
counts but do not certify semantic labels, and this release does not report an
inter-coder agreement coefficient. See the codebook's
[reliability boundary](taxonomy/audit_codebook_v1.md#reliability-and-verification-boundary).

## Evidence-chain frame

The survey organizes multi-hop RAG around five coupled bottlenecks:

| Evidence-chain target | Question it asks |
| --- | --- |
| **Observability** | Does the retrieved pool contain the needed support chain? |
| **Selection preservation** | Does budgeted selection preserve a valid evidence chain? |
| **Exposure** | Is the evidence accessible to the reader at the point of use? |
| **Fusion reliability** | Can the reader compose the evidence correctly? |
| **Causal faithfulness** | Did the generated answer actually depend on the evidence? |

[Open Figure 1 (PDF)](mh_figures/fig1.pdf)

## What is in this repository

```text
.
├── taxonomy/                      # machine-readable, community-maintained catalog
├── docs/                          # taxonomy rules, roadmap, and change log
├── mh_figures/                    # current Figure 1 PDF
├── scripts/                       # catalog utilities and validation
├── CITATION.cff                   # GitHub citation metadata
├── CONTRIBUTING.md                # how to propose catalog updates
└── LICENSE                        # license for repository-authored materials
```

| File | Contents |
| --- | --- |
| [`taxonomy/methods.csv`](taxonomy/methods.csv) | Methods and analyses, tagged by architectural family and primary evidence-chain target |
| [`taxonomy/benchmarks.csv`](taxonomy/benchmarks.csv) | Benchmarks, observed diagnostics, and evaluation cautions |
| [`taxonomy/pipeline_mapping.csv`](taxonomy/pipeline_mapping.csv) | Which pipeline stage and evidence-chain target a method affects |
| [`taxonomy/audit_records.csv`](taxonomy/audit_records.csv) | Frozen 40-record claim-and-evidence audit |
| [`taxonomy/audit_codebook_v1.md`](taxonomy/audit_codebook_v1.md) | Eligibility, 24 fields, allowed values, and counting rules |
| [`taxonomy/reading_list.bib`](taxonomy/reading_list.bib) | BibTeX entries for catalogued work |
| [`docs/index.html`](docs/index.html) | Filterable catalog interface, automatically built from the CSV catalog |
| [`docs/coverage_protocol.md`](docs/coverage_protocol.md) | Scope, discovery, verification, and correction rules |
| [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) | Reproducible query families for maintaining a separate unreviewed candidate queue |
| [`docs/quantitative_audit.md`](docs/quantitative_audit.md) | Generated counts for the frozen 40-record comparative audit |

## Literature navigator

The catalog is designed to be read as a map, not as an unstructured paper list. Start from either the bottleneck you want to solve or the system design you want to study:

| Navigate by research question | Navigate by design route |
| --- | --- |
| [Can the needed chain be found? — Observability](docs/literature_navigator.md#observability-find-the-support-chain) | [Dense / iterative retrieval](docs/literature_navigator.md#by-design-route) |
| [Which evidence survives the budget? — Selection preservation](docs/literature_navigator.md#selection-preservation-keep-a-valid-chain-under-budget) | [Graph and knowledge-grounded methods](docs/literature_navigator.md#by-design-route) |
| [Is evidence usable in context? — Exposure](docs/literature_navigator.md#exposure-make-evidence-usable-in-context) | [Reader and fusion architectures](docs/literature_navigator.md#by-design-route) |
| [Can the model compose evidence? — Fusion](docs/literature_navigator.md#fusion-compose-evidence-correctly) | [Reasoning-interleaved and agentic RAG](docs/literature_navigator.md#by-design-route) |
| [Did the answer rely on its evidence? — Faithfulness](docs/literature_navigator.md#faithfulness-and-joint-control) | [Context organization and hierarchical retrieval](docs/literature_navigator.md#by-design-route) |

- **New to multi-hop RAG?** Follow the [foundation-to-agentic reading path](docs/literature_navigator.md#suggested-reading-paths).
- **Looking for a specific paper?** Use the [chronological index](docs/literature_navigator.md#chronological-index) or open the machine-readable [methods catalog](taxonomy/methods.csv).
- **Adding a paper?** Follow the [annotation rules](docs/taxonomy.md) and [contribution guide](CONTRIBUTING.md).

## Associated manuscript

- Title: **Multi-Hop Retrieval-Augmented Generation through the Lens of Latent Evidence-Chain Inference: A Diagnostic Survey**
- Authors: Yuqing Luo and Kai Zhang, University of Science and Technology of China
- Venue status: author manuscript draft, typeset with the ACM `acmart` class.

> The submission manuscript is maintained separately from this evidence
> artifact. This repository does not contain an ACM Version of Record. Update
> citation metadata and DOI links only after the publisher supplies the final
> bibliographic record.

## Scope

We cover retrieval-grounded multi-hop reasoning over text, knowledge graphs, tables, and hybrid sources. The repository includes foundational components when they materially affect multi-hop evidence acquisition, selection, ordering, fusion, or verification. It does not aim to be a general survey of single-hop retrieval or general-purpose agents.

## Contributing

Corrections and additions are welcome, particularly newly published methods, overlooked benchmarks, reproducibility links, and taxonomy disagreements. Please follow [CONTRIBUTING.md](CONTRIBUTING.md), provide a stable paper URL or DOI, and explain the proposed evidence-chain target label.

For substantial taxonomy changes, open an issue first so that labels remain comparable across entries.

## Citation

Until a DOI and final venue record exist, cite this work as an unpublished manuscript:

```bibtex
@article{luo2026multihopragsurvey,
  author  = {Yuqing Luo and Kai Zhang},
  title   = {Multi-Hop Retrieval-Augmented Generation through the Lens of Latent Evidence-Chain Inference: A Diagnostic Survey},
  year    = {2026},
  note    = {Manuscript draft. Repository companion: https://github.com/TsingyuL/multi-hop-rag-survey}
}
```

Please update both this entry and [`CITATION.cff`](CITATION.cff) from the publisher's final metadata when available.

## License and attribution

The repository-authored catalog, documentation, and utility code are released under the [MIT License](LICENSE). The manuscript and figures remain © 2026 Yuqing Luo, subject to the rights and publication terms shown in the manuscript. Do not treat the repository license as permission to redistribute a publisher's Version of Record.
