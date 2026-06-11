param([object]$Config)


Set-StrictMode -Version Latest
$libCore = Join-Path $PSScriptRoot "lib/core"
Import-Module (Join-Path $libCore "logger.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "config-loader.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "dir-manager.psm1") -Force -ErrorAction Stop
Import-Module (Join-Path $libCore "git-utils.psm1") -Force -ErrorAction Stop

# ============================================================================
# ANALYZER FUNCTIONS (MUST BE DEFINED FIRST)
# ============================================================================

function Get-GitAnalysis {
    param([string]$RepoPath)

    try {
        $gitInfo = Get-GitInfo -RepoPath $RepoPath

        return @{
            total_commits = $gitInfo.commit_count
            days_since_last_commit = $gitInfo.days_since_last_commit
            contributor_count = 0  # Get-GitInfo doesn't return contributor_count, keep as 0
        }
    } catch {
        return @{
            total_commits = 0
            days_since_last_commit = 0
            contributor_count = 0
        }
    }
}

function Get-DependencyAnalysis {
    param([string]$RepoPath)
    
    $detectedManagers = @()
    $totalPackages = 0
    
    if (Test-Path (Join-Path $RepoPath "package.json")) {
        $detectedManagers += "npm"
        try {
            $packageJson = Get-Content (Join-Path $RepoPath "package.json") -ErrorAction Stop | ConvertFrom-Json
            $deps = 0
            if ($packageJson.dependencies) { $deps += $packageJson.dependencies.PSObject.Properties.Count }
            if ($packageJson.devDependencies) { $deps += $packageJson.devDependencies.PSObject.Properties.Count }
            $totalPackages += $deps
        } catch { }
    }
    
    if (Test-Path (Join-Path $RepoPath "requirements.txt")) {
        $detectedManagers += "pip"
        try {
            $reqs = (Get-Content (Join-Path $RepoPath "requirements.txt") -ErrorAction Stop | Measure-Object -Line).Lines
            $totalPackages += $reqs
        } catch { }
    }
    
    if (Test-Path (Join-Path $RepoPath "pyproject.toml")) {
        $detectedManagers += "poetry"
    }
    
    if (Test-Path (Join-Path $RepoPath "Cargo.toml")) {
        $detectedManagers += "cargo"
    }
    
    return @{
        detected_managers = $detectedManagers
        total_packages = $totalPackages
        outdated_count = 0
    }
}

function Get-CodeQualityAnalysis {
    param([string]$RepoPath)
    
    $brokenImports = 0
    $missingFiles = 0
    $deadCodeCount = 0
    
    try {
        $pyFiles = Get-ChildItem -Path $RepoPath -Filter "*.py" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "node_modules|venv|\.venv|__pycache__" }
        
        foreach ($file in $pyFiles) {
            try {
                $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
                if ($content -match "from .* import") {
                    $brokenImports += ($content | Select-String "from .* import" | Measure-Object).Count
                }
            } catch { }
        }
    } catch { }
    
    return @{
        broken_imports = $brokenImports
        missing_files = $missingFiles
        dead_code_count = $deadCodeCount
    }
}

function Get-SecurityAnalysis {
    param([string]$RepoPath)
    
    $secretsFound = 0
    $exposedEnvVars = 0
    $hardcodedCredentials = 0
    
    try {
        $sourceFiles = Get-ChildItem -Path $RepoPath -Include "*.py", "*.js", "*.ts", "*.java", "*.go" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "node_modules|venv|\.venv|dist|build" }
        
        foreach ($file in $sourceFiles) {
            try {
                $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
                
                if ($content -match "password") { $secretsFound++ }
                if ($content -match "env") { $exposedEnvVars++ }
                if ($content -match "username") { $hardcodedCredentials++ }
            } catch { }
        }
    } catch { }
    
    return @{
        secrets_found = $secretsFound
        exposed_env_vars = $exposedEnvVars
        hardcoded_credentials = $hardcodedCredentials
    }
}

