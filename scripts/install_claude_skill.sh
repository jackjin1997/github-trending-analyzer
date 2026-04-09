#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT_DIR/skills/claude-code/github-trending-analyzer/SKILL.md"
DEST_DIR="$HOME/.claude/skills/github-trending-analyzer"
DEST="$DEST_DIR/SKILL.md"

FORCE="false"
DRY_RUN="false"

for arg in "$@"; do
  case "$arg" in
    --force) FORCE="true" ;;
    --dry-run) DRY_RUN="true" ;;
    *)
      echo "Unknown option: $arg"
      echo "Usage: $0 [--force] [--dry-run]"
      exit 1
      ;;
  esac
done

if [ ! -f "$SRC" ]; then
  echo "Source skill file not found: $SRC"
  exit 1
fi

if [ "$DRY_RUN" = "true" ]; then
  echo "[dry-run] would create: $DEST_DIR"
  echo "[dry-run] would copy: $SRC -> $DEST"
  exit 0
fi

mkdir -p "$DEST_DIR"

if [ -f "$DEST" ] && [ "$FORCE" != "true" ]; then
  echo "Skill already exists: $DEST"
  echo "Re-run with --force to overwrite."
  exit 0
fi

cp "$SRC" "$DEST"

echo "Installed Claude Code skill: github-trending-analyzer"
echo "Location: $DEST"
echo "Use it in Claude Code with: /github-trending-analyzer"
