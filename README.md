# Multi-Hop Retrieval-Augmented Generation through Evidence Chains

> **A diagnostic survey of multi-hop RAG through evidence-chain events.**

[![Paper](https://img.shields.io/badge/paper-PDF-B31B1B.svg)](MH_survey.pdf)
[![License: MIT](https://img.shields.io/badge/code%20%26%20catalog-MIT-green.svg)](LICENSE)
[![ACM template](https://img.shields.io/badge/typeset%20with-acmart-00629B.svg)](MH_survey.pdf)

This is the paper repository for **“Multi-Hop Retrieval-Augmented Generation through the Lens of Evidence Chains: A Diagnostic Survey.”** It contains the current manuscript PDF, LaTeX source, figure source, and the companion taxonomy artifact used to audit the survey's evidence-chain claims.

The taxonomy pages in [`docs/`](docs/) are supporting material for the manuscript. They are kept intentionally small and versioned with the paper, so the repository has one current public version rather than a separate catalog site.

The paper frames end-to-end success as five coupled bottlenecks:

| Evidence-chain target | Question it asks |
| --- | --- |
| **Observability** | Does the retrieved pool contain the needed support chain? |
| **Selection preservation** | Does budgeted selection preserve a valid evidence chain? |
| **Exposure** | Is the evidence accessible to the reader at the point of use? |
| **Fusion reliability** | Can the reader compose the evidence correctly? |
| **Causal faithfulness** | Did the generated answer actually depend on the evidence? |

![Evidence-chain diagnostic diagram](paper/figs/fig1_evidence_chain_v3.png)

## Paper

- [Read the manuscript (PDF)](MH_survey.pdf)
- [Read the manuscript source](paper/main.tex)
- Authors: Yuqing Luo and Kai Zhang, University of Science and Technology of China
- Venue status: author manuscript draft, typeset with the ACM `acmart` class.

> The PDF currently contains placeholder publication metadata (including the DOI). It is **not** the ACM Version of Record. Replace this notice, the citation metadata, and any DOI links only after the publisher supplies the final bibliographic record.

## What is in this repository

```text
.
├── MH_survey.pdf                  # compiled manuscript draft
├── paper/                         # LaTeX source, bibliography snapshot, and figures
│   ├── main.tex
│   ├── main_TOIS_verified.bbl
│   └── figs/
├── taxonomy/                      # machine-readable companion artifact
├── docs/                          # taxonomy guide, audit notes, and catalog preview
├── scripts/                       # artifact validation and catalog-page builder
├── CITATION.cff                   # GitHub citation metadata
├── CONTRIBUTING.md                # how to propose catalog updates
└── LICENSE                        # license for repository-authored materials
```

The repository keeps one current manuscript and one current companion artifact. The current catalog contains **23 method records**, **6 benchmark records**, and **27 intervention mappings**; the manuscript's frozen quantitative audit uses the **20 source-verified method records** and excludes seeded or needs-review entries. This distinction is deliberate: coverage should not be confused with a taxonomy judgment.

| File | Contents |
| --- | --- |
| [`taxonomy/methods.csv`](taxonomy/methods.csv) | Methods and analyses, tagged by architectural family and primary evidence-chain target |
| [`taxonomy/benchmarks.csv`](taxonomy/benchmarks.csv) | Benchmarks, observed diagnostics, and evaluation cautions |
| [`taxonomy/pipeline_mapping.csv`](taxonomy/pipeline_mapping.csv) | Which pipeline stage and evidence-chain target a method affects |
| [`taxonomy/reading_list.bib`](taxonomy/reading_list.bib) | BibTeX entries for catalogued work |
| [`docs/index.html`](docs/index.html) | Filterable companion-catalog preview, automatically built from the CSV catalog |
| [`docs/coverage_protocol.md`](docs/coverage_protocol.md) | Scope, discovery, verification, and correction rules |
| [`taxonomy/discovery_queries.csv`](taxonomy/discovery_queries.csv) | Reproducible query families for maintaining a separate unreviewed candidate queue |
| [`docs/quantitative_audit.md`](docs/quantitative_audit.md) | Frozen seed counts used by the manuscript reporting audit |

## Build and validate

Build the manuscript from the checked-in source:

```bash
latexmk -pdf -outdir=paper/build paper/main.tex
```

Validate the companion artifact:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_catalog_site.py
```

## Literature Navigator

The catalog is designed as a manuscript companion, not as an unstructured paper list. Start from either the bottleneck you want to solve or the system design you want to study:

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

## Start here

1. Read [the taxonomy guide](docs/taxonomy.md) for the dual-axis annotation rules.
2. Browse the catalog files above, or filter them in a spreadsheet/dataframe.
3. Use the [reporting checklist](docs/reporting_checklist.md) when evaluating a multi-hop RAG system.
4. See [the roadmap](docs/roadmap.md) for planned catalog coverage and releases.

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
  title   = {Multi-Hop Retrieval-Augmented Generation through the Lens of Evidence Chains: A Diagnostic Survey},
  year    = {2026},
  note    = {Manuscript draft. Repository companion: https://github.com/TsingyuL/multi-hop-rag-survey}
}
```

Please update both this entry and [`CITATION.cff`](CITATION.cff) from the publisher's final metadata when available.

## License and attribution

The repository-authored catalog, documentation, and utility code are released under the [MIT License](LICENSE). The manuscript and figures remain © 2026 Yuqing Luo, subject to the rights and publication terms shown in the manuscript. Do not treat the repository license as permission to redistribute a publisher's Version of Record.