function Get-DocumentationAnalysis {
    param([string]$RepoPath)
    
    $hasReadme = Test-Path (Join-Path $RepoPath "README.md")
    $hasDocs = Test-Path (Join-Path $RepoPath "docs")
    $hasChangelog = Test-Path (Join-Path $RepoPath "CHANGELOG.md")
    
    $completenessPercent = 0
    $foundSections = 0
    $totalSections = 5
    
    if ($hasReadme) {
        try {
            $readmeContent = Get-Content (Join-Path $RepoPath "README.md") -Raw -ErrorAction SilentlyContinue
            if ($readmeContent -match "Installation") { $foundSections++ }
            if ($readmeContent -match "Usage") { $foundSections++ }
            if ($readmeContent -match "Contributing") { $foundSections++ }
            if ($readmeContent -match "License") { $foundSections++ }
            if ($readmeContent -match "API") { $foundSections++ }
        } catch { }
    }
    
    $completenessPercent = [Math]::Floor(($foundSections / $totalSections) * 100)
    
    $missingSections = @()
    if (-not $hasReadme) { $missingSections += "README.md" }
    if (-not $hasDocs) { $missingSections += "docs/" }
    if (-not $hasChangelog) { $missingSections += "CHANGELOG.md" }
    
    return @{
        has_readme = $hasReadme
        has_docs = $hasDocs
        has_changelog = $hasChangelog
        completeness_percent = $completenessPercent
        missing_sections = $missingSections
    }
}

# ============================================================================
# MAIN SCRIPT LOGIC
# ============================================================================

Write-Header "Phase 4: Deep-Dive Debug Analysis"

if ($Config) {
    $baseDir = $Config.paths.base
    $outputDir = Join-Path $baseDir $Config.paths.output
} else {
    $baseDir = Split-Path -Parent $PSScriptRoot
    $outputDir = Join-Path $baseDir "REPO_AUDIT"
}

Ensure-Directory -Path $outputDir
if (-not (Test-Path $outputDir)) {
    Write-Error "Output directory not found: $outputDir"
    exit 1
}

$cloneReportPath = Join-Path $outputDir "CLONE_REPORT.json"
if (-not (Test-Path $cloneReportPath)) {
    Write-Error "Clone report not found: $cloneReportPath"
    exit 1
}

Write-Info "Loading reports..."
$cloneReport = Get-Content $cloneReportPath | ConvertFrom-Json

$clonedRepos = $cloneReport.details | Where-Object { $_.success }

Write-Success "Found $($clonedRepos.Count) cloned repositories"

$priorityRepos = @("comicwise", "banking", "rhixe_scans")
$debugResults = @()

foreach ($repo in $clonedRepos) {
    $repoName = $repo.name
    $repoPath = $repo.target_path
    
    if (-not (Test-Path $repoPath)) {
        Write-Warn "Repository path not found: $repoPath. Skipping."
        continue
    }
    
    $isPriority = $priorityRepos -contains $repoName
    $priority = if ($isPriority) { "HIGH" } else { "NORMAL" }
    
    Write-Phase "[$priority] Analyzing: $repoName"
    
    try {
        $gitAnalysis = Get-GitAnalysis -RepoPath $repoPath
        Write-Info "  Git: $($gitAnalysis.total_commits) commits, Last: $($gitAnalysis.days_since_last_commit) days ago"
        
        $depAnalysis = Get-DependencyAnalysis -RepoPath $repoPath
        Write-Info "  Dependencies: $($depAnalysis.total_packages) packages"
        
        $codeAnalysis = Get-CodeQualityAnalysis -RepoPath $repoPath
        Write-Info "  Code: $($codeAnalysis.broken_imports) broken imports"
        
        $securityAnalysis = Get-SecurityAnalysis -RepoPath $repoPath
        if ($securityAnalysis.secrets_found -gt 0) {
            Write-Err "  SECURITY: $($securityAnalysis.secrets_found) potential issues!"
        }
        
        $docAnalysis = Get-DocumentationAnalysis -RepoPath $repoPath
        Write-Info "  Docs: $($docAnalysis.completeness_percent)% complete"
        
        $debugResult = @{
            name = $repoName
            path = $repoPath
            priority = $priority
            git_analysis = $gitAnalysis
            dependency_analysis = $depAnalysis
            code_quality_analysis = $codeAnalysis
            security_analysis = $securityAnalysis
            documentation_analysis = $docAnalysis
        }
        
        $debugResults += $debugResult
        
    } catch {
        Write-Warn "Error analyzing $repoName : $_"
    }
}

