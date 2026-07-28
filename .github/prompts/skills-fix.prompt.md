---
name: skills-fix
title: Skills Audit and Remediation
description: 'Audit, debug, deduplicate, and enhance Hermes skills in the adminbot profile. Runs hermes skills list → reorganizes misplaced skills → deduplicates → batch-audits all SKILL.md files in groups of 7 → generates per-skill reports and a master index → creates a remediation plan and execution prompt → applies fixes in priority order (F → C → B → A-).'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - code_execution
  - file
  - terminal
  - web
scripts: []
skills:
  - introspection-only-general
  - no-git-delete
  - no-net-fetch
  - skills-tools-preflight-check
  - subagent-driven-development
  - using-superpowers
  - brainstorming
  - plans-and-specs
  - dispatching-parallel-agents
  - systematic-debugging
  - simplify
  - skill-judge
  - skill-creator
formatter: default
plan: None
dependencies:
  - prompt:context-map
  - prompt:update-implementation-plan
  - prompt:skills-debug-prompt
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
  - skill:introspection-only-general
  - skill:no-git-delete
  - skill:no-net-fetch
  - skill:skills-tools-preflight-check
tags:
  - ai-assistant
  - audit
  - data
  - debugging
  - fix
  - generator
  - prompts
  - skills
  - typescript
trigger: /skills-fix
metadata:
  hermes: {}
---
## GoalFull lifecycle audit and remediation of the Hermes adminbot skill library.Discovers all SKILL.md files, reorganizes misplaced skills, deduplicatescross-category copies, audits every skill for quality issues, generatesreports, plans fixes, and applies them in priority order.

## Context- **Skills root:** `$HOME/AppData/Local/hermes/skills/` (resolves to `C:\Users\Alexa\AppData\Local\hermes\skills\`)- **Audit output:** `docs/skills-debug-context.md` (master index)- **Per-skill reports:** `docs/<category>/<skill>/skills-debug-context.md`- **Remediation plan:** `docs/plan/skills-debug-plan.md`- **Execution prompt:** `prompts/skills-debug-prompt.prompt.md`- **Batch size:** exactly 7 skills per turn- **Grade scale:** A (clean) → A- (minor) → B (1 major / 3+ minor) → C (2+ major) → F (critical)

## Inputs- Hermes skills directory (`hermes skills list` output)- Existing per-skill reports if resuming from a prior run- Optional priority areas or category filters from user

## Outputs- Reorganized skill directory (correct categories, no duplicate root-level skills)- Per-skill audit reports at `docs/<category>/<skill>/skills-debug-context.md`- Master index at `docs/skills-debug-context.md`- Remediation plan at `docs/plan/skills-debug-plan.md`- Execution prompt at `prompts/skills-debug-prompt.prompt.md`- Patched SKILL.md files for all F/C-grade skills

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)1. Read `docs/skills-debug-context.md` first if it exists — resume rather than re-run.2. Run `hermes skills list` before any other step to get the live inventory.3. Run `hermes skills update` to pull latest official skill versions.4. Reorganize misplaced root-level skills to correct category subfolders before auditing.5. Remove confirmed duplicates only after verifying the canonical copy exists.6. Process skills in batches of exactly 7; never more.7. Use `patch()` for targeted fixes; `write_file()` only for full rewrites.8. Do not create backup files — git is the rollback mechanism.9. Fix F-grade (critical) before C-grade (major) before B-grade (moderate).10. Run `hermes skills check <name>` after each patch to verify.11. Keep `docs/plan/skills-debug-plan.md` checklist updated as work completes.

## Known Issue Patterns (from 2026-06-04 audit)| Code | Pattern                                                    | Fix                                          || ---- | ---------------------------------------------------------- | -------------------------------------------- || F1   | Missing YAML frontmatter `---` block                       | Add frontmatter with `name:`, `description:` || F2   | Missing required frontmatter key (`name`/`description`)    | Add the key with a value                     || F3   | Boilerplate: `

## Goal\nUse when Use when <desc>`           | Replace with clean one-line description      || F3b  | Boilerplate: `

## Goal\nUse when "<desc>" to accomplish...` | Replace with clean description               || C2   | Unclosed code fence (odd ``` count)                        | Append closing ` ``` ` at end of file        || S1   | Missing `

## When to Use` or `

## Workflow` (exact heading)  | Add section or accept semantic variant       || S2   | Heading level jump (H2 → H4 with no H3)                    | Insert intermediate heading                  || C1   | Stale patterns (`pip install`, `npm install -g`)           | Note as supply_chain warning                 || R1   | Duplicate section heading                                  | Remove second occurrence, merge content      |

## Reorganization Map (from 2026-06-04 session)Skills moved to correct categories:- `agent-browser` → `autonomous-ai-agents/`- `algorithmic-art` → `creative/`- `asdf` → `devops/`- `banking` → `software-development/`- `brainstorming` → `planning/` (was duplicate with `development/brainstorming`)- `brand-guidelines` → `creative/`- `canvas-design` → `creative/`- `validate-memories` → `devops/`- `watchers` → `devops/`Duplicates removed:- `development/brainstorming` (canonical: `planning/brainstorming`)- `(root)/dogfood` (canonical: `qa/dogfood`)- `(root)/yuanbao` (canonical: `productivity/yuanbao`)

## Phases

