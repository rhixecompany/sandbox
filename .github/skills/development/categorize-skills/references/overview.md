# Categorize Skills

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/categorize_skills.py`.

## Script Purpose

The `categorize_skills.py` script automates categorize skills operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/categorize_skills.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/categorize_skills.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/categorize_skills.py --dry-run
```