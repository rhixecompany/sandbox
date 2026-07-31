---

name: dev-init

title: Dev Init - Prompt Conversion and Enhancement Planning

description: 'Create a comprehensive plan for converting plaintext prompts to markdown, enhancing prompt quality, and updating related implementation plans.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills:

  - introspection-only-general

  - no-git-delete

  - no-net-fetch

  - skills-tools-preflight-check

  - context-map

  - convert-plaintext-to-md

  - boost-prompt

  - ai-prompt-engineering-safety-review

  - update-implementation-plan

  - prompt-builder

  - brainstorming

  - plans-and-specs

  - writing-skills

  - writing-plans

  - acpx-executor

  - executing-plans

  - simplify

  - subagent-driven-development

formatter: default

plan: None

dependencies:

  - prompt:context-map.prompt.md

  - prompt:convert-plaintext-to-md.prompt.md

  - prompt:boost-prompt.prompt.md

  - prompt:ai-prompt-engineering-safety-review.prompt.md

  - prompt:update-implementation-plan.prompt.md

  - prompt:prompt-builder.prompt.md

  - skill:brainstorming

  - skill:plans-and-specs

  - skill:writing-skills

  - skill:writing-plans

  - skill:acpx-executor

  - skill:executing-plans

  - skill:simplify

  - skill:subagent-driven-development

  - skill:introspection-only-general

  - skill:no-git-delete

  - skill:no-net-fetch

  - skill:skills-tools-preflight-check

  - skill:context-map

  - skill:convert-plaintext-to-md

  - skill:boost-prompt

  - skill:ai-prompt-engineering-safety-review

  - skill:update-implementation-plan

  - skill:prompt-builder

tags:

  - audit

  - markdown

  - ml

  - planning

  - prompts

  - security

  - typescript

  - workflow

  - git

trigger: /dev-init

metadata:

  hermes: {}

---

## Goal

Create a comprehensive plan for converting plaintext prompts to markdown, enhancing prompt quality, and updating related implementation plans.

>> Create a detailed prompt-library plan> and verification criteria.

## Goal

Plan the prompt-library refresh end to end: convert plaintext prompts tomarkdown, improve prompt quality, review safety, and keep the implementationplan current.

## Context

Use this prompt when a prompt-library refresh needs planning beforeimplementation. The primary workflow is:1. `prompts/context-map`2. `prompts/convert-plaintext-to-md`3. `prompts/boost-prompt`4. `prompts/ai-prompt-engineering-safety-review`5. `prompts/update-implementation-plan`6. `prompts/prompt-builder`7. `.github/prompts/*.md`Reference artifacts:- `docs/dev-init-comprehensive-plan.md`- `docs/dev-init-spec.md`- `docs/prompts-cross-reference-registry.md`- `docs/prompt-conversion-enhancement-plan.md`- `projects/Bash/archive/artifacts/context-maps/dev-init.context.json`

## Input

s

- Source inventory for `.github/prompts/*.txt`
- Existing `.github/prompts/*.md` files
- Related `.github/prompts/*.prompt.md` workflows
- Workspace context and implementation constraints

## Output

s

- A conversion and enhancement plan
- A safety and quality review checklist
- File references and integration points
- An implementation guide with verification steps

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Run `context-map` before any conversion or planning work.
2. Keep the pipeline idempotent and safe to re-run.
3. Preserve the original task intent while improving clarity and structure.
4. Keep manual safety notes unless they are wrong.
5. Use git for rollback; do not create backup copies.
6. Update the implementation plan when scope or requirements change.
7. Prefer file-backed evidence over inference.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill                                 | Purpose                                                          |
| ------------------------------------- | ---------------------------------------------------------------- |
| `context-map` (prompt)                | Map source, destination, and dependency impact before conversion |
| `convert-plaintext-to-md`             | Convert plaintext prompts to markdown                            |
| `boost-prompt`                        | Improve prompt quality and structure                             |
| `ai-prompt-engineering-safety-review` | Review prompts for safety and clarity                            |
| `update-implementation-plan`          | Keep the implementation plan current                             |
| `prompt-builder`                      | Scaffold new prompt files                                        |
| `brainstorming`                       | Explore conversion and enhancement approaches                    |
| `plans-and-specs`                     | Create detailed specs with file references                       |
| `writing-skills`                      | Craft and optimize prompts and instructions                      |
| `writing-plans`                       | Structure the plan and its sections                              |
| `acpx-executor`                       | Execute a prompt via any ACPX provider                           |
| `executing-plans`                     | Execute implementation steps in order                            |
| `simplify`                            | Keep the output concise and non-redundant                        |

