# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail

# orchestrator.sh
# Thin wrapper: forward to TypeScript orchestrator entrypoint
if [ "$#" -eq 0 ]; then
  bunx tsx scripts/orchestrator.ts --help
  exit $?
else
  bunx tsx scripts/orchestrator.ts "$@"
  exit $?
fi
