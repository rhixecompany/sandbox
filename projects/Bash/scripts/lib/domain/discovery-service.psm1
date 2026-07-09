#Requires -Version 5.1
<#
.SYNOPSIS
    Discovery service module for repository discovery and metadata collection

.DESCRIPTION
    Provides functions to scan org directories, discover git repositories,
    collect metadata, and generate discovery reports. Uses core modules
    for configuration, path resolution, git operations, and logging.
#>

#region Module Dependencies
Import-Module (Join-Path $PSScriptRoot '../core/path-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/config-loader.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/git-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/logger.psm1') -Force

# Load lib files (dot-sourced as they are scripts, not modules)
$libPath = Join-Path $PSScriptRoot '../'
. (Join-Path $libPath 'repo-analyzer.ps1')
#endregion

#region Public Functions

function Get-LocalRepos {
    <#
    .SYNOPSIS
        Scans org directories from repo inventory and finds .git directories

    .DESCRIPTION
        Reads the repository inventory configuration, iterates through each
        org directory, scans for .git subdirectories, and returns a list of
        discovered repository paths.

    .PARAMETER OrgFilter
        Optional filter to limit scanning to specific org names

    .OUTPUTS
        Array of hashtables with repo information (name, path, org)

    .EXAMPLE
        $repos = Get-LocalRepos
        # Returns all discovered repos from configured orgs
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param(
        [Parameter(Mandatory=$false)]
        [string[]]$OrgFilter
    )

    try {
        $inventory = Get-RepoInventory
        $discoveredRepos = @()

        foreach ($org in $inventory) {
            if ($OrgFilter -and $org.name -notin $OrgFilter) {
                continue
            }

            $orgPath = $org.path
            if (-not (Test-Path $orgPath)) {
                Write-Warn "Org directory not found: $orgPath"
                continue
            }

            # Scan for .git directories
            $gitDirs = Get-ChildItem -Path $orgPath -Directory -Recurse -Filter ".git" -ErrorAction SilentlyContinue |
                       Where-Object { $_.PSIsContainer }

            foreach ($gitDir in $gitDirs) {
                $repoPath = Split-Path $gitDir.FullName -Parent
                $repoName = Split-Path $repoPath -Leaf

                $discoveredRepos += @{
                    name = $repoName
                    path = $repoPath
                    org = $org.name
                }
            }
        }

        return $discoveredRepos
    }
    catch {
        Write-Err "Failed to scan local repos: $($_.Exception.Message)"
        return @()
    }
}

function Get-RepoMetadata {
    <#
    .SYNOPSIS
        Collects comprehensive metadata for a repository

    .DESCRIPTION
        Uses Get-GitInfo from git-utils and Get-RepositoryMetadata from
        repo-analyzer.ps1 to gather git information, size, and language stats.

    .PARAMETER RepoPath
        Path to the repository

    .PARAMETER RepoName
        Name of the repository

    .OUTPUTS
        Hashtable with comprehensive repo metadata

    .EXAMPLE
        $metadata = Get-RepoMetadata -RepoPath "C:\repos\myapp" -RepoName "myapp"
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
        Write-Warn "Repository path does not exist: $RepoPath"
        return $null
    }

    # Get git info from git-utils
    $gitInfo = Get-GitInfo -RepoPath $RepoPath

    # Get repo metadata from repo-analyzer.ps1
    $repoMetadata = Get-RepositoryMetadata -RepoPath $RepoPath -RepoName $RepoName

    # Merge the results
    $metadata = @{
        name = $RepoName
        path = $RepoPath
        remote_url = if ($gitInfo) { $gitInfo.remote_url } else { "" }
        branch = if ($gitInfo) { $gitInfo.branch } else { "unknown" }
        commit_count = if ($gitInfo) { $gitInfo.commit_count } else { 0 }
        last_commit_date = if ($gitInfo) { $gitInfo.last_commit_date } else { "" }
        days_since_last_commit = if ($gitInfo) { $gitInfo.days_since_last_commit } else { -1 }
        size_mb = $repoMetadata.size_mb
        file_count = $repoMetadata.file_count
        languages = $repoMetadata.languages
    }

    return $metadata
}

function Test-RepoValidation {
    <#
    .SYNOPSIS
        Validates a repository object has required properties

    .DESCRIPTION
        Checks that a repo hashtable contains valid name, url, and path.
        Used to ensure repo objects are properly formed before processing.

    .PARAMETER Repo
        Hashtable representing a repository

    .OUTPUTS
        Boolean indicating if repo is valid

    .EXAMPLE
        if (Test-RepoValidation -Repo $repo) { ... }
    #>
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$Repo
    )

    if (-not $Repo) {
        return $false
    }

    # Check required properties
    if (-not $Repo.name -or $Repo.name -eq "") {
        return $false
    }

    if (-not $Repo.path -or $Repo.path -eq "") {
        return $false
    }

    # Validate path exists
    if (-not (Test-Path $Repo.path)) {
        return $false
    }

    return $true
}

function Deduplicate-Repos {
    <#
    .SYNOPSIS
        Removes duplicate repositories based on URL

    .DESCRIPTION
        Takes an array of repo objects and returns only unique repositories
        by comparing their remote URLs. First occurrence is kept.

    .PARAMETER Repos
        Array of repository hashtables

    .OUTPUTS
        Array of unique repository hashtables

    .EXAMPLE
        $unique = Deduplicate-Repos -Repos $allRepos
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Repos
    )

    $seenUrls = @{}
    $uniqueRepos = @()

    foreach ($repo in $Repos) {
        $url = if ($repo.remote_url) { $repo.remote_url } else { "" }

        if ($url -and -not $seenUrls.ContainsKey($url)) {
            $seenUrls[$url] = $true
            $uniqueRepos += $repo
        }
        elseif (-not $url) {
            # Keep repos without URLs (local-only)
            $uniqueRepos += $repo
        }
    }

    return $uniqueRepos
}

function New-DiscoveryReport {
    <#
    .SYNOPSIS
        Builds a discovery report hashtable ready for JSON serialization

    .DESCRIPTION
        Assembles a comprehensive discovery report including discovered
        repositories, metadata, validation results, and summary statistics.

    .PARAMETER Repos
        Array of discovered repository hashtables

    .PARAMETER IncludeMetadata
        If $true, includes full metadata for each repo (default: $true)

    .OUTPUTS
        Hashtable representing the discovery report

    .EXAMPLE
        $report = New-DiscoveryReport -Repos $discoveredRepos
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [array]$Repos,

        [Parameter(Mandatory=$false)]
        [bool]$IncludeMetadata = $true
    )

    $report = @{
        timestamp = (Get-Date -Format "o")
        total_discovered = $Repos.Count
        repositories = @()
    }

    foreach ($repo in $Repos) {
        $repoEntry = @{
            name = $repo.name
            path = $repo.path
            org = if ($repo.org) { $repo.org } else { "" }
        }

        if ($IncludeMetadata -and $repo.path) {
            $metadata = Get-RepoMetadata -RepoPath $repo.path -RepoName $repo.name
            if ($metadata) {
                $repoEntry.metadata = $metadata
            }
        }

        $report.repositories += $repoEntry
    }

    # Add summary
    $report.summary = @{
        total = $Repos.Count
        valid = ($Repos | Where-Object { Test-RepoValidation -Repo $_ }).Count
        invalid = ($Repos | Where-Object { -not (Test-RepoValidation -Repo $_) }).Count
    }

    return $report
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Get-LocalRepos'
    'Get-RepoMetadata'
    'Test-RepoValidation'
    'Deduplicate-Repos'
    'New-DiscoveryReport'
)
#endregion