---
trigger: /comprehensive-prompt-enhancer
name: comprehensive-prompt-enhancer
title: Comprehensive Prompt Library Enhancer
description: 'Enhances and updates all prompts at ./.github/prompts/*.prompt.md using DRY principle, best practices, and all appropriate structural sections: personas, profiles, personalities, steps, rules, goals, phases, tasks, subtasks, subgoals, checklists, skills, MCP servers, tools, templates, plans, prompts, toolsets. Ensures each prompt and all its files are verified, validated.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
- web
- delegation
scripts:
- .enhance/comprehensive_enhance.py
- .enhance/analyze_prompts.py
- .enhance/fix_prompt_artifacts.py
- .enhance/fix_fence_glue.py
skills:
- using-superpowers
- subagent-driven-development
- brainstorming
- prompt-engineering-patterns
- prompt-management
- skill-judge
dependencies:
- skill:using-superpowers
- skill:subagent-driven-development
- skill:brainstorming
- skill:prompt-engineering-patterns
- skill:prompt-management
- skill:skill-judge
tags:
- hermes
- prompts
- enhancement
- library
- DRY
- workflow
metadata:
  hermes:
    tags:
    - prompts
    - enhancement
    - library
formatter: default
plan: ''
---
## Goal

Enhance and update all prompts at `./.github/prompts/*.prompt.md` using the DRY principle, prompt engineering best practices, and all appropriate structural sections — personas, profiles, personalities, steps, rules, goals, phases, tasks, subtasks, subgoals, checklists, skills, MCP servers, tools, templates, plans, prompts, toolsets. Ensure each prompt and all its files are verified, validated, and have zero issues remaining.

## Subgoals

1. **Audit** — Scan all prompts for structural gaps, YAML validity, DRY compliance, and missing sections.
2. **Enhance** — Add missing sections using shared templates from `templates/_shared/` without inlining duplicate content.
3. **Validate** — Verify every prompt has valid YAML frontmatter, all referenced files exist, and the enhancement script is idempotent.
4. **Verify** — Run full analysis, confirm zero issues, zero pending changes, and that all files pass schema checks.
5. **Document** — Record the enhancement stats, decisions, and lessons learned.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear phases, explicit commands, and verification gates
- **Avoid**: Ambiguity, assumptions, scope creep, incomplete passes
- **Encourage**: Idempotent scripts, DRY references, evidence-based decisions, minimal changes

## Context

The prompt library at `./.github/prompts/` contains `.prompt.md` files that may be partially enhanced. Target state: every prompt has all 13 structural sections (Goal, Subgoals, Personas, Personality, Context, Rules, Phases, Best Practices, Verification Checklist, Skills Required, MCP Servers & Tools, Tasks, Dependencies) with shared templates referenced via DRY, not inlined.

Enhancement scripts live in `.enhance/`:

- `comprehensive_enhance.py` — Appends missing sections using shared templates
- `analyze_prompts.py` — Scans all prompts for frontmatter validity, section coverage, DRY compliance
- `repair_yaml_v2.py` — Targeted YAML quote repair for stubborn files

Shared templates live in `templates/_shared/` (frontmatter.md, rules-core.md, skills-table-core.md, goals.md, phases.md, best-practices.md, verification-checklist.md, personality.md, personas.md, deps-core.md, section-skeleton.md, skill-refs.md).

The enhancement workflow must be **idempotent** — re-running the same script on an already-enhanced library must produce zero changes and zero issues.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

1. **DRY first** — Reference shared templates in `templates/_shared/` instead of inlining content. Each section heading should link to the corresponding shared template.
2. **Idempotent** — Every script and workflow must be safe to re-run without side effects or duplicate content.
3. **No backup artifacts** — Use git for rollback. Never create `.bak`, `.old`, or timestamped copies.
4. **YAML validity is mandatory** — All 214 prompts must pass `yaml.safe_load` without errors. Broken YAML blocks the entire pipeline.
5. **Quote all YAML values with `:` or `#` or `[]{}`** — These are YAML mapping indicators and will break parse without proper quoting. Prefer single quotes for values containing `"`; double quotes otherwise.
6. **Verify before claim** — After each phase, run the analyzer and check `--dry-run` output before declaring phase complete.

