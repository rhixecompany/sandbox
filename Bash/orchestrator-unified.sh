# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# orchestrator-unified.sh — thin wrapper, forwards to PowerShell orchestrator

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

pwsh -NoProfile -ExecutionPolicy Bypass -Command "& '$SCRIPT_DIR/orchestrator-unified.ps1' $@"
exit $?
