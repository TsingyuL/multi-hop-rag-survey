# Audit v2 aggregate snapshot

This directory contains the aggregate statistics used by the current manuscript *Resolving Evidence Chains in Multi-Hop RAG: A Challenge-Centered Survey*.

See the [paper-to-hub map](../../docs/paper_hub.md) for the relationship between
these aggregates, the manuscript sections, and the planned row-level release.

## Files

- `search_flow.csv`: discovery, screening, source-resolution, and scope-tier counts.
- `challenge_counts.csv`: Direct and Direct+Secondary challenge counts among the 135 Core works.
- `direct_overlap.csv`: pairwise Direct overlap matrix among Core works.

The aggregate snapshot is aligned to the review cutoff **2026-08-09** and to `docs/submission_audit_v2.md`.

## Important reproducibility boundary

These aggregate files are not a substitute for the row-level audit. Before the repository is tagged for submission, add the frozen discovery/screening ledger, the 208-work canonical table, the 135-Core challenge-relation table, and reviewer/adjudication provenance. Those row-level files are required to regenerate the aggregate snapshot independently.

The legacy 40-record audit under `taxonomy/audit_records.csv` and `taxonomy/audit_codebook_v1.md` is retained for provenance only and is **not** the source of the current manuscript counts.
