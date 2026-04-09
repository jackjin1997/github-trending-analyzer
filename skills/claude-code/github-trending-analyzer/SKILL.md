---
name: github-trending-analyzer
description: Fetch, categorize, and summarize GitHub Trending projects across daily, weekly, and monthly spans in Chinese.
---

## When to use

Use this skill when the user asks for:
- GitHub trending summary
- hot/open-source projects this week
- categorized trend reports
- Chinese weekly trend digest

## Inputs

Optional arguments:
- language (default: Chinese)
- output path (default: `reports/latest.md`)

## Workflow

1. Fetch data:
   - `bash scripts/fetch_trending.sh daily`
   - `bash scripts/fetch_trending.sh weekly`
   - `bash scripts/fetch_trending.sh monthly`
2. Parse HTML into JSON:
   - `python3 scripts/parse_trending.py data/daily.html -o data/daily.json`
   - `python3 scripts/parse_trending.py data/weekly.html -o data/weekly.json`
   - `python3 scripts/parse_trending.py data/monthly.html -o data/monthly.json`
3. Generate report:
   - `python3 scripts/generate_report.py --data-dir data --out reports/latest.md`

## Output requirements

- Part 1: full Daily/Weekly/Monthly list (do not omit repos)
- Part 2: categorized markdown tables with links
- Part 3: 3-5 trend insights
- Explicit duplicate notes for repos appearing in multiple spans

## Response style

- Keep output concise and action-oriented
- Include clickable GitHub URLs for all repositories
- If scraping/parsing fails, report exact command and failure reason