## Phases

### Phase 1: Discover and verify

Confirm the source files, target prompts, and required templates before planningchanges.

### Phase 2: Plan conversion

Define how `.github/prompts/*.txt` should convert to `.github/prompts/*.md` and what must bepreserved.

### Phase 3: Plan audits and fixes

Specify how to audit `boost-prompt`, `ai-prompt-engineering-safety-review`,`update-implementation-plan`, and `prompt-builder` with concrete findings.

### Phase 4: Review and hand off

Produce a compact completion report with execution steps, risk notes, and exitcriteria.

### Phase 5: Execute Implementation Plan

Run the conversion and enhancement pipeline end-to-end. Idempotent — safe to re-run.

## Steps

1. Load `context-map`, `brainstorming`, and `plans-and-specs`.
2. Verify the conversion and audit templates exist.
3. Map the prompt-library dependencies.
4. Plan `.github/prompts/*.txt` → `.github/prompts/*.md` conversion.
5. Plan audits for the related `.github/prompts/*.prompt.md` files.
6. Confirm the target prompts reference `context-map` where relevant.
7. Produce the final plan and handoff notes.

## Tasks

- [ ] Read the source inventory and target prompt files- [ ] Confirm the conversion and audit templates exist- [ ] Define the TXT→MD conversion scope and idempotency rules- [ ] Capture the feature specs, file references, and safety checks- [ ] List the prompts that need audit and cross-reference updates- [ ] Document the risk items and missing dependency links- [ ] Compile a concise completion report for implementation

## Subtasks

- [ ] Map `.github/prompts/*.txt` to their `.md` counterparts- [ ] Preserve source intent and safety notes in each converted file- [ ] Check for `context-map` references in each audit target- [ ] Record any missing template or format assumptions

## Actions

- `read_file("prompts/context-map.prompt.md")` — Load the dependency map  before planning
- `skill_view(name="brainstorming")` — Expand workflow options and tradeoffs
- `skill_view(name="plans-and-specs")` — Produce the detailed plan artifact
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers
- `search_files(pattern, target)` — Locate related prompt files and templates
- `delegate_task(goal, toolsets)` — Split audit work when multiple files are  involved---

## Reference: `/enhance-markdown` Prompt

> Full definition: `_archive/dev-init.prompts.txt` (lines 99–836)The `/enhance-markdown` prompt is the four-phase markdown auditor and enhancerused by the TXT→MD conversion pipeline. Key properties:```bash/enhance-markdown <file
> [slug]       # audit + enhance mode/enhance-markdown --txt-to-md [file]  # TXT→MD conversion mode (batch or single)```- **9-section template**: Skills → Subagents → Personas → Rules → Phases → Steps  → Tasks → Subtasks → Actions- **Batch size**: exactly 7 files per batch- **Resumable**: each phase checks for existing artifacts before re-running- **Plugin planning**: uses `createPlan`/`createSpec`/`appendSpec` with  companion markdown fallback---

## Phase 5: Execute Implementation Plan

> Run the conversion and enhancement pipeline end-to-end. Idempotent — safe to re-run.

### Entry Check

```
IF docs/prompt-conversion-enhancement-plan.md EXISTS → read it, skip to Step 5.3ELSE IF docs/dev-init-comprehensive-plan.md EXISTS → plan exists, skip to Step 5.2ELSE → run Phase 1–4 first, then return here
```

### Step 5.1 — Load Plan Artifacts

```
bashread_file("docs/dev-init-comprehensive-plan.md")read_file("docs/dev-init-spec.md")read_file("projects/Bash/archive/artifacts/context-maps/dev-init.context.json")
```