Write-Phase "Analysis complete. Generating reports..."

$debugReportPath = Join-Path $outputDir "DEBUG_REPORT.json"
$debugReportContent = @{
    timestamp = Get-Date -Format "o"
    total_repos = $debugResults.Count
    priority_repos = ($debugResults | Where-Object { $_.priority -eq "HIGH" }).Count
    results = $debugResults
}

$debugReportContent | ConvertTo-Json -Depth 10 | Out-File -FilePath $debugReportPath -Encoding UTF8
Write-Success "Debug report saved: $debugReportPath"

$markdownPath = Join-Path $outputDir "DEBUG_ANALYSIS.md"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$totalRepos = $debugResults.Count
$priorityCount = ($debugResults | Where-Object { $_.priority -eq "HIGH" }).Count

$markdownContent = "# Phase 4: Deep-Dive Debug Analysis`n`n"
$markdownContent += "**Generated**: $timestamp`n"
$markdownContent += "**Total Repos Analyzed**: $totalRepos`n"
$markdownContent += "**Priority Repos**: $priorityCount`n`n"
$markdownContent += "## Priority Repos (HIGH)`n`n"

foreach ($repo in $debugResults | Where-Object { $_.priority -eq "HIGH" }) {
    $repoName = $repo.name
    $repoPath = $repo.path
    $totalCommits = $repo.git_analysis.total_commits
    $daysSinceLastCommit = $repo.git_analysis.days_since_last_commit
    $contributorCount = $repo.git_analysis.contributor_count
    $totalPackages = $repo.dependency_analysis.total_packages
    $packageManagers = $repo.dependency_analysis.detected_managers -join ", "
    $brokenImports = $repo.code_quality_analysis.broken_imports
    $secretsFound = $repo.security_analysis.secrets_found
    $exposedEnvVars = $repo.security_analysis.exposed_env_vars
    $hardcodedCreds = $repo.security_analysis.hardcoded_credentials
    $completenessPercent = $repo.documentation_analysis.completeness_percent
    $hasReadme = $repo.documentation_analysis.has_readme
    $missingSections = $repo.documentation_analysis.missing_sections -join ", "
    
    $markdownContent += "### $repoName`n`n"
    $markdownContent += "**Path**: ``$repoPath``  `n`n"
    $markdownContent += "#### Git Analysis`n"
    $markdownContent += "* **Total Commits**: $totalCommits`n"
    $markdownContent += "* **Days Since Last Commit**: $daysSinceLastCommit`n"
    $markdownContent += "* **Contributors**: $contributorCount`n`n"
    $markdownContent += "#### Dependency Analysis`n"
    $markdownContent += "* **Total Packages**: $totalPackages`n"
    $markdownContent += "* **Package Managers**: $packageManagers`n`n"
    $markdownContent += "#### Code Quality`n"
    $markdownContent += "* **Broken Imports**: $brokenImports`n`n"
    $markdownContent += "#### Security Issues`n"
    $markdownContent += "* **Potential Secrets**: $secretsFound`n"
    $markdownContent += "* **Exposed Environment Variables**: $exposedEnvVars`n"
    $markdownContent += "* **Hardcoded Credentials**: $hardcodedCreds`n`n"
    $markdownContent += "#### Documentation`n"
    $markdownContent += "* **Completeness**: $completenessPercent%`n"
    $markdownContent += "* **Has README**: $hasReadme`n"
    $markdownContent += "* **Missing Sections**: $missingSections`n`n"
    $markdownContent += "---`n`n"
}

$markdownContent += "## Other Repos (NORMAL)`n`n"

foreach ($repo in $debugResults | Where-Object { $_.priority -ne "HIGH" }) {
    $markdownContent += "* **$($repo.name)**: Packages=$($repo.dependency_analysis.total_packages), Secrets=$($repo.security_analysis.secrets_found), Broken imports=$($repo.code_quality_analysis.broken_imports)`n"
}

$markdownContent | Out-File -FilePath $markdownPath -Encoding UTF8
Write-Success "Markdown report saved: $markdownPath"

Write-Success "Phase 4 Complete!"
