---
author: Hermes Agent
description: Audit and fix VS Code workspace configurations (.vscode/settings.json, launch.json, tasks.json, extensions.json) for ESLint mismatches, hardcoded paths, missing extensions, and stack mismatches. Generates corrected configs and audit reports.
license: MIT
metadata:
  hermes:
    related_skills:
    - vscode-workspace-configurator
    - vscode-ext-commands
    tags:
    - vscode
    - audit
    - configuration
    - eslint
    - workspace
name: vscode-config-audit
tags:
- vscode
- audit
- configuration
- eslint
- workspace
- ide
title: VS Code Config Audit
version: 1.0.0
---

# VS Code Config Audit

## Overview

Audit VS Code workspace configurations for common issues: ESLint code actions without extension, hardcoded absolute paths, missing recommended extensions, formatter conflicts, and tech stack mismatches.

## When to Use

- Onboarding new projects
- CI/CD workspace validation
- Debugging IDE integration issues
- Periodic workspace hygiene

## When NOT to Use

- For generating configs from scratch (use `vscode-workspace-configurator`)
- For extension management (use `vscode-ext-commands`)

## Audit Categories

| Category | Checks |
|----------|--------|
| **ESLint** | Code actions without `dbaeumer.vscode-eslint` extension |
| **Paths** | Hardcoded `C:\Users\...`, `/home/...`, `$HOME` without expansion |
| **Extensions** | Missing recommended extensions for detected stack |
| **Formatters** | Multiple formatters for same language, missing format-on-save |
| **Tasks** | Shell commands with hardcoded paths, missing problem matchers |
| **Launch** | Debug configs with absolute paths, missing env vars |

## Workflow

### Phase 1: Run Audit

```bash
python $LOCALAPPDATA/hermes/scripts/audit_vscode_config.py \
  --workspace . \
  --output docs/vscode-audit-report.md
```

### Phase 2: Review & Fix

```bash
# Auto-fix common issues
python $LOCALAPPDATA/hermes/scripts/audit_vscode_config.py \
  --workspace . --fix --backup

# Generate corrected configs
python $LOCALAPPDATA/hermes/scripts/generate_vscode_configs.py \
  --workspace . --output .vscode/
```

### Phase 3: Verify

```bash
# Re-audit
python $LOCALAPPDATA/hermes/scripts/audit_vscode_config.py --workspace .
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/`

| Script | Purpose |
|--------|---------|
| `audit_vscode_config.py` | Core audit engine |
| `generate_vscode_configs.py` | Generate corrected configs |
| `validate_vscode_json.py` | JSON syntax + schema validation |
| `validate_vscode_configs.py` | Full config validation |

## Report Output

- **Markdown:** Human-readable with issue table, file list, fix suggestions
- **JSON:** Machine-readable for CI/CD
- **Summary:** Issue counts by category/severity

## Common Fixes

| Issue | Auto-fix | Manual Fix |
|-------|----------|------------|
| ESLint action no extension | ✓ Add `dbaeumer.vscode-eslint` | |
| Hardcoded Windows path | ✓ Replace with `${workspaceFolder}` | |
| Missing format-on-save | ✓ Add `editor.formatOnSave: true` | |
| Missing recommended extensions | ✓ Add to `extensions.json` | |
| Multiple formatters | | Keep one primary |

## Related Skills

- `vscode-workspace-configurator` — Generate configs from scratch
- `vscode-ext-commands` — Manage extensions