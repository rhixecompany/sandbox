# Boost Near Pass Refs

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/boost_near_pass_refs.py`.

## Script Purpose

The `boost_near_pass_refs.py` script automates boost near pass refs operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/boost_near_pass_refs.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/boost_near_pass_refs.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/boost_near_pass_refs.py --dry-run
```