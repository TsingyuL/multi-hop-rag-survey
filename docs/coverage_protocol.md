# Coverage and curation protocol

## Purpose and claim boundary

This repository is a **living, curated evidence map** for multi-hop retrieval-augmented reasoning. It is not a registered systematic review and does not make a PRISMA-style claim of exhaustive retrieval. In particular, an absent paper should never be interpreted as evidence that the paper is irrelevant or low quality.

The protocol exists so readers can distinguish three things that are often conflated in survey repositories: scope, metadata verification, and interpretive taxonomy labels.

## Scope

An entry is in scope when it makes a material contribution to at least one of these stages in retrieval-grounded multi-hop reasoning:

1. finding a multi-step support chain in an external corpus, knowledge graph, table, or hybrid source;
2. selecting, ordering, or compressing that evidence under a budget;
3. composing evidence to answer or verify a multi-step query; or
4. testing or improving whether the output causally uses the retrieved evidence.

Foundational single-hop retrieval and general agent papers are included only when they provide a concrete mechanism, benchmark, or evaluation setting that directly informs this scope. Purely parametric chain-of-thought work is out of scope unless it performs external evidence access.

## Discovery sources and query families

The seed catalog was assembled from canonical landing pages at ACL Anthology, OpenReview, arXiv, venue proceedings, and official project repositories. Updates should search more than one source where possible.

Suggested query families:

- `"multi-hop" AND (retrieval OR RAG OR "open-domain QA")`
- `("iterative retrieval" OR "multi-step retrieval" OR "reasoning path") AND question answering`
- `("evidence chain" OR "supporting facts") AND (retrieval OR reasoning)`
- benchmark names such as `HotpotQA`, `2WikiMultiHopQA`, `MuSiQue`, `HoVer`, and `QASC` combined with retrieval terms.

The tracked [`discovery_queries.csv`](../taxonomy/discovery_queries.csv) makes these query families executable. Run `python3 scripts/refresh_discovery_queue.py` to create a separate `discovery_queue.csv`; it is intentionally not merged into the reviewed catalog automatically. Public scholarly APIs may rate-limit unauthenticated bulk refreshes, so a failed refresh must be retried rather than treated as zero results.

Searches should be recorded in the pull request or issue that motivates a substantial coverage update. The current seed collection was last curated on **2026-07-11**.

## Required record evidence

Every method entry must contain:

| Field | Curation rule |
| --- | --- |
| Canonical title, year, venue | Check against a publisher, proceedings, ACL Anthology, OpenReview, or arXiv landing page. |
| `source_url` | Use a stable landing page rather than a direct PDF whenever possible. |
| Task and datasets | Record the paper’s evaluation setting; do not infer a dataset from a citation alone. |
| Taxonomy labels | Assign using the [taxonomy guide](taxonomy.md), and state a concrete intervention in `pipeline_mapping.csv`. |
| Code or data URL | Link only author-maintained or official resources. An empty `code_url` means no official link was verified, not that no implementation exists. |

## Review status

- `seeded`: a starter record that meets the schema but may need independent cross-checking or broader contextual review.
- `reviewed`: metadata, canonical link, primary taxonomy label, and at least one pipeline mapping were checked against the paper or official project page.
- `needs_review`: useful candidate whose placement or scope needs explicit verification before comparative claims rely on it.

`reviewed` does not certify experimental reproducibility, correctness of every result, or superiority over other work.

## Imported full library

[`library_papers.csv`](../taxonomy/library_papers.csv) is a deduplicated public import of the project's working literature library. It preserves the workbook's original folders in `library_categories`, including broad adjacent areas such as CoT, agentic systems, and surveys. It must not be read as a list of papers that all meet the narrow multi-hop RAG scope. The private source workbook is not committed; a maintainer who has an updated workbook can rebuild the public import with:

```bash
python3 -m pip install -r scripts/requirements.txt
python3 scripts/import_library.py --input /path/to/MH_QA_Library.xlsx
python3 scripts/validate_catalog.py
python3 scripts/build_catalog_site.py
```

- `imported` means metadata was carried over from the working library and still needs per-record verification before being promoted to the reviewed catalog.
- `needs_triage` marks records that were flagged as misclassified or suggested for cleanup in the source library.

The two layers make the hub useful for broad discovery without weakening the validity of comparative claims in the reviewed taxonomy.

## Taxonomy adjudication

The catalog labels the **earliest primary bottleneck deliberately targeted by the central mechanism**, not every metric that improves in an experiment. When a label is genuinely ambiguous, retain the primary label only if the rationale is defensible and use `secondary_estimands` for material downstream effects. Discuss new categories or contested labels in an issue before merging.

## Update and correction policy

1. Add the catalog row, BibTeX key, and pipeline mapping in the same change.
2. Run `python3 scripts/validate_catalog.py` and `python3 scripts/build_catalog_site.py`.
3. Update the reading paths only when a new work changes the recommended conceptual route; do not turn the guide into a leaderboard.
4. For factual corrections, open an issue or pull request with the authoritative URL. Corrections are preferred over silent deletion; summarize material changes in the [change log](changelog.md).

This protocol deliberately favors auditable coverage over inflated paper counts.
