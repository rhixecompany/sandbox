# Session Evidence — 2026-07-24 Full Hook Cleanup

## Live state observed

- `hermes hooks list` showed 7 shell hooks registered from:
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger`
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/session-auto-commit`
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit`
- Canonical hook trees existed under:
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/`
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/`
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/`
- Each hook tree included `hook.sh`, `hook.py`, and `hooks.json`.
- Each hook tree also included compiled caches under `__pycache__/`.

## Exact stale-wrapper comparison

Wrappers in `~/AppData/Local/hermes/scripts/<name>` were one-line launch shims:

```bash
LOCALAPPDATA="${LOCALAPPDATA:-C:/Users/Alexa/AppData/Local}"
HOOK_SH="$LOCALAPPDATA/hermes/hooks/<name>/hook.sh"
cd "$LOCALAPPDATA/hermes"
exec bash "$HOOK_SH"
```

Repo-side `.github/scripts/<name>` files were identical stale wrapper copies.

## Applied cleanup

- Removed `.github/scripts/session-logger`
- Removed `.github/scripts/session-auto-commit`
- Removed `.github/scripts/governance-audit`
- Removed live wrappers:
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/session-logger`
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/session-auto-commit`
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/governance-audit`
- Removed compiled caches:
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/session-logger/__pycache__`
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/__pycache__`
  - `C:/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/__pycache__`

## Remaining blockers

- `config.yaml` still references stale wrapper paths.
- Local `hermes hooks` command set does not expose an `add/register` subcommand in this install.
- Direct config edit was blocked by Hermes config security tooling.

## Approval artifacts

- `.hermes/approvals/2026-07-24-full-hook-plugin-cleanup.md`

## Verification evidence

- Ad-hoc verification script passed:
  - repo wrappers removed
  - canonical `hook.sh` present
  - live wrappers removed
  - `hooks.json` present
  - `__pycache__` removed
- Hermes validation reviewed:
  - `hermes hooks list`
  - `hermes hooks doctor`
  - `grep -A 20 "^hooks:" "$LOCALAPPDATA/hermes/config.yaml"`
- `SESSION_REPORT.md` updated with exact changed artifacts and remaining blocker