### Step 5.2 — Run `context-map`1. Load `prompts/context-map.prompt.md`2. Map all `.github/prompts/*.txt` → `.github/prompts/*.md` pairs3. Map all `.github/prompts/*.prompt.md` dependencies4. Write `docs/prompts-cross-reference-registry.md`

### Step 5.3 — Run `convert-plaintext-to-md`For each `.github/prompts/*.txt` file:1. Read raw `.txt` content2. Apply enhancement (Stanford/Anthropic patterns):    - Critical rules in first 15%    - Nesting depth ≤ 4    - Instruction ratio 40–50%    - Single source of truth (no rule repeated

> 2×)    - 3-tier prioritization: Safety → Core Workflow → Optimization3. Apply 9-section template:   `Skills → Subagents → Personas → Rules → Phases → Steps → Tasks → Subtasks → Actions`4. Write to `.github/prompts/<same-stem>.md` (overwrite if exists)

### Step 5.4 — Run `boost-prompt`For each `.github/prompts/*.md` file:1. Load `prompts/boost-prompt.prompt.md`2. Apply quality enhancements:    - Strengthen rule language (imperative, specific)    - Add missing frontmatter (title, description, tags, trigger)    - Ensure consistent heading hierarchy    - Remove redundant sections3. **Constraint Preservation Audit**: log any rule removals with justification4. Write enhanced file back

### Step 5.5 — Run `ai-prompt-engineering-safety-review`For each `.github/prompts/*.md` and `.github/prompts/*.prompt.md`:1. Load `prompts/ai-prompt-engineering-safety-review.prompt.md`2. Check for:    - Credential handling safety    - Backup/rollback instructions present    - Approval workflows for destructive ops    - No fabricated verification claims3. Add safety notes where missing4. **Fail if critical safety constraints removed** — halt and report

### Step 5.6 — Run `prompt-builder`For any missing prompts:1. Load `prompts/prompt-builder.prompt.md`2. Scaffold new `.prompt.md` files from template3. Populate with content from plan artifacts

### Step 5.7 — Run `update-implementation-plan`1. Load `prompts/update-implementation-plan.prompt.md`2. Update `docs/dev-init-comprehensive-plan.md` with:    - Actual files processed    - Issues found and resolved    - Remaining items3. Mark completed phases

### Tasks

- [ ] Load all plan artifacts (Step 5.1)- [ ] Run context-map and write cross-reference registry (Step 5.2)- [ ] Convert all `.github/prompts/*.txt` → `.github/prompts/*.md` (Step 5.3)- [ ] Boost all `.github/prompts/*.md` files (Step 5.4)- [ ] Safety-review all prompts (Step 5.5)- [ ] Build missing prompts (Step 5.6)- [ ] Update implementation plan (Step 5.7)---

## Phase 6: Verify All Prompts Optimal

> Independent verification — read Phase 1 outputs only, not Phase 5 outputs (prevents confirmation bias).

### Step 6.1 — Structural Audit

For each `.github/prompts/*.md`:```bash# Check frontmatterhead -10 Prompts/<name

> .prompts.md | grep "^title:"head -10 Prompts/<name>.prompts.md | grep "^description:"head -10 Prompts/<name>.prompts.md | grep "^trigger:"head -10 Prompts/<name>.prompts.md | grep "^tags:"# Check required sections existgrep -c "^

## Goal

" Prompts/<name>.prompts.mdgrep -c "^

## Phases

" Prompts/<name>.prompts.mdgrep -c "^

## Steps

" Prompts/<name>.prompts.mdgrep -c "^

## Tasks" Prompts/<name

> .prompts.mdgrep -c "^

## Actions

" Prompts/<name>.prompts.md```

### Step 6.2 — Cross-Reference Validation

```bash
# Verify all internal references resolvegrep -o '\[.*\](\./[^)]*)' Prompts/<name>.prompts.md | while read ref; do  path=$(echo "$ref" | sed 's/.*(\(.*\))/\1/')  test -f "$path" || echo "BROKEN REF: $ref in Prompts/<name>.prompts.md"done
```

### Step 6.3 — Conflict Detection

