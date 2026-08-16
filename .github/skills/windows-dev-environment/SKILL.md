---
name: windows-dev-environment
title: Windows Dev Environment (paths, python toolchain, elevation)
description: "Windows/MSYS dev quirks - paths, python tooling, elevation."
version: 1.0.0
author: Hermes Curator
license: MIT
tags: [windows, msys, paths, python, ruff, pyright, elevation, portability]
---

# Windows Dev Environment

Class-level knowledge bank for making code, scripts, and tooling behave on
Windows + git-bash/MSYS. Three subsections, each backed by references/scripts.
For winget/choco package operations see `windows-package-management`.

## When to use
- A script/verification passes on Linux but fails on Windows with no data diff
- Refactoring hardcoded `C:/Users/<user>/...` paths to env-var resolution
- Setting up or debugging ruff / pyright / VS Code Python tooling on Windows
- A user-scope Windows operation is refused because the shell is elevated

## 1. Env-var & path portability (absorbed: `env-path-portability`)

`$env:LOCALAPPDATA` is **PowerShell-only**. Never copy that literal into
bash/python/node files — it silently resolves to an empty or literal string.

| Shell / Lang | Correct form |
|---|---|
| PowerShell | `$env:LOCALAPPDATA\hermes` |
| Bash / sh | `${LOCALAPPDATA:-$HOME/AppData/Local}/hermes` |
| Python | `os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"` |
| Node | `process.env.LOCALAPPDATA || process.env.USERPROFILE` |

Mass-refactor scoping rule: fix **executable resolution** in `.py`/`.js`/`.sh`;
leave doc prose and historical data files alone. Confirm scope before hundreds
of blind edits.

Support: `references/msys-path-normalization.md`, `references/msys2-path-portability.md`,
`references/windows-env-vars.md`, `references/hermes-hooks-windows-path.md`,
`references/unicode-decode-lock-cache.md`, `references/windows-config-lock-reproduction.md`,
`scripts/verify_paths.py`, `scripts/_pathutil.py`, `scripts/install-pathutil.sh`,
`scripts/fix-unicode-decode-skills-hub.md`.

## 2. Python toolchain on Windows (absorbed: `windows-python-toolchain`)

- `python3` does not exist on Windows — always `python`.
- `pyright` must be resolved as `pyright.cmd` in subprocess calls; the extension-less
  file is a POSIX script and raises `[WinError 193]`.
- `str(Path(...))` yields **backslashes** — normalize both sides
  (`.as_posix()` / `.replace("\\", "/")`) before any comparison against a
  forward-slash allowlist. This is a silent FAIL, not an exception.
- CRLF discipline in fixer scripts: read AND write with `newline=""`, or a
  rewrite pass reintroduces CRLF across an LF repo.
- `hermes config set` has limited YAML list support — register MCP servers via
  a `.bat` wrapper with no `args`.
- Prove test failures are pre-existing with the stash A/B pattern:
  `git stash push <changed-files>` then rerun; identical failures = not your regression.
- Remove deprecated VS Code keys (`python.languageServer`, `python.linting.*`,
  `python.formatting.*`).

Support: `references/windows-python-toolchain.md` (full guide),
`references/workspace-python-tooling.md`, `references/workspace-python-tooling-notes.md`,
`references/win32-quality-check.md`, `references/msys-nopathconv-fix.md`.

## 3. De-elevating user-scope operations (absorbed: `windows-deelevation`)

An elevated shell cannot perform user-scope changes (winget/choco uninstall,
user registry, user env vars) — winget returns exit 125. Detect with
`net session >/dev/null 2>&1 && echo ELEVATED`, then run the op under a
limited token:

```bash
schtasks /Create /TN "HermesOp" /TR "cmd /c call C:\path\to\op.bat" /SC ONCE /ST 23:59 /RL LIMITED /F
schtasks /Run /TN "HermesOp"
schtasks /Delete /TN "HermesOp" /F
```
The `.bat` writes one explicit command per target plus a `DONE` marker to a log.
Pitfall: never generate the target list with a comma-delimited `for /f` loop —
`%%` expansion mangles tokens into false "not found" results.
Full recipe: `references/de-elevation-user-scope.md`.

## Verification
- [ ] Refactored paths resolve at runtime in *their own* interpreter, not just PowerShell
- [ ] `ruff --version` + narrow `ruff check`, `pyright.cmd --version` + narrow check pass
- [ ] No CRLF reintroduced (`grep -rlU $'\r' <dir>` empty)
- [ ] Elevation task reached `DONE` and the temp scheduled task was deleted

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Windows Dev Environment (paths, python toolchain, elevation) operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for Windows Dev Environment (paths, python toolchain, elevation).

### Phase 2: Execution

Run the primary Windows Dev Environment (paths, python toolchain, elevation) operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
