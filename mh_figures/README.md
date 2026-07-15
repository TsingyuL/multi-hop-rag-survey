# Multi-Hop RAG Survey Figure Package

This package contains 10 vector figures for the survey *Multi-Hop Retrieval-Augmented Reasoning: A Latent Evidence-Chain Inference Perspective*.

## Folders

- `pdf/`: vector PDFs for LaTeX `\includegraphics`.
- `pdf/`: committed vector PDFs used by the manuscript.
- `svg/`: editable vector versions, generated locally when needed.
- `png/`: high-resolution previews, generated locally when needed.
- `source/make_figures.py`: Python source used to regenerate individual figures.
- `rendered_pdf_contact_sheet.png`: render-verified preview of the merged PDF.

## Visual grammar

- Observability: blue
- Selection preservation: green (conditional utility may appear only as a mechanism-level score)
- Exposure / ordering: orange
- Fusion: purple
- Faithfulness: red
- Latent chain elements: dashed gray boxes
- Observable system artifacts: solid boxes

## Rebuild

From the repository root, install the figure dependencies and regenerate the individual figure files:

```bash
python3 -m pip install -r mh_figures/requirements.txt
python3 mh_figures/source/make_figures.py
```

The generator writes to this directory, not to a machine-specific temporary path.

## Recommended LaTeX usage

Copy `pdf/` into your project as `figures/`, then update the paths in `latex/figures.tex` from `pdf/...` to `figures/...` if needed.
