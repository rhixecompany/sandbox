# Hermes Profile Restore from Workspace (.github/) Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Create a backup of the current Hermes profile state, then install/verify/test/debug all hooks, skills, and plugins from the workspace `.github/` directory into the active `adminbot` profile.

**Architecture:** The workspace `.github/` is the source of truth for this project's Hermes configuration. Current profile state (`~/.hermes/` and `~/AppData/Local/hermes/`) will be backed up to `backup.hermes/`, then synced from `.github/`. Priority order: plugins → hooks → skills.

**Tech Stack:** Hermes Agent (CLI), bash/git-bash on Windows, config.yaml management, skill/plugin/hook installation procedures.

---

## Current State Analysis

| Component | Workspace Source (`.github/`) | Profile Target (`~/AppData/Local/hermes/`) | Status |
|-----------|------------------------------|--------------------------------------------|--------|
| **Hooks** | 3 dirs (governance-audit, session-auto-commit, session-logger) — **no hook.sh files** | 3 hooks with working `hook.sh` scripts | ⚠️ Source incomplete |
| **Plugins** | 46 dirs (Copilot agent configs, **not Hermes plugins**) | 4 built-in plugins enabled in config.yaml | ⚠️ Type mismatch |
| **Skills** | 27 categories, 200+ skills (valid Hermes skills) | 100+ skills in `~/.hermes/skills/` | ✅ Compatible |

**Key Insight:** `.github/plugins/` contains GitHub Copilot agent configurations, NOT Hermes plugins. Hermes plugins are managed via `config.yaml` `plugins.enabled` list (built-in: disk-cleanup, model-providers/openrouter, security-guidance, memory/honcho). The plan addresses this mismatch.

---

## Phase 0: Backup Current Profile State

### Task 0.1: Create backup.hermes/ directory structure

**Objective:** Create timestamped backup of current hooks, plugins config, skills, and config.yaml

**Files:**
- Create: `backup.hermes/2026-06-11_173000/`
- Create: `backup.hermes/2026-06-11_173000/hooks/` (copy of `~/AppData/Local/hermes/hooks/`)
- Create: `backup.hermes/2026-06-11_173000/plugins/` (copy of `~/AppData/Local/hermes/plugins/`)
- Create: `backup.hermes/2026-06-11_173000/skills/` (copy of `~/.hermes/skills/`)
- Create: `backup.hermes/2026-06-11_173000/config.yaml` (copy of `~/AppData/Local/hermes/config.yaml`)
- Create: `backup.hermes/2026-06-11_173000/manifest.json` (inventory of backed up items)

**Step 1: Create backup directory and manifest**

```bash
#!/usr/bin/env bash
set -euo pipefail

TIMESTAMP="2026-06-11_173000"
BACKUP_ROOT="backup.hermes/${TIMESTAMP}"
HERMES_DATA="$HOME/AppData/Local/hermes"
HERMES_SKILLS="$HOME/.hermes/skills"

mkdir -p "${BACKUP_ROOT}/hooks"
mkdir -p "${BACKUP_ROOT}/plugins"
mkdir -p "${BACKUP_ROOT}/skills"

# Backup hooks
cp -r "${HERMES_DATA}/hooks/"* "${BACKUP_ROOT}/hooks/" 2>/dev/null || true

# Backup plugins directory
cp -r "${HERMES_DATA}/plugins/"* "${BACKUP_ROOT}/plugins/" 2>/dev/null || true

# Backup skills (installed skills)
cp -r "${HERMES_SKILLS}/"* "${BACKUP_ROOT}/skills/" 2>/dev/null || true

# Backup config.yaml
cp "${HERMES_DATA}/config.yaml" "${BACKUP_ROOT}/config.yaml"

# Create manifest
cat > "${BACKUP_ROOT}/manifest.json" <<EOF
{
  "timestamp": "${TIMESTAMP}",
  "profile": "adminbot",
  "hermes_data": "${HERMES_DATA}",
  "hermes_skills": "${HERMES_SKILLS}",
  "hooks_count": $(find "${BACKUP_ROOT}/hooks" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "plugins_count": $(find "${BACKUP_ROOT}/plugins" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "skills_count": $(find "${BACKUP_ROOT}/skills" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "config_yaml_backed_up": true
}
EOF

echo "Backup complete: ${BACKUP_ROOT}"
cat "${BACKUP_ROOT}/manifest.json"
```

