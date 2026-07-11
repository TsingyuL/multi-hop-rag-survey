# Multi-Hop RAG reporting checklist

Use this checklist alongside aggregate answer metrics. It translates the survey's latent-chain framework into reviewable evidence.

| Report | Why it matters |
| --- | --- |
| Task, corpus, retriever, reader, and context-budget details | Defines the observation process |
| Chain/passage recall before selection | Diagnoses observability |
| Selection recall or utility at the reported budget | Diagnoses budget-induced loss |
| Context ordering and placement policy | Makes exposure claims testable |
| Multi-hop composition metric or error analysis | Separates fusion from retrieval failure |
| Ablations that remove, swap, or corrupt evidence | Tests causal evidence use |
| Cost, latency, stopping rule, and number of retrieval calls | Enables comparison of adaptive systems |
| Dataset-specific caveats and supervision type | Prevents invalid cross-benchmark claims |

An answer-only metric cannot distinguish absent evidence, dropped evidence, inaccessible evidence, failed composition, and post-hoc reasoning. Report the earliest available diagnostic for each claimed bottleneck.
