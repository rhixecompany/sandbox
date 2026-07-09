---
title: Code Style Guide — Bash Toolkit
description: Naming conventions, file organization, and coding standards for Bash, PowerShell, and TypeScript scripts.
status: active
tags: [style-guide, conventions, bash, powershell, typescript]
updated: 2026-05-27
---

     1|# Code Style
     2|
     3|## Naming Conventions
     4|
     5|### Files
     6|
     7|- **Scripts**: lowercase with hyphens (`clean_dependency_folders.sh`, `upgrade.ps1`)
     8|- **Logs**: descriptive with timestamp (`upgrade_20260509_165745.log`)
     9|- **Directories**: lowercase (`logs/`, `thoughts/`)
    10|
    11|### Variables (Bash)
    12|
    13|- Uppercase with underscores: `LOG_DIR`, `TARGETS`, `AUTO_CONFIRM`
    14|- Local functions: lowercase with underscores: `folder_size()`, `build_expr()`
    15|
    16|### Variables (PowerShell)
    17|
    18|- PascalCase: `$ScriptDir`, `$LogFile`, `$DebugMode`
    19|- Functions: PascalCase: `Initialize-Logging`, `Invoke-BashScript`
    20|
    21|## File Organization
    22|
    23|### Bash Scripts
    24|
    25|1. Shebang (`#!/usr/bin/env bash`)
    26|2. Description/comment block
    27|3. Configuration (defaults)
    28|4. Color codes
    29|5. Functions (logging, helpers, core logic)
    30|6. Argument parsing
    31|7. Main execution
    32|
    33|### PowerShell Scripts
    34|
    35|1. Comment-based metadata
    36|2. `param()` block
    37|3. Configuration
    38|4. Hashtable for colors
    39|5. Functions
    40|6. Main execution block
    41|
    42|### Cache Cleanup Scripts (`cache-clean.*`)
    43|
    44|- Follow the same structure as core scripts above
    45|- Define cache types in a central hashtable/array
    46|- Support `-DryRun`/`--dry-run` for safe preview
    47|- Confirm before destructive operations (unless `-Auto`/`--auto`)
    48|- Version: `1.0.0`
    49|
    50|### Disk Analysis Scripts (`disk-analysis.ps1`)
    51|
    52|- Read-only operations only (no deletions)
    53|- Output formatted tables for readability
    54|- Support `-OutputFile` for report generation
    55|- Version: `1.0.0`
    56|
    57|## Code Patterns
    58|
    59|### Bash Function Template
    60|
    61|```bash
    62|function_name() {
    63|    local arg1="$1"
    64|    local result
    65|    # ... logic ...
    66|    echo "$result"
    67|}
    68|```
    69|
    70|### PowerShell Function Template
    71|
    72|```powershell
    73|function Invoke-Something {
    74|    param(
    75|        [string]$Input,
    76|        [switch]$Force
    77|    )
    78|    # ... logic ...
    79|}
    80|```
    81|
    82|### Color Output (Bash)
    83|
    84|```bash
    85|RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
    86|echo -e "${GREEN}Success${NC}"
    87|```
    88|
    89|### Color Output (PowerShell)
    90|
    91|```powershell
    92|$Colors = @{ Red = "`e[0;31m"; Green = "`e[0;32m" }
    93|Write-Host "$($Colors['Green'])Success$($Colors['NC'])"
    94|```
    95|
    96|## Error Handling
    97|
    98|### Bash
    99|

100|- `set -uo pipefail` at script start 101|- Check exit codes: `[[ $? -eq 0 ]]` 102|- Use traps: `trap cleanup EXIT` 103| 104|### PowerShell 105| 106|- Try/catch blocks for critical operations 107|- Check `$LASTEXITCODE` after external commands 108|- Return boolean for success/failure 109| 110|## Logging 111| 112|### Log Format 113| 114|`    115|[timestamp] [LEVEL] message    116|` 117| 118|### Log Levels 119| 120|- `ERROR` - Failures 121|- `WARN` - Warnings 122|- `INFO` - General info 123|- `SUCCESS` - Positive outcomes 124|- `SECTION` - Section headers 125|- `DEBUG` - Debug messages (when enabled) 126| 127|## Testing 128| 129|- Use `--what-if` flag to preview without executing 130|- Check logs in `./logs/` directory 131|- Verify with `verify_cleanup.ps1` after deletions 132| 133|## Do's and Don'ts 134| 135|### Do 136| 137|- Use descriptive variable names 138|- Add comments for complex logic 139|- Log all operations 140|- Handle errors gracefully 141|- Support `--help` flag 142| 143|### Don't 144| 145|- Hardcode paths (use variables) 146|- Delete without confirmation (unless `--auto-confirm`) 147|- Ignore exit codes 148|- Mix Bash and PowerShell syntax in same file 149|
