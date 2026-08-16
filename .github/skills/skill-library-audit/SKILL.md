---
author: Hermes Agent
description: Generate comprehensive skill library audit report. Runs skill-judge on all skills, categorizes by domain, identifies gaps/duplicates/outdated skills, and produces executive summary with remediation priorities.
category: qa
license: MIT
metadata:
  hermes:
    related_skills:
    - skill-judge
    - skills
    - batch-skills-audit
    - batch-skills-remediation
    tags:
    - skills
    - audit
    - report
    - quality
    - library
name: skill-library-audit
tags:
- skills
- audit
- report
- quality
- library
- governance
title: Skill Library Audit
version: 1.0.0
---
# Skill Library Audit

## Overview

Comprehensive audit of entire Hermes skill library. Runs skill-judge across all skills, categorizes by domain, identifies gaps, duplicates, and outdated skills, and produces executive summary with remediation priorities.

## When to Use

- Quarterly skill library health check
- Before major Hermes upgrades
- Onboarding new skill maintainers
- Governance/compliance reporting

## Audit Dimensions

| Dimension | Checks |
|-----------|--------|
| **Coverage** | Domain coverage map, gap analysis |
| **Quality** | skill-judge scores, distribution |
| **Deduplication** | Similar titles, overlapping scopes |
| **Currency** | Last updated, deprecated patterns |
| **Structure** | Frontmatter completeness, reference validity |

## Workflow

### Phase 1: Full Audit

```bash
python $LOCALAPPDATA/hermes/scripts/audit_skills_judge.py \
  --skills-dir $LOCALAPPDATA/hermes/skills \
  --output docs/skill-library-audit.md \
  --json docs/skill-library-audit.json
```

### Phase 2: Gap Analysis

### Phase 2.5: Cross-Reference Analysis (Orphan Detection)

Determine which skills are actually referenced by prompts or other skills vs. which are unreferenced orphans safe to delete.

```bash
python3 -c "
import os, glob, yaml

skills_root = os.path.expanduser('~/AppData/Local/hermes/skills')
prompts_dir = './prompts'

on_disk = {os.path.basename(r) for r,_,f in os.walk(skills_root) if 'SKILL.md' in f}

refs_from_prompts = set()
for fp in glob.glob(os.path.join(prompts_dir, '*.prompt.md')):
    with open(fp) as f:
        try:
            parts = f.read().split('---', 2)
            fm = yaml.safe_load(parts[1]) if len(parts) >= 3 else {}
        except: fm = {}
    for s in (fm.get('skills') or []): refs_from_prompts.add(s)

refs_from_skills = set()
for r,_,f in os.walk(skills_root):
    if any(x in r for x in ('.archive', '.restore-backups')): continue
    if 'SKILL.md' not in f: continue
    fp = os.path.join(r, 'SKILL.md')
    with open(fp, encoding='utf-8', errors='ignore') as fh:
        try:
            parts = fh.read().split('---', 2)
            fm = yaml.safe_load(parts[1]) if len(parts) >= 3 else {}
        except: fm = {}
    for s in (fm.get('skills') or []): refs_from_skills.add(s)
    for s in (fm.get('related_skills') or []): refs_from_skills.add(s)

all_refs = refs_from_prompts | refs_from_skills
orphans = on_disk - all_refs
print(f'Skills: {len(on_disk)} | Referenced: {len(all_refs)} | Orphans: {len(orphans)}')
for o in sorted(orphans): print(f'  UNUSED: {o}')
"
```

**Interpretation:** Skill referenced by 0 prompts AND 0 other skills = orphan safe to delete. Skip `.archive`/`.restore-backups.DISABLED` dirs.
python $LOCALAPPDATA/hermes/scripts/audit_skills_judge.py \
  --skills-dir $LOCALAPPDATA/hermes/skills \
  --gap-analysis \
  --output docs/skill-gaps.md
```

### Phase 3: Remediation Plan

```bash
python $LOCALAPPDATA/hermes/scripts/audit_skills_judge.py \
  --skills-dir $LOCALAPPDATA/hermes/skills \
  --remediation-plan docs/skill-remediation-plan.md
```

## Script Reference

**Location:** `~/AppData/Local/hermes/scripts/audit_skills_judge.py`

**Options:**
| Flag | Description |
|------|-------------|
| `--skills-dir` | Skills root directory |
| `--output` | Report output path |
| `--json` | JSON output for CI |
| `--gap-analysis` | Domain gap analysis |
| `--remediation-plan` | Generate prioritized fix list |
| `--threshold` | Quality threshold (default: 70) |

## Report Sections

1. **Executive Summary** — Overall score, counts, trend
2. **Domain Coverage** — Skills per category, gaps
3. **Quality Distribution** — Score histogram, pass/fail
4. **Duplicates** — Similar skills, merge candidates
5. **Outdated** — Skills needing updates
6. **Remediation Priority** — Ranked fix list


## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Related Skills

- `skill-judge` — Single skill evaluation
- `batch-skills-audit` — Batch quality pipeline
- `batch-skills-remediation` — Auto-fix pipeline
- `skills` — Skill management CLI

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Skill Library Audit operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
