# Prompt Migration Fix Plan

## Overview

Fix 224 `.prompt.md` files by severity priority. Process in batches of 7 files (newest-first). Sync changes to `./prompts/`.

## Fix Types

| Type | Description | Count |
|------|-------------|-------|
| **A — YAML frontmatter** | Fix parse errors, missing fences, broken structures | ~64 files |
| **B — Body fence bleed** | Remove/replace `---` dividers in markdown body | 35 files |
| **C — Missing fields** | Add `trigger:`, `tags:`, `dependencies:`, `skills:`, `name:` | ~187 files |
| **D — Dependency paths** | Fix `.github/prompts/` prefix to correct relative paths | 8 issues |
| **E — Enhancement** | Add version, author, normalize cross-references | all files |

## Fix Rules

1. **Never change prompt intent or semantics** — only structural/metadata fixes
2. **For body `---` dividers**: Replace with `---` (no change) OR wrap in comments. The `---` themselves may be intentional HRs — keep them but ensure they don't break frontmatter parsing. The real fix is ensuring frontmatter is properly delimited.
3. **For `.github/prompts/` prefix in deps**: Change to `../.github/prompts/` so the path resolves from `./prompts/`
4. **For missing fields**: Only add when the value can be confidently inferred from content
5. **For empty `skills:`**: Leave as `skills: []` or `skills:` on its own
