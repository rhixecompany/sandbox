---
name: async-migration-patterns
title: "Async Migration Patterns"
description: "Convert bash hooks and synchronous Python scripts to asyncio. Covers the thin shell-wrapper pattern, shared async lib design, and batch conversion via delegate_task."
version: 1.0.0
author: Alexa
license: MIT
tags: [async, migration, python, hooks, refactoring]
---
# Async Migration Patterns

Techniques for converting bash hooks and Python scripts to async, proven in production on 82 Python scripts and 3 hook packages.

## Architecture: Bash Hook → Async Python

Hermes hooks are shell scripts called by the agent at lifecycle events. Convert them to async Python without changing the execution model:

```
hook.sh (thin bash wrapper)      ← Hermes calls this (hooks.json entrypoint)
  └─ exec python3 hook.py        ← reads stdin JSON, dispatches to async handlers
       └─ import lib.py          ← shared async utilities (sibling directory)
```

### Thin Wrapper (`hook.sh`)
Keep this 2-line bash wrapper so Hermes's hook execution model needs zero changes:
```bash
#!/usr/bin/env bash
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/hook.py"
```

### Async Entrypoint (`hook.py`)
One file per hook package, dispatching by event type:
```python
#!/usr/bin/env python3
import asyncio, sys
from pathlib import Path

_HOOK_DIR = Path(__file__).resolve().parent
_LIB_DIR = _HOOK_DIR.parent
if str(_LIB_DIR) not in sys.path:
    sys.path.insert(0, str(_LIB_DIR))

from lib import log_info, read_payload

_EVENT_HANDLERS = {
    "session_start": handle_session_start,
    "session_end": handle_session_end,
}

async def main():
    payload = read_payload()
    handler = _EVENT_HANDLERS.get(payload.get("event", ""))
    if handler is None:
        sys.exit(1)
    await handler(payload)

if __name__ == "__main__":
    asyncio.run(main())
```

### Shared Library (`lib.py`)
Stdlib-only async utilities — place one directory above hook packages:

| Function | Pattern |
|----------|---------|
| `log_info`, `log_error` | Colored stderr via async `print(..., file=sys.stderr)` |
| `write_jsonl(file, record)` | Append JSONL via `asyncio.to_thread(lambda: open(file, "a").write(...))` |
| `run_cmd(*args)` | `asyncio.create_subprocess_exec` with timeout |
| `run_git(*args)` | Wrapper around `run_cmd("git", *args)` |
| `read_payload()` | Sync `json.loads(sys.stdin.read())` — stdin is a one-shot pipe |

## Batch Script Conversion via delegate_task

For 50+ scripts, dispatch parallel subagents rather than converting one-by-one:

```python
delegate_task(tasks=[
    {"goal": f"Convert batch N to async", "context": CONVERSION_RULES},
    # ... up to 6 parallel
])
```

### Conversion Rules (pass as context)

For each .py file:
1. Add `import asyncio` at top
2. Change `def main():` to `async def main():`
3. Change `if __name__ == "__main__": main()` to `asyncio.run(main())`
4. Wrap `subprocess.run()` / `check_output()` with `await asyncio.to_thread()`
5. Wrap file I/O with `await asyncio.to_thread()` for concurrent operations
6. Keep CPU-bound processing (regex, yaml, json parsing) synchronous
7. Verify syntax after each file: `python3 -c "import ast; ast.parse(open('FILE').read())"`
8. Skip .sh, .ps1, .cjs, .js, .json files

### Verification After Batch

**Subagent summaries are self-reports — always run a systematic independent verification pass.**

