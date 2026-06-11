---
name: script-orchestration
title: "Script Orchestration — Unified Multi-Script Management"
description: "Build unified orchestrators for large script repositories: auto-discovery, category-based execution, error handling, structured logging. Consolidates scattered scripts into single intelligent entry point with auto-run plus interactive fallback."
author: Alexa
date: 2026-05-27
keywords:
  - orchestration
  - script-management
  - auto-discovery
  - multi-language-scripts
  - error-handling
  - json-logging
  - powershell
references:
  - references/orchestrator-real-world.md
  - references/error-handling-patterns.md
templates:
  - templates/orchestrator-template.ps1
scripts:
  - scripts/discovery-validator.ps1
---
## Goal
Build unified orchestrators for large script repositories: auto-discovery, category-based execution, error handling, structured logging. Consolidates scattered scripts into single intelligent entry point with auto-run plus interactive fallback.


# Script Orchestration — Unified Multi-Script Management

When you have 50+ scripts scattered across directories, build a unified orchestrator to:
- Auto-discover all scripts (by language, directory, pattern)
- Organize into categories with priority ordering
- Default: auto-run core pipeline; fallback: interactive menu
- Robust error handling (retry, timeout, logging)
- Structured JSON logging for metrics and errors

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## When to Use This Pattern

YES: 50+ scripts across multiple directories  
YES: Mixed languages (PowerShell, shell, batch, TypeScript)  
YES: Sequential execution with error recovery needed  
YES: Progress visibility and detailed logging required  
YES: Support both automated (CI/cron) and manual (interactive) execution  

NO: Single script or monolithic tool  
NO: Scripts that must run in parallel  

## Core Pattern

### 1. Architecture: Auto-Discovery and Categorization

Define categories with paths and priorities:

```powershell
$Categories = @{
    'Core' = @{
        Description = 'Production pipeline'
        Paths       = @('src', 'scripts', '.')
        Priority    = 1
        Scripts     = @()
    }
}
```

Discover recursively, excluding junk paths:

```powershell
function Discover-Scripts {
    foreach ($catName in $Categories.Keys | Sort-Object { $Categories[$_].Priority }) {
        $cat = $Categories[$catName]
        $scripts = @()
        
        foreach ($path in $cat.Paths) {
            $searchPath = if ($path -eq '.') { Get-Location } else { Join-Path (Get-Location) $path }
            if (Test-Path $searchPath) {
                $found = Get-ChildItem -Path $searchPath -Recurse -Include '*.sh','*.ps1','*.bat','*.ts' `
                    -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\node_modules|__pycache__|\.git' }
                $scripts += $found
            }
        }
        
        $cat.Scripts = $scripts | Select-Object -Unique
    }
}
```

Key decisions:
- Paths support relative, absolute, and '.' for current directory
- Exclude build artifacts: node_modules, __pycache__, .git, .venv, dist, build
- Directory structure is single source of truth for categorization

### 2. Execution: Auto-Run Pipeline and Interactive Fallback

Auto-run executes predefined sequence:

```powershell
$AutoRunPipeline = @(
    @{ Category = 'Core'; Pattern = 'disk-analysis'; Description = 'Analyze disk' }
    @{ Category = 'Core'; Pattern = 'cache-clean'; Description = 'Clean caches' }
    @{ Category = 'Core'; Pattern = 'upgrade'; Description = 'Upgrade packages' }
)
```

Interactive falls back to menu-driven selection:

```powershell
function Run-Interactive {
    do {
        $catChoice = Show-CategoryMenu
        if ($catChoice -eq '0') { break }
        
        $selectedCat = Get-CategoryByChoice $catChoice
        $script = Show-ScriptMenu -Category $selectedCat
        
        if ($script) {
            Invoke-Script -ScriptFile $script
        }
    } while ($true)
}
```

Both modes feed same executor (Invoke-Script).

### 3. Error Handling: Retry, Timeout, and Logging

Implement retry with exponential backoff:

```powershell
function Invoke-Script {
    param([System.IO.FileInfo]$ScriptFile, [int]$Index)
    
    $scriptName = $ScriptFile.Name
    $ext = $ScriptFile.Extension
    $retryCount = 0
    
    do {
        try {
            switch ($ext) {
                '.ps1' { & pwsh -NoProfile -ExecutionPolicy Bypass -File $ScriptFile.FullName 2>&1 }
                '.sh'  { bash -n $ScriptFile.FullName 2>&1 }
                '.bat' { & cmd /c $ScriptFile.FullName 2>&1 }
                '.ts'  { bunx tsx $ScriptFile.FullName 2>&1 }
            }
            $Metrics.SuccessCount++
            return $true
            
        } catch {
            $retryCount++
            if ($retryCount -lt $Config.MaxRetries) {
                Start-Sleep -Seconds 2
            } else {
                Write-Error-Log -ScriptName $scriptName -ErrorMessage $_.Exception.Message
                $Metrics.FailureCount++
                return $false
            }
        }
    } while ($retryCount -lt $Config.MaxRetries)
}
```

Retry strategy:
- 3 attempts by default (configurable via $Config.MaxRetries)
- 2-second delay between attempts (exponential backoff)
- Failed scripts do not halt pipeline; log and continue
- Each error logged with timestamp, script name, and message

### 4. Structured Logging: JSON Error and Metrics

Initialize logs with timestamps:

```powershell
function Initialize-Logging {
    @{ StartTime = Get-Date -Format o; Errors = @() } | ConvertTo-Json | Set-Content $ErrorLogFile
}
```

Append errors to log file:

```powershell
function Write-Error-Log {
    param([string]$ScriptName, [string]$ErrorMessage)
    
    $error_obj = @{
        Timestamp = Get-Date -Format o
        Script    = $ScriptName
        Error     = $ErrorMessage
        ExitCode  = $LASTEXITCODE
    }
    
    $log = Get-Content $ErrorLogFile | ConvertFrom-Json
    $log.Errors += $error_obj
    $log | ConvertTo-Json | Set-Content $ErrorLogFile
}
```

Log structure:
- One timestamped file per run (yyyyMMdd-HHmmss format)
- JSON format (jq-compatible for analysis)
- Error entries: timestamp, script name, message, exit code
- Metrics entries: per-script execution times, success/failure counts

### 5. Modes: Auto, Interactive, Discover, Validate

Expose all modes via parameter:

```powershell
param([ValidateSet('auto', 'interactive', 'discover', 'validate')][string]$Mode = 'auto')

