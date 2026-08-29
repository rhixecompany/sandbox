---
name: prompt-management
title: Prompt Management
description: "Manage the .github/prompts/ lifecycle end to end: inventory, dedupe, extract shared templates, update every prompt to use them, create missing skills/scripts, and run strict validation."
trigger: /prompt-management
version: 1.0.0
author: Hermes Agent
tags: [prompts, lifecycle, dedupe, templates, validation, refactor, automation]
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
date: '2026-08-25'
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Copy-write frontmatter template strict validator](#copy-write-frontmatter-template-strict-validator)
- [Contract](#contract)
  - [Hard Requirements](#hard-requirements)
- [Library Verification Checklist](#library-verification-checklist)
- [Phases](#phases)
- [Phase 1: Inventory](#phase-1:-inventory)
  - [1.1 Discover files](#11-discover-files)
  - [1.2 Parse metadata](#12-parse-metadata)
  - [1.3 Triage markers](#13-triage-markers)
  - [1.4 Write tentative registry](#14-write-tentative-registry)
- [Phase 2: Deduplicate](#phase-2:-deduplicate)
  - [2.1 Define duplicateA duplicate is any prompt that:](#21-define-duplicatea-duplicate-is-any-prompt-that:)
  - [2.2 Duplicate resolution](#22-duplicate-resolution)
  - [2.3 Update references](#23-update-references)
  - [2.4 Update registry](#24-update-registry)
- [Phase 3: Template extraction](#phase-3:-template-extraction)
  - [3.1 Identify shared patterns](#31-identify-shared-patterns)
  - [3.2 Create shared templates](#32-create-shared-templates)
  - [3.3 Extract prompt-specific variants](#33-extract-prompt-specific-variants)
  - [<prompt-name](#<prompt-name)
  - [3.4 Register templates](#34-register-templates)
- [Phase 4: Prompt updates](#phase-4:-prompt-updates)
  - [4.1 Update references](#41-update-references)
  - [4.2 Canonical format](#42-canonical-format)
  - [4.3 Keep templates drivable](#43-keep-templates-drivable)
  - [4.4 Apply atomic changes](#44-apply-atomic-changes)
- [Phase 5: Create missing skills and scripts](#phase-5:-create-missing-skills-and-scripts)
  - [5.1 Inventory references](#51-inventory-references)
  - [5.2 Create missing skills](#52-create-missing-skills)
  - [5.3 Create missing scripts](#53-create-missing-scripts)
  - [5.4 Verify scripts](#54-verify-scripts)
- [Phase 6: Strict validation](#phase-6:-strict-validation)
  - [6.1 Strict checks](#61-strict-checks)
  - [6.2 Write validation report](#62-write-validation-report)
  - [6.3 Stop conditions](#63-stop-conditions)
- [Deliver](#deliver)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Copy-write frontmatter template strict validator](#copy-write-frontmatter-template-strict-validator)
- [Contract](#contract)
- [Hard Requirements](#hard-requirements)
- [Library Verification Checklist](#library-verification-checklist)
- [Phases](#phases)
- [Phase 1: Inventory](#phase-1:-inventory)
- [1.1 Discover files](#11-discover-files)
- [1.2 Parse metadata](#12-parse-metadata)
- [1.3 Triage markers](#13-triage-markers)
- [1.4 Write tentative registry](#14-write-tentative-registry)
- [Phase 2: Deduplicate](#phase-2:-deduplicate)
- [2.1 Define duplicateA duplicate is any prompt that:](#21-define-duplicatea-duplicate-is-any-prompt-that:)
- [2.2 Duplicate resolution](#22-duplicate-resolution)
- [2.3 Update references](#23-update-references)
- [2.4 Update registry](#24-update-registry)
- [Phase 3: Template extraction](#phase-3:-template-extraction)
- [3.1 Identify shared patterns](#31-identify-shared-patterns)
- [3.2 Create shared templates](#32-create-shared-templates)
- [3.3 Extract prompt-specific variants](#33-extract-prompt-specific-variants)
- [<prompt-name](#<prompt-name)
- [3.4 Register templates](#34-register-templates)
- [Phase 4: Prompt updates](#phase-4:-prompt-updates)
- [4.1 Update references](#41-update-references)
- [4.2 Canonical format](#42-canonical-format)
- [4.3 Keep templates drivable](#43-keep-templates-drivable)
- [4.4 Apply atomic changes](#44-apply-atomic-changes)
- [Phase 5: Create missing skills and scripts](#phase-5:-create-missing-skills-and-scripts)
- [5.1 Inventory references](#51-inventory-references)
- [5.2 Create missing skills](#52-create-missing-skills)
- [5.3 Create missing scripts](#53-create-missing-scripts)
- [5.4 Verify scripts](#54-verify-scripts)
- [Phase 6: Strict validation](#phase-6:-strict-validation)
- [6.1 Strict checks](#61-strict-checks)
- [6.2 Write validation report](#62-write-validation-report)
- [6.3 Stop conditions](#63-stop-conditions)
- [Deliver](#deliver)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Manage the whole `.github/prompts/` prompt lifecycle end to end: catalog, dedupe, consolidate reusable context into crisp shared markdown templates, update every affected prompt to use those templates, ensure all prompt references resolve, create any missing skills or scripts referenced by prompts, and validate the prompt inventory is clean.

## Copy-write frontmatter template strict validator

Run the strict validator on all prompt front matter. Compare each `frontmatter` block against the strict template. Collect failures: missing fields, wrong types, invalid license values, required `name/title/version/description/tags`. Report a per-file validation result.

## Contract

### Hard Requirements

- Keep `.github/prompts/` as the single source of truth for prompt files.
- Never introduce/orphan a prompt/template without wiring it through frontmatter and at least one resolvable reference.
- If a prompt references a skill/script that does not exist, stop and create it before completion.
- If a duplicate prompt is found by content or function, evaluate carefully before deletion. Keep intentional parallel domain-specific prompts when they have distinct `name`, `title`, `dependencies`, or scope.
- Do not delete files solely for structural similarity; remove only exact or near-identical duplicates after confirming no exact refs remain.

## Library Verification Checklist

- Every `.prompt.md` includes required frontmatter fields: `name`, `title`, `description`, `version`, `tags`.- `version` is semver-like and not blank.
- `tags` is a non-empty list.
- No prompt references a missing skill/script.
- No duplicate prompt by content or function remains.
- The shared templates at `templates/_shared/...` are linked from prompts and loadable.


## Phase 1: Inventory

Produce the current prompt inventory without changing files. The inventory is a working registry used throughout the pipeline.

### 1.1 Discover files

Collect every prompt artifact under `.github/prompts/`:

- `.github/prompts/*.prompt.md`
- duplicate directories under `templates/<prompt-name>/` — index `templates/_index.md` if present

### 1.2 Parse metadata

From each `*.prompt.md`, extract:

- `name`- `title`- `description`- `version`- `tags`- `dependencies`- `skills`

### 1.3 Triage markers

For each prompt, record:

- `frontmatter_valid`: yes/no- `references_exist`: yes/no- `potential_duplicate`: yes/no

### 1.4 Write tentative registry

Write or update:

- `docs/prompt-inventory.md`Include:- `last_updated`- prompt table- duplicate candidates table- dependency errors table---

## Phase 2: Deduplicate

Remove intentional duplicates and clean up after them.

### 2.1 Define duplicateA duplicate is any prompt that:

- has the same `name`- or has the same `title` ignoring case- or has identical or near-identical body content after stripping frontmatter

### 2.2 Duplicate resolution

For each duplicate pair:

- Keep the prompt with valid frontmatter and valid references- If both are valid, keep the one closer to `.github/prompts/*.prompt.md`- For each deleted duplicate, record: - deleted path - kept path - reason

### 2.3 Update references

Search all `dependencies` and bodies for references to deleted paths and rewrite them to the kept path.

### 2.4 Update registry

Update `docs/prompt-inventory.md` to mark each duplicate as:- `deleted`- `references_updated`---

## Phase 3: Template extraction

Extract repeated reusable context into crispy concise shared markdown files.

### 3.1 Identify shared patterns

Scan prompts for repeated blocks across multiple files, especially:

- frontmatter patterns- section headers- dependency blocks- skill tables- phase templates- input/output contracts- rules blocks- examples

### 3.2 Create shared templates

Create or update template files under `templates/_shared/`:

- `templates/_shared/frontmatter.md`- `templates/_shared/skills-table-core.md`- `templates/_shared/rules-core.md`- `templates/_shared/deps-core.md`- `templates/_shared/section-skeleton.md`- `templates/_shared/phases.md`- `templates/_shared/verification-checklist.md`- additional domain-specific shared files as neededEach shared file must:- be concise and scannable- contain only the reusable content- not repeat full prompt bodies- include enough context for prompts to reference/graft cleanly

### 3.3 Extract prompt-specific variants

For areas where shared content is almost the same but differs in a few fields, use placeholders instead of duplication:Example:```| `prompt-management` | <one-line purpose

> |```or```

### <prompt-name

> | Skill | Purpose |...```

### 3.4 Register templates

Update `templates/_index.md` to include at minimum:

- template path- one-line description- related prompts- required fields---

## Phase 4: Prompt updates

Make every prompt use the shared templates without breaking intent.

### 4.1 Update references

For each prompt:

- replace duplicated frontmatter/body blocks with references to `templates/_shared/...`- keep domain-specific content local- preserve triggers, names, directories, and filenames

### 4.2 Canonical format

Prompt format:- File: `.github/prompts/<name

> .prompt.md`- Frontmatter uses keys from`templates/_shared/frontmatter.md`- Outputs include: - docs or shared templates - scripts under`~/AppData/Local/hermes/scripts/` - skills under `~/AppData/Local/hermes/skills/...`

### 4.3 Keep templates drivable

Each prompt must remain directly executable as a standalone prompt file.

### 4.4 Apply atomic changes

Use `patch` for in-place updates. Use `write_file` for new files.---

## Phase 5: Create missing skills and scripts

Prompts may reference skills or scripts that do not exist. Create them.

### 5.1 Inventory references

Collect all:

- `skill:*` from prompt `dependencies` and `skills`- `prompt:*`- `tool:*`- scripts referenced by path in prompt bodies

### 5.2 Create missing skills

For each missing skill:

- create `~/AppData/Local/hermes/skills/<name>/SKILL.md`
- include minimal viable content:
- frontmatter
- when to use
- workflow
- verification checklist
- if the skill already exists elsewhere in repo, import/reference it instead

### 5.3 Create missing scripts

If no script exists for a pattern, create:

- `~/AppData/Local/hermes/scripts/<name

> .py` or `.sh`- keep it minimal and rerunnable

### 5.4 Verify scripts

Run syntax validation on every script after creation.---

## Phase 6: Strict validation

Validate the entire prompt inventory with the shared strict format.

### 6.1 Strict checks

For every `*.prompt.md`:

- frontmatter contains required fields- `tags` is non-empty- `version` is semver-like- all `prompt:*` dependencies exist- all `tool:*` dependencies are valid Hermes tools- all `skill:*` dependencies exist as Hermes skills- no orphan references

### 6.2 Write validation report

Write/update:

- `docs/prompt-validation-report.md`Report:- file count- failures by category- missing dependencies- broken references- fixed items

### 6.3 Stop conditions

Stop and block completion only if:

- a referenced skill or script is missing and cannot be created- a template file is referenced but cannot be written- a prompt cannot be loaded or parsedOtherwise continue to Phase 7.---

## Deliver

Stop only after the pipeline is complete and the registry confirms zero unresolved issues. By the end, produce:

- `docs/prompt-inventory.md`- `docs/prompt-validation-report.md`- updated `.github/prompts/*.prompt.md` files using templates- updated `templates/_shared/**`- any newly created skills/scripts under `~/AppData/Local/hermes/`- explicit status summary in the assistant responseDo not rename prompts, skill names, triggers, or dependency keys unless the user explicitly requests it.The final state must be verifiable by reading the prompt files, the registry, and the validation report.---

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
4. **Report blockers** — State when something fails.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`prompt-builder.prompt.md`](prompt-builder.prompt.md)