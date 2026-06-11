<#
.SYNOPSIS
    Validation utilities for discovery phase
#>


Set-StrictMode -Version Latest
function Test-RepoMetadata {
    param(
        [Parameter(Mandatory=$true)]
        [object]$Repo
    )
    
    $errors = @()
    
    if (-not $Repo.name) { $errors += "Missing repo name" }
    if (-not $Repo.url) { $errors += "Missing repo URL" }
    if (-not $Repo.owner) { $errors += "Missing repo owner" }
    
    return @{
        valid = $errors.Count -eq 0
        errors = $errors
    }
}

function Deduplicate-Repos {
    param(
        [Parameter(Mandatory=$true)]
        [object[]]$Repos
    )
    
    $seen = @{}
    $deduplicated = @()
    
    foreach ($repo in $Repos) {
        $key = "$($repo.owner)/$($repo.name)"
        
        if (-not $seen.ContainsKey($key)) {
            $seen[$key] = $true
            $deduplicated += $repo
        } else {
            Write-Warning "Duplicate repo found: $key, skipping"
        }
    }
    
    return $deduplicated
}

function Format-DiscoveryReport {
    param(
        [Parameter(Mandatory=$true)]
        [object[]]$Repos,
        
        [Parameter(Mandatory=$false)]
        [string]$Timestamp = (Get-Date -Format "o")
    )
    
    return @{
        timestamp = $Timestamp
        total_repos = $Repos.Count
        repos = $Repos
        validation_status = @{
            all_valid = ($Repos | Where-Object { -not $_.validation.valid }).Count -eq 0
            invalid_count = ($Repos | Where-Object { -not $_.validation.valid }).Count
        }
    }
}

# Export functions for use when dot-sourced
# Note: Not using Export-ModuleMember as this script is dot-sourced, not imported as a module
