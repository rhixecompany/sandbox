# DRY_RUN_SUPPORT=true
﻿#!/usr/bin/env pwsh
<#
.SYNOPSIS
Phase 1: Deep Triage - Scan CRITICAL+HIGH priority repos for issues
.DESCRIPTION
Performs deep diagnostics on 4 CRITICAL+HIGH repos:
- comicwise (CRITICAL)
- banking (HIGH)
- rhixe_scans (HIGH)
- university-libary-jsm (HIGH)

Generates diagnostic findings and saves to docs/audits/
#>

param(
    [string]$AuditDir = "../docs/audits",
    [string]$ConfigFile = "./config/repo-inventory.json"
)


Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"
$TIMESTAMP = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

# Load shared modules
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "logger.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "config-loader.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "git-utils.psm1") -Force -ErrorAction Stop
$libDomain = Join-Path $PSScriptRoot "lib/domain"
Import-Module (Join-Path $libDomain "discovery-service.psm1") -Force -ErrorAction Stop

# Load repo inventory
$repoData = Get-RepoInventory
$repos = $repoData.repos

# Ensure audit directory exists
Ensure-Directory -Path $AuditDir | Out-Null

# Filter to CRITICAL+HIGH repos
$criticalHighRepos = $repos | Where-Object { $_.priority -in @("CRITICAL", "HIGH") }

Write-Header "Phase 1: Deep Triage"
Write-Phase "Scanning $($criticalHighRepos.Count) CRITICAL+HIGH repos..."

$findings = @()

foreach ($repo in $criticalHighRepos) {
    $repoId = $repo.id
    $repoPath = $repo.path
    $stack = $repo.stack

    Write-Phase "Scanning: $repoId ($stack)"

    $repoFindings = @()

    # Check if repo exists
    if (-not (Test-Path $repoPath)) {
        $repoFindings += @{
            type = "MISSING_REPO"
            severity = "CRITICAL"
            description = "Repository directory not found"
            path = $repoPath
            proposed_fix = "Clone or restore repository"
            complexity = "LOW"
            risk = "HIGH"
        }
    } else {
        # Scan for common issues

        # 1. Check for missing package files
        if ($stack -match "node|javascript|typescript") {
            if (-not (Test-Path "$repoPath/package.json")) {
                $repoFindings += @{
                    type = "MISSING_PACKAGE_JSON"
                    severity = "CRITICAL"
                    description = "Node.js project missing package.json"
                    path = "$repoPath/package.json"
                    proposed_fix = "Create package.json or restore from version control"
                    complexity = "MEDIUM"
                    risk = "HIGH"
                }
            }

            # Check for node_modules
            if ((Test-Path "$repoPath/node_modules") -and (Get-ChildItem "$repoPath/node_modules" -ErrorAction SilentlyContinue | Measure-Object).Count -eq 0) {
                $repoFindings += @{
                    type = "EMPTY_NODE_MODULES"
                    severity = "HIGH"
                    description = "node_modules directory exists but is empty"
                    path = "$repoPath/node_modules"
                    proposed_fix = "Run 'npm install' to restore dependencies"
                    complexity = "LOW"
                    risk = "MEDIUM"
                }
            }
        }

        # 2. Check for Python issues
        if ($stack -match "python|django|flask") {
            if (-not (Test-Path "$repoPath/requirements.txt") -and -not (Test-Path "$repoPath/setup.py") -and -not (Test-Path "$repoPath/pyproject.toml")) {
                $repoFindings += @{
                    type = "MISSING_PYTHON_DEPS"
                    severity = "HIGH"
                    description = "Python project missing dependency file (requirements.txt, setup.py, or pyproject.toml)"
                    path = $repoPath
                    proposed_fix = "Create requirements.txt or pyproject.toml"
                    complexity = "MEDIUM"
                    risk = "HIGH"
                }
            }
        }

        # 3. Check for .gitignore
        if (-not (Test-Path "$repoPath/.gitignore")) {
            $repoFindings += @{
                type = "MISSING_GITIGNORE"
                severity = "MEDIUM"
                description = "Repository missing .gitignore file"
                path = "$repoPath/.gitignore"
                proposed_fix = "Create .gitignore with appropriate patterns for stack"
                complexity = "LOW"
                risk = "MEDIUM"
            }
        }

        # 4. Check for README
        if (-not (Test-Path "$repoPath/README.md") -and -not (Test-Path "$repoPath/README.txt")) {
            $repoFindings += @{
                type = "MISSING_README"
                severity = "MEDIUM"
                description = "Repository missing README documentation"
                path = "$repoPath/README.md"
                proposed_fix = "Create comprehensive README.md"
                complexity = "MEDIUM"
                risk = "LOW"
            }
        }

        # 5. Check for large files (>100MB)
        $largeFiles = Get-ChildItem -Path $repoPath -Recurse -ErrorAction SilentlyContinue |
            Where-Object { $_.Length -gt 100MB } |
            Select-Object -First 5

        if ($largeFiles) {
            $repoFindings += @{
                type = "LARGE_FILES"
                severity = "MEDIUM"
                description = "Repository contains large files (>100MB)"
                path = ($largeFiles | ForEach-Object { $_.FullName } | Join-String -Separator ", ")
                proposed_fix = "Move large files to external storage or use Git LFS"
                complexity = "MEDIUM"
                risk = "MEDIUM"
            }
        }

        # 6. Check for outdated dependencies (basic check)
        if (Test-Path "$repoPath/package.json") {
            $packageJson = Get-Content "$repoPath/package.json" | ConvertFrom-Json
            if ($packageJson.dependencies -or $packageJson.devDependencies) {
                # Count dependencies
                $depCount = ($packageJson.dependencies | Get-Member -MemberType NoteProperty | Measure-Object).Count
                $devDepCount = ($packageJson.devDependencies | Get-Member -MemberType NoteProperty | Measure-Object).Count

                if ($depCount -gt 50 -or $devDepCount -gt 50) {
                    $repoFindings += @{
                        type = "EXCESSIVE_DEPENDENCIES"
                        severity = "MEDIUM"
                        description = "Project has excessive dependencies ($depCount prod, $devDepCount dev)"
                        path = "$repoPath/package.json"
                        proposed_fix = "Audit and remove unused dependencies"
                        complexity = "HIGH"
                        risk = "MEDIUM"
                    }
                }
            }
        }
    }

    # Save findings for this repo
    if ($repoFindings.Count -gt 0) {
        $diagnosticFile = Join-Path $AuditDir "${repoId}_diagnostic_${TIMESTAMP}.json"
        $repoFindings | ConvertTo-Json | Set-Content $diagnosticFile
        Write-Success "  Found $($repoFindings.Count) issues"
        $findings += $repoFindings
    } else {
        Write-Success "  No issues found"
    }
}

# Save consolidated findings
$consolidatedFile = Join-Path $AuditDir "phase1_findings_${TIMESTAMP}.json"
$findings | ConvertTo-Json | Set-Content $consolidatedFile

Write-Header "Phase 1 Complete"
Write-Info "Total findings: $($findings.Count)"
Write-Info "Output: $consolidatedFile"
