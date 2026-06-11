#!/usr/bin/env pwsh
# orchestrator.ps1
# Thin PowerShell wrapper that forwards to TypeScript implementation
# Usage: ./orchestrator.ps1 [arguments]

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$tsPath = Join-Path $scriptDir 'orchestrator.ts'

try {
    & bunx tsx $tsPath @Arguments
    exit $LASTEXITCODE
} catch {
    Write-Error "Failed to invoke orchestrator: $_"
    exit 1
}
