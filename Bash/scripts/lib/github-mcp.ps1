<#
.SYNOPSIS
    GitHub MCP API wrapper functions
#>


Set-StrictMode -Version Latest
# Import logger if available (may already be loaded by caller)
$LOGGER_PATH = Join-Path -Path $PSScriptRoot -ChildPath "logger.psm1"
if (Test-Path $LOGGER_PATH) {
    Import-Module $LOGGER_PATH -Force -ErrorAction SilentlyContinue
}

function Connect-GitHubMCP {
    param(
        [Parameter(Mandatory=$true)]
        [string]$MCPServerUrl = "http://localhost:3000"
    )
    
    $script:MCPServerUrl = $MCPServerUrl
    if (Get-Command Write-Success -ErrorAction SilentlyContinue) {
        Write-Success "Connected to GitHub MCP server at $MCPServerUrl"
    } else {
        Write-Host "Connected to GitHub MCP server at $MCPServerUrl" -ForegroundColor Green
    }
}

function Get-GitHubOrganizationRepos {
    param(
        [Parameter(Mandatory=$true)]
        [string]$OrgName,
        
        [Parameter(Mandatory=$false)]
        [int]$PerPage = 100
    )
    
    $repos = @()
    $page = 1
    
    do {
        try {
            $response = Invoke-RestMethod `
                -Uri "$script:MCPServerUrl/repos?org=$OrgName&page=$page&per_page=$PerPage" `
                -Method Get `
                -TimeoutSec 30
            
            if ($response -is [array]) {
                $repos += $response
                $page++
            } else {
                break
            }
        } catch {
            Write-Error "Failed to fetch repos for org $OrgName page ${page}: $_"
            break
        }
    } while ($response.Count -eq $PerPage)
    
    return $repos
}

function Test-GitHubRepoAccessibility {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoUrl,
        
        [Parameter(Mandatory=$false)]
        [int]$TimeoutSec = 10
    )
    
    try {
        $response = Invoke-WebRequest `
            -Uri $RepoUrl `
            -Method Head `
            -TimeoutSec $TimeoutSec `
            -ErrorAction Stop
        
        return @{
            accessible = $true
            status_code = $response.StatusCode
            error = $null
        }
    } catch {
        return @{
            accessible = $false
            status_code = $null
            error = $_.Exception.Message
        }
    }
}

function Get-GitHubRepoIssueCount {
    param(
        [Parameter(Mandatory=$true)]
        [string]$OrgName,
        
        [Parameter(Mandatory=$true)]
        [string]$RepoName
    )
    
    try {
        $response = Invoke-RestMethod `
            -Uri "$script:MCPServerUrl/repos/$OrgName/$RepoName/issues?state=all" `
            -Method Get `
            -TimeoutSec 30
        
        return $response.Count
     } catch {
         Write-Warning "Failed to fetch issue count for $OrgName/${RepoName}: $_"
         return -1
     }
}

# Export functions for use when dot-sourced
# Note: Not using Export-ModuleMember as this script is dot-sourced, not imported as a module
