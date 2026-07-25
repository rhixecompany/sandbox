# Create Missing Souls

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/create_missing_souls.py`.

## Script Purpose

The `create_missing_souls.py` script automates create missing souls operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/create_missing_souls.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/create_missing_souls.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/create_missing_souls.py --dry-run
```