#Requires -Version 7.0
<#
.SYNOPSIS
Unified Script Orchestrator - Manages all 177 Sandbox/Bash scripts
Auto-runs core production tasks with interactive category selection, 
error handling, and structured logging.

.DESCRIPTION
- Discovers all 177 scripts across 11 directories
- Groups into: Core (64) + Domain-Specific (95) + Utilities (18)
- Auto-runs core production pipeline or interactive mode
- Provides category-based script selection
- Full error handling, retry logic, and JSON logging
- Real-time progress tracking and metrics collection

.PARAMETER Mode
    'auto' (default) - Execute core production pipeline
    'interactive' - Choose categories and scripts interactively
    'discover' - List all scripts and exit
    'validate' - Syntax check all scripts

.PARAMETER Category
    Filter to specific category: Core, Banking, Comicwise, etc.

.PARAMETER ScriptFilter
    Run scripts matching pattern (e.g., 'cache-clean', 'upgrade')

.PARAMETER DryRun
    Preview operations without execution

.PARAMETER LogPath
    Custom log directory (default: ./logs)

.EXAMPLE
    .\orchestrator-unified.ps1
    # Auto-runs core production pipeline

.EXAMPLE
    .\orchestrator-unified.ps1 -Mode interactive
    # Interactive category/script selection

.EXAMPLE
    .\orchestrator-unified.ps1 -Category Banking -DryRun
    # Preview Banking scripts

.NOTES
    Author: Alexa
    Date: 2026-05-27
    Status: Production
#>

