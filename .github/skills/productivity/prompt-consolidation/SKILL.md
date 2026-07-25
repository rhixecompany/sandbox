---
name: prompt-consolidation
title: Prompt Consolidation Workflow
description: Detect near-duplicate prompts, consolidate them into parameterized forms, normalize toolsets, and clean up orphaned templates. Companion to prompt-management Phase 4–6.
version: 1.0.0
author: Alexa
license: MIT
tags:
  - prompt
  - consolidation
  - dedup
  - audit
  - toolset
---

# Prompt Consolidation Workflow

Detect near-duplicate prompts (>80% body overlap), consolidate into parameterized forms, normalize toolsets, fix name consistency, and validate.

## When to Use

- A folder has prompts with near-identical Goal/Context/Inputs/Outputs/Rules sections differing only by a type variable.
- VS-Code-style toolsets (`edit/editFiles`, `runCommands`, `web/fetch`) need conversion to Hermes equivalents.
- Batch-fixing frontmatter fields (name, tags, toolsets) across 50+ prompts.
- Cleaning up orphaned template directories after a deletion pass.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `prompt-management` | Phases 4–6 for batch audit, extraction, and consolidation |
| `enhance-markdown` | Frontmatter normalization and validation |

## Workflow

### Phase 1: Inspection

1. Count files: `ls prompts/*.prompt.md | wc -l`
2. Run frontmatter validation: `validate_prompt_frontmatter.py`
3. Run dry-run validation: `dry_run_prompts.py`
4. Scan heading frequency to identify repeated patterns (Goal, Context, Phases, etc.)
5. Identify short prompts (<50 lines body) — consolidation candidates

### Phase 2: Near-Duplicate Detection

1. Compute word-level Jaccard similarity between all prompt body pairs.
2. Report pairs with similarity ≥80%.
3. For each pair/group, compare the variable sections (Phases, Requirements, Process) — if those are near-identical too, classify as consolidation candidate.
4. Distinguish genuine near-duplicates from false positives (boilerplate-only overlap).

### Phase 3: Toolset Normalization

1. For each prompt, read `toolsets:` from frontmatter.
2. Filter against known Hermes toolsets: `web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`, `search`.
3. Map VS-Code entries to Hermes equivalents:
   - `edit/editFiles` → `file`
   - `search/codebase` → `file`
   - `runCommands`, `terminalCommand` → `terminal`
   - `web/fetch` → `web`
   - `githubRepo`, `github/*` → `web` (or remove if no Hermes equivalent)
   - `openSimpleBrowser` → `web`
   - `changes`, `problems`, `todos`, `vscodeAPI`, `extensions` → remove (no Hermes equivalent)
   - `microsoft.docs.mcp`, `playwright/*` → keep as MCP tool refs
4. If after filtering no tools remain, default to `[terminal, file]`.
5. Deduplicate: remove any repeated entries in the list.

### Phase 4: Name Consistency

For each prompt, verify `name:` in frontmatter matches the filename stem (without `.prompt.md`). Fix mismatches with:

```python
# Regex replacement
re.sub(r'^name:.*$', f'name: {correct_name}', content, count=1, flags=re.MULTILINE)
```

### Phase 5: Parameterized Consolidation

1. For each group of near-duplicates, identify the variable elements.
2. Create a mapping table showing per-prompt values for each variable.
3. Create one consolidated prompt with:
   - A `## Parameters` table
   - Phases/Requirements that use `{variable}` placeholders
   - A clear trigger path
4. Delete old prompts: `git rm -f`
5. Archive orphaned template dirs to `.hermes/archived-prompt-templates/`

### Phase 6: Verification

1. Run `validate_prompt_frontmatter.py` — all pass
2. Run `dry_run_prompts.py` — all pass
3. Confirm no orphaned references: `grep -rn "old-name" prompts/`
4. Confirm zero template dirs for deleted prompts remain in `prompts/templates/`

## Pitfalls

- **Jaccard false positives**: Boilerplate sections (Rules, Inputs, Outputs) inflate similarity for prompts that are genuinely different in their execution sections. Always inspect the variable sections before consolidating.
- **Parameter explosion**: If >5 parameters differ, the consolidated prompt becomes unwieldy. Split into a smaller group or keep separate.
- **Trigger collisions**: The consolidated prompt's trigger must not collide with any remaining prompt's trigger.
- **Cross-references**: Other plan files, docs, or prompts may reference the old names. Always grep before deleting.
- **Security-gated skills**: If the parent `prompt-management` skill is security-blocked, edits to its files will fail. Add the technique as a standalone reference or umbrella skill instead.
- **VS-Code toolsets are not errors**: `dry_run_prompts.py` flags unknown toolsets as warnings, not failures. The consolidation workflow treats them as normalization targets, not errors.

## Verification Checklist

- [ ] Frontmatter validation passes (0 errors)
- [ ] Dry-run validation passes (0 errors)
- [ ] Jaccard similarity scan completed with findings documented
- [ ] Near-duplicate groups identified and classified
- [ ] VS-Code toolsets converted to Hermes equivalents
- [ ] Name mismatches fixed
- [ ] Consolidated prompt passes both validators
- [ ] Old prompts deleted with `git rm`
- [ ] Orphaned template dirs archived
- [ ] Zero stale references to old names

## Assets

- **Reference**: `references/near-duplicate-consolidation.md` — detailed technique for Jaccard similarity, mapping table pattern, and cleanup steps.
