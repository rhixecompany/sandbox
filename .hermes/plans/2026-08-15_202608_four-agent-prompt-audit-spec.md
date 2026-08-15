# Comprehensive Audit & Enhancement of .github/prompts/*.md for Multi-Agent Support — SPEC

## Goal
Audit, standardize, enhance, and verify the entire `.github/prompts/` library (226+ prompts) to serve as the single source of truth for four AI agents: **Hermes**, **GitHub Copilot**, **OpenCode**, and **OpenAI Codex**.

## Acceptance Criteria

- [ ] **AC1 - Migration Complete**: All 226 legacy Hermes prompts either migrated to `.github/prompts/` or explicitly archived with justification; zero prompts remaining only in legacy location
- [ ] **AC2 - Zero Duplicate Bodies**: No two prompt files in `.github/prompts/` have identical body content (by SHA-256 hash of normalized body); duplicates consolidated with cross-references
- [ ] **AC3 - Standardized Frontmatter**: Every `.prompt.md` file has valid YAML frontmatter conforming to the standard schema with all four agent metadata sections (`hermes`, `copilot`, `opencode`, `codex`) populated appropriately
- [ ] **AC4 - YAML/JSON Valid**: All frontmatter YAML and any embedded JSON in prompt bodies parse without errors; `bun run check` passes on entire `.github/prompts/` directory
- [ ] **AC5 - References Resolve**: Every file reference in frontmatter (`dependencies`, `scripts`, `template` refs) and body (`templates/...`, `templates/_shared/...`) points to an existing file
- [ ] **AC6 - Agent Metadata Complete**: Each prompt has non-empty configurations for Hermes (profile, mcp_servers, context_size), Copilot (context_size, extensions), OpenCode (command, flags, compatibility), Codex (model_override, enabled)
- [ ] **AC7 - Index & Docs Accurate**: `index.md` count matches actual file count; `copilot-instructions.md` prompt library count is correct; navigation links work
- [ ] **AC8 - Lint/Format Clean**: `bun run markdownlint` and `bun run format:check` pass on all `.github/prompts/**/*.md` files; `cspell lint` passes
- [ ] **AC9 - Git Clean**: Final state has meaningful conventional commits with `[B]`/`[I]` markers; no stray `.bak`, `.backup`, `.old` files; no uncommitted changes except intentional

## Scope

### In scope
- All `.github/prompts/*.prompt.md` files (canonical library)
- Legacy Hermes prompts in `%LOCALAPPDATA%\hermes\.github\prompts\*.prompt.md` (226 files)
- Template bodies in `.github/prompts/templates/*/README.md`
- Shared templates in `.github/prompts/templates/_shared/`
- Index files: `index.md`, `_index.md`
- Enhancement tooling in `.github/prompts/.enhance/`
- Documentation references in `.github/copilot-instructions.md` and `AGENTS.md`

### Out of scope
- `.github/agents/` directory (separate from prompt library)
- `.github/instructions/` directory (separate from prompt library)
- `.github/workflows/` (CI workflows, not prompts)
- Subproject-specific prompts under `projects/*/`
- Root-level `prompts/` directory (if exists — legacy)
- Changes to shared tooling configs (ESLint, Prettier, Ruff, markdownlint, cspell) — only prompt files themselves
- MCP server configurations outside of prompt metadata

## Schema

### Canonical Frontmatter (from `templates/_shared/frontmatter-template.md`)

Every `.prompt.md` MUST have this YAML frontmatter structure:

```yaml
---
name: kebab-case-id          # Required — matches file stem
title: "Human-readable title" # Required
description: |               # Required — multi-line
  What this prompt does.
version: 1.0.0              # Required — semver
license: MIT                # Required
author: "Hermes Agent"      # Required
trigger: /<trigger>          # Required — CLI trigger, unique across library
toolsets:                    # Required — array of toolset names
  - file
  - terminal
skills:                      # Required — array of skill refs
  - skill:<skill-name>
dependencies: []             # Required — prompt/skill dependencies
formatter: default           # Required
plan: null                   # Optional — path to phases breakdown
metadata:                    # Required — all 4 agent sections
  hermes:
    profile: code-architect   # Required — profile for Hermes routing
    mcp_servers: []           # Required — MCP servers needed
    context_size: medium      # Required — small|medium|large
  copilot:
    context_size: medium      # Required
    extensions: []            # Optional — VS Code extensions
    keybinding: null          # Optional
  opencode:
    command: "opencode /<trigger>"  # Required
    flags: {}                  # Optional — CLI flags
    help: ""                   # Optional — CLI help text
  codex:
    model_override: null      # Optional — model preference
    system_prompt_id: null    # Optional
    temperature: null         # Optional
    max_tokens: null          # Optional
tags: []                      # Required — discovery tags
scripts: []                   # Optional — pre/post scripts
---
```

