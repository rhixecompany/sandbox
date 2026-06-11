# ==============================================================================
# Disk Space Analysis Script
# Version: 1.0.0
# Description: Scans directories for 50+ dependency folder types and produces
#              a detailed disk space analysis report including drive overview,
#              top 10 largest folders, category breakdown, and cleanup estimates.
#
# Usage:
#   disk-analysis.ps1                                    # Interactive mode
#   disk-analysis.ps1 -Paths "C:\Foo","D:\Bar"           # Custom paths
#   disk-analysis.ps1 -MaxDepth 5                        # Limit scan depth
#   disk-analysis.ps1 -OutputFile "report.txt"           # Save report to file
#   disk-analysis.ps1 -Help                              # Show help
#
# Target Folder Types:
#   - Node.js: node_modules, .npm, .pnpm-store, .yarn
#   - Python: venv, __pycache__, .venv, .pytest_cache
#   - .NET: bin, obj, Packages, TestResults
#   - Java/Gradle: .gradle, build, target, .m2
#   - Build outputs: dist, build, out, .next, .nuxt
#   - Caches: .cache, .parcel-cache, .turbo, .vite, .esbuild
#   - IDE: .idea, .vscode
#
# Requirements:
#   - PowerShell 5.1+
#   - Windows Vista+
#
# Exit Codes:
#   0 - Success
#   1 - Errors occurred
# ==============================================================================

param(
    [string[]]$Paths = @(),
    [int][ValidateRange(1, 20)]$MaxDepth = 10,
    [string]$OutputFile = "",
    [switch]$Help
)


Set-StrictMode -Version Latest
# ----- Defaults -----
$DefaultPaths = @(
    $env:SCAN_PATHS -split ';' | Where-Object { $_ -and (Test-Path $_) }
)
if ($DefaultPaths.Count -eq 0) {
    $DefaultPaths = @(
        "$env:USERPROFILE\Desktop\SandBox",
        "E:\Development",
        "C:\Projects"
    ) | Where-Object { Test-Path $_ }
}

# 50+ target folder types across ALL development ecosystems (deduplicated)
$DefaultTargets = @(
    # Node.js
    "node_modules", ".npm", ".pnpm-store", ".yarn", ".yarn-cache",
    # Python
    "venv", "myvenv", "__pycache__", ".venv", ".env", ".venv34",
    "env", ".env3", "ENV", ".tox", ".pytest_cache", ".mypy_cache",
    ".coverage", "htmlcov", "*.egg-info", ".eggs", "pip-log",
    "pip-delete", ".pip", ".wheel", "wheels", "pip-build",
    # .NET
    "bin", "obj", "Packages", "TestResults",
    # Java/Gradle/Maven
    ".gradle", "build", "target", ".m2", "dependency-reduced-pom.xml",
    # Rust/Cargo
    "Cargo.lock",
    # Go
    "vendor", "go.sum",
    # PHP/Composer
    "composer.lock", ".phpunit.cache",
    # Ruby/Bundler
    "vendor/bundle", ".bundle", "Gemfile.lock",
    # Build outputs
    "dist", "out", ".output", "publish", "release",
    # Next.js/Nuxt
    ".next", ".nuxt",
    # Cache folders
    ".cache", ".parcel-cache", ".turbo", ".swc", ".esbuild",
    ".rspack", ".webpack", ".rollup.cache", ".vite", ".tsbuildinfo",
    # IDE
    ".idea", ".vscode", ".vs", ".idea_modules",
    # Coverage
    "coverage", ".nyc_output", "lcov.info",
    # Package managers
    "bower_components", ".nuget", "packages",
    # Dart/Flutter
    ".dart_tool", ".pub-cache", ".pub",
    # Android
    "app/build", ".android",
    # iOS/macOS
    "DerivedData", ".symlinks",
    # Unity
    "Library", "Temp", "Logs",
    # Unreal
    "Intermediate", "Saved", "DerivedDataCache",
    # Terraform
    ".terraform", ".terraform.lock.hcl",
    # Docker
    ".docker", "node_modules/.cache",
    # Misc
    "*.pyc", "*.pyo", ".DS_Store", "Thumbs.db"
)

# Deduplicate target array (case-insensitive on Windows)
$DefaultTargets = $DefaultTargets | Select-Object -Unique