### Phase 1: Setup and Inventory1. Load required skills with `skill_view()`2. Run `hermes skills update` to pull latest official versions3. Run `hermes skills list` for the live inventory count4. Find all SKILL.md files: `find <skills_root> -name 'SKILL.md' | sort`5. Check for misplaced root-level skills (individual skills not in a category subdir)6. Check for duplicate skill names across categories

### Phase 2: Reorganize and Deduplicate1. Move misplaced root-level local skills to correct category subfolders2. Verify canonical copy exists before removing any duplicate3. Remove confirmed duplicate copies4. Verify root directory contains only category dirs + known official root-skills

### Phase 3: Batch AuditRun the audit script (`C:/Users/Alexa/AppData/Local/Temp/audit_skills.py`) orimplement equivalent logic in `execute_code`. For each skill in batches of 7:1. Read SKILL.md content2. Check: frontmatter present, required keys, boilerplate corruption3. Check: required sections (with variant matching)4. Check: heading hierarchy, code fence parity, table pipe consistency5. Check: stale patterns, duplicate headings, placeholder text6. Assign grade (A/A-/B/C/F) and write per-skill report7. Append to master index

### Phase 4: Generate Plan and Execution Prompt1. Write `docs/plan/skills-debug-plan.md` — phased fix plan from audit findings2. Write `prompts/skills-debug-prompt.prompt.md` — prompt to execute the plan

### Phase 5: Execute Fixes (Priority Order)**F-grade first** — Fix critical issues (unclosed fences, missing frontmatter):````python# For unclosed code fences: append closing fencewith open(skill_path, 'a', encoding='utf-8') as f:    f.write("\n```\n")````**C-grade next** — Fix major issues (boilerplate `

## Goal`, missing `

## When to Use`):```python# F3 fix pattern:content = content.replace(    "

## Goal\nUse when Use when <desc>",    "

## Goal\n<desc>")```**B-grade last** — Fix moderate issues in batches of 7 (S1 section stubs, R1 dedup,S2 heading gaps, C1 stale comments).

### Phase 6: Verify1. Re-run audit script — confirm F=0, C=0, total issues reduced2. Update master index with re-run results3. Mark plan checklist items `[x]`4. `git diff --stat` to review scope5. `git commit -m "chore: skill library audit and remediation <date>"`

## Steps1. Load required skills (`using-superpowers`, `skill-judge`, `plans-and-specs`, `dispatching-parallel-agents`)2. Run `hermes skills update` — pull official updates3. Run `hermes skills list` + `find` — build live inventory4. Reorganize misplaced root-level skills; remove duplicates5. Run audit script in batches of 7 → write per-skill reports + master index6. Write `docs/plan/skills-debug-plan.md` from audit findings7. Write `prompts/skills-debug-prompt.prompt.md`8. Fix F-grade skills (critical issues)9. Fix C-grade skills (major issues)10. Fix B-grade skills in batches of 711. Re-run audit → verify grade distribution (target: F=0, C=0)12. Update plan checklist; git commit

## Tasks- [ ] Run `hermes skills update` for latest official versions- [ ] Run `hermes skills list` and `find` for inventory- [ ] Reorganize misplaced root-level skills to correct categories- [ ] Remove confirmed duplicate skills- [ ] Batch-audit all SKILL.md files in groups of 7- [ ] Write per-skill reports to `docs/<category>/<skill>/skills-debug-context.md`- [ ] Write master index to `docs/skills-debug-context.md`- [ ] Write remediation plan to `docs/plan/skills-debug-plan.md`- [ ] Write execution prompt to `prompts/skills-debug-prompt.prompt.md`- [ ] Fix all F-grade skills (critical issues)- [ ] Fix all C-grade skills (major issues)- [ ] Fix B-grade skills in batches of 7- [ ] Re-run audit and verify F=0, C=0- [ ] Update plan checklist and commit

## Actions- `terminal("hermes skills list")` — Get live skill inventory- `terminal("hermes skills update")` — Pull latest official skill versions- `terminal("hermes skills check <name>")` — Validate skill format after fix- `terminal("find <skills_root> -name 'SKILL.md' | sort")` — Enumerate all skill files- `terminal("mv <src> <dst>")` — Move misplaced skill to correct category- `terminal("rm -rf <dup_path>")` — Remove duplicate after verifying canonical exists- `execute_code(audit_script)` — Run batch audit across all skills- `read_file(path)` — Read individual skill for manual review- `patch(path, old_string, new_string)` — Apply targeted skill fix- `write_file(path, content)` — Write audit reports, plans, or full skill rewrites- `terminal("git diff --stat")` — Review scope before commit- `terminal("git commit -m 'chore: ...'")` — Commit remediation changes

## SubagentsWhen processing B-grade batch remediations, dispatch in parallel using:```pythondelegate_task(tasks=[    {"goal": "Fix B-grade issues in batch: skill-a, skill-b, skill-c, skill-d, skill-e, skill-f, skill-g",     "context": "Skills root: C:\\...\\skills\\ Per-skill reports in docs/. Fix issues listed in each report.",     "toolsets": ["file", "terminal"]},    # up to 3 concurrent batches])```

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
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.


## Phases

### Phase 1: Intake
- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute
- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify
- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off
- Return final artifact or findings clearly.
- Stop once the requested result is delivered.


## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.


## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Audit, debug, deduplicate, and enhance Hermes skills in the adminbot profile. Runs hermes skills list → reorganizes misplaced skills → deduplicates → batch-audits all SKILL.md files in groups of 7 → generates per-skill reports and a master index → creates a remediation plan and execution prompt → applies fixes in priority order (F → C → B → A-).


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |



## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions


