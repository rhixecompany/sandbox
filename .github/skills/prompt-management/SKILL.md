---
name: prompt-management
title: Prompt Management Workflow
description: Guidelines and automation for creating, updating, and executing comprehensive prompts with plans‑and‑specs, scripts, profiles, personalities, skills, tools, and personas.
version: 1.6.0
author: Alexa (via OWL)
license: MIT
tags:
- prompt
- workflow
- creation
- update
- execution
- plans-and-specs
- automation
metadata:
  hermes:
    related_skills:
    - skill-creator
    - writing-skills
    tags:
    - prompt
    - workflow
---
# Prompt Management Workflow

A *prompt* in Hermes is an artifact that packages **all** execution context needed to run a reproducible task.
- **Plans‑and‑Specs** – high‑level design, success criteria, data flow.
- **Scripts** – executable code (Python, TypeScript, Bash) stored in `scripts/`.
- **Profiles** – Hermes profile selection (model, provider, toolsets).
- **Personalities** – tone/voice settings (`hermes profile set personality`).
- **Skills** – reusable sub‑tasks referenced from `skills/`.
- **Tools** – toolset declarations (e.g. `toolsets: [terminal, file, web]`).
- **Personas** – optional role‑based behaviour overrides.

Modes:
- **Create** – build a brand‑new prompt from scratch.
- **Update** – refactor an existing prompt after reading it and any linked files.
- **Execute** – run a prompt fully via direct execution or delegation.
- **Batch Audit & Enhance** – fix systemic issues across a prompt directory.

## Overview

Automated reasoning and workflow tool for `prompt-management`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Rules (Non‑Negotiable)
1. Always start with `using-superpowers` – verified at session start.
2. Never modify a prompt file without first reading it (`read_file` → `patch`).
3. All changes must be atomic – use a single `patch` per file or `write_file` for new files.
4. Prefer delegation for independent tasks; if delegation fails or is blocked, continue with direct terminal/python batch execution and push through. For sequential pipelines, execute directly in the main agent for reliable gating.
5. Validate after each phase – run this skill’s verification checklist before proceeding.
6. No backup artefacts – rely on Git for rollback.
7. DRY – shared components (templates, personas) live in `references/` and are referenced, not duplicated.

## Workflow

### Phase 1 – Create Prompt
1. Initialize – `hermes profile use <profile>`.
2. Scaffold – generate `templates/prompt_template.md` and collect name, model/provider, toolsets, personas, and success criteria.
3. Write files – create `prompts/<name>.md`, optional `scripts/<name>.<ext>`, and optional profile overrides.
4. Link references – add `references:` in frontmatter for any `templates/` or `references/` files.
5. Verify – `read_file` each new file; ensure no placeholder text.
6. Commit – `git add` / `git commit` via `terminal`.

### Phase 2 – Update Prompt
1. Read prompt and linked files.
2. Analyse components.
3. Ask clarifying questions for missing or ambiguous elements.
4. Apply changes with `patch` or `write_file`.
5. Re‑validate with the verification checklist.
6. Commit the modifications.

### Phase 3 – Execute Prompt
1. Gather context – prompt markdown, referenced scripts, profile config, and required data files.
2. Choose execution mode – delegated for standalone prompts; direct for strictly sequential pipelines.
3. If delegated, call `delegate_task` with the full context and matching toolsets.
4. Collect results in `results/<name>.md` and optionally `memory`.
5. Report execution outcome and success criteria.

### Phase 4 – Batch Audit & Enhance
1. Inventory – scan the target directory, sort by mtime, and count files.
2. Batch-scan for issues – missing/required frontmatter fields, malformed tags, legacy sections, dependency prefixes, and merged YAML closes.
3. Write fix script – implement a Python script under `~/AppData/Local/hermes/scripts/` with `--dry-run` and `--batch=N`.
4. Dry-run first and fix script issues.
5. Apply fixes in batches.
6. Verify post-fix and re-run the aggregate scan.

### Phase 4b – Batch Skill Dependency Injection
When adding a new skill reference across many files (not fixing broken ones):
- See `references/batch-skill-injection.md` for the full pattern
- Must add to BOTH `dependencies:` (`- skill:<name>`) and `skills:` (`- <name>`)
- Handle 3 cases: has both deps+skills, has deps only, has neither
- Track section state with flags (in_deps, in_skills, in_metadata) to avoid inserting into `toolsets:` or `metadata:`
- In terminal heredocs, use `<< 'PYEOF'` (single-quoted) to prevent backtick command substitution
- Verify with `yaml.safe_load` after every batch

