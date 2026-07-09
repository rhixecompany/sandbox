# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# Git Commit Batches — thin wrapper (forwards to TypeScript implementation)

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cd "$SCRIPT_DIR"

bunx tsx src/git-commit-batches.ts "$@"
exit $?
