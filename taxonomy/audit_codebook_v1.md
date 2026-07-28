# Evidence-chain audit codebook v1.0

This codebook governs the frozen 40-record audit in
`taxonomy/audit_records.csv`. The broad catalog and the audit sample are
different objects:

- `methods.csv` is the curated discovery and taxonomy layer.
- `audit_records.csv` contains only records admitted to the frozen comparative
  audit.
- `reviewed` in the catalog means that metadata and the central taxonomy label
  were checked. It does not automatically make a record audit-eligible.

## Eligibility

A record is audit-eligible when the checked primary source establishes all of
the following:

1. the work materially changes or diagnoses retrieval-grounded dependent
   evidence;
2. the central intervention can be assigned to an earliest active
   evidence-chain stage;
3. the evaluation exposes at least one stage-aligned claim or observable; and
4. the source and bibliographic identity are stable enough to audit.

General single-hop retrievers, purely parametric reasoning methods, survey
papers, and systems whose multi-hop framing is incidental remain in the broad
literature layer but are excluded from this audit.

`joint` is never a primary estimand. When a method jointly changes several
stages, `primary_estimand` is the earliest stage directly changed by the
central mechanism and `joint` may appear only in `secondary_estimands`.

## The 24 fields

Fields 1--8 identify and stratify the record. Fields 9--13 code claims. Fields
14--23 code evidence. Field 24 records the adjudication rationale.

| # | Field | Allowed values / rule |
| ---: | --- | --- |
| 1 | `citation_key` | Unique key also present in `methods.csv` and `reading_list.bib`. |
| 2 | `title` | Canonical title from the primary source. |
| 3 | `year` | Four-digit archival or checked preprint year. |
| 4 | `architectural_family` | Controlled family from `docs/taxonomy.md`. |
| 5 | `primary_estimand` | `observability`, `selection_preservation`, `exposure`, `fusion`, or `faithfulness`. |
| 6 | `secondary_estimands` | Semicolon-separated controlled values; `joint` is allowed only here. |
| 7 | `source_url` | Stable primary-source landing page. |
| 8 | `audit_stratum` | `existing_seed`, `targeted_observability`, `targeted_selection`, `targeted_exposure`, `targeted_fusion`, `targeted_faithfulness`, `discretionary_recency`, or `discretionary_process`. |
| 9 | `claim_observability` | `primary`, `secondary`, `not_coded`, or `unclear`. |
| 10 | `claim_selection` | Same claim vocabulary. |
| 11 | `claim_exposure` | Same claim vocabulary. |
| 12 | `claim_fusion` | Same claim vocabulary. |
| 13 | `claim_faithfulness` | Same claim vocabulary. |
| 14 | `ev_chain_recall` | Evidence for complete-chain or hop-wise recall. |
| 15 | `ev_budget_match` | Evidence under matched passage, token, retrieval-call, or latency budget. |
| 16 | `ev_membership` | Evidence isolating selected-set membership. |
| 17 | `ev_ordering` | Evidence isolating position or order while membership is fixed. |
| 18 | `ev_stage_metric` | A metric aligned to the coded primary stage. |
| 19 | `ev_fusion_ablation` | Conditional reader/fusion ablation with evidence availability controlled. |
| 20 | `ev_deletion` | Evidence-removal or deletion intervention. |
| 21 | `ev_conflict` | Contradictory-evidence or conflict intervention. |
| 22 | `ev_counterfactual` | Counterfactual support or bridge intervention. |
| 23 | `ev_cost` | Retrieval-call, token, latency, FLOP, or comparable cost evidence. |
| 24 | `adjudication_note` | Short source-grounded reason for inclusion and the main confounder. |

Evidence fields use `yes`, `partial`, `unclear`, `not_reported`, or
`not_applicable`. `yes` requires a direct reported analysis. `partial` means
that the paper reports a related measurement but does not fully isolate the
target. `unclear` means the available checked evidence does not justify a
positive or negative judgment. `not_reported` may be used only after full-text
inspection; an abstract-level screen is never enough to assign it. Missing or
uncertain evidence is not treated as a negative result.

## Adjudication and counting

- Primary stage counts use only `primary_estimand`.
- A claim field is counted only when it is `primary` or `secondary`.
- An evidence field is counted as verified positive only when it is `yes`;
  `partial` is reported separately.
- `unclear`, `not_reported`, and `not_applicable` are never pooled.
- Statistics are generated from this CSV; prose counts must not be edited by
  hand.
- The two discretionary records improve recency and process-supervision
  coverage. They are declared rather than hidden inside the stage quotas.

## Reliability and verification boundary

The frozen v1.0 audit is single-coded. It has not undergone an independent
blind recoding pass, disagreement adjudication, or inter-coder reliability
analysis. No Cohen's kappa, Krippendorff's alpha, or percentage-agreement
claim should be inferred from this release.

The repository validators check record count, schema completeness, controlled
vocabularies, key uniqueness, cross-file identity, and reproducibility of
aggregate counts. Those checks catch structural drift; they do not certify
that a paper has been interpreted correctly. Semantic corrections should cite
the canonical source, identify the affected field, and explain the proposed
replacement in a pull request or issue.
