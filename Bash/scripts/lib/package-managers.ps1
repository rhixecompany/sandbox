<#
.SYNOPSIS
    Package Manager Registry and Detection
    
.DESCRIPTION
    Defines all supported package managers with detection and scanning logic.
    Provides a centralized registry for managing multiple package managers.
#>


Set-StrictMode -Version Latest
# Registry structure: Each manager has:
# - name: display name
# - detector: function name to detect presence
# - scanner: function name to run audit
# - file_patterns: glob patterns for detection
# - note: description

$script:PackageManagerRegistry = @(
    @{
        name = "npm"
        detector = "Test-NpmPresent"
        scanner = "Invoke-NpmAudit"
        file_patterns = @("package.json", "package-lock.json")
        note = "Node Package Manager"
    }
    @{
        name = "pnpm"
        detector = "Test-PnpmPresent"
        scanner = "Invoke-PnpmAudit"
        file_patterns = @("pnpm-lock.yaml", "pnpm-workspace.yaml")
        note = "Fast, disk space efficient package manager"
    }
    @{
        name = "yarn"
        detector = "Test-YarnPresent"
        scanner = "Invoke-YarnAudit"
        file_patterns = @("yarn.lock", ".yarnrc")
        note = "Yarn package manager"
    }
    @{
        name = "pip"
        detector = "Test-PipPresent"
        scanner = "Invoke-PipCheck"
        file_patterns = @("requirements.txt", "setup.py", "pyproject.toml", "Pipfile")
        note = "Python package manager"
    }
    @{
        name = "poetry"
        detector = "Test-PoetryPresent"
        scanner = "Invoke-PoetryCheck"
        file_patterns = @("pyproject.toml", "poetry.lock")
        note = "Python dependency management and packaging"
    }
    @{
        name = "Maven"
        detector = "Test-MavenPresent"
        scanner = "Invoke-MavenAudit"
        file_patterns = @("pom.xml")
        note = "Apache Maven build tool"
    }
    @{
        name = "Gradle"
        detector = "Test-GradlePresent"
        scanner = "Invoke-GradleAudit"
        file_patterns = @("build.gradle", "build.gradle.kts", "gradle.properties")
        note = "Gradle build automation"
    }
    @{
        name = "NuGet"
        detector = "Test-NugetPresent"
        scanner = "Invoke-NugetAudit"
        file_patterns = @("*.csproj", "packages.config", "nuget.config")
        note = ".NET package manager"
    }
    @{
        name = "Go Modules"
        detector = "Test-GoModPresent"
        scanner = "Invoke-GoModAudit"
        file_patterns = @("go.mod", "go.sum")
        note = "Go dependency management"
    }
    @{
        name = "Cargo"
        detector = "Test-CargoPresent"
        scanner = "Invoke-CargoAudit"
        file_patterns = @("Cargo.toml", "Cargo.lock")
        note = "Rust package manager"
    }
    @{
        name = "Bundler"
        detector = "Test-BundlerPresent"
        scanner = "Invoke-BundlerAudit"
        file_patterns = @("Gemfile", "Gemfile.lock")
        note = "Ruby dependency manager"
    }
    @{
        name = "Composer"
        detector = "Test-ComposerPresent"
        scanner = "Invoke-ComposerAudit"
        file_patterns = @("composer.json", "composer.lock")
        note = "PHP dependency manager"
    }
    @{
        name = "Bun"
        detector = "Test-BunPresent"
        scanner = "Invoke-BunAudit"
        file_patterns = @("bunfig.toml", "bun.lockb")
        note = "JavaScript runtime and package manager"
    }
)

function Get-PackageManagerRegistry {
    <#
    .SYNOPSIS
    Returns the package manager registry.
    
    .DESCRIPTION
    Returns an array of hashtables, each defining a package manager's metadata.
    
    .OUTPUTS
    Array[Hashtable] with manager definitions
    
    .EXAMPLE
    $registry = Get-PackageManagerRegistry
    $registry | ForEach-Object { Write-Host $_.name }
    #>
    return $script:PackageManagerRegistry
}

function Get-ManagerByName {
    <#
    .SYNOPSIS
    Get a specific manager definition by name.
    
    .PARAMETER ManagerName
    Name of the manager to retrieve (e.g., "npm", "pip")
    
    .OUTPUTS
    Hashtable with manager metadata or $null if not found
    
    .EXAMPLE
    $npm = Get-ManagerByName "npm"
    Write-Host "Scanner: $($npm.scanner)"
    #>
    param([string]$ManagerName)
    
    return ($script:PackageManagerRegistry | Where-Object { $_.name -eq $ManagerName })
}

