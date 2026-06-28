# Profile Sync Procedure — Root → Profiles

Copy operational files (config.yaml, .env, hooks/, plugins/, skills/) from the Hermes root to all profile directories.

## When to Use

- After modifying root-level Hermes configuration that should propagate to all profiles
- When resetting profile state to match the canonical root configuration
- After `hermes setup` or major version upgrade

## Workflow

### Phase 1: Backup (Optional)

Skip if git-tracked or if profiles have no local changes worth preserving.

### Phase 2: Delete Profile-Specific Copies

```bash
ROOT=~/AppData/Local/hermes
for p in "$ROOT"/profiles/*/; do
  rm -rf "$p"config.yaml "$p".env "$p"skills "$p"hooks "$p"plugins
done
```

This removes the five operational items from every profile directory. Profile-exclusive files (auth.json, state.db, sessions/, logs/, etc.) are preserved.

### Phase 3: Copy from Root

```bash
ROOT=~/AppData/Local/hermes
for p in "$ROOT"/profiles/*/; do
  cp "$ROOT/config.yaml" "$p"
  cp "$ROOT/.env" "$p"
  cp -r "$ROOT/skills/" "$p"
  cp -r "$ROOT/hooks/" "$p"
  cp -r "$ROOT/plugins/" "$p"
done
```

Note: skills/ can be large (100+ directories). The copy may take 30-60s per profile. Use a generous timeout (300s).

### Phase 4: Verify Sync

```bash
ROOT=~/AppData/Local/hermes

# 1. config.yaml — all must match root
md5sum "$ROOT/config.yaml" "$ROOT"/profiles/*/config.yaml

# 2. .env — all must match root
md5sum "$ROOT/.env" "$ROOT"/profiles/*/.env

# 3. hooks/ — all must have same subdirectories
for p in "$ROOT"/profiles/*/; do echo "$(basename $p): $(ls "$p"hooks/)"; done

# 4. plugins/ — all must have same plugin dirs
for p in "$ROOT"/profiles/*/; do echo "$(basename $p): $(ls "$p"plugins/)"; done

# 5. skills/ — all must match root listing
for p in "$ROOT"/profiles/*/; do
  diff <(ls "$ROOT/skills/") <(ls "$p"skills/) >/dev/null &&
    echo "$(basename $p): MATCH" ||
    echo "$(basename $p): MISMATCH"
done
```

## What Gets Synced

| Item | Type | Notes |
|------|------|-------|
| `config.yaml` | File | Hermes main config (v30 format). Profile configs get upgraded to match root format. |
| `.env` | File | Environment variables, API keys, tokens. |
| `hooks/` | Dir | Hook scripts + configs (session-logger, governance-audit, session-auto-commit). |
| `plugins/` | Dir | Plugin directories (may contain `.git` repos — permission errors on `.git/objects/pack/` are non-fatal). |
| `skills/` | Dir | Full skill library with 100+ skill directories. |

## What Does NOT Get Synced

Profile-exclusive runtime state (NOT affected by this procedure):

- `auth.json` — per-profile auth tokens and credentials
- `state.db` — session database
- `sessions/` — session history
- `logs/` — per-profile logs
- `cache/` — per-profile caches
- `cron/` — per-profile cron jobs
- `memories/` — per-profile memory files (USER.md, MEMORY.md)
- `SOUL.md` — per-profile personality (must remain unique per profile)
- `.env` equivalents that vary by profile

## Pitfalls

- **`.git/objects/pack/` permission errors**: Plugin directories that are git clones may fail to copy their packed objects (locked by git). All plugin content (plugin.yaml, assets, etc.) copies successfully despite these errors — they are cosmetic.
- **Skills copy timeout**: The skills/ directory can be large (100+ skill dirs, >50MB). Use timeout=300 or larger for the copy command.
- **Root config differs from old profile configs**: The root uses modern config format (v30) with `mcp_servers`, `hooks`, `plugins` sections. Older profile configs use a minimal v1 format. Copying the root config upgrades them — verify compatibility before deploying.
- **Don't delete profile-exclusive files**: The glob pattern `profiles/*/{config.yaml,skills,hooks,.env,plugins}` only targets the five operational items. Do NOT use `rm -rf profiles/*/` which destroys runtime state.
