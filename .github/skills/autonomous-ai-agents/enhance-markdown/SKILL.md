---
name: enhance-markdown
title: Enhance Markdown
description: Auditing, enhancing, and normalizing markdown/prompt files. Use for batch `.md`/`.txt`→`.markdown`, frontmatter fixes, and folder/glob processing.
version: 1.3.0
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

# Enhance Markdown

Four-phase auditor/renormalizer: catalog, audit, fix, verify. Supports single-file, TXT→MD, Hermes normalization, batch file/folder/glob modes.

## When to Use

- Audit/upgrade `.md` or prompt files
- Batch convert `.txt`→`.markdown`
- Normalize prompt files across Hermes/Copilot/OpenCode
- Triggers: `/enhance-markdown`, `enhance markdown`

## Modes

| Mode | Trigger | Notes |
|------|---------|-------|
| Audit | file path | Infer purpose from `tags`/heading/filename |
| TXT→MD | `--txt-to-md` | See `references/txt-to-md-pipeline.md` |
| Hermes Normalize | prompt family | See `references/hermes-prompt-normalization.md` |
| Batch | `--batch` | Explicit file list |
| Folder | `--folder` | Recursive `**/*.md` by default |
| Glob | `--glob` | Pattern filter |

## Usage

```bash
/enhance-markdown path/to/file.md                      # single file
/enhance-markmark --txt-to-md Prompts/my.txt            # single txt
/enhance-markdown --batch a.prompt.md b.prompt.md      # explicit list
/enhance-markdown --folder Prompts/ --pattern "*.prompt.md"
/enhance-markdown --glob "Prompts/*.prompt.md"
```

Purpose resolution: explicit arg → frontmatter/heading slug → filename stem. Slug-ify: lowercase, replace spaces/`_` with `-`, strip non-alphanumeric except `-`, truncate 40 chars.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `plans-and-specs` | Fix plan creation/management |
| `systematic-debugging` | Audit root-cause analysis |
| `writing-plans` | Companion fix-plan markdown |
| `verification-before-completion` | Independent verification |
| `skill-judge` | Post-fix quality evaluation |

## Subagents

| Profile | Role |
|---------|------|
| `research-analyst` | Dependency scan + batch audit |
| `code-architect` | Fix planning + application |
| `exec-assistant` | Readiness + orchestration |

Fallback: `delegate_task` with matching toolsets; use `execute_code` on tool-count limits.

## Artifact Map

| Artifact | Phase | Purpose |
|----------|-------|---------|
| `docs/{purpose}-context.md` | 1 | Dependency catalog |
| `docs/{purpose}-issues-context.md` | 1 | Audit findings |
| `thoughts/plans/{purpose}-debug.md` | 2 | Fix plan |
| `docs/{purpose}-fix-issues-context.md` | 2 | Fix plan + progress |
| `docs/{purpose}-verify-context.md` | 4 | Verification report |

## Multi-Command Chaining Mode

When chaining skills with `only then` constraints, execute in exact order, verify artifact dependencies, track progress in `docs/orchestrator-progress.md`, and encode the workflow in a single orchestrator prompt.

## Phase 0: Batch Discovery

Resolve target list from `--batch`, `--folder`, or `--glob`. Filter to existing files, group by `tags`/`category`/directory, and write `docs/{purpose}-batch-context.md`. Default batch size: 7.

## Phase 1: Catalog & Audit

Entry check: `docs/{purpose}-issues-context.md` exists → skip to Phase 2. Only `docs/{purpose}-context.md` exists → resume from Step 3.

1. Resolve purpose slug.
2. Two-way dependency scan: forward links/mentions/commands; reverse grep for references.
3. Write `docs/{purpose}-context.md`.
4. Batch audit in groups of 7 for formatting, structure, content.
5. Write `docs/{purpose}-issues-context.md`.

