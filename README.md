# GitHub Trending Analyzer

A lightweight open-source toolkit to turn GitHub Trending into a structured, Chinese report you can publish every week.

## Positioning

`github-trending-analyzer` is not just a crawler. It is a repeatable workflow for:
- full D/W/M trending inventory,
- cross-list duplicate tracking,
- categorized project analysis,
- strategic insight summary for creators and indie builders.

## Quick Start

```bash
bash scripts/fetch_trending.sh daily
bash scripts/fetch_trending.sh weekly
bash scripts/fetch_trending.sh monthly

python3 scripts/parse_trending.py data/daily.html -o data/daily.json
python3 scripts/parse_trending.py data/weekly.html -o data/weekly.json
python3 scripts/parse_trending.py data/monthly.html -o data/monthly.json

python3 scripts/generate_report.py --data-dir data --out reports/latest.md
```

Output: `reports/latest.md`

## What You Get

- **Part 1**: Full Daily/Weekly/Monthly repository lists
- **Part 2**: Categorized markdown tables with project URLs
- **Part 3**: Strategic trend observations

## Repo Structure

- `scripts/fetch_trending.sh` - fetches trending HTML
- `scripts/parse_trending.py` - parses HTML into JSON
- `scripts/generate_report.py` - generates Chinese markdown report
- `.github/workflows/weekly-report.yml` - scheduled weekly report generation
- `reports/latest.md` - latest generated output

## Distribution Loop (recommended)

1. Generate report each Monday.
2. Publish a short summary post (X / 小红书 / 即刻 / 公众号).
3. Link back to this repository.
4. Track which categories and repos get most engagement.

## License

MIT
