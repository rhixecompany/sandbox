#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

# setup-dev.sh - ComicWise Development Setup Wrapper
# Thin orchestrator wrapper that delegates to pnpm setup
#
# Usage:
#   ./setup-dev.sh                    # Interactive setup wizard
#   ./setup-dev.sh --help             # Show help
#   ./setup-dev.sh --all              # Full setup (all tasks)
#   ./setup-dev.sh --deps             # Install/verify dependencies
#
# Exit codes:
#   0  Success
#   1  Command failed
#
# See unified-dev-setup.ts for all available options.

set -e

# Show help (passthrough to the setup runner)
if [[ "$*" == *"--help"* ]] || [[ "$*" == *"-h"* ]]; then
  echo "ComicWise Development Setup Launcher"
  echo ""
  echo "Usage:"
  echo "  ./setup-dev.sh                    # Interactive setup wizard"
  echo "  ./setup-dev.sh --all              # Full setup (all tasks)"
  echo "  ./setup-dev.sh --deps             # Install/verify dependencies"
  echo "  ./setup-dev.sh --env              # Initialize .env.local"
  echo "  ./setup-dev.sh --help             # Show this help message"
  echo ""
  echo "For complete options, run:"
  echo "  pnpm setup --help"
  echo ""
  exit 0
fi

# Delegate to pnpm setup
exec pnpm setup "$@"