# ----- Logging setup -----
$script:LogLines = @()
$script:Errors = 0
$script:Warnings = 0
$LogDir = Join-Path $PSScriptRoot "logs"

# ----- Load shared libraries -----
. "$PSScriptRoot\lib\log-rotate.ps1"

function Write-Log {
    param([string]$Message, [ValidateSet("INFO","WARN","ERROR","SUCCESS","SECTION")]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Level] $Message" -ForegroundColor (
        @{INFO="White";WARN="Yellow";ERROR="Red";SUCCESS="Green";SECTION="Cyan"}[$Level]
    )
    $script:LogLines += "[$timestamp] [$Level] $Message"
}

function Save-Log {
    if (-not (Test-Path -LiteralPath $LogDir)) {
        New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
    }
    $stamp = Get-Date -Format "yyyyMMdd-HHMMss"
    $logFile = Join-Path $LogDir "analysis-$stamp.log"
    $script:LogLines | Set-Content -Path $logFile -Encoding UTF8
    Write-Log "Log saved: $logFile" -Level SUCCESS
    return $logFile
}

# ----- Helper: Format bytes to human-readable -----
function Format-Size {
    param([long]$Bytes)
    if ($Bytes -ge 1GB) { return "{0:N2} GB" -f ($Bytes / 1GB) }
    elseif ($Bytes -ge 1MB) { return "{0:N2} MB" -f ($Bytes / 1MB) }
    elseif ($Bytes -ge 1KB) { return "{0:N2} KB" -f ($Bytes / 1KB) }
    else { return "$Bytes bytes" }
}

# ----- Helper: Get folder size -----
function Get-FolderSize {
    param([string]$Path)
    try {
        $result = Get-ChildItem -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue |
                  Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue
        return [long]($result.Sum ?? 0)
    } catch {
        return 0
    }
}

# ----- Helper: Categorize folder by name -----
function Get-Category {
    param([string]$FolderName)
    $name = $FolderName.ToLowerInvariant()

    # Node.js
    if ($name -in @("node_modules", ".npm", ".pnpm-store", ".yarn", ".yarn-cache", "bower_components")) {
        return "Node.js"
    }
    # Python
    if ($name -in @("venv", "myvenv", "__pycache__", ".venv", ".env", ".venv34", "env", ".env3", "env",
                     ".tox", ".pytest_cache", ".mypy_cache", ".coverage", "htmlcov", ".eggs", "pip-log",
                     "pip-delete", ".pip", ".wheel", "wheels", "pip-build")) {
        return "Python"
    }
    # .NET
    if ($name -in @("bin", "obj", "packages", "testresults", ".nuget", ".vs")) {
        return ".NET"
    }
    # Java/Gradle
    if ($name -in @(".gradle", "build", "target", ".m2", "dependency-reduced-pom.xml")) {
        return "Java/Gradle"
    }
    # Framework caches
    if ($name -in @(".next", ".nuxt", ".cache", ".parcel-cache", ".turbo", ".swc", ".esbuild",
                     ".rspack", ".webpack", ".rollup.cache", ".vite", ".tsbuildinfo", ".output")) {
        return "Framework"
    }
    # IDE
    if ($name -in @(".idea", ".vscode", ".idea_modules")) {
        return "IDE"
    }
    # Go
    if ($name -in @("vendor", "go.sum")) {
        return "Go"
    }
    # PHP
    if ($name -in @("composer.lock", ".phpunit.cache")) {
        return "PHP"
    }
    # Ruby
    if ($name -in @("vendor/bundle", ".bundle", "gemfile.lock")) {
        return "Ruby"
    }
    # Rust
    if ($name -eq "cargo.lock") {
        return "Rust"
    }
    # Dart/Flutter
    if ($name -in @(".dart_tool", ".pub-cache", ".pub")) {
        return "Dart/Flutter"
    }
    # Android
    if ($name -in @("app/build", ".android")) {
        return "Android"
    }
    # iOS/macOS
    if ($name -in @("deriveddata", ".symlinks")) {
        return "iOS/macOS"
    }
    # Unity
    if ($name -in @("library", "temp", "logs")) {
        return "Unity"
    }
    # Unreal
    if ($name -in @("intermediate", "saved", "deriveddatacache")) {
        return "Unreal"
    }
    # Terraform
    if ($name -in @(".terraform", ".terraform.lock.hcl")) {
        return "Terraform"
    }
    # Docker
    if ($name -in @(".docker", "node_modules/.cache")) {
        return "Docker"
    }
    # Coverage
    if ($name -in @("coverage", ".nyc_output", "lcov.info")) {
        return "Coverage"
    }
    # Build outputs
    if ($name -in @("dist", "out", "publish", "release")) {
        return "Build"
    }
    # Misc
    if ($name -in @("*.pyc", "*.pyo", ".ds_store", "thumbs.db")) {
        return "Misc"
    }

    return "Other"
}