**Step 2: Run backup script**

Run: `bash backup.hermes/create_backup.sh`
Expected: SUCCESS — manifest.json shows counts matching current state

**Step 3: Verify backup integrity**

Run: `ls -la backup.hermes/2026-06-11_173000/`
Expected: All directories populated, manifest.json valid JSON

**Step 4: Commit backup**

```bash
git add backup.hermes/
git commit -m "chore: backup current hermes profile state before workspace sync"
```

---

## Phase 1: Plugins — Install, Verify, Test, Debug

**Context:** `.github/plugins/` contains 46 Copilot agent configs (NOT Hermes plugins). Hermes plugins are configured in `config.yaml` under `plugins.enabled`. Current enabled: `disk-cleanup`, `model-providers/openrouter`, `security-guidance`, `memory/honcho`. The workspace doesn't appear to have custom Hermes plugins to install.

### Task 1.1: Audit current plugin configuration

**Objective:** Document current plugin state and verify built-in plugins are functional

**Files:**
- Read: `~/AppData/Local/hermes/config.yaml` (lines 734-740)

**Step 1: List enabled plugins from config**

Run: `grep -A 10 "plugins:" ~/AppData/Local/hermes/config.yaml | head -15`
Expected: Shows 4 enabled plugins

**Step 2: Verify each built-in plugin loads**

Run: `hermes plugins list`
Expected: All 4 show as "enabled"

**Step 3: Test plugin functionality**

```bash
# Test disk-cleanup (should run silently on schedule)
# Test openrouter (verify model provider works)
hermes chat --model openrouter/claude-3.5-sonnet "test" --max-turns 1
# Test security-guidance (verify it scans prompts)
# Test memory/honcho (verify cross-session memory)
```

Expected: All plugins respond without errors

### Task 1.2: Document .github/plugins/ mismatch

**Objective:** Create decision record that .github/plugins/ are Copilot agents, not Hermes plugins

**Files:**
- Create: `docs/hermes-plugin-decision.md`

**Step 1: Write decision document**

```markdown
# Decision: .github/plugins/ are NOT Hermes Plugins

**Date:** 2026-06-11
**Status:** Accepted

## Context
The workspace `.github/plugins/` directory contains 46 GitHub Copilot agent configurations (e.g., `awesome-copilot`, `azure-cloud-development`, `hermes-achievements`). These are **not** Hermes plugins.

## Evidence
- No `plugin.yaml` manifest in any directory
- Content structure: `agents/`, `commands/`, `.github/` — Copilot agent format
- Hermes plugins require `plugin.yaml` with `type`, `entry_point`, `config_schema`

## Decision
Do NOT attempt to install `.github/plugins/` as Hermes plugins. Manage Hermes plugins exclusively via `config.yaml` `plugins.enabled` list.

## Consequences
- Workspace plugin configs remain for Copilot/VS Code use
- Hermes profile uses built-in plugins only (current 4)
- Future custom Hermes plugins would go in `~/.hermes/plugins/<name>/` with `plugin.yaml`
```

**Step 2: Commit decision record**

```bash
git add docs/hermes-plugin-decision.md
git commit -m "docs: record .github/plugins/ are Copilot agents, not Hermes plugins"
```

### Task 1.3: Verify no plugin regressions

**Objective:** Ensure all 4 built-in plugins still work after any config changes

**Step 1: Restart Hermes to reload plugins**

Run: `hermes restart` (or restart the session)

**Step 2: Verify plugin list**

Run: `hermes plugins list`
Expected: 4 enabled, 0 errors

**Step 3: Quick functional test per plugin**

- **openrouter:** `hermes chat --model openrouter/anthropic/claude-3.5-sonnet "hi" --max-turns 1`
- **security-guidance:** Send a prompt with a fake secret, verify it's flagged
- **memory/honcho:** Send a message, start new session, verify memory persists
- **disk-cleanup:** Verify cron job exists: `hermes cron list | grep disk-cleanup`

