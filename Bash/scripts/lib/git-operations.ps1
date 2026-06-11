<#
.SYNOPSIS
    Git operations for cloning repositories
#>


Set-StrictMode -Version Latest
# Import logger if available (may already be loaded by caller)
$LOGGER_PATH = Join-Path -Path $PSScriptRoot -ChildPath "logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force -ErrorAction SilentlyContinue
}

function Invoke-GitClone {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoUrl,
        
        [Parameter(Mandatory=$true)]
        [string]$TargetPath,
        
        [Parameter(Mandatory=$false)]
        [int]$TimeoutSeconds = 300,
        
        [Parameter(Mandatory=$false)]
        [int]$MaxRetries = 3
    )
    
    $attempt = 0
    $lastError = $null
    
    while ($attempt -lt $MaxRetries) {
        $attempt++
        if (Get-Command Write-Info -ErrorAction SilentlyContinue) {
            Write-Info "  Clone attempt $attempt/$MaxRetries for $RepoUrl"
        } else {
            Write-Host "  Clone attempt $attempt/$MaxRetries for $RepoUrl" -ForegroundColor Gray
        }
        
        try {
            # Create parent directory if needed
            $parentDir = Split-Path -Parent $TargetPath
            if (-not (Test-Path $parentDir)) {
                New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
            }
            
            # Attempt clone with timeout
            $job = Start-Job -ScriptBlock {
                param($url, $path)
                git clone $url $path 2>&1
            } -ArgumentList $RepoUrl, $TargetPath
            
            $completed = Wait-Job -Job $job -Timeout $TimeoutSeconds
            
            if ($completed) {
                $output = Receive-Job -Job $job
                Remove-Job -Job $job
                
                if (Test-Path $TargetPath) {
                    return @{
                        success = $true
                        error = $null
                        attempt = $attempt
                        duration_seconds = $TimeoutSeconds
                    }
                } else {
                    $lastError = "Clone directory not created"
                }
            } else {
                Remove-Job -Job $job -Force
                $lastError = "Clone timeout after $TimeoutSeconds seconds"
            }
        } catch {
            $lastError = $_.Exception.Message
        }
        
        if ($attempt -lt $MaxRetries) {
            if (Get-Command Write-Warn -ErrorAction SilentlyContinue) {
                Write-Warn "    Retrying in 5 seconds..."
            } else {
                Write-Host "    Retrying in 5 seconds..." -ForegroundColor Yellow
            }
            Start-Sleep -Seconds 5
        }
    }
    
    return @{
        success = $false
        error = $lastError
        attempt = $attempt
        duration_seconds = $null
    }
}

function Test-GitRepository {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return $false
    }
    
    $gitDir = Join-Path $RepoPath ".git"
    return (Test-Path $gitDir)
}

function Get-GitRepositoryInfo {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path $RepoPath)) {
        return $null
    }
    
    $gitDir = Join-Path $RepoPath ".git"
    if (-not (Test-Path $gitDir)) {
        return $null
    }
    
    try {
        Push-Location $RepoPath
        
        $remoteUrl = & git config --get remote.origin.url 2>$null
        $branch = & git rev-parse --abbrev-ref HEAD 2>$null
        $commitCount = & git rev-list --count HEAD 2>$null
        $lastCommit = & git log -1 --format="%ai" 2>$null
        
        Pop-Location
        
        return @{
            remote_url = $remoteUrl
            current_branch = $branch
            commit_count = [int]$commitCount
            last_commit = $lastCommit
        }
    } catch {
        Pop-Location
        return $null
    }
}

function Invoke-GitCloneBatch {
    param(
        [Parameter(Mandatory=$true)]
        [array]$Repositories,
        
        [Parameter(Mandatory=$true)]
        [string]$BaseDirectory,
        
        [Parameter(Mandatory=$false)]
        [int]$TimeoutSeconds = 300,
        
        [Parameter(Mandatory=$false)]
        [int]$MaxRetries = 3,
        
        [Parameter(Mandatory=$false)]
        [scriptblock]$ProgressCallback
    )
    
    $results = @()
    $deduped = @{}
    
    foreach ($repo in $Repositories) {
        # Deduplicate by URL
        if ($deduped.ContainsKey($repo.clone_url)) {
            Write-Host "Skipping duplicate: $($repo.clone_url)" -ForegroundColor Yellow
            continue
        }
        $deduped[$repo.clone_url] = $true
        
        if ($ProgressCallback) {
            & $ProgressCallback -Repository $repo -Index ($results.Count + 1) -Total $Repositories.Count
        }
        
        $targetPath = Join-Path $BaseDirectory $repo.name
        $cloneResult = Invoke-GitClone -RepoUrl $repo.clone_url -TargetPath $targetPath -TimeoutSeconds $TimeoutSeconds -MaxRetries $MaxRetries
        
        $results += @{
            name = $repo.name
            clone_url = $repo.clone_url
            target_path = $targetPath
            success = $cloneResult.success
            error = $cloneResult.error
            attempt = $cloneResult.attempt
            duration_seconds = $cloneResult.duration_seconds
        }
    }
    
    return $results
}
