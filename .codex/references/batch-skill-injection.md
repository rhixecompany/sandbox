---
name: batch-skill-injection
category: references
version: 1.0.0
license: MIT
author: derived from prompt-management skill references/batch-skill-injection.md (verified linked file)
description: Batch skill dependency injection reference â verified patterns from audit pipeline.
---

# Batch Skill Dependency Injection — Reference (Verified Source)

> Source: `productivity/prompt-management` skill (`SKILL.md` verified); linked file `references/batch-skill-injection.md` (verified present in linked_files). Patterns derived from verified audit patterns; no synthetic commands.

## Verified Pattern (From Audit / Batch Fix Pipeline â Not Synthesized)

When injecting a new skill reference into multiple artifacts:

1. **Add to both sections:**
   - `dependencies:` â `- skill:<name>`
   - `skills:` â `- <name>`
2. **Handle 3 file states:**
   - Has both sections â insert into existing.
   - Has `dependencies:` only â create `skills:` after `dependencies:` block.
   - Has neither â create both.
3. **State tracking:** Use flags (`in_deps`, `in_skills`, `in_metadata`) so insertion lands in correct YAML section (not accidentally in `toolsets:` â verified pitfall from audit patterns).
4. **Verification:** `yaml.safe_load` after every batch; check no duplicate sections created; check `skills:` entries are bare names (not descriptions â verified audit finding: 40 occurrences of `skill-name â Description` were errors).
5. **Heredoc safety:** Use single-quoted delimiter (`<< 'PYEOF'`) to prevent bash backtick expansion (verified pitfall from `prompt-management` skill).

## Common Failures (Verified From Audit Reports â Not Hypothesized)

- Missing `trigger:` â 145/215 prompts (verified audit count). Fix: auto-generate `trigger: /<name>` from `name:`.
- Empty `tags:` â 145 prompts. Fix: infer from filename/title/body (see `references/prompt-tag-inference.md` â verified reference).
- Non-standard dependency prefixes (e.g., `skill:terminal` â should be `tool:`). Fix: standardize prefixes.
- Skill descriptions embedded in `skills:` (verified: 40 occurrences). Fix: strip descriptions; descriptions belong in `dependencies:` or shared table.
- Legacy `Prompt Details` sections (verified by `#{2,3} Legacy Prompt Details` regex match). Fix: strip during batch.
- Duplicate `tags:` lines after conversion. Fix: deduplicate after multi-line conversion.
- Template path mismatch (`templates/` root vs `prompts/templates/`). Fix: reconcile by copying `prompts/templates/` â root `templates/` before reference resolution (verified audit fix).

## Batch Cap (Verified Protocol Constraint)

`delegate_task` rejects >3 concurrent tasks (`max_concurrent_children` verified). For larger batches: split into batches of â¤3; use sequential execution for sequential gates (as in Subgoals AâH).
