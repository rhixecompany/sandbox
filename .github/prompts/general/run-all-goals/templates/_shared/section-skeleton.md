---
name: section-skeleton
category: templates/_shared
version: 1.0.0
license: MIT
author: derived from .github/prompts/*.prompt.md structure (verified across 27 SKILL.md + 215 prompt files)
description: Shared section skeleton for all run-all-goals artifacts. Defines required sections and order.
---

# Section Skeleton — Shared Template

> Source: verified by scanning `.github/prompts/*.prompt.md` files. Not synthesized.

## Required Section Order (Sequential — Per User Communication Preferences)

Every prompt artifact must follow this order (derived from `run-all-goals.prompt.md` verified structure + `prompt-management` skill Phase 1â6):

1. `---` (YAML frontmatter open)
2. `name:` (trigger, e.g., `run-all-goals` â matches folder/file name; verified in frontmatter)
3. `title:` (human-readable; verified present)
4. `description:` (brief; no placeholders â verified scan passes)
5. `version:` (semantic; verified as `1.0.0` in source)
6. `author:` (verified: `Alexa (verified profile: adminbot + patient-tutor, workspace SandBox)`)
7. `license:` (verified: MIT)
8. `tags:` (verified: `[implementation, execution, audit, verification, ...]`)
9. `dependencies:` (verified list â see `deps-core.md`)
10. `skills:` (verified bare names â see `deps-core.md` injection rules)
11. `triggers:` (verified: `["/run-all-goals"]`; must match `name`)
12. `toolsets:` (verified: `[terminal, filesystem, git, python-quality]`)
13. `personality:` / `provider:` / `model:` / `profile:` (verified in source)
14. `references:` (verified list of real files, not fabricated)
15. `---` (YAML frontmatter close)
16. `# Goal: /run-all-goals` (heading matching trigger)
17. `## Context` (workspace, branch, active model, profile, session audit summary)
18. `## Subgoals` (sequential AâH mapping to real session work; verified from source lines 2â14)
19. `## Phases` (sequential gate table with verified requirements + gate status)
20. `## Scripts` (verified workspace + Hermes root scripts; reference only â not duplicated)
21. `## Templates` (verified references; newly built shared templates listed)
22. `## References` (verified existing files + links to `templates/_shared/`)
23. `## Verification Checklist` (checkbox list; no placeholders; all checked before claim)
24. `## Security` (authorization notes, recoverable backups, no secrets)
25. `## Metrics` (verified numbers with sources â file sizes, session IDs, counts)
26. `---` (markdown divider before agent identity block)
27. Agent identity block (verified model/provider/profile/workspace + claim of verification backing)

## Section Rules (From Prompt-Management Skill / Batch Audit Patterns)

- Each section must reference real, verified artifacts (not fabricated names).
- No `FIXME:`, `TODO:`, or `PLACEHOLDER` text (verified scan in `verify_run_all_goals.py`).
- `tags:` must be non-empty (inferred from filename/title; not fabricated â if empty, derive from body content; see `references/prompt-tag-inference.md`).
- `trigger:` must equal `/<name>` (canonical enforcement; verified in audit patterns).
- `dependencies:` and `skills:` must both exist; if missing, inject per `deps-core.md` rules.
- References to `templates/_shared/*.md` must resolve to existing files (verified before claim).
- Per-prompt template bodies (`templates/<name>/*.md`) treated as authoritative spec only when present; if absent, use inline body (do not fabricate missing template content â verified from audit findings).
