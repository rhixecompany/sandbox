# batch_delete_profiles.py — Overview

## Purpose
Batch deletes Hermes agent profiles based on filtering criteria. This script processes all profiles under the Hermes profiles directory and removes those matching specified conditions — by name pattern, age (last used), size, or status flags. Includes safety features like dry-run and confirmation prompts.

## Usage

```bash
python batch_delete_profiles.py [--pattern PATTERN] [--older-than DAYS] [--force] [--dry-run] [--keep N] [--exclude NAMES]
```

### Options

| Option          | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--pattern`    | Glob or regex pattern to match profile names for deletion      |
| `--older-than` | Delete profiles not used in more than N days                   |
| `--force`      | Skip confirmation prompts (non-interactive mode)               |
| `--dry-run`    | Show which profiles would be deleted without actually deleting |
| `--keep`       | Keep the N most recent profiles, delete the rest               |
| `--exclude`    | Comma-separated profile names to exclude from deletion         |

## Behavior

- Scans the Hermes profiles directory (`~/AppData/Local/hermes/profiles/`) for all profile folders.
- Applies all specified filters (AND logic) to determine the target set.
- For each matched profile: deletes the entire profile directory (config files, memories, skills).
- When not in `--force` mode, lists profiles and asks for confirmation before deletion.
- Logs deleted profiles to stdout with timestamps.
- Never deletes the "default" profile unless explicitly matched by `--pattern`.

## Example

**Dry run to see what would be deleted:**
```bash
python batch_delete_profiles.py --older-than 90 --dry-run
```

**Delete all profiles matching a pattern, keeping 3 most recent:**
```bash
python batch_delete_profiles.py --pattern "test-*" --keep 3 --force
```

**Delete unused profiles older than 30 days:**
```bash
python batch_delete_profiles.py --older-than 30
```

## Dependencies

- Python 3.7+
- No external dependencies

## See Also

- Hermes profile management
- `batch-update-hermes-paths` skill