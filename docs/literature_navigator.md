# Literature navigator

This page is a curated entry point to the survey catalog. It is intentionally a **seeded guide**, rather than a claim of complete coverage. Each title links to its canonical paper landing page; the complete, machine-readable metadata lives in [`taxonomy/methods.csv`](../taxonomy/methods.csv).

## How to use this map

Choose a row below when you have a research question in mind; choose a design route when you are comparing systems. A paper can affect more than one bottleneck, but it appears under the primary estimand used in this survey's controlled taxonomy. See the [taxonomy guide](taxonomy.md) for the annotation rationale.

## By research question

### 1. Observability: find the support chain

Work in this group aims to increase the chance that all required evidence reaches the retrieved pool.

- [GRAFT-Net (2018)](https://aclanthology.org/D18-1455/) — graph retrieval and evidence composition across text and knowledge bases.
- [PullNet (2019)](https://aclanthology.org/D19-1242/) — iteratively expands a question-specific graph over text and knowledge bases.
- [MDR (2021)](https://aclanthology.org/2021.naacl-main.424/) — dense retrieval trained for multi-hop evidence acquisition.
- [IRCoT (2023)](https://aclanthology.org/2023.acl-long.557/) — alternates generated reasoning steps with retrieval.
- [FLARE (2023)](https://arxiv.org/abs/2305.06983) — triggers retrieval during generation when uncertainty is high.

### 2. Utility: keep useful evidence under a budget

These papers target the selection or ranking of evidence when retrieval, context length, or computation is limited.

- [PullNet (2019)](https://aclanthology.org/D19-1242/) — evidence expansion guided by the evolving graph.
- [MDR (2021)](https://aclanthology.org/2021.naacl-main.424/) — multi-hop dense retrieval objective.
- [IRCoT (2023)](https://aclanthology.org/2023.acl-long.557/) — intermediate reasoning conditions the next retrieval step.
- [FLARE (2023)](https://arxiv.org/abs/2305.06983) — retrieval is adaptively invoked during generation.

### 3. Exposure: make evidence available to the reader

Exposure concerns how selected evidence is organized and presented at the point of use.

- [RAPTOR (2024)](https://arxiv.org/abs/2401.18059) — hierarchical summaries and tree-organized retrieval change the granularity and ordering of available context.

### 4. Fusion: compose evidence correctly

These systems focus on combining information across passages or graph nodes after it has been retrieved.

- [GRAFT-Net (2018)](https://aclanthology.org/D18-1455/) — graph-based composition over heterogeneous evidence.
- [Fusion-in-Decoder (2021)](https://arxiv.org/abs/2007.01282) — decoder-side fusion of independently encoded retrieved passages.

### 5. Faithfulness: test causal evidence use

Faithfulness asks whether the final answer actually depends on the cited or retrieved support, not merely whether it is plausible.

- [Self-RAG (2023)](https://arxiv.org/abs/2310.11511) — jointly learns retrieval, generation, and self-critique; its catalog entry is intentionally labeled `joint` because it targets several bottlenecks.

## By design route

### 1. Retrieval

- [MDR (2021)](https://aclanthology.org/2021.naacl-main.424/)
- [RAPTOR (2024)](https://arxiv.org/abs/2401.18059)

### 2. Graph & knowledge-grounded methods

- [GRAFT-Net (2018)](https://aclanthology.org/D18-1455/)
- [PullNet (2019)](https://aclanthology.org/D19-1242/)

### 3. Reader & fusion architectures

- [Fusion-in-Decoder (2021)](https://arxiv.org/abs/2007.01282)

### 4. Reasoning-interleaved & agentic RAG

- [IRCoT (2023)](https://aclanthology.org/2023.acl-long.557/)
- [FLARE (2023)](https://arxiv.org/abs/2305.06983)
- [Self-RAG (2023)](https://arxiv.org/abs/2310.11511)

### 5. Context organization

- [RAPTOR (2024)](https://arxiv.org/abs/2401.18059)

## Suggested reading paths

| Goal | Suggested sequence | Why this sequence |
| --- | --- | --- |
| Learn the foundations | GRAFT-Net → PullNet → MDR → Fusion-in-Decoder | Moves from heterogeneous graph retrieval to dense retrieval and neural evidence fusion. |
| Build an iterative RAG system | MDR → IRCoT → FLARE → Self-RAG | Adds retrieval-reasoning interleaving, adaptive retrieval, and self-reflection in stages. |
| Study long-context design | Fusion-in-Decoder → RAPTOR → Self-RAG | Compares passage fusion, hierarchical context organization, and reflective control. |

## Chronological index

| Year | Paper | Route | Primary bottleneck |
| --- | --- | --- | --- |
| 2018 | [GRAFT-Net](https://aclanthology.org/D18-1455/) | Graph / KG | Observability |
| 2019 | [PullNet](https://aclanthology.org/D19-1242/) | Graph / KG | Observability |
| 2021 | [Fusion-in-Decoder](https://arxiv.org/abs/2007.01282) | Reader / fusion | Fusion |
| 2021 | [MDR](https://aclanthology.org/2021.naacl-main.424/) | Retrieval | Observability |
| 2023 | [IRCoT](https://aclanthology.org/2023.acl-long.557/) | Reasoning-interleaved | Observability |
| 2023 | [FLARE](https://arxiv.org/abs/2305.06983) | Agentic | Observability |
| 2023 | [Self-RAG](https://arxiv.org/abs/2310.11511) | Agentic | Joint |
| 2024 | [RAPTOR](https://arxiv.org/abs/2401.18059) | Retrieval | Exposure |

## Keep this page current

The navigation page summarizes the entries in the catalog. When adding or changing a paper, update the relevant catalog row and BibTeX entry first, then update this page if it changes a recommended path or category overview. Run:

```bash
python3 scripts/validate_catalog.py
```
