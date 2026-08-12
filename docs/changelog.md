# Changelog

All notable repository changes are recorded here.

## Unreleased

### 2026-08-12 synchronization

- Added a paper-to-hub map that connects manuscript sections, figures, review
  claims, and literature resources to their public repository counterparts.
- Reframed the static site as the paper-aligned Research Hub and moved the v1
  catalog explorer into an explicitly labeled legacy section.
- Redesigned the Web Hub with an editorial paper hero, challenge cards,
  manuscript-figure previews, corpus-flow and evidence-map summaries, and a
  clearer resource library.
- Added lightweight PNG previews derived from the three current vector figure
  PDFs while retaining the PDFs as the canonical downloadable assets.
- Added a repository-root GitHub Pages entry point and README badge for the
  public Web Hub.
- Corrected public-completeness wording: the current hub publishes aggregate
  audit outputs, while the 208-work canonical table, 135-Core relation table,
  and reviewer provenance remain submission-release work.
- Migrated the reporting checklist to the five current challenge functions and
  rewrote the roadmap around manuscript-aligned release priorities.
- Synchronized manuscript-facing author metadata with the current TOIS draft:
  Yuqing Luo, Kai Zhang, and Liyang He.
- Synchronized all three current manuscript figure assets: the
  evidence-dependency scope, five-challenge control loop, and
  challenge-mechanism landscape.
- Added a seven-survey reference-library layer containing 886 raw citation
  records and 771 deduplicated papers, with an explicit boundary separating it
  from the 208-work reviewed evidence map.
- Reframed the literature navigator around Next-Hop Discovery, Path Management,
  Evidence Sufficiency, Error Recovery, and Evidence Composition.

### Manuscript-aligned v2 layer

- Aligned repository identity with **Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey** and the then-current author metadata.
- Added `taxonomy/challenge_codebook_v2.md` with the current evidence-dependency scope, Core/Supporting/Transfer-relevant tiers, and Direct/Secondary/No challenge relations.
- Added `docs/submission_audit_v2.md` and aggregate files under `taxonomy/audit_v2/` for the frozen 2026-08-09 manuscript snapshot.
- Documented the corpus construction flow: 452 raw hits, 342 unique candidates, 265 records entering primary-source review, 263 resolved sources, and 208 reviewed canonical works.
- Documented the 208-work scope split: 135 Core, 54 Supporting, and 19 Transfer-relevant.
- Added current Direct and Direct+Secondary challenge counts and the pairwise Direct overlap matrix used by the manuscript.
- Updated the coverage protocol to distinguish candidate discovery, scope inclusion, challenge coding, independent review, and source-grounded adjudication.
- Updated README, ARTIFACT, CITATION metadata, and contribution guidance to distinguish the current v2 manuscript layer from the historical v1 catalog and audit.
- Preserved the legacy 50-record catalog and 40-record single-coded audit for provenance; they are no longer presented as the source of current manuscript counts.

### Remaining release work

- Publish the 208-work canonical table and 135-Core challenge-relation table.
- Publish source, coding, reviewer, and adjudication provenance for the final
  reviewed evidence map, within the documented public boundary.
- Regenerate and tag the final manuscript-linked figures and quantitative outputs before submission.

## Legacy v1 history

The repository previously used a 50-method broad catalog and a frozen 40-method comparative audit organized around Observability, Selection preservation, Exposure, Fusion reliability, and Causal faithfulness. The v1 audit is single-coded and remains available only as a historical artifact.