param(
    [ValidateSet('auto', 'interactive', 'discover', 'validate')]
    [string]$Mode = 'auto',
    
    [string]$Category = '',
    [string]$ScriptFilter = '',
    [switch]$DryRun,
    [string]$LogPath = './logs'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS & CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

$Script:Config = @{
    BasePath           = Get-Location
    LogPath            = $LogPath
    StartTime          = Get-Date
    DryRun             = $DryRun
    Verbose            = $VerbosePreference -eq 'Continue'
    MaxRetries         = 1
    TimeoutSeconds     = 60
    ErrorLogFile       = $null
    MetricsLogFile     = $null
}

$Script:Metrics = @{
    TotalScripts     = 0
    ExecutedScripts  = 0
    SuccessCount     = 0
    FailureCount     = 0
    SkippedCount     = 0
    Errors           = @()
    ExecutionTimes   = @()
    StartTime        = Get-Date
}

# Script category definitions
$Script:Categories = @{
    'Core' = @{
        Description = 'Core Production Scripts (64 scripts)'
        Paths       = @('src', 'scripts', '.') # Root scripts
        Priority    = 1
        Scripts     = @()
    }
    'Banking' = @{
        Description = 'Banking Domain (34 scripts)'
        Paths       = @('Banking')
        Priority    = 2
        Scripts     = @()
    }
    'Archive' = @{
        Description = 'Git Commit Batches (51 scripts)'
        Paths       = @('archive/skills-commit-batches')
        Priority    = 3
        Scripts     = @()
    }
    'Comicwise' = @{
        Description = 'Comic/Media Project (10 scripts)'
        Paths       = @('comicwise')
        Priority    = 4
        Scripts     = @()
    }
    'Bash' = @{
        Description = 'Bash Migration Utils (7 scripts)'
        Paths       = @('Bash')
        Priority    = 5
        Scripts     = @()
    }
    'Utilities' = @{
        Description = 'Misc Utils (tests, lib, ecom, rhixe_scans, etc.)'
        Paths       = @('tests', 'lib', 'ecom', 'rhixe_scans', 'root')
        Priority    = 6
        Scripts     = @()
    }
}

# Auto-run core pipeline (sequential order)
# NOTE: Skip upgrade & test-all in auto mode due to:
#   - upgrade.ps1 requires UAC (hangs in job context)
#   - test-all.sh has bash spawn issues from pwsh job wrapper
$Script:AutoRunPipeline = @(
    @{ Category = 'Core'; Pattern = 'disk-analysis\.ps1$'; Description = 'Analyze disk usage'; Exact = $true }
    @{ Category = 'Core'; Pattern = 'cache-clean\.ps1$'; Description = 'Clean caches'; Exact = $true }
    @{ Category = 'Core'; Pattern = 'clean-dependency-folders\.ps1$'; Description = 'Clean dependencies'; Exact = $true }
)

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING & OUTPUT
# ─────────────────────────────────────────────────────────────────────────────

function Initialize-Logging {
    <#
    .SYNOPSIS
    Initialize logging infrastructure
    #>
    
    if (-not (Test-Path $Config.LogPath)) {
        New-Item -ItemType Directory -Path $Config.LogPath -Force | Out-Null
    }
    
    $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $Config.ErrorLogFile = Join-Path $Config.LogPath "errors-$timestamp.json"
    $Config.MetricsLogFile = Join-Path $Config.LogPath "metrics-$timestamp.json"
    
    # Initialize JSON log files
    @{
        StartTime = Get-Date -Format o
        Errors    = @()
    } | ConvertTo-Json | Set-Content $Config.ErrorLogFile
    
    @{
        StartTime      = Get-Date -Format o
        Pipeline       = @()
        ScriptExecTime = @{}
    } | ConvertTo-Json | Set-Content $Config.MetricsLogFile
    
    Write-Host "📝 Logs: $($Config.LogPath)" -ForegroundColor Cyan
    Write-Host "  ├─ Errors: $(Split-Path $Config.ErrorLogFile -Leaf)" -ForegroundColor Gray
    Write-Host "  └─ Metrics: $(Split-Path $Config.MetricsLogFile -Leaf)" -ForegroundColor Gray
}

function Write-Log {
    [CmdletBinding()]
    param(
        [string]$Message,
        [ValidateSet('INFO', 'SUCCESS', 'WARNING', 'ERROR')]
        [string]$Level = 'INFO',
        [object]$Data = $null
    )
    
    $timestamp = Get-Date -Format 'HH:mm:ss'
    $symbol = @{
        'INFO'    = 'ℹ️ '
        'SUCCESS' = '✓ '
        'WARNING' = '⚠️ '
        'ERROR'   = '✗ '
    }[$Level]
    
    $color = @{
        'INFO'    = 'White'
        'SUCCESS' = 'Green'
        'WARNING' = 'Yellow'
        'ERROR'   = 'Red'
    }[$Level]
    
    Write-Host "$symbol [$timestamp] $Message" -ForegroundColor $color
    
    if ($Data) {
        Write-Host ($Data | ConvertTo-Json -Depth 3) -ForegroundColor Gray -Indent 2
    }
}

function Write-Error-Log {
    [CmdletBinding()]
    param(
        [string]$ScriptName,
        [string]$ErrorMessage,
        [int]$ExitCode = 1
    )
    
    $error_obj = @{
        Timestamp   = Get-Date -Format o
        Script      = $ScriptName
        Error       = $ErrorMessage
        ExitCode    = $ExitCode
    }
    
    $Metrics.Errors += $error_obj
    
    # Append to error log file
    $log = Get-Content $Config.ErrorLogFile | ConvertFrom-Json
    $log.Errors += $error_obj
    $log | ConvertTo-Json | Set-Content $Config.ErrorLogFile
}

# ─────────────────────────────────────────────────────────────────────────────
# SCRIPT DISCOVERY & CATEGORIZATION
# ─────────────────────────────────────────────────────────────────────────────

function Discover-Scripts {
    <#
    .SYNOPSIS
    Discover and categorize all 177 scripts
    #>
    
    Write-Host "`n🔍 Discovering scripts..." -ForegroundColor Cyan
    
    $allScripts = @()
    
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $cat = $Categories[$catName]
        $scripts = @()
        
        foreach ($path in $cat.Paths) {
            $searchPath = if ($path -eq '.') { 
                $Config.BasePath 
            } else { 
                Join-Path $Config.BasePath $path 
            }
            
            if (Test-Path $searchPath) {
                $found = Get-ChildItem -Path $searchPath -Recurse -Include '*.sh', '*.ps1', '*.bat', '*.ts' `
                    -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\node_modules' }
                
                $scripts += $found
            }
        }
        
        $cat.Scripts = $scripts | Select-Object -Unique
        $allScripts += $scripts
    }
    
    $Metrics.TotalScripts = @($allScripts | Select-Object -Unique).Count
    
    # Display summary
    Write-Host "`n📊 Discovery Summary:" -ForegroundColor Green
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $count = @($Categories[$catName].Scripts).Count
        if ($count -gt 0) {
            Write-Host "  • $catName`: $count scripts" -ForegroundColor White
        }
    }
    Write-Host "  ─────────────────────" -ForegroundColor Gray
    Write-Host "  TOTAL: $($Metrics.TotalScripts) scripts" -ForegroundColor Cyan
}

# ─────────────────────────────────────────────────────────────────────────────
# SCRIPT EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

function Invoke-Script {
    [CmdletBinding()]
    param(
        [System.IO.FileInfo]$ScriptFile,
        [int]$Index = 0,
        [int]$Total = 1
    )
    
    $scriptName = $ScriptFile.Name
    $scriptPath = $ScriptFile.FullName
    $ext = $ScriptFile.Extension
    
    Write-Host "`n  [$Index/$Total] Running: $scriptName" -ForegroundColor Yellow
    
    $startTime = Get-Date
    $success = $false
    $output = ''
    $retryCount = 0
    
    do {
        try {
            if ($Config.DryRun) {
                Write-Host "    [DRY-RUN] Would execute: $scriptPath" -ForegroundColor Cyan
                $success = $true
                break
            }
            
            # For shell scripts on Windows, just do syntax check (don't execute)
            if ($ext -eq '.sh') {
                Write-Host "    [SYNTAX-CHECK] Validating shell script..." -ForegroundColor Cyan
                $output = bash -n $scriptPath 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "    ✓ Valid" -ForegroundColor Green
                    $success = $true
                } else {
                    throw "Syntax error: $output"
                }
                break
            }
            
            # Execute PowerShell and Batch with timeout
            $output = $null
            $job = $null
            
            switch ($ext) {
                '.ps1' {
                    $job = Start-Job -ScriptBlock {
                        param($Path)
                        & pwsh -NoProfile -ExecutionPolicy Bypass -File $Path 2>&1
                    } -ArgumentList $scriptPath
                }
                '.bat' {
                    $job = Start-Job -ScriptBlock {
                        param($Path)
                        & cmd /c $Path 2>&1
                    } -ArgumentList $scriptPath
                }
                '.ts' {
                    $job = Start-Job -ScriptBlock {
                        param($Path)
                        bunx tsx $Path 2>&1
                    } -ArgumentList $scriptPath
                }
                default {
                    throw "Unsupported file type: $ext"
                }
            }
            
            # Wait for job with timeout
            if ($job) {
                $completed = Wait-Job -Job $job -Timeout $Config.TimeoutSeconds
                if (-not $completed) {
                    Stop-Job -Job $job -Force -ErrorAction SilentlyContinue | Out-Null
                    Remove-Job -Job $job -Force -ErrorAction SilentlyContinue | Out-Null
                    throw "Execution timeout after $($Config.TimeoutSeconds) seconds"
                }
                
                $output = Receive-Job -Job $job -ErrorAction SilentlyContinue
                $exitCode = $job.ChildJobs[0].JobStateInfo.State
                Remove-Job -Job $job -Force -ErrorAction SilentlyContinue | Out-Null
                
                # Check if job completed successfully
                if ($exitCode -eq 'Completed') {
                    $success = $true
                } else {
                    throw "Job failed with state: $exitCode. Output: $output"
                }
            }
            
            $Metrics.SuccessCount++
            Write-Host "    ✓ Success" -ForegroundColor Green
            
        } catch {
            $retryCount++
            $errorMsg = $_.Exception.Message
            
            if ($retryCount -lt $Config.MaxRetries) {
                Write-Host "    ⚠️  Attempt $retryCount failed, retrying..." -ForegroundColor Yellow
                Start-Sleep -Seconds 2
            } else {
                Write-Host "    ✗ Failed after $retryCount attempts" -ForegroundColor Red
                Write-Host "      Error: $errorMsg" -ForegroundColor Red
                Write-Error-Log -ScriptName $scriptName -ErrorMessage $errorMsg
                $Metrics.FailureCount++
                $success = $false
            }
        }
    } while (-not $success -and $retryCount -lt $Config.MaxRetries)
    
    $elapsed = (Get-Date) - $startTime
    $Metrics.ExecutionTimes += @{
        Script  = $scriptName
        Elapsed = $elapsed.TotalSeconds
    }
    
    $Metrics.ExecutedScripts++
    
    return $success
}

# ─────────────────────────────────────────────────────────────────────────────
# INTERACTIVE MODE
# ─────────────────────────────────────────────────────────────────────────────

function Show-CategoryMenu {
    <#
    .SYNOPSIS
    Display interactive category selection
    #>
    
    Write-Host "`n🎯 SELECT CATEGORY:" -ForegroundColor Cyan
    $i = 1
    
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $count = @($Categories[$catName].Scripts).Count
        Write-Host "  $i) $catName`: $count scripts" -ForegroundColor White
        $i++
    }
    Write-Host "  $i) All" -ForegroundColor White
    Write-Host "  0) Exit" -ForegroundColor Gray
    
    $choice = Read-Host "`nEnter choice"
    return $choice
}

