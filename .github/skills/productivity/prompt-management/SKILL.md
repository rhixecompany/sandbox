---
author: Alexa (via OWL)
description: Guidelines and automation for creating, updating, and executing comprehensive
  prompts with plans‑and‑specs, scripts, profiles, personalities, skills, tools, and
  personas.
license: MIT
metadata:
  hermes:
    related_skills:
    - skill-creator
    - writing-skills
    tags:
    - prompt
    - workflow
name: prompt-management
tags:
- prompt
- workflow
- creation
- update
- execution
- plans-and-specs
- automation
title: Prompt Management Workflow
version: 1.2.0

---

# Prompt Management Workflow

## Overview
A *prompt* in Hermes is an artifact that packages **all** execution context needed to run a reproducible task:
- **Plans‑and‑Specs** – high‑level design, success criteria, data flow.
- **Scripts** – executable code (Python, TypeScript, Bash) stored in `scripts/`.
- **Profiles** – Hermes profile selection (model, provider, toolsets).
- **Personalities** – tone/voice settings (`hermes profile set personality`).
- **Skills** – reusable sub‑tasks referenced from `skills/`.
- **Tools** – toolset declarations (e.g., `toolsets: [terminal, file, web]`).
- **Personas** – optional role‑based behaviour overrides.

The skill defines four *modes*:
| Mode | Intent | Interaction |
|------|--------|-------------|
| **Create** | Build a brand‑new prompt from scratch. | Interactive questionnaire – the user is asked for each component.
| **Update** | Refactor an existing prompt. | Read the prompt, its referenced files, then ask clarifying questions before applying changes.
| **Execute** | Run a prompt fully. | Orchestrates sub‑agents via `delegate_task` to provide context, data, and environment.
| **Batch Audit & Enhance** | Fix systemic issues across an entire prompt directory. | Write a Python fix script, run in batches of N files (default 7), verify each batch.

## Rules (Non‑Negotiable)
1. **Always start with `using-superpowers`** – verified at session start.
2. **Never modify a prompt file without first reading it** (`read_file` → `patch`).
3. **All changes must be atomic** – use a single `patch` per file or `write_file` for new files.
4. **Execution must be delegated** – never run the full prompt in the main agent; spawn sub‑agents with the full context.
5. **Validate after each phase** – run the skill’s `Verification Checklist` before proceeding.
6. **No backup artefacts** – rely on Git (`git status`, `git commit`) for rollback.
7. **DRY** – shared components (templates, personas) live in `references/` and are referenced, not duplicated.

## Required Skills & Tools
| Asset | Reason |
|-------|--------|
| `skill-creator` | Scaffold the SKILL files and templates. |
| `writing-skills` | Produce concise, action‑first instructions. |
| `delegate_task` (tool) | Run sub‑agents for prompt execution. |
| `hermes profile` CLI | Switch profiles per prompt requirements. |
| `memory` tool | Persist prompt metadata when needed. |
| `terminal` tool | Validate scripts, run lint, packaging steps. |

## Workflow Details

### Phase 1 – Create Prompt (Interactive)
1. **Initialize** – `hermes profile use <profile>` (default: `default`).
2. **Prompt Scaffold** – generate `templates/prompt_template.md` (see reference). Prompt user for:
   - Prompt name & brief description.
   - Desired model/provider.
   - Toolsets required.
   - Personas / tone.
   - High‑level success criteria.
3. **Write Files** – `write_file` creates:
   - `prompts/<name>.md` (the main prompt document).
   - `scripts/<name>.<ext>` (if code supplied).
   - Optional `profiles/<name>.yaml` (profile overrides).
4. **Link References** – add YAML front‑matter with `references:` pointing to any `templates/` or `references/` files.
5. **Verify** – run `read_file` on each new file, ensure no placeholder text.
6. **Commit** – optionally `git add`/`git commit` via `terminal`.

