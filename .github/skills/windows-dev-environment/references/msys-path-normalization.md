# MSYS/Git Bash Path Normalization on Windows

## The Problem

MSYS (Git Bash) rewrites POSIX-style paths (`/c/Users/...`) to Windows-native paths (`C:\\Users\\...`) when passing arguments to native Windows executables — but only in some contexts. This causes double-translation.

### Scenario 1: Auto-translation active (default)

When `MSYS_NO_PATHCONV` is unset or `0`, MSYS automatically translates paths. This can go wrong when a path is already partially translated:

- `$(cd ... && pwd)` returns `/c/Users/Alexa/...` (MSYS path)
- Passed to Windows Python → MSYS rewrites to `C:\\c\\Users\\Alexa\\...` (WRONG — stray `\\c\\`)
- Original was `C:\\Users\\` but MSYS sees `/c/Users/...` as two tokens: `/c` (drive C:) + `Users/...`

### Scenario 2: Auto-translation disabled (`MSYS_NO_PATHCONV=1`)

Many MSYS2/git-bash environments have `MSYS_NO_PATHCONV=1` to prevent unwanted path mangling (e.g., Docker commands, Git arguments). When this is set, **no automatic path translation occurs**:

```bash
# ❌ Fails with MSYS_NO_PATHCONV=1 — path passed literally
python3 /c/Users/Alexa/script.py
# → python.exe: can't open file 'C:\c\Users\Alexa\script.py': No such file or directory
```

The path `/c/Users/...` is treated as a relative path from the current drive root, producing `C:\c\Users\...`.

## The Fix

### Tiered Path Resolution (recommended)

Use a three-tier fallback for maximum portability:

```bash
HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd )"
# Tier 1: cygpath -w (most portable, handles MSYS_NO_PATHCONV=1 correctly)
if command -v cygpath &>/dev/null; then
    HOOK_DIR=$(cygpath -w "$HOOK_DIR" 2>/dev/null || echo "$HOOK_DIR")
# Tier 2: pwd -W (bash-specific, MSYS2 only, only works with auto-translation)
elif command -v pwd && pwd -W &>/dev/null; then
    HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
fi
# Normalize backslashes to forward slashes for cross-runtime compatibility
HOOK_DIR=${HOOK_DIR//\\//}
```

This gives `C:/Users/Alexa/...` — correct for both Windows Python and bash in all scenarios.

### Simple workaround (single script)

```bash
python3 "$(cygpath -w '/c/Users/Alexa/script.py')"
```

## When This Bites

| Scenario | Wrong | Right |
|----------|-------|-------|
| Hook.sh calling Python | `$(cd ... && pwd)/hook.py` → `C:\\c\\Users\\...` | `cygpath -w` or `pwd -W` → `C:/Users/...` |
| Script passing a path to node | Same double-translation | Tiered fallback |
| Any MSYS→Windows executable call | MSYS `/c/` path passed literally | `cygpath -w` conversion |
| `python3` from uv shim on MSYS2 | `/c/Users/...` → `C:\c\Users\...` | `cygpath -w` mandatory |

## Detecting MSYS_NO_PATHCONV

```bash
# Check current setting
echo "$MSYS_NO_PATHCONV"  # 1 = disabled, empty/0 = enabled

# Temporarily enable translation for one command
MSYS_NO_PATHCONV=0 python3 /c/Users/Alexa/script.py  # may double-translate!

# Better: always use explicit cygpath -w
```

## The `python3` / uv Shim Problem

On Windows MSYS2/git-bash, `python3` often resolves to uv's Python shim at `~/.local/bin/python3`, which is a **native Windows PE32+ executable** — NOT a Cygwin/MSYS port. Because it's native, MSYS NO path translation applies. The path `/c/Users/...` is passed literally and Windows Python interprets it relative to the current drive.

```bash
# Check what python3 actually is
file /c/Users/Alexa/.local/bin/python3
# → PE32+ executable for MS Windows (console), x86-64

# ALWAYS use cygpath -w when calling python3 from MSYS2/bash
python3 "$(cygpath -w "$SCRIPT_PATH")"
```

## winpty for Console Applications

When running Python CLI tools (like `hermes`) from MSYS2/bash, `prompt_toolkit` crashes with `NoConsoleScreenBufferError` because `TERM=xterm-256color` (set by MSYS2) conflicts with the Windows console API. `winpty` provides the Windows console buffer that `prompt_toolkit` expects:

```bash
# Detect MSYS2 and use winpty automatically
if [[ -n "$MSYSTEM" ]] && command -v winpty &>/dev/null; then
    exec winpty hermes -p alexa "$@"
else
    exec hermes -p alexa "$@"
fi
```

## Alternatives

- **`cygpath -w "..."`** — most explicit, works everywhere MSYS does. Slightly slower (subprocess).
- **`pwd -W`** — fast but bash-specific; only works when auto-translation is active.
- **`cmd //c echo %CD%`** — works but fragile and slow.
- **`$LOCALAPPDATA` env var** — always a native Windows path, use when available.

## Rule of Thumb

If you see a path like `C:\\c\\Users\\...` or `/c/c/Users/...` at runtime, MSYS path handling is the cause. Use `cygpath -w` in the shell script that derives the path, then normalize with `${VAR//\\\\//}`. Prefer the tiered fallback pattern for library scripts that need to work across various MSYS2 configurations.
