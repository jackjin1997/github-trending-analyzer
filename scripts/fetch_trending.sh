#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="$ROOT_DIR/data"

SPAN="${1:-daily}"
case "$SPAN" in
  daily|weekly|monthly) ;;
  *)
    echo "Usage: $0 [daily|weekly|monthly]"
    exit 1
    ;;
esac

mkdir -p "$DATA_DIR"

URL="https://github.com/trending?since=${SPAN}"
OUT_HTML="$DATA_DIR/${SPAN}.html"

echo "Fetching GitHub trending (${SPAN})..."
curl -fsSL "$URL" \
  -H "User-Agent: github-trending-analyzer/0.1" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -o "$OUT_HTML"

echo "Saved to $OUT_HTML"
