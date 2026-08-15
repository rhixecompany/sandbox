---
name: four-agent-prompt-audit-plan
title: Four-Agent Prompt Library Audit & Enhancement — Plan
description: Comprehensive plan to audit, standardize, enhance, and verify .github/prompts/ for Hermes, Copilot, OpenCode, and Codex
date: 2026-08-15
status: draft
---

# Four-Agent Prompt Library Audit & Enhancement — Plan

**Goal:** Audit, standardize, enhance, and verify the entire `.github/prompts/` library (226 prompts) to serve as the single source of truth for four AI agents: Hermes, GitHub Copilot, OpenCode, and OpenAI Codex.

**Current State (Discovery 2026-08-15):**
- 226 `.prompt.md` files in `.github/prompts/`
- 226 legacy Hermes prompts in `%LOCALAPPDATA%\hermes\prompts/` (same filenames, different bodies — all unique)
- 159 prompts have valid frontmatter, 67 without frontmatter
- 26 prompts have full 4-agent metadata, 131 have only Hermes metadata, 2 have partial metadata
- 0 duplicate bodies within SandBox, 0 broken YAML
- 14 shared templates in `templates/_shared/`
- 0 cross-location body duplicates (legacy bodies are all different from SandBox bodies)

---

## Phase 0: Discovery & Baseline (COMPLETED)

See discovery results above. Key findings:
- All 226 legacy prompts share filenames with SandBox prompts but have different bodies
- No content hash collisions between locations
- 67 SandBox prompts lack frontmatter entirely
- Only 26/226 (11.5%) have complete 4-agent metadata

---

## Phase 1: Frontmatter Standardisation — All 226 Prompts

**Goal:** Every `.prompt.md` gets a complete, valid YAML frontmatter with all 4 agent metadata sections.

### Step 1.1: Define the canonical frontmatter schema

Use `templates/_shared/frontmatter-template.md` as the authoritative template. Every prompt gets:

```yaml
---
name: <kebab-case-id>        # Required — matches filename stem
title: "<Human-readable>"    # Required
description: |               # Required — multi-line
  What this prompt does.
version: 1.0.0               # Required
license: MIT                 # Required
author: "Hermes Agent"      # Required
trigger: /<trigger-name>     # Required — CLI trigger
toolsets:                    # Required
  - file
  - terminal
skills:                      # Required
  - skill:<skill-name>
dependencies: []             # Required
formatter: default           # Required
plan: null                   # Optional
metadata:                    # Required — all 4 agents
  hermes:
    profile: default
    mcp_servers: []
    context_size: medium
  copilot:
    context_size: medium
    extensions: []
    keybinding: null
  opencode:
    command: "opencode /<trigger>"
    flags: {}
    help: ""
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags: []                     # Required
scripts: []                  # Optional
---
```

### Step 1.2: Read existing body content for each prompt

For each of the 226 prompts, extract:
- Existing frontmatter (if any) — preserve `trigger`, `name`, `skills`, `dependencies`, `tags` where present
- Body content — preserve as-is
- Template references — note for AC5 verification

### Step 1.3: Generate canonical frontmatter per prompt

For each prompt, populate the canonical schema:
- **name**: from filename stem (or existing frontmatter `name`)
- **title**: from existing frontmatter or derive from filename
- **description**: from existing frontmatter or "Auto-generated prompt for <trigger>"
- **trigger**: from existing frontmatter or `/<name>`
- **toolsets**: default `["file", "terminal"]` — refine per prompt type
- **skills**: from existing frontmatter or `[]`
- **dependencies**: from existing frontmatter or `[]`
- **formatter**: `default`
- **metadata.hermes**: `profile: default`, `mcp_servers: []`, `context_size: medium`
- **metadata.copilot**: `context_size: medium`, `extensions: []`
- **metadata.opencode**: `command: "opencode /<trigger>"`, empty flags
- **metadata.codex**: all nulls
- **tags**: from existing frontmatter or `["agent-type:hermes"]`
- **scripts**: `[]`

