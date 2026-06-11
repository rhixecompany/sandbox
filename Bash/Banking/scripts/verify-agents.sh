#!/usr/bin/env bash
# shellcheck shell=bash
# verify-agents.sh
# Thin Bash wrapper that forwards to TypeScript implementation

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

cd "$REPO_ROOT"
bunx tsx scripts/ts/verify-agents.ts "$@"
exit $?
