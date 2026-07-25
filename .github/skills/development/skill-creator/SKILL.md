---
name: skill-creator
title: Skill Creator
description: "Use when authoring, scaffolding, and validating in-repo SKILL.md files and skill assets."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [skills, authoring, scaffolding, validation]
metadata:
  hermes:
    tags: [skills, authoring, validation]
    related_skills: [writing-skills, skill-judge]
---

# Skill Creator

## Overview

Use this skill when authoring, scaffolding, validating, or improving in-repo skills. It covers skill lifecycle planning, structure, validation, and optional optimization.

## When to Use

- Creating a new skill from scratch
- Improving or editing an existing skill
- Running validation on a skill
- Benchmarking or comparing skill variants
- Publishing or packaging skill updates
- Reviewing prior art before adding a new skill

## When NOT to Use

- Using existing skills for regular tasks
- Non-skill document changes
- Operations that do not require skill lifecycle changes
- Editing prompt libraries or template artifacts outside skill scope

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-skills` | Create clear skill prose and structure |
| `skill-judge` | Audit skills against quality criteria |

## Workflow

### Phase 1: Plan

1. Identify purpose and triggers.
2. Define acceptance criteria and intended use cases.
3. Plan structure: frontmatter, sections, references, templates, validation.
4. Validate against similar existing skills.

### Phase 2: Scaffold

1. Create `SKILL.md` with validated frontmatter.
2. Add required sections.
3. Add supporting files in `references/`, `templates/`, and `scripts/` where needed.

### Phase 3: Validate

1. Review behavior and intended outputs.
2. Run lightweight validation or checks.
3. Fix frontmatter, section ordering, and referenced paths.
4. Normalize style and markdown structure.

### Phase 4: Optimize If Needed

1. Improve `description` for discoverability.
2. Remove redundancy and improve clarity.
3. Benchmark if evaluation is required.
4. Revise if metrics or feedback indicate gaps.

## Outputs

- Valid scaffolded skill files
- Confirmed working frontmatter and section structure
- Updated references or templates

## Verification Checklist

- [ ] Skill has clear purpose, use cases, and structured workflow
- [ ] Frontmatter is complete and valid
- [ ] Files are created in expected locations
- [ ] Behavior matches intended use cases
- [ ] Quality bar matches related skills

## Pitfalls

- Avoid duplicate skills when similar prior art exists.
- Do not embed unchanged template boilerplate without adapting it to the skill.
- Avoid partial scaffolding and leaving the skill unreviewed.
- **Over-250-line DRY penalty:** Skills >250 lines lose DRY points (max 10/20 instead of 20/20). Move detailed content to `references/<topic>.md` and keep SKILL.md as a compact core (workflow + one-line pointers to references).
- **Missing structure sections:** Skills without Skills Required table, Pitfalls, Verification Checklist, or ≥3 workflow phases lose Structure points (max 16/20).
- **Missing reference files:** Skills without `references/overview.md` + `templates/template.md` lose Refs points (max 7/20). Create both with substantive content.
- **Insufficient content depth:** Skills scoring 60-79 typically have adequate structure but lack concrete examples, code blocks, and domain-specific reference files. Add usage examples and reference files to push ≥80.
- **Template-in-skill-body anti-pattern:** Embedding large parameterized templates directly in SKILL.md instead of `templates/` or `references/` scores poorly on DRY and Structure. Move templates out; keep SKILL.md under 250 lines.
- **YAML frontmatter format:** Tags must be inline array (`tags: [a, b]`) or YAML list (each on new line with `-`). Mixed formats break parsers.
- **Batch audit calibration:** When judging many skills, calibrate on first batch then lock thresholds. The TSV output format (`skill_name|path|score|rating|dim1|dim2|dim3|dim4|dim5|lines`) is useful for cross-skill queries.
- **Windows path handling in scripts:** Use `pathlib.Path` with `os.path.expanduser("~/AppData/Local/hermes")` for cross-backend compatibility.
- **Over-250-line DRY penalty:** Skills >250 lines lose DRY points (max 10/20 instead of 20/20). Move detailed content to `references/<topic>.md` and keep SKILL.md as a compact core (workflow + one-line pointers to references).
- **Missing structure sections:** Skills without Skills Required table, Pitfalls, Verification Checklist, or ≥3 workflow phases lose Structure points (max 16/20).
- **Missing reference files:** Skills without `references/overview.md` + `templates/template.md` lose Refs points (max 7/20). Create both with substantive content.
- **Insufficient content depth:** Skills scoring 60-79 typically have adequate structure but lack concrete examples, code blocks, and domain-specific reference files. Add usage examples and reference files to push ≥80.
- **Template-in-skill-body anti-pattern:** Embedding large parameterized templates directly in SKILL.md instead of `templates/` or `references/` scores poorly on DRY and Structure. Move templates out; keep SKILL.md under 250 lines.
- **YAML frontmatter format:** Tags must be inline array (`tags: [a, b]`) or YAML list (each on new line with `-`). Mixed formats break parsers.
- **Batch audit calibration:** When judging many skills, calibrate on first batch then lock thresholds. The TSV output format (`skill_name|path|score|rating|dim1|dim2|dim3|dim4|dim5|lines`) is useful for cross-skill queries.
- **Windows path handling in scripts:** Use `pathlib.Path` with `os.path.expanduser("~/AppData/Local/hermes")` for cross-backend compatibility.
