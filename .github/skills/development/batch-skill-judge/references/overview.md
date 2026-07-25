# batch_skill_judge.py — Overview

## Purpose
Batch evaluation and scoring of Hermes skills using a predefined quality rubric. This script processes multiple skills at once, scores them across multiple dimensions (frontmatter, structure, content, DRY, references), and generates aggregate reports to identify skills needing improvement.

## Usage

```bash
python batch_skill_judge.py [--dir PATH] [--output FORMAT] [--report FILE] [--threshold N] [--parallel] [--verbose] [--rules PATH]
```

### Options

| Option        | Description                                                    |
|--------------|----------------------------------------------------------------|
| `--dir`      | Directory containing skills to evaluate                        |
| `--output`   | Output format: `terminal`, `json`, `markdown`, `csv`          |
| `--report`   | Save the full scoring report to a file                         |
| `--threshold` | Only show skills below this score (useful for triage)         |
| `--parallel` | Evaluate multiple skills in parallel                           |
| `--verbose`  | Show per-category breakdown for each skill                    |
| `--rules`    | Path to custom scoring rules YAML file                        |

## Behavior

- Iterates over all SKILL.md files in the target directory tree.
- For each skill, evaluates 5 scoring dimensions:
  - **FM (Frontmatter, 0–20):** Presence and validity of YAML frontmatter with required fields.
  - **Struct (Structure, 0–20):** Presence of required sections (Overview, Workflow, Verification, Pitfalls).
  - **Content (Content, 0–25):** Non-generic, substantive descriptions and meaningful content.
  - **DRY (DRY, 0–20):** Avoids boilerplate, uses references instead of inline duplication.
  - **Refs (References, 0–15):** Existence and quality of reference files (references/, templates/, scripts/).
- Aggregates scores into a composite total (max 100).
- Can publish scores in structured formats for downstream tools (batch-remediate, batch-rewrite-worst).

## Example

**Full evaluation of all development skills:**
```bash
python batch_skill_judge.py --dir $LOCALAPPDATA/hermes/skills/development
```

**Find skills below 80 and save report:**
```bash
python batch_skill_judge.py --dir $LOCALAPPDATA/hermes/skills --threshold 80 --output json --report needs_work.json
```

**Parallel evaluation with verbose scores:**
```bash
python batch_skill_judge.py --dir $LOCALAPPDATA/hermes/skills --parallel --verbose
```

## Dependencies

- Python 3.8+
- `pyyaml` (for frontmatter parsing)
- May require `ruamel.yaml` for frontmatter preservation

## See Also

- `skill-judge` — single-skill evaluation
- `batch-remediate` — fixing skills based on judge output