### Phase 2 – Update Prompt
1. **Read Prompt** – `read_file` the target prompt markdown and any linked files (scripts, profiles, references).
2. **Analyse** – Extract current components (plans, scripts, toolsets, personalities).
3. **Ask Clarifying Questions** – for each missing/ambiguous element (e.g., "Do you want to change the model?", "Should the script language stay Python?").
4. **Apply Changes** – use `patch` (V4A) for targeted edits or `write_file` for full rewrites.
5. **Re‑validate** – run the **Verification Checklist** (see below).
6. **Commit** – `git commit` the modifications.

### Phase 3 – Execute Prompt
1. **Gather Context** – combine:
   - Prompt markdown.
   - All referenced scripts.
   - Profile configuration (`hermes profile show`).
   - Required data files (via `search_files` or `read_file`).
2. **Spawn Sub‑agents** – call `delegate_task` with a **goal** like:
   ```
   Run the prompt "<name>" using its full context. Provide any required data files, set the correct Hermes profile, and capture the final output.
   ```
   Include `toolsets` matching the prompt’s declared needs.
3. **Monitor** – use `process` tool to poll sub‑agent status, collect logs.
4. **Collect Result** – when the sub‑agent finishes, store the output in `results/<name>.md` and optionally `memory` for later retrieval.
5. **Report** – summarise execution, list any errors, and confirm success criteria defined in the plan.

### Phase 4 – Batch Audit & Enhance

**Use when:** a prompt library (10+ files) needs standardized frontmatter, structural fixes, or format migration. Do NOT use for single-prompt edits — that's Phase 2.

1. **Inventory** – scan the target directory, sort by mtime (oldest first), count total files.
2. **Batch-scan for issues** – run aggregate grep checks across all files:
   - Missing YAML frontmatter (`head -1`)
   - Missing required fields (`name:`, `title:`, `version:`, `tags:`, `author:`, `license:`)
   - Python-list `tags: [...]` format (convert to YAML array)
   - Mixed dep prefix formats (`command:`/`tool:` vs `skill:`)
   - `##`/`### Legacy Prompt Details` redundant sections
   - Copilot-style `agent:`/`model:`/`tools:` fields (identify, decide preserve/migrate)
3. **Write fix script** – create a Python script at `~/AppData/Local/hermes/scripts/` that:
   - Reads each file, parses YAML frontmatter
   - Applies all detected issues as programmatic fixes
   - Skips `.txt` files (raw source references)
   - Supports `--dry-run` mode for preview
   - Supports `--batch=N` for per-batch execution
   - Reports changed files and what was fixed
4. **Dry-run first** – execute with `--dry-run`, verify the fix list, fix any script bugs.
5. **Apply in batches** – run the script on all files (or per-batch if the user specified). Re-run after fixing any script issues.
6. **Verify post-fix** – re-run the aggregate scan; confirm zero files missing required fields, zero legacy sections, zero empty `tags:`.
7. **Handle edge cases**:
   - `plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md` → rename to sane name
   - `Developement.prompt.md` → rename to `development.prompt.md`
   - Empty `tags:` after `tags: []` conversion → fix with next-line check
   - `### Legacy Prompt Details` (H3) as well as `##` (H2) heading levels
   - **Multi-line `tools:` format** — Copilot prompts often write `tools:\n  [\n    "item1",\n  ]`. The fix script's get_field() only reads the first line (returns `""`), leaving an orphaned `[` block. Before conversion, detect multi-line `tools:` by checking whether the line after `tools:` starts with `[`. Collect items, remove the entire bracket block, write `toolsets:` with a YAML block list.
   - **Multi-line `tags:` format** — `tags: []\n  [` looks like an empty flow sequence with a dangling bracket continuation. Convert to proper `tags:` with `  - item` lines. Verify with `grep -A1 '^tags:'` after fix.
   - **Orphaned `[` block after conversion** — After migrating multi-line `tools:`, scan frontmatter for lines starting with `[`. Run: `awk '/^---/{c++;next} c==1 && /^\s*\[/{print FILENAME}'`
   - **Bare `toolsets:` with no value and no items** — After multi-line conversion, `toolsets:` may appear alone. Post-fix: the line after `toolsets:` must be `  - item`, `  [`, or a different field (set `toolsets: []` if truly empty).

