# Changelog

All notable repository changes are recorded here.

## Unreleased

### Manuscript-aligned v2 layer

- Aligned repository identity with **Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey** and authors Yuqing Luo, Kai Zhang, and Heli Yang.
- Added `taxonomy/challenge_codebook_v2.md` with the current evidence-dependency scope, Core/Supporting/Transfer-relevant tiers, and Direct/Secondary/No challenge relations.
- Added `docs/submission_audit_v2.md` and aggregate files under `taxonomy/audit_v2/` for the frozen 2026-08-09 manuscript snapshot.
- Documented the corpus construction flow: 452 raw hits, 342 unique candidates, 265 records entering primary-source review, 263 resolved sources, and 208 reviewed canonical works.
- Documented the 208-work scope split: 135 Core, 54 Supporting, and 19 Transfer-relevant.
- Added current Direct and Direct+Secondary challenge counts and the pairwise Direct overlap matrix used by the manuscript.
- Updated the coverage protocol to distinguish candidate discovery, scope inclusion, challenge coding, independent review, and source-grounded adjudication.
- Updated README, ARTIFACT, CITATION metadata, and contribution guidance to distinguish the current v2 manuscript layer from the historical v1 catalog and audit.
- Preserved the legacy 50-record catalog and 40-record single-coded audit for provenance; they are no longer presented as the source of current manuscript counts.

### Remaining release work

- Publish the row-level frozen discovery/screening ledger.
- Publish the 208-work canonical table and 135-Core challenge-relation table.
- Publish reviewer/adjudication provenance needed to independently regenerate the v2 aggregate snapshot.
- Regenerate and tag the final manuscript-linked figures and quantitative outputs before submission.

## Legacy v1 history

The repository previously used a 50-method broad catalog and a frozen 40-method comparative audit organized around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness. The v1 audit is single-coded and remains available only as a historical artifact.