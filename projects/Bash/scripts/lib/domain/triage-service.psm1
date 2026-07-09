#Requires -Version 5.1
<#
.SYNOPSIS
    Triage service module for repository health assessment

.DESCRIPTION
    Provides functions to assess repository health, run dependency
    scans, and generate triage reports. Uses dependency-scanner.ps1
    for vulnerability scanning and git-utils for commit analysis.
#>

#region Module Dependencies
Import-Module (Join-Path $PSScriptRoot '../core/path-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/git-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/logger.psm1') -Force

# Load lib files (dot-sourced as they are scripts, not modules)
$libPath = Join-Path $PSScriptRoot '../'
. (Join-Path $libPath 'dependency-scanner.ps1')
. (Join-Path $libPath 'package-managers.ps1')
#endregion

#region Public Functions

function Get-HealthScore {
    <#
    .SYNOPSIS
        Calculates repository health score based on issues and vulnerabilities

    .DESCRIPTION
        Implements the health score formula: 100 - (issues * 2) - (vulns * 5) - stale deduction
        - Issues: multiplied by 2
        - Vulnerabilities: multiplied by 5
        - Stale: additional deduction for repos with no recent commits

    .PARAMETER Issues
        Number of issues found in the repository

    .PARAMETER Vulnerabilities
        Number of vulnerabilities found

    .PARAMETER DaysSinceLastCommit
        Number of days since the last commit

    .OUTPUTS
        Integer health score (0-100)

    .EXAMPLE
        $score = Get-HealthScore -Issues 5 -Vulnerabilities 2 -DaysSinceLastCommit 30
    #>
    [CmdletBinding()]
    [OutputType([int])]
    param(
        [Parameter(Mandatory=$false)]
        [int]$Issues = 0,

        [Parameter(Mandatory=$false)]
        [int]$Vulnerabilities = 0,

        [Parameter(Mandatory=$false)]
        [int]$DaysSinceLastCommit = -1
    )

    $score = 100

    # Deduct for issues (2 points each)
    $score -= ($Issues * 2)

    # Deduct for vulnerabilities (5 points each)
    $score -= ($Vulnerabilities * 5)

    # Stale deduction: additional 10 points if no commits in 180+ days
    if ($DaysSinceLastCommit -ge 180) {
        $score -= 10
    }
    # Additional 5 points if no commits in 365+ days
    elseif ($DaysSinceLastCommit -ge 365) {
        $score -= 5
    }

    # Ensure score is within bounds
    if ($score -lt 0) { $score = 0 }
    if ($score -gt 100) { $score = 100 }

    return $score
}

function Get-HealthCategory {
    <#
    .SYNOPSIS
        Returns health category based on score thresholds

    .DESCRIPTION
        Categorizes a health score into one of four categories:
        - Healthy: 80-100
        - Caution: 60-79
        - Warning: 40-59
        - Critical: 0-39

    .PARAMETER Score
        Health score to categorize

    .OUTPUTS
        String category name

    .EXAMPLE
        $category = Get-HealthCategory -Score 75
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory=$true)]
        [int]$Score
    )

    if ($Score -ge 80) {
        return "Healthy"
    }
    elseif ($Score -ge 60) {
        return "Caution"
    }
    elseif ($Score -ge 40) {
        return "Warning"
    }
    else {
        return "Critical"
    }
}

function Invoke-DependencyScan {
    <#
    .SYNOPSIS
        Runs dependency vulnerability scans on a repository

    .DESCRIPTION
        Uses Invoke-AllScanners from dependency-scanner.ps1 to run
        all available vulnerability scanners for detected package managers.

    .PARAMETER RepoPath
        Path to the repository to scan

    .PARAMETER IncludeStdout
        If $true, includes full scanner output in results

    .OUTPUTS
        Hashtable with scan results

    .EXAMPLE
        $scan = Invoke-DependencyScan -RepoPath "C:\repos\myapp"
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath,

        [Parameter(Mandatory=$false)]
        [bool]$IncludeStdout = $false
    )

    if (-not (Test-Path $RepoPath)) {
        Write-Warn "Repository path does not exist: $RepoPath"
        return $null
    }

    try {
        $result = Invoke-AllScanners -RepoPath $RepoPath -IncludeStdout $IncludeStdout
        return $result
    }
    catch {
        Write-Err "Dependency scan failed: $($_.Exception.Message)"
        return @{
            repo_path = $RepoPath
            status = "error"
            error = $_.Exception.Message
        }
    }
}

