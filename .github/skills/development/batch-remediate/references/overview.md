# batch_remediate.py — Overview

## Purpose
Batch remediation tool for fixing common issues across skills, prompts, and configurations in the Hermes environment. This script scans multiple skills and applies programmatic fixes to known problem patterns — such as missing YAML frontmatter, broken section structures, inconsistent formatting, and stale content.

## Usage

```bash
python batch_remediate.py [--dir PATH] [--rules PATH] [--fix TYPE] [--dry-run] [--report FILE] [--limit N] [--verbose]
```

### Options

| Option      | Description                                                    |
|------------|----------------------------------------------------------------|
| `--dir`    | Directory containing skills or files to remediate              |
| `--rules`  | Path to remediation rules YAML file                            |
| `--fix`     | Specific fix type(s) to apply (comma-separated)              |
| `--dry-run` | Show what would be fixed without making changes               |
| `--report` | Save remediation report to a file                              |
| `--limit`  | Max number of files to process (useful for testing)            |
| `--verbose` | Detailed logging of each remediation action                   |

## Behavior

- Recursively discovers SKILL.md, prompt files, and markdown documents in the target directory.
- Matches each file against a ruleset — either built-in rules or a custom rules file.
- Available fix categories: `frontmatter` (missing YAML), `formatting` (whitespace, headings), `references` (stale file paths), `templates` (missing boilerplate).
- Applies fixes in order: structural issues first, then formatting, then content.
- Generates a summary report: how many files scanned, issues found, fixes applied, and any failures.
- Non-destructive by default (only `--dry-run` shows changes without writing).

## Example

**Dry run to see what would be fixed:**
```bash
python batch_remediate.py --dir $LOCALAPPDATA/hermes/skills/development --dry-run
```

**Apply only frontmatter fixes with a report:**
```bash
python batch_remediate.py --dir ./skills --fix frontmatter --report remediate.json
```

**Full remediation with custom rules:**
```bash
python batch_remediate.py --dir ./skills --rules my_remediation_rules.yaml --fix frontmatter,structure,formatting
```

## Dependencies

- Python 3.8+
- `pyyaml` (for rules parsing)

## See Also

- `batch-remediate-42-59` — targeted remediation for specific skill ranges
- `batch-skill-judge` — batch evaluation companion tool