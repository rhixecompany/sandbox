# Fix Prompts

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/fix_prompts.py`.

## Script Purpose

The `fix_prompts.py` script automates fix prompts operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/fix_prompts.py --dry-run
```