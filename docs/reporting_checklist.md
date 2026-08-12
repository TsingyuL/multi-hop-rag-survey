# Multi-Hop RAG reporting checklist

Use this checklist alongside final-answer metrics. It follows the five
challenge functions in the current manuscript and asks authors to expose the
decision object changed by a method, not only its architecture name.

| Challenge or control | Report | Why it matters |
| --- | --- | --- |
| Task and evidence protocol | Corpus, evidence access, retriever, reader, context budget, supervision, and allowed retrieval calls | Defines which evidence dependencies are observable and which comparisons are valid |
| Next-Hop Discovery | The next-information-need representation, acquisition action, hop-wise retrieval diagnostics, and state used to generate the action | Distinguishes a better acquisition decision from simply allocating more retrieval opportunity |
| Path Management | Candidate trajectory representation, pruning or retention rule, beam/frontier size, survival of valid partial chains, and matched search budget | Separates future trajectory value from local document relevance |
| Evidence Sufficiency | Adequacy or answerability signal, stopping threshold, calibration, premature-stop errors, excessive-search errors, and cost-quality trade-off | Tests whether the system knows when the current evidence is enough |
| Error Recovery | Failure or integrity signal, diagnosed state, corrective transition, rollback or replanning behavior, and recovery success conditional on a detected failure | Distinguishes actual repair from undiagnosed additional retrieval |
| Evidence Composition | Required operator across evidence units, evidence accessibility, operation-specific accuracy or error analysis, and controlled evidence-use ablations | Separates obtaining the right evidence from correctly binding, comparing, aggregating, or transforming it |
| Cross-challenge controller | Interfaces among acquisition, trajectory allocation, stopping, repair, and composition; matched compute and retrieval opportunity | Makes gains attributable when several challenge functions share one controller |
| Final outcome | Answer quality, grounding, cost, latency, and dataset-specific caveats | Keeps end-task performance necessary but not sufficient for mechanism claims |

An answer-only metric cannot distinguish a wrong acquisition action, loss of a
valid path, premature stopping, failed repair, or incorrect composition. Report
the earliest challenge-specific diagnostic available for each claimed
mechanism, together with final-answer quality and matched resource controls.
