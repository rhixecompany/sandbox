# DRY_RUN_SUPPORT=true
﻿#!/usr/bin/env pwsh
param([String[]]$Args)

Set-StrictMode -Version Latest
# If no args provided, default to --list
if (-not $Args -or $Args.Count -eq 0) {
    bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts --list --catalog-path .opencode/mcp_servers.json
} else {
    bunx tsx scripts/ts/entrypoints/opencode-mcp-cli.ts @Args
}
