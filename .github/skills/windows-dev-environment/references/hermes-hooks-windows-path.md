# Hermes Hook Path Resolution on Windows (MSYS/Git Bash)

## The Problem

`hermes hooks doctor` reports "script missing or not executable" even when the hook scripts exist in `hooks/<name>/hook.sh`.

**Root cause:** The config.yaml list hooks as `command: session-logger` (bare name). Hermes resolves this as an executable in its `scripts/` directory, but the actual shell script lives in `hooks/session-logger/hook.sh`. On Windows, MSYS path translation can also cause double-translation errors (`C:\c\Users\...`).

## Fix: Wrapper Scripts + Full Paths

### Step 1 — Create wrapper scripts in `scripts/`

Each hook gets a thin wrapper that delegates to its `hook.sh`:

```bash
#!/usr/bin/env bash
# Wrapper: delegates to hooks/session-logger/hook.sh
set -euo pipefail
LOCALAPPDATA="${LOCALAPPDATA:-C:/Users/<user>/AppData/Local}"
HOOK_SH="$LOCALAPPDATA/hermes/hooks/session-logger/hook.sh"
cd "$LOCALAPPDATA/hermes"
exec bash "$HOOK_SH"
```

Save as `scripts/session-logger` (no extension), then `chmod +x`.

### Step 2 — Update config.yaml to use full paths

```yaml
hooks:
  on_session_end:
    - command: bash "C:/Users/<user>/AppData/Local/hermes/scripts/session-logger"
```

The doctor checks the `command:` string directly — full paths pass where bare names fail.

### Step 3 — Fix MSYS path translation in hook.sh (three-tier fallback)

The original `hook.sh` pattern:

```bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

On MSYS, `pwd` returns `/c/Users/...` which gets double-translated to `C:\\c\\Users\\...` when passed to Windows Python. Fix with a three-tier fallback that handles `MSYS_NO_PATHCONV=1` environments:

```bash
# Resolve hook directory — handle MSYS2/Windows path translation
HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd )"
if command -v cygpath &>/dev/null; then
    HOOK_DIR=$(cygpath -w "$HOOK_DIR" 2>/dev/null || echo "$HOOK_DIR")
elif command -v pwd && pwd -W &>/dev/null; then
    HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
fi
HOOK_DIR=${HOOK_DIR//\\//}
```

- **Tier 1:** `cygpath -w` — most portable, works with `MSYS_NO_PATHCONV=1` (which disables auto-translation)
- **Tier 2:** `pwd -W` — fast fallback for MSYS2/git-bash with auto-translation active
- **Tier 3:** plain `pwd` — last resort for non-MSYS Unix-like shells
- `${HOOK_DIR//\\//}` normalizes any backslashes to forward slashes for cross-runtime consistency

### Step 4 — Re-allowlist

Changing the `command:` path invalidates previous approvals in `shell-hooks-allowlist.json`. Add new entries or the doctor will show `✗ not allowlisted`.

### Step 5 — Verify

```bash
hermes hooks doctor
# Expected: ✓ script exists and is executable, ✓ allowlisted
```

## When This Pattern Is Needed

| Symptom | Likely Cause |
|---------|-------------|
| `✗ script missing or not executable` | Hook `command:` uses bare name, no matching file in `scripts/` |
| `C:\c\Users\...` error in Python | MSYS `pwd` double-translation — use `pwd -W` |
| `✗ command not found` at hook test | Name not resolvable in PATH or scripts dir |

## Related

- `env-path-portability` SKILL.md — general MSYS path normalization and env-var resolution
- `references/msys-path-normalization.md` — `pwd -W`, `cygpath -w`, and the stray `\c\` bug
