---
name: hermes-profile-management
description: Hermes profile backup, restore, and workspace synchronization procedures
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, profile, backup, restore, sync, devops]
    category: devops
    requires_toolsets: [terminal, file, skills]
---

# Hermes Profile Management Skill

## When to Use
- Backing up a Hermes profile before major changes
- Restoring a profile from backup
- Synchronizing profile configuration (hooks, plugins, skills) from a workspace `.github/` source of truth
- Migrating profile between machines or environments
- Disaster recovery after profile corruption

## Procedure

### 1. Backup Current Profile State
```bash
# Create timestamped backup
TIMESTAMP=$(date +%Y-%m-%d_%H%M%S)
BACKUP_ROOT="backup.hermes/${TIMESTAMP}"
HERMES_DATA="$HOME/AppData/Local/hermes"   # Windows
HERMES_SKILLS="$HOME/.hermes/skills"        # Cross-platform skills dir

mkdir -p "${BACKUP_ROOT}/hooks"
mkdir -p "${BACKUP_ROOT}/plugins"
mkdir -p "${BACKUP_ROOT}/skills"

# Backup hooks (profile → backup)
cp -r "${HERMES_DATA}/hooks/"* "${BACKUP_ROOT}/hooks/" 2>/dev/null || true

# Backup plugins directory (profile → backup)
cp -r "${HERMES_DATA}/plugins/"* "${BACKUP_ROOT}/plugins/" 2>/dev/null || true

# Backup installed skills (skills dir → backup)
cp -r "${HERMES_SKILLS}/"* "${BACKUP_ROOT}/skills/" 2>/dev/null || true

# Backup config.yaml
cp "${HERMES_DATA}/config.yaml" "${BACKUP_ROOT}/config.yaml"

# Create manifest
cat > "${BACKUP_ROOT}/manifest.json" <<EOF
{
  "timestamp": "${TIMESTAMP}",
  "profile": "$(basename $(dirname ${HERMES_DATA}))",
  "hooks_count": $(find "${BACKUP_ROOT}/hooks" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "plugins_count": $(find "${BACKUP_ROOT}/plugins" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "skills_count": $(find "${BACKUP_ROOT}/skills" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "config_yaml_backed_up": true
}
EOF
```

### 2. Restore Profile from Backup
```bash
TIMESTAMP="2026-06-11_173000"  # Specify backup to restore
BACKUP_ROOT="backup.hermes/${TIMESTAMP}"
HERMES_DATA="$HOME/AppData/Local/hermes"
HERMES_SKILLS="$HOME/.hermes/skills"

# Restore hooks
cp -r "${BACKUP_ROOT}/hooks/"* "${HERMES_DATA}/hooks/"

# Restore plugins
cp -r "${BACKUP_ROOT}/plugins/"* "${HERMES_DATA}/plugins/"

# Restore skills
cp -r "${BACKUP_ROOT}/skills/"* "${HERMES_SKILLS}/"

# Restore config.yaml
cp "${BACKUP_ROOT}/config.yaml" "${HERMES_DATA}/config.yaml"

# Restart Hermes to reload
hermes restart
```

### 3. Sync Workspace `.github/` → Profile (Source of Truth Pattern)
**Critical Distinction:** Workspace `.github/` structure differs from Hermes profile structure:

| Workspace Path | Contains | Hermes Profile Target | Notes |
|----------------|----------|----------------------|-------|
| `.github/hooks/` | Hook source scripts (hook.sh) | `~/AppData/Local/hermes/hooks/` | Copy hook.sh files, keep config.yaml pointing to profile paths |
| `.github/plugins/` | **Copilot agent configs** (NOT Hermes plugins) | N/A — **Do not install** | Hermes plugins managed via `config.yaml plugins.enabled` only |
| `.github/skills/` | Valid Hermes skills (SKILL.md) | `~/.hermes/skills/` | Sync bidirectionally; workspace wins |

