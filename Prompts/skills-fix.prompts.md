---
title: Skills Audit and Remediation
trigger: /skills-fix
description: >
  Audit, debug, deduplicate, and enhance Hermes skills in the adminbot profile.
  Runs hermes skills list → reorganizes misplaced skills → deduplicates →
  batch-audits all SKILL.md files in groups of 7 → generates per-skill reports
  and a master index → creates a remediation plan and execution prompt →
  applies fixes in priority order (F → C → B → A-).
tags: [hermes, skills, debugging, audit, dedup, remediation]
dependencies:
  - prompt:.github/prompts/context-map.prompt.md
  - prompt:.github/prompts/update-implementation-plan.prompt.md
  - prompt:.github/prompts/skills-debug-prompt.prompt.md
  - skill:using-superpowers
  - skill:brainstorming
  - skill:plans-and-specs
  - skill:dispatching-parallel-agents
  - skill:subagent-driven-development
  - skill:systematic-debugging
  - skill:simplify
  - skill:skill-judge
  - skill:skill-creator
  - tool:terminal
  - tool:patch
  - tool:write_file
  - tool:execute_code
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
  - using-superpowers — Establish session context and tool availability
  - brainstorming — Explore audit strategies and issue classification
  - plans-and-specs — Create remediation plan with fix specifications
  - dispatching-parallel-agents — Audit skills in parallel batches of 7
  - subagent-driven-development — Delegate per-skill debugging to subagents
  - systematic-debugging — Identify formatting, content, and structural issues
  - simplify — Consolidate redundant skill documentation
  - skill-judge — Evaluate and score skills against quality criteria
  - skill-creator — Author, scaffold, and validate in-repo skills---

## Goal

Full lifecycle audit and remediation of the Hermes adminbot skill library.
Discovers all SKILL.md files, reorganizes misplaced skills, deduplicates
cross-category copies, audits every skill for quality issues, generates
reports, plans fixes, and applies them in priority order.

## Context

