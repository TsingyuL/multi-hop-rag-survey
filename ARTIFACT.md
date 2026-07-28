# Artifact readiness

This is a survey companion, not a benchmark submission or a claim of independently reproduced experimental results. It nevertheless follows the artifact-oriented practices relevant to an ACM-style public companion: clear scope, permanent-source metadata, the current Figure 1 asset, catalog schemas, and automated catalog checks.

## Included artifacts

| Artifact | Location | Verification |
| --- | --- | --- |
| Figure 1 | [`mh_figures/fig1.pdf`](mh_figures/fig1.pdf) | Open the PDF and compare it with the manuscript figure |
| Survey catalog | [`taxonomy/`](taxonomy) | Run `python3 scripts/validate_catalog.py` |
| Frozen audit records | [`taxonomy/audit_records.csv`](taxonomy/audit_records.csv) | Validate against [`taxonomy/audit_codebook_v1.md`](taxonomy/audit_codebook_v1.md) |
| Generated reporting audit | [`docs/quantitative_audit.md`](docs/quantitative_audit.md) | Run `python3 scripts/build_quantitative_audit.py` and verify a clean diff |

## Reproducibility boundary

The catalog supports inspection and extension of the survey taxonomy. The
40-record audit supports claim-to-evidence counts only under its codebook; it
is not a prevalence estimate or a claim of exhaustive coverage. The repository
does not redistribute third-party datasets, model weights, or publisher PDFs,
and it does not claim that every result cited in the manuscript can be rerun
from this repository.

The v1.0 audit is single-coded. Automated validation checks its structure and
regenerates aggregate counts; it does not replace independent semantic
recoding or justify an inter-coder reliability claim.

The manuscript is submitted separately. No convenience manuscript PDF is
included in the frozen artifact, which prevents a stale draft from being
mistaken for the version whose counts cite this snapshot.

## Release practice

Create a GitHub release and archive it through a DOI-minting service (for example, Zenodo) for each manuscript revision. Add the resulting DOI to `CITATION.cff`; only add the final ACM DOI and venue metadata after they are assigned.
