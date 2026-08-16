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

## Overview

Automated reasoning and workflow tool for `hermes-hooks`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Hook Directory Structure

```
C:/Users/Alexa/AppData/Local/hermes/hooks/
├── lib.py                        # Shared async helper library
├── lib.sh                        # Shared bash helper library
├── session-logger/
│   ├── README.md
│   ├── hooks.json
│   ├── hook.sh
│   ├── hook.py
│   ├── log-session-start.sh   # legacy, deprecated event alias
│   ├── log-session-end.sh     # legacy, deprecated event alias
│   └── log-prompt.sh          # legacy, deprecated event alias
├── session-auto-commit/
│   ├── README.md
│   ├── hooks.json
│   ├── hook.sh
│   ├── hook.py
│   └── auto-commit.sh         # legacy, deprecated event alias
└── governance-audit/
    ├── README.md
    ├── hooks.json
    ├── hook.sh
    ├── hook.py
    ├── audit-session-start.sh   # legacy, deprecated event alias
    ├── audit-session-end.sh     # legacy, deprecated event alias
    └── audit-prompt.sh          # legacy, deprecated event alias
```

**Canonical event names:** `on_session_start`, `on_session_end`, `pre_llm_call`

**Log root:** `C:/Users/Alexa/AppData/Local/hermes/logs/hermes/`

**Sub-directories:**
- session logs: `logs/sessions/<session_id>.jsonl`
- governance logs: `logs/hermes/governance/<session_id>.jsonl`
- deprecated governance fallback: `logs/audit/<session_id>.jsonl`

**CRITICAL:** `C:/Users/Alexa/AppData/Local/hermes/hooks` is the LIVE source of truth. Do not regenerate from docs alone; inspect `lib.py`, `lib.sh`, `hooks.json`, `hook.py`, and `hook.sh` before changing any hook tree.

---

## Hook Events

| Canonical Event | Legacy Alias | When Fired |
|-----------------|--------------|-----------|
| `on_session_start` | `session_start`, `sessionStart` | New Hermes session begins |
| `on_session_end` | `session_end`, `sessionEnd` | Hermes session ends |
| `pre_llm_call` | `userPromptSubmitted`, `pre_llm_call` | Before the tool loop for a user turn |

Event normalization rule: rewrite every incoming event with `event.strip().lower().replace("-", "_")` before dispatch.

---

## Hook Script Requirements

1. **Shared library first:** import `C:/Users/Alexa/AppData/Local/hermes/hooks/lib.py` from every `hook.py`; source `C:/Users/Alexa/AppData/Local/hermes/hooks/lib.sh` from every `hook.sh`.
2. **Single Python entrypoint per hook:** `hook.sh` is a thin wrapper that delegates to `hook.py`; do not add new shell logic there unless Python is unavailable.
3. **Read input safely:** use `read_payload()` from `lib.py` for stdin JSON parsing.
4. **Skip flag:** support `SKIP_<HOOK_NAME>=true`, case-insensitive; prefer `lib.skip_context()` / `lib.is_skipped()` from `lib.py`.
5. **Exit codes:** `0` = success, non-zero = error; write structured failures to per-hook error JSONL instead of failing silently.
6. **JSONL output:** use `lib.write_jsonl()`; do not use `jq` from Python code.
7. **Log paths:** resolve paths with `Path.home()` / `HERMES_HOME`; never hardcode `$USERPROFILE` in scripts.
8. **No backups:** never create `.bak` files; use git for rollback.
9. **Repo-origin policy:** do not copy samples from this skill into a hook tree unless they exactly match the event names in `hooks.json` and the canonical log paths live under `logs/hermes/`.

---

## Built-in Hooks

### 1. session-logger

Logs session lifecycle and prompt events.

```bash
C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger
```

**Outputs:**
- `logs/sessions/<session_id>.jsonl`
- `logs/hermes/session-auto-commit-errors.jsonl`
- `logs/hermes/session-auto-commit-skips.jsonl`

---

### 2. session-auto-commit

Auto-commits git changes on session end.

```bash
C:/Users/Alexa/AppData/Local/hermes/scripts/session-auto-commit
```

**Output:** Git commit with a `chore(session):` prefixed message or structured skip/error JSONL when no repo or no changes are present.

---

### 3. governance-audit

Governance audit for session lifecycle and prompts.

```bash
C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit
```

**Output:**
- `logs/hermes/governance/<session_id>.jsonl`
- deprecated fallback: `logs/audit/<session_id>.jsonl`
- `logs/hermes/governance-audit-errors.jsonl`
- `logs/hermes/governance-audit-skips.jsonl`

---

## Workflow

### Phase 1: Discover

```bash
# List hooks
find C:/Users/Alexa/AppData/Local/hermes/hooks -maxdepth 2 -type f | sort

# Read canonical source of truth
cat C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hooks.json
cat C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.py

# Check config registration
grep -A 20 "hooks:" C:/Users/Alexa/AppData/Local/hermes/config.yaml

# Review live logs
cat C:/Users/Alexa/AppData/Local/hermes/logs/sessions/*.jsonl
cat C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance/*.jsonl
```

### Phase 2: Create / Update

1. Create/edit files under `C:/Users/Alexa/AppData/Local/hermes/hooks/<hook-name>/`.
2. Required files: `hooks.json`, `README.md`, `hook.sh`, `hook.py`, plus any legacy `.sh` scripts when changing event names.
3. Use `lib.py` helpers from `C:/Users/Alexa/AppData/Local/hermes/hooks/lib.py`; do not inline new path/JSON constants.
4. Update `README.md` log-root paths, skip flag, and event examples; keep docs synced with `hooks.json`.
5. If registration changes, edit `C:/Users/Alexa/AppData/Local/hermes/config.yaml`.