- **Skills root:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\`
- **Audit output:** `docs/skills-debug-context.md` (master index)
- **Per-skill reports:** `docs/<category>/<skill>/skills-debug-context.md`
- **Remediation plan:** `docs/plan/skills-debug-plan.md`
- **Execution prompt:** `.github/prompts/skills-debug-prompt.prompt.md`
- **Batch size:** exactly 7 skills per turn
- **Grade scale:** A (clean) → A- (minor) → B (1 major / 3+ minor) → C (2+ major) → F (critical)

## Inputs

- Hermes skills directory (`hermes skills list` output)
- Existing per-skill reports if resuming from a prior run
- Optional priority areas or category filters from user

## Outputs

- Reorganized skill directory (correct categories, no duplicate root-level skills)
- Per-skill audit reports at `docs/<category>/<skill>/skills-debug-context.md`
- Master index at `docs/skills-debug-context.md`
- Remediation plan at `docs/plan/skills-debug-plan.md`
- Execution prompt at `.github/prompts/skills-debug-prompt.prompt.md`
- Patched SKILL.md files for all F/C-grade skills

## Rules

1. Read `docs/skills-debug-context.md` first if it exists — resume rather than re-run.
2. Run `hermes skills list` before any other step to get the live inventory.
3. Run `hermes skills update` to pull latest official skill versions.
4. Reorganize misplaced root-level skills to correct category subfolders before auditing.
5. Remove confirmed duplicates only after verifying the canonical copy exists.
6. Process skills in batches of exactly 7; never more.
7. Use `patch()` for targeted fixes; `write_file()` only for full rewrites.
8. Do not create backup files — git is the rollback mechanism.
9. Fix F-grade (critical) before C-grade (major) before B-grade (moderate).
10. Run `hermes skills check <name>` after each patch to verify.
11. Keep `docs/plan/skills-debug-plan.md` checklist updated as work completes.

## Known Issue Patterns (from 2026-06-04 audit)

| Code | Pattern                                                    | Fix                                          |
| ---- | ---------------------------------------------------------- | -------------------------------------------- |
| F1   | Missing YAML frontmatter `---` block                       | Add frontmatter with `name:`, `description:` |
| F2   | Missing required frontmatter key (`name`/`description`)    | Add the key with a value                     |
| F3   | Boilerplate: `## Goal\nUse when Use when <desc>`           | Replace with clean one-line description      |
| F3b  | Boilerplate: `## Goal\nUse when "<desc>" to accomplish...` | Replace with clean description               |
| C2   | Unclosed code fence (odd ``` count)                        | Append closing ` ``` ` at end of file        |
| S1   | Missing `## When to Use` or `## Workflow` (exact heading)  | Add section or accept semantic variant       |
| S2   | Heading level jump (H2 → H4 with no H3)                    | Insert intermediate heading                  |
| C1   | Stale patterns (`pip install`, `npm install -g`)           | Note as supply_chain warning                 |
| R1   | Duplicate section heading                                  | Remove second occurrence, merge content      |

## Reorganization Map (from 2026-06-04 session)

Skills moved to correct categories:

- `agent-browser` → `autonomous-ai-agents/`
- `algorithmic-art` → `creative/`
- `asdf` → `devops/`
- `banking` → `software-development/`
- `brainstorming` → `planning/` (was duplicate with `development/brainstorming`)
- `brand-guidelines` → `creative/`
- `canvas-design` → `creative/`
- `validate-memories` → `devops/`
- `watchers` → `devops/`

Duplicates removed:

- `development/brainstorming` (canonical: `planning/brainstorming`)
- `(root)/dogfood` (canonical: `qa/dogfood`)
- `(root)/yuanbao` (canonical: `productivity/yuanbao`)

## Phases

### Phase 1: Setup and Inventory

1. Load required skills with `skill_view()`
2. Run `hermes skills update` to pull latest official versions
3. Run `hermes skills list` for the live inventory count
4. Find all SKILL.md files: `find <skills_root> -name 'SKILL.md' | sort`
5. Check for misplaced root-level skills (individual skills not in a category subdir)
6. Check for duplicate skill names across categories

### Phase 2: Reorganize and Deduplicate

1. Move misplaced root-level local skills to correct category subfolders
2. Verify canonical copy exists before removing any duplicate
3. Remove confirmed duplicate copies
4. Verify root directory contains only category dirs + known official root-skills

### Phase 3: Batch Audit

Run the audit script (`C:/Users/Alexa/AppData/Local/Temp/audit_skills.py`) or
implement equivalent logic in `execute_code`. For each skill in batches of 7:

1. Read SKILL.md content
2. Check: frontmatter present, required keys, boilerplate corruption
3. Check: required sections (with variant matching)
4. Check: heading hierarchy, code fence parity, table pipe consistency
5. Check: stale patterns, duplicate headings, placeholder text
6. Assign grade (A/A-/B/C/F) and write per-skill report
7. Append to master index

### Phase 4: Generate Plan and Execution Prompt

1. Write `docs/plan/skills-debug-plan.md` — phased fix plan from audit findings
2. Write `.github/prompts/skills-debug-prompt.prompt.md` — prompt to execute the plan

### Phase 5: Execute Fixes (Priority Order)

**F-grade first** — Fix critical issues (unclosed fences, missing frontmatter):

````python
# For unclosed code fences: append closing fence
with open(skill_path, 'a', encoding='utf-8') as f:
    f.write("\n```\n")
````

**C-grade next** — Fix major issues (boilerplate `## Goal`, missing `## When to Use`):

```python
# F3 fix pattern:
content = content.replace(
    "## Goal\nUse when Use when <desc>",
    "## Goal\n<desc>"
)
```

**B-grade last** — Fix moderate issues in batches of 7 (S1 section stubs, R1 dedup,
S2 heading gaps, C1 stale comments).

### Phase 6: Verify

1. Re-run audit script — confirm F=0, C=0, total issues reduced
2. Update master index with re-run results
3. Mark plan checklist items `[x]`
4. `git diff --stat` to review scope
5. `git commit -m "chore: skill library audit and remediation <date>"`

## Steps

1. Load required skills (`using-superpowers`, `skill-judge`, `plans-and-specs`, `dispatching-parallel-agents`)
2. Run `hermes skills update` — pull official updates
3. Run `hermes skills list` + `find` — build live inventory
4. Reorganize misplaced root-level skills; remove duplicates
5. Run audit script in batches of 7 → write per-skill reports + master index
6. Write `docs/plan/skills-debug-plan.md` from audit findings
7. Write `.github/prompts/skills-debug-prompt.prompt.md`
8. Fix F-grade skills (critical issues)
9. Fix C-grade skills (major issues)
10. Fix B-grade skills in batches of 7
11. Re-run audit → verify grade distribution (target: F=0, C=0)
12. Update plan checklist; git commit

## Tasks

- [ ] Run `hermes skills update` for latest official versions
- [ ] Run `hermes skills list` and `find` for inventory
- [ ] Reorganize misplaced root-level skills to correct categories
- [ ] Remove confirmed duplicate skills
- [ ] Batch-audit all SKILL.md files in groups of 7
- [ ] Write per-skill reports to `docs/<category>/<skill>/skills-debug-context.md`
- [ ] Write master index to `docs/skills-debug-context.md`
- [ ] Write remediation plan to `docs/plan/skills-debug-plan.md`
- [ ] Write execution prompt to `.github/prompts/skills-debug-prompt.prompt.md`
- [ ] Fix all F-grade skills (critical issues)
- [ ] Fix all C-grade skills (major issues)
- [ ] Fix B-grade skills in batches of 7
- [ ] Re-run audit and verify F=0, C=0
- [ ] Update plan checklist and commit

## Actions

- `terminal("hermes skills list")` — Get live skill inventory
- `terminal("hermes skills update")` — Pull latest official skill versions
- `terminal("hermes skills check <name>")` — Validate skill format after fix
- `terminal("find <skills_root> -name 'SKILL.md' | sort")` — Enumerate all skill files
- `terminal("mv <src> <dst>")` — Move misplaced skill to correct category
- `terminal("rm -rf <dup_path>")` — Remove duplicate after verifying canonical exists
- `execute_code(audit_script)` — Run batch audit across all skills
- `read_file(path)` — Read individual skill for manual review
- `patch(path, old_string, new_string)` — Apply targeted skill fix
- `write_file(path, content)` — Write audit reports, plans, or full skill rewrites
- `terminal("git diff --stat")` — Review scope before commit
- `terminal("git commit -m 'chore: ...'")` — Commit remediation changes

## Subagents

When processing B-grade batch remediations, dispatch in parallel using:

```python
delegate_task(tasks=[
    {"goal": "Fix B-grade issues in batch: skill-a, skill-b, skill-c, skill-d, skill-e, skill-f, skill-g",
     "context": "Skills root: C:\\...\\skills\\ Per-skill reports in docs/. Fix issues listed in each report.",
     "toolsets": ["file", "terminal"]},
    # up to 3 concurrent batches
])
```