```python
import ast, os, subprocess, sys
from pathlib import Path

target = Path("scripts")  # directory subagents wrote to

results = {"pass": 0, "syntax_err": 0, "missing_pattern": 0, "regression": 0}

for f in sorted(target.glob("*.py")):
    text = f.read_text(encoding="utf-8")

    # 1. Syntax check
    try:
        tree = ast.parse(text)
    except SyntaxError as e:
        print(f"SYNTAX ERROR: {f.name} — {e}")
        results["syntax_err"] += 1
        continue

    # 2. Pattern check — has async def OR asyncio.run?
    has_async_def = any(isinstance(n, ast.AsyncFunctionDef) for n in ast.walk(tree))
    has_asyncio_run = any(
        isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        and n.func.attr == "run" and isinstance(n.func.value, ast.Name)
        and n.func.value.id == "asyncio"
        for n in ast.walk(tree)
    )
    if not (has_async_def or has_asyncio_run):
        print(f"MISSING async: {f.name}")
        results["missing_pattern"] += 1
        continue

    # 3. Regression: missing 'import os' despite os usage
    if ("os.environ" in text or "os.path" in text) and "import os" not in text:
        print(f"REGRESSION: {f.name} uses os but missing 'import os'")
        results["regression"] += 1

    # 4. Regression: sync subprocess.run without async wrapper
    if "subprocess.run" in text and "asyncio.to_thread" not in text:
        print(f"REGRESSION: {f.name} has bare subprocess.run — no async wrapper")
        results["regression"] += 1

    results["pass"] += 1

print(f"\nResults: {results['pass']} pass, {results['syntax_err']} syntax errors, "
      f"{results['missing_pattern']} missing async, {results['regression']} regressions")
```

### Hook Wrapper Verification (if hooks were converted)

For every hook package, verify the `.sh` wrapper correctly calls `hook.py`:

```python
for pkg in sorted(Path("hooks").iterdir()):
    if not pkg.is_dir() or pkg.name == "__pycache__":
        continue
    sh = pkg / "hook.sh"
    py = pkg / "hook.py"
    if sh.exists() and "hook.py" not in sh.read_text(encoding="utf-8"):
        print(f"WRAPPER MISMATCH: {pkg.name}/hook.sh doesn't reference hook.py")
```

### Smoke Tests

Run a representative sample — not every file, but at least one from each subagent batch:

```bash
# Verify imports work
python3 -c "import sys; sys.path.insert(0, 'scripts'); import validate_prompts; print('OK')"
python3 -c "import sys; sys.path.insert(0, 'scripts'); import generate_skills; print('OK')"

# Run with --help to catch runtime errors
python3 scripts/validate_prompts.py --help > /dev/null 2>&1 && echo "validate_prompts OK"
python3 scripts/generate_skills.py --help > /dev/null 2>&1 && echo "generate_skills OK"
```

### Timed-Out Tasks

Subagents that timed out may have left partial output. **Always verify timed-out files independently** using the same checks above. Do not trust the partial output as-is.

## Pitfalls

- **Security scanner blocks edits to flagged skills.** Pre-existing dangerous patterns (rm -rf examples, sudo chmod 777) in a skill cause the security scanner to deny ANY file write to that skill, including adding innocent reference files. Fix: create a new skill rather than fighting the scanner.
- **MSYS path mangling on Windows.** `python3 /c/Users/.../hook.py` becomes `C:\c\Users\...` and fails. Use `cd` into the directory first, then `python3 hook.py`.
- **`hooks.json` entrypoint stays unchanged.** Pointing at `hook.sh` means zero config changes — `hook.sh` is the thin wrapper that execs Python.
- **`asyncio.to_thread` requires Python 3.9+.** On older runtimes, fall back to `loop.run_in_executor(None, sync_fn)`.
- **Not all scripts benefit from async.** Scripts that read one file, process, and exit gain nothing. The value is in concurrent I/O (writing to multiple log files, running subprocesses in parallel) and future extensibility.
- **Preserve old .sh files for rollback.** Don't delete originals — keep them alongside new .py files. Revert by editing hook.sh wrapper or updating hooks.json.
- **Subagents assume globals that don't exist.** When scripts reference a global like `SANDBOX` that other files in the same directory define, the subagent may write code assuming it's available without defining it. Always check for undefined symbols in subagent-created files by smoke-testing a representative sample. The `fix-frontmatter.py` script in the actual 82-script conversion had this exact bug — it used `SANDBOX` (no definition) and `os.environ` without `import os`.
