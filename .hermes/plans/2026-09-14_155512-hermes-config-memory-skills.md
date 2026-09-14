---
goal: Consolidate Hermes configuration, root context files, and authoring skills
version: 1.0
date_created: 2026-09-14
last_updated: 2026-09-14
owner: Alexa
status: Completed
tags: [hermes, config, memory, skills, migration]
---

# Goal

Safely reconcile `$HERMES_HOME/config.yaml` with its parseable backups, consolidate workspace/root context files into canonical Hermes locations, create `writing-spec`, `writing-plan`, and `writing-prompt`, and update `multi-file-change-protocol` with the requested workflow dependencies.

## Scope and decisions

- Treat `$HERMES_HOME/config.yaml` (currently schema version 44) as the authoritative current configuration; backups are evidence, not overwrite sources.
- Parse and compare all direct `config.yaml*` backups plus config snapshots under `$HERMES_HOME/backups/config/`.
- Exclude malformed/corrupt backups from merge candidates; retain them unchanged for forensic rollback.
- Use `hermes config migrate`, `hermes config check`, and targeted `hermes config get --json` for configuration writes/verification. Never write the Hermes config YAML directly.
- Search exact `SOUL.md`, `USER.md`, and `MEMORY.md` names recursively for inventory, but mutate only the explicitly requested workspace-root and Hermes-home-root files. Profile/nested memory files remain untouched.
- Merge with source markers and exact-content de-duplication. Delete only source files after the target contains their exact content and post-write checks pass.
- Create user-local skills via `skill_manage`; generated runtime artifacts belong in the user-requested `$HERMES_HOME/specs/<spec-filename>`, `$HERMES_HOME/plans/<spec-filename>`, and workspace `.github/prompts/<prompt-category>/<prompt-trigger>` folders.

## Phases and gates

### Phase 1 — Inventory and config analysis

- [x] Load applicable protocol/config/profile/skill-authoring/verification skills.
- [x] Inventory config candidates, exact context-file paths, sizes, and hashes without exposing secrets.
- [x] Compare parseable configs and record added/removed/changed paths and config versions.
- [x] Run `hermes config migrate`; capture exit code and output.

**Gate 1:** canonical config parses, migration completes, and `hermes config check` exits 0. No backup is overwritten or deleted.

### Phase 2 — Context-file consolidation

- [x] Build merged `$HERMES_HOME/SOUL.md` from current canonical content plus workspace `SOUL.md`.
- [x] Build merged `$HERMES_HOME/memories/USER.md` from existing canonical memory plus Hermes-home-root and workspace `USER.md`.
- [x] Build merged `$HERMES_HOME/memories/MEMORY.md` from existing canonical memory plus Hermes-home-root and workspace `MEMORY.md`.
- [x] Verify exact source-content inclusion, non-empty structure, and target hashes before deleting sources.
- [x] Delete only workspace-root `SOUL.md`, `USER.md`, `MEMORY.md` and Hermes-home-root `USER.md`, `MEMORY.md` as explicitly requested.

**Gate 2:** targets contain each source exactly once (or an explicit existing exact duplicate is retained once), deleted source paths are absent, and nested profile files are unchanged.

### Phase 3 — Create writing skills

- [x] Create `writing-spec`, `writing-plan`, and `writing-prompt` with valid frontmatter, triggers, workflows, references, templates, pitfalls, and verification checklists.
- [x] Document executable code-block rules and cross-platform script execution.
- [x] Validate all new SKILL.md files and supporting assets.

**Gate 3:** each skill has a complete workflow, no placeholders, and valid referenced paths.

### Phase 4 — Update multi-file protocol

- [x] Extend the protocol stack with the requested using/implementation/update/create/executing/judge/writing skill families.
- [x] Preserve existing protocol semantics and make availability gaps explicit rather than inventing installed capabilities.
- [x] Validate the updated skill frontmatter and references.

**Gate 4:** updated protocol parses and names all requested dependency families without duplicate or contradictory rules.

### Phase 5 — Final verification

- [x] Re-run `hermes config check` and targeted `hermes config get --json` checks.
- [x] Validate generated skill files, Markdown code fences, Python syntax, and TypeScript syntax where applicable.
- [x] Re-inventory exact context files and check nested profile files remain unchanged.
- [x] Run `git status --short` and report all real blockers or pre-existing failures.

**Final gate:** every acceptance criterion has command/file evidence; no claim is made for an unverified result.

## Verification evidence (2026-09-14)

- Config evidence: `.hermes/plans/config-diff-evidence-2026-09-14.md` records five candidates, three parseable versions (44/42/37), two malformed snapshots, and redacted scalar-path diffs. The active version-44 file remained authoritative; no stale backup value was copied.
- CLI: `hermes config migrate` exited 0; `hermes config check` exited 0 and reported version 44. Targeted model/fallback reads returned structured values without exposing secrets. CLI warnings about `chrome_profiles`, `opencode`, and `weather` toolsets were preserved rather than silently removed.
- Consolidation: `$HERMES_HOME/SOUL.md` is 33,663 bytes with one workspace-root source marker; canonical memory targets are 40,496 and 31,674 bytes with one home-root and one workspace-root marker each. The five requested source paths are absent. Recursive inventory still finds nested profile context files, which were not mutated.
- Skills: `writing-spec` (139 lines), `writing-plan` (103 lines), and `writing-prompt` (92 lines) have valid frontmatter, co-located references/templates, and descriptions within the 60-character index limit. The updated protocol is 125 lines, uses the >5-file trigger, and includes every requested family name plus an availability/non-fabrication rule.
- Skill availability: the installed registry exposes `create-implementation-plan`, `implementation-plan`, `update-implementation-plan`, `executing-plans`, all four requested judge names, `systematic-debugging`, and `plan-mode`. The other requested implementation-family spellings were documented as unresolved/unavailable rather than fabricated; the protocol permits canonical singular resolution when one exists.
- Integrity: no `.env` content was read into artifacts; no backup was deleted; no commit or push was performed.