Expected: All pass

---

## Phase 2: Hooks — Install, Verify, Test, Debug

**Context:** `.github/hooks/` has 3 directories but **no `hook.sh` scripts**. The working hook scripts are in `~/AppData/Local/hermes/hooks/`. The plan: copy working hooks from profile to `.github/hooks/` as the new source of truth, then verify they're properly registered in config.yaml.

### Task 2.1: Sync hook scripts from profile to workspace

**Objective:** Make `.github/hooks/` the canonical source by copying working hook.sh files

**Files:**
- Modify: `.github/hooks/governance-audit/hook.sh` (create from profile)
- Modify: `.github/hooks/session-auto-commit/hook.sh` (create from profile)
- Modify: `.github/hooks/session-logger/hook.sh` (create from profile)

**Step 1: Copy hook.sh files to workspace**

```bash
#!/usr/bin/env bash
set -euo pipefail

SRC="$HOME/AppData/Local/hermes/hooks"
DST=".github/hooks"

for hook in governance-audit session-auto-commit session-logger; do
  if [[ -f "${SRC}/${hook}/hook.sh" ]]; then
    cp "${SRC}/${hook}/hook.sh" "${DST}/${hook}/hook.sh"
    chmod +x "${DST}/${hook}/hook.sh"
    echo "Copied ${hook}/hook.sh"
  else
    echo "WARNING: ${SRC}/${hook}/hook.sh not found"
  fi
done
```

**Step 2: Run sync script**

Run: `bash sync_hooks_to_workspace.sh`
Expected: All 3 hook.sh files copied, executable

**Step 3: Verify hook.sh content matches profile**

Run: `diff ~/AppData/Local/hermes/hooks/session-logger/hook.sh .github/hooks/session-logger/hook.sh`
Expected: No differences

### Task 2.2: Validate hook.sh syntax and patterns

**Objective:** Ensure all hooks follow Hermes conventions (jq -c, skip flag, absolute paths, awk for floats)

**Files:**
- Read: `.github/hooks/*/hook.sh`

**Step 1: Check each hook for required patterns**

```bash
for hook in .github/hooks/*/hook.sh; do
  echo "=== $(basename $(dirname $hook)) ==="
  grep -n "SKIP_" "$hook" || echo "MISSING: Skip flag"
  grep -n "jq -c" "$hook" || echo "MISSING: jq -c"
  grep -n "awk.*BEGIN.*exit" "$hook" || echo "OK: no float comparison needed"
  grep -n 'logs/hermes' "$hook" || echo "MISSING: logs/hermes path"
  head -1 "$hook" | grep -q '#!/usr/bin/env bash' && echo "OK: shebang" || echo "MISSING: shebang"
done
```

Expected: All hooks have skip flag, jq -c, shebang, correct log path

**Step 2: Fix any violations**

Edit hook.sh files to add missing patterns (use `patch` tool)

### Task 2.3: Verify config.yaml hook registration matches workspace

**Objective:** Ensure config.yaml points to workspace hook paths (or profile paths) consistently

**Files:**
- Read: `~/AppData/Local/hermes/config.yaml` lines 485-504

**Step 1: Check current config paths**

Run: `grep -A 5 "hooks:" ~/AppData/Local/hermes/config.yaml | head -20`
Expected: Paths point to `C:\Users\Alexa\AppData\Local\hermes\hooks\...`

**Step 2: Decide on path strategy**

**Decision:** Keep config.yaml pointing to profile paths (`~/AppData/Local/hermes/hooks/`) since Hermes loads from there. Workspace `.github/hooks/` is the *source* for version control; deployment copies to profile.

**Step 3: Create deployment script**

```bash
#!/usr/bin/env bash
# deploy_hooks.sh - Copy hooks from workspace to profile
set -euo pipefail
SRC=".github/hooks"
DST="$HOME/AppData/Local/hermes/hooks"
for hook in governance-audit session-auto-commit session-logger; do
  cp "${SRC}/${hook}/hook.sh" "${DST}/${hook}/hook.sh"
  chmod +x "${DST}/${hook}/hook.sh"
done
echo "Hooks deployed to profile"
```

