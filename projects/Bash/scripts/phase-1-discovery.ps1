# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Phase 1: Discovery & Validation
    Discovers repositories across organizations and generates DISCOVERY_REPORT.json
#>

param(
    [string]$ProjectRoot = (Get-Location).Path
)


Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Import logger module
$LOGGER_PATH = Join-Path -Path $PSScriptRoot -ChildPath "lib\logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force
}

Write-Phase "Phase 1: Discovery & Validation"

# Load configuration
Write-Info "Loading configuration from config/discovery-config.json..."

$configPath = Join-Path -Path $PSScriptRoot -ChildPath "config\discovery-config.json"
if (-not (Test-Path -LiteralPath $configPath)) {
    Write-Error "Configuration file not found at: $configPath"
    exit 1
}

$discoveryConfig = Get-Content -LiteralPath $configPath | ConvertFrom-Json
$orgs = $discoveryConfig.github.orgs

Write-Info "Discovering repositories..."

$allRepos = @()

# Discover repos from local filesystem
foreach ($org in $orgs) {
    Write-SubHeader "Querying org: $($org.name)"
    
    $orgPath = Join-Path -Path $ProjectRoot -ChildPath $org.name
    if (-not (Test-Path -LiteralPath $orgPath -PathType Container)) {
        Write-Warn "Org directory not found: $orgPath"
        continue
    }
    
    $repos = Get-ChildItem -LiteralPath $orgPath -Directory -ErrorAction SilentlyContinue
    
    foreach ($repo in $repos) {
        Write-Info "Processing: $($repo.Name)"
        
        $gitDir = Join-Path -Path $repo.FullName -ChildPath ".git"
        if (-not (Test-Path -LiteralPath $gitDir -PathType Container)) {
            continue
        }
        
        # Get remote URL
        $remoteUrl = ""
        try {
            $remoteUrl = & git -C $repo.FullName config --get remote.origin.url 2>$null
        } catch {
            $remoteUrl = ""
        }
        
        # Get HEAD ref
        $headRef = ""
        try {
            $headRef = & git -C $repo.FullName symbolic-ref --short HEAD 2>$null
        } catch {
            $headRef = "unknown"
        }
        
        # Get commit count
        $commitCount = 0
        try {
            $commitCount = [int]((& git -C $repo.FullName rev-list --count HEAD 2>$null) -as [string])
        } catch {
            $commitCount = 0
        }
        
        # Get last commit date
        $lastCommitDate = ""
        try {
            $lastCommitDate = & git -C $repo.FullName log -1 --format=%aI 2>$null
        } catch {
            $lastCommitDate = "unknown"
        }
        
        $repoData = @{
            name = $repo.Name
            org = $org.name
            url = $remoteUrl
            local_path = $repo.FullName
            git_head = $headRef
            commits = if ($commitCount) { $commitCount } else { 0 }
            last_commit = if ($lastCommitDate) { $lastCommitDate } else { "unknown" }
            validation = @{
                valid = $true
                errors = @()
                warnings = @()
            }
            metadata = @{
                discovered_at = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
                discovery_source = "local_filesystem"
            }
        }
        
        # Validate repo metadata
        if ($discoveryConfig.validation.check_accessibility) {
            if (-not (Test-Path -LiteralPath "$($repo.FullName)\.git" -PathType Container)) {
                $repoData.validation.valid = $false
                $repoData.validation.errors += ".git directory not accessible"
            }
        }
        
        $allRepos += $repoData
    }
    
    Write-Success "Found $($repos.Count) repos"
}

# Deduplication function
Write-Info "Validating repositories..."
Write-Info "Deduplicating repositories..."

$deduplicatedRepos = @()
$seenUrls = @{}

foreach ($repo in $allRepos) {
    $repoUrl = if ($repo.url) { $repo.url } else { $repo.name }
    
    if ($seenUrls.ContainsKey($repoUrl)) {
        Write-Verbose "Duplicate repo found and skipped: $($repo.name)"
        continue
    }
    
    $seenUrls[$repoUrl] = $true
    $deduplicatedRepos += $repo
}

