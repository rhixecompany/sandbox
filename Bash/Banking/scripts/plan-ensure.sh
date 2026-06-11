#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail

# Usage: ./plan-ensure.sh
if [ "$#" -eq 0 ]; then
  bunx tsx scripts/plan-ensure.ts --help
  exit $?
else
  bunx tsx scripts/plan-ensure.ts "$@"
  exit $?
fi