```bash
# Check for duplicate triggers across Prompts/grep -h "^trigger:" Prompts/*.prompts.md | sort | uniq -d# Check for duplicate titlesgrep -h "^title:" Prompts/*.prompts.md | sort | uniq -d
```

### Step 6.4 — Quality Scoring

Score each `.github/prompts/*.md`:| Criterion                             | Points | Detection                                        || ------------------------------------

- | ------ | ------------------------------------------------ || YAML frontmatter complete             | +20    | title + description + trigger + tags present     || Summary paragraph present             | +15    | First paragraph after frontmatter is a summary   || All required sections                 | +20    | Goal, Phases, Steps, Tasks, Actions present      || Skills section references real skills | +10    | Each skill listed exists in `hermes skills list` || Actions use real tools                | +10    | Each action maps to an available tool            || No broken internal refs               | +15    | All relative paths resolve                       || Consistent heading hierarchy          | +10    | H1→H2→H3, no skipped levels                      |**Threshold**: ≥80 = optimal, 60–79 = needs work, <60 = rewrite required.

### Step 6.5 — Write Verification Report

```markdown
# docs/dev-init-verification-report.md

## Summary

- Total .md files: N- Optimal (≥80): N- Needs work (60–79): N- Rewrite required (<60): N

## Per-File Scores| File | Score | Issues || ---- | ----- | ------ || ...  | ...   | ...    |

## Conflicts Found| Type              | Files | Resolution || ----------------

- | ----- | ---------- || Duplicate trigger | ...   | ...        |

## Broken References| File | Reference | Status || ---

- | --------- | ------ || ...  | ...       | ...    |
```

### Tasks

- [ ] Structural audit all `.github/prompts/*.md` files- [ ] Validate all cross-references resolve- [ ] Detect duplicate triggers/titles- [ ] Score each file against quality criteria- [ ] Write verification report to `docs/dev-init-verification-report.md`- [ ] Fix any files scoring <80- [ ] Re-verify after fixes---

## Phase 7: Cross-Reference Registry

> Build the master registry of all prompts and their relationships.

### Step 7.1 — Build Registry

Write `docs/prompts-cross-reference-registry.md`:```markdown# Prompts Cross-Reference Registry

## Prompts/\*.md (Conversion Targets)| File                  | Trigger     | Status | Score | Depends On                           || --------------------

- | ----------- | ------ | ----- | ------------------------------------ || skills-fix.prompts.md | /skills-fix | ✅     | 85    | context-map, skill-judge             || dev-init.prompts.md   | /dev-init   | ✅     | 90    | context-map, convert-plaintext-to-md || ...                   | ...         | ...    | ...   | ...                                  |

## prompts/\*.prompt.md (Workflow Prompts)| File                              | Purpose             | Used By             || --------------------------------

- | ------------------- | ------------------- || context-map.prompt.md             | Dependency mapping  | All dev-init phases || convert-plaintext-to-md.prompt.md | TXT→MD conversion   | Phase 5.3           || boost-prompt.prompt.md            | Quality enhancement | Phase 5.4           || ...                               | ...                 | ...                 |

## Conflict Log| Conflict | Files | Resolution || -------

- | ----- | ---------- || ...      | ...   | ...        |```

### Step 7.2 — Final Verification

```

bash# Count total promptsls Prompts/*.prompts.md | wc -lls prompts/*.prompt.md | wc -l# Verify registry matches disk# Every file on disk is in registry# Every registry entry exists on disk

```

### Tasks

- [ ] Build cross-reference registry- [ ] Verify registry matches disk state- [ ] Commit all changes with `git commit -m "dev-init: complete prompt-library refresh"`---

## Execution Summary

When all 7 phases are complete, output:```========================================DEV INIT — PROMPT LIBRARY REFRESH COMPLETE========================================Phases executed:    7/7Prompts converted:  N/N (.txt → .md)Prompts boosted:    N/NSafety reviews:     N passed, N failedQuality score ≥80:  N/NConflicts resolved: NBroken refs fixed:  NRegistry:           docs/prompts-cross-reference-registry.mdVerification:       docs/dev-init-verification-report.md========================================```

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
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
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
