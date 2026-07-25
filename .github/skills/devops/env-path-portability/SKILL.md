---
name: env-path-portability
title: "Env-Var Path Portability ($env:LOCALAPPDATA pitfall)"
description: "Resolve OS/user paths portably inside scripts and skill docs. Covers the $env:LOCALAPPDATA PowerShell-only trap, native per-shell env-var forms (python/node/bash), and the executable-code-only vs doc-prose scoping rule for mass path refactors."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [paths, env-vars, windows, portability, localization, shell]
---

# Env-Path Portability

## When to Use

- Refactoring hardcoded `C:/Users/<user>/...` or `/home/<user>/...` paths to env-var resolution.
- Writing scripts (`.py`/`.js`/`.cjs`/`.sh`) that locate app data dirs (Hermes lives in `AppData\Local`).
- User asks to "use `$env:LOCALAPPDATA\...` for paths" or similar — interpret correctly per runtime.
- Auditing a skill library / repo for machine-specific path leaks.

## CRITICAL: `$env:LOCALAPPDATA` is PowerShell-only

If the instruction literally says `$env:LOCALAPPDATA`, do **NOT** copy that string into non-PowerShell files. It is PowerShell syntax that:
- in **bash/sh**: `$env:LOCALAPPDATA` → empty (not a bash var) → broken path
- in **python/node**: `"$env:LOCALAPPDATA\hermes"` → a literal string, never resolved → broken path
- backslash `\` is also an escape char in bash/double-quoted strings

**Correct native forms (all resolve at runtime):**

| Shell / Lang | Form |
|---|---|
| PowerShell | `$env:LOCALAPPDATA\hermes` |
| Bash / sh | `${LOCALAPPDATA:-$HOME/AppData/Local}/hermes` |
| Python | `os.environ.get("LOCALAPPDATA", os.path.expanduser("~/AppData/Local")) + "/hermes"` |
| Node | `process.env.LOCALAPPDATA || process.env.USERPROFILE || 'C:\\Users\\Alexa'` |

**Availability (verified):** `LOCALAPPDATA` is set in Git Bash/MSYS, python, node, and sh on Windows. `USERPROFILE` and `HOME` also exist but point to different dirs — `LOCALAPPDATA` is the *correct* var for `AppData\Local` (Hermes install dir), not `USERPROFILE`/`HOME`.

## Scoping rule (mass refactors)

When asked to "enhance all scripts,skills,hooks to use $env:VAR":
1. **Separate executable code from prose.** A grep for the hardcoded path returns both:
   - **Executable resolution** in `.py`/`.js`/`.sh` source → in-scope, fix it.
   - **Doc prose / example commands** in `.md` (e.g. 225 SKILL.md files, 900+ mentions) → NOT runtime resolution; converting makes docs cryptic with zero runtime gain. Leave unless user explicitly wants full literal coverage.
2. **Hooks** often already use env vars (`$HOME`, `$LOCALAPPDATA`) — grep first; usually 0 matches.
3. **Data/log files** (`.jsonl`, `.json` snapshots) are historical artifacts — not code; leave.
4. Confirm scope with the user (clarify) before 900 blind edits.

## Safe edit procedure

1. Grep to size the blast radius: `grep -rln "C:/Users/<user>/AppData/Local/hermes" --include=*.py --include=*.js --include=*.sh .`
2. Patch each executable resolution line to the native env-var form (see table).
3. For python, build subpaths with `os.path.join(HERMES_HOME, "skills")` — never string-concatenate across platforms.
4. **Verify** (see `scripts/verify_paths.py`): set `LOCALAPPDATA` to a temp dir, import/exec the module, assert `HERMES_HOME` resolves to `<temp>/hermes`. Also `py_compile` / `node --check` / `bash -n`.

## Pitfalls

- **Don't paste `$env:` into .py/.sh** — it is silent (resolves to nothing) until the path is used, then breaks mysteriously.
- **Don't use `HOME`/`USERPROFILE` for `AppData\Local`** — they point to the user home, not the Local app-data dir. Hermes is in `LOCALAPPDATA`.
- **Stale `.pyc` bytecode** can retain old hardcoded strings in greps — clear `__pycache__` after editing source.
- **`eval()` in verify harnesses**: sandbox it (empty `__builtins__`, whitelist `Path`/`os`, gate with `ast.parse`) and only run on your own source, never user input.
- **Mass prose edits waste context** and degrade docs — scope to executable code unless told otherwise.

## Verification

```bash
# no hardcoded path remains in SOURCE (ignore .pyc / .jsonl data)
grep -rn "C:/Users/Alexa/AppData/Local/hermes" scripts/*.py scripts/*.js scripts/*.sh 2>/dev/null || echo CLEAN
# runtime proof
python3 -c "import os; print(os.environ['LOCALAPPDATA']+'/hermes')"
```

## Assets

- `scripts/verify_paths.py` — temp-redirect harness: sets `LOCALAPPDATA` to `tempfile.mkdtemp(prefix="hermes-verify-")`, imports target modules, asserts `HERMES_HOME` resolves under the temp dir. Run, then self-clean.
- `references/windows-env-vars.md` — quick reference: `LOCALAPPDATA`, `APPDATA`, `USERPROFILE`, `HOME`, availability per shell.
- `references/msys-path-normalization.md` — MSYS/Git Bash path double-translation: `pwd -W`, `cygpath -w`, and the stray `\\c\\` bug when passing MSYS paths to Windows-native executables.
- `references/hermes-hooks-windows-path.md` — concrete walkthrough for fixing Hermes hook path resolution on Windows: wrapper scripts, full-path config, and allowlist re-approval.

## Related

- `pending-store-apply` — drains Hermes native pending store; its scripts MUST use the LOCALAPPDATA form above.
- `hermes-system-maintenance` — key paths section; keep using `LOCALAPPDATA`, not hardcoded user paths.
