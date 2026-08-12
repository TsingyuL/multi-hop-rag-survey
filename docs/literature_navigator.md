# Literature navigator

This page follows the manuscript's current challenge-centered map of multi-hop
RAG. The five branches are decision functions over dependent evidence, not
exclusive architecture classes. A work can therefore appear in more than one
branch.

Use this page for a guided entry into the literature. Use the
[seven-survey reference library](../literature/README.md) for broad discovery,
and use the [v2 challenge codebook](../taxonomy/challenge_codebook_v2.md) plus
[current audit summary](submission_audit_v2.md) for manuscript-level coding and
counts.

## Start with your question

| If you are asking… | Begin with | Then compare |
| --- | --- | --- |
| What evidence should the system retrieve next? | Next-Hop Discovery | Evidence-conditioned retrieval, explicit subgoals, missing-information models, and agentic search policies |
| Which partial trajectory is worth preserving? | Path Management | Beam retention, joint candidate sets, subgraph management, and lookahead |
| Does the system already have enough evidence? | Evidence Sufficiency | Answerability judgments, adaptive stopping, gap diagnosis, and cost-aware control |
| How should the system repair a failed state? | Error Recovery | Local correction, rollback, reversible state, and verifier-guided replanning |
| How should supplied evidence be joined or transformed? | Evidence Composition | Graph propagation, explicit intermediate variables, executable operators, and heterogeneous alignment |

## 1. Next-Hop Discovery

Next-Hop Discovery maps the current evidence state to a concrete acquisition
target. The useful comparison is the interface exposed between what is already
known and what should be sought next.

