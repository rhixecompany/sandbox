#!/usr/bin/env bash
# Dependency Folder Cleanup — thin wrapper (forwards to TypeScript implementation)
set -euo pipefail
cd "$(dirname "$0")"
bunx tsx src/clean-dep.ts "$@"