function Show-ScriptMenu {
    [CmdletBinding()]
    param(
        [string]$Category
    )
    
    $scripts = $Categories[$Category].Scripts
    
    if ($scripts.Count -eq 0) {
        Write-Host "No scripts found in $Category" -ForegroundColor Yellow
        return $null
    }
    
    Write-Host "`n🎯 SELECT SCRIPT from $Category`:" -ForegroundColor Cyan
    $i = 1
    
    foreach ($script in $scripts | Sort-Object Name) {
        Write-Host "  $i) $($script.Name)" -ForegroundColor White
        $i++
    }
    Write-Host "  0) Back" -ForegroundColor Gray
    
    $choice = Read-Host "`nEnter choice"
    
    if ($choice -eq '0' -or [int]$choice -lt 1 -or [int]$choice -gt $scripts.Count) {
        return $null
    }
    
    return $scripts[[int]$choice - 1]
}

function Run-Interactive {
    <#
    .SYNOPSIS
    Interactive mode with menu-driven script selection
    #>
    
    do {
        $catChoice = Show-CategoryMenu
        
        if ($catChoice -eq '0') { break }
        
        $catIndex = 1
        $selectedCat = $null
        
        foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
            if ([int]$catChoice -eq $catIndex) {
                $selectedCat = $catName
                break
            }
            $catIndex++
        }
        
        if ($selectedCat) {
            $script = Show-ScriptMenu -Category $selectedCat
            
            if ($script) {
                Invoke-Script -ScriptFile $script -Index 1 -Total 1
                
                $continue = Read-Host "`nContinue? (y/n)"
                if ($continue -ne 'y') { break }
            }
        }
        
    } while ($true)
}

