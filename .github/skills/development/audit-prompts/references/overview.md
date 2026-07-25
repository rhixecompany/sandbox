# audit_prompts.py — Overview

## Purpose
Audits prompt files for quality issues, formatting consistency, structural completeness, and content guidelines compliance. This script scans markdown prompt files across the Hermes project and identifies problems such as missing frontmatter, broken YAML, missing required sections, overly long lines, and adherence to prompt-writing conventions.

## Usage

```bash
python audit_prompts.py [--dir PATH] [--output FORMAT] [--report FILE] [--fix] [--severity LEVEL] [--rules FILE]
```

### Options

| Option        | Description                                                     |
|--------------|-----------------------------------------------------------------|
| `--dir`       | Directory containing prompt files to audit                    |
| `--output`    | Output format: `terminal`, `json`, `markdown` (default: `terminal`) |
| `--report`    | Save the full audit report to a file                              |
| `--fix`       | Attempt to auto-fix certain issues (missing frontmatter, whitespace) |
| `--severity`  | Minimum severity level to report: `error`, `warning`, `info`  |
| `--rules`     | Path to a custom rules YAML file                                 |

## Behavior

- Recursively finds all `.md` and `.prompt` files in the target directory.
- Checks each file for valid YAML frontmatter with required fields (`name`, `description`, `version`).
- Validates section structure against the prompt template specification.
- Flags issues: missing/empty sections, inconsistent heading levels, code blocks without language, trailing whitespace, lines >120 chars.
- Supports fix mode for common issues (adds missing frontmatter templates, normalizes whitespace).
- Produces a severity-categorized summary suitable for CI.

## Example

**Audit all prompts in the Hermes workspace:**
```bash
python audit_prompts.py --dir $LOCALAPPDATA/hermes/skills
```

**Generate a JSON report for CI consumption:**
```bash
python audit_prompts.py --dir ./prompts --output json --report audit_results.json
```

**Audit with auto-fix of minor issues:**
```bash
python audit_prompts.py --dir ./prompts --fix
```

## Dependencies

- Python 3.7+
- `pyyaml` (for frontmatter parsing)

## See Also

- Hermes prompt writing guidelines
- YAML frontmatter specification: https://jekyllrb.com/docs/front-matter/