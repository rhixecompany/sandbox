---
name: prompts-repair
title: Prompts Repair
description: Repair broken GitHub Copilot / Hermes .prompt.md files in the SandBox/prompts repo. Dedupe frontmatter, materialize missing template subdirs per the repo's DRY convention, fix doubled headers and filename typos, and fetch the awesome-copilot catalog for suggest-* execution.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - prompts
  - copilot
  - repair
  - hermes
  - templates
---

# Prompts Repair

## Description

Repair malformed or broken `.prompt.md` prompt files in the `SandBox/prompts/`
collection (GitHub Copilot + Hermes prompt format). This is the *repair*
counterpart to `prompt-builder` (which scaffolds *new* prompts).

## When to Use

- A `.prompt.md` references a `templates/<name>/` subdir that doesn't exist.
- Frontmatter lists a toolset twice, or a section header appears twice.
- The "Template References" list has filename typos or points to missing files.
- You are asked to run a `suggest-awesome-github-copilot-*` prompt and need the
  awesome-copilot skill catalog to execute it.

## When NOT to Use

- Creating a brand-new prompt from spec → use `prompt-builder`.
- Only fixing YAML frontmatter metadata fields → `prompt-fix-metadata`.

## Goal

Make every `.prompt.md` self-consistent: all referenced `templates/...` files
exist and resolve, frontmatter has no duplicates, headings are unique, and any
suggest-* prompt can be executed against the live awesome-copilot catalog.

## The Repo DRY Convention (load-bearing)

`prompts/templates/_index.md` mandates:

- Each `.prompt.md` (stem = `<name>`) SHOULD have a `templates/<name>/` folder.
- Long sections (>40 lines) are extracted there as standalone `.md` files; the
  prompt cross-references them instead of duplicating.
- Shared/reusable content lives in `templates/_shared/` (e.g. `rules-core.md`,
  `section-skeleton.md`, `frontmatter.md`).
- Each per-prompt template folder should include a `README.md` inventory.

When a prompt's "Template References" list files that are missing, **materialize
them** (write the extracted section content as a file) rather than deleting the
reference. See `references/dry-template-convention.md`.

## Common Defects (audit checklist)

1. **Duplicate frontmatter toolset** — e.g. `- search` listed twice under
   `toolsets:`. Remove the duplicate; keep one canonical entry.
2. **Missing template subdir** — "Template References" lists
   `templates/<name>/<file>.md` but the folder/file doesn't exist. Create it.
3. **Doubled section header** — two identical `## Template References` blocks
   (often from a bad merge). Collapse to one.
4. **Filename typos in reference list** — e.g. `skill_structure_requireme.md`
   → `skill_structure_requirements.md`, `version_comparison_proces.md` →
   `version_comparison_process.md`. Fix the name AND create the file (or rename
   an existing one).
5. **Broken inline links** — `templates/_shared/rules-core.md` etc. must resolve.

## Workflow

### Phase 1: Detect
- Read the target `.prompt.md`.
- Enumerate every `templates/...` reference (both inline links and the
  "Template References" list).
- `search_files(target='files')` for each referenced path to find missing ones.
- Scan frontmatter for duplicate toolset entries and duplicated `##` headers.

### Phase 2: Repair (smallest safe change set)
- Dedupe frontmatter entries (`patch` mode='replace').
- Create missing `templates/<name>/` files — extract the in-prompt section body
  into each file; add a `README.md` inventory listing each file + source line
  range.
- Collapse doubled headers; fix filename typos in the reference list.
- Verify no reference now points to a non-existent file.

### Phase 3: Verify
- Re-run `search_files` for each referenced template path → all must resolve.
- `search_files` for the duplicate pattern → 0 matches (except the legit one).
- For suggest-* prompts, fetch the catalog (below) and confirm the comparison
  table can be built.

### Phase 4: Hand off
- Report files created/fixed and the verification result. Do not commit unless
  asked.

## Fetching the awesome-copilot Catalog (for suggest-* execution)

`web_extract` on the GitHub contents API **truncates** large JSON arrays
(~310 KB). Use the API + regex, not the raw markdown dump:

```
GET https://api.github.com/repos/github/awesome-copilot/contents/skills?ref=main
```

Each directory entry is `{ "name": "<skill-name>", "type": "dir", ... }`.
Extract with regex `"name":\s*"([^"]+)"` (ignore `_url` escaped fields).
Sort + de-dup → current catalog (≈371 skills as of 2026-07).

Reusable script: `scripts/parse_copilot_catalog.py` (fetches live, or parses a
cached `api.github.com-*.md` file). See `references/awesome-copilot-catalog-fetch.md`.

## Pitfalls

- Don't *delete* a template reference just because the file is missing — the
  DRY convention wants the file created, not the link removed.
- `web_extract` truncation will silently drop the middle of the skill list;
  always use the API+regex path for a complete count.
- This repo has **no `.github/skills/`** — `suggest-awesome-github-copilot-*`
  prompts scan a Copilot skills dir that doesn't exist here. Local-skill side of
  the comparison table is legitimately empty; don't fabricate local skills.
- Pinned/bundled skills are out of scope — only repair files under `prompts/`.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `prompt-builder` | Structure rules when recreating extracted sections |
| `systematic-debugging` | Root-cause the break before patching |

## References

- `references/dry-template-convention.md` — full DRY convention from `templates/_index.md`
- `references/awesome-copilot-catalog-fetch.md` — API URL, regex, truncation note
- `scripts/parse_copilot_catalog.py` — fetch/parse the catalog deterministically
