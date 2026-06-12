# prompts-md — Issues Context
Generated: 2026-06-12 Source set: `Prompts/*.md` (9 files)

## Summary

Fresh audit completed against 9 prompt files in `Prompts/`. Issues fall into three categories: (1) malformed dependency references, (2) incomplete or missing sections, (3) structural inconsistencies between files. No broken tool references were detected.

## Findings by file

### agents-fix.prompts.md

- [High] Frontmatter `skills:` section contains malformed dependency-style entries that duplicate and contradict `dependencies:`. Lines 21–30 use bullet labels like `prompt:context-map — ...` inside `skills:` instead of plain skill names. This blocks tooling that parses `skills:` as a flat list.
- [Medium] Multi-platform claim not grounded: the body references "three ecosystems" and a "three-way cross-reference table" but only Hermes and Copilot are present. Consider clarifying or removing the third ecosystem.
- [Low] Batch structure is acceptable; no other structural problems detected.

### bash-scripts-fix.prompts.md

- [High] Body references an implementation plan archive file `_archive/bash-scripts-fix.prompts.txt` (line 151) that is not known to exist in the audit; if missing, that is a stale in-body reference.
- [High] `skills:` section again contains dependency-style prose fragments instead of plain skill identifiers (lines 22–31).
- [Medium] Large doc size plus embedded 7-phase table and action blocks is acceptable, but the `phases:` section naming does not match the later numbered phases (Phase 1–4 vs 7-phase plan table).

### dev-init.prompts.md

- [High] A heading `## Phase 3` exists without any body content — this is an incomplete section.
- [Medium] References several output docs (`docs/dev-init-comprehensive-plan.md`, `docs/dev-init-spec.md`, `docs/prompts-cross-reference-registry.md`, `docs/prompt-conversion-enhancement.md`, `Bash/archive/artifacts/context-maps/dev-init.context.json`) whose existence should be verified before this prompt is used.
- [Low] Skill section is large and may create redundancy with `dependencies:` after a fix pass.

### general.prompts.md

- [Medium] Structural inconsistency versus peer prompts: `general.prompts.md` lacks the `Skills Required` / `Phases` table and numbered phase headings seen in agents-fix and bash-scripts-fix. Not broken, but makes cross-prompt tooling harder.
- [Low] No confirmed broken path references detected in the inspected content.

### prompts-fix.prompts.md

- [High] Title and description both contain the phrase "prompt prompts", which is a copy-paste/duplication slip in frontmatter.
- [High] `Skills Required` section is truncated mid-skill-list in the inspected content; the section may be incomplete.
- [Medium] Same `skills:`-as-dependency-prose pattern observed in peers.

### repo-management.prompts.md

- [Medium] Uses YAML block scalar form for `description:` and includes non-standard top-level keys (`mode: agent`, `system:`). This is internally consistent within this file, but inconsistent with the other 8 prompt files.
- [Low] Path references appear valid in inspected content.

### repo.prompts.md

- [Medium] Same non-standard YAML as repo-management (`mode: agent`, `system:` at top level).
- [Low] References are consistent in inspected content; no broken paths confirmed.

### skills-fix.prompts.md

- [High] `Skills Required` section is truncated in the inspected content; list appears to cut off mid-skill.
- [Medium] `dependencies:` and `skills:` duplication pattern present here too.

### workspace-consolidate.prompts.md

- [High] Very large single-file prompt (~498 lines) with embedded self-referential TOC and extensive example text. This increases maintenance and regeneration cost; should be considered for splitting in a later pass.
- [Medium] References project docs paths and outputs under `docs/project-docs/<name>/` that should be validated.
- [Low] Structural format overlaps with `repo-management.prompts.md`; normalize only if fixing in-batch.

## Cross-file issues

- `skills:` sections in 5 of 9 files contain dependency-style prose instead of skill identifiers; this will impede any tool that consumes the `skills:` list.
- Frontmatter style is inconsistent: two files use `mode:`/`system:`; the other seven use the older title/trigger/description/dependencies/skills form.
- Phrase duplication in frontmatter. e.g. `prompts-fix.prompts.md` says "prompt prompts".
- One file has a body-only `## Phase 3` heading with no content; one skill list is truncated.
