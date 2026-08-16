---
name: windows-python-toolchain
title: "Windows Python Toolchain Reference"
description: "Windows Python toolchain: linting/type-checking/MCP quirks, workspace ruff/pyright/VS Code setup, and post-setup verification."
version: 1.0.0
author: "Hermes Agent"
tags: [reference, windows, python, toolchain, pyright, mcp, vscode]
---
# Windows Python Toolchain Reference

## Overview

Automated reasoning and workflow tool for `windows-python-toolchain`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Setting up Python linting/type-checking on Windows
- Debugging subprocess failures when Python tools don't work from MCP servers
- Debugging VSCode settings warnings on Windows
- Testing MCP servers locally on Windows

## `python` vs `python3`

On Windows, `python3` is NOT a valid command — use `python`.

| Context | Use | Don't Use |
|---------|-----|-----------|
| VSCode tasks.json | `"command": "python -m pytest"` | `"command": "python3 -m pytest"` |
| Python subprocess | `subprocess.run(["python", ...])` | `subprocess.run(["python3", ...])` |
| Git Bash terminal | `python` | `python3` |

## `pyright` vs `pyright.cmd`

The `pyright` npm package installs multiple entry points. Only `pyright.cmd` works in subprocess calls:

| File | Type | Subprocess | 
|------|------|-----------|
| `pyright` | POSIX shell script | ❌ `[WinError 193]` |
| `pyright.cmd` | Windows cmd | ✅ |
| `pyright.ps1` | PowerShell | ❌ |

When calling pyright from Python subprocess, resolve to `.cmd`:

```python
import shutil
pyright = shutil.which("pyright.cmd") or shutil.which("pyright") or "pyright"
```

## Path Separators: `str(Path(...))` yields BACKSLASHES on Windows

`str(Path("templates") / "foo" / "bar.md")` on Windows returns
`templates\foo\bar.md` — backslash separators. Any comparison against a
forward-slash allowlist / hardcoded path string **silently fails to match**
(no error, just a wrong result). This bit a fence-verifier twice (2026-07-31):
`str(p.relative_to(dir))` produced backslashes while the `KNOWN_FENCE_CONVENTIONS`
allowlist used forward slashes → false FAIL on Windows-only runs.

Fix — normalize BOTH sides of the comparison:

```python
rel = str(p.relative_to(PROMPTS_DIR)).replace("\\", "/")
if rel not in KNOWN_CONVENTIONS:   # allowlist written with "/"
    ...
```

Rules of thumb:
- Use `Path.as_posix()` or `.replace("\\", "/")` whenever a path string is
  compared, hashed, or stored in a config/report.
- For membership checks against literals, prefer `PurePosixPath`-normalized
  keys, or normalize the input, not the literal.
- When a verification passes on Linux but fails on Windows (or vice versa)
  with zero diff in the data, suspect separator mismatch before anything else.
- This is a SILENT failure mode: no exception, no warning — the check just
  reports FAIL. Include a self-test that compares one known key both ways.

## CRLF Discipline in Fixer Scripts

Python `open(..., "w")` on Windows translates `\n` → `\r\n` (universal
newlines). A fixer that rewrites files via `write_text` silently reintroduces
CRLF into an LF-only repo (observed: 33 files after one fence-fix pass).
Always open with `newline=""` on BOTH read and write:

```python
text = path.read_text(encoding="utf-8", newline="")   # preserve exactly
path.write_text(text, encoding="utf-8", newline="")   # do not translate
```

Verify after any rewrite pass: `grep -rlU $'\r' <dir>` or count files with
`b"\r\n" in p.read_bytes()`. Normalize offenders with the repo's LF tool
(e.g. `.enhance/normalize_lf.py --apply`).

## MCP Server Registration

On Windows, `hermes config set` has limited YAML list support — setting `args.0` creates a mapping, not a list. Workaround: use a `.bat` wrapper.

```bat
@"C:\path\to\python.exe" "C:\path\to\mcp_server.py" %*
```

Register as: `command: "C:\path\to\wrapper.bat"` with no `args`.

For JSON arguments in MCP protocol tests, use forward slashes:
```
C:/Users/Alexa/Desktop/SandBox    # ✅ works
C:\\Users\\...                     # ❌ JSON escape errors
```

## Deprecated VSCode Settings

These generate warnings in VS Code settings UI:

| Setting | Fix |
|---------|-----|
| `python.languageServer: "Pylance"` | Remove — auto-detected |
| `python.linting.enabled: true` | Remove — Ruff extension handles this |
| `python.linting.ruffEnabled: true` | Remove — Ruff extension handles this |
| `python.formatting.provider: "none"` | Remove — Ruff extension handles this |

## Duplicate `[language]` Blocks

JSON allows duplicate keys — the last one wins silently. After editing `settings.json`:
```bash
python -c "import json; json.load(open('.vscode/settings.json'))" && echo "valid"
```

