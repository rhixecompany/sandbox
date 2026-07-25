# Fix Crlf Frontmatter

## Overview

This skill wraps a Python script in `~/AppData/Local/hermes/scripts/fix_crlf_frontmatter.py`.

## Script Purpose

The `fix_crlf_frontmatter.py` script automates fix crlf frontmatter operations within the Hermes ecosystem.

## Usage

```bash
python $LOCALAPPDATA/hermes/scripts/fix_crlf_frontmatter.py [options]
```

## Common Options

- `--help`: Display usage information
- `--dry-run`: Preview changes without applying them
- `--verbose`: Detailed output for debugging

## Examples

```bash
# Run with default settings
python $LOCALAPPDATA/hermes/scripts/fix_crlf_frontmatter.py

# Preview changes
python $LOCALAPPDATA/hermes/scripts/fix_crlf_frontmatter.py --dry-run
```