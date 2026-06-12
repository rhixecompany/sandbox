# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

# dev.sh - ComicWise Development Wrapper
# Thin orchestrator wrapper that delegates to pnpm dev
#
# Usage:
#   ./dev.sh                    # Start dev server
#   ./dev.sh --help             # Show help
#
# Exit codes:
#   0  Success
#   1  Command failed

set -e

# Show help
if [[ "$*" == *"--help"* ]] || [[ "$*" == *"-h"* ]]; then
  echo "ComicWise Development Server Launcher"
  echo ""
  echo "Usage:"
  echo "  ./dev.sh                    # Start dev server"
  echo "  ./dev.sh --help             # Show this help message"
  echo ""
  echo "For more setup options, use:"
  echo "  ./setup-dev.sh              # Initialize dev environment"
  echo ""
  exit 0
fi

# Delegate to pnpm dev
exec pnpm dev
