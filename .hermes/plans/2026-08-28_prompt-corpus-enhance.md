---
title: ".github/prompts/ Corpus Enhancement"
description: "Normalize frontmatter, fix structural defects, and enhance all 226 prompts via parallel subagent batches"
date: 2026-08-28
author: Hermes Agent
status: in_progress
---

# .github/prompts/ Corpus Enhancement

## Goal

Bring all 226 `.prompt.md` files in `.github/prompts/` to a consistent, well-structured, fully-enhanced state using `convert-plaintext-to-md` (DONE for the 8 root .txt sources), `enhance-markdown` (frontmatter/structure/verification), and `enhance-prompt` (clarity/structure/intent) per skill workflows.

## Audit (2026-08-28)

| Metric | Value |
|--------|-------|
| Total `.prompt.md` files | 226 |
| Files with `name:` field | 3 |
| Files missing `name:` | 223 |
| Double frontmatter fence | 1 (`php-mcp-server-generator.prompt.md`) |
| Body lines <20 (thin) | 2 (`repo-init` 4 lines, `setup-bun-bunx` 7 lines) |
| 20-50 body lines | 1 |
| 50-200 body lines | 150 |
| 200+ body lines | 73 |
| Median body length | 174 lines |
| Longest | `setup-groq-cloud.prompt.md` (2299 lines) |
| Root `.prompt.txt` files | 8 (all already converted to `.prompt.md`) |

## Prior work preserved

- `BATCH_2_STANDARDIZATION_REPORT.md` (67 files, C–G range) — earlier schema
- `2026-08-25` convert-plaintext-to-md pass (8 root files, minimal schema)
- `.prompt.md` extension universally used — no `.prompts.md` drift

## Phases

### Phase A — Structural normalization (parallel, 9 batches of ~25 files)

For every `.prompt.md`:

1. **Frontmatter schema** (required fields, in order):
   - `name` (kebab-case from filename, no extension) — MISSING in 223
   - `title` (human-readable)
   - `description` (1-sentence, what + when)
   - `version` (X.Y.Z)
   - `author` (Hermes Agent)
   - `tags` (5–12 categorization tags)
   - `metadata` (nested hermes / copilot / opencode / codex blocks)
2. **Fix double-fence** (`php-mcp-server-generator.prompt.md`)
3. **Expand thin bodies** (`repo-init` 4→100+ lines, `setup-bun-bunx` 7→100+ lines)
4. **No content loss** — preserve all original instructions
5. **No scope creep** — don't rewrite the prompt's intent

### Phase B — Prompt enhancement (parallel, after A)

Apply `enhance-prompt` workflow to every file:

- Restructure: clear sections (Goal / Trigger / Inputs / Steps / Output / Examples)
- Resolve skill command fragments into ordered procedures
- Strip AI-puffery, vague quantifiers, promotional adjectives
- Active voice, concrete language, omit needless words
- Add missing context (prerequisites, verification, pitfalls)

### Phase C — Verify

- `yaml.safe_load` parses every frontmatter
- Zero double-fence, zero merged close fence
- All files have `name`, `title`, `description`, `version`, `author`, `tags`
- Body line distribution: 0 in <20, 0 in 20-50 (or justified)
- Final corpus report

## Execution

- **Subagent-driven-development** — fresh subagent per batch
- **Batch size**: ~25 files per subagent (9 batches for 226)
- **Toolsets per subagent**: `['file']` (read+write only, no terminal)
- **Shared config**: N/A (each subagent owns its own file set)
- **Verification**: parent runs final audit + commits

## Risk

- 2 files >2K lines (`setup-groq-cloud.prompt.md` 2300, `smithery-setup.prompt.md` 1611) — these are corpus-anomalies; subagents must use targeted `patch` not `write_file` to avoid >8K-token stream limit
- Conversion noise in `repo-init.prompt.md` (it has nested `---` from a pasted docker cleanup plan) — fix in Phase A

## Out of scope

- Don't touch `BATCH_2_STANDARDIZATION_REPORT.md`
- Don't change file extensions
- Don't move files to new directories
- Don't add new prompts (enhancement only)
