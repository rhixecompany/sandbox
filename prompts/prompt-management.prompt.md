---
license: MIT
author: Hermes Agent
version: 1.0.0
name: prompt-management
title: Prompt Management
trigger: /prompt-management
description: List, triage, catalog, consolidate, dedupe, template, validate, and verify all .prompt.md artifacts in the prompts/ tree. Extract repeated reusable context into shared markdown, update prompts to use shared templates, create missing skills/scripts if they do not exist, and then declare the pipeline clean or continue remediation.
tags:
  - hermes
  - prompts
  - cleanup
  - template
  - validation
dependencies:
  - skill:brainstorming
  - skill:plans-and-specs
  - skill:writing-plans
  - skill:simplify
  - skill:systematic-debugging
  - skill:dispatching-parallel-agents
  - skill:subagent-driven-development
  - skill:test-driven-development
  - skill:skill-creator
  - skill:writing-skills
  - skill:test-skill
  - skill:verification-before-completion
  - prompt:context-map.prompt.md
  - prompt:update-implementation-plan.prompt.md
  - prompt:agents-fix.prompt.md
  - prompt:agents-fix.prompt.md
skills:
  - brainstorming
  - plans-and-specs
  - writing-plans
  - simplify
  - systematic-debugging
  - dispatching-parallel-agents
  - subagent-driven-development
  - test-driven-development
  - creating-skills
  - writing-skills
  - verification-before-completion
---

## Goal

Manage the whole `prompts/` prompt lifecycle end to end: catalog, dedupe, consolidate reusable context into crisp shared markdown templates, update every affected prompt to use those templates, ensure all prompt references resolve, create any missing skills or scripts referenced by prompts, and validate the prompt inventory is clean.

 

## COpy-write frontmatter template strict validator

Run the strict validator on all prompt front matter. Compare each `frontmatter` block against the strict template. Collect failures: missing fields, wrong types, invalid license values, required `name/title/version/description/tags`. Report a per-file validation result.

## Contract

### Hard Requirements

- Keep `prompts/` as the single source of truth for prompt files.
- Never introduce/orphan a prompt/template without wiring it through frontmatter and at least one resolvable reference.
- If a prompt references a skill/script that does not exist, stop and create it before completion.
- If a duplicate prompt is found by content or function, evaluate carefully before deletion. Keep intentional parallel domain-specific prompts when they have distinct `name`, `title`, `dependencies`, or scope.
- Do not delete files solely for structural similarity; remove only exact or near-identical duplicates after confirming no exact refs remain.

## Verification checklist
 - Every `.prompt.md` includes required frontmatter fields: `name`, `title`, `description`, `version`, `tags`.
 - `version` is semver-like and not blank.
 - `tags` is a non-empty list.
 - No prompt references a missing skill/script.
 - No duplicate prompt by content or function remains.
 - The shared templates at `prompts/templates/_shared/...` are linked from prompts and loadable.


## Phases

## Phase 1: Inventory

Produce the current prompt inventory without changing files. The inventory is a working registry used throughout the pipeline.

### 1.1 Discover files

Collect every prompt artifact under `prompts/`:

- `prompts/*.prompt.md`
- duplicate directories under `prompts/templates/<prompt-name>/`
- index `prompts/templates/_index.md` if present

### 1.2 Parse metadata

From each `*.prompt.md`, extract:

- `name`
- `title`
- `description`
- `version`
- `tags`
- `dependencies`
- `skills`

### 1.3 Triage markers

For each prompt, record:

- `frontmatter_valid`: yes/no
- `references_exist`: yes/no
- `potential_duplicate`: yes/no

### 1.4 Write tentative registry

Write or update:

- `docs/prompt-inventory.md`

Include:

- `last_updated`
- prompt table
- duplicate candidates table
- dependency errors table

---

## Phase 2: Deduplicate

Remove intentional duplicates and clean up after them.

### 2.1 Define duplicate

A duplicate is any prompt that:

- has the same `name`
- or has the same `title` ignoring case
- or has identical or near-identical body content after stripping frontmatter

### 2.2 Duplicate resolution

For each duplicate pair:

- Keep the prompt with valid frontmatter and valid references
- If both are valid, keep the one closer to `prompts/*.prompt.md`
- For each deleted duplicate, record:
  - deleted path
  - kept path
  - reason

### 2.3 Update references