## Verification Checklist
- [ ] Prompt markdown contains required sections: `## Plans‑and‑Specs`, `## Scripts`, `## Profile`, `## Personality`, `## Tools`, `## Personas`.
- [ ] All referenced files exist (`read_file` succeeds).
- [ ] Front‑matter lists `toolsets:` and `references:` correctly.
- [ ] Scripts pass a lint check (`terminal "python -m py_compile <script>"` for Python).
- [ ] Profile exists and is selectable (`hermes profile list`).
- [ ] No placeholder text like `TODO` remains.
- [ ] Execution sub‑agent runs without unexpected exit code (`process wait`).
- [ ] Result file created and saved under `results/`.
- [ ] **Batch audit only:** Aggregate scan shows 0 files missing `name:`, `title:`, `version:`.
- [ ] **Batch audit only:** 0 `## Legacy Prompt Details` or `### Legacy Prompt Details` sections remain.
- [ ] **Batch audit only:** 0 empty `tags:` lines (every `tags:` has `[]` or items underneath).
- [ ] **Batch audit only:** 0 orphaned `[` blocks in frontmatter (run `awk '/^---/{c++;next} c==1 && /^\s*\[/'` — should return nothing).
- [ ] **Batch audit only:** 0 bare `toolsets:` lines with no value and no block items below.
- [ ] **Batch audit only:** 0 `agent:` or `model:` fields remaining in frontmatter.
- [ ] **Batch audit only:** All `.txt` files in prompts dir left untouched.

## Pitfalls & Mitigations
| Pitfall | Mitigation |
|----------|------------|
| Missing script references | Validate with `search_files` before commit. |
| Profile mismatch (model/provider) | Explicitly set profile in the prompt front‑matter and enforce with `hermes profile use`. |
| Sub‑agent hangs | Use `process wait` with timeout and fallback to `process kill`. |
| Duplicate data in `references/` | Enforce DRY – only one source of truth, use symbolic links or relative imports. |
| Over‑broad toolset | Keep `toolsets` minimal; security‑review with `skill‑judge`. |
| Empty `tags:` from `tags: []` conversion | Check next frontmatter line: if not `  - <item>`, emit `tags: []` not bare `tags:`. |
| Mixed heading level for legacy sections | `### Legacy Prompt Details` (H3) won't match `##`-only regex. Use `#{2,3}` in the removal pattern. |
| Batch fix broke tags on files that already had YAML list format | Never `sed`-replace `tags:\n` globally — it matches valid list headers. Use Python with a lookahead check for `  -`. |
| `.txt` files in the prompt directory | Skip them — they're raw source references, not prompt markdown. Never add YAML frontmatter. |
| Running 7+ grep loops across 250+ files | Batch scans into single `grep -l` passes or use `execute_code` for bulk checks; individual `for f in *.prompt.md` loops time out.
| Multi-line `tools:` produces orphaned `[` blocks | Before converting `tools:` → `toolsets:`, check whether the value spans multiple lines (next line starts with `[`). Collect all bracket lines, remove them, write YAML block list. See `references/copilot-hermes-migration.md`.
| `tags: []` followed by `[` on next line | `tags: []` + `  [  item,  ]` is invalid YAML. Convert to `tags:` with `  - item` block list. Do NOT conflate with valid `tags: []` + `  - item` which most parsers handle.
| Copilot `agent:`/`model:` fields survive conversion | Verify zero `^agent:` / `^model:` lines remain after fix. These are not Hermes fields and can silently override profile selection.

