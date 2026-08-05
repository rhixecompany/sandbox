# sync-hermes-opencode Template

This directory contains the phase instructions and shared templates for the Hermes ↔ OpenCode ↔ OpenAI Codex synchronization workflow.

## Files

- `phases.md` — Detailed phase instructions with gates
- `rules-core.md` — Core synchronization rules (symlink to `_shared/rules-core.md`)
- `personas.md` — Persona templates (symlink to `_shared/personas.md`)
- `personality.md` — Personality guidelines (symlink to `_shared/personality.md`)
- `section-skeleton.md` — Workflow structure (symlink to `_shared/section-skeleton.md`)
- `best-practices.md` — Best practices (symlink to `_shared/best-practices.md`)
- `deps-core.md` — Dependency patterns (symlink to `_shared/deps-core.md`)
- `skills-table-core.md` — Skills table (symlink to `_shared/skills-table-core.md`)

## Usage

The main prompt at `.github/prompts/sync-hermes-opencode.prompt.md` references these templates. Do not edit directly — update the shared templates in `templates/_shared/` instead.

## Platforms

1. **Hermes** — Primary agent, source of truth for profiles
2. **OpenAI Codex** — Secondary, agent definitions in TOML
3. **OpenCode** — Tertiary, workspace config + agent configs