**Sync Script — Hooks (Workspace → Profile):**
```bash
#!/usr/bin/env bash
# deploy_hooks.sh
set -euo pipefail
SRC=".github/hooks"
DST="$HOME/AppData/Local/hermes/hooks"
for hook in governance-audit session-auto-commit session-logger; do
  [[ -f "${SRC}/${hook}/hook.sh" ]] && cp "${SRC}/${hook}/hook.sh" "${DST}/${hook}/hook.sh"
  chmod +x "${DST}/${hook}/hook.sh"
done
echo "Hooks deployed to profile"
```

**Sync Script — Skills (Workspace ↔ Profile):**
```bash
#!/usr/bin/env bash
# sync_skills.sh
set -euo pipefail
SRC=".github/skills"
DST="$HOME/.hermes/skills"
CORE_SKILLS="hermes-hooks hermes-skills hermes-plugins hermes-tools hermes-mcp hermes-context hermes-personality hermes-quickstart"

# 1. Install missing from workspace
find "${SRC}" -mindepth 2 -maxdepth 2 -type d | while read dir; do
  skill=$(basename "$dir")
  [[ -f "${SRC}/${skill}/SKILL.md" ]] && cp -r "${SRC}/${skill}" "${DST}/"
done

# 2. Remove non-core extras in profile not in workspace
find "${DST}" -mindepth 1 -maxdepth 1 -type d | while read dir; do
  skill=$(basename "$dir")
  [[ " $CORE_SKILLS " == *" $skill "* ]] && continue
  [[ -d "${SRC}/${skill}" ]] || rm -rf "${dir}"
done

# 3. Verify all load
hermes skills list | wc -l
```

### 4. Verify Profile Health
```bash
#!/usr/bin/env bash
# health_check.sh
echo "=== Hermes Profile Health Check ==="
echo "1. Config: $(hermes config validate && echo OK || echo FAIL)"
echo "2. Plugins: $(hermes plugins list | grep -c enabled) enabled"
echo "3. Hooks:"
for h in governance-audit session-auto-commit session-logger; do
  [[ -x "$HOME/AppData/Local/hermes/hooks/${h}/hook.sh" ]] && echo "  ${h}: OK" || echo "  ${h}: MISSING"
done
echo "4. Skills: $(hermes skills list | wc -l) installed"
```

## Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| `.github/plugins/` are Copilot agents | No `plugin.yaml`, directories have `agents/`, `commands/` | **Do not install** — manage Hermes plugins via `config.yaml` only |
| Hook scripts missing in workspace | `.github/hooks/<name>/` exists but no `hook.sh` | Copy from profile (`~/AppData/Local/hermes/hooks/`) to workspace as source |
| Config.yaml paths use Windows format | `C:\Users\...` in config.yaml | Hermes handles POSIX↔Windows translation; use POSIX in scripts |
| Skill `platforms` missing `windows` | Skill loads on Linux/macOS but not Windows | Add `platforms: [linux, macos, windows]` to SKILL.md frontmatter |
| Curator archives workspace skills | `prune_builtins: true` removes unmodified bundled | Only affects bundled skills; workspace skills modified = kept |
| `hermes skills install` (singular) fails | Command not found | Correct command is `hermes skills install` (plural) |

## Verification

1. **Backup:** `cat backup.hermes/<timestamp>/manifest.json` shows expected counts
2. **Restore:** `hermes plugins list`, `hermes skills list`, hook scripts executable
3. **Sync:** `diff .github/hooks/<name>/hook.sh ~/AppData/Local/hermes/hooks/<name>/hook.sh` shows no diff
4. **Health check:** All 4 checks pass (config, plugins, hooks, skills)
5. **E2E session:** Start session → send prompt → end session → verify logs, git commit, audit

## References
- `references/workspace-sync-decision.md` — Why `.github/plugins/` are not Hermes plugins
- `references/hook-template.md` — Required hook.sh patterns (skip flag, jq -c, awk floats, logs/hermes)
- `references/skill-inventory-template.md` — Workspace vs profile skill diff template
- `references/health-check.sh` — Runnable verification script