### Step 1.4: Write updated frontmatter to each file

Overwrite each `.prompt.md` with: new frontmatter + original body (preserved exactly).

### Step 1.5: Validation gate

- All 226 files parse with `yaml.safe_load` → 0 errors
- All 226 files have all required frontmatter fields
- All 226 files have all 4 metadata sections

**Estimate:** 4-6 hours (scripted bulk operation)

---

## Phase 2: Legacy Prompt Migration & Deduplication (AC1, AC2)

**Discovery finding:** All 226 legacy prompts share filenames with SandBox prompts but have different bodies. 0 content hash collisions.

### Step 2.1: Compare legacy vs SandBox bodies semantically

For each of the 226 legacy prompts that share a name with a SandBox prompt:
- If the legacy body is an **older version** of the SandBox body (same intent, SandBox is more complete) → skip legacy, note in report
- If the legacy body contains **unique content** not in SandBox → migrate body into SandBox prompt (append/merge)
- If the legacy body is **completely different** from SandBox → create a new prompt with a disambiguated name

### Step 2.2: Migrate unique legacy content

For legacy prompts with unique content:
- Copy body into the corresponding SandBox `.prompt.md` (if same trigger) or create new prompt
- Add proper frontmatter (from Phase 1 schema)
- Record migration in `MIGRATION_LOG.md`

### Step 2.3: Deduplicate by SHA-256 content hash (AC2)

After all migrations:
- Compute SHA-256 of normalized body for all 226+ prompts
- Identify any exact duplicate bodies
- For duplicates: keep the prompt with better frontmatter, add cross-reference note to the other
- Remove duplicate prompt files (git rm)

### Step 2.4: Verify zero prompts remain only in legacy location (AC1)

- All legacy prompts either: merged into SandBox, explicitly archived, or noted as superseded
- Archive remaining legacy-only prompts to `templates/archived/` with justification

**Estimate:** 2-3 hours

---

## Phase 3: YAML/JSON Validation & Broken Prompt Fixes (AC4)

### Step 3.1: YAML validation

```bash
python -c "import yaml; [yaml.safe_load(open(f)) for f in Path('.github/prompts').glob('*.prompt.md')]"
```

Fix any parse errors by targeted patching.

### Step 3.2: JSON validation

Scan bodies for embedded JSON blocks (````json ... ``` ` or inline `{...}`) and validate each.

### Step 3.3: Duplicate frontmatter detection

Check for prompts with duplicate YAML blocks (like `comprehensive-prompt-enhancer.prompt.md` which has frontmatter appearing twice).

### Step 3.4: Duplicate tags normalization

Flags like `typescript - prompts - enhancement - library` (spaces instead of commas) need normalization to proper YAML list format.

### Step 3.5: Run `bun run check` on `.github/prompts/`

```bash
bun run lint
bun run format:check
bun run markdownlint
bun run spellcheck
```

Fix all issues found.

**Estimate:** 1-2 hours

---

## Phase 4: Reference Integrity Verification (AC5)

### Step 4.1: Scan all file references

For every prompt, extract references to:
- `templates/_shared/<file>.md`
- `templates/<trigger>/README.md`
- `templates/<trigger>/<section].md`
- `../hooks/README.md`
- Other relative paths

### Step 4.2: Verify each reference resolves

For each extracted reference, check the target file exists.

### Step 4.3: Fix broken references

- If target moved: update path
- If target deleted: remove reference or update to valid alternative
- If reference is to a shared template that doesn't exist: create it or remove reference

### Step 4.4: Verify trigger uniqueness

Ensure no two prompts share the same `trigger:` value.

**Estimate:** 1 hour

---

## Phase 5: Agent Metadata Enrichment (AC3, AC6)

### Step 5.1: Enrich Hermes metadata

