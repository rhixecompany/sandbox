# add_hooks_to_config.py — Overview

## Purpose
Adds configuration hooks to the Hermes Agent setup. This script reads the existing Hermes configuration file (`config.yaml`) and injects hook definitions — pre-command, post-command, session-start, and session-end hooks — enabling custom automation at various lifecycle stages of the agent.

## Usage

```bash
python add_hooks_to_config.py [--config PATH] [--hooks PATH] [--dry-run] [--backup]
```

### Options

| Option       | Description                                                      |
|-------------|------------------------------------------------------------------|
| `--config`  | Path to the Hermes config.yaml file (default: auto-detected)     |
| `--hooks`   | Path to a YAML file defining hooks to add                        |
| `--dry-run` | Show what would be changed without modifying the file            |
| `--backup`  | Create a backup of the existing config before modifying it       |

## Behavior

- Parses the existing config to locate the `hooks:` section (or creates one if absent).
- Merges the provided hook definitions without duplicating existing entries.
- Validates hook syntax: each hook must specify a `command`, `type`, and optional `description`.
- When `--backup` is set, the original config is saved as `config.yaml.bak` with a timestamp.
- Exits with code 0 on success, 1 on validation errors, 2 on file-not-found.

## Examples

**Add default hooks:**
```bash
python add_hooks_to_config.py --hooks my_hooks.yaml
```

**Preview changes before applying:**
```bash
python add_hooks_to_config.py --hooks my_hooks.yaml --dry-run
```

**Use a non-default config path with backup:**
```bash
python add_hooks_to_config.py --config ~/.hermes/custom_config.yaml --backup
```

## Dependencies

- Python 3.7+
- PyYAML (`pip install pyyaml`)

## See Also

- `hermes config` command
- Hook lifecycle documentation at ~/AppData/Local/hermes/docs/