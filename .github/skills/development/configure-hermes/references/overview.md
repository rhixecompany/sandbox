# Configure Hermes

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/configure_hermes.py`.

## Script Purpose

The `configure_hermes.py` script automates configure hermes operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/configure_hermes.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/configure_hermes.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/configure_hermes.py --dry-run
```