#!/usr/bin/env python3
"""Refresh a transparent, unreviewed discovery queue from Semantic Scholar.

The output is deliberately separate from the reviewed survey catalog. Search results
are candidates, not inclusion decisions and not taxonomy labels.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parents[1]
QUERIES = ROOT / "taxonomy" / "discovery_queries.csv"
DEFAULT_OUTPUT = ROOT / "taxonomy" / "discovery_queue.csv"
API = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,year,venue,url,externalIds,authors,publicationDate"


def fetch(query: str, limit: int) -> list[dict]:
    params = urllib.parse.urlencode({"query": query, "limit": limit, "fields": FIELDS})
    request = urllib.request.Request(
        f"{API}?{params}", headers={"User-Agent": "multi-hop-rag-survey/1.0 (literature discovery)"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.load(response).get("data", [])
        except HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise
            retry_after = error.headers.get("Retry-After")
            delay = min(float(retry_after) if retry_after else 2 ** attempt, 30)
            print(f"Transient HTTP {error.code}; retrying in {delay:g}s…")
            time.sleep(delay)
        except URLError:
            if attempt == 3:
                raise
            delay = 2 ** attempt
            print(f"Network error; retrying in {delay:g}s…")
            time.sleep(delay)
    raise RuntimeError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--per-query", type=int, default=100, choices=range(1, 101), metavar="1..100")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--pause", type=float, default=1.0, help="Seconds between API requests.")
    args = parser.parse_args()

    with QUERIES.open(encoding="utf-8", newline="") as handle:
        queries = [row for row in csv.DictReader(handle) if row["enabled"].lower() == "yes"]

    candidates: dict[str, dict[str, str]] = {}
    for index, search in enumerate(queries):
        for paper in fetch(search["query"], args.per_query):
            year = paper.get("year")
            title = (paper.get("title") or "").strip()
            if not title or not isinstance(year, int) or year < 2017:
                continue
            identifiers = paper.get("externalIds") or {}
            candidate_id = paper.get("paperId") or f"{year}:{title.lower()}"
            if candidate_id not in candidates:
                candidates[candidate_id] = {
                    "candidate_id": candidate_id,
                    "title": title,
                    "year": str(year),
                    "venue": (paper.get("venue") or "").strip(),
                    "candidate_url": (paper.get("url") or "").strip(),
                    "doi": identifiers.get("DOI", ""),
                    "arxiv_id": identifiers.get("ArXiv", ""),
                    "query_ids": search["query_id"],
                    "discovered_on": date.today().isoformat(),
                    "review_state": "unreviewed",
                    "triage_note": "Auto-discovered candidate; not yet included in the reviewed catalog.",
                }
            else:
                existing = candidates[candidate_id]
                existing["query_ids"] = ";".join(sorted(set(existing["query_ids"].split(";")) | {search["query_id"]}))
        if index < len(queries) - 1:
            time.sleep(args.pause)

    columns = [
        "candidate_id", "title", "year", "venue", "candidate_url", "doi", "arxiv_id",
        "query_ids", "discovered_on", "review_state", "triage_note",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(sorted(candidates.values(), key=lambda row: (-int(row["year"]), row["title"].casefold())))
    print(f"Wrote {len(candidates)} candidates to {args.output.relative_to(ROOT)} from {len(queries)} queries.")


if __name__ == "__main__":
    main()