### Task 2.4: Test each hook end-to-end

**Objective:** Verify hooks fire correctly on their registered events

**Step 1: Deploy hooks to profile**

Run: `bash deploy_hooks.sh`

**Step 2: Restart Hermes session**

Run: `hermes restart` (or new session)

**Step 3: Test session-logger**

- Start new session
- Send a prompt
- End session
- Check log file: `cat ~/AppData/Local/hermes/logs/hermes/session-*.log`
- Expected: SESSION_START, PRE_LLM_CALL, SESSION_END entries

**Step 4: Test session-auto-commit**

- Make a file change in workspace
- End session
- Run: `git log --oneline -1`
- Expected: New commit with session summary

**Step 5: Test governance-audit**

- Send a prompt containing a fake secret (e.g., `API_KEY=sk-fake123`)
- Check logs for audit detection
- Expected: Governance audit flags the secret

### Task 2.5: Add hook health-check to config

**Objective:** Add a verification step that runs on session start

**Files:**
- Modify: `~/AppData/Local/hermes/config.yaml` (add hook validation)

**Step 1: Create hook verification script**

```bash
#!/usr/bin/env bash
# verify_hooks.sh - Run on session start
set -euo pipefail
HOOKS_DIR="$HOME/AppData/Local/hermes/hooks"
for hook in governance-audit session-auto-commit session-logger; do
  [[ -x "${HOOKS_DIR}/${hook}/hook.sh" ]] || { echo "FAIL: ${hook} not executable"; exit 1; }
  # Quick syntax check
  bash -n "${HOOKS_DIR}/${hook}/hook.sh" || { echo "FAIL: ${hook} syntax error"; exit 1; }
done
echo "All hooks OK"
```

**Step 2: Add as a lightweight hook or alias**

Add to config.yaml or create alias for manual verification.

---

## Phase 3: Skills — Install, Verify, Test, Debug

**Context:** `.github/skills/` has 27 categories with 200+ valid Hermes skills. Current profile has 100+ skills in `~/.hermes/skills/` (many from bundled seeding). Need to sync workspace skills to profile, verify each loads, and debug any failures.

### Task 3.1: Inventory workspace skills vs profile skills

**Objective:** Generate diff of what's in `.github/skills/` vs `~/.hermes/skills/`

**Files:**
- Create: `skill_inventory.json`

**Step 1: Generate workspace skill list**

```bash
#!/usr/bin/env bash
find .github/skills -mindepth 2 -maxdepth 2 -type d -name "*" | \
  sed 's|.github/skills/||' | sort > workspace_skills.txt
echo "Workspace skills: $(wc -l < workspace_skills.txt)"
```

**Step 2: Generate profile skill list**

```bash
find ~/.hermes/skills -mindepth 1 -maxdepth 1 -type d | \
  sed 's|.*/.hermes/skills/||' | sort > profile_skills.txt
echo "Profile skills: $(wc -l < profile_skills.txt)"
```

**Step 3: Compute diff**

```bash
comm -23 workspace_skills.txt profile_skills.txt > missing_in_profile.txt
comm -13 workspace_skills.txt profile_skills.txt > extra_in_profile.txt
comm -12 workspace_skills.txt profile_skills.txt > common.txt
```

**Step 4: Review and categorize**

- `missing_in_profile.txt` → Need to install
- `extra_in_profile.txt` → Bundled skills not in workspace (decide: keep or remove)
- `common.txt` → Verify versions match

### Task 3.2: Install missing skills from workspace to profile

**Objective:** Copy missing skill directories to `~/.hermes/skills/`

**Files:**
- Create: `~/.hermes/skills/<skill-name>/` for each missing skill

**Step 1: Install missing skills**

```bash
#!/usr/bin/env bash
set -euo pipefail
SRC=".github/skills"
DST="$HOME/.hermes/skills"

while IFS= read -r skill; do
  [[ -z "$skill" ]] && continue
  if [[ -d "${SRC}/${skill}" ]]; then
    # Check if SKILL.md exists
    if [[ -f "${SRC}/${skill}/SKILL.md" ]]; then
      cp -r "${SRC}/${skill}" "${DST}/"
      echo "Installed: ${skill}"
    else
      echo "SKIP (no SKILL.md): ${skill}"
    fi
  fi
done < missing_in_profile.txt
```

