---
name: apply-vscode-customizations
title: Apply VSCode Customizations
description: Applies custom VS Code configuration settings and extensions
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - vscode
  - customization
  - config
---

# Apply VSCode Customizations

## Overview

Wrapper skill for the `apply_vscode_customizations.py` script in `~/AppData/Local/hermes/scripts/`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/apply_vscode_customizations.py`

**Usage:**
```bash
python apply_vscode_customizations.py [options]
```

## When to Use

- When setting up VS Code customizations for a new Hermes environment
- When syncing VS Code settings from a template or config

## When NOT to Use

- When manually configuring VS Code settings one-by-one
- When VS Code is not installed

## Workflow

### Phase 1: Setup
Ensure VS Code is installed and current settings are backed up.

### Phase 2: Customize
Run the script with the desired customization profile or arguments.

### Phase 3: Verify
Open VS Code and confirm settings are applied correctly.

## Verification Checklist

- [ ] Script completes without errors
- [ ] Settings.json is updated with expected values
- [ ] Extensions are installed
- [ ] Old settings are backed up
- [ ] VS Code restarts cleanly

## Pitfalls
- May overwrite existing settings if not careful with merge behavior
- Some extensions may require VS Code restart