---
author: Hermes Agent
description: 'Full lifecycle management of Hermes hooks: session-logger, session-auto-commit,
  governance-audit. Create, update, delete, test, debug, enhance.'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: hermes-hooks
tags:
- imported
title: Hermes Hooks
version: 2.0.0

---
# Hermes Hooks

Single authoritative skill for all Hermes hook lifecycle management. Consolidates: `hermes-hooks-manager`, `hermes-hooks`.

---

## Hook Directory Structure

```
~/AppData/Local/hermes/hooks/
├── coding-task-hooks.py          # Python-based ACPX dispatch hook
├── session-logger/               # Logs session start/end/prompts
│   ├── README.md
│   ├── hooks.json
│   ├── log-session-start.sh
│   ├── log-session-end.sh
│   └── log-prompt.sh
├── session-auto-commit/          # Auto-commits on session end
│   ├── README.md
│   ├── hooks.json
│   └── auto-commit.sh
└── governance-audit/             # Threat detection for prompts
    ├── README.md
    ├── hooks.json
    ├── audit-session-start.sh
    ├── audit-session-end.sh
    └── audit-prompt.sh
```

**Logs go to:** `~/AppData/Local/hermes/logs/hermes/` (governance: `logs/hermes/governance/`)

**CRITICAL:** `~/.hermes/hooks` is the LIVE source of truth. `.github/hooks` is reference-only. Never delete the live tree.

---

## Hook Events

| Event | When Fired |
|-------|------------|
| `on_session_start` | New Hermes session begins |
| `on_session_end` | Hermes session ends |
| `pre_llm_call` | Before tool loop for user turn |

---

## Hook Script Requirements

1. **Shebang:** `#!/bin/bash`
2. **Strict mode:** `set -euo pipefail`
3. **Read input:** `INPUT=$(cat)` — JSON via stdin
4. **Skip flag:** Every hook MUST support `SKIP_<HOOKNAME>=true` env var
5. **Exit codes:** 0 = success, non-zero = error (governance: 1 = blocked)
6. **JSON output:** Use `jq -c` for compact single-line JSON (never multi-line)
7. **Log paths:** `$HOME/AppData/Local/hermes/logs/hermes/` (NOT `logs/copilot/`)
8. **No backups:** Never create `.bak` files; use git for rollback
9. **Unified entry point:** One `hook.sh` per hook, dispatch by `$1` event type — NOT separate scripts per event
10. **Shared library:** Source `$(dirname "$0")/../lib.sh` for utility functions (escape, timestamp, log_jsonl, ensure_log_dir, git_commit_if_changed)

---

## Built-in Hooks

### 1. session-logger

Logs session lifecycle and prompts.

```bash
# Test
echo '{}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-session-start.sh
echo '{}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-session-end.sh
echo '{"user_message":"test"}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-prompt.sh

# Skip
SKIP_LOGGING=true echo '{}' | bash .../log-session-start.sh
```

**Outputs:**
- `logs/hermes/session.log` — session start/end events
- `logs/hermes/prompts.log` — user prompts

### 2. session-auto-commit

Auto-commits git changes on session end.

```bash
# Test (needs git repo with changes)
bash ~/AppData/Local/hermes/hooks/session-auto-commit/auto-commit.sh
```

**Output:** Git commit with session summary

### 3. governance-audit

Threat detection for prompts.

```bash
# Test
echo '{}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-session-start.sh
echo '{"user_message":"clean prompt"}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh
echo '{"user_message":"sudo chmod 777"}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh

# Skip
SKIP_GOVERNANCE_AUDIT=true echo '{}' | bash .../audit-session-start.sh
```

**Output:** `logs/hermes/governance/audit.log` — threat scores, blocks

---

## Workflow

### Phase 1: Discover

```bash
# List hooks
ls ~/AppData/Local/hermes/hooks/

# Read hook structure
cat ~/AppData/Local/hermes/hooks/session-logger/hooks.json
cat ~/AppData/Local/hermes/hooks/session-logger/README.md

# Check config.yaml registration
grep -A 20 "hooks:" ~/.hermes/config.yaml

# Review logs
cat ~/AppData/Local/hermes/logs/hermes/session.log
cat ~/AppData/Local/hermes/logs/hermes/governance/audit.log
```

