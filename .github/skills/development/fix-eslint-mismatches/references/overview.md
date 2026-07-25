# Fix Eslint Mismatches

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/fix_eslint_mismatches.py`.

## Script Purpose

The `fix_eslint_mismatches.py` script automates fix eslint mismatches operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/fix_eslint_mismatches.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/fix_eslint_mismatches.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/fix_eslint_mismatches.py --dry-run
```