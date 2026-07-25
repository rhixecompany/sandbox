# Create Missing Memories

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/create_missing_memories.py`.

## Script Purpose

The `create_missing_memories.py` script automates create missing memories operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/create_missing_memories.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/create_missing_memories.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/create_missing_memories.py --dry-run
```