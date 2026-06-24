# Prompt Migration Context Catalog

Generated: 2026-06-24
Source: `.github/prompts/`
Target: `./prompts/`

## Overview

| Metric | Value |
|--------|-------|
| Total `.prompt.md` files | 224 |
| Total supporting `.md` files | 890 (templates, shared refs) |
| Source file range (by mtime) | 1.78e9 (newest) → 1.78e9 (oldest) |
| Sync state | Byte-identical — both directories mirror each other |

## Shared Template Dependencies

The following shared templates under `templates/_shared/` are referenced across prompts:

- `templates/_shared/goals.md` — Goal section patterns
- `templates/_shared/personas.md` — Persona table patterns
- `templates/_shared/personality.md` — Tone/style guidance
- `templates/_shared/phases.md` — Phase structure patterns
- `templates/_shared/best-practices.md` — Best practices blocks
- `templates/_shared/frontmatter.md` — YAML frontmatter template
- `templates/_shared/skill-refs.md` — Common skill reference table
- `templates/_shared/verification-checklist.md` — Verification checklist patterns

Per-prompt template directories (1:1 with prompt files) also exist under `templates/<prompt-name>/`.

## File-On-Disk Verification

- Source `./.github/prompts/`: 224 `.prompt.md` files confirmed on disk
- Dest `./prompts/`: 224 `.prompt.md` files confirmed on disk
- Every file in source has an identical-named counterpart in dest
- All content is byte-identical between source and dest (proven by `diff --stat` comparison)
