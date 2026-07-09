# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# Package Manager Upgrade — thin wrapper (forwards to TypeScript implementation)
set -euo pipefail
cd "$(dirname "$0")"
bunx tsx src/upgrade.ts "$@"
