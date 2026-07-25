# Consolidate Skills

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/consolidate_skills.py`.

## Script Purpose

The `consolidate_skills.py` script automates consolidate skills operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/consolidate_skills.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/consolidate_skills.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/consolidate_skills.py --dry-run
```