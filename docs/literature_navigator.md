# Literature navigator

This page offers conceptual reading paths through the catalog. For a filterable view with venue, task, dataset, and verified-code metadata, open the [research catalog site](index.html). This guide is curated rather than exhaustive; see the [coverage protocol](coverage_protocol.md) for what that means.

## Start with your question

| If you are asking… | Begin with | Then compare |
| --- | --- | --- |
| Can a system recover every supporting document? | [PathRetriever](https://openreview.net/forum?id=SJgVHkrYDH) → [MDR](https://aclanthology.org/2021.naacl-main.424/) | [Baleen](https://openreview.net/forum?id=Ghk0AJ8XtVx) and [Beam Retrieval](https://aclanthology.org/2024.naacl-long.96/) for more structured search. |
| Should a complex question be decomposed before retrieval? | [DecompRC](https://aclanthology.org/P19-1613/) → [ONUS](https://aclanthology.org/2020.emnlp-main.713/) | [RERC](https://aclanthology.org/2021.findings-emnlp.17/) and [EfficientRAG](https://aclanthology.org/2024.emnlp-main.199/) for staged decomposition. |
| How should a model combine scattered evidence? | [DFGN](https://aclanthology.org/P19-1617/) → [HGN](https://aclanthology.org/2020.emnlp-main.710/) | [Fusion-in-Decoder](https://arxiv.org/abs/2007.01282) for passage-level generative fusion. |
| When should retrieval be iterative or adaptive? | [IRCoT](https://aclanthology.org/2023.acl-long.557/) → [ReAct](https://arxiv.org/abs/2210.03629) | [FLARE](https://arxiv.org/abs/2305.06983), [Self-RAG](https://arxiv.org/abs/2310.11511), and [Adaptive-RAG](https://arxiv.org/abs/2403.14403). |
| How does context organization alter downstream use? | [Fusion-in-Decoder](https://arxiv.org/abs/2007.01282) | [RAPTOR](https://arxiv.org/abs/2401.18059) and [CRAG](https://arxiv.org/abs/2401.15884). |

## By latent-chain bottleneck

### Observability: find the support chain

- [GRAFT-Net (2018)](https://aclanthology.org/D18-1455/) and [PullNet (2019)](https://aclanthology.org/D19-1242/) — early graph-based retrieval over text and knowledge bases.
- [PathRetriever (2020)](https://openreview.net/forum?id=SJgVHkrYDH) and [MDR (2021)](https://aclanthology.org/2021.naacl-main.424/) — sequential and dense retrieval for open-domain multi-hop QA.
- [Baleen (2021)](https://openreview.net/forum?id=Ghk0AJ8XtVx) and [Beam Retrieval (2024)](https://aclanthology.org/2024.naacl-long.96/) — address uncertainty and combinatorial growth in multi-hop search.
- [HippoRAG (2024)](https://arxiv.org/abs/2405.14831) — retrieves through a graph-memory index using personalized PageRank.
- [IRCoT (2023)](https://aclanthology.org/2023.acl-long.557/) and [FLARE (2023)](https://arxiv.org/abs/2305.06983) — make reasoning or generation state inform the next retrieval action.

### Utility: keep useful evidence under a budget

- [PullNet (2019)](https://aclanthology.org/D19-1242/) and [PathRetriever (2020)](https://openreview.net/forum?id=SJgVHkrYDH) — use previous hops to focus subsequent retrieval.
- [IRCoT (2023)](https://aclanthology.org/2023.acl-long.557/), [CRAG (2024)](https://arxiv.org/abs/2401.15884), and [Adaptive-RAG (2024)](https://arxiv.org/abs/2403.14403) — adapt retrieval decisions to intermediate reasoning, context quality, or query complexity.

### Exposure: make evidence usable in context

- [Baleen (2021)](https://openreview.net/forum?id=Ghk0AJ8XtVx) — condenses retrieved context between hops.
- [RAPTOR (2024)](https://arxiv.org/abs/2401.18059) — organizes evidence as a hierarchy of retrieved and summarized units.
- [GraphRAG (2024)](https://arxiv.org/abs/2404.16130) — exposes corpus-level evidence through graph communities and their summaries.

### Fusion: compose evidence correctly

- [DFGN (2019)](https://aclanthology.org/P19-1617/) and [HGN (2020)](https://aclanthology.org/2020.emnlp-main.710/) — graph propagation over heterogeneous text structures.
- [Fusion-in-Decoder (2021)](https://arxiv.org/abs/2007.01282) — reader-side generative fusion across independently encoded passages.

### Faithfulness and joint control

- [ReAct (2023)](https://arxiv.org/abs/2210.03629) exposes reasoning-and-action trajectories, but trajectories alone are not causal evidence of grounding.
- [Self-RAG (2024)](https://arxiv.org/abs/2310.11511) jointly learns retrieval, generation, and critique; it is labeled `joint` because it deliberately spans several bottlenecks.

## By design route

| Route | Representative papers | Useful contrast |
| --- | --- | --- |
| Graph / KG | GRAFT-Net, PullNet, DFGN, HGN | Explicit graph construction versus neural graph fusion. |
| Retrieval | PathRetriever, MDR, Baleen, RAPTOR, HippoRAG, Beam Retrieval | Sequential paths, dense retrieval, condensation, hierarchy, graph memory, and beam search. |
| Decomposition | DecompRC, ONUS, RERC, EfficientRAG | Supervised, unsupervised, staged, and retrieval-pruning decompositions. |
| Reader / fusion | Fusion-in-Decoder | Evidence is fixed first, then composed by the reader. |
| Reasoning-interleaved | IRCoT, ReAct | Generated reasoning guides external actions. |
| Agentic / corrective | FLARE, Self-RAG, CRAG, Adaptive-RAG | The policy decides whether, when, or how to retrieve and correct evidence. |

## Suggested benchmark paths

| Evaluation need | Start with | Important caution |
| --- | --- | --- |
| Two-hop QA with supporting facts | [HotpotQA](https://aclanthology.org/D18-1259/) | Supporting-fact labels remain an imperfect proxy for the complete latent chain. |
| Diverse evidence and reasoning forms | [2WikiMultiHopQA](https://aclanthology.org/2020.coling-main.580/) and [MuSiQue](https://aclanthology.org/2022.tacl-1.31/) | Compare retrieval setting and distractor construction before comparing scores. |
| More than two hops / claim verification | [HoVer](https://aclanthology.org/2020.findings-emnlp.309/) | It is fact verification, so it is not directly interchangeable with answer extraction. |
| Two-fact scientific composition | [QASC](https://ojs.aaai.org/index.php/AAAI/article/view/6319) | The composed fact may introduce a bridge concept absent from the question. |

## Chronological index

| Year | Paper | Route | Primary bottleneck |
| --- | --- | --- | --- |
| 2018 | [GRAFT-Net](https://aclanthology.org/D18-1455/) | Graph / KG | Observability |
| 2019 | [DecompRC](https://aclanthology.org/P19-1613/), [DFGN](https://aclanthology.org/P19-1617/), [PullNet](https://aclanthology.org/D19-1242/) | Decomposition / Graph | Utility / Fusion / Observability |
| 2020 | [PathRetriever](https://openreview.net/forum?id=SJgVHkrYDH), [ONUS](https://aclanthology.org/2020.emnlp-main.713/), [HGN](https://aclanthology.org/2020.emnlp-main.710/), [MHGRN](https://aclanthology.org/2020.emnlp-main.99/) | Retrieval / Decomposition / Graph | Observability / Utility / Fusion |
| 2021 | [Fusion-in-Decoder](https://arxiv.org/abs/2007.01282), [MDR](https://aclanthology.org/2021.naacl-main.424/), [Baleen](https://openreview.net/forum?id=Ghk0AJ8XtVx), [RERC](https://aclanthology.org/2021.findings-emnlp.17/) | Reader / Retrieval / Decomposition | Fusion / Observability |
| 2023 | [ReAct](https://arxiv.org/abs/2210.03629), [IRCoT](https://aclanthology.org/2023.acl-long.557/), [FLARE](https://arxiv.org/abs/2305.06983) | Agentic / Reasoning | Joint / Observability |
| 2024 | [Self-RAG](https://arxiv.org/abs/2310.11511), [RAPTOR](https://arxiv.org/abs/2401.18059), [CRAG](https://arxiv.org/abs/2401.15884), [Adaptive-RAG](https://arxiv.org/abs/2403.14403), [Beam Retrieval](https://aclanthology.org/2024.naacl-long.96/), [GraphRAG](https://arxiv.org/abs/2404.16130), [HippoRAG](https://arxiv.org/abs/2405.14831), [EfficientRAG](https://aclanthology.org/2024.emnlp-main.199/) | Agentic / Retrieval / Graph / Decomposition | Joint / Exposure / Utility / Observability |

## Keep this page current

Update the structured catalog first, then revise this page only if a new work changes a recommended conceptual comparison. Run:

```bash
python3 scripts/validate_catalog.py
python3 scripts/build_catalog_site.py
```