### Standing Rules

1. **Map before touch** — Understand the current prompt state before making changes. Run analyzer first.
2. **Smallest safe change** — Minimal change that achieves the goal. Don't restructure what already works.
3. **Verify before claim** — Test before reporting complete. Run full analysis and dry-run.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Setup and Discovery

1. Load mandatory skills: `/using-superpowers`, `/subagent-driven-development`, `/brainstorming`, `/prompt-engineering-patterns`, `/prompt-management`, `/skill-judge`.
2. Run `analyze_prompts.py --all` to establish baselines: YAML validity, section coverage, DRY compliance, pending changes count.
3. Read 3-5 sample prompts to understand current state and structural patterns.
4. Review shared templates in `templates/_shared/` for section structure and DRY references.

### Phase 2: Enhancement

1. Run `comprehensive_enhance.py --dry-run` first to see what would change.
2. Review the diff plan and validate it adds missing sections without duplicating existing content.
3. Apply with `comprehensive_enhance.py --apply`.
4. After apply, immediately validate all YAML with `python -c "import yaml; [yaml.safe_load(open(f)) for f in Path(...).glob('*.prompt.md')]"`.

### Phase 3: YAML Repair (if needed)

1. Identify parse failures and categorize root cause:
   - Unquoted `:` in values → `repair_yaml_v2.py` or manual single-quote fix
   - Unescaped internal `"` → switch to single-quote wrapping
   - Copilot-style frontmatter not migrated → add `trigger:`, `mode: agent`, proper `description:`
2. Fix each category with targeted patches. Never batch-fix blindly.
3. Re-run `comprehensive_enhance.py --apply` after YAML repair to recalculate pending changes.
4. If files are corrupt beyond repair: `git checkout -- .github/prompts/` and re-apply with fixed script.

### Phase 4: Verification

1. Run `analyze_prompts.py --all` — confirm **0 critical issues**, **0 files with no frontmatter**, **100% valid YAML**.
2. Run `comprehensive_enhance.py --dry-run` — confirm **0 pending changes** (idempotent).
3. Manual checks:
   - Every prompt has `## Goal` section
   - All descriptions end with exactly one period
   - Skills table uses `templates/_shared/skills-table-core.md` reference
   - No duplicate section headings
   - No `promptmetadata` artifacts from corruption
4. Count total prompts vs modifications: `git diff --stat .github/prompts/`

### Phase 5: Documentation and Handoff

1. Generate `ENHANCEMENT_REPORT.md` with:
   - Phase-by-phase stats
   - Total files modified, lines added/removed
   - YAML parse status
   - Any remaining open items
   - Key decisions and lessons learned
2. Record findings in session memory and Honcho conclusions.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates in `templates/_shared/` instead of duplicating content. Every standardized section (Personas, Personality, Rules, Best Practices, Verification Checklist, Dependencies) links to its template.
2. **Structured output** — Use clear sections with consistent heading levels (`##` for top-level sections). Each prompt should have the same section ordering.
3. **Verification gates** — Always verify after each phase before moving to the next. An incomplete phase compounds into downstream issues.
4. **Minimal changes** — Fix root cause, not symptoms. A YAML parse error from incorrect quoting is a quoting bug, not a "regenerate the file" problem.
5. **Git safety net** — Before any bulk operation, ensure `git checkout -- .github/prompts/` can restore clean state if the enhancement corrupts files.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Discovery | Analyzer runs, sample prompts reviewed, templates read |
| 2 | Enhancement | `comprehensive_enhance.py` runs without errors, all prompts updated |
| 3 | YAML | All prompts pass `yaml.safe_load` — zero parse failures |
| 4 | Idempotency | `--dry-run` after apply shows 0 pending changes |
| 5 | Coverage | All 13 structural sections present on every prompt |
| 6 | DRY | Shared templates referenced, not inlined, in standardized sections |
| 7 | Quality | No duplicate headings, no corruption artifacts, descriptions end with `.` |
| 8 | Stats | Git diff counts match expected (all prompts touched once) |
| 9 | Documentation | ENHANCEMENT_REPORT.md written with full stats and decisions |

