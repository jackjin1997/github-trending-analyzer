#!/usr/bin/env python3
"""Generate Chinese markdown report for daily/weekly/monthly trending."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Dict, List

CATEGORY_RULES = [
    ("⌨️ Terminal Agents & AI Coding", [
        "agent",
        "claude",
        "codex",
        "swe",
        "skill",
        "harness",
        "hud",
        "code",
    ]),
    ("🛡️ Autonomous Security", ["security", "scan", "sherlock", "vulnerability", "pentest"]),
    ("🧠 Memory & Knowledge Management", ["memory", "rag", "knowledge", "context", "index"]),
    ("⚙️ AI Infra & Protocols", ["model", "inference", "framework", "platform", "browser", "physics", "timesfm", "bitnet"]),
    ("🔓 Prompt Engineering & Data", ["prompt", "dataset", "design language"]),
]
DEFAULT_CATEGORY = "🛠️ Productivity & Specialized Apps"


def load_json(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def classify(entry: Dict[str, str]) -> str:
    text = (entry.get("path", "") + " " + entry.get("description", "")).lower()
    for category, keywords in CATEGORY_RULES:
        if any(keyword in text for keyword in keywords):
            return category
    return DEFAULT_CATEGORY


def format_span_items(items: List[Dict[str, str]]) -> List[str]:
    lines = []
    for it in items:
        desc = it.get("description", "").strip() or "No description"
        lines.append(f"- **[{it['path']}]({it['url']})** — {desc}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--out", type=Path, default=Path("reports/latest.md"))
    args = parser.parse_args()

    spans = {
        "Daily": load_json(args.data_dir / "daily.json"),
        "Weekly": load_json(args.data_dir / "weekly.json"),
        "Monthly": load_json(args.data_dir / "monthly.json"),
    }

    # Cross-span map.
    by_repo: Dict[str, Dict[str, str]] = {}
    repo_spans: Dict[str, List[str]] = defaultdict(list)
    for span, items in spans.items():
        for item in items:
            repo = item["path"]
            by_repo[repo] = item
            repo_spans[repo].append(span[0])

    categories: Dict[str, List[str]] = defaultdict(list)
    for repo, item in by_repo.items():
        cat = classify(item)
        categories[cat].append(repo)

    lines: List[str] = []
    lines.append(f"# GitHub Trending 中文报告 ({date.today().isoformat()})")
    lines.append("")
    lines.append("## 📅 Part 1: Full Trending Lists")
    lines.append("")
    for span in ("Daily", "Weekly", "Monthly"):
        lines.append(f"### {span}")
        lines.extend(format_span_items(spans[span]))
        lines.append("")

    lines.append("### Cross-list Duplicates")
    duplicates = [repo for repo, v in repo_spans.items() if len(v) > 1]
    if duplicates:
        for repo in sorted(duplicates):
            item = by_repo[repo]
            lines.append(
                f"- **[{repo}]({item['url']})** — appears in {', '.join(repo_spans[repo])}"
            )
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## 🏗️ Part 2: Categorized Analysis")
    lines.append("")
    order = [c for c, _ in CATEGORY_RULES] + [DEFAULT_CATEGORY]
    for cat in order:
        lines.append(f"### {cat}")
        lines.append("| Project | Span | Description |")
        lines.append("| :--- | :---: | :--- |")
        for repo in sorted(categories.get(cat, [])):
            item = by_repo[repo]
            desc = item.get("description", "").strip() or "No description"
            lines.append(
                f"| **[{repo}]({item['url']})** | {'/'.join(repo_spans[repo])} | {desc} |"
            )
        if not categories.get(cat):
            lines.append("| — | — | — |")
        lines.append("")

    lines.append("## 💡 Part 3: Strategic Insights")
    lines.append("")
    lines.append("- Agent engineering and toolchain repos continue to dominate attention.")
    lines.append("- On-device/lightweight AI infrastructure momentum remains strong.")
    lines.append("- More projects package workflows and distribution, not just models.")
    lines.append("- Cross-span repeaters signal sustained interest beyond one-day spikes.")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
