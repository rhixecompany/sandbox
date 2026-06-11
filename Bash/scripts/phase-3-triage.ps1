param([object]$Config)


Set-StrictMode -Version Latest
# Load shared modules
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "path-utils.psm1") -Force
Import-Module (Join-Path $libCore "config-loader.psm1") -Force
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force
Import-Module (Join-Path $libCore "git-utils.psm1") -Force
Import-Module (Join-Path $libCore "logger.psm1") -Force

# Load domain modules
$libDomain = Join-Path $PSScriptRoot "lib/domain"
Import-Module (Join-Path $libDomain "triage-service.psm1") -Force
Import-Module (Join-Path $libDomain "scanning-service.psm1") -Force

# Load existing lib files (these are still needed for package manager detection and repo analysis)
. (Join-Path $PSScriptRoot "lib/repo-analyzer.ps1")
. (Join-Path $PSScriptRoot "lib/package-managers.ps1")
. (Join-Path $PSScriptRoot "lib/package-manager-scanners.ps1")
. (Join-Path $PSScriptRoot "lib/dependency-scanner.ps1")

Write-Header "Phase 3: Triage & Catalog"

# Load triage config using shared module
$triageConfig = Get-TriageConfig -ConfigPath (Join-Path $PSScriptRoot "config/triage-config.json")
Write-Success "Loaded triage config"

# Determine paths
if ($Config) {
    $baseDir = $Config.paths.base
    $outputDir = Join-Path $baseDir $Config.paths.output
} else {
    # Default paths: CLONE_REPORT is in ./.. /REPO_AUDIT (relative to scripts dir)
    $baseDir = Split-Path -Parent $PSScriptRoot
    $outputDir = Join-Path $baseDir "REPO_AUDIT"
}

# Ensure output directory exists
Ensure-Directory -Path $outputDir

# Load clone report
$cloneReportPath = Join-Path $outputDir "CLONE_REPORT.json"

if (-not (Test-Path $cloneReportPath)) {
    Write-Error "Clone report not found: $cloneReportPath"
    Write-Warn "Please run Phase 2 first"
    exit 1
}

Write-Phase "Loading clone report from: $cloneReportPath"
$cloneReport = Get-Content $cloneReportPath | ConvertFrom-Json

# Extract cloned repos (handle both "repos" and "details" keys)
if ($cloneReport.repos) {
    $clonedRepos = $cloneReport.repos | Where-Object { $_.clone_status.success }
} elseif ($cloneReport.details) {
    $clonedRepos = $cloneReport.details | Where-Object { $_.success }
} else {
    Write-Error "Unknown CLONE_REPORT structure"
    exit 1
}

Write-Phase "Analyzing $($clonedRepos.Count) cloned repositories..."

# Analyze each repo
$triageResults = @()

foreach ($repo in $clonedRepos) {
    $repoName = $repo.name
    $repoPath = $repo.target_path
    
    Write-Info "Analyzing: $repoName"

    # Verify repo path exists
    if (-not (Test-Path $repoPath)) {
        Write-Warn "  Repository path not found: $repoPath. Skipping."
        continue
    }
    
    # Get repo metadata
    $metadata = Get-RepositoryMetadata -RepoPath $repoPath -RepoName $repoName
    
    # Get dependency vulnerabilities using shared scanning service
    $scanResult = Invoke-StackScan -RepoPath $repoPath -IncludeStdout $false
    
    # Extract vulnerabilities and per-manager breakdown
    $vulnerabilities = $scanResult.managers
    $totalVulnerabilities = $scanResult.total_vulnerabilities
    $detectedManagers = $scanResult.detected_managers
    
    # Get issue count from GitHub (placeholder - would use GitHub API in real implementation)
    $issueCount = 0
    
    # Get days since last commit
    $daysSinceLastCommit = if ($metadata.commit_history) {
        $metadata.commit_history.days_since_last_commit
    } else {
        -1
    }
    
    # Calculate health score using shared module
    $healthScore = Get-HealthScore -IssueCount $issueCount -VulnerabilityCount $totalVulnerabilities -DaysSinceLastCommit $daysSinceLastCommit -TriageConfig $triageConfig

    $healthCategory = Get-HealthCategory -HealthScore $healthScore

    Write-Info "  Health Score: $healthScore/100 ($healthCategory)"
    
    $triageResults += @{
        name = $repoName
        org = if ($repo.org) { $repo.org } else { "unknown" }
        url = if ($repo.url) { $repo.url } else { $repo.clone_url }
        path = $repoPath
        metadata = $metadata
        issue_count = $issueCount
        vulnerabilities = $vulnerabilities
        detected_managers = $detectedManagers
        total_vulnerabilities = $totalVulnerabilities
        days_since_last_commit = $daysSinceLastCommit
        health_score = $healthScore
        health_category = $healthCategory
    }
}

if ($triageResults.Count -eq 0) {
    Write-Error "No repositories were analyzed successfully"
    exit 1
}

# Generate triage report using shared module
Write-Info "Generating triage report..."
$triageReport = New-TriageReport -TriageResults $triageResults

# Save triage report
$triageReportPath = Join-Path $outputDir "TRIAGE_REPORT.json"
$triageReport | ConvertTo-Json -Depth 10 | Set-Content $triageReportPath
Write-Success "Triage report saved to: $triageReportPath"

# Generate catalog markdown using shared module
Write-Info "Generating catalog..."
$catalogMarkdown = Format-CatalogMarkdown -TriageReport $triageReport

# Save catalog
$catalogPath = Join-Path $outputDir "CATALOG.md"
$catalogMarkdown | Set-Content $catalogPath
Write-Success "Catalog saved to: $catalogPath"

# Summary
Write-SubHeader "Phase 3 Summary"
Write-Info "Repositories analyzed: $($triageReport.summary.total_repos)"
Write-Info "Average health score: $([math]::Round($triageReport.summary.average_health_score, 2))/100"
Write-Info "Health distribution:"
Write-Success "  - Healthy: $($triageReport.summary.health_distribution.healthy)"
Write-Info "  - Caution: $($triageReport.summary.health_distribution.caution)"
Write-Warn "  - Warning: $($triageReport.summary.health_distribution.warning)"
Write-Err "  - Critical: $($triageReport.summary.health_distribution.critical)"

Write-Success "Phase 3 complete!"
