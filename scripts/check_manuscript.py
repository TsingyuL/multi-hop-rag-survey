#!/usr/bin/env python3
"""Fail on manuscript metadata defects that can invalidate a release."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


ENTRY_START = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
FIELD = re.compile(r"(?ms)^\s*(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}\s*,?")


def entries(text: str) -> list[tuple[str, dict[str, str]]]:
    starts = list(ENTRY_START.finditer(text))
    parsed: list[tuple[str, dict[str, str]]] = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[match.end():end]
        fields = {name.lower(): value.strip() for name, value in FIELD.findall(block)}
        parsed.append((match.group(2), fields))
    return parsed


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"[{}\\]", "", value).lower())


def validate_bib(path: Path) -> list[str]:
    parsed = entries(path.read_text(encoding="utf-8"))
    failures: list[str] = []
    titles: dict[str, list[str]] = defaultdict(list)
    for key, fields in parsed:
        title = fields.get("title", "")
        if title:
            titles[normalized_title(title)].append(key)
        year = fields.get("year", "")
        if not re.fullmatch(r"\d{4}", year):
            failures.append(f"{key}: missing or malformed four-digit year")
        elif not 1950 <= int(year) <= 2026:
            failures.append(f"{key}: suspicious year {year}")
    for keys in titles.values():
        if len(keys) > 1:
            failures.append(f"duplicate BibTeX title: {', '.join(keys)}")
    placeholders = [key for key, fields in parsed if "and others" in fields.get("author", "").lower()]
    if placeholders:
        print(f"Metadata warning: {len(placeholders)} entries still use 'and others'; prioritize frequently cited entries.")
    print(f"BibTeX metadata checked: {len(parsed)} entries.")
    return failures


def validate_log(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing LaTeX log: {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    patterns = {
        "undefined references": r"There were undefined references|Reference `[^']+' .* undefined",
        "undefined citations": r"There were undefined citations|Citation `[^']+' .* undefined",
        "multiply-defined labels": r"multiply defined",
    }
    return [label for label, pattern in patterns.items() if re.search(pattern, text, re.IGNORECASE)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bib", type=Path, required=True)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    failures = validate_bib(args.bib)
    if args.log:
        failures.extend(validate_log(args.log))
    if failures:
        for failure in failures:
            print(f"Manuscript check failed: {failure}", file=sys.stderr)
        return 1
    print("Manuscript checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
