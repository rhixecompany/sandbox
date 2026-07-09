---
title: Architecture — Bash Toolkit
description: System architecture, tech stack, directory structure, and core component overview for the Windows system maintenance toolkit.
status: active
tags: [architecture, bash, powershell, windows, maintenance]
updated: 2026-05-27
---

     1|# Architecture
     2|
     3|## Overview
     4|
     5|Windows system maintenance utility providing dependency cleanup and package upgrade capabilities across multiple package managers (winget, chocolatey).
     6|
     7|## Tech Stack
     8|
     9|- **Languages**: Bash, PowerShell, Batch
    10|- **Target Platform**: Windows (with WSL/Git Bash support)
    11|- **Package Managers**: winget, chocolatey
    12|
    13|## Directory Structure
    14|
    15|```
    16|Bash/
    17|├── clean_dependency_folders.sh    # Core cleanup (Bash)
    18|├── clean-dependency-folders.ps1   # Core cleanup (PowerShell)
    19|├── clean-dependency-folders.bat   # Core cleanup (Batch)
    20|├── upgrade.sh                    # Package upgrade (Bash)
    21|├── upgrade.ps1                   # PowerShell wrapper for upgrade.sh
    22|├── upgrade.bat                   # Batch wrapper for upgrade.sh
    23|├── upgrade-native.ps1            # Native PowerShell upgrade
    24|├── cache-clean.ps1               # Cache cleaner (PowerShell)
    25|├── cache-clean.sh                # Cache cleaner (Bash)
    26|├── cache-clean.bat               # Cache cleaner (Batch)
    27|├── disk-analysis.ps1             # Disk space analysis
    28|├── verify_cleanup.ps1            # Verification script
    29|├── logs/                         # Execution logs
    30|└── thoughts/                     # Session notes
    31|```
    32|
    33|## Core Components
    34|
    35|### 1. Dependency Cleanup (`clean_dependency_folders.sh`)
    36|
    37|- Scans 50+ dependency folder types (node_modules, venv, .venv, **pycache**, bin, obj, etc.)
    38|- Supports parallel scanning and fast deletion
    39|- Configurable paths, targets, and max depth
    40|- Modes: interactive, auto-confirm, what-if
    41|
    42|### 2. Package Upgrade (`upgrade.sh`)
    43|
    44|- Updates packages via winget and chocolatey
    45|- Colored output with detailed logging
    46|- Error handling with summary reports
    47|- Configurable skip options
    48|
    49|### 3. PowerShell Wrappers
    50|
    51|- Execute bash scripts on Windows
    52|- Detect available bash interpreters (WSL, Git Bash, MSYS2)
    53|- Preserve colored output
    54|
    55|### 4. Cache Cleanup (`cache-clean.ps1`)
    56|
    57|- Cleans 14 cache types: winget, choco, docker, npm, pnpm, bun, git-lfs, opencode, vscode, temp, windows-update, dns, thumbnails, wer
    58|- Supports dry-run, auto, and selective cache modes
    59|- Safety confirmations for destructive operations
    60|
    61|### 5. Disk Analysis (`disk-analysis.ps1`)
    62|
    63|- Drive overview with total/free/used space
    64|- Top 10 largest dependency folders
    65|- Category breakdown by ecosystem
    66|- Estimated cleanup savings
    67|
    68|## Data Flow
    69|
    70|```
    71|User Execution
    72|    ├── upgrade.ps1 (PowerShell)
    73|    │   └── upgrade.sh (Bash via WSL/Git Bash)
    74|    │       ├── winget update/upgrade
    75|    │       └── chocolatey upgrade
    76|    │
    77|    ├── clean-dependency-folders.ps1
    78|    │   └── clean_dependency_folders.sh
    79|    │       ├── Scan directories (find)
    80|    │       ├── Calculate sizes (du)
    81|    │       └── Delete folders (rm -rf)
    82|    │
    83|    ├── cache-clean.ps1 (PowerShell)
    84|    │   ├── cache-clean.sh (Bash)
    85|    │   └── cache-clean.bat (Batch)
    86|    │       ├── Detect cache types
    87|    │       ├── Calculate sizes
    88|    │       └── Clean selected caches
    89|    │
    90|    └── disk-analysis.ps1
    91|        ├── Scan drive usage
    92|        ├── Analyze dependency folders
    93|        └── Generate cleanup report
    94|```
    95|
    96|## Configuration
    97|
    98|- Default scan paths: configurable via `SCAN_PATHS` env var, fallback to `$HOME/Desktop/SandBox`, `/e/Development`, `/c/Projects`
    99|- Log directory: `./logs`

100|- Max recursion depth: 10 101| 102|## Build & Deploy 103| 104|No build required. Scripts are directly executable: 105| 106|- Bash: `bash upgrade.sh` or `./upgrade.sh` 107|- PowerShell: `.\upgrade.ps1` 108|- Batch: `.\upgrade.bat` 109|
