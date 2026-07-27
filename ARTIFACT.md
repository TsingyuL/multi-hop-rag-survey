# Artifact readiness

This is a survey companion, not a benchmark submission or a claim of independently reproduced experimental results. It nevertheless follows the artifact-oriented practices relevant to an ACM-style public companion: clear scope, permanent-source metadata, current figure source, catalog schemas, and automated catalog checks.

## Included artifacts

| Artifact | Location | Verification |
| --- | --- | --- |
| Manuscript draft | [`MH_survey.pdf`](MH_survey.pdf) | Open the PDF and compare its title and figure references |
| Figure 1 source | [`mh_figures/source/F1_evidence_chain_v7.tex`](mh_figures/source/F1_evidence_chain_v7.tex) | Run the rebuild command in [`mh_figures/README.md`](mh_figures/README.md) |
| Survey catalog | [`taxonomy/`](taxonomy) | Run `python3 scripts/validate_catalog.py` |
| Frozen reporting audit | [`docs/quantitative_audit.md`](docs/quantitative_audit.md) | Compare counts against `taxonomy/methods.csv` status labels |

## Reproducibility boundary

The catalog supports inspection and extension of the survey taxonomy. It does not redistribute third-party datasets, model weights, or publisher PDFs, and it does not claim that every result cited in the manuscript can be rerun from this repository.

## Release practice

Create a GitHub release and archive it through a DOI-minting service (for example, Zenodo) for each manuscript revision. Add the resulting DOI to `CITATION.cff`; only add the final ACM DOI and venue metadata after they are assigned.