### Phase 2: Create / Update

```bash
# 1. Create directory
mkdir -p ~/AppData/Local/hermes/hooks/<hook-name>/

# 2. Required files
# hooks.json (event mapping + script paths)
# README.md (documentation)
# <function>.sh (executable scripts)

# 3. hooks.json template
cat > ~/AppData/Local/hermes/hooks/<hook-name>/hooks.json <<'JSON'
{
  "name": "<hook-name>",
  "events": ["on_session_start", "on_session_end", "pre_llm_call"],
  "script": "main-function.sh"
}
JSON

# 4. Make executable
chmod +x ~/AppData/Local/hermes/hooks/<hook-name>/*.sh

# 5. Update config.yaml if needed
hermes config edit
```

### Phase 3: Test

```bash
# Always test every script individually
echo '{}' | bash ~/AppData/Local/hermes/hooks/<hook>/main-function.sh

# Test with sample input
echo '{"user_message":"test"}' | bash .../pre-llm-call.sh

# Test SKIP flags
SKIP_<HOOK>=true bash ...
```

**Verify logs:**
```bash
cat ~/AppData/Local/hermes/logs/hermes/session.log
cat ~/AppData/Local/hermes/logs/hermes/prompts.log
cat ~/AppData/Local/hermes/logs/hermes/governance/audit.log
```

### Phase 4: Debug

| Symptom | Cause | Fix |
|---------|-------|-----|
| Multi-line JSON in logs | Missing `jq -c` | Add `-c` to all `jq` |
| `bc` float compare fails | `(( ))` integers only | Use `awk "BEGIN {exit !($a > $b)}"` |
| Scripts not executable | Missing `chmod +x` | `chmod +x ~/.../hooks/<hook>/*.sh` |
| Wrong log directory | Using `logs/copilot/` | Change to `logs/hermes/` |
| Relative paths in hooks.json | `.github/hooks/...` paths | Use absolute `C:/Users/...` paths |
| SKIP env var not working | Var not passed to bash | `VAR=true bash script.sh` |

### Phase 5: Enhance

1. **Add threat patterns** to `audit-prompt.sh`:
   ```bash
   check_pattern "regex" "category" "severity" "description"
   ```
2. **Add new event types** in `hooks.json`
3. **Improve logging** — more fields, `jq -c` encoding
4. **Add SKIP flags** — every hook must be disableable
5. **Update README** — keep in sync
6. **Test after every change**

---

## Governance Audit Threat Categories

| Category | Severity | Examples |
|----------|----------|----------|
| `data_exfiltration` | 0.7-0.95 | Bulk transfer, external export, credential upload |
| `privilege_escalation` | 0.8-0.95 | sudo, chmod 777, adding admin |
| `system_destruction` | 0.9-0.95 | rm -rf /, drop database, mass deletion |
| `prompt_injection` | 0.6-0.9 | Instruction override, role reassignment |
| `credential_exposure` | 0.9-0.95 | Hardcoded API keys, AWS keys |

---

## Restore / Rehydrate Procedure

```bash
mkdir -p ~/AppData/Local/hermes/hooks/{session-logger,session-auto-commit,governance-audit}

# session-logger
cat > ~/AppData/Local/hermes/hooks/session-logger/hooks.json <<'JSON'
{"name":"session-logger","events":["on_session_start","on_session_end","pre_llm_call"],"script":"log-session-start.sh"}
JSON
for s in hook.sh log-session-start.sh log-session-end.sh log-prompt.sh; do
  cat > ~/AppData/Local/hermes/hooks/session-logger/$s <<'SH'
#!/bin/bash
set -euo pipefail
INPUT=$(cat)
echo '{}'
SH
  chmod +x ~/AppData/Local/hermes/hooks/session-logger/$s
done

# session-auto-commit
cat > ~/AppData/Local/hermes/hooks/session-auto-commit/hooks.json <<'JSON'
{"name":"session-auto-commit","events":["on_session_end"],"script":"auto-commit.sh"}
JSON
for s in hook.sh auto-commit.sh; do
  cat > ~/AppData/Local/hermes/hooks/session-auto-commit/$s <<'SH'
#!/bin/bash
set -euo pipefail
INPUT=$(cat)
echo '{}'
SH
  chmod +x ~/AppData/Local/hermes/hooks/session-auto-commit/$s
done

# governance-audit
cat > ~/AppData/Local/hermes/hooks/governance-audit/hooks.json <<'JSON'
{"name":"governance-audit","events":["on_session_start","on_session_end","pre_llm_call"],"script":"audit-session-start.sh"}
JSON
for s in hook.sh audit-session-start.sh audit-session-end.sh audit-prompt.sh; do
  cat > ~/AppData/Local/hermes/hooks/governance-audit/$s <<'SH'
#!/bin/bash
set -euo pipefail
INPUT=$(cat)
if [ "${SKIP_GOVERNANCE_AUDIT:-false}" = "true" ]; then exit 0; fi
echo '{}'
SH
  chmod +x ~/AppData/Local/hermes/hooks/governance-audit/$s
done

# Sync reference copy if needed
cp -a ~/AppData/Local/hermes/hooks /path/to/reference/hooks
```

