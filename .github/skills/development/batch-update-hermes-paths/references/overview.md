# batch_update_hermes_paths.py — Overview

## Purpose
Batch updates Hermes path references across skills, configurations, and prompt files. When Hermes paths change (e.g., due to installation location changes, profile switches, or platform moves), this script scans and updates all references to the old path pattern to the new one.

## Usage

```bash
python batch_update_hermes_paths.py [--dir PATH] [--old-old TEXT] [--new TEXT] [--dry-run] [--confirm] [--file-types TYPES] [--report FILE]
```

### Options

| Option        | Description                                                    |
|--------------|----------------------------------------------------------------|
| `--dir`      | Root directory to scan for files needing path updates          |
| `--old`      | The old path string to replace (default: auto-detected)        |
| `--new`      | The new path string to use                                     |
| `--dry-run`  | Show what files would change without modifying them            |
| `--confirm`  | Ask for confirmation before each file change                   |
| `--file-types` | Comma-separated file extensions to include (default: `md,py,yaml,json,toml`) |
| `--safe`     | Only apply changes to files where paths are clearly references |

## Behavior

- Scans recursively for all matching file types in the target directory.
- Searches for occurrences of the old path pattern (e.g., `C:/Users/OldUser/AppData/Local/hermes`).
- Replaces with the new path while preserving path structure.
- For each file, performs a backup before modification.
- Tracks the number of replacements per file and total.
- In safe mode, skips files where the path appears in ambiguous context (e.g., inside code strings vs. documentation).

## Example

**Dry run to see what would change:**
```bash
python batch_update_hermes_paths.py --dir $LOCALAPPDATA/hermes/skills --old "C:/OldPath" --new "C:/NewPath" --dry-run
```

**Update all paths interactively with confirmation:**
```bash
python batch_update_hermes_paths.py --dir $LOCALAPPDATA/hermes --new "D:/hermes_v2" --confirm
```

**Safe one-shot update of markdown files only:**
```bash
python batch_update_hermes_paths.py --dir ./docs --new "$LOCALAPPDATA/hermes" --file-types "*.md" --safe
```

## Dependencies

- Python 3.7+
- No external dependencies

## See Also

- Hermes installation path documentation
- `hermes config` commands for path configuration