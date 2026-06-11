#!/usr/bin/env pwsh
# plan-ensure.ps1
# Thin PowerShell wrapper that forwards to TypeScript implementation
# Usage: ./plan-ensure.ps1 [arguments]

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $PSCommandPath
$tsPath = Join-Path $scriptDir 'plan-ensure.ts'

try {
    & bunx tsx $tsPath @Arguments
    exit $LASTEXITCODE
} catch {
    Write-Error "Failed to invoke plan-ensure: $_"
    exit 1
}
