---
title: Goal 5 — Profile Cleanup + Root Mirror
status: "in_progress"
created: 2026-09-11
applies_to: ~/AppData/Local/hermes/profiles/*
trigger_threshold: >6 file changes → load multi-file-change-protocol
---

# Goal 5 — Profile Cleanup + Root Mirror

## Decision Lock (from clarifications)

| Decision        | Value                                                                   |
| --------------- | ----------------------------------------------------------------------- |
| Sequence        | 1 → 2 → 3 → 4 → 5 (Goal 1 first, this last)                             |
| Backup strategy | Full mirror to `~/AppData/Local/hermes/profiles-backup-<ts>/<profile>/` |
| Diff before rm  | Yes, capture for review                                                 |

## Scope (17 profiles)

alexa, code-architect, creative-director, cto, default, designer, dev,
exec-assistant, ops, patient-tutor, pm, qa, research-analyst, security,
skills, +2 verified via `ls` output.

## Phase 1 — Capture Current Profile State

```bash
ls -la ~/AppData/Local/hermes/profiles/<each>/
# Record per profile: which of (skills,hooks,plugins,scripts,config.yaml,.env) exist
```

**Gate 1.1:** State table for 17 profiles.

## Phase 2 — Mirror Backup

```bash
TS=$(date +%Y%m%d_%H%M%S)
BACKUP_ROOT=~/AppData/Local/hermes/profiles-backup-$TS
mkdir -p $BACKUP_ROOT
for prof in ~/AppData/Local/hermes/profiles/*/; do
  cp -r "$prof" $BACKUP_ROOT/
done
```

**Gate 2.1:** `$BACKUP_ROOT` exists, contains all 17 profiles with full structure.

## Phase 3 — Diff Root vs Profile (informational)

```bash
for prof in ~/AppData/Local/hermes/profiles/*/; do
  name=$(basename "$prof")
  echo "=== $name ==="
  diff -rq ~/AppData/Local/hermes/skills "$prof/skills" 2>&1 | head -3
  # ... hooks, plugins, scripts, config.yaml, .env
done > ./scratch/profile-diff-pre.txt
```

**Gate 3.1:** `profile-diff-pre.txt` exists, shows profile-vs-root deltas.

## Phase 4 — Delete Target Files from Each Profile

For each of 17 profiles, remove:

- `skills/` (folder)
- `hooks/` (folder, if exists)
- `plugins/` (folder, if exists)
- `scripts/` (folder, if exists)
- `config.yaml` (file, if exists)
- `.env` (file, if exists)

**Gate 4.1:** All target files removed from all 17 profiles.
**Gate 4.2:** Each profile retains its `memories/`, `prompts/`, custom additions not in scope.

## Phase 5 — Mirror Root → Each Profile

```bash
ROOT=~/AppData/Local/hermes
for prof in $ROOT/profiles/*/; do
  [ -d "$ROOT/skills" ] && cp -r "$ROOT/skills" "$prof/"
  [ -d "$ROOT/hooks" ] && cp -r "$ROOT/hooks" "$prof/"
  [ -d "$ROOT/plugins" ] && cp -r "$ROOT/plugins" "$prof/"
  [ -d "$ROOT/scripts" ] && cp -r "$ROOT/scripts" "$prof/"
  [ -f "$ROOT/config.yaml" ] && cp "$ROOT/config.yaml" "$prof/"
  [ -f "$ROOT/.env" ] && cp "$ROOT/.env" "$prof/"
done
```

**Gate 5.1:** Every profile contains root's skills/hooks/plugins/scripts/config.yaml/.env.

## Phase 6 — Verification

```bash
for prof in $ROOT/profiles/*/; do
  echo "$prof: $(diff -rq $ROOT/skills $prof/skills | wc -l) skill diffs"
done
```

**Gate 6.1:** Diff count = 0 between root and each profile for skills (and ideally all other copied assets).

## Risks

| Risk                                                    | Mitigation                                                                                                 |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Profile has unique customization outside scope          | Backup captures everything; user can restore from backup                                                   |
| Hermes config validation breaks                         | Use `hermes config check` after copy; if errors, restore profile's original config.yaml from backup        |
| Skills reference scripts/hooks/plugins by relative path | Root copy makes paths work the same as default profile                                                     |
| Live profile sessions disrupted                         | Hermes uses one profile at a time; other profiles are passive. Profile copies won't affect active session. |

## Out of Scope

- Profile content customizations (e.g. memories/USER.md per-profile)
- Future-proofing for new profile types
- Hermes config validation beyond config check

## Completion Signal

"All 17 profiles mirror root for skills/hooks/plugins/scripts/config.yaml/.env, backup exists at `profiles-backup-<ts>/`, diff confirms parity, no hermes config validation errors."
