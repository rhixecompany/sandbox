---
author: Alexa
description: Use when consolidating a Hermes profile config.yaml into the root config.yaml
  — merging model blocks, provider chains, and agent fields between v30 and legacy
  format configs across all profiles.
license: MIT
name: hermes-config-merge
tags:
- hermes
- config
- merge
- sync
- profiles
title: Hermes Config Merge
version: 1.0.0

---

# Hermes Config Merge

## When to Use
- A profile config.yaml has a different format than root config (e.g., legacy `model:` block at top vs `_config_version: 30`)
- You need to copy root config to all profiles after an update
- You need to add missing agent fields from one config to another
- Syncing config across 6+ profiles after a model/provider change

## When NOT to Use
- Single profile changes (just edit that profile's config.yaml)
- Env/auth file changes (those live separately)
- Configs are already identical

## Workflow

### Phase 1: Diagnose Config State
1. Check root and profile config formats with `head -3` on each
2. Check model blocks, fallback providers, agent fields with `grep`
3. Diff root vs each profile to find actual differences
4. Check MD5 hashes to see which profile configs already match root

### Phase 2: Plan Merge Strategy
| Scenario | Action |
|----------|--------|
| Root is v30, profile is legacy | Merge model block from profile → root, then sync root → all profiles |
| All are v30, minor quoting diffs | Replace profile configs with root |
| Root lacks model block entirely | Insert model block after `_config_version: 30` |

### Phase 3: Execute Merge
Use a Python script (see `~/AppData/Local/hermes/scripts/merge_config.py`):
1. Open file in `'rb'` mode to detect `\r\n` vs `\n`
2. Backup with `shutil.copy2(config, config + '.backup')`
3. Split on newline, keep first line, insert model block
4. Write in `'wb'` mode using same newline convention

### Phase 4: Sync to All Profiles
```bash
for p in alexa code-architect creative-director exec-assistant patient-tutor research-analyst; do
  cp config.yaml profiles/$p/config.yaml
done
# Verify all MD5-identical
```

### Phase 5: Sync Skills, Hooks, Plugins
- Skills: `diff <(ls skills/) <(ls profiles/alexa/skills/)` → sync missing skill dirs
- Hooks: `diff -rq hooks/ profiles/alexa/hooks/` → sync missing scripts
- `.env`: Already identical across profiles

## Pitfalls
- **CRLF line endings**: Windows configs use `\r\n`. Always use binary mode for merge operations.
- **Backup before merge**: `shutil.copy2(config, config + '.backup')` first.
- **Duplicate fields**: Check that original root config doesn't already have the fields (v30 already has service_tier, restart_drain_timeout, etc.)
- **Legacy alexa format**: alexa profile may have `model:` at top instead of `_config_version: 30`. Merge, don't overwrite blindly.
- **auth.json differs**: Each profile may have different auth tokens. Don't sync auth.json between profiles.

## Script Location
`~/AppData/Local/hermes/scripts/merge_config.py`

## Verification Checklist
- [ ] Root config has both `_config_version: 30` and `model:` block
- [ ] All 6 profile configs are MD5-identical to root
- [ ] Skills library synced root → all profiles
- [ ] Hooks synced (docs-cleanup-verify.sh, lib.sh)
- [ ] .env verified identical across profiles
- [ ] auth.json NOT overwritten
- [ ] Backup removed after verification
