# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Clone-specific utilities for Phase 2
#>


Set-StrictMode -Version Latest
# Import logger if available (may already be loaded by caller)
$LOGGER_PATH = Join-Path -Path $PSScriptRoot -ChildPath "logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force -ErrorAction SilentlyContinue
}

function ConvertTo-CloneReport {
    param(
        [Parameter(Mandatory=$true)]
        [array]$CloneResults,
        
        [Parameter(Mandatory=$false)]
        [string]$ReportPath
    )
    
    $totalRepos = $CloneResults.Count
    $successCount = ($CloneResults | Where-Object { $_.success } | Measure-Object).Count
    $failureCount = $totalRepos - $successCount
    $successRate = if ($totalRepos -gt 0) { [math]::Round(($successCount / $totalRepos) * 100, 2) } else { 0 }
    
    $report = @{
        timestamp = Get-Date -Format "O"
        summary = @{
            total_repos = $totalRepos
            successful_clones = $successCount
            failed_clones = $failureCount
            success_rate_percent = $successRate
        }
        details = @()
    }
    
    foreach ($result in $CloneResults) {
        $report.details += @{
            name = $result.name
            clone_url = $result.clone_url
            target_path = $result.target_path
            success = $result.success
            error = $result.error
            attempt = $result.attempt
            duration_seconds = $result.duration_seconds
        }
    }
    
    if ($ReportPath) {
        $json = $report | ConvertTo-Json -Depth 10
        Set-Content -Path $ReportPath -Value $json -Encoding UTF8
        if (Get-Command Write-Success -ErrorAction SilentlyContinue) {
            Write-Success "Clone report saved to: $ReportPath"
        } else {
            Write-Host "Clone report saved to: $ReportPath" -ForegroundColor Green
        }
    }
    
    return $report
}

function Get-DuplicateRepositories {
    param(
        [Parameter(Mandatory=$true)]
        [array]$Repositories
    )
    
    $urlMap = @{}
    $duplicates = @()
    
    foreach ($repo in $Repositories) {
        if ($urlMap.ContainsKey($repo.clone_url)) {
            $duplicates += @{
                url = $repo.clone_url
                repos = @($urlMap[$repo.clone_url], $repo.name)
            }
        } else {
            $urlMap[$repo.clone_url] = $repo.name
        }
    }
    
    return $duplicates
}

function Invoke-CloneValidation {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return @{ valid = $false; reason = "Repository path does not exist" }
    }
    
    $gitDir = Join-Path $RepoPath ".git"
    if (-not (Test-Path $gitDir)) {
        return @{ valid = $false; reason = "Not a valid git repository (.git directory missing)" }
    }
    
    $hasObjects = Test-Path (Join-Path $gitDir "objects")
    $hasRefs = Test-Path (Join-Path $gitDir "refs")
    $hasConfig = Test-Path (Join-Path $gitDir "config")
    
    if (-not ($hasObjects -and $hasRefs -and $hasConfig)) {
        return @{ valid = $false; reason = "Corrupted git repository (missing essential directories)" }
    }
    
    return @{ valid = $true; reason = "Repository is valid" }
}

function Get-CloneStatistics {
    param(
        [Parameter(Mandatory=$true)]
        [array]$CloneResults
    )
    
    $stats = @{
        total = $CloneResults.Count
        successful = ($CloneResults | Where-Object { $_.success } | Measure-Object).Count
        failed = ($CloneResults | Where-Object { -not $_.success } | Measure-Object).Count
        average_attempts = [math]::Round(($CloneResults.attempt | Measure-Object -Average).Average, 2)
        by_attempt = @{}
    }
    
    foreach ($result in $CloneResults) {
        $attemptKey = "attempt_$($result.attempt)"
        if (-not $stats.by_attempt.ContainsKey($attemptKey)) {
            $stats.by_attempt[$attemptKey] = 0
        }
        $stats.by_attempt[$attemptKey]++
    }
    
    return $stats
}
