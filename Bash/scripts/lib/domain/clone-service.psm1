#Requires -Version 5.1
<#
.SYNOPSIS
    Clone service module for repository cloning operations

.DESCRIPTION
    Provides functions to clone repositories in batches, validate
    accessibility, and generate clone reports. Uses git-utils for
    git operations and logging for output.
#>

#region Module Dependencies
Import-Module (Join-Path $PSScriptRoot '../core/path-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/git-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/logger.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/dir-manager.psm1') -Force
#endregion

#region Public Functions

function Invoke-CloneBatch {
    <#
    .SYNOPSIS
        Clones an array of repositories to a target directory

    .DESCRIPTION
        Takes an array of repos with URL and name properties, clones each
        to the specified target directory, and returns an array of results
        with success/failure status.

    .PARAMETER Repos
        Array of hashtables with 'url' and 'name' properties

    .PARAMETER TargetDirectory
        Directory where repositories should be cloned

    .PARAMETER Force
        If $true, removes existing directories before cloning

    .OUTPUTS
        Array of hashtables with clone results

    .EXAMPLE
        $results = Invoke-CloneBatch -Repos $repos -TargetDirectory "C:\clones"
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Repos,

        [Parameter(Mandatory=$true)]
        [string]$TargetDirectory,

        [Parameter(Mandatory=$false)]
        [switch]$Force
    )

    # Ensure target directory exists
    Ensure-Directory -Path $TargetDirectory | Out-Null

    $results = @()
    $total = $Repos.Count
    $current = 0

    foreach ($repo in $Repos) {
        $current++
        $repoName = if ($repo.name) { $repo.name } else { "unknown" }
        $repoUrl = if ($repo.url) { $repo.url } else { $repo.remote_url }

        Write-Progress-Custom -Current $current -Total $total -Message "Cloning $repoName"

        $result = @{
            name = $repoName
            url = $repoUrl
            success = $false
            path = ""
            error = ""
        }

        if (-not $repoUrl) {
            $result.error = "No URL provided"
            $results += $result
            Write-Warn "Skipping $repoName - no URL"
            continue
        }

        $clonePath = Join-Path $TargetDirectory $repoName

        # Check if already exists
        if (Test-Path $clonePath) {
            if ($Force) {
                Remove-Item -Path $clonePath -Recurse -Force -ErrorAction SilentlyContinue
            }
            else {
                $result.path = $clonePath
                $result.success = $true
                $result.note = "Already exists"
                $results += $result
                Write-Info "Skipping $repoName - already exists"
                continue
            }
        }

        # Clone the repository
        try {
            $gitResult = Invoke-Git -RepoPath $TargetDirectory -Args @('clone', $repoUrl, $repoName)

            if ($gitResult.success) {
                $result.success = $true
                $result.path = $clonePath
                Write-Success "Cloned $repoName"
            }
            else {
                $result.error = $gitResult.output
                Write-Err "Failed to clone $repoName`: $($gitResult.output)"
            }
        }
        catch {
            $result.error = $_.Exception.Message
            Write-Err "Exception cloning $repoName`: $($_.Exception.Message)"
        }

        $results += $result
    }

    return $results
}

function Test-RepoAccessible {
    <#
    .SYNOPSIS
        Tests if a repository is accessible and valid

    .DESCRIPTION
        Uses Test-GitAccessible from git-utils to verify a cloned
        repository is valid and accessible.

    .PARAMETER RepoPath
        Path to the repository to test

    .OUTPUTS
        Hashtable with 'valid' and 'reason' properties

    .EXAMPLE
        $check = Test-RepoAccessible -RepoPath "C:\clones\myapp"
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )

    return Test-GitAccessible -RepoPath $RepoPath
}

function New-CloneReport {
    <#
    .SYNOPSIS
        Builds a clone report hashtable with summary statistics

    .DESCRIPTION
        Takes clone results and assembles a report with summary
        statistics including total, success, failed counts and rates.

    .PARAMETER Results
        Array of clone result hashtables from Invoke-CloneBatch

    .OUTPUTS
        Hashtable representing the clone report

    .EXAMPLE
        $report = New-CloneReport -Results $cloneResults
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Results
    )

    $total = $Results.Count
    $successful = ($Results | Where-Object { $_.success }).Count
    $failed = $total - $successful
    $successRate = if ($total -gt 0) { [math]::Round(($successful / $total) * 100, 2) } else { 0 }

    $report = @{
        timestamp = (Get-Date -Format "o")
        total = $total
        successful = $successful
        failed = $failed
        success_rate = $successRate
        results = $Results
    }

    return $report
}

function Get-CloneStatistics {
    <#
    .SYNOPSIS
        Computes statistics from clone results

    .DESCRIPTION
        Analyzes clone results and returns detailed statistics including
        success rate, failure reasons, and timing information.

    .PARAMETER Results
        Array of clone result hashtables

    .OUTPUTS
        Hashtable with computed statistics

    .EXAMPLE
        $stats = Get-CloneStatistics -Results $cloneResults
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Results
    )

    $stats = @{
        total = $Results.Count
        successful = 0
        failed = 0
        already_existed = 0
        failure_reasons = @{}
    }

    foreach ($result in $Results) {
        if ($result.success) {
            if ($result.note -eq "Already exists") {
                $stats.already_existed++
            }
            else {
                $stats.successful++
            }
        }
        else {
            $stats.failed++
            $reason = if ($result.error) { $result.error } else { "Unknown" }
            if (-not $stats.failure_reasons.ContainsKey($reason)) {
                $stats.failure_reasons[$reason] = 0
            }
            $stats.failure_reasons[$reason]++
        }
    }

    $stats.success_rate = if ($stats.total -gt 0) {
        [math]::Round(($stats.successful / $stats.total) * 100, 2)
    } else { 0 }

    return $stats
}

function Invoke-CloneValidation {
    <#
    .SYNOPSIS
        Validates a cloned repository path

    .DESCRIPTION
        Performs comprehensive validation of a cloned repository including
        path existence, git validity, and accessibility checks.

    .PARAMETER RepoPath
        Path to the cloned repository

    .PARAMETER RepoName
        Name of the repository (optional, for logging)

    .OUTPUTS
        Hashtable with validation results

    .EXAMPLE
        $validation = Invoke-CloneValidation -RepoPath "C:\clones\myapp"
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath,

        [Parameter(Mandatory=$false)]
        [string]$RepoName = ""
    )

    $validation = @{
        path_exists = $false
        is_git_repo = $false
        is_accessible = $false
        valid = $false
        errors = @()
    }

    # Check path exists
    if (-not (Test-Path $RepoPath)) {
        $validation.errors += "Path does not exist: $RepoPath"
        return $validation
    }
    $validation.path_exists = $true

    # Check is git repo
    $isGit = Test-IsGitRepo -Path $RepoPath
    if (-not $isGit) {
        $validation.errors += "Not a git repository"
        return $validation
    }
    $validation.is_git_repo = $true

    # Check accessibility
    $accessible = Test-RepoAccessible -RepoPath $RepoPath
    if (-not $accessible.valid) {
        $validation.errors += $accessible.reason
        return $validation
    }
    $validation.is_accessible = $true
    $validation.valid = $true

    return $validation
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Invoke-CloneBatch'
    'Test-RepoAccessible'
    'New-CloneReport'
    'Get-CloneStatistics'
    'Invoke-CloneValidation'
)
#endregion