### Required vs Optional Fields

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | Must match file stem (kebab-case) |
| `title` | Yes | Human-readable |
| `description` | Yes | Multi-line, used for discovery |
| `version` | Yes | Semver format |
| `license` | Yes | SPDX identifier |
| `author` | Yes | |
| `trigger` | Yes | Must be unique across 226 prompts; CLI-safe |
| `toolsets` | Yes | Non-empty array |
| `skills` | Yes | Non-empty array of `skill:<name>` |
| `dependencies` | Yes | Array (can be empty) |
| `formatter` | Yes | `default`, `markdown`, `json`, `yaml`, `html` |
| `plan` | No | Path to phases breakdown |
| `metadata` | Yes | Must contain all 4 agent sections |
| `tags` | Yes | Non-empty array |
| `scripts` | No | Array of script paths |

### Agent Metadata Requirements (AC6)

| Agent | Required Fields | Notes |
|-------|----------------|-------|
| **Hermes** | `profile`, `mcp_servers`, `context_size` | Profile from: code-architect, research-analyst, creative-director, exec-assistant, patient-tutor, alexa, default |
| **Copilot** | `context_size`, `extensions` | `extensions` can be empty array |
| **OpenCode** | `command`, `flags`, `help` | `command` must be `"opencode /<trigger>"` |
| **Codex** | `model_override`, `enabled` | `model_override` can be null; `enabled` defaults to true |

### Profile Assignment Heuristic

Map prompt domain to Hermes profile:
- Code/debug/refactor/test → `code-architect`
- Research/docs/analysis → `research-analyst`
- Design/content/creative → `creative-director`
- Planning/planning/admin → `exec-assistant`
- Tutorial/teaching → `patient-tutor`
- Operations/setup/config → `alexa`
- General → `default`

### Tags Requirement

Each prompt MUST have tags including at least:
- One agent-type tag: `agent-type:hermes`, `agent-type:copilot`, `agent-type:opencode`, or `agent-type:codex`
- One domain tag: e.g., `domain:setup`, `domain:code-quality`, `domain:debugging`

## Migration Strategy (AC1)

### Phase 1: Inventory legacy prompts
- List all 226 files in `%LOCALAPPDATA%\hermes\.github\prompts\`
- Compare filenames against `.github/prompts/` library
- Categorize: already-present / missing-in-SandBox / naming-conflict

### Phase 2: Content hash comparison
- Compute SHA-256 of normalized body for each legacy prompt
- Compare against SandBox prompt bodies
- Identical bodies → skip migration (already present)
- Different bodies → migrate (append/merge or replace)

### Phase 3: Migration
- For unique legacy content: copy into corresponding SandBox prompt (if same trigger) or create new prompt file
- For naming conflicts: rename legacy file to avoid collision, or merge content
- For superseded content: archive with justification in `templates/archived/`

### Phase 4: Deduplication (AC2)
- After migration, compute SHA-256 of all bodies
- Identify exact duplicates
- Keep one canonical copy, add cross-reference note to others
- Remove duplicate files (git rm)

## Enhancement Strategy (AC3, AC4, AC6)

### Bulk frontmatter standardization approach

1. **Read existing body content** for each prompt (preserve body)
2. **Extract existing frontmatter** if present (preserve trigger, skills, dependencies, tags)
3. **Generate canonical frontmatter** per the schema above
4. **Populate 4-agent metadata** based on:
   - Hermes: profile from domain heuristic, mcp_servers from prompt content analysis, context_size from body length
   - Copilot: context_size from body length, extensions from domain (e.g., GitHub.copilot for PR prompts)
   - OpenCode: command = `"opencode /<trigger>"`, flags = {}, help = short description
   - Codex: model_override = null (defaults), temperature = 0.2 (code) or 0.7 (creative)
5. **Write updated frontmatter + original body** to each file

### Handling special cases
- **No existing frontmatter** (67 prompts): generate full canonical frontmatter, derive trigger from filename
- **Incomplete frontmatter**: fill missing fields, preserve existing valid fields
- **Duplicate frontmatter** (like comprehensive-prompt-enhancer): use second occurrence as canonical, discard first
- **Copilot-style frontmatter** (metadata with hermes/copilot/opencode/codex): upgrade to full schema, add missing fields

## Reference Integrity (AC5)

### Reference types to verify
1. `templates/_shared/<file>.md` — shared template references
2. `templates/<trigger>/README.md` — per-prompt template references
3. `../hooks/README.md` — hooks references
4. `dependencies:` frontmatter entries — prompt/skill references
5. `scripts:` frontmatter entries — script references
6. Inline markdown links: `[text](path)` — file paths

### Verification approach
- For each prompt, extract all file references (regex patterns)
- Resolve each reference relative to `.github/prompts/`
- Check target file exists
- Report broken references with file + line + reference

## Index & Docs Updates (AC7)

### `index.md` updates
- Update prompt count from "220+" to actual count after migration
- Add note about multi-agent support (4 agents)
- Update "New Prompts" section with any newly migrated prompts

### `copilot-instructions.md` updates
- Update "Prompts" count from "190+" to actual count
- Add note about Hermes/Copilot/OpenCode/Codex compatibility

### `_index.md` updates
- Update generation date
- Add count of prompts with full 4-agent metadata

## Quality Gates (AC8)

### Commands to run
```bash
# Full check
bun run check

