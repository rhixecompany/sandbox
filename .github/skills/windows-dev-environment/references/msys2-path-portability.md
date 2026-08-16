---
name: windows-msys2-path-portability
author: Hermes Agent
title: "Windows MSYS2 Path Portability"
description: "Use when debugging path translation failures between MSYS2/git-bash and native Windows executables. Covers MSYS_NO_PATHCONV, cygpath -w, winpty, hook.sh path resolution, and .sh/.bat wrapper patterns."
version: 1.0.0
tags: [windows, msys2, path, git-bash, cygpath, winpty]
---
# Windows MSYS2 Path Portability

## Overview

Automated reasoning and workflow tool for `windows-msys2-path-portability`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- A native Windows executable (python3, hermes, node.exe) called from MSYS2/bash can't find a file at `/c/Users/...`
- A script running under MSYS2/git-bash crashes with `NoConsoleScreenBufferError`
- Creating shell wrappers that must work from both cmd.exe and MSYS2/bash
- Writing Hermes hooks or scripts that delegate to Python on Windows
- **`hermes plugins enable/disable` fails with PermissionError** from a running TUI session — config file lock, not a missing binary. See `windows-config-lock-reproduction.md` (same directory).

## Root Cause: MSYS_NO_PATHCONV

MSYS2 (and git-bash) can perform automatic path translation: when you pass `/c/Users/foo` to a native Windows executable, it converts it to `C:\Users\foo`. However:

- `MSYS_NO_PATHCONV=1` **disables this translation** (common in Hermes TUI and VS Code terminals)
- The uv Python shim (`python3`) is a native Windows PE32+ exe — it receives paths literally
- Result: `python3 /c/Users/...` → `C:\c\Users\...` (wrong drive-letter translation)

## The Fix: cygpath -w

```bash
python3 "$(cygpath -w /c/Users/You/script.py)"
```

`cygpath -w` converts MSYS paths to Windows format (`C:\Users\...`). Always available in MSYS2, git-bash, and Cygwin.

## 3-Tier Path Resolution

```bash
RESOLVED="$(
  cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd
)"
if command -v cygpath &>/dev/null; then
    RESOLVED=$(cygpath -w "$RESOLVED" 2>/dev/null || echo "$RESOLVED")
elif command -v pwd && pwd -W &>/dev/null; then
    RESOLVED="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -W)"
fi
RESOLVED=${RESOLVED//\\//}  # Normalize backslashes to forward slashes
exec python3 "$RESOLVED/hook.py"
```

This 3-tier fallback handles:
1. **cygpath -w** — MSYS2, Cygwin, git-bash
2. **pwd -W** — bash-specific (git-bash)
3. **plain pwd** — Last resort (may fail with native tools)

## winpty for Console Apps

When launching native Windows console apps from MSYS2/bash:

```bash
# Without winpty: NoConsoleScreenBufferError
hermes -p profile
# With winpty: works
winpty hermes -p profile
```

**Root cause:** MSYS2 sets `TERM=xterm-256color`. Windows prompt_toolkit detects this and tries to use Win32 console buffer APIs, but inside MSYS2 there is no Win32 console buffer — only a PTY.

### Detection in wrappers

```bash
#!/usr/bin/env bash
if [[ -n "$MSYSTEM" ]] && command -v winpty &>/dev/null; then
    exec winpty hermes -p profile "$@"
else
    exec hermes -p profile "$@"
fi
```

## Tool Behavior Reference

| Tool | Type | Path Issue? | Fix |
|------|------|-------------|-----|
| `python3` (uv shim) | Native Windows | Yes — rejects MSYS paths | `cygpath -w` |
| `python` (system) | Native Windows | Yes | `cygpath -w` |
| `git` | MSYS2-built | No | None needed |
| `hermes` | Native Windows | Yes (console) | `winpty hermes` |
| bash builtins | Shell | No | None needed |
| grep, sed, awk | MSYS2-built | No | None needed |

## .bat vs .sh Wrapper Strategy

| Wrapper | Runs in | Pattern |
|---------|---------|---------|
| `.bat` | cmd.exe, PowerShell | `hermes -p profile %*` |
| `.sh` | MSYS2/bash, Cygwin | MSYSTEM+winpty detection |

Always provide both for profiles/aliases that need cross-environment launching.

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| `pwd -W` not available on Linux/macOS | Only use `pwd -W` inside MSYS2 fallback, never as the sole resolver |
| `cygpath` not on PATH | Test with `command -v` before using |
| .bat file paths contain spaces | Double-quote all paths in .bat files |
| uv python3 shim vs system python | Both are native Windows exes — both need `cygpath -w` |
| `Path(args.X).resolve()` corrupts MSYS paths | Use the shared `_pathutil.resolve_path()` helper (see `../scripts/_pathutil.py`) |
| **Hermes config.yaml file lock (Windows)** — running Hermes TUI holds `config.yaml` open, so sequential `hermes plugins enable/disable` calls fail with `PermissionError: The process cannot access the file because it is being used by another process` after the first write | **Workaround:** use retry-with-exponential-backoff (1.5× delay per attempt, 2-3 attempts) between consecutive `plugins enable` calls. Or batch all changes into a single `hermes config edit` / direct `patch` on `config.yaml`. The first write per batch succeeds (file released after write), subsequent writes race with the running TUI session's own config reads. |
