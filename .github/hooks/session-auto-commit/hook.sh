#!/usr/bin/env bash
set -euo pipefail

[[ "${SKIP_AUTO_COMMIT:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

# Only auto-commit if in a git repo with changes
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo '{"status": "ignored"}'
  exit 0
fi

if [[ -z "$(git status --porcelain)" ]]; then
  echo '{"status": "no-changes"}'
  exit 0
fi

git add -A
if ! git commit -m "chore: auto-commit at session end [$(date -Iseconds)]" >/dev/null 2>&1; then
  echo '{"status": "commit-failed"}'
  exit 0
fi

if git push >/dev/null 2>&1; then
  echo '{"status": "committed"}'
else
  echo '{"status": "committed-local"}'
fi
