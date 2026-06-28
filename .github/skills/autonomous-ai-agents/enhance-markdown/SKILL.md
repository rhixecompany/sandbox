---
name: enhance-markdown
title: Enhance Markdown
description: "Use when auditing and enhancing markdown files, batch converting .txt to .markdown, or normalizing prompt files for cross-system compatibility. Four-phase auditor: catalogs dependencies, audits in batches, creates dual-channel fix plans, applies fixes in batches of 7, then independently verifies. Fully resumable with entry checks at each phase."
version: 1.2.0
author: Hermes Agent
license: MIT
tags:
  - markdown
  - audit
  - enhance
  - idempotent
  - plans-and-specs
  - txt-to-md
metadata:
  hermes:
    related_skills:
      - plans-and-specs
      - systematic-debugging
      - writing-plans
      - verification-before-completion
      - skill-judge
---

## Goal

Four-phase markdown auditor and enhancer. Catalog related files, audit for issues, create and apply fix plans, then verify results. Supports single-file audit mode, batch TXT→Markdown conversion, Hermes prompt normalization, **and batch processing of multiple markdown files or folders**.

## When to Use

- Auditing and enhancing existing `.md` files
- Batch converting `.txt` prompts to structured `.markdown`
- Normalizing prompt files for cross-system compatibility (Hermes/Copilot/OpenCode)
- **Batch processing multiple markdown files or entire folders**
- **Triggers**: `/enhance-markdown`, `/enhance-markdown --batch`, `/enhance-markdown --folder`, "enhance markdown"

## Description

`/enhance-markdown` is a four-phase markdown auditor and enhancer. It builds a two-way dependency catalog (Phase 1), creates a dual-channel fix plan and applies fixes in batches of 7 (Phase 2), executes remaining plan items (Phase 3), then independently verifies all fixes (Phase 4). Supports TXT→MD batch conversion and Hermes prompt normalization modes. Fully resumable — each phase checks for existing artifacts before re-running.

## Modes

| Mode | Trigger | Reference |
|------|---------|-----------|
| Audit (default) | File path argument | Phases 1–4 below |
| TXT→MD Conversion | `--txt-to-md` | `references/txt-to-md-pipeline.md` |
| Hermes Normalization | Target is prompt family | `references/hermes-prompt-normalization.md` |
| **Batch File Processing** | `--batch file1.md file2.md ...` | Phases 1–4 (parallel) |
| **Folder Processing** | `--folder path/to/folder` | Phases 1–4 (recursive) |
| **Glob Pattern** | `--glob "Prompts/*.prompt.md` | Phases 1–4 (glob match) |

## Usage

