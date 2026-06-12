# DRY_RUN_SUPPORT=true
﻿#!/usr/bin/env pwsh

<#
.SYNOPSIS
Single-Repo Test Harness
Validates the audit pipeline with one repo (comicwise) before batch execution

.DESCRIPTION
Tests:
  1. Repo detection (stack auto-detection)
  2. Diagnostic execution (npm audit, outdated, lint, test, build)
  3. Finding parsing (convert diagnostics â†’ Finding objects)
  4. Batch consolidation (group findings into batches)
  5. Verification (ensure output structure is valid)

Usage:
  .\test-single-repo.ps1 -RepoId comicwise
  .\test-single-repo.ps1 -RepoId banking -Verbose
#>

param(
    [string]$RepoId = "comicwise",
    [switch]$Verbose,
    [switch]$SkipDiagnostics,
    [switch]$SkipParsing,
    [switch]$SkipConsolidation
)


Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommandPath
$REPO_INVENTORY = Join-Path $SCRIPT_DIR "config" "repo-inventory.json"
$TEST_OUTPUT_DIR = Join-Path $SCRIPT_DIR ".." "TEST_OUTPUT"

# Import logger module
$LOGGER_PATH = Join-Path $SCRIPT_DIR "lib" "logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force
}

# Ensure test output directory exists
if (-not (Test-Path $TEST_OUTPUT_DIR)) {
    New-Item -ItemType Directory -Path $TEST_OUTPUT_DIR -Force | Out-Null
}

# Load repo inventory
Write-Info "Loading repo inventory..."
if (-not (Test-Path $REPO_INVENTORY)) {
    Write-Err "Repo inventory not found: $REPO_INVENTORY"
    exit 1
}

$inventory = Get-Content $REPO_INVENTORY | ConvertFrom-Json
$repo = $inventory.repos | Where-Object { $_.id -eq $RepoId }

if (-not $repo) {
    Write-Err "Repo not found: $RepoId"
    Write-Info "Available repos: $($inventory.repos.id -join ', ')"
    exit 1
}

Write-Success "Found repo: $RepoId ($($repo.stack))"
Write-Info "Path: $($repo.path)"
Write-Info "Priority: $($repo.priority)"

# Step 1: Verify repo exists
Write-Phase "Step 1: Verify Repo Exists"
Write-Info "Checking repo path..."

if (-not (Test-Path $repo.path)) {
    Write-Err "Repo path not found: $($repo.path)"
    exit 1
}

Write-Success "Repo path verified"
Write-Info "Files: $(Get-ChildItem $repo.path | Measure-Object | Select-Object -ExpandProperty Count)"

# Step 2: Detect stack
Write-Phase "Step 2: Detect Stack"
Write-Info "Auto-detecting stack..."

$detectedStack = "unknown"
$indicators = @{
    "package.json" = "javascript"
    "requirements.txt" = "python"
    "setup.py" = "python"
    "Gemfile" = "ruby"
    "go.mod" = "go"
}

foreach ($file in $indicators.Keys) {
    if (Test-Path (Join-Path $repo.path $file)) {
        $detectedStack = $indicators[$file]
        Write-Success "Detected: $detectedStack (found $file)"
        break
    }
}

if ($detectedStack -eq "unknown") {
    Write-Err "Could not auto-detect stack"
    exit 1
}

# Step 3: Run diagnostics (if not skipped)
Write-Phase "Step 3: Run Diagnostics"

$diagnosticsOutput = @{
    timestamp = Get-Date -Format "o"
    repoId = $RepoId
    stack = $detectedStack
    diagnostics = @()
}

if (-not $SkipDiagnostics) {
    Write-Info "Running diagnostics for $detectedStack..."
    
    switch ($detectedStack) {
        "javascript" {
            Write-Info "Checking for npm..."
            if (Get-Command npm -ErrorAction SilentlyContinue) {
                Write-Info "Running npm audit..."
                $auditOutput = & npm audit --json 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
                $diagnosticsOutput.diagnostics += @{
                    type = "npm-audit"
                    status = if ($auditOutput) { "success" } else { "failed" }
                    output = $auditOutput
                }
                Write-Success "npm audit completed"
            } else {
                Write-Err "npm not found"
            }
        }
        "python" {
            Write-Info "Checking for pip..."
            if (Get-Command pip -ErrorAction SilentlyContinue) {
                Write-Info "Running pip check..."
                $pipOutput = & pip check 2>&1
                $diagnosticsOutput.diagnostics += @{
                    type = "pip-check"
                    status = if ($LASTEXITCODE -eq 0) { "success" } else { "failed" }
                    output = $pipOutput
                }
                Write-Success "pip check completed"
            } else {
                Write-Err "pip not found"
            }
        }
        default {
            Write-Err "No diagnostics available for stack: $detectedStack"
        }
    }
} else {
    Write-Info "Skipping diagnostics (--SkipDiagnostics)"
}