# ============================================================================
# Detector Functions - Check if package manager is present in repo
# ============================================================================

function Test-NpmPresent {
    <#
    .SYNOPSIS
    Check if npm is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if npm is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "package.json")) -or 
           (Test-Path (Join-Path $RepoPath "package-lock.json"))
}

function Test-PnpmPresent {
    <#
    .SYNOPSIS
    Check if pnpm is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if pnpm is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "pnpm-lock.yaml")) -or 
           (Test-Path (Join-Path $RepoPath "pnpm-workspace.yaml"))
}

function Test-YarnPresent {
    <#
    .SYNOPSIS
    Check if Yarn is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Yarn is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "yarn.lock")) -or 
           (Test-Path (Join-Path $RepoPath ".yarnrc"))
}

function Test-PipPresent {
    <#
    .SYNOPSIS
    Check if pip (Python) is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if pip is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "requirements.txt")) -or 
           (Test-Path (Join-Path $RepoPath "setup.py")) -or 
           (Test-Path (Join-Path $RepoPath "pyproject.toml")) -or 
           (Test-Path (Join-Path $RepoPath "Pipfile"))
}

function Test-PoetryPresent {
    <#
    .SYNOPSIS
    Check if Poetry is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Poetry is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "poetry.lock"))
}

function Test-MavenPresent {
    <#
    .SYNOPSIS
    Check if Maven is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Maven is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "pom.xml"))
}

function Test-GradlePresent {
    <#
    .SYNOPSIS
    Check if Gradle is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Gradle is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "build.gradle")) -or 
           (Test-Path (Join-Path $RepoPath "build.gradle.kts")) -or 
           (Test-Path (Join-Path $RepoPath "gradle.properties"))
}

function Test-NugetPresent {
    <#
    .SYNOPSIS
    Check if NuGet is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if NuGet is detected, $false otherwise
    #>
    param([string]$RepoPath)
    $csprojFiles = Get-ChildItem -Path $RepoPath -Filter "*.csproj" -Recurse -ErrorAction SilentlyContinue
    return ($csprojFiles.Count -gt 0) -or 
           (Test-Path (Join-Path $RepoPath "packages.config")) -or 
           (Test-Path (Join-Path $RepoPath "nuget.config"))
}

function Test-GoModPresent {
    <#
    .SYNOPSIS
    Check if Go Modules is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Go Modules is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "go.mod"))
}

function Test-CargoPresent {
    <#
    .SYNOPSIS
    Check if Cargo (Rust) is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Cargo is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "Cargo.toml"))
}

function Test-BundlerPresent {
    <#
    .SYNOPSIS
    Check if Bundler (Ruby) is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Bundler is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "Gemfile")) -or 
           (Test-Path (Join-Path $RepoPath "Gemfile.lock"))
}

function Test-ComposerPresent {
    <#
    .SYNOPSIS
    Check if Composer (PHP) is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Composer is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "composer.json")) -or 
           (Test-Path (Join-Path $RepoPath "composer.lock"))
}

function Test-BunPresent {
    <#
    .SYNOPSIS
    Check if Bun is present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to check
    
    .OUTPUTS
    Boolean - $true if Bun is detected, $false otherwise
    #>
    param([string]$RepoPath)
    return (Test-Path (Join-Path $RepoPath "bunfig.toml")) -or 
           (Test-Path (Join-Path $RepoPath "bun.lockb"))
}

function Detect-PackageManagers {
    <#
    .SYNOPSIS
    Detect which package managers are present in a repository.
    
    .PARAMETER RepoPath
    Path to repository to scan
    
    .OUTPUTS
    Array of detected manager names (strings)
    
    .EXAMPLE
    $detected = Detect-PackageManagers "C:\repos\my-project"
    Write-Host "Detected: $($detected -join ', ')"
    #>
    param([string]$RepoPath)
    
    if (-not (Test-Path $RepoPath)) {
        return @()
    }
    
    $detected = @()
    $registry = Get-PackageManagerRegistry
    
    foreach ($manager in $registry) {
        $detectorFunc = $manager.detector
        if (& $detectorFunc $RepoPath) {
            $detected += $manager.name
        }
    }
    
    return $detected
}
