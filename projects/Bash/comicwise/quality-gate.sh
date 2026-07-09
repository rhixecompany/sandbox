# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# quality-gate.sh — thin wrapper, delegates to pnpm quality:gate:sh

set -euo pipefail

exec pnpm quality:gate:sh "$@"
