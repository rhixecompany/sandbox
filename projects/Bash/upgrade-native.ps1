# DRY_RUN_SUPPORT=true
﻿# ==============================================================================
# Native PowerShell Package Manager Upgrade Script
# Version: 3.0.0
# Description: Updates and upgrades packages via winget and chocolatey using
#              native PowerShell commands. No bash required. Includes colored
#              output, detailed logging, error handling, and summary reports.
#
# Usage:
#   .\upgrade-native.ps1              Run normal upgrade
#   .\upgrade-native.ps1 -DebugMode    Run with debug output
#   .\upgrade-native.ps1 -SkipWinget   Skip winget, only run chocolatey
#   .\upgrade-native.ps1 -SkipChoco    Skip chocolatey, only run winget
#   .\upgrade-native.ps1 -Help         Show help message
#
# Requirements:
#   - PowerShell 5.1+
#   - winget (Windows Package Manager) and/or chocolatey
#
# Exit Codes:
#   0 - Success
#   1 - All operations failed
# ==============================================================================

param(
    [switch]$DebugMode,
    [switch]$SkipWinget,
    [switch]$SkipChoco,
    [switch]$Help
)


Set-StrictMode -Version Latest
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LogDir = Join-Path $ScriptDir "logs"
$LogFile = Join-Path $LogDir "upgrade_native_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"

$Colors = @{
    Red = "`e[0;31m"
    Green = "`e[0;32m"
    Yellow = "`e[1;33m"
    Blue = "`e[0;34m"
    Cyan = "`e[0;36m"
    Bold = "`e[1m"
    NC = "`e[0m"
}

function Write-ColorOutput {
    param($Message, $Color = "White", [switch]$NoLog)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $colorCode = $Colors[$Color]
    Write-Host "$colorCode[$timestamp] $Message$($Colors['NC'])"
    if (-not $NoLog) {
        Add-Content -Path $LogFile -Value "[$timestamp] $Message" -ErrorAction SilentlyContinue
    }
}

function Write-DebugMsg {
    param($Message)
    if ($DebugMode) {
        Write-ColorOutput "DEBUG: $Message" "Cyan" -NoLog
    }
}

function Write-Info { param($Message) Write-ColorOutput "â„¹ $Message" "Blue" }
function Write-Success { param($Message) Write-ColorOutput "âœ“ $Message" "Green" }
function Write-Warning { param($Message) Write-ColorOutput "âš  $Message" "Yellow" }
function Write-Error { param($Message) Write-ColorOutput "âœ— $Message" "Red" }

function Write-Header {
    param($Title)
    Write-Host ""
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])===============================================================$($Colors['NC'])"
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])  $Title$($Colors['NC'])"
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])===============================================================$($Colors['NC'])"
    Write-Host ""
}

function Initialize-Logging {
    if (-not (Test-Path $LogDir)) {
        New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
    }
    $header = "========================================"
    Add-Content -Path $LogFile -Value $header
    Add-Content -Path $LogFile -Value "Native PowerShell Execution - $(Get-Date)"
    Add-Content -Path $LogFile -Value $header
    Write-Info "Logging to: $LogFile"
}

function Test-CommandAvailable {
    param($Command)
    try {
        $null = Get-Command $Command -ErrorAction SilentlyContinue
        return $true
    } catch {
        return $false
    }
}

function Invoke-SafeCommand {
    param($Command, $Description, $ScriptBlock)
    Write-Info "Running: $Description"
    Write-DebugMsg "Command: $Command"
    try {
        $output = & $ScriptBlock 2>&1
        $exitCode = $LASTEXITCODE
        $output | ForEach-Object { Add-Content -Path $LogFile -Value "  $_" -ErrorAction SilentlyContinue }
        if ($exitCode -eq 0 -or $null -eq $exitCode) {
            Write-Success "$Description completed successfully"
            return @{ Success = $true; ExitCode = 0 }
        } else {
            Write-Error "$Description failed with exit code: $exitCode"
            return @{ Success = $false; ExitCode = $exitCode }
        }
    } catch {
        Write-Error "$Description failed: $_"
        return @{ Success = $false; ExitCode = 1 }
    }
}

function Test-WingetAvailable {
    if (Test-CommandAvailable "winget") {
        try {
            $version = winget --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Success "Winget is available (version: $version)"
                return $true
            }
        } catch {
            Write-Warning "Winget command found but not properly configured"
        }
    }
    Write-Warning "Winget is not installed"
    return $false
}

function Test-ChocoAvailable {
    if (Test-CommandAvailable "choco") {
        try {
            $version = choco --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Success "Chocolatey is available (version: $version)"
                return $true
            }
        } catch {
            Write-Warning "Chocolatey command found but not properly configured"
        }
    }
    Write-Warning "Chocolatey is not installed"
    return $false
}

function Invoke-WingetUpdate {
    param([switch]$Skip)
    if ($Skip) {
        Write-Warning "Skipping winget update (requested)"
        return @{ Success = $true; ExitCode = 0 }
    }
    Write-Header "Winget Update Phase"
    if (-not (Test-WingetAvailable)) {
        Write-Warning "Skipping winget update - not available"
        return @{ Success = $false; ExitCode = 1 }
    }
    Write-Info "Checking for winget updates..."
    $result = Invoke-SafeCommand -Command "winget update --accept-source-agreements" -Description "Winget Update" -ScriptBlock {
        winget update --accept-source-agreements 2>&1
    }
    return $result
}

function Invoke-WingetUpgrade {
    param([switch]$Skip)
    if ($Skip) {
        Write-Warning "Skipping winget upgrade (requested)"
        return @{ Success = $true; ExitCode = 0 }
    }
    Write-Header "Winget Upgrade Phase"
    if (-not (Test-WingetAvailable)) {
        Write-Warning "Skipping winget upgrade - not available"
        return @{ Success = $false; ExitCode = 1 }
    }
    Write-Info "Upgrading all winget packages..."
    $result = Invoke-SafeCommand -Command "winget upgrade --accept-source-agreements --accept-package-agreements" -Description "Winget Upgrade All" -ScriptBlock {
        winget upgrade --accept-source-agreements --accept-package-agreements 2>&1
    }
    return $result
}

function Invoke-ChocoUpgrade {
    param([switch]$Skip)
    if ($Skip) {
        Write-Warning "Skipping chocolatey upgrade (requested)"
        return @{ Success = $true; ExitCode = 0 }
    }
    Write-Header "Chocolatey Upgrade Phase"
    if (-not (Test-ChocoAvailable)) {
        Write-Warning "Skipping chocolatey upgrade - not available"
        return @{ Success = $false; ExitCode = 1 }
    }
    Write-Info "Upgrading all chocolatey packages..."
    $result = Invoke-SafeCommand -Command "choco upgrade all -y" -Description "Chocolatey Upgrade All" -ScriptBlock {
        choco upgrade all -y 2>&1
    }
    return $result
}

function Clear-Logs {
    param([string]$LogDir, [int]$MaxLogs = 10)
    if (Test-Path $LogDir) {
        $logs = Get-ChildItem -Path $LogDir -Filter "*.log" | Sort-Object LastWriteTime -Descending
        if ($logs.Count -gt $MaxLogs) {
            $logs | Select-Object -Skip $MaxLogs | Remove-Item -Force
            Write-Info "Cleared old logs: removed $($logs.Count - $MaxLogs) old log files"
        }
    }
}

function Show-Summary {
    Write-Header "Execution Summary"
    $endTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Info "Script completed at: $endTime"
    Write-Success "All package manager operations finished"
    Write-Info "Log file saved to: $LogFile"
    Write-Host ""
    Write-Host "$($Colors['Bold'])Next steps:$($Colors['NC'])"
    Write-Host "  - Review the log file for details" -ForegroundColor Gray
    Write-Host "  - Restart any applications that were updated" -ForegroundColor Gray
    Write-Host "  - Check for any pending system reboots" -ForegroundColor Gray
    Write-Host ""
}

function Show-Help {
    Write-Host ""
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])Package Manager Upgrade Script v3.0.0 - Help$($Colors['NC'])" -ForegroundColor Cyan
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])=====================================================$($Colors['NC'])" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage: .\upgrade-native.ps1 [Options]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -DebugMode   Enable debug output"
    Write-Host "  -SkipWinget  Skip winget updates"
    Write-Host "  -SkipChoco   Skip chocolatey updates"
    Write-Host "  -Help        Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\upgrade-native.ps1              Run normal upgrade"
    Write-Host "  .\upgrade-native.ps1 -DebugMode    Run with debug output"
    Write-Host "  .\upgrade-native.ps1 -SkipWinget   Skip winget, only run chocolatey"
    Write-Host "  .\upgrade-native.ps1 -SkipChoco    Skip chocolatey, only run winget"
    Write-Host ""
}

function Main {
    if ($Help) {
        Show-Help
        return 0
    }

    $startTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host ""
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])===============================================================$($Colors['NC'])"
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])  Package Manager Upgrade Script v3.0.0       $($Colors['NC'])"
    Write-Host "$($Colors['Bold'])$($Colors['Cyan'])===============================================================$($Colors['NC'])"
    Write-Host ""
    Initialize-Logging
    Write-Info "Script started at: $startTime"
    Write-Info "Debug mode: $(if ($DebugMode) { 'ENABLED' } else { 'DISABLED' })"
    Write-Info "Skip Winget: $SkipWinget"
    Write-Info "Skip Choco: $SkipChoco"
    Write-DebugMsg "Operating System: $([System.Environment]::OSVersion.VersionString)"
    Write-DebugMsg "PowerShell: $($PSVersionTable.PSVersion)"
    Write-DebugMsg "User: $env:USERNAME"
    
    # Track success status
    $anySuccess = $false
    
    $wingetUpdateResult = Invoke-WingetUpdate -Skip:$SkipWinget
    if ($wingetUpdateResult.Success) { $anySuccess = $true }
    
    $wingetUpgradeResult = Invoke-WingetUpgrade -Skip:$SkipWinget
    if ($wingetUpgradeResult.Success) { $anySuccess = $true }
    
    $chocoUpgradeResult = Invoke-ChocoUpgrade -Skip:$SkipChoco
    if ($chocoUpgradeResult.Success) { $anySuccess = $true }
    
    Show-Summary

    # Clear old logs - keep last 10
    Clear-Logs -LogDir $LogDir

    if (-not $anySuccess) {
        Write-Error "All package manager operations failed"
        return 1
    }
    return 0
}

$exitCode = Main
exit $exitCode
