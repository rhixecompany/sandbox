# fix-skills.py — Overview

## Purpose
Automated skill repair utility that fixes common structural and content issues in Hermes SKILL.md files. Handles problems like missing frontmatter, broken YAML syntax, empty sections, formatting irregularities, and missing required fields — restoring skills to a valid baseline without rewriting content.

## Usage

```bash
python fix-skills.py [--dir PATH] [--skill NAME] [--fix TYPE] [--dry-run] [--backup] [--report FILE] [--verbose]
```

### Options

| Option        | Description                                                    |
|--------------|----------------------------------------------------------------|
| `--dir`      | Directory containing skill files to fix                         |
| `--skill`    | Fix a single named skill (omit to fix all in directory)         |
| `--fix`      | Comma-separated types of fixes: `frontmatter`, `formatting`, `structure`, `all` (default: `all`) |
| `--dry-run`  | Show what would be fixed without modifying                     |
| `--backup`   | Create a `.bak` backup of each file before modifying              |
| `--report`   | Save fix report to a file                                      |
| `--verbose`   | Show detailed logs per fix operation                           |

## Behavior

- Parses each SKILL.md and validates YAML frontmatter completeness.
- Checks for required frontmatter fields: `name`, `title`, `description`, `version`, `author`, `license`, `tags`.
- Validates section structure: Overview, When to Use, Workflow, Verification, Pitfalls.
- Fixes common formatting: trailing whitespace, inconsistent heading spacing, missing blank lines after frontmatter.
- Reports files that require manual intervention (content-level issues it can't auto-fix).
- Preserves original content as much as possible — only adds missing structural elements.

## Example

**Fix all skills in the development directory:**
```bash
python fix-skills.py --dir $LOCALAPPDATA/hermes/skills/development
```

**Dry run on a single skill:**
```bash
python fix-skills.py --skill add-hooks-to-config --dry-run
```

**Only fix frontmatter, with backup:**
```bash
python fix-skills.py --dir $LOCALAPPDATA/hermes/skills --fix frontmatter --backup
```

## Dependencies

- Python 3.8+
- `pyyaml` (for frontmatter parsing/validation)
- `ruamel.yaml` (optional, for YAML formatting preservation)

## See Also

- `batch-remediate` — broader batch issues remediation
- Skill quality scoring documentation