For each prompt, determine appropriate:
- `profile`: based on prompt domain (code-architect for code, research-analyst for research, etc.)
- `mcp_servers`: based on prompt needs (github for PR prompts, filesystem for file ops, etc.)
- `context_size`: small/medium/large based on prompt complexity

### Step 5.2: Enrich Copilot metadata

For each prompt:
- `context_size`: estimate based on body length
- `extensions`: which VS Code extensions are relevant (e.g., `["GitHub.copilot"]` for PR prompts)
- `keybinding`: optional, only for frequently-used prompts

### Step 5.3: Enrich OpenCode metadata

For each prompt:
- `command`: `"opencode /<trigger>"`
- `flags`: relevant CLI flags
- `help`: short description

### Step 5.4: Enrich Codex metadata

For each prompt:
- `model_override`: appropriate model for the task
- `temperature`: based on task type (0.1 for code, 0.7 for creative)
- `max_tokens`: estimate based on expected output

**Estimate:** 2-3 hours (scripted with domain-based heuristics)

---

## Phase 6: Index & Documentation Updates (AC7)

### Step 6.1: Update `index.md`

- Correct prompt count: `226+` → actual count after all changes
- Add agent coverage note: "Serves Hermes, Copilot, OpenCode, and Codex"
- List new/modified prompts

### Step 6.2: Update `copilot-instructions.md`

- Fix prompt library count: `190+` → actual count
- Add 4-agent coverage note

### Step 6.3: Update `templates/_index.md`

- Add generation date
- List all template directories

### Step 6.4: Create `MIGRATION_REPORT.md`

Document:
- How many legacy prompts were migrated vs archived
- Which prompts received new content from legacy
- Any prompts that were deduplicated
- Frontmatter statistics before/after

**Estimate:** 30 min

---

## Phase 7: Quality Gate — Lint, Format, Spellcheck (AC8)

### Step 7.1: `bun run markdownlint`

Fix all markdownlint errors in `.github/prompts/**/*.md`.

### Step 7.2: `bun run format:check`

Fix all Prettier formatting issues.

### Step 7.3: `bun run spellcheck`

Fix all cspell errors.

### Step 7.4: `bun run check` (full gate)

All four commands must pass.

**Estimate:** 1-2 hours

---

## Phase 8: Git Cleanup & Commits (AC9)

### Step 8.1: Remove backup artifacts

Ensure no `.bak`, `.backup`, `.old`, `.orig` files exist in `.github/prompts/`.

### Step 8.2: Conventional commits

Commit in logical batches:

```
feat(prompts): [B] standardize frontmatter schema for 226 prompts
fix(prompts): [B] add 4-agent metadata to 200 prompts
fix(prompts): [B] migrate unique legacy prompt content
fix(prompts): [B] fix duplicate frontmatter in comprehensive-prompt-enhancer
fix(prompts): [B] normalize duplicate tags format
fix(prompts): [B] verify and fix broken template references
docs(prompts): [I] update index.md with accurate counts
docs(prompts): [I] update copilot-instructions.md prompt count
chore(prompts): [I] run markdownlint + spellcheck fixes
```

### Step 8.3: Verify git state

- No uncommitted changes
- No stray backup files
- All changes are meaningful

**Estimate:** 30 min

---

## Phase 9: MCP Server Skills/Hooks/Quick Commands Sync

**Goal:** Ensure each MCP server has corresponding skills, hooks, and quick commands configured.

### Step 9.1: Inventory MCP servers

From `.hermes.md` and `config.yaml`, list all configured MCP servers:
- `honcho`, `ast-grep`, `code-sandbox`, `github`, `mcp-docker`, `memory`, `mindstudio`, `playwright`, `sequential-thinking`, `smithery`, `python-quality`, `tooling-lint`, `tooling-config`, `context7`, `sentry`, `tavily`, `parallel-search`, `parallel-task`, `fetch`, `filesystem`

