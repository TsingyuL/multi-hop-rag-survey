# Challenge codebook v2

**Status:** manuscript-aligned coding guide for *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*.

**Review cutoff:** 2026-08-09.

This codebook governs the scope tiers, challenge relations, and quantitative claims used by the current manuscript. It is distinct from the legacy v1 estimand audit retained in `taxonomy/audit_codebook_v1.md`.

## Scope criterion

A work is in the target multi-hop RAG problem space when solving the task depends on external evidence in at least one of two ways:

1. **Acquisition dependency:** evidence obtained earlier changes or specifies a later information need, retrieval target, or search action.
2. **Reasoning dependency:** answering requires a substantive operation across multiple external evidence units, such as binding, comparison, conjunction, relational join, aggregation, temporal alignment, or transformation.

Document count, retrieval-call count, or reasoning length alone does not establish multi-hop scope.

## Scope tiers

| Tier | Rule |
| --- | --- |
| **Core** | The central contribution materially depends on evidence dependencies across multiple steps or units. Removing those dependencies would substantially change the research problem or the method's central mechanism. |
| **Supporting** | The work remains within retrieval, RAG, or QA system design and provides a mechanism relevant to multi-hop systems, but dependent evidence resolution is not central to its research problem. |
| **Transfer-relevant** | The work originates outside the target retrieval/RAG task population and is retained because its mechanism or boundary case clarifies one of the five challenges. |

The current frozen snapshot contains **208 canonical works: 135 Core, 54 Supporting, and 19 Transfer-relevant**.

## Relation strengths

The primary coding unit is the relation between a canonical work and a challenge.

- **Direct:** the work's central mechanism explicitly instantiates the challenge decision or operation.
- **Secondary:** the work has a meaningful supporting effect or transferable mechanism for the challenge, but the challenge is not central enough to enter Direct prevalence counts.
- **No:** no qualifying relation is established from the reviewed source. This is not a claim that the work could never support the capability in another setting.

A work may receive several Direct labels.

## Five challenge families

| Challenge | Decision or operation | Direct criterion | Common confound |
| --- | --- | --- | --- |
| **Next-Hop Discovery** | Determine the next concrete information need or acquisition action. | The current evidence state determines a query, subquestion, bridge key, relation, node, or expansion target. | Deciding only whether to continue retrieval. |
| **Path Management** | Allocate search or retention according to future trajectory value. | The mechanism explicitly compares, retains, prioritizes, merges, or prunes candidate multi-hop trajectories. | Reranking individual documents, memory, or compression without trajectory semantics. |
| **Evidence Sufficiency** | Assess whether current external evidence is adequate for the remaining task. | The current evidence state drives an adequacy, answerability, continue, or finish decision. | Complexity routing before retrieval or generic uncertainty not tied to accumulated evidence. |
| **Error Recovery** | Repair a diagnosed failed intermediate state. | An explicit failure diagnosis triggers rollback, revision, replacement, or redirection. | Retrying, continued retrieval, proactive alternative preservation, or generic reflection without state repair. |
| **Evidence Composition** | Execute a substantive operation across supplied evidence units. | Bridge binding, comparison, join, conjunction, aggregation, transformation, or alignment across representations is central. | Context selection, packing, compression, or reasoning over one evidence unit. |

## Boundary rules

Sufficiency and Discovery may share a controller but answer different questions: **is more evidence needed?** versus **what evidence should be sought next?**

Path Management is prospective. It preserves or compares trajectories before failure is established. Recovery begins only after a failure is diagnosed and requires a corrective state transition.

Sufficiency and Recovery are not mutually exclusive. A controller may independently assess adequacy and state integrity and therefore receive both labels.

Composition requires an operation across multiple supplied evidence units. Context accessibility, memory, evidence selection, retrieval-augmented verification, or generic reasoning guidance is Secondary unless the deployed method itself performs the required cross-evidence operation.

## Review and adjudication

The scope and challenge assignments used in manuscript-level quantitative analysis are independently reviewed by two reviewers under the same codebook. Reviewers inspect the relevant primary technical source before reconciliation. Disagreements are revisited against those sources and resolved through explicit adjudication.

The adjudicated canonical-work table is the counting source for challenge prevalence and pairwise overlap. Aggregate corpus construction counts come from the internal frozen discovery and screening ledger rather than from the final canonical-work table.

## Public release boundary

The public row-level artifact begins with the final **208 reviewed canonical works**. Candidate-level discovery and screening records are not part of the public release.

The public release should include the 208-work canonical table, the 135-Core challenge-relation table, and reviewer/adjudication provenance sufficient to regenerate the manuscript's challenge counts and overlap statistics. Aggregate screening counts and the search protocol remain public even though the full candidate queue is not.

## Counting rules

- Primary prevalence uses **Direct relations among the 135 Core works**.
- `Direct+Secondary` is reported only as a sensitivity analysis for relation strength.
- Pairwise overlap counts a Core work once when both challenge relations are Direct.
- Supporting and Transfer-relevant works inform mechanism synthesis and boundary analysis but do not enter Core prevalence counts.
- Narrative inclusion in the manuscript does not determine quantitative coding.

See `docs/submission_audit_v2.md` for the frozen aggregate snapshot.