---
author: Hermes Agent
description: Batch skill quality audit pipeline. Runs skill-judge on all local skills, generates aggregate report with scores, identifies failing skills, and optionally runs auto-remediation.
license: MIT
metadata:
  hermes:
    related_skills:
    - skill-judge
    - skill-creator
    - skills
    - batch-skills-remediation
    tags:
    - skills
    - audit
    - batch
    - quality
    - pipeline
name: batch-skills-audit
tags:
- skills
- audit
- batch
- quality
- pipeline
- remediation
title: Batch Skills Audit
version: 1.0.0
---

# Batch Skills Audit

## Overview

Run skill-judge on all local Hermes skills in parallel, aggregate results, identify skills below quality threshold, and optionally trigger remediation pipeline.

## When to Use

- Periodic skill library health checks
- Before Hermes upgrades
- CI/CD nightly quality gate
- After bulk skill operations

## When NOT to Use

- Single skill validation (use `skill-judge`)
- Creating new skills (use `skill-creator`)

## Workflow

### Phase 1: Full Audit

```bash
python $LOCALAPPDATA/hermes/scripts/batch_skill_judge.py \
  --workspace $LOCALAPPDATA/hermes/skills \
  --output docs/skill-audit-report.md \
  --json docs/skill-audit-report.json
```

### Phase 2: Remediation

```bash
# Auto-fix common issues
python $LOCALAPPDATA/hermes/scripts/batch_remediate.py \
  --input docs/skill-audit-report.json \
  --threshold 70

# Or run full remediation pipeline
python $LOCALAPPDATA/hermes/scripts/batch_skills_remediation.py \
  --audit-report docs/skill-audit-report.json
```

### Phase 3: Re-audit

```bash
python $LOCALAPPDATA/hermes/scripts/batch_skill_judge.py \
  --workspace $LOCALAPPDATA/hermes/skills \
  --threshold 80
```

## Script Reference

| Script | Purpose |
|--------|---------|
| `batch_skill_judge.py` | Parallel skill-judge execution |
| `batch_remediate.py` | Auto-fix common issues |
| `batch_skills_remediation.py` | Full remediation pipeline |
| `aggregate_benchmark.py` | Cross-skill benchmark aggregation |

## Output

- **Markdown report:** Per-skill scores, dimension breakdown, failure reasons
- **JSON report:** Machine-readable for CI/CD
- **Summary:** Pass/fail counts, avg score, top issues

## CI Integration

```yaml
- name: Audit Skills
  run: |
    python ~/AppData/Local/hermes/scripts/batch_skill_judge.py \
      --workspace ~/AppData/Local/hermes/skills \
      --threshold 75 \
      --fail-on-below-threshold \
      --output-json skill-audit.json
```

## Related Skills

- `skill-judge` — Single skill evaluation
- `skill-creator` — Author new skills
- `batch-skills-remediation` — Auto-fix pipeline