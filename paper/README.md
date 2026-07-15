# Manuscript source

This directory is the buildable source for *Multi-Hop Retrieval-Augmented Generation as Latent Evidence-Chain Inference: A Survey*.

## Build

```bash
latexmk -pdf -halt-on-error main.tex
```

Run repository checks from the repository root:

```bash
python3 scripts/check_manuscript.py --bib paper/references.bib --log paper/main.log
```

The paper uses `figures/fig1.pdf` through `figures/fig5.pdf`. Their reproducible source is `../mh_figures/source/make_figures.py`; the fifth manuscript figure is the simplified benchmark-estimand heatmap generated as `F9_benchmark_estimand_alignment.pdf` in the broader ten-figure package.

The repository MIT license covers repository-authored code, catalog data, and documentation only. It does not apply to the manuscript or figures.
