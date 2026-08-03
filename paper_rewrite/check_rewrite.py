#!/usr/bin/env python3
"""Static checks for the functional-taxonomy manuscript rewrite."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BIB_FILES = [
    ROOT / "references.bib",
    ROOT / "references_methods.bib",
    ROOT / "references_figure.bib",
    ROOT / "references_harness.bib",
    ROOT / "references_expansion_initial.bib",
    ROOT / "references_expansion_followup.bib",
    ROOT / "references_expansion_integration.bib",
    ROOT / "references_expansion_feedback.bib",
]


def collect_tex() -> list[Path]:
    return sorted(ROOT.rglob("*.tex"))


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        escaped = False
        kept: list[str] = []
        for char in line:
            if char == "%" and not escaped:
                break
            kept.append(char)
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        lines.append("".join(kept))
    return "\n".join(lines)


def parse_citations(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\cite(?!style)\w*\{([^}]*)\}", text):
        keys.update(k.strip() for k in match.group(1).split(",") if k.strip())
    return keys


def parse_bibkeys(text: str) -> list[str]:
    return re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text)


def resolve_input(source: Path, raw: str) -> Path:
    candidate = source.parent / raw
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    if candidate.exists():
        return candidate
    candidate = ROOT / raw
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    return candidate


def check_inputs(tex_files: list[Path]) -> list[str]:
    missing: list[str] = []
    for source in tex_files:
        text = strip_comments(source.read_text(encoding="utf-8"))
        for raw in re.findall(r"\\input\{([^}]+)\}", text):
            path = resolve_input(source, raw)
            if not path.exists():
                missing.append(f"{source.relative_to(ROOT)} -> {raw}")
    return sorted(set(missing))


def main() -> int:
    tex_files = collect_tex()
    tex_text = "\n".join(
        strip_comments(path.read_text(encoding="utf-8")) for path in tex_files
    )
    citations = parse_citations(tex_text)
    bibkeys: list[str] = []
    for path in BIB_FILES:
        if not path.exists():
            print(f"ERROR: missing bibliography file: {path.name}")
            return 1
        bibkeys.extend(parse_bibkeys(path.read_text(encoding="utf-8")))

    duplicates = sorted(k for k, n in Counter(bibkeys).items() if n > 1)
    undefined = sorted(citations - set(bibkeys))
    missing_inputs = check_inputs(tex_files)
    placeholders = [
        str(path.relative_to(ROOT))
        for path in tex_files
        if "% TODO" in path.read_text(encoding="utf-8")
        or "% Cover " in path.read_text(encoding="utf-8")
    ]

    errors = 0
    if duplicates:
        errors += 1
        print("ERROR: duplicate BibTeX keys:")
        for key in duplicates:
            print(f"  - {key}")
    if undefined:
        errors += 1
        print("ERROR: undefined citation keys:")
        for key in undefined:
            print(f"  - {key}")
    if missing_inputs:
        errors += 1
        print("ERROR: missing input files:")
        for path in missing_inputs:
            print(f"  - {path}")
    if placeholders:
        print("WARNING: placeholder comments remain in:")
        for path in placeholders:
            print(f"  - {path}")

    print(
        f"Checked {len(tex_files)} TeX files, {len(citations)} cited keys, "
        f"and {len(set(bibkeys))} unique bibliography entries."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