High-signal issues:
- Double frontmatter fences in first 60 lines → High
- `skills:` prose in YAML → Medium
- Merged YAML close: `---##` → split to standalone `---` + heading
- `write_file` stream timeout on >~8K-token payloads → split writes
- `toolsets:` entries that are not valid Hermes toolset names → Medium (see `references/vscode-toolset-mapping.md`)
- Orphaned thin wrappers: body <20 lines AND references a file that no longer exists → High (stale/throwaway prompt)
- Duplicate `toolsets:` entries in same frontmatter → Low (deduplicate mechanically)

## Phase 2: Fix Planning

Entry check: `thoughts/plans/{purpose}-debug.md` exists → skip to Phase 3.

1. Write fix plan to `thoughts/plans/{purpose}-debug.md`.
2. Write progress doc to `docs/{purpose}-fix-issues-context.md`.
3. Apply Batch 1 as proof-of-concept (≤7 files/issues).
4. Gate: apply fixes only; do not add new changes here.

## Phase 3: Execute Remaining Fixes

1. Apply remaining batches (≤7 files/issues each).
2. Update progress in `docs/{purpose}-fix-issues-context.md`.
3. Stop when all batches complete.

Use `execute_code` or `delegate_task` per batch. Apply the balanced trim pattern when replacing long inline sections with template references.

## Phase 4: Verify

1. Re-run parsing/audit checks on modified files.
2. Confirm zero unresolved high-severity issues.
3. **Post-consolidation orphan check** — After deleting old prompts during consolidation, verify no leftover thin wrappers reference deleted plan files or skills. Scan body text for paths under `.hermes/plans/` or `.hermes/skills/` that no longer exist.

Per-file checks:
- `yaml.safe_load` frontmatter parses as single document
- Zero double-fence repeats in first 60 lines
- No dependency-style prose in `skills:` lists
- `.prompt.md` extension used
- Trigger matches filename stem
- No merged YAML close (`---##` / `|---##`)

Fail Phase 4 if any modified file still has parse errors or high-severity issues.

## Verification Checklist

- Frontmatter has `name`, `title`, `description`, `tags`, `version`, `author`, `license`
- `metadata.hermes.related_skills` matches prerequisite skills
- All 4 phases have entry checks
- Phase 1 produces context + issues artifacts
- Phase 2 produces debug plan + fix context
- Phase 3 completes all fix batches
- Phase 4 produces verification report with zero high-severity issues
- TXT→MD reports zero cross-file gaps
- Reference files exist and substantive
- No duplicate content across sections

## Patterns

| Reference | Topic |
|-----------|-------|
| `references/ai-readiness-scoring.md` | AI-consumption scoring |
| `references/audit-detection-edge-cases.md` | False positives |
| `references/batch-frontmatter-analysis.md` | 100+ prompt scanning |
| `references/cross-skill-orchestration-pipeline.md` | enhance-markdown → skill-judge → executing-plans |
| `references/cross-system-prompt-template.md` | Cross-system templates |
| `references/doc-symmetry-validation.md` | Doc/manifest validation |
| `references/heading-hierarchy-validation.md` | Heading rules |
| `references/hermes-prompt-normalization.md` | Hermes prompt normalization |
| `references/hermes-vs-opencode-platform-guide.md` | Platform mapping |
| `references/phase1-reconstruction.md` | Deterministic Phase 1 |
| `references/phase3-reconciliation.md` | Phase 3 reconciliation |
| `references/prompt-file-debugging-patterns.md` | Prompt bug taxonomy |
| `references/prompt-file-extension-normalization.md` | `.prompts.md` → `.prompt.md` |
| `references/prompt-template-extraction.md` | Template extraction + DRY |
| `references/skills-extraction-from-prompts.md` | Skill extraction |
| `references/txt-to-md-pipeline.md` | TXT→MD pipeline |
| `references/verification-pattern.md` | Independent verification |
| `references/vscode-toolset-mapping.md` | VS Code → Hermes toolset name mapping |

---
**End of Skill**