# ─────────────────────────────────────────────────────────────────────────────
# AUTO-RUN PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

function Run-AutoPipeline {
    <#
    .SYNOPSIS
    Execute core production pipeline in sequence
    #>
    
    Write-Host "`n▶️  AUTO-RUN PIPELINE" -ForegroundColor Cyan
    Write-Host "Running core production scripts in sequence...`n" -ForegroundColor White
    
    $index = 1
    $successCount = 0
    $totalTasks = @($Script:AutoRunPipeline).Count
    
    foreach ($task in $Script:AutoRunPipeline) {
        $categoryScripts = $Categories[$task.Category].Scripts
        
        $scripts = $categoryScripts | Where-Object { 
            $_.Name -match $task.Pattern
        }
        
        if ($scripts) {
            Write-Host "`n── $($task.Description) ──" -ForegroundColor Magenta
            
            # Take only the first matching script to avoid executing multiple variants
            $script = $scripts | Select-Object -First 1
            
            if (Invoke-Script -ScriptFile $script -Index $index -Total $totalTasks) {
                $successCount++
            }
            $index++
        } else {
            Write-Host "  ⚠️  No scripts matched" -ForegroundColor Yellow
        }
    }
    
    return $successCount
}

# ─────────────────────────────────────────────────────────────────────────────
# VALIDATION & DISCOVERY MODES
# ─────────────────────────────────────────────────────────────────────────────

function Run-Validate {
    <#
    .SYNOPSIS
    Validate syntax of all shell scripts
    #>
    
    Write-Host "`n🔍 VALIDATING SCRIPTS..." -ForegroundColor Cyan
    
    $index = 1
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $scripts = $Categories[$catName].Scripts | Where-Object { $_.Extension -eq '.sh' }
        
        foreach ($script in $scripts) {
            Write-Host "[$index] Validating: $($script.Name)" -ForegroundColor White
            
            try {
                $output = bash -n $script.FullName 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "  ✓ Valid" -ForegroundColor Green
                } else {
                    Write-Host "  ✗ Syntax error: $output" -ForegroundColor Red
                    Write-Error-Log -ScriptName $script.Name -ErrorMessage $output
                }
            } catch {
                Write-Host "  ? Check failed: $($_.Exception.Message)" -ForegroundColor Yellow
            }
            
            $index++
        }
    }
}

