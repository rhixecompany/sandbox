# batch_rewrite_worst.py — Overview

## Purpose
Identifies and rewrites the worst-performing skills based on quality scores. This script analyzes skills that score below a defined threshold and uses an LLM or template system to regenerate better versions of their SKILL.md files while preserving the core purpose and metadata.

## Usage

```bash
python batch_rewrite_worst.py [--dir PATH] [--threshold N] [--score-file PATH] [--template PATH] [--limit N] [--dry-run] [--report FILE] [--model NAME]
```

### Options

| Option         | Description                                                    |
|---------------|----------------------------------------------------------------|
| `--dir`       | Directory containing skills to evaluate and rewrite           |
| `--threshold` | Scores below this value will be rewritten (default: 60)      |
| `--score-file` | Path to pre-computed scores JSON file                         |
| `--template`  | Path to a markdown template for the new SKILL.md content      |
| `--limit`     | Maximum number of skills to rewrite (default: 5)              |
| `--dry-run`   | Show which skills would be rewritten without doing it          |
| `--report`    | Save rewrite log to a file                                    |
| `--model`     | LLM model to use for content generation                       |

## Behavior

- Reads quality scores for all skills from a JSON file or compute them on the fly.
- Filters skills below the specified threshold.
- For each selected skill: reads the existing SKILL.md, determines its purpose from the description and frontmatter, and generates a new SKILL.md using a template.
- Preserves the original frontmatter (name, title, description, version, author, license, tags).
- Rewrites the body with proper sections: Overview, When to Use, Workflow, Verification, Pitfalls.
- Backs up the original file as `SKILL.md.bak` before overwriting.
- Logs each rewrite with skill name, old score, and status.

## Example

**Dry run to identify skills below threshold:**
```bash
python batch_rewrite_worst.py --dir $LOCALAPPDATA/hermes/skills --score-file scores.json --threshold 65 --dry-run
```

**Rewrite the 3 worst skills:**
```bash
python batch_rewrite_worst.py --dir $LOCALAPPDATA/hermes/skills/development --score-file scores.json --limit 3
```

**Rewrite with a custom template:**
```bash
python batch_rewrite_worst.py --dir ./skills --score-file scores.json --template my_template.md
```

## Dependencies

- Python 3.8+
- `pyyaml` (for frontmatter parsing)
- `openai` or compatible API client if using LLM mode

## See Also

- `batch-remediate` — lighter-weight fix approach
- `batch-remediate-42-59` — focused on the 42–59 range