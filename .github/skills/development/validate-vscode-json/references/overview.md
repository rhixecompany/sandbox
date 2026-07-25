# Validate Vscode Json

## Overview

This skill provides a wrapper for the `validate_vscode_json script in `~/AppData/Local/hermes/scripts/`.

## Script Purpose

The script walks entire SandBox workspace validating .vscode JSON files within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/validate_vscode_json.py [options]

# For Node.js/CJS scripts
node $LOCALAPPDATA/hermes/scripts/validate_vscode_json.cjs [options]
```

## Common Options

| Option | Description |
|--------|-------------|
| `--help` | Display usage information |
| `--dry-run` | Preview changes without applying |
| `--verbose` | Detailed debug output |

## Typical Workflow

1. **Setup** — Ensure the target files exist and are accessible
2. **Preview** — Run with `--dry-run` first
3. **Execute** — Apply changes with production mode
4. **Verify** — Confirm expected output

## Related Skills

- Located in `development/` category with similar utility skills