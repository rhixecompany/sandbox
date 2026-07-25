---
name: hermes-profiles
title: Hermes Profiles
description: 'Profile identity & state: USER.md, SOUL.md, MEMORY.md. Provider enumeration, system maintenance, toolsets, operator policies, personality, context files. Single source of truth via DRY.'
version: 2.2.0
author: Hermes Agent
license: MIT
tags:
  - imported
metadata:
  hermes:
    tags:
      - imported
---

# Hermes Profiles

Compact command + workflow reference. Detailed docs moved to `references/profile-docs.md`.

## Quick Commands

- `hermes profile list`
- `hermes profile use <name>`
- `hermes profile show <name>`
- `hermes profile create <name> --clone-from default --description "<role>"`
- `hermes profile alias <name>`
- `hermes profile export <name> > backup.tar.gz`
- `hermes profile import backup.tar.gz`
- `hermes config check`

## Workflow

### Phase 1: Discover
Confirm Hermes home, profile directories, and key files:
- default profile root: `~/AppData/Local/hermes/`
- non-default profile docs: `profiles/<name>/memories/`

### Phase 2: Validate
Check core files:
- `~/AppData/Local/hermes/memories/USER.md`
- `~/AppData/Local/hermes/SOUL.md`
- `~/AppData/Local/hermes/memories/MEMORY.md`
For non-default profiles, also check `profiles/<name>/memories/USER.md` and `SOUL.md`.

### Phase 3: Fix
Apply minimal edits:
- USER.md/MEMORY.md: update via `write_file` or `memory` batch operations
- cross-profile edits: use `cross_profile=True` when authorized
- stale model/profile: sync from `config.yaml`

### Phase 4: Verify
Run:
- `hermes config check`
- `git status --short`
- size checks: USER.md < 2000 bytes, MEMORY.md < 6000 bytes

## Rules
- default profile uses root `~/AppData/Local/hermes/`, not `profiles/default/`
- keep `memories/USER.md` compact; it is the authoritative user identity for the default profile
- prefer references over duplicated rule text
- preserve original plan files; do not delete history

## Reference
For full detail: `references/profile-docs.md`

## Pitfalls

- **None documented yet.**
- **Mass file moves require systematic path updates across docs + prompts.** When `Bash/` → `projects/Bash/`, update all references in `docs/Project_Architecture/*.md`, `prompts/*.prompt.md`, and root `AGENTS.md`/`README.md`. Use `sed -i 's|\`Bash/`|\`projects/Bash/`|g'` for inline backtick paths and `s|Bash/|projects/Bash/|g` for unquoted paths. Verify with `grep -r "Bash/" --include="*.md" . | grep -v "projects/Bash/"`.
- Add common pitfalls, edge cases, and failure modes specific to this skill.

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled
