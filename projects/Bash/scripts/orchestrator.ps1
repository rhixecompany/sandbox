# DRY_RUN_SUPPORT=true
﻿#!/usr/bin/env pwsh

<#
.SYNOPSIS
Interactive Audit Orchestration Menu
Allows selective phase execution, re-runs, and batch management

.DESCRIPTION
Master control panel for the 5-phase Rhixe audit system.
Supports:
  - Run all phases sequentially
  - Run individual phases
  - Re-run failed phases
  - Skip phases
  - Review outputs
  - Clean up logs
#>

param(
    [switch]$AutoRun,
    [string]$Phase,
    [switch]$SkipPhase1,
    [switch]$SkipPhase2,
    [switch]$SkipPhase3,
    [switch]$SkipPhase4,
    [switch]$SkipPhase5
)

# Support DryRun via env or --dry-run switch
param(
    [switch]$DryRun
)


Set-StrictMode -Version Latest
# Load shared logger module
Import-Module (Join-Path $PSScriptRoot "lib/core/logger.psm1") -Force
Import-Module (Join-Path $PSScriptRoot "lib/core/dir-manager.psm1") -Force

$ErrorActionPreference = "Continue"
$TIMESTAMP = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$SCRIPT_DIR = Get-Location
$AUDIT_DIR = Join-Path $SCRIPT_DIR ".." "docs" "audits"
$BATCH_LOGS = Join-Path $SCRIPT_DIR ".." "BATCH_LOGS"

# Ensure directories exist
Ensure-Directory $AUDIT_DIR
Ensure-Directory $BATCH_LOGS

if ($env:DRY_RUN -eq 'true' -or $DryRun.IsPresent) {
    Write-Host "DRY-RUN: Orchestrator would run phases (no side effects)."
    exit 0
}

function Show-Menu {
    Write-Header "Rhixe Audit Orchestration Menu"
    Write-Success "1. Run all phases (1-5)"
    Write-Phase "2. Run Phase 1 only (Deep Triage)"
    Write-Phase "3. Run Phase 2 only (Light Inventory)"
    Write-Phase "4. Run Phase 3 only (Consolidation)"
    Write-Phase "5. Run Phase 4 only (Batch Executor)"
    Write-Phase "6. Run Phase 5 only (Final Summary)"
    Write-Phase "7. Run Phases 3-5 (skip diagnostics)"
    Write-Info "8. Review audit outputs"
    Write-Err "9. Clean up logs"
    Write-Info "0. Exit"
}

function Run-Phase {
    param(
        [int]$PhaseNum,
        [string]$ScriptName,
        [string]$Description
    )
    
    Write-Phase "Phase ${PhaseNum}: $Description"
    
    $scriptPath = Join-Path $SCRIPT_DIR $ScriptName
    
    if (-not (Test-Path $scriptPath)) {
        Write-Error "Script not found: $scriptPath"
        return $false
    }
    
    try {
        if ($scriptPath -match "\.sh$") {
            # Try bash, but fall back to PowerShell equivalent
            if (Get-Command bash -ErrorAction SilentlyContinue) {
                bash $scriptPath
            } else {
                # Use PowerShell equivalent
                $psScript = $scriptPath -replace '\.sh$', '.ps1'
                if (Test-Path $psScript) {
                    & $psScript
                } else {
                    Write-Warning "Neither bash nor PowerShell equivalent found for $scriptPath"
                    return $false
                }
            }
        } elseif ($scriptPath -match "\.js$") {
            & node $scriptPath
        } else {
            & $scriptPath
        }
        Write-Success "Phase $PhaseNum completed"
        return $true
    } catch {
        Write-Warning "Phase $PhaseNum had issues: $_"
        return $false
    }
}

