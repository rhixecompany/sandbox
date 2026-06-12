# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Phase 2: Clone & Deduplicate - Main script
    
.DESCRIPTION
    Reads DISCOVERY_REPORT.json from Phase 1, clones all repositories,
    handles retries, deduplicates by URL, and generates CLONE_REPORT.json
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$DiscoveryReportPath = "REPO_AUDIT/DISCOVERY_REPORT.json",
    
    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "scripts/config/clone-config.json",
    
    [Parameter(Mandatory=$false)]
    [switch]$DryRun
)


Set-StrictMode -Version Latest
# Determine script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workingDir = Get-Location

# Resolve paths
if (-not (Test-Path $ConfigPath)) {
    $ConfigPath = Join-Path $scriptDir $ConfigPath
}
if (-not (Test-Path $DiscoveryReportPath)) {
    $DiscoveryReportPath = Join-Path $workingDir $DiscoveryReportPath
}

# Load shared modules
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "path-utils.psm1") -Force
Import-Module (Join-Path $libCore "config-loader.psm1") -Force
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force
Import-Module (Join-Path $libCore "git-utils.psm1") -Force
Import-Module (Join-Path $libCore "logger.psm1") -Force

# Load domain modules
$libDomain = Join-Path $PSScriptRoot "lib/domain"
Import-Module (Join-Path $libDomain "clone-service.psm1") -Force
Import-Module (Join-Path $libDomain "discovery-service.psm1") -Force

Write-Header "Phase 2: Clone & Deduplicate"
if ($env:DRY_RUN -eq 'true' -or $DryRun.IsPresent) {
    Write-Host "DRY-RUN: Phase 2 (clone) would run; no side effects performed."
    exit 0
}
Write-Info "Script directory: $scriptDir"
Write-Info "Working directory: $workingDir"
Write-Info "Discovery report: $DiscoveryReportPath"
Write-Info "Config path: $ConfigPath"
Write-Info ""

# Load configuration using shared module
Write-Info "Loading libraries..."
$cloneConfig = Get-CloneConfig -ConfigPath $ConfigPath
$discoveryReport = Get-DiscoveryConfig -DiscoveryReportPath $DiscoveryReportPath
Write-Success "Libraries loaded successfully"
Write-Info ""

# Extract repositories from discovery report
$repositories = $discoveryReport.repositories

if (-not $repositories -or $repositories.Count -eq 0) {
    Write-Err "No repositories found in discovery report"
    exit 1
}

Write-Phase "Found $($repositories.Count) repositories to clone"
Write-Info ""

# Create base directory
$baseDir = $cloneConfig.clone.base_directory
Ensure-Directory -Path $baseDir

# Clone repositories
Write-Phase "Starting clone operations..."
$cloneStartTime = Get-Date

# Progress callback
$progressCallback = {
    param($Repository, $Index, $Total)
    Write-Progress-Custom -Message "[$Index/$Total] Cloning: $($Repository.name) from $($Repository.clone_url)"
}

# Convert repositories to array of custom objects if needed
$repoArray = @()
foreach ($repo in $repositories) {
    $repoArray += @{
        name = $repo.name
        clone_url = $repo.url
    }
}

# Perform clone batch
$cloneResults = Invoke-GitCloneBatch `
    -Repositories $repoArray `
    -BaseDirectory $baseDir `
    -TimeoutSeconds $cloneConfig.clone.timeout_seconds `
    -MaxRetries $cloneConfig.clone.max_retries `
    -ProgressCallback $progressCallback

$cloneEndTime = Get-Date
$cloneDuration = ($cloneEndTime - $cloneStartTime).TotalSeconds

# Generate clone report
Write-Info ""
Write-Info "Generating clone report..."

$outputDir = $cloneConfig.clone.output_directory
$reportPath = Join-Path $outputDir $cloneConfig.clone.report_filename

Ensure-Directory -Path $outputDir

$cloneReport = ConvertTo-CloneReport -CloneResults $cloneResults -ReportPath $reportPath

# Print summary
Write-Info ""
Write-SubHeader "Clone Summary"
Write-Info "Total repositories: $($cloneReport.summary.total_repos)"
Write-Info "Successful clones: $($cloneReport.summary.successful_clones)"
Write-Info "Failed clones: $($cloneReport.summary.failed_clones)"
Write-Phase "Success rate: $($cloneReport.summary.success_rate_percent)%"
Write-Info "Total duration: $([math]::Round($cloneDuration, 2)) seconds"
Write-Info ""

# Print failed repositories
if ($cloneReport.summary.failed_clones -gt 0) {
    Write-Err "Failed repositories:"
    $cloneReport.details | Where-Object { -not $_.success } | ForEach-Object {
        Write-Err "  - $($_.name): $($_.error)"
    }
    Write-Info ""
}

Write-Success "Clone report saved to: $reportPath"
Write-Success "Phase 2 complete!"