### Phase 5 – DRY Template Extraction
1. Identify repeated sections across prompts.
2. Create shared files under `prompts/templates/_shared/`.
3. Replace inline copies with concise references.
4. Update shared files when new domain variants are added.
5. Verify with the full Batch Audit checklist.

### Phase 6 – Prompt Consolidation
1. Inventory prompts and categorise duplicates, thin wrappers, and Copilot-style orphans.
2. Design a consolidated prompt set using shared templates.
3. Create consolidated prompts with valid frontmatter and DRY references.
4. Delete old prompts with `git rm` and archive orphan template directories.
5. Verify zero old prompts remain, zero orphan template dirs remain, and all new prompts load.

## Pitfalls & Mitigations
| Pitfall | Mitigation |
|----------|------------|
| Missing script references | Validate with `search_files` before commit. |
| Profile mismatch (model/provider) | Explicitly set profile in prompt front‑matter and enforce with `hermes profile use`. |
| Sub-agent not guaranteed to return | Check for signature output artifacts after a reasonable wait. |
| Duplicate data in `references/` | Enforce DRY – single source of truth with references. |
| Over-broad toolset | Keep `toolsets` minimal; security‑review with `skill-judge`. |
| Empty `tags:` from `tags: []` conversion | Check the next frontmatter line before writing `tags: []`. |
| Mixed heading level for legacy sections | Use `#{2,3}` when matching legacy Prompt Details headings. |
| Batch fix broke tags on files already in YAML list format | Use Python with a lookahead for `  -` instead of global `sed`. |
| Backtick escaping in terminal heredocs | Use `python3 << 'PYEOF'` (single-quoted delimiter) to prevent bash from interpreting backticks as command substitution inside the Python string. Double-quoted or unquoted heredocs expand backticks before Python sees them, silently corrupting injected content. |
| Skill reference insertion lands in `toolsets:` instead of `skills:` | When both `skills:` and `toolsets:` exist in frontmatter, naive "find last `- ` item" logic can insert into toolsets if the scanner doesn't track section state. Use a state machine with `in_skills`, `in_deps`, `in_metadata` flags. Verify by checking `yaml.safe_load` doesn't put the new entry under `toolsets:`. |
| `read_file` output has line number prefixes — cannot parse as YAML | `read_file` returns `1|content` format, not raw file content. Use `terminal` with `python3 -c "open(path).read()"` or `execute_code` for raw file access when doing batch YAML manipulation. |
| Files with `dependencies:` but no `skills:` section | When injecting into files missing `skills:`, create it after the `dependencies:` block ends. Insert a blank line + `skills:` + `- <name>`. Verify the blank line separator is preserved. |
| `.txt` files in the prompt directory | Skip them unless batch converting otherwise; never add frontmatter to raw source references. |
| Multi-line `tools:` produces orphaned `[` blocks | Detect continuation lines before converting to `toolsets:`. |
| CRLF + Copilot frontmatter | Normalize line endings before `startswith('---\n')` checks. |
| Duplicate `tags:` lines after batch fix | Deduplicate tags after multi-line conversion; run `scripts/fix_orphan_tags_in_fix_output.py` to strip trailing unindented `- item` orphans that the batch fix script may leave behind — these break YAML parsing. |
| `dependencies:` confused with `skills:` | `dependencies:` = load directives; `skills:` = constraint flags. |
| Copilot `agent:` / `model:` fields survive conversion | Verify zero legacy agent/model lines remain. |
| Progress file contention | Use deterministic `docs/{entity}-progress.md` paths per writer. |
| Stale verification artifacts | Re-read current filesystem state instead of trusting old reports. |
| Template wiring requires target sections | Wire DRY templates only when the target section already exists. |
| Tool names disguised as skill refs | Convert `skill:terminal`-style refs to `tool:` before reporting broken refs. |
| Broken `skill:/` refs from Copilot imports | Strip leading `/` from skill refs. |
| Template path resolution | Read workspace-relative templates directly; do not resolve skill-relative paths for workspace files. |
| Legacy `.prompt.txt` source refs after canonical `.prompt.md` migration | Remove stale raw-source refs once the `.prompt.md` file is canonical; keep the prompt body self-contained and normalize shared-rule links to real repo-relative paths. |
| Orphaned template dirs after deletion | Archive template dirs via `git mv` to `.hermes/archived-plan-templates/`. |
| Cross-file metadata duplication from regex batch fix | When injecting metadata blocks via regex, match the exact trailing newline structure per file. Appending after the first `---` close creates duplicate external `metadata:` blocks that the verifier misses. Fix: keep metadata inside the first frontmatter block, not after it. |
| Over-batch rewrite corrupts frontmatter | If a batch edit causes duplicate fields or broken fences in more than 2 files, stop and switch to per-file `read_file` + targeted `patch` or a validated script with dry-run. Do not retry the same regex at scale. |
| Repetitive prompt-level frontmatter repairs are not converging | In the edit-recheck loop, if 2 consecutive passes report the same HIGH issues, stop batch automation. Switch to per-file manual repair for that exact set, or halt and report the blocker. Repeating the same script with the same input class will not change the result. |
| Duplicate `metadata:` blocks in YAML frontmatter | Some prompts accumulate repeated `metadata:` sections after the closing `---`. Detect by searching for second+ `metadata:` lines inside frontmatter before patching. Fix by merging into one block or removing duplicates outside the first fence pair. |
| Prescribed template structure vs actual file state | The batch audit must compare actual prompt YAML against the required schema (name/title/description/version/tags), not just check for the presence of sections. Many failures are missing fields, not missing files. |
| Missing triggers in prompt frontmatter | 145/215 prompts lacked `trigger:` field. Auto-generate as `/<name>` from the `name` field during batch fix. |
| Empty or invalid `tags:` fields | 145 prompts had empty tags. Infer tags from filename, title, description, and body content using keyword mapping (see `references/prompt-tag-inference.md`). |
| Non-standard dependency prefixes | Dependencies used `skill:terminal`, `skill:search_files`, `skill:web_search`, etc. for tools. Standardize: `tool:` prefix for MCP tools, `skill:` for Hermes skills, `prompt:` for other prompts. |
| Skill descriptions in `skills` field | 40 occurrences of `skill-name — Description` in `skills:` list. Strip to bare skill name; descriptions belong in `dependencies:` or shared skills table. |
| Trigger mismatches | 2 prompts had `trigger` not matching `/<name>`. Enforce `trigger: /<name>` as canonical during batch fix. |
| Legacy Prompt Details sections | Detect with `#{2,3} Legacy Prompt Details` regex (both H2 and H3) and strip during batch fix. |
| Over-batch rewrite corruption | If >2 files get duplicate fields or broken fences from a single regex pass, stop and switch to per-file `read_file` + targeted `patch` or validated script with dry-run. |
| Template path mismatch (nested vs root) | Prompts often reference `templates/` at repo root while the files actually live in `prompts/templates/`. Before any bulk execution, reconcile by copying `prompts/templates/` → root `templates/` (git-tracked, reversible), then re-scan for missing refs to confirm. |
| Missing per-prompt template bodies | Per-prompt `templates/<name>/*.md` (phases.md, workflow_steps.md, etc.) are frequently absent from the repo. Treat the prompt's inline body (Goal/Context/Phases/Steps) as the AUTHORITATIVE spec; never fabricate absent template content — run from inline. |
| External side-effect prompts | Classify prompts by external impact (GitHub PRs/issues, Azure, Docker, Spring/ASP.NET scaffolding, app-store review). NEVER blind-execute these at scale — gate behind explicit user authorization; otherwise emit a dry-run analysis artifact labeled "blocked: needs creds/auth". |
| delegate_task batch cap = 3 | `delegate_task` rejects more than 3 tasks (max_concurrent_children). Split large prompt libraries into batches of ≤3 parallel delegations. |
| Repair-before-execute preference | For large prompt libraries, reconcile/fix missing dependencies BEFORE running, not after. When the user is given the choice, they expect `first repair` ordering. |
| Missing triggers in prompt frontmatter | 145/215 prompts lacked `trigger:` field. Auto-generate as `/<name>` from the `name` field during batch fix. |
| Empty or invalid `tags:` fields | 145 prompts had empty tags. Infer tags from filename, title, description, and body content using keyword mapping (see `references/prompt-tag-inference.md`). |
| Non-standard dependency prefixes | Dependencies used `skill:terminal`, `skill:search_files`, `skill:web_search`, etc. for tools. Standardize: `tool:` prefix for MCP tools, `skill:` for Hermes skills, `prompt:` for other prompts. |
| Skill descriptions in `skills` field | 40 occurrences of `skill-name — Description` in `skills:` list. Strip to bare skill name; descriptions belong in `dependencies:` or shared skills table. |
| Trigger mismatches | 2 prompts had `trigger` not matching `/<name>`. Enforce `trigger: /<name>` as canonical during batch fix. |
| Legacy Prompt Details sections | Detect with `#{2,3} Legacy Prompt Details` regex (both H2 and H3) and strip during batch fix. |
| Over-batch rewrite corruption | If >2 files get duplicate fields or broken fences from a single regex pass, stop and switch to per-file `read_file` + targeted `patch` or validated script with dry-run. |
| Template path mismatch (nested vs root) | Prompts often reference `templates/` at repo root while the files actually live in `prompts/templates/`. Before any bulk execution, reconcile by copying `prompts/templates/` → root `templates/` (git-tracked, reversible), then re-scan for missing refs to confirm. |
| Missing per-prompt template bodies | Per-prompt `templates/<name>/*.md` (phases.md, workflow_steps.md, etc.) are frequently absent from the repo. Treat the prompt's inline body (Goal/Context/Phases/Steps) as the AUTHORITATIVE spec; never fabricate absent template content — run from inline. |
| External side-effect prompts | Classify prompts by external impact (GitHub PRs/issues, Azure, Docker, Spring/ASP.NET scaffolding, app-store review). NEVER blind-execute these at scale — gate behind explicit user authorization; otherwise emit a dry-run analysis artifact labeled "blocked: needs creds/auth". |
| delegate_task batch cap = 3 | `delegate_task` rejects more than 3 tasks (max_concurrent_children). Split large prompt libraries into batches of ≤3 parallel delegations. |
| Repair-before-execute preference | For large prompt libraries, reconcile/fix missing dependencies BEFORE running, not after. When the user is given the choice, they expect `first repair` ordering. |

