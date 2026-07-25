---
name: fix-prompts-comprehensive
title: Fix Prompts Comprehensive
description: Fixes prompts comprehensive issues across files
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - python
  - remediation
  - prompts
  - scripts
---

# Fix Prompts Comprehensive

## Overview

Wrapper skill for the `fix_prompts_comprehensive.py` script in `~/AppData/Local/hermes/scripts/`.

The script is located at `~/AppData/Local/hermes/scripts/fix_prompts_comprehensive.py`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/fix_prompts_comprehensive.py`

**Type:** Python

**Usage:**
```bash
python fix_prompts_comprehensive.py [options]
```

Run from the scripts directory or use the full path:
```bash
cd ~/AppData/Local/hermes/scripts && python fix_prompts_comprehensive.py [options]
```

## When to Use

- When you need to perform fix prompts comprehensive as part of your workflow
- When automating batch operations that involve this script
- When you need the specific functionality this script provides

## When NOT to Use

- When you are looking for a more general-purpose tool for the same task
- When the environment does not support Python execution
- When the specific task is better handled by Hermes built-in commands

## Workflow

### Phase 1: Setup
Ensure the Hermes scripts directory is accessible and all dependencies for this script are installed. Verify the script exists at the expected path. For Python scripts, check that required packages are installed. For PowerShell scripts, ensure execution policy permits running scripts.

### Phase 2: Run
Execute the script with the appropriate arguments. Review any usage/help output if needed by passing `--help` or no arguments.

### Phase 3: Verify
Check the script output for correctness. Verify any files that were modified or created. Confirm the script completed with exit code 0.

## Verification Checklist

- [ ] Script executes without errors (exit code 0)
- [ ] Output matches expected format
- [ ] Any file changes are as anticipated
- [ ] Script arguments work as documented
- [ ] No unintended side effects were introduced
- [ ] Help/usage text displays correctly
- [ ] Exit codes are handled appropriately

## Pitfalls

- Always run Python scripts from within a virtual environment to avoid dependency conflicts
- PowerShell scripts on Windows may be blocked by execution policy (`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)
- Node.js scripts may require `npm install` for dependencies before running
- Some scripts modify files in-place; always back up before running
- The script path must be absolute or run from the scripts directory