# Individual gates
bun run markdownlint
bun run format:check
cspell lint "**/*.md"
```

### Known issues to fix
- markdownlint MD001 (heading increments) — fix heading hierarchy
- markdownlint MD004 (ul-style) — fix bullet style consistency
- cspell typos — fix or add to dictionary
- Line ending inconsistencies — enforce LF

## Git Strategy (AC9)

### Commit structure
- Builder commits: `type(prompts): [B] <description>` with `Assisted-by: OpenAI:GPT-5.6 Luna`
- Inspector commits: `chore(prompts): [I] <description>` with `Assisted-by: OpenAI:GPT-5.6 Sol`

### Commit sequence
1. `[B] migrate 226 legacy prompts from Hermes .github/prompts/`
2. `[B] deduplicate prompt bodies (SHA-256)` — if duplicates found
3. `[B] standardize frontmatter schema for 226 prompts`
4. `[B] add 4-agent metadata (hermes/copilot/opencode/codex) to all prompts`
5. `[B] fix duplicate frontmatter in comprehensive-prompt-enhancer`
6. `[B] normalize duplicate tags format`
7. `[B] verify and fix broken template references`
8. `[I] update index.md with accurate prompt count`
9. `[I] update copilot-instructions.md prompt library count`
10. `[I] update _index.md generation date`
11. `[I] run markdownlint + cspell fixes`
12. `[I] final verification: 0 issues, 0 uncommitted changes`

## Implementation Order (Phase Sequence)

Execute strictly in order:
1. **Discovery & Baseline** — inventory, count, hash all prompts
2. **Migration** (AC1) — copy/merge legacy prompts
3. **Deduplication** (AC2) — remove duplicate bodies
4. **Frontmatter Standardization** (AC3) — canonical YAML for all prompts
5. **Agent Metadata** (AC6) — populate 4-agent sections
6. **YAML/JSON Validation** (AC4) — fix parse errors
7. **Reference Integrity** (AC5) — fix broken references
8. **Index & Docs** (AC7) — update counts
9. **Quality Gates** (AC8) — lint/format/spellcheck
10. **Git Cleanup** (AC9) — commits, no backup artifacts

## Tooling

### Scripts (use existing + create as needed)
- `.enhance/analyze_prompts.py` — existing: frontmatter validation, section coverage
- `.enhance/comprehensive_enhance.py` — existing: append missing sections (IDEMPOTENT)
- `.enhance/repair_yaml_v2.py` — existing: YAML quote repair
- `.enhance/fix_prompt_artifacts.py` — existing: orphan-s, bullet-glue, dup-section
- Custom: `migrate_legacy_prompts.py` — migration + dedup (new)
- Custom: `verify_references.py` — reference integrity check (new)
- Custom: `update_frontmatter_4agent.py` — bulk 4-agent metadata addition (new)

### Validation after each phase
- Run `analyze_prompts.py --all` after frontmatter changes
- Run `comprehensive_enhance.py --dry-run` to verify idempotency
- Run `yaml.safe_load` on all files after YAML changes
- Run `bun run check` after all changes

## Open Questions / Risks

1. **Legacy prompt bodies with embedded YAML**: Some legacy prompts may have YAML in body that conflicts with frontmatter. Need per-file review for prompts with complex bodies.
2. **Trigger uniqueness**: 226 prompts must have unique triggers. Need to verify no collisions after migration.
3. **MCP server references**: Some prompts reference MCP servers that may not be configured. Should we validate MCP server existence? (Out of scope per AC, but worth flagging.)
4. **Time estimate**: This is a large task. 226 prompts × ~5 min per prompt (read, analyze, write) = ~19 hours minimum. With scripting, can reduce to ~4-6 hours for bulk operations + 2-3 hours for special cases.
