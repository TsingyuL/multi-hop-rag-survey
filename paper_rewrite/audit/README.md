# Diagnostic audit artifact

The manuscript uses a frozen, purposively stratified selection of 70 papers:

- 15 Initial Retrieval
- 25 Follow-up Retrieval
- 20 Evidence Integration
- 10 Feedback Learning

Selection is not treated as completed full-text auditing. A record is promoted to `completed_full_text_audit` only after the relevant paper and appendix have been inspected and the coding includes:

1. a primary claim;
2. claim-aligned diagnostic values;
3. a page, section, table, figure, or appendix locator;
4. a short evidence summary; and
5. an unresolved diagnostic gap.

## Files

- `audit_batch_01_completed.csv`: first balanced calibration batch, containing two papers from each primary category.

## Coding values

- `reported`: direct aggregate evidence is reported.
- `partial`: a closely related diagnostic is present, but the target process is not fully exposed.
- `not_reported`: the diagnostic is relevant to the central claim but was not found in the inspected full text.
- `not_applicable`: the diagnostic is outside the paper's stated claim or task.
- `unclear`: the setup does not permit a defensible decision.

The first batch contains 8 completed records. The other 62 papers remain selected but unresolved. No category-level prevalence statistic should be computed until its claim-aligned denominator has been fully coded. Before submission, a stratified subset should be independently double-coded and adjudicated.
