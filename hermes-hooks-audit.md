# Hermes Hooks Audit — default profile

Environment:
- Host: Windows 11
- Profile: default
- Config: `C:/Users/Alexa/AppData/Local/hermes/config.yaml`
- Hooks dir: `C:/Users/Alexa/AppData/Local/hermes/hooks`
- Wrapper scripts dir: `C:/Users/Alexa/AppData/Local/hermes/scripts`

## 1) Live hook registrations

Config `hooks` block:
```yaml
hooks:
  on_session_end:
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger"
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/session-auto-commit"
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit"
  on_session_start:
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger"
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit"
  pre_llm_call:
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger"
    - command: bash "C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit"
hooks_auto_accept: false
```

Registration map:
- `session-logger`: `on_session_start`, `on_session_end`, `pre_llm_call`
- `session-auto-commit`: `on_session_end`
- `governance-audit`: `on_session_start`, `on_session_end`, `pre_llm_call`

Note: No separate runtime hook registry file was found under `C:/Users/Alexa/AppData/Local/hermes`. Config currently appears to be the authoritative registration source.

## 2) Hook files present on disk

All three named hooks have directories under `.../hermes/hooks/`, metadata files, shell entrypoints, Python entrypoints, wrapper scripts under `.../hermes/scripts/`, and compiled Python `.pyc` artifacts.

Disk facts:
- `hooks_auto_accept` is `false`, so hook execution depends on approval behavior rather than auto-accept.
- Wrapper script pattern: `bash "C:/Users/Alexa/AppData/Local/hermes/scripts/<name>"`.
- Each wrapper then delegates to `hooks/<name>/hook.sh`, which executes `hook.py` under `python3` or `python`.

## 3) Missing or invalid scripts

No missing scripts detected for the three known hook names. Each hook has:
- `hooks/<name>/hooks.json`
- `hooks/<name>/hook.sh`
- `hooks/<name>/hook.py`
- `scripts/<name>`

Residual .sh files remain under `hooks/<name>/`:
- `session-logger`: `log-prompt.sh`, `log-session-start.sh`, `log-session-end.sh`
- `governance-audit`: `audit-prompt.sh`, `audit-session-start.sh`, `audit-session-end.sh`

These appear to be leftovers from an older shell-based implementation; current config and `hooks.json` point to `hook.sh`/`hook.py`. They are not a hard breakage, but they are repair/deprecation candidates.

## 4) Repair candidates / approvals needed

Candidates:
- deprecate/delete leftover per-event `.sh` files under each hook package
- remove stale `__pycache__` artifacts if hygiene is desired
- clean empty hook directory `C:/Users/Alexa/AppData/Local/hooks` if it is unused

Required approvals before mutation:
- any unregister/reregister action would need explicit user approval before changing `config.yaml` `hooks:` block
- any config write approval is required because `hooks_auto_accept: false` and current setup uses `bash` commands with shell hooks
