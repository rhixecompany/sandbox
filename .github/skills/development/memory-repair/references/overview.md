# memory_repair.py — Overview

## Purpose

Repairs, validates, and manages Hermes memory files for user profiles. This script checks memory files (`USER.md`, `MEMORY.md`, `SOUL.md`) for structural integrity, content freshness, and completeness — restoring or rebuilding them when corruption or staleness is detected.

## Usage

```bash
python memory_repair.py [--profile NAME] [--all-profiles] [--check-only] [--backup] [--dry-run] [--rebuild] [--report FILE] [--verbose]
```

### Options

| Option          | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--profile`    | Target a specific profile name (default: current profile)       |
| `--all-profiles` | Check/repair all profiles                                   |
| `--check`      | Check memory files for issues without making changes           |
| `--fix`        | Apply fixes to detected issues                                 |
| `--backup`     | Create timestamped backups before modifying                 |
| `--dry-run`    | Show what would be repaired without making changes            |
| `--rebuild`    | Rebuild a missing/corrupt memory file from available context   |
| `--report`     | Save the repair report to a file                               |
| `--verbose`    | Detailed logging of each check and repair action               |

## Behavior

- Locates profile memory files at `~/AppData/Local/hermes/profiles/<profile>/`.
- Validates: file existence, YAML frontmatter (if present), minimum content length, and cross-references between memory files.
- Detects issues: missing files, empty files, stale content (last modified > 30 days), broken YAML, missing required tags.
- With `--fix`, applies repairs: creates missing files from templates, patches broken YAML, adds missing fields.
- With `--rebuild`, reconstructs memory files using available session data and profile metadata.
- Generates a report showing each profile's status and any actions taken.

## Example

**Check the current profile's memory:**
```bash
python memory_repair.py --check
```

**Repair all profiles with backup:**
```bash
python memory_repair.py --all-profiles --fix --backup
```

**Dry run on a specific profile:**
```bash
python memory_repair.py --profile work --dry-run --check
```

## Dependencies

- Python 3.7+
- `pyyaml` (for frontmatter parsing)

## See Also

- Hermes memory documentation: USER.md, MEMORY.md, SOUL.md
- Profile management commands (`hermes profiles`)