## Tasks

1. Run `analyze_prompts.py --all` for baseline.
2. Read sample prompts and shared templates.
3. Run `comprehensive_enhance.py --dry-run` and review.
4. Apply enhancement with `comprehensive_enhance.py --apply`.
5. Validate YAML across all prompts.
6. Fix any YAML parse errors (repair_yaml_v2.py or manual patch).
7. Re-run enhancement dry-run to confirm idempotent.
8. Generate ENHANCEMENT_REPORT.md.
9. Save lessons to memory and Honcho.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow and mandatory startup |
| `subagent-driven-development` | Implement -> spec-review -> quality-review pipeline within each task |
| `brainstorming` | Ideation for enhancement strategy and edge case identification |
| `prompt-engineering-patterns` | DRY patterns, section structure, best practice templates |
| `prompt-management` | Prompt library lifecycle: create, update, batch audit, document |
| `system-owner-docs` | Documentation generation for prompt library state |
| `skill-judge` | Score structure, compliance, and completeness of generated prompt files |

## MCP Servers & Tools

| Tool | Purpose |
| ------ | --------- |
| `filesystem` (MCP) | Read/write prompt files, list directories |
| `ast-grep` (MCP) | Code search across prompts for patterns |
| `memory` (MCP) | Persistent cross-session fact storage |
| `sequential-thinking` (MCP) | Structured reasoning for complex enhancement decisions |
| `terminal` (native) | Run enhancement scripts, git operations, YAML validation |
| `read_file` (native) | Read prompt files and templates |
| `write_file` (native) | Create new files, write documentation |
| `patch` (native) | Targeted edits to prompt files or scripts |
| `delegate_task` (native) | Parallel execution of independent enhancement workstreams |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

- **Python 3.11+** — Required for enhancement scripts (yaml, pathlib)
- **PyYAML** — `pip install pyyaml` for YAML validation
- **Git** — Rollback via `git checkout -- .github/prompts/` if enhancement corrupts files
- **Shared templates** — `templates/_shared/` must exist with all 12 reference files
- **Enhancement scripts** — `.enhance/comprehensive_enhance.py`, `.enhance/analyze_prompts.py`, `.enhance/fix_prompt_artifacts.py`, `.enhance/fix_fence_glue.py` must exist

## Workflow

See [`templates/_shared/section-skeleton.md`](templates/_shared/section-skeleton.md) for workflow structure.

### Invocation

This prompt is designed to be invoked with the stacked skill bundle:

```
/goal /using-superpowers /subagent-driven-development /brainstorming
```

Followed by the task description:

```
enhance, update all prompts at "./.github/prompts/*.prompt.md" using DRY principle, best practices and all appropriate, needed, optional personas, profiles, personalities, steps, rules, goal, phases, tasks, subtasks, subgoal, checklist, skills, MCP servers tools, tool, templates, plans, prompts and toolsets. Ensure each prompt and all its files is verified and validated and no issues remain.
```

### Phase Sequence

Execute strictly in order: **Discovery → Enhancement → YAML Repair → Verification → Documentation**. Do not proceed to the next phase until the current one passes all gates.

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`ai-prompt-engineering-safety-review.prompt.md`](ai-prompt-engineering-safety-review.prompt.md)
- [`boost-prompt.prompt.md`](boost-prompt.prompt.md)
- [`debugger-prompt.prompt.md`](debugger-prompt.prompt.md)
- [`tldr-prompt.prompt.md`](tldr-prompt.prompt.md)