function Get-TriageResult {
    <#
    .SYNOPSIS
        Assembles a single repository's triage result

    .DESCRIPTION
        Combines health score, vulnerabilities, detected package managers,
        and days since last commit into a comprehensive triage result.

    .PARAMETER RepoPath
        Path to the repository

    .PARAMETER RepoName
        Name of the repository

    .OUTPUTS
        Hashtable with complete triage result

    .EXAMPLE
        $result = Get-TriageResult -RepoPath "C:\repos\myapp" -RepoName "myapp"
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath,

        [Parameter(Mandatory=$true)]
        [string]$RepoName
    )

    if (-not (Test-Path $RepoPath)) {
        return $null
    }

    # Get git info
    $gitInfo = Get-GitInfo -RepoPath $RepoPath
    $daysSinceCommit = if ($gitInfo) { $gitInfo.days_since_last_commit } else { -1 }

    # Detect package managers
    $managers = Detect-PackageManagers -RepoPath $RepoPath

    # Run dependency scan
    $scanResult = Invoke-DependencyScan -RepoPath $RepoPath

    $vulns = 0
    if ($scanResult -and $scanResult.total_vulnerabilities) {
        $vulns = $scanResult.total_vulnerabilities
    }

    # Calculate health score
    $healthScore = Get-HealthScore -Issues 0 -Vulnerabilities $vulns -DaysSinceLastCommit $daysSinceCommit

    # Get health category
    $healthCategory = Get-HealthCategory -Score $healthScore

    $result = @{
        name = $RepoName
        path = $RepoPath
        health_score = $healthScore
        health_category = $healthCategory
        vulnerabilities = $vulns
        package_managers = $managers
        days_since_last_commit = $daysSinceCommit
        scan_result = $scanResult
    }

    return $result
}

function New-TriageReport {
    <#
    .SYNOPSIS
        Builds a full triage report with summary statistics

    .DESCRIPTION
        Takes an array of triage results and assembles a comprehensive
        report with summary statistics across all repositories.

    .PARAMETER Results
        Array of triage result hashtables

    .OUTPUTS
        Hashtable representing the triage report

    .EXAMPLE
        $report = New-TriageReport -Results $triageResults
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Results
    )

    $healthy = ($Results | Where-Object { $_.health_category -eq "Healthy" }).Count
    $caution = ($Results | Where-Object { $_.health_category -eq "Caution" }).Count
    $warning = ($Results | Where-Object { $_.health_category -eq "Warning" }).Count
    $critical = ($Results | Where-Object { $_.health_category -eq "Critical" }).Count

    $totalVulns = ($Results | Measure-Object -Property vulnerabilities -Sum).Sum

    $report = @{
        timestamp = (Get-Date -Format "o")
        total_repos = $Results.Count
        summary = @{
            healthy = $healthy
            caution = $caution
            warning = $warning
            critical = $critical
            total_vulnerabilities = $totalVulns
            average_health_score = [math]::Round(($Results | Measure-Object -Property health_score -Average).Average, 2)
        }
        results = $Results
    }

    return $report
}

function Format-CatalogMarkdown {
    <#
    .SYNOPSIS
        Generates CATALOG.md markdown from triage report

    .DESCRIPTION
        Creates a formatted markdown document from triage results,
        suitable for documentation or reporting purposes.

    .PARAMETER Report
        Triage report hashtable from New-TriageReport

    .PARAMETER Title
        Optional title for the catalog

    .OUTPUTS
        String containing markdown formatted catalog

    .EXAMPLE
        $markdown = Format-CatalogMarkdown -Report $triageReport
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Report,

        [Parameter(Mandatory=$false)]
        [string]$Title = "Repository Catalog"
    )

    $sb = [System.Text.StringBuilder]::new()

    [void]$sb.AppendLine("# $Title")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')")
    [void]$sb.AppendLine("")

    # Summary section
    [void]$sb.AppendLine("## Summary")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("| Metric | Count |")
    [void]$sb.AppendLine("|--------|-------|")
    [void]$sb.AppendLine("| Total Repositories | $($Report.total_repos) |")
    [void]$sb.AppendLine("| Healthy | $($Report.summary.healthy) |")
    [void]$sb.AppendLine("| Caution | $($Report.summary.caution) |")
    [void]$sb.AppendLine("| Warning | $($Report.summary.warning) |")
    [void]$sb.AppendLine("| Critical | $($Report.summary.critical) |")
    [void]$sb.AppendLine("| Total Vulnerabilities | $($Report.summary.total_vulnerabilities) |")
    [void]$sb.AppendLine("| Average Health Score | $($Report.summary.average_health_score) |")
    [void]$sb.AppendLine("")

    # Repository table
    [void]$sb.AppendLine("## Repositories")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("| Name | Health Score | Category | Vulnerabilities | Package Managers | Days Since Commit |")
    [void]$sb.AppendLine("|------|---------------|----------|-----------------|------------------|-------------------|")

    foreach ($result in $Report.results) {
        $managers = if ($result.package_managers.Count -gt 0) { $result.package_managers -join ", " } else { "None" }
        $days = if ($result.days_since_last_commit -ge 0) { $result.days_since_last_commit } else { "N/A" }

        [void]$sb.AppendLine("| $($result.name) | $($result.health_score) | $($result.health_category) | $($result.vulnerabilities) | $managers | $days |")
    }

    [void]$sb.AppendLine("")

    return $sb.ToString()
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Get-HealthScore'
    'Get-HealthCategory'
    'Invoke-DependencyScan'
    'Get-TriageResult'
    'New-TriageReport'
    'Format-CatalogMarkdown'
)
#endregion