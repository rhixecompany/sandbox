# Triage utility functions for Phase 3 analysis

# Calculate health score based on multiple factors
function Calculate-HealthScore {
    param(
        [int]$IssueCount = 0,
        [int]$VulnerabilityCount = 0,
        [int]$DaysSinceLastCommit = -1
    )
    
    $score = 100
    
    # Deduct points for issues (max 30 points)
    $issueDeduction = [Math]::Min($IssueCount * 2, 30)
    $score -= $issueDeduction
    
    # Deduct points for vulnerabilities (max 40 points)
    $vulnDeduction = [Math]::Min($VulnerabilityCount * 5, 40)
    $score -= $vulnDeduction
    
    # Deduct points for stale commits (max 30 points)
    if ($DaysSinceLastCommit -gt 0) {
        if ($DaysSinceLastCommit -gt 365) {
            $score -= 30
        } elseif ($DaysSinceLastCommit -gt 180) {
            $score -= 20
        } elseif ($DaysSinceLastCommit -gt 90) {
            $score -= 10
        } elseif ($DaysSinceLastCommit -gt 30) {
            $score -= 5
        }
    }
    
    return [Math]::Max($score, 0)
}

# Get health category based on score
function Get-HealthCategory {
    param(
        [int]$HealthScore
    )
    
    if ($HealthScore -ge 80) {
        return "Healthy"
    } elseif ($HealthScore -ge 60) {
        return "Caution"
    } elseif ($HealthScore -ge 40) {
        return "Warning"
    } else {
        return "Critical"
    }
}

# Format triage results into a report structure
function Format-TriageReport {
    param(
        [array]$TriageResults
    )
    
    $Timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
    
    # Verify input
    if (-not $TriageResults -or $TriageResults.Count -eq 0) {
        return @{
            timestamp = $Timestamp
            summary = @{
                total_repos = 0
                average_health_score = 0
                health_distribution = @{
                    healthy = 0
                    caution = 0
                    warning = 0
                    critical = 0
                }
            }
            repos = @()
        }
    }
    
    # Convert to array if single object
    if ($TriageResults -isnot [array]) {
        $TriageResults = @($TriageResults)
    }
    
    $healthSummary = @{
        healthy = ($TriageResults | Where-Object { $_.health_category -eq "Healthy" }).Count
        caution = ($TriageResults | Where-Object { $_.health_category -eq "Caution" }).Count
        warning = ($TriageResults | Where-Object { $_.health_category -eq "Warning" }).Count
        critical = ($TriageResults | Where-Object { $_.health_category -eq "Critical" }).Count
    }
    
    $avgHealthScore = if ($TriageResults.Count -gt 0) {
        $scores = @($TriageResults | ForEach-Object { [double]$_.health_score })
        [math]::Round(($scores | Measure-Object -Average).Average, 2)
    } else {
        0
    }
    
    return @{
        timestamp = $Timestamp
        summary = @{
            total_repos = $TriageResults.Count
            average_health_score = $avgHealthScore
            health_distribution = $healthSummary
        }
        repos = $TriageResults
    }
}

# Format triage report as markdown catalog
function Format-CatalogMarkdown {
    param(
        [hashtable]$TriageReport
    )
    
    $markdown = @"
# Repository Catalog

**Generated**: $($TriageReport.timestamp)

## Summary

- **Total Repositories**: $($TriageReport.summary.total_repos)
- **Average Health Score**: $($TriageReport.summary.average_health_score)/100
- **Healthy**: $($TriageReport.summary.health_distribution.healthy)
- **Caution**: $($TriageReport.summary.health_distribution.caution)
- **Warning**: $($TriageReport.summary.health_distribution.warning)
- **Critical**: $($TriageReport.summary.health_distribution.critical)

## Repositories

"@
    
    foreach ($repo in $TriageReport.repos) {
        $markdown += @"

### $($repo.name)

- **Organization**: $($repo.org)
- **URL**: $($repo.url)
- **Health Score**: $($repo.health_score)/100 ($($repo.health_category))
- **Issues**: $($repo.issue_count)
- **Vulnerabilities**: $($repo.total_vulnerabilities)
- **Detected Package Managers**: $(if ($repo.detected_managers) { $repo.detected_managers -join ", " } else { "None" })
- **Days Since Last Commit**: $($repo.days_since_last_commit)

"@
    }
    
    return $markdown
}
Set-StrictMode -Version Latest
