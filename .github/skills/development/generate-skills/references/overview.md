# generate_skills.py — Overview

## Purpose
Generates new Hermes skill scaffolding from templates or specifications. This script creates fully-structured SKILL.md files with proper YAML frontmatter, standardized sections, and optional companion files (references/, templates/, scripts/), reducing friction in the skill creation process.

## Usage

```bash
python generate_skills.py [--name NAME] [--title TITLE] [--description DESC] [--tags TAGS] [--template NAME] [--output DIR] [--force] [--with-refs] [--with-scripts] [--list-templates]
```

### Options

| Option           | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `--name`        | Skill name (lowercase, hyphen-separated, e.g., `my-new-skill`) |
| `--title`       | Human-readable title                                           |
| `--description` | One-line description of the skill                              |
| `--tags`        | Comma-separated tags (e.g., `python,configuration,hooks`)      |
| `--template`    | Template to use (use `--list-templates` to see available)      |
| `--output`      | Output directory (default: current working directory)          |
| `--force`       | Overwrite existing skill directory if it exists                |
| `--with-refs`   | Create references/ subdirectory                                |
| `--with-scripts` | Create scripts/ subdirectory                                  |
| `--list-templates` | Show available templates and exit                            |

## Behavior

- Provides ready-to-use templates: `python-script`, `node-script`, `powershell-script`, `generic`, and `example`.
- Generates a complete SKILL.md with valid YAML frontmatter (name, title, description, version=1.0.0, author, license=MIT, tags).
- Optional companion subdirectories: `references/`, `templates/`, `scripts/`.
- Automatically sanitizes skill names (lowercase, replaces spaces with hyphens).
- Creates the skill directory with all requested files in one pass.
- Does NOT register the skill with Hermes — use `hermes skills install` after generation.

## Example

**List available templates:**
```bash
python generate_skills.py --list-templates
```

**Create a Python script skill:**
```bash
python generate_skills.py --name my-automation --title "My Automation" --description "Automates daily reports" --tags python,automation,reports --template python-script --with-refs
```

**Create a skill with scripts and references:**
```bash
python generate_skills.py --name data-analyzer --title "Data Analyzer" --output $LOCALAPPDATA/hermes/skills/development --with-refs --with-scripts --force
```

## Dependencies

- Python 3.7+
- `pyyaml` (for frontmatter generation)

## See Also

- `hermes skills install` — install a generated skill
- Skill quality scoring guide