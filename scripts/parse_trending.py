#!/usr/bin/env python3
"""Parse GitHub Trending HTML into structured JSON."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from html import unescape
from pathlib import Path
from typing import List


@dataclass
class RepoEntry:
    path: str
    url: str
    description: str


def parse_trending_html(content: str) -> List[RepoEntry]:
    rows = re.findall(
        r'<article[^>]*class="[^"]*Box-row[^"]*"[^>]*>(.*?)</article>',
        content,
        flags=re.S,
    )

    result: List[RepoEntry] = []
    for row in rows:
        repo_match = re.search(
            r'<h2[^>]*>.*?<a[^>]*href="/([^"/]+/[^"/]+)"', row, flags=re.S
        )
        if not repo_match:
            continue

        repo = repo_match.group(1).strip()

        desc = ""
        desc_match = re.search(
            r'<p[^>]*class="[^"]*color-fg-muted[^"]*"[^>]*>(.*?)</p>',
            row,
            flags=re.S,
        )
        if desc_match:
            desc_text = re.sub(r"<[^>]+>", " ", desc_match.group(1))
            desc = unescape(" ".join(desc_text.split()))

        result.append(
            RepoEntry(
                path=repo,
                url=f"https://github.com/{repo}",
                description=desc,
            )
        )

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_file", type=Path)
    parser.add_argument("--output", "-o", type=Path)
    args = parser.parse_args()

    content = args.html_file.read_text(encoding="utf-8")
    repos = parse_trending_html(content)

    payload = [asdict(repo) for repo in repos]
    if args.output:
        args.output.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
