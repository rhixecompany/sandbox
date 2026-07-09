# DRY_RUN_SUPPORT=true
﻿<#
.SYNOPSIS
    Package Manager Scanner Implementations
    
.DESCRIPTION
    Implements scanner functions for each package manager. Scanners run audit tools
    and return vulnerability data as hashtables.
    
.NOTES
    npm audit is handled in dependency-scanner.ps1
    This file focuses on pnpm, yarn, poetry, maven, gradle, nuget, go, bundler, composer, bun
#>


Set-StrictMode -Version Latest
function Invoke-PnpmAudit {
    <#
    .SYNOPSIS
    Run pnpm audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .EXAMPLE
    $result = Invoke-PnpmAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & pnpm audit --json 2>$null | ConvertFrom-Json
        Pop-Location
        
        if ($output -and $output.metadata) {
            return @{
                vulnerabilities = $output.metadata.vulnerabilities
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_output" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-YarnAudit {
    <#
    .SYNOPSIS
    Run yarn audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .EXAMPLE
    $result = Invoke-YarnAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & yarn audit --json 2>$null | ConvertFrom-Json
        Pop-Location
        
        if ($output.data -and $output.data.vulnerabilities) {
            $vulnCount = 0
            $output.data.vulnerabilities | ForEach-Object {
                $vulnCount += $_.cves.Length
            }
            return @{
                vulnerabilities = $vulnCount
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-PoetryCheck {
    <#
    .SYNOPSIS
    Run poetry check on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Poetry check validates pyproject.toml, not vulnerabilities.
    For security scanning, use poetry show or safety check.
    
    .EXAMPLE
    $result = Invoke-PoetryCheck "C:\repos\my-project"
    Write-Host "Status: $($result.status)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & poetry check 2>&1
        Pop-Location
        
        if ($LASTEXITCODE -eq 0) {
            return @{
                vulnerabilities = 0
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
                note = "poetry check validates pyproject.toml, not vulnerabilities"
            }
        }
        return @{ vulnerabilities = 0; status = "check_failed" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-MavenAudit {
    <#
    .SYNOPSIS
    Run Maven dependency check (requires Maven installed).
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Requires maven-dependency-check-plugin configured in pom.xml
    
    .EXAMPLE
    $result = Invoke-MavenAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & mvn dependency-check:check 2>&1
        Pop-Location
        
        # Parse output for vulnerability counts
        if ($output -match "(?<vuln>\d+)\s+vulnerabilities? found") {
            return @{
                vulnerabilities = [int]$matches['vuln']
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-GradleAudit {
    <#
    .SYNOPSIS
    Run Gradle dependency check (requires Gradle and plugin configured).
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Requires org.owasp.dependencycheck plugin in build.gradle
    
    .EXAMPLE
    $result = Invoke-GradleAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        # Gradle requires plugin in build.gradle for dependency-check
        $output = & gradle dependencyCheckAnalyze 2>&1
        Pop-Location
        
        # Parse output for vulnerability counts
        if ($output -match "Found (?<vuln>\d+)\s+vulnerabilities?") {
            return @{
                vulnerabilities = [int]$matches['vuln']
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "requires_plugin"; note = "Gradle requires dependency-check plugin" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-NugetAudit {
    <#
    .SYNOPSIS
    Run NuGet audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    nuget verify checks package authenticity.
    Use SecurityCodeScan for vulnerability scanning.
    
    .EXAMPLE
    $result = Invoke-NugetAudit "C:\repos\my-project"
    Write-Host "Status: $($result.status)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & nuget verify 2>&1
        Pop-Location
        
        return @{
            vulnerabilities = 0
            timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
            status = "success"
            note = "nuget verify checks authenticity; use SecurityCodeScan for vulnerabilities"
        }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-GoModAudit {
    <#
    .SYNOPSIS
    Run Go mod audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Uses nancy (github.com/sonatype-nexus-community/nancy) for scanning
    Requires: go list command and nancy installed
    
    .EXAMPLE
    $result = Invoke-GoModAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & go list -json -m all 2>$null | & nancy sleuth --json 2>&1
        Pop-Location
        
        if ($output) {
            $vulnCount = ($output | ConvertFrom-Json | Measure-Object).Count
            return @{
                vulnerabilities = $vulnCount
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-BundlerAudit {
    <#
    .SYNOPSIS
    Run Bundler audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Requires: bundle audit gem installed
    
    .EXAMPLE
    $result = Invoke-BundlerAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & bundle audit check --json 2>&1
        Pop-Location
        
        if ($output) {
            $parsed = $output | ConvertFrom-Json
            $vulnCount = ($parsed.vulnerabilities | Measure-Object).Count
            return @{
                vulnerabilities = $vulnCount
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-ComposerAudit {
    <#
    .SYNOPSIS
    Run Composer audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Requires: PHP and Composer installed
    composer audit: checks for vulnerabilities in dependencies
    
    .EXAMPLE
    $result = Invoke-ComposerAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & composer audit --format=json 2>&1
        Pop-Location
        
        if ($output) {
            $parsed = $output | ConvertFrom-Json
            $vulnCount = ($parsed.vulnerabilities | Measure-Object).Count
            return @{
                vulnerabilities = $vulnCount
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}

function Invoke-BunAudit {
    <#
    .SYNOPSIS
    Run Bun audit on a repository.
    
    .PARAMETER RepoPath
    Path to repository
    
    .OUTPUTS
    Hashtable with vulnerabilities count or error info
    
    .NOTES
    Requires: Bun runtime installed (version 1.0+)
    
    .EXAMPLE
    $result = Invoke-BunAudit "C:\repos\my-project"
    Write-Host "Vulnerabilities: $($result.vulnerabilities)"
    #>
    param([string]$RepoPath)
    
    try {
        Push-Location $RepoPath
        $output = & bun audit 2>&1
        Pop-Location
        
        # Parse bun audit output for vulnerability counts
        if ($output -match "(?<vuln>\d+)\s+vulnerabilities?") {
            return @{
                vulnerabilities = [int]$matches['vuln']
                timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
                status = "success"
            }
        }
        return @{ vulnerabilities = 0; status = "no_vulnerabilities" }
    } catch {
        return @{ vulnerabilities = 0; status = "error"; error = $_.Exception.Message }
    }
}