**Step 2: Run installation**

Run: `bash install_missing_skills.sh`
Expected: All missing skills copied

**Step 3: Verify SKILL.md syntax for each new skill**

```bash
for skill in $(cat missing_in_profile.txt); do
  hermes skills view "$skill" >/dev/null 2>&1 && echo "OK: $skill" || echo "FAIL: $skill"
done
```

Expected: All new skills load without error

### Task 3.3: Handle extra skills in profile (bundled skills)

**Objective:** Decide fate of skills in profile but not in workspace

**Decision Matrix:**
| Skill Category | Action |
|----------------|--------|
| Core Hermes skills (hermes-*) | KEEP — essential for operation |
| Official bundled skills | KEEP — curated by Nous Research |
| Custom/workspace skills not in .github/ | REMOVE — not in source of truth |

**Step 1: Identify core/official skills to keep**

```bash
# Core skills (always keep)
CORE_SKILLS="hermes-hooks hermes-skills hermes-plugins hermes-tools hermes-mcp hermes-context hermes-personality hermes-quickstart"
```

**Step 2: Remove non-core extra skills**

```bash
#!/usr/bin/env bash
set -euo pipefail
CORE="hermes-hooks hermes-skills hermes-plugins hermes-tools hermes-mcp hermes-context hermes-personality hermes-quickstart"

while IFS= read -r skill; do
  [[ -z "$skill" ]] && continue
  if [[ " $CORE " != *" $skill "* ]]; then
    echo "Removing non-core extra skill: $skill"
    rm -rf "$HOME/.hermes/skills/$skill"
  else
    echo "Keeping core skill: $skill"
  fi
done < extra_in_profile.txt
```

### Task 3.4: Verify all workspace skills load correctly

**Objective:** Full load test of every skill in `.github/skills/`

**Step 1: Load test each skill**

```bash
#!/usr/bin/env bash
set -euo pipefail
FAILED=()
PASSED=()

find .github/skills -mindepth 2 -maxdepth 2 -type d -name "*" | while IFS= read -r dir; do
  skill=$(basename "$dir")
  if hermes skills view "$skill" >/dev/null 2>&1; then
    PASSED+=("$skill")
    echo "PASS: $skill"
  else
    FAILED+=("$skill")
    echo "FAIL: $skill"
  fi
done

echo "Passed: ${#PASSED[@]}"
echo "Failed: ${#FAILED[@]}"
for f in "${FAILED[@]}"; do echo "  - $f"; done
```

**Step 2: Debug failures**

For each FAIL:
- Check SKILL.md syntax (YAML frontmatter, required fields)
- Check `platforms` includes `windows`
- Check `metadata.hermes.category` is valid
- Check file permissions
- Fix and re-test

**Common Fixes:**
- Add `platforms: [linux, macos, windows]` to SKILL.md
- Fix YAML frontmatter indentation
- Ensure `name` field matches directory name
- Add `metadata.hermes.requires_toolsets` if tools used

### Task 3.5: Functional test critical skills

**Objective:** Verify high-value skills actually work end-to-end

**Test List:**
| Skill | Test Command | Expected |
|-------|-------------|----------|
| `plan` | `/plan test feature` | Creates plan in `.hermes/plans/` |
| `github-pr-workflow` | `/github-pr-workflow create PR for test` | Opens PR workflow |
| `subagent-driven-development` | `/subagent-driven-development` | Loads skill |
| `test-driven-development` | `/test-driven-development` | Loads skill |
| `systematic-debugging` | `/systematic-debugging` | Loads skill |
| `code-wiki` | `/code-wiki generate` | Runs wiki generation |
| `docker-management` | `/docker-management list` | Lists containers |

**Step 1: Run functional tests**

Execute each test command, verify no errors.

**Step 2: Fix any runtime issues**

- Missing dependencies → install via package manager
- Config issues → update config.yaml
- Path issues → fix absolute paths in skill scripts

### Task 3.6: Update skill curator config

**Objective:** Ensure curator manages the synced skill set properly