### Phase 3: Test

```bash
# Canonical event names
echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh"
echo '{"event":"on_session_end","session_id":"test"}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.sh"
echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh"

# SKIP flags
SKIP_session_logger=true echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh"
SKIP_SESSION_AUTO_COMMIT=true echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.sh"
SKIP_GOVERNANCE_AUDIT=true echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh"

# Legacy aliases
echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/log-session-start.sh"
echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/auto-commit.sh"
echo '{}' | bash "C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh"
```

**Verify logs:**
```bash
cat C:/Users/Alexa/AppData/Local/hermes/logs/sessions/*.jsonl
cat C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance/*.jsonl
cat C:/Users/Alexa/AppData/Local/hermes/logs/audit/*.jsonl
```

### Phase 4: Debug

| Symptom | Cause | Fix |
|---------|-------|-----|
| Unknown event error | Runtime emits legacy event name | Normalize with `event.strip().lower().replace("-", "_")` |
| Skip flag ignored | Mixed case env var or wrong hook prefix | Use `lib.skip_context()` from `lib.py` |
| Missing log files | Wrong repo-rooted log path | Use canonical paths under `logs/hermes/` |
| Scripts not executable | Missing `chmod +x` | `chmod +x` on `hook.sh` and legacy `.sh` files |
| Relative paths in docs | Sample copied from docs verbatim | Use live files under `C:/Users/Alexa/AppData/Local/hermes/hooks/` |

### Phase 5: Enhance

1. Keep `lib.py` and `lib.sh` as the single source of truth for path constants and JSONL helpers.
2. Add new event types in `hooks.json` first, then add handlers in `hook.py`.
3. Improve logging by adding fields to JSONL records, not by adding new log files.
4. Add SKIP flags using `lib.skip_context()` / `lib.is_skipped()` from `lib.py`.
5. Update each hook's `README.md` immediately after code changes.
6. Test after every change, including legacy `.sh` aliases.

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

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-setup` | Initial Hermes configuration and paths |
| `hermes-profiles` | Profile-specific hook config |
| `hermes-hooks` | This skill; hook lifecycle management |

## References

- `C:/Users/Alexa/AppData/Local/hermes/hooks/lib.py` — canonical async helper library
- `C:/Users/Alexa/AppData/Local/hermes/hooks/lib.sh` — canonical bash helper library
- `C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hooks.json` — canonical event map
- `C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.py` — canonical session logger implementation
- `C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.py` — canonical auto-commit implementation
- `C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.py` — canonical governance implementation
- `C:/Users/Alexa/AppData/Local/hermes/docs/hermes-hooks-summary.md` — line-by-line script catalog and debug hook runner

## Verification Checklist

- [ ] `lib.py` and legacy `lib.sh` are inspected before editing hooks
- [ ] `hooks.json` uses canonical event names
- [ ] `hook.py` uses `lib.py` helpers for skip, logging, JSONL, and payload parsing
- [ ] Legacy `.sh` scripts still run and produce JSONL in canonical log dirs
- [ ] `hermes hooks doctor` passes or surfaces exact allowlist mismatch
- [ ] `SESSION_REPORT.md` is updated because this session changed hook files

## When to Use

- Creating/updating/deleting hooks
- Testing hook scripts
- Debugging hook failures
- Reviewing hook logs
- **Triggers**: "hook", "hooks", "hermes-hook", "session-logger", "session-auto-commit", "governance-audit", "create hook", "manage hooks"

## Pitfalls

- **Wire-payload shape drift (2026-08-08).** Shell hooks do NOT receive the
  raw kwargs the runtime passes to `invoke_hook`. The bridge serializes a
  normalized envelope `{hook_event_name, session_id, cwd, extra:{...}}`.
  `profile`, `user`, `provider`, and `timestamp` are never present —
  resolve them locally via `lib.py` (`resolve_profile`, `resolve_user`,
  `load_model_config`, `now_iso`). Reading `payload["user"]`/`payload["model"]`
  top-level yields permanent `unknown/""` records. See
  `references/event-payloads.md` for the verified wire shapes.
- **No session-end metrics on the wire (2026-08-08).** `on_session_end` never
  sends `duration_ms`, `turns`, `tokens_*`, `status`, or `exit_code`. Reading
  those top-level yields permanent `0/unknown` end records. Derive locally:
  status from `extra.turn_exit_reason`/`extra.completed|failed|interrupted`
  (`lib.resolve_end_status`), duration from the session_start timestamp and
  turns by counting `pre_llm_call` rows in the same session JSONL
  (`lib.duration_seconds_between`). The `cwd` envelope field is the working
  dir — never rely on `working_dir` alone (same bug class hit
  session-auto-commit).
- **Docs drift:** do not trust old event names in docs; read live `hook.py` files.
- **Stale log paths:** deprecated `logs/audit/` exists only as a compatibility fallback; new records must land under `logs/hermes/governance/`.
- **Skip flag mismatch:** `SKIP_LOGGING` is not the same as `SKIP_session_logger`; codified behavior lives in `lib.py`.
- **Windows consent:** exact-match command strings in `hooks:` still need explicit allowlist entries after recreate.
- **Thin content:** Add concrete code examples and real-world use cases where applicable.
- **Missing error handling:** Include retry-safe JSONL writes and structured error records in every hook.
- **No resumability:** Add entry/exit checks at each phase for long-running workflows.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