Search all `dependencies` and bodies for references to deleted paths and rewrite them to the kept path.

### 2.4 Update registry

Update `docs/prompt-inventory.md` to mark each duplicate as:

- `deleted`
- `references_updated`

---

## Phase 3: Template extraction

Extract repeated reusable context into crispy concise shared markdown files.

### 3.1 Identify shared patterns

Scan prompts for repeated blocks across multiple files, especially:

- frontmatter patterns
- section headers
- dependency blocks
- skill tables
- phase templates
- input/output contracts
- rules blocks
- examples

### 3.2 Create shared templates

Create or update template files under `prompts/templates/_shared/`:

- `prompts/templates/_shared/frontmatter.md`
- `prompts/templates/_shared/skills-table-core.md`
- `prompts/templates/_shared/rules-core.md`
- `prompts/templates/_shared/deps-core.md`
- `prompts/templates/_shared/section-skeleton.md`
- `prompts/templates/_shared/phases.md`
- `prompts/templates/_shared/verification-checklist.md`
- additional domain-specific shared files as needed

Each shared file must:

- be concise and scannable
- contain only the reusable content
- not repeat full prompt bodies
- include enough context for prompts to reference/graft cleanly

### 3.3 Extract prompt-specific variants

For areas where shared content is almost the same but differs in a few fields, use placeholders instead of duplication:

Example:

```
| `prompt-management` | <one-line purpose> |
```

or

```
### <prompt-name>
| Skill | Purpose |
...
```

### 3.4 Register templates

Update `prompts/templates/_index.md` to include at minimum:

- template path
- one-line description
- related prompts
- required fields

---

## Phase 4: Prompt updates

Make every prompt use the shared templates without breaking intent.

### 4.1 Update references

For each prompt:

- replace duplicated frontmatter/body blocks with references to `prompts/templates/_shared/...`
- keep domain-specific content local
- preserve triggers, names, directories, and filenames

### 4.2 Canonical format

Prompt format:

- File: `prompts/<name>.prompt.md`
- Frontmatter uses keys from `prompts/templates/_shared/frontmatter.md`
- Outputs include:
  - docs or shared templates
  - scripts under `~/AppData/Local/hermes/scripts/`
  - skills under `~/AppData/Local/hermes/skills/...`

### 4.3 Keep templates drivable

Each prompt must remain directly executable as a standalone prompt file.

### 4.4 Apply atomic changes

Use `patch` for in-place updates. Use `write_file` for new files.

---

## Phase 5: Create missing skills and scripts

Prompts may reference skills or scripts that do not exist. Create them.

### 5.1 Inventory references

Collect all:

- `skill:*` from prompt `dependencies` and `skills`
- `prompt:*`
- `tool:*`
- scripts referenced by path in prompt bodies

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

- `~/AppData/Local/hermes/scripts/<name>.py` or `.sh`
- keep it minimal and rerunnable

### 5.4 Verify scripts

Run syntax validation on every script after creation.

---

## Phase 6: Strict validation

Validate the entire prompt inventory with the shared strict format.

### 6.1 Strict checks

For every `*.prompt.md`:

- frontmatter contains required fields
- `tags` is non-empty
- `version` is semver-like
- all `prompt:*` dependencies exist
- all `tool:*` dependencies are valid Hermes tools
- all `skill:*` dependencies exist as Hermes skills
- no orphan references

### 6.2 Write validation report

Write/update:

- `docs/prompt-validation-report.md`

Report:

- file count
- failures by category
- missing dependencies
- broken references
- fixed items

### 6.3 Stop conditions

Stop and block completion only if:

- a referenced skill or script is missing and cannot be created
- a template file is referenced but cannot be written
- a prompt cannot be loaded or parsed

Otherwise continue to Phase 7.

---



## Deliver

Stop only after the pipeline is complete and the registry confirms zero unresolved issues.

By the end, produce:

- `docs/prompt-inventory.md`
- `docs/prompt-validation-report.md`
- updated `prompts/*.prompt.md` files using templates
- updated `prompts/templates/_shared/**`
- any newly created skills/scripts under `~/AppData/Local/hermes/`
- explicit status summary in the assistant response

Do not rename prompts, skill names, triggers, or dependency keys unless the user explicitly requests it.

The final state must be verifiable by reading the prompt files, the registry, and the validation report.

---
