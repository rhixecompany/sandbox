# inventory_prompts.py — Overview

## Purpose
Creates a structured inventory of all prompt files within the Hermes workspace. This script scans directories for prompt files, extracts their metadata (name, description, tags, version), and generates a catalog report that can be used for quality tracking, deduplication, and organization.

## Usage

```bash
python inventory_prompts.py [--dir PATH] [--output FORMAT] [--report FILE] [--include FILE_TYPES] [--recursive] [--stats] [--deduplicate] [--tags]
```

### Options

| Option          | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--dir`        | Directory to scan (default: current directory)                  |
| `--output`     | Output format: `table`, `json`, `markdown`, `csv`            |
| `--report`     | Save the inventory to a file                                  |
| `--include`    | Comma-separated file extensions to include (default: `md,prompts,txt`) |
| `--recursive`  | Recursively scan subdirectories (default: enabled)            |
| `--stats`      | Show summary statistics (counts, missing fields, duplicates) |
| `--deduplicate` | Identify prompts with duplicate names or descriptions       |
| `--verbose`    | List all fields per prompt in the report                      |

## Behavior

- Recursively finds all prompt files in the target directory tree.
- For each file, attempts to parse the YAML frontmatter and extract: `name`, `title`, `description`, `version`, `author`, `tags`, `category`.
- Files without frontmatter are still included in the inventory with "unknown" field values.
- Generates a catalog with: file path, name, title, version, tags, and last-modified date.
- With `--stats`, provides aggregate data: total prompts, prompts with/without frontmatter, average version, top tags.
- With `--deduplicate`, flags prompts that share the same name or very similar descriptions.

## Example

**Inventory all prompts in the skills directory:**
```bash
python inventory_prompts.py --dir $LOCALAPPDATA/hermes/skills
```

**Generate a CSV report for spreadsheet analysis:**
```bash
python inventory_prompts.py --dir $LOCALAPPDATA/hermes/skills --output csv --report prompt_inventory.csv
```

**Find duplicates with stats:**
```bash
python inventory_prompts.py --dir ./prompts --deduplicate --stats --output markdown
```

## Dependencies

- Python 3.7+
- `pyyaml` (for frontmatter parsing)

## See Also

- `audit-prompts` — audit prompt quality
- Prompt file specification documentation