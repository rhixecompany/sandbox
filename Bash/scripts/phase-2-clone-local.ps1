<#
.SYNOPSIS
    Phase 2: Clone & Deduplicate - Using Local Repos
    
.DESCRIPTION
    Reads DISCOVERY_REPORT.json from Phase 1, validates existing local repositories,
    deduplicates by URL, and generates CLONE_REPORT.json
#>

param(
    [Parameter(Mandatory=$false)]
    [string]$DiscoveryReportPath = "REPO_AUDIT/DISCOVERY_REPORT.json"
)


Set-StrictMode -Version Latest
# Load shared modules
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "logger.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "config-loader.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "git-utils.psm1") -Force -ErrorAction Stop
$libDomain = Join-Path $PSScriptRoot "lib/domain"
Import-Module (Join-Path $libDomain "clone-service.psm1") -Force -ErrorAction Stop

$workingDir = Get-Location

# Resolve paths
if (-not (Test-Path $DiscoveryReportPath)) {
    $DiscoveryReportPath = Join-Path $workingDir $DiscoveryReportPath
}

Write-Header "Phase 2: Clone & Deduplicate (Using Local Repos)"
Write-Info "Working directory: $workingDir"
Write-Info "Discovery report: $DiscoveryReportPath"
Write-Info ""

# Load discovery report
if (-not (Test-Path $DiscoveryReportPath)) {
    Write-Error "Discovery report not found at $DiscoveryReportPath"
    exit 1
}

$discoveryReport = Get-Content $DiscoveryReportPath | ConvertFrom-Json

# Extract repositories from discovery report
$repositories = $discoveryReport.repositories

if (-not $repositories -or $repositories.Count -eq 0) {
    Write-Error "No repositories found in discovery report"
    exit 1
}

Write-Phase "Found $($repositories.Count) repositories"
Write-Phase ""

# Validate and process repositories
Write-Phase "Validating local repositories..."
$cloneResults = @()
$deduped = @{}
$validated = 0
$failed = 0

foreach ($repo in $repositories) {
    # Deduplicate by URL
    if ($deduped.ContainsKey($repo.url)) {
        Write-Warn "Skipping duplicate: $($repo.url)"
        continue
    }
    $deduped[$repo.url] = $true

    $localPath = $repo.local_path
    Write-Info "Validating: $($repo.name) at $localPath"
    
    if (-not (Test-Path $localPath)) {
        Write-Err "  ERROR: Path does not exist"
        $cloneResults += @{
            name = $repo.name
            clone_url = $repo.url
            target_path = $localPath
            success = $false
            error = "Repository path does not exist"
            attempt = 1
            duration_seconds = $null
        }
        $failed++
        continue
    }
    
    if (-not (Test-IsGitRepo -Path $localPath)) {
        Write-Err "  ERROR: Not a git repository"
        $cloneResults += @{
            name = $repo.name
            clone_url = $repo.url
            target_path = $localPath
            success = $false
            error = "Not a valid git repository (.git directory missing)"
            attempt = 1
            duration_seconds = $null
        }
        $failed++
        continue
    }
    
    Write-Success "Repository is valid"
    $cloneResults += @{
        name = $repo.name
        clone_url = $repo.url
        target_path = $localPath
        success = $true
        error = $null
        attempt = 1
        duration_seconds = 0
    }
    $validated++
}

# Generate clone report
Write-Phase "Generating clone report..."
$totalRepos = $cloneResults.Count
$successCount = ($cloneResults | Where-Object { $_.success } | Measure-Object).Count
$failureCount = $totalRepos - $successCount
$successRate = if ($totalRepos -gt 0) { [math]::Round(($successCount / $totalRepos) * 100, 2) } else { 0 }

$cloneReport = @{
    timestamp = Get-Date -Format "O"
    discovery_method = "local_filesystem_validation"
    summary = @{
        total_repos = $totalRepos
        successful_clones = $successCount
        failed_clones = $failureCount
        success_rate_percent = $successRate
    }
    details = $cloneResults
}

$outputDir = "REPO_AUDIT"
$reportPath = Join-Path $outputDir "CLONE_REPORT.json"

if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$json = $cloneReport | ConvertTo-Json -Depth 10
Set-Content -Path $reportPath -Value $json -Encoding UTF8

# Print summary
Write-SubHeader "Clone Summary"
Write-Info "Total repositories: $($cloneReport.summary.total_repos)"
Write-Success "Successful validations: $($cloneReport.summary.successful_clones)"
Write-Warn "Failed validations: $($cloneReport.summary.failed_clones)"
Write-Phase "Success rate: $($cloneReport.summary.success_rate_percent)%"

# Print failed repositories
if ($cloneReport.summary.failed_clones -gt 0) {
    Write-Err "Failed repositories:"
    $cloneReport.details | Where-Object { -not $_.success } | ForEach-Object {
        Write-Err "  - $($_.name): $($_.error)"
    }
}

Write-Success "Clone report saved to: $reportPath"
Write-Phase "Phase 2 complete!"