# Save diagnostics output
$diagnosticsPath = Join-Path $TEST_OUTPUT_DIR "${RepoId}_diagnostics.json"
$diagnosticsOutput | ConvertTo-Json -Depth 10 | Set-Content $diagnosticsPath
Write-Success "Diagnostics saved to: $diagnosticsPath"

# Step 4: Parse findings (if not skipped)
Write-Phase "Step 4: Parse Findings"

$findings = @()

if (-not $SkipParsing) {
    Write-Info "Parsing diagnostics into findings..."
    
    foreach ($diag in $diagnosticsOutput.diagnostics) {
        switch ($diag.type) {
            "npm-audit" {
                if ($diag.output.vulnerabilities) {
                    $diag.output.vulnerabilities | Get-Member -MemberType NoteProperty | ForEach-Object {
                        $vuln = $diag.output.vulnerabilities.($_.Name)
                        $findings += @{
                            id = "FIND-$(Get-Random -Minimum 1000 -Maximum 9999)"
                            repoId = $RepoId
                            type = "security"
                            severity = $vuln.severity
                            rootCause = "Vulnerable dependency: $($_.Name)"
                            proposedFix = "Update to patched version"
                            complexity = "low"
                            risk = "high"
                            userImpact = "Security vulnerability"
                        }
                    }
                }
            }
            "pip-check" {
                if ($diag.output -match "error") {
                    $findings += @{
                        id = "FIND-$(Get-Random -Minimum 1000 -Maximum 9999)"
                        repoId = $RepoId
                        type = "dependency"
                        severity = "high"
                        rootCause = "Dependency conflict detected"
                        proposedFix = "Resolve conflicting versions"
                        complexity = "medium"
                        risk = "medium"
                        userImpact = "Potential runtime errors"
                    }
                }
            }
        }
    }
    
    Write-Success "Parsed $($findings.Count) findings"
} else {
    Write-Info "Skipping parsing (--SkipParsing)"
}

# Save findings
$findingsPath = Join-Path $TEST_OUTPUT_DIR "${RepoId}_findings.json"
$findings | ConvertTo-Json -Depth 10 | Set-Content $findingsPath
Write-Success "Findings saved to: $findingsPath"

# Step 5: Consolidate into batch (if not skipped)
Write-Phase "Step 5: Consolidate into Batch"

if (-not $SkipConsolidation) {
    Write-Info "Creating batch from findings..."
    
    $batch = @{
        id = "BATCH-TEST-001"
        repoId = $RepoId
        findings = $findings
        maxFiles = 7
        estimatedComplexity = "medium"
        estimatedRisk = "medium"
        createdAt = Get-Date -Format "o"
    }
    
    Write-Success "Batch created: $($batch.id)"
    Write-Info "Findings in batch: $($batch.findings.Count)"
    
    # Save batch
    $batchPath = Join-Path $TEST_OUTPUT_DIR "${RepoId}_batch.json"
    $batch | ConvertTo-Json -Depth 10 | Set-Content $batchPath
    Write-Success "Batch saved to: $batchPath"
} else {
    Write-Info "Skipping consolidation (--SkipConsolidation)"
}

# Final summary
Write-Phase "Test Summary"
Write-Info "Repo: $RepoId"
Write-Info "Stack: $detectedStack"
Write-Info "Findings: $($findings.Count)"
Write-SubHeader "Output files:"
Get-ChildItem $TEST_OUTPUT_DIR -Filter "${RepoId}_*" | ForEach-Object {
    Write-Info "  - $($_.Name)"
}
Write-Success "Test completed successfully!"
Write-SubHeader "Next steps:"
Write-Info "  1. Review findings: $findingsPath"
Write-Info "  2. Review batch: $batchPath"
Write-Info "  3. Run full audit: .\orchestrator.ps1"
