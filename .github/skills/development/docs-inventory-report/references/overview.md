# Docs Inventory Report

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/docs_inventory_report.py`.

## Script Purpose

The `docs_inventory_report.py` script automates docs inventory report operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/docs_inventory_report.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/docs_inventory_report.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/docs_inventory_report.py --dry-run
```