### Step 9.2: Create/update skills for each MCP server

For each MCP server without a dedicated skill, create a SKILL.md in `~/AppData/Local/hermes/skills/mcp/<server-name>/` with:
- Server description and purpose
- Configuration details
- Common operations/workflows
- Tool listing
- Troubleshooting

### Step 9.3: Create/update hooks

For each MCP server, ensure hooks exist for:
- Health checks
- Connection validation
- Rate limit monitoring

### Step 9.4: Quick commands

Add quick command aliases for frequent MCP operations in `.github/copilot-instructions.md` and relevant skill files.

**Estimate:** 2-3 hours

---

## Phase 10: Final Verification & Report

### Step 10.1: Run full verification suite

```bash
# YAML validation
python -c "import yaml; [yaml.safe_load(open(f)) for f in Path('.github/prompts').glob('*.prompt.md')]"

# Bun check
bun run check

# Reference check
python verify_references.py .github/prompts/

# Frontmatter coverage
python check_frontmatter.py .github/prompts/
```

### Step 10.2: Verify all 9 ACs

| AC | Criteria | Status |
|----|----------|--------|
| AC1 | Zero prompts only in legacy location | ☐ |
| AC2 | Zero duplicate bodies by SHA-256 | ☐ |
| AC3 | All prompts have valid YAML with 4-agent metadata | ☐ |
| AC4 | All YAML/JSON valid, `bun run check` passes | ☐ |
| AC5 | All internal references resolve | ☐ |
| AC6 | Each prompt has non-empty Hermes/Copilot/OpenCode/Codex configs | ☐ |
| AC7 | `index.md` and `copilot-instructions.md` counts accurate | ☐ |
| AC8 | `bun run markdownlint` + `format:check` + `spellcheck` clean | ☐ |
| AC9 | Git clean, conventional commits, no backup artifacts | ☐ |

### Step 10.3: Generate final report

`PROMPT_AUDIT_REPORT.md` with:
- Phase-by-phase stats
- Before/after metrics
- Remaining open items
- Lessons learned

**Estimate:** 1 hour

---

## Total Timeline

| Phase | Steps | Estimate |
|-------|-------|----------|
| 0: Discovery | — | COMPLETED |
| 1: Frontmatter standardisation | 1.1–1.5 | 4–6 h |
| 2: Migration & dedup | 2.1–2.4 | 2–3 h |
| 3: YAML/JSON validation | 3.1–3.5 | 1–2 h |
| 4: Reference integrity | 4.1–4.4 | 1 h |
| 5: Agent metadata enrichment | 5.1–5.4 | 2–3 h |
| 6: Index updates | 6.1–6.4 | 30 min |
| 7: Quality gate | 7.1–7.4 | 1–2 h |
| 8: Git commits | 8.1–8.3 | 30 min |
| 9: MCP skills/hooks/commands | 9.1–9.4 | 2–3 h |
| 10: Final verification | 10.1–10.3 | 1 h |
| **Total** | | **~16–22 hours** |

## Parallelization Opportunities

- **Phase 1 + Phase 5** can share the same file-read pass — read all prompts once, generate frontmatter + metadata together
- **Phase 3 + Phase 7** overlap — YAML fixes inform lint fixes
- **Phase 9** is independent of Phases 1–8 and can run concurrently

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Legacy bodies are genuinely different (not older versions) | Medium | High | Phase 2 semantic comparison determines merge vs. new-prompt |
| Bulk frontmatter script corrupts bodies | Low | High | Dry-run first, verify sample, git rollback ready |
| 67 no-frontmatter prompts lose body content | Low | High | Script preserves body exactly; verify after |
| markdownlint introduces many new errors | Medium | Medium | Fix in batches, prioritize MD001/MD002/MD003 |
| MCP skill creation duplicates existing skills | Low | Low | Check skills_list before creating |
