#!/usr/bin/env bash
# Cache Cleaner — thin wrapper (forwards to TypeScript implementation)
set -euo pipefail
cd "$(dirname "$0")"
bunx tsx src/cache-clean.ts "$@"
