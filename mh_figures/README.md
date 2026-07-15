# Multi-Hop RAG Survey Figures

This package contains the figure PDFs used by the current manuscript
*Multi-Hop Retrieval-Augmented Generation as Latent Evidence-Chain Inference:
A Survey*.

## Folders

- `pdf/`: committed vector PDFs used by the manuscript (`fig1.pdf`,
  `fig2.pdf`, `fig3.pdf`, `fig4.pdf`, and `fig9.pdf`).
- `rendered_pdf_contact_sheet.png`: render-verified preview of the current
  committed figures.

## Visual grammar

- Observability: blue
- Selection: green
- Exposure / ordering: orange
- Fusion: purple
- Faithfulness: red
- Latent chain elements: dashed gray boxes
- Observable system artifacts: solid boxes

## Rebuild

The canonical figure sources live in the manuscript project. Copy the current
`fig*.pdf` outputs into `mh_figures/pdf/`, then regenerate
`rendered_pdf_contact_sheet.png` from those PDFs.

## Recommended LaTeX usage

Copy `pdf/` into your project as `figures/`, then include the relevant files
with LaTeX `\includegraphics`.
