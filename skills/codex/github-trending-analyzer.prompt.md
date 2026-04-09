# Codex Skill Prompt: github-trending-analyzer

You are running inside this repository. Produce a complete Chinese GitHub Trending report.

## Goal

Generate `reports/latest.md` from GitHub Trending daily/weekly/monthly pages with full inventory, deduplication, categorization, and insights.

## Commands

```bash
bash scripts/fetch_trending.sh daily
bash scripts/fetch_trending.sh weekly
bash scripts/fetch_trending.sh monthly

python3 scripts/parse_trending.py data/daily.html -o data/daily.json
python3 scripts/parse_trending.py data/weekly.html -o data/weekly.json
python3 scripts/parse_trending.py data/monthly.html -o data/monthly.json

python3 scripts/generate_report.py --data-dir data --out reports/latest.md
```

## Output contract

- Include every discovered repo in Daily, Weekly, Monthly.
- Include cross-list duplicates.
- Include markdown tables by category.
- Include 3-5 high-level trend insights.
- Ensure all repos are linked with full GitHub URL.

## Optional follow-up

After generating the report, summarize in 6-10 bullets for social posting.
