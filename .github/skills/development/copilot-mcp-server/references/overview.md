# Copilot Mcp Server

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/copilot_mcp_server.py`.

## Script Purpose

The `copilot_mcp_server.py` script automates copilot mcp server operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/copilot_mcp_server.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/copilot_mcp_server.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/copilot_mcp_server.py --dry-run
```