Visually inspect for any `[python]` (or other language block) appearing twice.

## MCP Server Test Snippet

```bash
printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1"}}}\n{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}\n{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}\n' | python path/to/mcp_server.py
```


## Test Runners: POSIX Venv Probe Fails

Some repos' canonical test runners probe POSIX venv layouts and fail on Windows. Example: hermes-agent's `scripts/run_tests.sh` checks for `.venv` or `venv/bin/...` and exits `no virtualenv with pytest found`, even though the venv exists at `venv/Scripts/python.exe` (Windows layout).

**Fix:** invoke pytest directly against the venv interpreter, replicating the runner's env:

```bash
cd <repo> && TZ=UTC LANG=C.UTF-8 venv/Scripts/python.exe -m pytest <files> -q
```

Match the runner's per-file isolation (`python -m pytest <file>` per subprocess) when cross-file module leakage is a concern. (Verified 2026-07-31: venv `pytest 9.1.1` present, runner's probe still misses it.)

## Proving Test Failures Are Pre-Existing (Stash A/B)

When a change is followed by test failures, do NOT assume your edit caused them — prove it before touching unrelated code:

```bash
git stash push <changed-files>   # stash ONLY your edits
# re-run the exact same failing tests
# identical failures => pre-existing (legacy/environment), NOT your regression
git stash pop                    # restore your work
```

**Session example (2026-07-31):** after a 2-line `UnicodeDecodeError` catch patch to `hermes-agent/tools/skills_hub.py`, 7 repo tests failed. Stashing the change reproduced the identical 7 failures → the fix was innocent; the failures were environment/legacy. Report pre-existing failures as such with the stash-A/B evidence instead of "fixing" unrelated code.

**Pitfall:** a "verification unverified" flag after code edits is satisfied by compiling + linting + behavioral asserts + the stash-A/B test run — assemble the evidence, don't re-edit blindly.

## Workspace Tooling Setup (ruff / pyright / VS Code)

Installing and configuring Python editor tooling in a workspace — full guide at
`references/workspace-python-tooling.md`:

- **Setup order:** inspect existing manifests (`requirements.txt`,
  `pyproject.toml`, `.ruff.toml`, `pyrightconfig.json`, `.vscode/settings.json`)
  → add/repair config → align VS Code settings → narrow validation pass → expand.
- **ruff:** prefer `.ruff.toml`; `target-version` uses `py311`-style variants
  (`python-version = "3.11"` is invalid and blocks everything). Add `COM812` to
  `ignore` (formatter conflict), drop removed `UP038`. Cookiecutter/Jinja
  templates crash the TOML parser → top-level `exclude = ["cookiecutter-*"]`.
  Django: `RUF012` from model fields and `PLC0415` lazy imports are expected.
- **Sub-repos without `.ruff.toml` silently inherit the root config** — check
  root `target-version` matches each sub-repo's Python.
- **pyright:** run narrow (single file/folder) first; full-monorepo runs time
  out. Tune `exclude` before broadening.
- **VS Code:** keep interpreter/linter/language-server settings consistent; no
  stale backend interpreter paths. See also the deprecated-settings table above.

## Post-Setup Verification Sequence (win32 quality checks)

After any config change, run the ordered checks — full sequence at
`references/win32-quality-check.md`:

1. **VSCode JSON integrity** — parse every `.vscode/*.json`, check duplicate
   language blocks (`grep -n '^  "\[' settings.json | sort | uniq -d`), no
   deprecated `python.languageServer`/`python.linting.*`/`python.formatting.*`
   keys, no `python3` in tasks.json.
2. **Linters run** — `ruff --version` + narrow `ruff check`, `pyright --version`
   + narrow check.
3. **markdownlint** — remove `globs` from `.markdownlintrc.json`; always use
   `--no-globs` on the CLI (a `globs` entry makes it scan >100 files).
4. **Tool availability** — eslint, prettier, cspell, pre-commit, ruff, pyright,
   bunx; cspell.json / .pre-commit-config.yaml / cliff.toml exist and parse.
5. **MCP pre-registration** — ALWAYS `hermes mcp test <server>` BEFORE adding it
   to `config.yaml`; a failing server blocks tool discovery for all servers at
   startup.
- **Pitfall:** the patch tool can corrupt `- ` list markers to `|- ` — after
  patching markdown lists, immediately `read_file` to verify, and use
  `write_file` to rewrite the section if corrupted.

## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Reference Files

- `references/msys-nopathconv-fix.md` — `MSYS_NO_PATHCONV=1` workaround when calling native Windows Python from git-bash/MSYS2. Prevents `C:\c\` path corruption.

## Related Skills

- `software-development/python-quality` — Python quality workflow
- `vscode-workspace-configurator` — VSCode config templates (note: protected, cannot auto-patch)