# ----- Scanning -----
function Get-DependencyFolders {
    param([string[]]$BasePaths, [int]$Depth, [string[]]$TargetNames)

    $all = @()
    foreach ($path in $BasePaths) {
        Write-Log "Scanning: $path (depth $Depth)" -Level SECTION
        try {
            $dirs = Get-ChildItem -LiteralPath $path -Directory -Recurse -Depth $Depth -ErrorAction SilentlyContinue
            $found = $dirs | Where-Object { $TargetNames -contains $_.Name }
            foreach ($d in $found) {
                $all += $d.FullName
            }
            Write-Log "Found $($found.Count) target folders in $path" -Level INFO
        } catch {
            Write-Log "Error scanning $path : $_" -Level ERROR
            $script:Errors++
        }
    }
    return $all
}

# ----- Drive Overview -----
function Get-DriveOverview {
    param([string[]]$FolderPaths)

    $drives = @{}
    foreach ($folder in $FolderPaths) {
        $driveLetter = [System.IO.Path]::GetPathRoot($folder).TrimEnd('\')
        if ($driveLetter -and -not $drives.ContainsKey($driveLetter)) {
            try {
                $drive = Get-PSDrive -Name $driveLetter.TrimEnd(':') -PSProvider FileSystem -ErrorAction SilentlyContinue
                if ($drive) {
                    $drives[$driveLetter] = @{
                        Total = $drive.Used + $drive.Free
                        Free  = $drive.Free
                        Used  = $drive.Used
                    }
                }
            } catch {
                # Skip drives we can't query
            }
        }
    }
    return $drives
}

# ======================= MAIN =======================

# --- Help ---
if ($Help) {
    Write-Host ""
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host "   Disk Space Analysis  v1.0.0" -ForegroundColor Cyan
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Scans directories for 50+ dependency folder types and"
    Write-Host "produces a detailed disk space analysis report."
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\disk-analysis.ps1                                    # Default scan"
    Write-Host "  .\disk-analysis.ps1 -Paths `"C:\Foo`,`"D:\Bar`"          # Custom paths"
    Write-Host "  .\disk-analysis.ps1 -MaxDepth 5                        # Limit depth"
    Write-Host "  .\disk-analysis.ps1 -OutputFile `"report.txt`"           # Save report"
    Write-Host "  .\disk-analysis.ps1 -Help                              # This help"
    Write-Host ""
    exit 0
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "   Disk Space Analysis  v1.0.0" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

Write-Log "=== Analysis started ===" -Level SECTION

# Use defaults if not specified
if ($Paths.Count -eq 0) { $Paths = $DefaultPaths }
$Targets = $DefaultTargets

# --- Validate paths ---
$existingPaths = $Paths | Where-Object { Test-Path -LiteralPath $_ }
if ($existingPaths.Count -eq 0) {
    Write-Log "No valid paths found. Exiting." -Level ERROR
    exit 1
}

Write-Log "Scanning $($existingPaths.Count) path(s) for $($Targets.Count) target types..." -Level SECTION
Write-Log "Max depth: $MaxDepth" -Level INFO

# --- Scan phase ---
$allFolders = Get-DependencyFolders -BasePaths $existingPaths -Depth $MaxDepth -TargetNames $Targets

if ($allFolders.Count -eq 0) {
    Write-Log "No dependency folders found." -Level SUCCESS
    exit 0
}

Write-Log ""
Write-Log "=== Found $($allFolders.Count) dependency folders ===" -Level SECTION

# --- Calculate sizes ---
Write-Log "Calculating folder sizes..." -Level SECTION
$folderData = @()
foreach ($folder in $allFolders) {
    $size = Get-FolderSize -Path $folder
    $category = Get-Category -FolderName (Split-Path $folder -Leaf)
    $folderData += @{
        Path     = $folder
        Size     = $size
        Category = $category
    }
}

# Sort by size descending
$folderData = $folderData | Sort-Object -Property Size -Descending

# --- Build report ---
$reportLines = @()
function Add-Report {
    param([string]$Line, [ConsoleColor]$Color = "White")
    $reportLines += $Line
    Write-Host $Line -ForegroundColor $Color
}

Add-Report ""
Add-Report "=== Disk Space Analysis v1.0.0 ===" -ForegroundColor Cyan
Add-Report ""

# --- Drive Overview ---
Add-Report "=== Drive Overview ===" -ForegroundColor Cyan
$drives = Get-DriveOverview -FolderPaths $allFolders
foreach ($driveLetter in $drives.Keys | Sort-Object) {
    $info = $drives[$driveLetter]
    $total = $info.Total
    $free = $info.Free
    $used = $info.Used
    $pct = if ($total -gt 0) { [math]::Round(($used / $total) * 100) } else { 0 }
    Add-Report "Drive $driveLetter  Total: $(Format-Size $total) | Free: $(Format-Size $free) | Used: $(Format-Size $used) | Usage: ${pct}%" -ForegroundColor White
}
Add-Report ""

# --- Top 10 Largest ---
Add-Report "=== Top 10 Largest Dependency Folders ===" -ForegroundColor Cyan
$top10 = $folderData | Select-Object -First 10
$top10Total = 0
$idx = 1
foreach ($item in $top10) {
    $sizeStr = Format-Size $item.Size
    $padSize = $sizeStr.PadLeft(8)
    Add-Report "  $idx. $padSize  $($item.Path)" -ForegroundColor White
    $top10Total += $item.Size
    $idx++
}
Add-Report "  Total: $(Format-Size $top10Total) across $($top10.Count) folders" -ForegroundColor Green
Add-Report ""

# --- Category Breakdown ---
Add-Report "=== Space by Category ===" -ForegroundColor Cyan
$categoryGroups = $folderData | Group-Object -Property Category
$grandTotal = ($folderData | Measure-Object -Property Size -Sum).Sum

$categorySummary = @()
foreach ($group in $categoryGroups) {
    $catTotal = ($group.Group | Measure-Object -Property Size -Sum).Sum
    $pct = if ($grandTotal -gt 0) { [math]::Round(($catTotal / $grandTotal) * 100) } else { 0 }
    $count = $group.Count
    $categorySummary += @{
        Category = $group.Name
        Size     = $catTotal
        Pct      = $pct
        Count    = $count
    }
}

# Sort by size descending
$categorySummary = $categorySummary | Sort-Object -Property Size -Descending

foreach ($cat in $categorySummary) {
    $sizeStr = Format-Size $cat.Size
    $padSize = $sizeStr.PadLeft(8)
    $padCat = $cat.Category.PadRight(14)
    $padPct = "$($cat.Pct)%".PadLeft(4)
    Add-Report "  $padCat : $padSize ($padPct)  [$($cat.Count) folders]" -ForegroundColor White
}
Add-Report ""

# --- Summary ---
Add-Report "=== Summary ===" -ForegroundColor Cyan
Add-Report "  Total dependency folders: $($folderData.Count)" -ForegroundColor White
Add-Report "  Total space used: $(Format-Size $grandTotal)" -ForegroundColor White
Add-Report "  Estimated cleanup savings: $(Format-Size $grandTotal) (if all deleted)" -ForegroundColor Green
Add-Report ""

# --- Save report to file if requested ---
if ($OutputFile) {
    try {
        $reportLines | Out-File -FilePath $OutputFile -Encoding UTF8 -Force
        Write-Log "Report saved: $OutputFile" -Level SUCCESS
    } catch {
        Write-Log "Failed to save report: $_" -Level ERROR
        $script:Errors++
    }
}

# --- Save log ---
Save-Log | Out-Null

# Rotate logs - keep last 10
Rotate-Logs -LogDir $LogDir

Write-Log "=== Analysis completed ===" -Level SECTION
exit $(if ($script:Errors -gt 0) { 1 } else { 0 })
