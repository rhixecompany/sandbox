---
name: add-hooks-to-config
title: Add Hooks to Config
description: Adds lifecycle hooks to Hermes configuration files
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - hermes
  - hooks
  - config
---

# Add Hooks to Config

## Overview

Wrapper skill for the `add_hooks_to_config.py` script in `~/AppData/Local/hermes/scripts/`.

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/add_hooks_to_config.py`

**Usage:**
```bash
python add_hooks_to_config.py [options]
```

## When to Use

- When you need to register lifecycle hooks into Hermes configuration
- After installing new hooks that require config registration

## When NOT to Use

- When hooks are already configured and registered
- For inspecting existing hooks without modification

## Workflow

### Phase 1: Setup
Ensure Hermes is installed and config files are accessible.

### Phase 2: Execute
Run the script with the appropriate arguments to add hooks.

### Phase 3: Verify
Check that hooks appear in the config and test one hook lifecycle.

## Verification Checklist

- [ ] Script completes without errors
- [ ] Hooks are added to the relevant config files
- [ ] Hook lifecycle fires as expected
- [ ] No duplicate hook entries exist
- [ ] Original config backup is preserved

## Pitfalls
- Running the script multiple times may create duplicate entries
- Ensure Hermes is not actively running during config modification