function Run-Discover {
    <#
    .SYNOPSIS
    List all scripts and exit
    #>
    
    Discover-Scripts
    
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $scripts = $Categories[$catName].Scripts
        
        if ($scripts.Count -gt 0) {
            Write-Host "`n📂 $catName`:" -ForegroundColor Green
            
            foreach ($script in $scripts | Sort-Object Name) {
                $relPath = $script.FullName.Replace($Config.BasePath, '').TrimStart('\')
                Write-Host "  • $relPath" -ForegroundColor Gray
            }
        }
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# REPORTING & METRICS
# ─────────────────────────────────────────────────────────────────────────────

function Show-Report {
    <#
    .SYNOPSIS
    Display execution report and metrics
    #>
    
    $elapsed = (Get-Date) - $Config.StartTime
    $avgTime = if ($Metrics.ExecutedScripts -gt 0) { 
        ($Metrics.ExecutionTimes | Measure-Object -Property Elapsed -Average).Average 
    } else { 
        0 
    }
    
    Write-Host "`n$('='*80)" -ForegroundColor Cyan
    Write-Host "📊 EXECUTION REPORT" -ForegroundColor Cyan
    Write-Host $('='*80) -ForegroundColor Cyan
    
    Write-Host "`n📈 Statistics:" -ForegroundColor White
    Write-Host "  Total Scripts Found: $($Metrics.TotalScripts)" -ForegroundColor White
    Write-Host "  Scripts Executed:    $($Metrics.ExecutedScripts)" -ForegroundColor White
    Write-Host "  Successful:          $($Metrics.SuccessCount)" -ForegroundColor Green
    Write-Host "  Failed:              $($Metrics.FailureCount)" -ForegroundColor $(if ($Metrics.FailureCount -gt 0) { 'Red' } else { 'Green' })
    Write-Host "  Skipped:             $($Metrics.SkippedCount)" -ForegroundColor Yellow
    
    Write-Host "`n⏱️  Timing:" -ForegroundColor White
    Write-Host "  Total Duration:      $([math]::Round($elapsed.TotalSeconds, 2))s" -ForegroundColor White
    Write-Host "  Average Per Script:  $([math]::Round($avgTime, 2))s" -ForegroundColor White
    
    if ($Metrics.Errors.Count -gt 0) {
        Write-Host "`n❌ Errors:" -ForegroundColor Red
        foreach ($err in $Metrics.Errors | Select-Object -First 5) {
            Write-Host "  • $($err.Script): $($err.Error)" -ForegroundColor Red
        }
        if ($Metrics.Errors.Count -gt 5) {
            Write-Host "  ... and $($Metrics.Errors.Count - 5) more" -ForegroundColor Red
        }
    }
    
    Write-Host "`n📁 Log Files:" -ForegroundColor White
    Write-Host "  Errors:  $(Split-Path $Config.ErrorLogFile -Leaf)" -ForegroundColor Gray
    Write-Host "  Metrics: $(Split-Path $Config.MetricsLogFile -Leaf)" -ForegroundColor Gray
    
    Write-Host "`n$('='*80)`n" -ForegroundColor Cyan
}

# ─────────────────────────────────────────────────────────────────────────────
# MAIN ORCHESTRATION
# ─────────────────────────────────────────────────────────────────────────────

function Invoke-Orchestrator {
    <#
    .SYNOPSIS
    Main orchestrator entry point
    #>
    
    Write-Host "`n$('╔' + '═'*78 + '╗')" -ForegroundColor Cyan
    Write-Host "║ 🎼 UNIFIED SCRIPT ORCHESTRATOR - Sandbox/Bash (177 Scripts)              ║" -ForegroundColor Cyan
    Write-Host $('╚' + '═'*78 + '╝') -ForegroundColor Cyan
    
    Initialize-Logging
    Discover-Scripts
    
    Write-Host "`n📋 Mode: $Mode" -ForegroundColor Cyan
    Write-Host "🔧 DryRun: $($Config.DryRun)" -ForegroundColor Cyan
    
    switch ($Mode) {
        'auto' {
            Write-Log -Message "Starting auto-run pipeline..." -Level INFO
            Run-AutoPipeline | Out-Null
        }
        
        'interactive' {
            Write-Log -Message "Starting interactive mode..." -Level INFO
            Run-Interactive
        }
        
        'validate' {
            Write-Log -Message "Starting validation..." -Level INFO
            Run-Validate
        }
        
        'discover' {
            Write-Log -Message "Discovering scripts..." -Level INFO
            Run-Discover
            return
        }
    }
    
    Show-Report
    Write-Log -Message "Orchestrator completed" -Level SUCCESS
}

# ─────────────────────────────────────────────────────────────────────────────
# EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

try {
    Invoke-Orchestrator
    exit 0
} catch {
    Write-Log -Message "Fatal error: $($_.Exception.Message)" -Level ERROR
    Write-Error $_
    exit 1
}