function Run-AllPhases {
    Write-Header "Running All Phases (1-5)"
    
    $results = @()
    
    if (-not $SkipPhase1) {
        $results += @{ Phase = 1; Success = (Run-Phase 1 "phase-1-deep-triage.ps1" "Deep Triage") }
    }
    
    if (-not $SkipPhase2) {
        $results += @{ Phase = 2; Success = (Run-Phase 2 "phase-2-light-inventory.ps1" "Light Inventory") }
    }
    
    if (-not $SkipPhase3) {
        $results += @{ Phase = 3; Success = (Run-Phase 3 "phase-3-triage.ps1" "Consolidation") }
    }
    
    if (-not $SkipPhase4) {
        $results += @{ Phase = 4; Success = (Run-Phase 4 "phase-4-debug.ps1" "Batch Executor") }
    }
    
    if (-not $SkipPhase5) {
        $results += @{ Phase = 5; Success = (Run-Phase 5 "phase-5-remediation.ps1" "Final Summary") }
    }
    
    Write-Header "Audit Summary"
    $results | ForEach-Object {
        $status = if ($_.Success) { "âœ“ PASS" } else { "âœ— FAIL" }
        Write-Info "Phase $($_.Phase): $status"
    }

    $passed = ($results | Where-Object { $_.Success }).Count
    $total = $results.Count
    if ($passed -eq $total) {
        Write-Success "Result: $passed/$total phases passed"
    } else {
        Write-Phase "Result: $passed/$total phases passed"
    }
}

function Show-Outputs {
    Write-Header "Audit Outputs"

    Write-Phase "Audit Findings:"
    if (Test-Path $AUDIT_DIR) {
        Get-ChildItem $AUDIT_DIR -ErrorAction SilentlyContinue | ForEach-Object {
            Write-Info "  - $($_.Name)"
        }
    } else {
        Write-Warning "No audit findings yet"
    }

    Write-Phase "Batch Logs:"
    if (Test-Path $BATCH_LOGS) {
        Get-ChildItem $BATCH_LOGS -ErrorAction SilentlyContinue | ForEach-Object {
            Write-Info "  - $($_.Name)"
        }
    } else {
        Write-Warning "No batch logs yet"
    }

    Write-Phase "Reports:"
    @("CONSOLIDATED_PROPOSED_FIXES.md", "BATCHES.json", "FINAL_AUDIT_SUMMARY.md") | ForEach-Object {
        $path = Join-Path $SCRIPT_DIR ".." $_
        if (Test-Path $path) {
            Write-Success "$_"
        } else {
            Write-Warning "$_ (not yet generated)"
        }
    }
}

function Clean-Logs {
    Write-Header "Cleaning Logs"
    
    $confirm = Read-Host "Delete all batch logs and audit findings? (yes/no)"
    if ($confirm -eq "yes") {
        Remove-Item $BATCH_LOGS -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item $AUDIT_DIR -Recurse -Force -ErrorAction SilentlyContinue
        Write-Success "Logs cleaned"
    } else {
        Write-Warning "Cleanup cancelled"
    }
}

# Main loop
if ($AutoRun) {
    Run-AllPhases
} elseif ($Phase) {
    switch ($Phase) {
        "1" { Run-Phase 1 "phase-1-deep-triage.sh" "Deep Triage" }
        "2" { Run-Phase 2 "phase-2-light-inventory.sh" "Light Inventory" }
        "3" { Run-Phase 3 "phase-3-triage.ps1" "Consolidation" }
        "4" { Run-Phase 4 "phase-4-debug.ps1" "Batch Executor" }
        "5" { Run-Phase 5 "phase-5-remediation.ps1" "Final Summary" }
        default { Write-Error "Unknown phase: $Phase" }
    }
} else {
    # Interactive menu
    do {
        Show-Menu
        $choice = Read-Host "Select option"
        
        switch ($choice) {
            "1" { Run-AllPhases }
            "2" { Run-Phase 1 "phase-1-deep-triage.sh" "Deep Triage" }
            "3" { Run-Phase 2 "phase-2-light-inventory.sh" "Light Inventory" }
            "4" { Run-Phase 3 "phase-3-triage.ps1" "Consolidation" }
            "5" { Run-Phase 4 "phase-4-debug.ps1" "Batch Executor" }
            "6" { Run-Phase 5 "phase-5-remediation.ps1" "Final Summary" }
            "7" { 
                Write-Phase "Running Phases 3-5 (skipping diagnostics)"
                Run-Phase 3 "phase-3-triage.ps1" "Consolidation"
                Run-Phase 4 "phase-4-debug.ps1" "Batch Executor"
                Run-Phase 5 "phase-5-remediation.ps1" "Final Summary"
            }
            "8" { Show-Outputs }
            "9" { Clean-Logs }
            "0" {
                Write-Info "Exiting..."
                exit 0
            }
            default { Write-Error "Invalid option" }
        }
        
        if ($choice -ne "0") {
            Read-Host "Press Enter to continue"
        }
    } while ($true)
}
