#!/usr/bin/env pwsh
<#
.SYNOPSIS
Phase 2: Light Inventory - Quick snapshot of MEDIUM+LOW priority repos
.DESCRIPTION
Performs lightweight inventory scan on 13 MEDIUM+LOW repos:
- Collects basic metadata (stack, file count, size, last modified)
- Identifies obvious issues without deep diagnostics
- Generates inventory findings and saves to docs/audits/
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

# Ensure audit directory exists
Ensure-Directory -Path $AuditDir | Out-Null

# Load repo inventory
$repoData = Get-RepoInventory
$repos = $repoData.repos

# Filter to MEDIUM+LOW repos
$mediumLowRepos = $repos | Where-Object { $_.priority -in @("MEDIUM", "LOW") }

Write-Header "Phase 2: Light Inventory"
Write-Phase "Scanning $($mediumLowRepos.Count) MEDIUM+LOW repos..."

$findings = @()

foreach ($repo in $mediumLowRepos) {
    $repoId = $repo.id
    $repoPath = $repo.path
    $stack = $repo.stack

    Write-Phase "Scanning: $repoId ($stack)"

    $inventory = @{
        repo_id = $repoId
        stack = $stack
        path = $repoPath
        exists = $false
        file_count = 0
        total_size_mb = 0
        last_modified = $null
        issues = @()
    }

    # Check if repo exists
    if (Test-Path $repoPath) {
        $inventory.exists = $true

        # Count files and calculate size
        $items = Get-ChildItem -Path $repoPath -Recurse -ErrorAction SilentlyContinue
        $inventory.file_count = ($items | Measure-Object).Count
        $inventory.total_size_mb = [math]::Round(($items | Measure-Object -Property Length -Sum).Sum / 1MB, 2)

        # Get last modified date
        $lastModified = $items | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($lastModified) {
            $inventory.last_modified = $lastModified.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")
        }

        # Quick issue detection

        # Missing key files
        $missingFiles = @()
        if (-not (Test-Path "$repoPath/.gitignore")) { $missingFiles += ".gitignore" }
        if (-not (Test-Path "$repoPath/README.md") -and -not (Test-Path "$repoPath/README.txt")) { $missingFiles += "README" }

        if ($stack -match "node|javascript|typescript") {
            if (-not (Test-Path "$repoPath/package.json")) { $missingFiles += "package.json" }
        }

        if ($missingFiles.Count -gt 0) {
            $inventory.issues += @{
                type = "MISSING_FILES"
                files = $missingFiles
                severity = "MEDIUM"
            }
        }

        # Check for node_modules or venv (should be gitignored)
        $shouldIgnore = @()
        if (Test-Path "$repoPath/node_modules") { $shouldIgnore += "node_modules" }
        if (Test-Path "$repoPath/venv") { $shouldIgnore += "venv" }
        if (Test-Path "$repoPath/.venv") { $shouldIgnore += ".venv" }
        if (Test-Path "$repoPath/__pycache__") { $shouldIgnore += "__pycache__" }

        if ($shouldIgnore.Count -gt 0) {
            $inventory.issues += @{
                type = "UNIGNORED_ARTIFACTS"
                directories = $shouldIgnore
                severity = "LOW"
                note = "These should typically be in .gitignore"
            }
        }

        Write-Success "  Files: $($inventory.file_count), Size: $($inventory.total_size_mb)MB, Issues: $($inventory.issues.Count)"
    } else {
        $inventory.issues += @{
            type = "MISSING_REPO"
            severity = "CRITICAL"
        }
        Write-Err "  MISSING"
    }

    $findings += $inventory
}

# Save inventory findings
$inventoryFile = Join-Path $AuditDir "phase2_inventory_${TIMESTAMP}.json"
$findings | ConvertTo-Json | Set-Content $inventoryFile

Write-Header "Phase 2 Complete"
Write-Info "Repos scanned: $($findings.Count)"
Write-Info "Output: $inventoryFile"