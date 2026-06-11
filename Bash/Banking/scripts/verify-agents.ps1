#!/usr/bin/env pwsh
# verify-agents.ps1
# Thin PowerShell wrapper that forwards to TypeScript implementation
# Usage: ./verify-agents.ps1 [arguments]

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$tsPath = Join-Path $scriptDir 'ts' 'verify-agents.ts'

try {
    & bunx tsx $tsPath @Arguments
    exit $LASTEXITCODE
} catch {
    Write-Error "Failed to invoke verify-agents: $_"
    exit 1
}
