# GitHub Trending Analyzer

Turn GitHub Trending into a publish-ready Chinese intelligence brief in minutes.

`github-trending-analyzer` helps creators and indie builders generate consistent D/W/M trend reports with categorization, deduplication, and strategic insights.

## Why this project

Most people can scrape Trending. Few can turn it into an output loop that is:
- repeatable every week,
- readable in Chinese,
- shareable to X / 即刻 / 公众号,
- useful for product and content decisions.

This repo is built for that loop.

## What makes it different

- **Full inventory, no omissions**: keep Daily / Weekly / Monthly lists complete
- **Cross-list dedupe**: highlight repos appearing in multiple spans
- **Category-first analysis**: group projects into practical AI buckets
- **Ready-to-publish markdown**: direct output for newsletters and social posts

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

## Output format

Generated report includes:
- **Part 1**: Full Daily / Weekly / Monthly lists
- **Part 2**: Categorized tables (`Project | Span | Description`)
- **Part 3**: Strategic insights (3-5 trend observations)

## Repository structure

- `scripts/fetch_trending.sh` - Fetch trending HTML pages
- `scripts/parse_trending.py` - Parse HTML into structured JSON
- `scripts/generate_report.py` - Generate Chinese markdown report
- `.github/workflows/weekly-report.yml` - Weekly automation via GitHub Actions
- `reports/latest.md` - Latest generated sample report

## Growth loop (recommended)

1. Generate report every Monday.
2. Publish one short summary post and one long-form weekly post.
3. Link back to this repo and highlight 1-2 standout projects.
4. Track which categories get most engagement, then refine taxonomy.

## Roadmap

- [ ] Add "new this week" vs "dropped" delta section
- [ ] Add language-level slices (Python / TS / Go / Rust)
- [ ] Add optional JSON API output for downstream tools
- [ ] Add richer scoring for momentum and consistency

## Contributing

Issues and PRs are welcome. If you have ideas for better categorization or report templates, open an issue.

## License

MIT
