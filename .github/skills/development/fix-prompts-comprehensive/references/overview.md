# Fix Prompts Comprehensive

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/fix_prompts_comprehensive.py`.

## Script Purpose

The `fix_prompts_comprehensive.py` script automates fix prompts comprehensive operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/fix_prompts_comprehensive.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/fix_prompts_comprehensive.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/fix_prompts_comprehensive.py --dry-run
```