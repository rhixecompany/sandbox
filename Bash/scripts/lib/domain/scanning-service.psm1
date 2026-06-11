#Requires -Version 5.1
<#
.SYNOPSIS
    Scanning service module for package manager and vulnerability scanning

.DESCRIPTION
    Provides functions to detect package managers, run vulnerability
    scanners, and aggregate scan results. Uses package-managers.ps1
    for detection and dependency-scanner.ps1 for scanning.
#>

#region Module Dependencies
Import-Module (Join-Path $PSScriptRoot '../core/path-utils.psm1') -Force
Import-Module (Join-Path $PSScriptRoot '../core/logger.psm1') -Force

# Load lib files (dot-sourced as they are scripts, not modules)
$libPath = Join-Path $PSScriptRoot '../'
. (Join-Path $libPath 'package-managers.ps1')
. (Join-Path $libPath 'dependency-scanner.ps1')
#endregion

#region Public Functions

function Get-DetectedManagers {
    <#
    .SYNOPSIS
        Detects which package managers are present in a repository

    .DESCRIPTION
        Uses Detect-PackageManagers from package-managers.ps1 to identify
        all package managers used in a repository.

    .PARAMETER RepoPath
        Path to the repository to scan

    .OUTPUTS
        Array of detected manager names

    .EXAMPLE
        $managers = Get-DetectedManagers -RepoPath "C:\repos\myapp"
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param(
        [Parameter(Mandatory=$true)]
        [string]$RepoPath
    )

    if (-not (Test-Path $RepoPath)) {
        Write-Warn "Repository path does not exist: $RepoPath"
        return @()
    }

    return Detect-PackageManagers -RepoPath $RepoPath
}

function Invoke-StackScan {
    <#
    .SYNOPSIS
        Runs all scanners for detected package managers

    .DESCRIPTION
        Detects package managers in a repository and runs the appropriate
        vulnerability scanners for each. Uses Invoke-AllScanners internally.

    .PARAMETER RepoPath
        Path to the repository to scan

    .PARAMETER IncludeStdout
        If $true, includes full scanner output in results

    .OUTPUTS
        Hashtable with scan results for all detected managers

    .EXAMPLE
        $scan = Invoke-StackScan -RepoPath "C:\repos\myapp"
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
        Write-Info "Detecting package managers in: $RepoPath"
        $managers = Get-DetectedManagers -RepoPath $RepoPath

        if ($managers.Count -eq 0) {
            Write-Info "No package managers detected"
            return @{
                repo_path = $RepoPath
                detected_managers = @()
                total_vulnerabilities = 0
                status = "no_managers"
            }
        }

        Write-Info "Detected managers: $($managers -join ', ')"

        # Run all scanners
        $scanResult = Invoke-AllScanners -RepoPath $RepoPath -IncludeStdout $IncludeStdout

        return $scanResult
    }
    catch {
        Write-Err "Stack scan failed: $($_.Exception.Message)"
        return @{
            repo_path = $RepoPath
            status = "error"
            error = $_.Exception.Message
        }
    }
}

function Get-VulnerabilityReport {
    <#
    .SYNOPSIS
        Aggregates vulnerabilities from scan results

    .DESCRIPTION
        Takes scan results from Invoke-StackScan or Invoke-AllScanners
        and aggregates vulnerability information into a structured report.

    .PARAMETER ScanResults
        Hashtable with scan results from Invoke-StackScan

    .OUTPUTS
        Hashtable with aggregated vulnerability information

    .EXAMPLE
        $vulnReport = Get-VulnerabilityReport -ScanResults $scanResult
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$ScanResults
    )

    $report = @{
        repo_path = $ScanResults.repo_path
        total_vulnerabilities = 0
        managers = @{}
        by_severity = @{
            critical = 0
            high = 0
            medium = 0
            low = 0
            unknown = 0
        }
    }

    if ($ScanResults.total_vulnerabilities) {
        $report.total_vulnerabilities = $ScanResults.total_vulnerabilities
    }

    # Aggregate per-manager results
    if ($ScanResults.managers -and $ScanResults.managers.Count -gt 0) {
        foreach ($manager in $ScanResults.managers.Keys) {
            $managerResult = $ScanResults.managers[$manager]

            $report.managers[$manager] = @{
                status = $managerResult.status
                vulnerabilities = if ($managerResult.vulnerabilities) { $managerResult.vulnerabilities } else { 0 }
            }

            if ($managerResult.error) {
                $report.managers[$manager].error = $managerResult.error
            }
        }
    }

    return $report
}

function Get-ScanSummary {
    <#
    .SYNOPSIS
        Returns summary of detected managers and total vulnerabilities

    .DESCRIPTION
        Provides a quick summary of scan results including detected
        package managers and total vulnerability count.

    .PARAMETER ScanResults
        Hashtable with scan results from Invoke-StackScan

    .OUTPUTS
        Hashtable with summary information

    .EXAMPLE
        $summary = Get-ScanSummary -ScanResults $scanResult
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param(
        [Parameter(Mandatory=$true)]
        [hashtable]$ScanResults
    )

    $summary = @{
        repo_path = $ScanResults.repo_path
        detected_managers = @()
        total_vulnerabilities = 0
        scan_status = "unknown"
    }

    if ($ScanResults.detected_managers) {
        $summary.detected_managers = $ScanResults.detected_managers
    }

    if ($ScanResults.total_vulnerabilities) {
        $summary.total_vulnerabilities = $ScanResults.total_vulnerabilities
    }

    if ($ScanResults.status) {
        $summary.scan_status = $ScanResults.status
    }
    elseif ($ScanResults.total_vulnerabilities -gt 0) {
        $summary.scan_status = "vulnerabilities_found"
    }
    elseif ($ScanResults.detected_managers.Count -gt 0) {
        $summary.scan_status = "clean"
    }
    else {
        $summary.scan_status = "no_managers"
    }

    return $summary
}

#endregion

#region Module Export
Export-ModuleMember -Function @(
    'Get-DetectedManagers'
    'Invoke-StackScan'
    'Get-VulnerabilityReport'
    'Get-ScanSummary'
)
#endregion