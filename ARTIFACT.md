# Artifact readiness

This is the artifact note for the paper repository, not a benchmark submission or a claim of independently reproduced experimental results. The repository is centered on the current manuscript source and PDF, with a small companion taxonomy artifact that supports the survey's reporting audit.

## Included artifacts

| Artifact | Location | Verification |
| --- | --- | --- |
| Manuscript draft | [`MH_survey.pdf`](MH_survey.pdf) | Open the PDF and compare its title and figure references |
| Manuscript source | [`paper/main.tex`](paper/main.tex) | Run `latexmk -pdf -outdir=paper/build paper/main.tex` |
| Figure 1 source | [`paper/figs/fig1_evidence_chain_v3.tex`](paper/figs/fig1_evidence_chain_v3.tex) | Compare with [`paper/figs/fig1_evidence_chain_v3.pdf`](paper/figs/fig1_evidence_chain_v3.pdf) |
| Survey catalog | [`taxonomy/`](taxonomy) | Run `python3 scripts/validate_catalog.py` |
| Frozen reporting audit | [`docs/quantitative_audit.md`](docs/quantitative_audit.md) | Compare counts against `taxonomy/methods.csv` status labels |

## Reproducibility boundary

The catalog supports inspection and extension of the survey taxonomy. It does not redistribute third-party datasets, model weights, or publisher PDFs, and it does not claim that every result cited in the manuscript can be rerun from this repository.

## Release practice

Create a GitHub release and archive it through a DOI-minting service (for example, Zenodo) for each manuscript revision. Add the resulting DOI to `CITATION.cff`; only add the final ACM DOI and venue metadata after they are assigned.
