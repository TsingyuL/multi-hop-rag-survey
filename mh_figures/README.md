# Multi-Hop RAG Survey Figure Package

This directory contains the current Figure 1 assets for the survey *Multi-Hop Retrieval-Augmented Generation through the Lens of Evidence Chains: A Diagnostic Survey*.

## Folders

- `pdf/F1_latent_chain_pipeline.pdf`: vector PDF used by the manuscript.
- `F1_evidence_chain_v7.png`: README preview of the current diagram.
- `source/F1_evidence_chain_v7.tex`: LaTeX/TikZ source for the current diagram.

## Visual grammar

- Observability: blue
- Selection preservation: green
- Exposure / ordering: orange
- Fusion: purple
- Faithfulness: red
- Latent chain elements: dashed gray boxes
- Observable system artifacts: solid boxes

## Rebuild Figure 1

From the repository root, regenerate the Figure 1 PDF with LaTeX:

```bash
latexmk -pdf -outdir=mh_figures/pdf mh_figures/source/F1_evidence_chain_v7.tex
```

The committed `MH_survey.pdf` already includes the current rendered figure.