**Files:**
- Modify: `~/AppData/Local/hermes/config.yaml` (curator section)

**Step 1: Verify curator settings**

Run: `grep -A 10 "curator:" ~/AppData/Local/hermes/config.yaml`
Expected: `enabled: true`, `backup.enabled: true`

**Step 2: Run curator audit**

Run: `hermes skills audit`
Expected: Shows audit results for all installed skills

**Step 3: Handle audit BLOCKED verdicts**

Per hermes-skills skill: BLOCKED on official skills is informational (they remain functional). Community skills with DANGEROUS verdicts are blocked from install but already-installed ones work.

---

## Phase 4: Integration Verification

### Task 4.1: Full profile health check

**Objective:** Single command to verify hooks, plugins, skills all operational

**Step 1: Create health check script**

```bash
#!/usr/bin/env bash
# health_check.sh
set -euo pipefail
echo "=== Hermes Profile Health Check ==="
echo ""
echo "1. Config syntax:"
hermes config validate && echo "  OK" || echo "  FAIL"

echo ""
echo "2. Plugins:"
hermes plugins list | grep -E "enabled|disabled" | wc -l | xargs -I{} echo "  {} plugins configured"

echo ""
echo "3. Hooks:"
for hook in governance-audit session-auto-commit session-logger; do
  [[ -x "$HOME/AppData/Local/hermes/hooks/$hook/hook.sh" ]] && echo "  $hook: OK" || echo "  $hook: MISSING"
done

echo ""
echo "4. Skills:"
hermes skills list | grep -c "^\|" | xargs -I{} echo "  {} skills installed"

echo ""
echo "5. Quick functional test:"
/plan "health check test" 2>&1 | head -3
```

**Step 2: Run health check**

Run: `bash health_check.sh`
Expected: All sections report OK

### Task 4.2: End-to-end session test

**Objective:** Simulate a real session exercising all three systems

**Step 1: Start new session**

Send prompt: "Create a simple Python script that prints hello world"

**Step 2: Verify during session**
- `session-logger` logs PRE_LLM_CALL
- `governance-audit` scans prompt (no secrets)
- Skills load (e.g., `plan`, `github-pr-workflow` available)
- Plugins active (openrouter model works)

**Step 3: End session**
- `session-logger` logs SESSION_END
- `session-auto-commit` creates git commit
- `governance-audit` logs session end

**Step 4: Verify artifacts**
- Log file in `~/AppData/Local/hermes/logs/hermes/`
- Git commit exists
- No errors in Hermes logs

---

## Risks, Tradeoffs, and Open Questions

| Risk | Mitigation |
|------|------------|
| `.github/plugins/` are Copilot agents, not Hermes plugins | Documented decision; no install attempted |
| `.github/hooks/` missing hook.sh files | Copied from working profile; workspace becomes source |
| Bundled skills in profile not in workspace | Core skills kept; others removed per policy |
| Skill SKILL.md syntax errors on Windows | Validation step catches; platforms field includes windows |
| Config.yaml path mismatch (Windows vs POSIX) | Use POSIX paths in config; Hermes handles translation |
| Curator archive/prune removes workspace skills | Curator `prune_builtins: true` only affects unmodified bundled |

**Open Questions:**
1. Should `.github/hooks/` be the *only* source (deploy script copies to profile)? **Yes — planned.**
2. Should we install any custom Hermes plugins from elsewhere? **Not in scope; only built-ins.**
3. How to handle skill version drift between workspace and hub? **Workspace wins; hub updates pulled manually.**

---

## Execution Handoff

**Plan complete and saved. Ready to execute using subagent-driven-development — I'll dispatch a fresh subagent per task with two-stage review (spec compliance then code quality). Shall I proceed?**

**Suggested execution order:**
1. Phase 0 (Backup) — single task, run script
2. Phase 1 (Plugins) — 3 tasks, mostly verification
3. Phase 2 (Hooks) — 5 tasks, copy + test
4. Phase 3 (Skills) — 6 tasks, inventory → install → verify → test
5. Phase 4 (Integration) — 2 tasks, health check + E2E

Each task is bite-sized (2-5 min), with exact commands and verification steps.