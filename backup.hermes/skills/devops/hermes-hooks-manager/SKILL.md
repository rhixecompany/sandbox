---
name: hermes-hooks-manager
title: Hermes Hooks Manager
description: "Create, update, delete, test, debug, enhance and manage Hermes hooks. Use when working with hooks in ~/AppData/Local/hermes/hooks/. Triggers: hook, hooks, hermes-hook, session-logger, session-auto-commit, governance-audit, create hook, update hook, delete hook, test hook, debug hook, enhance hook, manage hooks."
category: devops
version: 1.0.0
author: Alexa
license: MIT
tags: [hooks, hermes, session-logger, session-auto-commit, governance-audit, management, testing, debugging]
---

# Hermes Hooks Manager

Full lifecycle management of Hermes hooks: create, update, delete, test, debug, enhance, and verify.

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

Logs go to: `~/AppData/Local/hermes/logs/hermes/` (and `logs/hermes/governance/`)

## When to Use

- Creating a new hook
- Updating/enhancing an existing hook
- Deleting a hook
- Testing hook scripts
- Debugging hook failures
- Reviewing hook logs
- Adding new threat patterns to governance-audit
- Changing hook event triggers

## When NOT TO Use

- Managing skills (use skill management skills)
- Managing plugins (use hermes-plugins-manager skill)
- Managing profile files (use profile-maintenance skill)

## Hook Events

| Event | When Fired |
|---|---|
| `sessionStart` | When a new Hermes session begins |
| `sessionEnd` | When a Hermes session ends |
| `userPromptSubmitted` | When user submits a prompt |

## Hook Script Requirements

1. **Shebang**: `#!/bin/bash` for shell scripts
2. **Strict mode**: `set -euo pipefail`
3. **Read input**: `INPUT=$(cat)` — hooks receive JSON via stdin
4. **Skip flag**: Every hook MUST support a `SKIP_<HOOKNAME>=true` env var
5. **Exit codes**: 0 = success, non-zero = error (governance uses 1 = blocked)
6. **JSON output**: Use `jq -c` for compact single-line JSON (never multi-line)
7. **Log paths**: Use `$HOME/AppData/Local/hermes/logs/hermes/` (not `logs/copilot/`)
8. **No backups**: Never create `.bak` files; use git for rollback

## Workflow

### Phase 1: Discover

1. List existing hooks: `ls ~/AppData/Local/hermes/hooks/`
2. Read the hook's `README.md`, `hooks.json`, and all scripts
3. Check `config.yaml` for hook registration: `hooks: {}`
4. Review existing logs: `~/AppData/Local/hermes/logs/hermes/`

### Phase 2: Create / Update

1. For new hooks: create directory under `~/AppData/Local/hermes/hooks/<hook-name>/`
2. Required files: `README.md`, `hooks.json`, `<function>.sh`
3. Update `hooks.json` with absolute paths (not relative `.github/hooks/...`)
4. Make scripts executable: `chmod +x *.sh`
5. Update `config.yaml` hooks section if needed

### Phase 3: Test

Test every hook script individually:

```bash
# Session logger
echo '{}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-session-start.sh
echo '{}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-session-end.sh
echo '{"userMessage":"test"}' | bash ~/AppData/Local/hermes/hooks/session-logger/log-prompt.sh

# Auto-commit (needs git repo with changes)
bash ~/AppData/Local/hermes/hooks/session-auto-commit/auto-commit.sh

# Governance audit
echo '{}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-session-start.sh
echo '{"userMessage":"clean prompt"}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh
echo '{"userMessage":"sudo chmod 777"}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh
echo '{}' | bash ~/AppData/Local/hermes/hooks/governance-audit/audit-session-end.sh

# Test SKIP flags
echo '{}' | SKIP_LOGGING=true bash ~/AppData/Local/hermes/hooks/session-logger/log-session-start.sh
echo '{}' | SKIP_GOVERNANCE_AUDIT=true bash ~/AppData/Local/hermes/hooks/governance-audit/audit-session-start.sh
```

Verify log output:
```bash
cat ~/AppData/Local/hermes/logs/hermes/session.log
cat ~/AppData/Local/hermes/logs/hermes/prompts.log
cat ~/AppData/Local/hermes/logs/hermes/governance/audit.log
```

### Phase 4: Debug

Common issues:

| Symptom | Cause | Fix |
|---|---|---|
| Multi-line JSON in logs | Missing `jq -c` flag | Add `-c` to all `jq` invocations |
| `bc` float comparison fails | `(( ))` only does integers | Use `awk "BEGIN {exit !($a > $b)}"` |
| Scripts not executable | Missing `chmod +x` | `chmod +x ~/AppData/Local/hermes/hooks/<hook>/*.sh` |
| Wrong log directory | Using `logs/copilot/` | Change to `logs/hermes/` |
| Relative paths in hooks.json | `.github/hooks/...` paths | Use absolute `C:/Users/...` paths |
| SKIP env var not working | Var not passed to bash | `VAR=true bash script.sh` not `VAR=true echo \| bash` |

### Phase 5: Enhance

When enhancing hooks:

1. **Add threat patterns** to `audit-prompt.sh`: use `check_pattern "regex" "category" "severity" "description"`
2. **Add new event types**: update `hooks.json` with new event + script mapping
3. **Improve logging**: add more fields to JSON output, use `jq -c` for encoding
4. **Add SKIP flags**: every hook must have a disable mechanism
5. **Update README**: keep in sync with script changes
6. **Test after every change**: run the test suite from Phase 3

## Governance Audit Threat Categories

| Category | Severity Range | Examples |
|---|---|---|
| `data_exfiltration` | 0.7 - 0.95 | Bulk data transfer, external export, credential upload |
| `privilege_escalation` | 0.8 - 0.95 | sudo, chmod 777, adding admin access |
| `system_destruction` | 0.9 - 0.95 | rm -rf /, drop database, mass deletion |
| `prompt_injection` | 0.6 - 0.9 | Instruction override, role reassignment |
| `credential_exposure` | 0.9 - 0.95 | Hardcoded API keys, AWS keys |

## Pitfalls

- **Never use multi-line `jq` output** in scripts that write to JSON Lines log files. Always use `jq -c`.
- **Never use `bc` + `(( ))`** for float comparison. `(( ))` is integer-only. Use `awk "BEGIN {exit !($a > $b)}"`.
- **Never use relative paths** in `hooks.json` — Hermes resolves from its own cwd, not the repo root.
- **Never hardcode `logs/copilot/`** — these are Hermes hooks, use `logs/hermes/`.
- **Always test SKIP flags** — every hook must be disableable without code changes.
- **Always use absolute paths** for log files: `$HOME/AppData/Local/hermes/logs/hermes/`.
