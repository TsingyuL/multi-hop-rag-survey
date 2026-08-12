# Seven-survey reference library

[`reference_library.xlsx`](reference_library.xlsx) consolidates the reference
lists of seven adjacent surveys on multi-hop question answering, RAG and
reasoning, reasoning-intensive retrieval, and agentic RAG.

## Snapshot

| Quantity | Count |
| --- | ---: |
| Source surveys | 7 |
| Raw citation records | 886 |
| Deduplicated papers | 771 |
| Papers cited by at least two surveys | 75 |
| Papers cited by at least three surveys | 16 |

The workbook contains five sheets:

| Sheet | Purpose |
| --- | --- |
| `README` | Scope, reconstruction notes, and the seven source surveys |
| `All References` | One row per source-survey citation record, preserving the raw reference text |
| `Deduplicated` | Canonicalized paper records with per-survey presence indicators |
| `Core Overlap` | The 75 papers cited by at least two surveys |
| `Survey Summary` | Per-survey coverage and pairwise overlap counts |

## Deduplication and parsing

Records are matched in the following order: arXiv identifier, DOI, normalized
title and year, then an exact normalized-title merge as a second pass. Parsed
titles, authors, venues, and identifiers are best-effort reconstructions from
survey PDFs. The source citation text is retained in `Raw Reference` so that a
reader can audit or correct the parse.

## Interpretation boundary

This workbook is a **discovery and cross-survey reference layer**. It is not the
manuscript's frozen 208-work evidence map and must not be used as the denominator
for challenge prevalence or overlap claims.

In particular:

- presence in the workbook means that at least one source survey cited the work;
- deduplication does not establish primary-source review or scope eligibility;
- the `Relevance` field in overlap views is an open review field, not a completed
  challenge label; and
- manuscript-level counts must come from the reviewed evidence map and the v2
  challenge codebook, not from this workbook.

Use the workbook to expand discovery, compare prior-survey coverage, and identify
high-overlap candidates for later primary-source review.
