# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Dependency vulnerability scanning functions
#>


Set-StrictMode -Version Latest
function Invoke-NpmAudit {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path (Join-Path $RepoPath "package.json"))) {
        return $null
    }
    
    try {
        Push-Location $RepoPath
        
        $auditOutput = npm audit --json 2>$null | ConvertFrom-Json
        
        Pop-Location
        
        return @{
            vulnerabilities = $auditOutput.metadata.vulnerabilities
            audited = $auditOutput.metadata.audited
            packages = $auditOutput.metadata.packages
        }
    } catch {
        Pop-Location
        return @{
            error = $_.Exception.Message
        }
    }
}

function Invoke-PipCheck {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path (Join-Path $RepoPath "requirements.txt")) -and 
        -not (Test-Path (Join-Path $RepoPath "setup.py")) -and
        -not (Test-Path (Join-Path $RepoPath "pyproject.toml"))) {
        return $null
    }
    
    try {
        Push-Location $RepoPath
        
        $pipOutput = pip check 2>$null
        
        Pop-Location
        
        $vulnCount = if ($pipOutput) { ($pipOutput | Measure-Object -Line).Lines } else { 0 }
        
        return @{
            vulnerabilities = $vulnCount
            output = $pipOutput
        }
    } catch {
        Pop-Location
        return @{
            error = $_.Exception.Message
        }
    }
}

function Invoke-CargoAudit {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    if (-not (Test-Path (Join-Path $RepoPath "Cargo.toml"))) {
        return $null
    }
    
    try {
        Push-Location $RepoPath
        
        $auditOutput = cargo audit --json 2>$null | ConvertFrom-Json
        
        Pop-Location
        
        return @{
            vulnerabilities = $auditOutput.vulnerabilities.Count
            advisories = $auditOutput.advisories
        }
    } catch {
        Pop-Location
        return @{
            error = $_.Exception.Message
        }
    }
}

function Get-DependencyVulnerabilities {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )
    
    $vulnerabilities = @{
        npm = Invoke-NpmAudit -RepoPath $RepoPath
        pip = Invoke-PipCheck -RepoPath $RepoPath
        cargo = Invoke-CargoAudit -RepoPath $RepoPath
    }
    
    return $vulnerabilities
}

<#
.SYNOPSIS
    Orchestrates vulnerability scanning across all detected package managers
.DESCRIPTION
    Automatically detects available package managers in a repository and runs
    appropriate vulnerability scanners for each. Aggregates results into a
    comprehensive report showing vulnerabilities across all package management systems.
.PARAMETER RepoPath
    The path to the repository to scan
.PARAMETER IncludeStdout
    If $true, includes scanner output in results. Default is $false.
.EXAMPLE
    $results = Invoke-AllScanners -RepoPath "C:\projects\myapp"
.OUTPUTS
    [hashtable] Scan results with detected managers and vulnerability counts
#>

Set-StrictMode -Version Latest
function Invoke-AllScanners {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath,
        
        [Parameter(Mandatory=$false)]
        [bool]$IncludeStdout = $false
    )
    
    # Validate repository path
    if (-not (Test-Path $RepoPath)) {
        throw "Repository path does not exist: $RepoPath"
    }
    
    try {
         # Load helper libraries
         $libPath = $PSScriptRoot
         $packageManagersPath = Join-Path $libPath "package-managers.ps1"
         $scannerPath = Join-Path $libPath "package-manager-scanners.ps1"
        
        if (-not (Test-Path $packageManagersPath)) {
            throw "Required library not found: $packageManagersPath"
        }
        
        if (-not (Test-Path $scannerPath)) {
            throw "Required library not found: $scannerPath"
        }
        
        . $packageManagersPath
        . $scannerPath
        
        # Detect available package managers
        $detectedManagers = Detect-PackageManagers -RepoPath $RepoPath
        
        if ($detectedManagers.Count -eq 0) {
            return @{
                repo_path = $RepoPath
                detected_managers = @()
                total_vulnerabilities = 0
                managers = @{}
                scan_timestamp = (Get-Date -Format "o")
                note = "No package managers detected"
            }
        }
        
        # Initialize results structure
        $results = @{
            repo_path = $RepoPath
            detected_managers = $detectedManagers
            total_vulnerabilities = 0
            managers = @{}
            scan_timestamp = (Get-Date -Format "o")
        }
        
        # Run scanner for each detected manager
        foreach ($manager in $detectedManagers) {
            try {
                $managerObj = Get-ManagerByName -ManagerName $manager
                
                if ($null -eq $managerObj) {
                    $results.managers[$manager] = @{
                        status = "unknown"
                        error = "Manager configuration not found"
                    }
                    continue
                }
                
                # Get scanner function name (e.g., "Invoke-NpmAudit")
                $functionName = $managerObj.scanner
                
                if (-not (Get-Command $functionName -ErrorAction SilentlyContinue)) {
                    $results.managers[$manager] = @{
                        status = "error"
                        error = "Scanner function not found: $functionName"
                    }
                    continue
                }
                
                # Execute scanner
                $scanResult = & $functionName -RepoPath $RepoPath
                
                if ($null -eq $scanResult) {
                    $results.managers[$manager] = @{
                        status = "skipped"
                        vulnerabilities = 0
                        note = "No manifest files detected"
                    }
                    continue
                }
                
                if ($scanResult.ContainsKey("error")) {
                    $results.managers[$manager] = @{
                        status = "error"
                        error = $scanResult.error
                        timestamp = (Get-Date -Format "o")
                    }
                    continue
                }
                
                # Add scanner result
                $vulnCount = $scanResult.vulnerabilities
                if ($null -eq $vulnCount) { $vulnCount = 0 }
                
                $results.managers[$manager] = @{
                    status = "success"
                    vulnerabilities = $vulnCount
                    timestamp = (Get-Date -Format "o")
                }
                
                # Include full output if requested
                if ($IncludeStdout) {
                    $results.managers[$manager].output = $scanResult
                }
                
                # Aggregate vulnerability count
                $results.total_vulnerabilities += $vulnCount
                
            } catch {
                $results.managers[$manager] = @{
                    status = "error"
                    error = $_.Exception.Message
                    timestamp = (Get-Date -Format "o")
                }
            }
        }
        
        return $results
        
    } catch {
        return @{
            repo_path = $RepoPath
            status = "error"
            error = $_.Exception.Message
            scan_timestamp = (Get-Date -Format "o")
        }
    }
}