## Assets
- **Template**: `templates/prompt_template.md` (skeleton with all sections).
- **Template**: `templates/plans_and_specs_template.md` (Plans‑and‑Specs section).
- **Template**: `templates/script_template.md` (Scripts section).
- **Template**: `templates/persona_template.md` (Personas section).
- **Template**: `templates/profile_template.md` (Profile section).
- **Reference**: `references/prompt_workflow.md` (detailed diagram of the four phases).
- **Reference**: `references/prompt_library_integration.md` (library reuse guide).
- **Reference**: `references/prompt-batch-audit-pattern.md` (batch audit workflow with common frontmatter issues and fix-script structure).
- **Reference**: `references/copilot-hermes-migration.md` (field mapping, multi-line format detection, orphaned bracket fix).
- **Script**: `scripts/validate_prompt_frontmatter.py` (CI front‑matter validation).
- **Script**: `scripts/dry_run_prompts.py` (smoke test for prompt dependencies).
- **Script**: `scripts/generate_prompt_changelog.py` (auto changelog on push).
- **Script**: `scripts/sync_prompt_library.py` (scheduled external library sync).
- **Script**: `~/AppData/Local/hermes/scripts/fix_prompts.py` (reusable batch fix script for prompt frontmatter, tags, legacy sections, dep prefixes — supports `--dry-run` and `--batch=N`).
- **Script**: `~/AppData/Local/hermes/scripts/fix_orphaned_brackets.py` (one-pass cleanup of orphaned `[` blocks after multi-line tools conversion — detect bracket block, extract items, write YAML block list under `toolsets:`).
- **CI Workflow**: `.github/workflows/prompt-validation.yml` (runs validation, lint, dry‑run, changelog, scheduled sync).

---

**Usage Example** (create a new prompt named *data‑ingest*):
```
hermes profile use default
# interactive – the skill will ask for model, toolsets, etc.
skill_view name="prompt-management"   # load the skill
# then follow the skill’s interactive steps (ask user, write files)
```

**Execution Example** (run the prompt):
```
delegate_task goal="Execute the 'data‑ingest' prompt with full context" toolsets=["terminal","file","web"]
```

---

### Maintenance
- Update the `templates/prompt_template.md` when new sections are needed.
- Run `skill-judge` quarterly to ensure compliance with global `MASTER_RULES.md`.
- When deprecating a toolset, bump the version in the front‑matter and add a migration note.

## Security & Compliance
*All prompts must*:
- Declare required permissions in the front‑matter (`permissions:`).
- Avoid embedding secrets; use `${ENV_VAR}` placeholders.
- Run a security scan (`hermes tools scan`) before committing.

## Testing & Validation
*Automated checks*:
- **Unit tests** for script files (e.g., `pytest` for Python, `bun test` for TypeScript).
- **Prompt lint** — ensure required sections exist via `skill-judge`.
- **Dry‑run** — execute the prompt in a sandbox sub‑agent with a `--dry` flag.

## Versioning & Release
*Prompt lifecycle*:
- Increment `version` in front‑matter for every change.
- Tag releases in Git (`git tag -a prompt/<name>@<version>`).
- Generate a changelog entry automatically (`scripts/generate_prompt_changelog.py`).

## Metrics & Monitoring
*Collect execution data*:
- Capture runtime logs (`results/<name>.log`).
- Store outcome metrics (success/failure, duration) in `memory` under `prompt_metrics`.
- Visualize via `hermes dashboard` widgets.

## Collaboration & Review
*Peer workflow*:
- Open a PR for each prompt change.
- Run `skill-judge` as a CI check.
- Require at least one `reviewer` approval before merge.

## Prompt Library Integration
*Reuse existing prompts*:
- See `references/prompt_library_integration.md` for detailed steps.
- Use `search_files` to discover library prompts.
- Import with `delegate_task` to copy and adapt.

## Custom Templates
*Available skeletons* (see `templates/`):
- `plans_and_specs_template.md`
- `script_template.md`
- `persona_template.md`
- `profile_template.md`

---

---

**End of Skill**