---

## Pitfalls

- **Treat `~/.hermes/hooks` as live truth.** `.github/hooks` is at-best reference.
- **Verify directory state before cleanup.** If `find ... -maxdepth 2 -mindepth 1` empty, STOP.
- **Use access probe after `rm -rf`:** `"[ -d PATH ] && echo PRESENT || echo GONE"` immediately after.
- **If live hooks deleted, recreate stubs first**, then mirror to `.github/hooks`.
- **Never multi-line `jq` output** in JSON Lines logs. Always `jq -c`.
- **Never `bc` + `(( ))`** for floats. Use `awk`.
- **Never relative paths** in `hooks.json` — Hermes resolves from its cwd.
- **Never hardcode `logs/copilot/`** — use `logs/hermes/`.
- **Always test SKIP flags** — every hook must be disableable.
- **Always absolute paths** for logs: `$HOME/AppData/Local/hermes/logs/hermes/`.
- **Verify removal in one shell step:** `rm -rf "$A" && [ -d "$A" ] && echo STILL_PRESENT || echo GONE`.
- **Hooks must be registered in config.yaml.** Writing scripts to `~/.hermes/hooks/` is NOT enough — Hermes only loads hooks listed under the `hooks:` key in `~/.hermes/config.yaml`. After creating/updating hooks, verify registration with `grep -A 20 "hooks:" ~/.hermes/config.yaml`. If the section is missing, hooks silently do nothing.
- **Config.yaml may appear empty but still work.** `hermes config show` reads from multiple sources (defaults, env vars, runtime). An empty or minimal `config.yaml` does NOT mean Hermes has no config — it means defaults are active. Always use `hermes config show` to verify actual runtime state, never rely on file size alone.

---

## Skills Required

| Skill | Purpose | When Needed |
|-------|---------|-------------|
| `hermes-setup` | Initial Hermes configuration | Before creating hooks |
| `hermes-profiles` | Profile-specific hook config | Per-profile hook setup |
| `governance-audit` | Threat detection configuration | Setting up audit patterns |
| `session-logger` | Session lifecycle logging | Core hook functionality |
| `session-auto-commit` | Auto-commit on session end | Core hook functionality |

---

## Verification Checklist

- [ ] Frontmatter complete: name, title, description, version, author, license, tags
- [ ] Skills Required table present
- [ ] Phased workflow with 5 clear phases (Discover → Create/Update → Test → Debug → Enhance)
- [ ] Pitfalls table with ≥10 entries covering all severity levels
- [ ] Verification checklist present
- [ ] Reference files exist in `references/` (5 files: audit-remediation, commands, config-registration-gotcha, event-payloads, hook-template)
- [ ] No placeholder text (`[Add ... here]`)
- [ ] Concrete bash examples for every hook operation
- [ ] Cross-references consistent
- [ ] SKIP flag testing documented for every hook
- [ ] Restore/rehydrate procedure included

---

## When to Use

- Creating/updating/deleting hooks
- Testing hook scripts
- Debugging hook failures
- Reviewing hook logs
- Adding threat patterns to governance-audit
- **Triggers**: "hook", "hooks", "hermes-hook", "session-logger", "session-auto-commit", "governance-audit", "create hook", "manage hooks"