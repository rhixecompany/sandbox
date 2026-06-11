---
title: Bash Toolkit — Documentation Root
description: Cross-platform system maintenance utilities for Windows: dependency cleanup, package upgrades, cache cleanup, and disk analysis.
status: active
tags: [bash, powershell, windows, maintenance, toolkit, documentation]
updated: 2026-05-27
---

     1|# Windows System Maintenance Toolkit
     2|
     3|Cross-platform system maintenance utilities for Windows providing dependency cleanup and package upgrade capabilities across multiple package managers (winget, chocolatey).
     4|
     5|## Features
     6|
     7|- **Dependency Cleanup** — Scans and removes 50+ dependency folder types (node_modules, venv, **pycache**, .next, .gradle, build outputs, etc.)
     8|- **Package Upgrades** — Updates packages via winget and chocolatey with colored output and detailed logging
     9|- **Cache Cleanup** — Cleans 14 cache types (winget, docker, npm, pnpm, bun, git-lfs, opencode, vscode, temp, etc.)
    10|- **Disk Analysis** — Analyzes disk usage with dependency breakdown and cleanup estimates
    11|- **Cross-Platform** — Available as Bash, PowerShell, and Batch scripts for maximum compatibility
    12|- **Performance** — Parallel scanning and fast deletion using robocopy and runspaces
    13|- **Safety** — Interactive confirmation, what-if mode, verification scans, and comprehensive logging
    14|
    15|## Quick Start
    16|
    17|### Prerequisites
    18|
    19|- **For Bash scripts**: Git Bash, WSL, or MSYS2
    20|- **For PowerShell scripts**: PowerShell 5.1+
    21|- **Package managers** (optional): winget or chocolatey
    22|
    23|### Installation
    24|
    25|```bash
    26|git clone <repository-url>
    27|cd Bash
    28|chmod +x upgrade.sh clean_dependency_folders.sh
    29|```
    30|
    31|### Basic Usage
    32|
    33|```bash
    34|# Upgrade all packages
    35|.\upgrade.ps1          # PowerShell (recommended)
    36|bash upgrade.sh        # Bash
    37|upgrade.bat            # Batch
    38|.\upgrade-native.ps1   # Native PowerShell
    39|
    40|# Cleanup dependencies
    41|.\clean-dependency-folders.ps1   # PowerShell (recommended)
    42|./clean_dependency_folders.sh   # Bash
    43|clean-dependency-folders.bat     # Batch
    44|```
    45|
    46|### Common Options
    47|
    48|```bash
    49|# Cleanup: auto-confirm, preview, custom paths/targets, fast delete
    50|.\clean-dependency-folders.ps1 -Auto -WhatIf -Fast
    51|.\clean-dependency-folders.ps1 -Paths "C:\Projects" -Targets "node_modules","venv"
    52|
    53|# Upgrade: debug, skip package managers
    54|.\upgrade.ps1 -DebugMode -SkipChoco
    55|```
    56|
    57|## Cache Cleanup
    58|
    59|Clean package manager and application caches:
    60|
    61|```bash
    62|# PowerShell (recommended)
    63|.\cache-clean.ps1 -AllCaches
    64|.\cache-clean.ps1 -Caches "docker,npm,temp" -DryRun
    65|
    66|# Bash
    67|./cache-clean.sh --all-caches
    68|./cache-clean.sh --caches docker,npm,temp --dry-run
    69|
    70|# Batch
    71|cache-clean.bat ALL
    72|cache-clean.bat DRYRUN CACHES "docker,npm,temp"
    73|```
    74|
    75|## Disk Analysis
    76|
    77|Analyze disk usage before cleanup:
    78|
    79|```bash
    80|.\disk-analysis.ps1
    81|.\disk-analysis.ps1 -Paths "C:\Projects" -OutputFile report.txt
    82|```
    83|
    84|## Requirements
    85|
    86|| Requirement | Version        | Purpose                    |
    87|| ----------- | -------------- | -------------------------- |
    88|| PowerShell  | 5.1+           | Running .ps1 scripts       |
    89|| Bash        | 4+             | Running .sh scripts        |
    90|| winget      | Latest         | Windows Package Manager    |
    91|| chocolatey  | Latest         | Package Manager (optional) |
    92|| robocopy    | Windows Vista+ | Fast folder deletion       |
    93|
    94|## Documentation
    95|
    96|- [Architecture](ARCHITECTURE.md) — System design, components, and full project structure
    97|- [Code Style](CODE_STYLE.md) — Coding conventions and supported dependency types
    98|
    99|## Troubleshooting

100| 101|- **"No bash interpreter found"**: Install Git for Windows, WSL, or MSYS2 102|- **"Access denied"**: Run PowerShell as Administrator 103|- **Remaining folders after cleanup**: Close locking processes and re-run 104|