Write-Success "After deduplication: $($deduplicatedRepos.Count) repos"

# Generate discovery report (simplified JSON construction)
Write-SubHeader "Generating discovery report..."

# Build valid/invalid counts
$validRepos = @($deduplicatedRepos | Where-Object { $_.validation.valid })
$invalidRepos = @($deduplicatedRepos | Where-Object { -not $_.validation.valid })

# Build org summary
$orgSummary = @()
foreach ($org in $orgs) {
    $count = @($deduplicatedRepos | Where-Object { $_.org -eq $org.name }).Count
    $orgSummary += @{
        name = $org.name
        count = $count
    }
}

# Build error summary
$errorSummary = @()
foreach ($repo in $deduplicatedRepos) {
    if ($repo.validation.errors.Count -gt 0) {
        $errorSummary += @{
            repo = $repo.name
            errors = $repo.validation.errors
        }
    }
}

# Manual JSON construction to avoid timeout
$jsonOutput = @"
{
  "timestamp": "$(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ')",
  "discovery_method": "local_filesystem_scan",
  "total_discovered": $($deduplicatedRepos.Count),
  "valid_repos": $($validRepos.Count),
  "invalid_repos": $($invalidRepos.Count),
  "organizations": [
"@

for ($i = 0; $i -lt $orgSummary.Count; $i++) {
    $org = $orgSummary[$i]
    $jsonOutput += "    { `"name`": `"$($org.name)`", `"count`": $($org.count) }"
    if ($i -lt $orgSummary.Count - 1) { $jsonOutput += "," }
    $jsonOutput += "`n"
}

$jsonOutput += @"
  ],
  "repositories": [
"@

for ($i = 0; $i -lt $deduplicatedRepos.Count; $i++) {
    $repo = $deduplicatedRepos[$i]
    $jsonOutput += @"
    {
      "name": "$($repo.name)",
      "org": "$($repo.org)",
      "url": "$($repo.url -replace '"', '\"')",
      "local_path": "$($repo.local_path -replace '\\', '\\')",
      "git_head": "$($repo.git_head)",
      "commits": $($repo.commits),
      "last_commit": "$($repo.last_commit)",
      "validation": {
        "valid": $(if ($repo.validation.valid) { 'true' } else { 'false' }),
        "errors": [],
        "warnings": []
      },
      "metadata": {
        "discovered_at": "$($repo.metadata.discovered_at)",
        "discovery_source": "$($repo.metadata.discovery_source)"
      }
    }
"@
    if ($i -lt $deduplicatedRepos.Count - 1) { $jsonOutput += "," }
    $jsonOutput += "`n"
}

$jsonOutput += @"
  ],
  "validation_summary": {
    "all_valid": $(if ($invalidRepos.Count -eq 0) { 'true' } else { 'false' }),
    "invalid_count": $($invalidRepos.Count),
    "errors": []
  }
}
"@

# Ensure output directory exists
$outputPath = $discoveryConfig.output.report_file
if ([string]::IsNullOrEmpty($outputPath)) {
    $outputPath = "REPO_AUDIT/DISCOVERY_REPORT.json"
}
$outputDir = Split-Path -Parent $outputPath
if ([string]::IsNullOrEmpty($outputDir)) {
    $outputDir = "REPO_AUDIT"
}

if (-not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

# Save report
$reportPath = Join-Path -Path $ProjectRoot -ChildPath $outputPath
Set-Content -LiteralPath $reportPath -Value $jsonOutput -Encoding UTF8

Write-Success "Discovery report saved to: $reportPath"

# Phase 1 Summary
Write-Phase "Phase 1 Summary"
Write-Info "Total repos discovered: $($deduplicatedRepos.Count)"
Write-Info "Valid repos: $($validRepos.Count)"
Write-Info "Invalid repos: $($invalidRepos.Count)"
Write-Info "All repos valid: $(if ($invalidRepos.Count -eq 0) { 'YES' } else { 'NO' })"

Write-Success "Phase 1 complete!"
