# GitHub Hooks Reference

This directory contains **reference copies** of active Hermes hooks.
These are for Copilot/VS Code consumption only — **never overwrite
active Hermes hooks from this directory**.

## Sync Direction

Hermes `~/AppData/Local/hermes/hooks/` → `.github/hooks/` (one-way, reference copy)

## Active Hermes Hooks

| Hook | Trigger | Reference File |
|---|---|---|
| session-logger | on_session_start, on_session_end, pre_llm_call | `session-logger/hook.sh` + `01-session-logger-hook.sh` |
| governance-audit | on_session_start, on_session_end, pre_llm_call | `governance-audit/hook.sh` + `02-governance-audit-hook.sh` |
| session-auto-commit | on_session_end | `session-auto-commit/hook.sh` + `03-session-auto-commit-hook.sh` |

## Standalone Hook Scripts

| Script | Purpose | Reference File |
|---|---|---|
| pre-exec-validate.sh | Pre-execution validation | `pre-exec-validate.sh` + `04-pre-exec-validate.sh` |
| post-exec-state-log.py | Post-execution state logging | `post-exec-state-log.py` + `05-post-exec-state-log.py` |

## Cross-Platform Quick Commands Reference

See `docs/quick-commands-reference.md` for the full cross-platform quick commands documentation.

## Active Hook Locations (canonical)

- Session logger: `~/AppData/Local/hermes/hooks/session-logger/`
- Governance audit: `~/AppData/Local/hermes/hooks/governance-audit/`
- Session auto-commit: `~/AppData/Local/hermes/hooks/session-auto-commit/`
- Pre-exec validate: `~/AppData/Local/hermes/hooks/pre-exec-validate.sh`
- Post-exec state log: `~/AppData/Local/hermes/hooks/post-exec-state-log.py`

## Configuration

Active hooks are wired in Hermes `config.yaml` under `hooks:`:

```yaml
hooks:
  on_session_end:
    - session-logger/hook.sh
    - session-auto-commit/hook.sh
    - governance-audit/hook.sh
  on_session_start:
    - session-logger/hook.sh
    - governance-audit/hook.sh
  pre_llm_call:
    - session-logger/hook.sh
    - governance-audit/hook.sh
    - mcp_preflight_check.py (inline)
```
