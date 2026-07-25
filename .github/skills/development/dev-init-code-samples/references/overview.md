# Dev Init Code Samples

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/dev_init_code_samples.py`.

## Script Purpose

The `dev_init_code_samples.py` script automates dev init code samples operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/dev_init_code_samples.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/dev_init_code_samples.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/dev_init_code_samples.py --dry-run
```