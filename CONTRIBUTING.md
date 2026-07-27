# Contributing to the Multi-Hop RAG Survey Catalog

Thank you for helping keep this survey useful and auditable. Contributions may add a method or benchmark, correct metadata, improve a label, or extend repository tooling.

## Before opening a pull request

1. Search existing rows and open issues to avoid duplicates.
2. Add a stable DOI, ACL Anthology, arXiv, or publisher URL. Do not add inaccessible or unverifiable citations.
3. Classify the work using [`docs/taxonomy.md`](docs/taxonomy.md). If the primary label is debatable, say why in the pull request.
4. Run `python3 scripts/validate_catalog.py` from the repository root.

## Catalog rules

- One row represents one paper, benchmark, or analysis—not one model checkpoint.
- Use a single `primary_estimand`; list additional effects in `secondary_estimands`.
- Use controlled vocabulary exactly as documented in the taxonomy guide.
- Prefer a canonical title and a persistent landing page over a PDF-only link.
- Keep claims descriptive. Comparative performance claims need a source and comparable setting.

## Pull request checklist

- [ ] CSV fields are valid and consistently quoted.
- [ ] The corresponding BibTeX entry uses the same `citation_key`.
- [ ] New labels have been discussed in an issue or added to the taxonomy guide.
- [ ] `python3 scripts/validate_catalog.py` succeeds.
- [ ] I have not added a publisher Version of Record without redistribution permission.

## Code and documentation

Keep changes small, explain the motivation, and preserve backward compatibility of the CSV headers. Propose schema changes in an issue before submitting a large data migration.