switch ($Mode) {
    'auto'        { Run-AutoPipeline }
    'interactive' { Run-Interactive }
    'discover'    { Show-AllScripts; exit 0 }
    'validate'    { Run-Validate }
}
```

## Pitfalls

### Pitfall 1: Infinite retries on permission errors
Exit code 5 (Windows permission denied) will not improve on retry. Detect and fail fast.

Fix: Check exit code before retry.

### Pitfall 2: Discovery includes build artifacts
Recursive discovery without exclusions will find files in node_modules, dist, __pycache__, etc.

Fix: Build comprehensive exclude pattern list.

### Pitfall 3: Timeout not enforced in subprocess
Spawned PowerShell/shell scripts do not auto-interrupt when they hang.

Fix: Use Start-Process with WaitForExit timeout and Kill() on timeout.

### Pitfall 4: Logging directory grows unbounded
Without rotation, logs accumulate indefinitely.

Fix: Implement monthly cleanup or archival.

### Pitfall 5: Undefined category execution order
If categories have identical priorities, sort order is undefined.

Fix: Use unique priorities and explicit sort by priority.

## Customization

**Add new category:**
```powershell
$Categories['NewCat'] = @{
    Description = 'Description'
    Paths       = @('path/to/scripts')
    Priority    = 7
}
```

**Change retry count and timeout:**
```powershell
$Config.MaxRetries = 5
$Config.TimeoutSeconds = 600
```

**Modify auto-run pipeline:**
```powershell
$AutoRunPipeline = @(
    @{ Category = 'Core'; Pattern = 'custom-task'; Description = 'Custom task' }
)
```

## Testing

1. Discover all scripts: `.\orchestrator.ps1 -Mode discover`
2. Dry-run (preview): `.\orchestrator.ps1 -DryRun`
3. Validate shell syntax: `.\orchestrator.ps1 -Mode validate`
4. Inspect error logs: `cat logs/errors-*.json | jq '.Errors'`
5. Inspect metrics: `cat logs/metrics-*.json | jq '.ScriptExecTime'`

## Integration Examples

GitHub Actions:
```yaml
- run: pwsh -NoProfile -ExecutionPolicy Bypass -File orchestrator.ps1 -Mode auto
```

Windows Task Scheduler (daily at 2 AM):
```powershell
$action = New-ScheduledTaskAction -Execute pwsh -Argument "-NoProfile -ExecutionPolicy Bypass -File orchestrator.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At 2:00AM
Register-ScheduledTask -TaskName "Daily Orchestrator" -Action $action -Trigger $trigger
```

Linux Cron (daily at 2 AM):
```
0 2 * * * /path/to/orchestrator.sh -m auto >> /var/log/orchestrator.log 2>&1
```

## Real-World Example

Sandbox/Bash project (2026-05-27):
- Consolidated 180 scripts across 11 directories
- 6 categories: Core (64), Banking (34), Archive (51), Comicwise (10), Bash (7), Utilities (13)
- Auto-run pipeline: disk analysis → cache cleanup → dependency cleanup → package upgrade → tests
- Typical execution: 20-60 seconds
- Error logs: timestamped JSON with script names and messages
- Success rate: all 5 core tasks passed on first execution

See references/orchestrator-real-world.md for detailed implementation and production metrics.