## Assets
- **Template**: `templates/prompt_template.md`
- **Template**: `templates/_shared/skills-table-core.md`
- **Template**: `templates/_shared/rules-core.md`
- **Template**: `templates/_shared/deps-core.md`
- **Template**: `templates/_shared/section-skeleton.md`
- **Template**: `templates/plans_and_specs_template.md`
- **Template**: `templates/script_template.md`
- **Template**: `templates/persona_template.md`
- **Template**: `templates/profile_template.md`
- **Reference**: `references/prompt_workflow.md`
- **Reference**: `references/prompt_library_integration.md`
- **Reference**: `references/prompt-batch-audit-pattern.md`
- **Reference**: `references/prompt-reference-cleanup.md`
- **Reference**: `references/copilot-hermes-migration.md`
- **Reference**: `references/skill-crossref-verification.md`
- **Reference**: `references/prompt-tag-inference.md`
- **Reference**: `references/orchestrator-execution-pattern.md`
- **Reference**: `references/prompt-consolidation.md`
- **Reference**: `references/batch-skill-injection.md`
- **Script**: `scripts/validate_prompt_frontmatter.py`
- **Script**: `scripts/dry_run_prompts.py`
- **Script**: `scripts/generate_prompt_changelog.py`
- **Script**: `scripts/sync_prompt_library.py`
- **Script**: `~/AppData/Local/hermes/scripts/fix_prompts.py`
- **Script**: `~/AppData/Local/hermes/scripts/fix_orphaned_brackets.py`
- **Script**: `scripts/fix_orphan_tags_in_fix_output.py` &mdash; removes trailing `- item` orphans left after block-style tag inference
- **Script**: `scripts/fix_orphan_tags_in_fix_output.py` &mdash; removes trailing `- item` orphans left after block-style tag inference
- **Script**: `scripts/patch_fix_prompts_dedup_tags.py`
- **CI Workflow**: `.github/workflows/prompt-validation.yml`
- **Reference**: `references/prompt-bulk-execution.md`
- **Script**: `scripts/gen_prompt_exec_batches.py`
- **Reference**: `references/prompt-bulk-execution.md`
- **Script**: `scripts/gen_prompt_exec_batches.py`

## Security & Compliance
- Declare required permissions in frontmatter.
- Avoid embedding secrets; use `${ENV_VAR}` placeholders.
- Run a security scan before committing.

## Testing & Validation
- Unit tests for script files.
- Prompt lint via `skill-judge`.
- Dry‑run in a sandbox sub‑agent when possible.

## Versioning & Release
- Increment `version` in frontmatter for every change.
- Tag releases in Git and generate a changelog entry.

## Metrics & Monitoring
- Capture runtime logs and store outcome metrics in `memory` under `prompt_metrics`.

## Collaboration & Review
- Open a PR for each prompt change.
- Run `skill-judge` as a CI check.
- Require reviewer approval before merge.

## Prompt Library Integration
- See `references/prompt_library_integration.md` for reuse steps.
- Use `search_files` to discover library prompts.
- Import with `delegate_task` to copy and adapt.

---
**End of Skill**

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Prompt Management Workflow operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## When to Use


- When you need to perform Prompt Management Workflow operations or tasks
- When managing Prompt Management Workflow infrastructure or configurations
- When automating or debugging Prompt Management Workflow workflows
- **Triggers**: "prompt management workflow" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