| Family | Representative papers | What to inspect |
| --- | --- | --- |
| Evidence-conditioned retrieval | [GoldEn Retriever](https://aclanthology.org/D19-1261/), [MDR](https://openreview.net/forum?id=EMHoBG0avc1), [Baleen](https://proceedings.neurips.cc/paper/2021/hash/e8b1cbd05f6e6a358a81dee52493dd06-Abstract.html) | Whether the accumulated context preserves the bridge needed for the next retrieval |
| Explicit decomposition or reasoning | [DecompRC](https://aclanthology.org/P19-1613/), [Self-Ask](https://aclanthology.org/2023.findings-emnlp.378/), [IRCoT](https://aclanthology.org/2023.acl-long.557/) | Whether the subquestion or reasoning state expresses a valid next information need |
| Missing-information modeling | [MIGRES](https://aclanthology.org/2025.coling-main.163/), [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) | Whether the system separates “insufficient” from “what is missing” |
| Structured or agentic search | [ToG](https://openreview.net/forum?id=nnVO1PvbTv), [Search-R1](https://arxiv.org/abs/2503.09516), [RAG-Gym](https://arxiv.org/abs/2502.13957) | How frontier actions, search rewards, and retrieval budgets shape the next hop |

## 2. Path Management

Path Management estimates the future value of partial evidence trajectories.
It is distinct from ordinary reranking because a locally weak item can still be
necessary for a valid future chain.

| Family | Representative papers | What to inspect |
| --- | --- | --- |
| Partial-chain retention | [PathRetriever](https://openreview.net/forum?id=SJgVHkrYDH), [BeamDR](https://aclanthology.org/2021.naacl-main.368/), [M3](https://aclanthology.org/2024.lrec-main.947/) | Whether valid chains survive pruning under a fixed budget |
| Set or subgraph management | [CORE](https://aclanthology.org/2022.findings-emnlp.392/), [CIRAG](https://aclanthology.org/2026.acl-long.1203/), [CatRAG](https://aclanthology.org/2026.findings-acl.290/) | Whether compatibility among evidence units is scored jointly |
| Lookahead or tree search | [PPRR](https://aclanthology.org/2026.findings-acl.1147/), [STEM](https://aclanthology.org/2026.acl-long.329/) | Whether the controller estimates future reachability rather than only current relevance |

## 3. Evidence Sufficiency

Evidence Sufficiency decides whether the current external evidence state is
adequate for the remaining task. It should be evaluated separately from the
decision about what to retrieve next.

| Family | Representative papers | What to inspect |
| --- | --- | --- |
| Answerability judgment | [IDRQA](https://doi.org/10.1145/3404835.3462853), [AISO](https://aclanthology.org/2021.emnlp-main.293/) | Whether adequacy can be diagnosed before final answer generation |
| Adaptive stopping | [Stop-RAG](https://arxiv.org/abs/2510.14337), [FrugalRAG](https://openreview.net/forum?id=uQKtwdJN0o) | Premature stopping, excessive search, and cost calibration |
| Gap-aware diagnosis | [MIGRES](https://aclanthology.org/2025.coling-main.163/), [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) | Whether the controller exposes the missing evidence rather than only a binary label |
| Evidence-aware control | [SEMA-RAG](https://aclanthology.org/2026.findings-acl.917/), [IterCOMP](https://aclanthology.org/2026.acl-long.1559/) | How evidence state, compression, and continuation decisions interact |

## 4. Error Recovery

Error Recovery requires an observable failure signal followed by a corrective
state transition. Merely requesting more evidence is not recovery unless the
system diagnoses and revises an invalid or unproductive state.

| Family | Representative papers | What to inspect |
| --- | --- | --- |
| Local correction | [Dr3](https://aclanthology.org/2024.lrec-main.476/), [ARI-KBQA](https://aclanthology.org/2026.acl-long.1479/) | Whether the method identifies and corrects a specific off-topic or invalid intermediate state |
| Rollback or reversible state | [ReAgent](https://aclanthology.org/2025.emnlp-main.202/), [RetroRAG](https://arxiv.org/abs/2501.05475) | Whether prior evidence and reasoning states remain editable or restorable |
| Verifier-guided replanning | [SR-RAG](https://aclanthology.org/2026.findings-acl.1922/), [D2Plan](https://aclanthology.org/2026.acl-long.216/) | Whether a verifier localizes the failure and constrains the next plan |

## 5. Evidence Composition

Evidence Composition begins once the required evidence units are available. It
asks whether the system can perform the binding, comparison, aggregation, or
transformation needed to produce an answer.

| Family | Representative papers | What to inspect |
| --- | --- | --- |
| Graph binding or propagation | [DFGN](https://aclanthology.org/P19-1617/), [HGN](https://aclanthology.org/2020.emnlp-main.710/), [KIFGraph](https://aclanthology.org/2022.dlg4nlp-1.8/) | Whether relations and message passing bind the correct evidence units |
| Explicit intermediate variables | [DecompRC](https://aclanthology.org/P19-1613/), [PathFiD](https://aclanthology.org/2022.acl-long.69/), [SSCOT](https://aclanthology.org/2024.naacl-long.475/) | Whether intermediate answers or slots expose the join variable |
| Join, comparison, or aggregation | [S3HQA](https://aclanthology.org/2023.acl-short.147/) | Whether the required operator is explicit and its failure can be localized |
| Heterogeneous alignment | [DEHG](https://aclanthology.org/2022.findings-naacl.12/), [HybridQA](https://aclanthology.org/2020.findings-emnlp.91/), [MultiModalQA](https://openreview.net/forum?id=ee6W5UgQLa) | Whether table, text, graph, and image evidence are aligned before composition |

## Benchmark reading paths

| Evaluation need | Start with | Important caution |
| --- | --- | --- |
| Two-hop QA with supporting facts | [HotpotQA](https://aclanthology.org/D18-1259/) | Supporting-fact labels are an imperfect proxy for the complete latent evidence chain |
| Diverse evidence and reasoning forms | [2WikiMultiHopQA](https://aclanthology.org/2020.coling-main.580/) and [MuSiQue](https://aclanthology.org/2022.tacl-1.31/) | Match retrieval settings and distractor construction before comparing scores |
| More than two hops or claim verification | [HoVer](https://aclanthology.org/2020.findings-emnlp.309/) | Fact verification is not directly interchangeable with answer extraction |
| Two-fact scientific composition | [QASC](https://ojs.aaai.org/index.php/AAAI/article/view/6319) | The composed fact can introduce a bridge concept absent from the question |
| Text-table-image composition | [HybridQA](https://aclanthology.org/2020.findings-emnlp.91/) and [MultiModalQA](https://openreview.net/forum?id=ee6W5UgQLa) | Separate evidence accessibility from the downstream composition operator |

## How the repository layers fit together

1. Use this navigator to choose a challenge and a few anchor papers.
2. Use the [reference library](../literature/README.md) to expand discovery and
   compare coverage across seven adjacent surveys.
3. Inspect primary technical sources before making a scope or mechanism claim.
4. Apply the [v2 challenge codebook](../taxonomy/challenge_codebook_v2.md) for
   Core, Supporting, Transfer-relevant, Direct, Secondary, and No decisions.
5. Use only the frozen reviewed evidence map for manuscript-level prevalence and
   overlap counts.

The reference library is intentionally broader than the reviewed evidence map;
neither citation frequency nor appearance in several surveys is a substitute
for primary-source coding.
