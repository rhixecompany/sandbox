#!/usr/bin/env bash
# shellcheck shell=bash
set -euo pipefail

# opencode-mcp.sh
if [ "$#" -eq 0 ]; then
  bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts --list --catalog-path .opencode/mcp_servers.json
  exit $?
else
  bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts "$@"
  exit $?
fi
