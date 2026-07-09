# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Repository metadata analysis functions
#>


Set-StrictMode -Version Latest
function Get-RepositoryLanguages {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return @{}
    }
    
    $languages = @{}
    
    # Detect by file extensions
    $fileExtensions = @{
        '.js' = 'JavaScript'
        '.ts' = 'TypeScript'
        '.tsx' = 'TypeScript'
        '.jsx' = 'JavaScript'
        '.py' = 'Python'
        '.cs' = 'C#'
        '.csproj' = 'C#'
        '.go' = 'Go'
        '.rs' = 'Rust'
        '.java' = 'Java'
        '.rb' = 'Ruby'
        '.php' = 'PHP'
        '.cpp' = 'C++'
        '.c' = 'C'
        '.h' = 'C'
    }
    
    try {
        $files = Get-ChildItem -Path $RepoPath -File -Recurse -ErrorAction SilentlyContinue | 
            Where-Object { $_.Extension -in $fileExtensions.Keys }
        
        foreach ($file in $files) {
            $lang = $fileExtensions[$file.Extension]
            if ($lang) {
                $languages[$lang] = ($languages[$lang] -as [int]) + 1
            }
        }
    } catch {
        # Silently continue if directory traversal fails
    }
    
    return $languages
}

function Get-RepositorySize {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return 0
    }
    
    try {
        $size = (Get-ChildItem -Path $RepoPath -Recurse -ErrorAction SilentlyContinue | 
            Measure-Object -Property Length -Sum).Sum
        return [math]::Round($size / 1MB, 2)
    } catch {
        return 0
    }
}

function Get-RepositoryCommitHistory {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return $null
    }
    
    try {
        Push-Location $RepoPath
        
        $totalCommits = (git rev-list --count HEAD 2>$null)
        $lastCommitDate = (git log -1 --format=%ai 2>$null)
        $lastCommitAuthor = (git log -1 --format=%an 2>$null)
        
        Pop-Location
        
        if ($lastCommitDate) {
            $lastCommitDateTime = [DateTime]::Parse($lastCommitDate)
            $daysSinceLastCommit = ([DateTime]::UtcNow - $lastCommitDateTime).Days
        } else {
            $daysSinceLastCommit = -1
        }
        
        return @{
            total_commits = $totalCommits
            last_commit_date = $lastCommitDate
            last_commit_author = $lastCommitAuthor
            days_since_last_commit = $daysSinceLastCommit
        }
    } catch {
        Pop-Location
        return $null
    }
}

function Get-RepositoryFileCount {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return 0
    }
    
    try {
        $count = (Get-ChildItem -Path $RepoPath -File -Recurse -ErrorAction SilentlyContinue | 
            Measure-Object).Count
        return $count
    } catch {
        return 0
    }
}

function Get-RepositoryMetadata {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath,
        
        [Parameter(Mandatory=$true)]
        [string]$RepoName
    )
    
    return @{
        name = $RepoName
        path = $RepoPath
        languages = Get-RepositoryLanguages -RepoPath $RepoPath
        size_mb = Get-RepositorySize -RepoPath $RepoPath
        file_count = Get-RepositoryFileCount -RepoPath $RepoPath
        commit_history = Get-RepositoryCommitHistory -RepoPath $RepoPath
    }
}
