# batch_remediate_42_59.py — Overview

## Purpose
Targeted batch remediation script focused on skills with quality scores in the 42–59 range. This script identifies skills that scored below the passing threshold and applies a focused set of automatic fixes to bring them up to minimum quality standards — adding frontmatter, fixing structure, and patching missing content.

## Usage

```bash
python batch_remediate_42_59.py [--dir PATH] [--dry-run] [--report FILE] [--score-file PATH] [--parallel] [--limit N]
```

### Options

| Option         | Description                                                    |
|---------------|----------------------------------------------------------------|
| `--dir`       | Directory containing skills to assess and remediate            |
| `--dry-run`   | Show what would be remediated without making changes          |
| `--report`    | Save remediation report to a file                              |
| `--score-file` | Path to a JSON file of pre-computed scores                     |
| `--parallel`  | Process multiple skills in parallel for faster execution       |
| `--limit`     | Maximum number of skills to process                            |

## Behavior

- Scans all skills in the target directory and checks each for a quality score
- Filters skills scoring between 42 and 59 (inclusive).
- Applies targeted fixes: missing YAML frontmatter, empty sections, broken formatting, and structural issues.
- Prioritizes fixes that provide the most point gain (e.g., adding frontmatter = +15 points).
- Reports before/after scores when a score-file is provided.
- When `--parallel` is set, uses multiprocessing to remediate multiple skills simultaneously.

## Example

**Dry run on all development skills:**
```bash
python batch_remediate_42_59.py --dir $LOCALAPPDATA/hermes/skills/development --dry-run
```

**Remediate with score tracking:**
```bash
python batch_remediate_42_59.py --dir $LOCALAPPDATA/hermes/skills/development --score-file scores.json --report remediation.json
```

**Parallel remediation for speed:**
```bash
python batch_remediate_42_59.py --dir $LOCALAPPDATA/hermes/skills/development --parallel --limit 10
```

## Dependencies

- Python 3.8+
- `pyyaml` (for frontmatter parsing)

## See Also

- `batch-remediate` — full batch remediation across all scores
- `batch-skill-judge` — companion scoring tool