#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

# cleanup.sh - ComicWise Project Cleanup Wrapper
# Thin orchestrator wrapper that delegates to pnpm cleanup:project
#
# Usage:
#   ./cleanup.sh                     # Prompt for confirmation before cleanup
#   ./cleanup.sh --force             # Skip confirmation
#   ./cleanup.sh --dry-run           # Show what would be cleaned without executing
#   ./cleanup.sh --help              # Show help
#
# Exit codes:
#   0  Success
#   1  User cancelled or cleanup failed

set -e

# Show help
if [[ "$*" == *"--help"* ]] || [[ "$*" == *"-h"* ]]; then
  echo "ComicWise Project Cleanup Tool"
  echo ""
  echo "Usage:"
  echo "  ./cleanup.sh                     # Prompt for confirmation before cleanup"
  echo "  ./cleanup.sh --force             # Skip confirmation"
  echo "  ./cleanup.sh --dry-run           # Show what would be cleaned without executing"
  echo "  ./cleanup.sh --help              # Show this help message"
  echo ""
  echo "Removes:"
  echo "  • .next/ (Next.js build cache)"
  echo "  • .turbo/ (Turbo cache)"
  echo "  • coverage/ (Test coverage)"
  echo "  • dist/, build/ (Build artifacts)"
  echo "  • .cache/ (General cache)"
  echo "  • *.log, *.tmp, .DS_Store"
  echo ""
  exit 0
fi

# Delegate to pnpm cleanup:project
exec pnpm cleanup:project "$@"
