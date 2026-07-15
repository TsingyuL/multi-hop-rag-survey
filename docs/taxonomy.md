# Taxonomy guide

The survey uses two complementary labels. The **estimand axis** captures the latent quantity a work tries to improve; the **architectural axis** captures how it does so. Neither label is a quality judgment.

## Controlled vocabulary

| Field | Allowed values | Meaning |
| --- | --- | --- |
| `primary_estimand` | `observability`, `selection`, `exposure`, `fusion`, `faithfulness`, `joint` | The main latent-chain bottleneck targeted by the work |
| `secondary_estimands` | Semicolon-separated values above | Meaningful secondary effects |
| `mechanism_signal` | blank or `conditional_utility` | Optional mechanism-level score; never a top-level estimand |
| `architectural_family` | `retrieval`, `graph_kg`, `decomposition`, `fusion_reader`, `llm_reasoning`, `agentic`, `hybrid`, `benchmark`, `analysis` | The work's primary surface design |
| `evidence_source` | `text`, `knowledge_graph`, `table`, `multimodal`, `hybrid` | Evidence substrate |
| `pipeline_stage` | `retrieve`, `select`, `order`, `read_fuse`, `verify`, `end_to_end` | Primary intervention point |
| `venue` | Free text | Venue or preprint status; do not guess a final venue from an arXiv record. |
| `tasks` / `task_type` | Semicolon-separated free text | Evaluation task(s), written at a useful comparison granularity. |
| `datasets` | Semicolon-separated catalog names | Method evaluation datasets. |
| `hops` | Free text | Benchmark hop range or `varied` when no single range applies. |
| `code_url` / `data_url` | HTTPS URL or blank `code_url` | Verified official implementation or dataset homepage; leave `code_url` blank when none is verified. |

## Estimand definitions

- **Observability**: increases the chance that every required support unit appears in the retrieved pool.
- **Selection**: preserves the complete support chain under a context, cost, or ranking budget.
- **Exposure**: makes selected support available at the reader's point of use; it includes ordering, placement, and context organization.
- **Fusion**: improves correct composition across evidence units conditional on their availability.
- **Faithfulness**: establishes or improves the causal use of supporting evidence, rather than merely producing a plausible rationale or citation.
- **Joint**: intentionally optimizes multiple bottlenecks without a defensible single primary target.

## Annotation procedure

1. State the paper's claimed intervention in one sentence.
2. Select the pipeline stage where that intervention is applied.
3. Select the primary estimand: the earliest latent bottleneck the central mechanism is intended to affect.
4. Add secondary estimands only where the paper supplies an explicit mechanism or evaluation.
5. Record the benchmark, persistent source URL, and any caveat that limits comparison.

For example, iterative retrieval that expands a pool after resolving a bridge entity is primarily `observability`, even if it also reranks results. A reader that changes attention across already-selected passages is primarily `fusion`; it should not be tagged `observability` merely because better answers may correlate with recall.

Conditional evidence utility may be recorded as `mechanism_signal=conditional_utility` when a method uses it to rank, compress, or retain evidence. It is not valid in `primary_estimand` or `secondary_estimands` because the paper treats it as a mechanism for improving selection preservation, not as an additional probability factor.

## Data conventions

- CSV uses UTF-8 and a header row. Semicolon separates values inside one field.
- `citation_key` must be unique and match an entry in `reading_list.bib`.
- `year` is a four-digit publication/preprint year.
- `source_url` should be a durable landing page (DOI, ACL Anthology, arXiv abstract, or publisher page).
- `code_url` is optional, but must point to an official or author-maintained implementation when present. Do not substitute an unrelated reimplementation.
- Every method must have at least one entry in `pipeline_mapping.csv`; this forces an intervention and diagnostic to be stated explicitly.
- `status` is one of `seeded`, `reviewed`, or `needs_review`.

The seeded rows are examples and starting points—not a claim that the catalog is complete. New additions should follow the same annotation process.