```bash
# Single file audit (purpose inferred from frontmatter/filename)
/enhance-markdown path/to/file.md

# Explicit purpose label
/enhance-markdown path/to/file.md my-purpose-slug

# TXT → Markdown batch conversion
/enhance-markdown --txt-to-md                    # all .txt in Prompts/
/enhance-markdown --txt-to-md Prompts/my.txt     # single file

# Batch file processing (multiple explicit files)
/enhance-markdown --batch Prompts/a.prompt.md Prompts/b.prompt.md Prompts/c.prompt.md

# Folder processing (recursive, all .md files)
/enhance-markdown --folder Prompts/
/enhance-markdown --folder Prompts/ --pattern "*.prompt.md"

# Glob pattern matching
/enhance-markdown --glob "Prompts/*.prompt.md"
/enhance-markdown --glob "**/*.md"

**Pre-Flight (mandatory):** When 3+ targets or prior artifacts exist, ask the user: resume from existing artifacts, or re-run fresh?

**Purpose resolution priority:** explicit `$2` argument → frontmatter/heading slug → filename stem. Slug-ification: lowercase, spaces/`_` → `-`, strip non-alphanumeric (except `-`), truncate at 40 chars.

**For `.txt` files with YAML frontmatter:** The `title` field in frontmatter is preferred over filename stem for purpose resolution (e.g., `title: Multi-Agent Research Template` → `multi-agent-research-template`).

## Modes

| Mode | Trigger | Reference |
|------|---------|-----------|
| Audit (default) | File path argument | Phases 1–4 below |
| TXT→MD Conversion | `--txt-to-md` | `references/txt-to-md-pipeline.md` |
| Hermes Normalization | Target is prompt family | `references/hermes-prompt-normalization.md` |

## Skills Required

| Skill | Purpose |
|-------|---------|
| `plans-and-specs` | Fix plan creation and management |
| `systematic-debugging` | Audit files for issues |
| `writing-plans` | Author companion fix plan markdown |
| `verification-before-completion` | Independent verification |
| `skill-judge` | Evaluate referenced skills for quality after extraction |

## Subagents

| Profile / Agent | Role | Phase |
|----------------|------|-------|
| `research-analyst` | Dependency scanning, batch audit | 1 |
| `code-architect` | Fix planning, applying fixes | 2–3 |
| `exec-assistant` | Readiness checks, orchestration | 2–3 |

**Fallback:** `delegate_task()` with appropriate toolsets if profiles unavailable. Use `execute_code` if `delegate_task` hits tool-count limits.

## Artifact Map

| Artifact | Phase | Description |
|----------|-------|-------------|
| `docs/{purpose}-context.md` | 1 | Two-way dependency catalog |
| `docs/{purpose}-issues-context.md` | 1 | Audit findings |
| `thoughts/plans/{purpose}-debug.md` | 2 | Companion plan markdown |
| `docs/{purpose}-fix-issues-context.md` | 2 | Fix plan + progress log |
| `docs/{purpose}-verify-context.md` | 4 | Verification report |

## Multi-Command Chaining Mode

When the user chains multiple skill commands in a single instruction with "only then" constraints (e.g., "/skill-judge in batches, /update-implementation-plan the prompt file, only then /create-implementation-plan, /executing-plans"), treat this as an orchestration workflow:

1. Execute each command in the exact order specified
2. Each command must complete (with verification) before the next begins
3. If a command produces artifacts that the next command depends on, verify the artifacts exist before proceeding
4. Track progress in a shared artifact (e.g., `docs/orchestrator-progress.md`)
5. Create an orchestrator prompt file (e.g., `execute-all-prompts.prompt.md`) that encodes the full workflow with phases, verification gates, and "only then" constraints

This mode was discovered in session 2026-06-22 when the user invoked `/enhance-markdown` with a 4-step chained instruction.

**Cross-skill orchestration pipeline:** When the chain includes `/enhance-markdown --batch` → `/skill-judge --batch` → fix skills → `/executing-plans --batch`, follow the detailed pattern in `references/cross-skill-orchestration-pipeline.md`.

### Pitfall: Duplicate Skill Deletion

When the orchestrator instructs to "delete duplicate skills" (e.g., flat vs category-subdir copies):

1. **ALWAYS verify the skill exists in the category subdirectory BEFORE deleting the flat version**
2. Check: `find skills/ -name "SKILL.md" | xargs grep -l "name: <skill-name>"` — confirm ≥2 paths exist
3. If only ONE path exists, that's the only copy — DO NOT delete it
4. If the flat version is the only copy, move it to the correct category directory instead of deleting
5. After deletion, verify with `hermes skills list --source local` that the skill count decreased by the expected number

**What went wrong (2026-06-22):** The flat `mcp-coding-agent-setup/` was deleted assuming a category copy existed. It was the only copy. The skill was lost with no hub source to reinstall from.

---

## Phase 0: Batch Discovery (Batch/Folder/Glob Modes Only)

**Entry check:** If `docs/{purpose}-batch-context.md` exists → skip to Phase 1.

### Steps

1. **Discover targets** — Resolve file list from:
   - `--batch` explicit file arguments
   - `--folder` recursive scan (`**/*.md` by default, or `--pattern`)
   - `--glob` pattern matching
2. **Validate targets** — Filter existing files, skip directories, validate extensions
3. **Group by purpose** — Auto-group files by frontmatter `tags`, `category`, or directory structure
4. **Write batch context** → `docs/{purpose}-batch-context.md` with:
   - File list with resolved purposes
   - Grouping strategy
   - Phase execution order

### Batch Execution Strategy

| Strategy | When | Behavior |
|----------|------|----------|
| **Sequential** | ≤7 files, high interdependency | Process files one-by-one through all 4 phases |
| **Parallel Batches** | 8+ files, low interdependency | Process in batches of 7 through Phase 1, then Phase 2, etc. |
| **Per-File Complete** | Independent files | Run all 4 phases per file before moving to next |

**Default:** Parallel Batches of 7 (matches existing batch size)

### Pitfalls

- **Mixed purpose files** — Group by frontmatter `category` or `tags` first; don't process unrelated prompts together
- **Large folder scans** — Cap at 100 files per run; use `--pattern` to filter
- **Artifact collision** — Each file group gets unique `{purpose}` slug to isolate artifacts
- **Non-standard extensions** — Some prompt files use `.prompts.md` (plural) instead of `.prompt.md` (singular). When running batch discovery with a pattern filter, include both: `--pattern "*.prompt*.md"` or check explicitly: `ls *.prompt.md *.prompts.md 2>/dev/null`. After processing, normalize to `.prompt.md` — see `references/prompt-file-extension-normalization.md`.

---

## Phase 1: Catalog & Audit

**Entry check:** If `docs/{purpose}-issues-context.md` exists → skip to Phase 2. If only `docs/{purpose}-context.md` exists → skip to Step 1.3.

### Steps

1. **Purpose resolution** — Resolve slug via cascading priority
2. **Two-way dependency scan** — Forward: extract links, `@mentions`, `/commands`, plan namespaces. Reverse: grep for this file's path/trigger
3. **Write context catalog** → `docs/{purpose}-context.md`
4. **Batch audit** — Analyze related files in batches of 7 for: formatting, structural, content issues
5. **Write issues context** → `docs/{purpose}-issues-context.md`

**Pitfalls:**
- Double frontmatter fences (`---` appearing 3+ times in first 60 lines) → flag as High
- `skills:` dependency-style prose in YAML frontmatter → flag as Medium
- Pipe-balance false positives in code blocks → see `references/audit-detection-edge-cases.md`
- **Merged YAML closing (`---##`):** Copilot-style prompts often merge the closing `---` with the next heading: `|---## Goal`. This breaks YAML parsing. Detection: `grep -n "^---|---" *.prompt.md` — matches line where `---` is immediately followed by non-whitespace, non-pipe content. Fix: split into standalone `---` + blank line + heading.
- **`write_file` stream timeout on large markdown output:** When the TXT→MD pipeline produces a large `.md` file with YAML frontmatter + full section structure (5+ KB of content embedded in the `content` argument), the `write_file` tool call can exceed the ~8K token stream limit and silently time out. **Fix:** Keep `content` under ~8K tokens per call. For large files, reduce content density or split into multiple smaller writes. If a `write_file` times out, retry — do NOT repeat the same large payload unchanged.
- **Batch mode:** When processing multiple files, Phase 1 writes a combined `docs/{purpose}-context.md` and `docs/{purpose}-issues-context.md` with per-file sections. Use `execute_code` for parallel batch processing to avoid context limits.

## Phase 2: Fix Planning

**Entry check:** If `thoughts/plans/{purpose}-debug.md` exists → skip to Phase 3.

1. **Create dual-channel fix plan** — Plugin system (when reachable) + companion markdown fallback
2. **Write plan** → `thoughts/plans/{purpose}-debug.md`
3. **Write fix context** → `docs/{purpose}-fix-issues-context.md`
4. **Apply Batch 1** (proof-of-concept) — exactly 7 files
5. **Gate check** — If Batch 1 produces empty plan and files are clean, Phase 2 is complete

**Pitfall:** Don't skip phases just because artifacts exist — honor the user's explicit "fresh re-run" request.

**Batch mode:** Phase 2 creates a combined fix plan at `thoughts/plans/{purpose}-debug.md` with per-file fix sections. Apply fixes in batches of 7 files (or 7 issues per file in single-file mode).

**Note on batch size:** In single-file audit mode, "batch of 7" means 7 issues per batch (not 7 files). For multi-file TXT→MD conversion or batch processing, it's 7 files per batch.

## Phase 3: Execute Remaining Fixes

1. Apply remaining fix batches (7 files/issues per batch)
2. Update progress log in `docs/{purpose}-fix-issues-context.md`
3. Continue until all batches complete

**Batch mode:** Process files in parallel using `execute_code` or `delegate_task` subagents. Each subagent handles one batch of 7 files. Use `delegate_task` with toolsets `['terminal', 'file', 'skills']` for isolation.

**Balanced trim pattern:** When replacing long inline sections with template references, keep the prompt actionable without opening templates. See `references/prompt-template-extraction.md` § Phase 5 for the balanced trim rules (inline goal + step table + template ref, never bare `> Full content:`).

## Phase 4: Verify

1. Re-run parsing/audit checks on all modified files
2. Confirm zero unresolved high-severity issues
3. Write `docs/{purpose}-verify-context.md`

**Verification gate:** For each modified `.prompt.md` file (also check `.prompts.md` if non-standard extension exists):
- `yaml.safe_load` on frontmatter parses as single document
- Zero double-fence repeats in first 60 lines
- No dependency-style prose in `skills:` lists
- File uses `.prompt.md` extension (rename from `.txt` or `.prompts.md` if needed)
- Trigger matches filename stem convention
- No merged YAML closing (`---##` or `|---##` pattern — line where `---` is immediately followed by non-whitespace)

**Fail Phase 4** if any modified file still shows frontmatter parse errors or unresolved high-severity issues.

**Batch mode:** Phase 4 writes a combined `docs/{purpose}-verify-context.md` with per-file verification results. Use `execute_code` to re-run YAML parsing and regex checks across all modified files in parallel. Report aggregate: total files, passed, failed, high-severity issues remaining.

---

## Pattern Analysis References

| Reference | Topic |
|-----------|-------|
| `references/ai-readiness-scoring.md` | Quantitative AI-consumption scoring |
| `references/audit-detection-edge-cases.md` | False positive handling |
| `references/prompt-file-debugging-patterns.md` | 5-bug taxonomy for prompt files |
| `references/doc-symmetry-validation.md` | Doc set manifest validation |
| `references/hermes-vs-opencode-platform-guide.md` | Platform-specific agent mapping |
| `references/phase1-reconstruction.md` | Deterministic Phase 1 reconstruction |
| `references/cross-skill-orchestration-pipeline.md` | Cross-skill pipeline: enhance-markdown → skill-judge → executing-plans |
| `references/skills-extraction-from-prompts.md` | Extract referenced skills from .prompt.md files during batch audit |
| `references/verification-pattern.md` | Independent verification with execute_code + YAML/regex |
| `references/batch-frontmatter-analysis.md` | Batch scanning 100+ prompts for frontmatter issues |
| `references/prompt-template-extraction.md` | Extract long sections into per-prompt template directories, DRY consolidation |
| `references/prompt-file-extension-normalization.md` | Normalize `.prompts.md` → `.prompt.md`, update cross-references |

## Verification Checklist

- [ ] Frontmatter has all required fields (`name`, `title`, `description`, `tags`, `version`, `author`, `license`)
- [ ] `metadata.hermes.related_skills` lists all prerequisite skills
- [ ] Skills Required table matches `related_skills`
- [ ] All 4 phases have entry checks (resumability)
- [ ] Phase 1 produces context + issues artifacts
- [ ] Phase 2 produces debug plan + fix context
- [ ] Phase 3 completes all fix batches
- [ ] Phase 4 produces verification report with zero high-severity issues
- [ ] TXT→MD Phase 6 reports zero cross-file gaps (when applicable)
- [ ] All reference files exist and are substantive
- [ ] No duplicate content across sections (DRY)
- [ ] SKILL.md is under 250 lines
