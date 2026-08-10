# Contributing to the Multi-Hop RAG Survey Companion

Contributions may add a method or benchmark, correct metadata, improve a challenge assignment, or extend repository tooling.

## Two repository layers

The repository currently preserves two layers:

1. **Current manuscript layer.** Scope tiers and challenge relations follow [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md). This layer supports *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*.
2. **Legacy v1 catalog.** The older CSV catalog and 40-record audit use the Observability / Selection preservation / Exposure / Fusion / Faithfulness schema. Those files remain for provenance and backward compatibility.

Do not use the legacy v1 audit to support current manuscript counts.

## Before opening a pull request

1. Search existing records and open issues to avoid duplicates.
2. Provide a stable DOI, ACL Anthology, arXiv, OpenReview, or publisher landing page.
3. State whether the proposal affects discovery only, scope membership, or challenge coding.
4. For current manuscript coding, apply [`taxonomy/challenge_codebook_v2.md`](taxonomy/challenge_codebook_v2.md).
5. If the change alters a reported count, update the row-level audit source first and regenerate the aggregate files under `taxonomy/audit_v2/`.
6. Preserve the primary-source rationale and any reviewer/adjudication information required by the current audit protocol.

## Current challenge-coding rules

- One canonical work may receive multiple challenge labels.
- Each work-to-challenge relation is `Direct`, `Secondary`, or `No`.
- Direct prevalence is computed only among Core works.
- Scope tier and relation strength are separate decisions.
- Next-Hop Discovery, Path Management, Evidence Sufficiency, Error Recovery, and Evidence Composition must be assigned by their decision object, not by architecture name.
- Absence of a label requires source review; missing abstract evidence is not enough for a negative assignment.

## Legacy catalog rules

If you intentionally update the legacy CSV catalog, preserve its existing headers and controlled vocabulary unless a migration has been discussed first. The historical files include `taxonomy/methods.csv`, `taxonomy/pipeline_mapping.csv`, `taxonomy/audit_records.csv`, and `taxonomy/audit_codebook_v1.md`.

## Pull request checklist

- [ ] Canonical identity and persistent source URL are verified.
- [ ] Scope tier is justified when the work enters the v2 reviewed corpus.
- [ ] Challenge relations follow the v2 codebook.
- [ ] Changes to reported counts originate from row-level records rather than hand-edited aggregate prose.
- [ ] Aggregate v2 CSVs and documentation are regenerated when counts change.
- [ ] Legacy CSV validators still pass if legacy files were modified.
- [ ] No publisher Version of Record is added without redistribution permission.

## Code and documentation

Keep changes auditable and explain the motivation. Schema changes should be proposed before a large migration. Corrections with stronger primary-source evidence are preferred over silent deletion.