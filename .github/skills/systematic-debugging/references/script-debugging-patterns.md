---
name: script-debugging-patterns
title: "Script Debugging Patterns — Python/Shell runner diagnosis"
description: "Diagnose silent exits, missing artifacts, and runner/script mismatches in orchestrators and CLI scripts. Uses root-cause-first checks instead of blind retries."
version: 1.0.0
author: Alexa
license: MIT
tags: [debugging, python, shell, orchestration, runner]
---
# Script Debugging Patterns

Use when a script or runner appears to start, then silently exit, fail with missing-file gates, or mismatch expected artifacts.

## Overview

Automated reasoning and workflow tool for `script-debugging-patterns`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use This Pattern

- Runner prints startup banner but never reaches phase/secondary steps
- Gate checks complain about missing files that were just written
- Script fails because another tool wrote to a different path than expected
- CLI wiring fails because `--output` means different things in different tools
- Subprocess logs are truncated by the terminal; need module-level inspection

## Root-Cause Checklist

1. **Inspect entrypoint invocation**
   - Confirm `if __name__ == "__main__": asyncio.run(main())` or equivalent is present.
   - For async Python, distinguish bare `main()` from `await main()`; calling a coroutine without await returns a coroutine object.

2. **Log state transitions, don't just print once**
   - Add prints at main entry, before/after each awaited phase/subprocess, and in exception handlers.
   - Capture timeout: `python script.py > /tmp/run.log 2>&1; echo "EXIT_CODE=$?"` and inspect the full log.

3. **Trace actual on-disk paths, then compare to code expectations**
   - Use explicit temporary verification scripts/modules that snapshot `Path.exists()` and sizes before/after.
   - When paths are constructed via repeated `.parent` segments, print the resolved absolute path and assert existence before gating.

4. **Verify CLI flag contracts, not just presence**
   - Run `python script.py --help` and inspect the actual parser output.
   - If a script ignores `--report` or `--output`, check whether the installed file matches the patched source.

5. **Normalize verification artifacts; don't blindly append**
   - If a progress/verification md is appended on every run, old blocked entries persist even after later passes.
   - After a green run, rewrite the verification file from a clean final-state template or snapshot the tail of `run.log`.

## Fixing Root Causes, Not Symptoms

- When a script assumes a harmless missing intermediate artifact exists, **create a minimal no-op fallback file** instead of deleting or inlining everything.
- When two scripts disagree on flag semantics (`--output` as path vs. format), **update the caller/wiring** to match the real contract, verified by running both manually.

## Module-import Verification Pattern

When runner logs disappear into subprocess stdout, bypass terminal truncation by importing the module programmatically:

```python
import asyncio
import importlib.util
from pathlib import Path

RUNNER = Path(r"C:\...\execute_all_prompts.py")
spec = importlib.util.spec_from_file_location("execute_all_prompts", str(RUNNER))
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
await mod.phaseN()
```

This avoids shell-bound stdout bouncing and lets you inspect phase state directly.

## Reproducible Verification Pattern

Use an ad-hoc temp script to prove behavior change instead of trusting transcript evidence alone:

```python
# temp script: create minimal inputs, run command/check outputs, cleanup temp files
import tempfile, subprocess, sys
from pathlib import Path

REPO = Path(r"C:\Users\Alexa\Desktop\SandBox")
SCRIPT = REPO / ".github/scripts/validate_vscode_configs.py"
EMPTY_DIR = Path(tempfile.gettempdir()) / "hermes-verify-empty-vscode"
REPORT = EMPTY_DIR / "report.txt"
if EMPTY_DIR.exists():
    for f in EMPTY_DIR.rglob("*"):
        f.unlink() if f.is_file() else None
    EMPTY_DIR.rmdir()
EMPTY_DIR.mkdir(parents=True, exist_ok=True)

p = subprocess.run(
    [sys.executable, str(SCRIPT), "--workspace", str(EMPTY_DIR), "--allow-empty", "--report", str(REPORT)],
    capture_output=True,
    text=True,
    cwd=str(REPO),
)
assert p.returncode == 0
assert REPORT.exists() and REPORT.read_text(encoding="utf-8").strip() != ""

# cleanup
if REPORT.exists():
    REPORT.unlink()
EMPTY_DIR.rmdir()
```

## Verification Checklist

- [ ] Entrypoint prints and awaits phases in order
- [ ] All expected on-disk artifacts exist at the resolved absolute paths
- [ ] Runner exit code reflects actual phase completion, not intermediate state
- [ ] CLI flag semantics verified from live `--help`/parser, not assumed
- [ ] Verification/progress artifacts reflect final run state, not stale prior failures

## Pitfalls

- **YAML frontmatter regex capture drops trailing newline.** `re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)` captures the fm string between the \n after `---` and the \n before `---`, so fm never ends with `\n`. Appending a YAML key with `fm = fm + f"newkey: value\n"` merges onto the last line (`oldkey: valuenewkey: value`). **Fix:** `if not fm.endswith("\n"): fm += "\n"` before any prepend/append. Applies to any script editing YAML frontmatter in SKILL.md/.prompt.md files.
- **Ad-hoc temp scripts must use native Windows paths, not MSYS.** Pass `"C:/Users/.../hermes-verify-x.py"` not MSYS `/c/Users/...` — the mount layer rewrites `/c/` to `\\c\` and python3 fails `[Errno 2]`. Write and execute in one statement so a stray `rm` doesn't wipe the script before retry.
