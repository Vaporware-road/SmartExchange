#!/usr/bin/env python3
"""Search the mirrored aiogram docs. Agents should run this instead of loading the whole tree."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def reference_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "reference"


def score_file(path: Path, terms: list[str], text: str) -> tuple[int, list[str]]:
    lower = text.lower()
    score = 0
    snippets: list[str] = []
    for term in terms:
        count = lower.count(term)
        if count:
            score += count * (3 if term in path.stem.lower() else 1)
            idx = lower.find(term)
            start = max(0, idx - 60)
            end = min(len(text), idx + len(term) + 80)
            snippets.append(re.sub(r"\s+", " ", text[start:end]).strip())
    return score, snippets[:2]


def search(query: str, limit: int) -> list[dict]:
    ref = reference_dir()
    root = ref / "aiogram"
    if not root.is_dir():
        raise SystemExit(f"No mirrored docs at {root}. Run scrape_aiogram_docs.sh first.")

    terms = [t.lower() for t in re.split(r"\s+", query.strip()) if t]
    if not terms:
        raise SystemExit("Empty query")

    hits: list[tuple[int, Path, list[str], str]] = []
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        score, snippets = score_file(path, terms, text)
        if score:
            title = path.stem
            for line in text.splitlines()[:5]:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            hits.append((score, path, snippets, title))

    hits.sort(key=lambda h: (-h[0], str(h[1])))
    results = []
    for score, path, snippets, title in hits[:limit]:
        rel = path.relative_to(ref).as_posix()
        results.append(
            {
                "score": score,
                "title": title,
                "path": rel,
                "snippets": snippets,
            }
        )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="Search terms")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    query = " ".join(args.query)
    results = search(query, args.limit)
    if args.json:
        json.dump(results, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return
    if not results:
        print(f"No hits for: {query}")
        return
    print(f"Hits for: {query}\n")
    for i, hit in enumerate(results, 1):
        print(f"{i}. {hit['title']}  (score={hit['score']})")
        print(f"   path: {hit['path']}")
        for snip in hit["snippets"]:
            print(f"   … {snip}")
        print()


if __name__ == "__main__":
    main()
