# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# Orchestrator: Calls the TypeScript implementation
# shellcheck shell=bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

cd "$REPO_ROOT"
bunx tsx scripts/ts/opencode-plugin-repair.ts "$@"
