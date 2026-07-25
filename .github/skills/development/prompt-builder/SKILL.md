---
author: Hermes Agent
description: Scaffold, generate, and build structured prompt files and prompt libraries from specifications. Works with the 9-section and 11-section templates from enforce-markdown, supports Hermes/Copilot/OpenCode cross-platform formats, and produces ready-to-use prompt artifacts.
license: MIT
metadata:
  hermes:
    tags: [imported, scaffolding, templates, library, prompt-engineering]
name: prompt-builder
tags:
- scaffolding
- templates
- library
- prompt-engineering
- scripts
title: Prompt Builder
version: 1.1.0
---

# Prompt Builder

## Description

Scaffold, generate, and build structured prompt files and prompt libraries from specifications. Works with the 9-section and 11-section templates from `enforce-markdown`, supports Hermes/Copilot/OpenCode cross-platform formats, and produces ready-to-use prompt artifacts.

## When to Use

- Scaffolding new prompt files from specifications
- Building prompt libraries from a set of requirements
- Converting feature specs into prompt definitions
- Generating starter prompts for new workflows
- Batch-creating prompts from a manifest or registry

## When NOT to Use

- Improving existing prompt content (use `prompt-engineering`)
- Auditing prompt quality (use `enhance-markdown`)
- Executing prompts (use `acpx-executor` or direct delegation)

## Goal

Generate well-structured, ready-to-use prompt files from specifications — with correct frontmatter, section ordering, and cross-platform compatibility.

## Inputs

- Prompt name, trigger, description
- Feature specifications or requirements
- Target platform (Hermes, Copilot, OpenCode, or cross-platform)
- Template choice (9-section for internal, 11-section for cross-system)

## Outputs

- Structured `.prompt.md` file with valid YAML frontmatter
- Cross-references to required skills and dependencies
- Validation report confirming structural compliance

## Rules

1. **Always include YAML frontmatter** — title, trigger, description, tags minimum
2. **Always include context-map dependency** when prompt is part of a pipeline
3. **Use 9-section template** for internal workflow prompts
4. **Use 11-section template** for cross-system commands
5. **Name section: `## Actions`** (not `Actions Summary`)
6. **Every Task must have at least one Action** — no orphaned checkboxes
7. **Validate before writing** — check structural compliance before file write

## Workflow

### Phase 1: Gather Requirements

- Collect prompt name, trigger, description
- Identify target platform(s)
- Determine template type (9-section vs 11-section)
- List required skills, dependencies, subagents

### Phase 2: Select Template

- 9-section: Goal, Context, Inputs, Outputs, Rules, Phases, Steps, Tasks, Actions
- 11-section: Adds YAML frontmatter fields, Description, Context sections with Steps/Tasks/Subtasks nesting
- Prefer 11-section when `trigger:` needs OpenCode compatibility

### Phase 3: Populate Sections

- Fill frontmatter (title first, then trigger, description, tags, dependencies)
- Write Goal as single paragraph (not blockquote)
- Extract Rules from requirements (behavioral guardrails)
- Build Phases from workflow stages
- Derive Steps from Phases
- Derive Tasks from Steps (each Task = one checkbox)
- List Actions with tool/command references

### Phase 4: Validate and Write

- Run structural validation (frontmatter, section ordering, heading levels)
- Check cross-references resolve
- Write to target path
- Report file path and size

### Phase 5: Repair an Existing Prompt (when asked to fix/repair, not create)

Common breakage pattern in this repo's `prompts/*.prompt.md` files: a "Template References"
section lists files under `templates/<prompt-name>/` that don't exist (or has typos /
duplicate headers). Repair steps:

1. **Materialize the template dir** per the repo DRY convention in `prompts/templates/_index.md`:
   each `.prompt.md` gets a `templates/<prompt-name>/` folder holding extracted long
   sections (sections >40 lines) plus a `README.md` inventory. Create one file per
   referenced name.
2. **Fix the referencing block** in the `.prompt.md`:
   - Remove duplicate headers (e.g. two `## Template References` blocks).
   - Correct filename typos to match the created files exactly.
   - Add a `README.md` entry to the list.
3. **Front-matter hygiene**: dedupe repeated toolset entries (e.g. `- search` listed twice
   in the `toolsets:` list). Each toolset must appear once.
4. **Verify every referenced path resolves** — `search_files` the `templates/<prompt-name>/`
   dir and confirm file count == referenced count; re-read the `.prompt.md` to confirm
   no leftover typo'd names or duplicate headers remain.

## Usage Examples

```bash
# Scaffold a new prompt
prompt-builder --name "my-workflow" --trigger "run my workflow" --platform hermes

# Build from manifest
prompt-builder --manifest prompt-manifest.json --out-dir prompts/

# Dry run to preview
prompt-builder --name "test" --dry-run
```

## Error Handling

- **Missing template:** Exits with code 1, lists available templates
- **Invalid frontmatter:** Exits with code 2, shows validation errors
- **Cross-reference unresolved:** Warns but continues, logs unresolved refs
- **Dry-run mode:** Uses `--dry-run` flag, outputs plan without writing files

## Verification Checklist

- [ ] Prompt name, trigger, description collected
- [ ] Target platform confirmed (Hermes/Copilot/OpenCode)
- [ ] Template type selected (9-section vs 11-section)
- [ ] YAML frontmatter valid
- [ ] Section ordering correct
- [ ] Cross-references resolve
- [ ] File written to target path

## Skills Required

| Skill | Purpose |
|-------|---------|
| `enhance-markdown` | Template application and structure rules |
| `writing-plans` | Structuring specifications |
| `systematic-debugging` | Validating structural compliance |
| `simplify` | Keeping output crisp |

## Related Skills

- `enhance-markdown` — Template application and structure rules
- `writing-plans` — Structuring specifications
- `systematic-debugging` — Validating structural compliance
- `simplify` — Keeping output crisp

## Pitfalls

- Start from a template, not blank
- Reuse existing prompt patterns over inventing new structures
- Always cross-link to `context-map` when part of a pipeline
- Keep Actions specific (named tools, not generic descriptions)
- Use Subtasks section only when Tasks need further decomposition
- **Dedup toolset lists**: a `toolsets:` block with the same entry twice (e.g. `- search`
  appears twice) is a real defect — each toolset must appear once.
- **Verify template references resolve**: when a prompt's "Template References" lists
  `templates/<name>/<file>.md`, that file MUST exist. Missing dirs/typos are the #1
  breakage in this repo's prompt library — materialize them (Phase 5), don't leave dangling
  links. Convention lives in `prompts/templates/_index.md` (per-prompt folder + `README.md`).
- **Watch for duplicate section headers**: copy-paste edits can leave two `## Template
  References` (or similar) blocks — collapse to one.

## References

- `references/prompt-templates.md` — 9-section and 11-section templates with examples
- `references/cross-platform-frontmatter.md` — Frontmatter field compatibility matrix
- `references/validation-rules.md` — Structural validation rules and common failures
- Repair workflow (template-dir materialization + front-matter hygiene) is inline in
  Workflow → Phase 5 and Pitfalls above.