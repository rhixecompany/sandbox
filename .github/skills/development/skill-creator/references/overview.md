# Skill Creator

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/skill_creator.py`.

## Script Purpose

The `skill_creator.py` script automates skill creator operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/skill_creator.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/skill_creator.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/skill_creator.py --dry-run
```