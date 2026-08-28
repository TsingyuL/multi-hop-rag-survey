# Paper-to-hub map

This repository is the research hub for *Multi-Hop Retrieval-Augmented Generation: A Survey of Evidence Dependency, Process Organization, Knowledge Access, and Evaluation Alignment*. The working manuscript source remains outside the repository.

## Hub contract

The current manuscript uses review cutoff **August 5, 2026** and a frozen **274-paper** canonical frame. A resource is manuscript-aligned only when its scope, terminology, counts, and caveats agree with that snapshot.

The hub separates four layers:

1. **Conceptual layer:** evidence dependency, process organization, knowledge-access conditions, and evaluation alignment;
2. **Review layer:** coverage protocol, canonical frame, coarse access mapping, and targeted routing-evaluation recheck;
3. **Discovery layer:** adjacent-survey reference resources and executable maintenance queries, which are not corpus denominators;
4. **Historical layer:** earlier challenge-centered and v1 audit artifacts retained for provenance.

## Paper structure and hub entry points

| Paper section or claim | Hub resource | Status |
| --- | --- | --- |
| Positioning and research questions | [`README.md`](../README.md) | current |
| RQ1: evidence-dependency scope | [`docs/coverage_protocol.md`](coverage_protocol.md) | current |
| RQ2: established process organization | manuscript + adjacent-survey reference layer | current conceptual synthesis |
| RQ3: knowledge-access mapping | submission artifact release required | current analysis, row-level public freeze pending |
| RQ4: evaluation alignment / routing recheck | submission artifact release required | targeted primary-source recheck complete; public freeze pending |
| Discovery queries | [`taxonomy/discovery_queries.csv`](../taxonomy/discovery_queries.csv) | current maintenance interface |
| Adjacent-survey reference layer | [`literature/README.md`](../literature/README.md) | discovery only |
| Artifact limitations | [`ARTIFACT.md`](../ARTIFACT.md) | current |
| Current alignment summary | [`submission_alignment_v10.md`](submission_alignment_v10.md) | current |
| Five-challenge codebook and audit-v2 materials | `taxonomy/challenge_codebook_v2.md`, `taxonomy/audit_v2/` | **historical snapshot; not current manuscript claims** |

## Current evidence snapshot

The manuscript's canonical frame contains **274 papers**:

- 149 CORE;
- 57 SUPPORTING;
- 68 TRANSFER.

The revised access synthesis uses 170 retrieval-bearing CORE/SUPPORTING papers and 111 acquisition-dependent papers. The state-dependent routing / transition-capable subset contains nine cases and is subjected to a separate primary-source evaluation recheck.

The current paper does not reuse the historical 208-work challenge prevalence analysis, and it does not report the historical `452 → … → 208` screening flow as the construction flow for the 274-paper frame.

## Figure mapping

The final manuscript figures are being redesigned around the layered story. Existing PDFs in `mh_figures/` reflect earlier manuscript snapshots and should be treated as historical until replaced by the submission figures.

Planned main-text roles are:

1. **Figure 1:** layered view of evidence dependency → process organization → knowledge access → evaluation alignment;
2. **Figure 2:** evidence-dependency scope boundary;
3. **Figure 3:** established process backbone plus orthogonal access view;
4. **Figure 4:** descriptive knowledge-access landscape;
5. **Figure 5:** evaluation coverage for adaptive access decisions.

## Reliability and release boundary

The broader fine-grained coding schema did not pass the pre-specified confirmatory reliability gate. Full-corpus percentages are therefore described as **descriptive evidence-backed mappings**, not reliability-validated prevalence estimates. High-leverage RQ4 claims rely on targeted primary-source rechecking of the nine routing cases.

A submission-ready release should provide the exact 274-paper frame, row-level coarse access mapping, nine-case routing recheck, executable queries, figure/table regeneration outputs, and an immutable release identifier.

## Historical materials

The earlier challenge-centered manuscript snapshot used 208 works and five challenge families. Those files remain useful as project provenance but are not the taxonomy, denominator, title, figures, or quantitative conclusions of the current manuscript.

## Versioning rule

Any change to the manuscript cutoff, corpus counts, analytical definitions, routing recheck, figures, or author metadata should update `README.md`, `ARTIFACT.md`, this map, `docs/coverage_protocol.md`, `docs/submission_alignment_v10.md`, and `CITATION.cff` together before a release is tagged.
