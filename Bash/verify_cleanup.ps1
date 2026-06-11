# ==============================================================================
# Cleanup Verification Script
# Version: 1.0.0
# Description: Scans directories for remaining dependency folders after cleanup.
#              Reports any folders that were not deleted.
#
# Usage:
#   .\verify_cleanup.ps1                          # Default paths
#   .\verify_cleanup.ps1 -Paths "C:\Foo","D:\Bar"  # Custom paths
#   .\verify_cleanup.ps1 -Targets "node","venv"    # Custom targets
#   .\verify_cleanup.ps1 -Depth 5                  # Custom depth
#
# Requirements:
#   - PowerShell 5.1+
# ==============================================================================

param(
    [string[]]$Paths = @(),
    [string[]]$Targets = @('node_modules', '.next', 'venv', 'myvenv', '__pycache__'),
    [int]$Depth = 10,
    [switch]$Help
)


Set-StrictMode -Version Latest
if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Full
    exit 0
}

# Resolve default paths from env var or fallback
if ($Paths.Count -eq 0) {
    if ($env:SCAN_PATHS) {
        $Paths = $env:SCAN_PATHS -split ';' | Where-Object { $_ -and (Test-Path $_) }
    }
    if ($Paths.Count -eq 0) {
        $Paths = @(
            "$env:USERPROFILE\Desktop\SandBox",
            "E:\Development",
            "C:\Projects"
        ) | Where-Object { Test-Path $_ }
    }
}

# ==============================================================================
# Main Verification Logic
# ==============================================================================

# Verify target folders don't remain
Write-Host "=== Cleanup Verification ===" -ForegroundColor Cyan

foreach ($base in $Paths) {
    Write-Host ""
    Write-Host "=== $base ===" -ForegroundColor Cyan
    
    if (-not (Test-Path -LiteralPath $base)) {
        Write-Host "PATH NOT FOUND: $base" -ForegroundColor Red
        continue
    }
    
    $result = Get-ChildItem -LiteralPath $base -Directory -Recurse -Depth $Depth -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -in $Targets }
    
    if ($result) {
        Write-Host "FOUND: $($result.Count) remaining folders" -ForegroundColor Yellow
        $result | ForEach-Object { Write-Host "  $($_.FullName)" }
    } else {
        Write-Host "CLEAN: No target folders found" -ForegroundColor Green
    }
}