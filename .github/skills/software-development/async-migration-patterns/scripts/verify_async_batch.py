#!/usr/bin/env python3
"""Verify a batch of async-converted scripts: syntax, async pattern, undefined-global smoke test.

Catches bugs that string-matching misses — e.g. a script using `SANDBOX` (undefined global)
or `os.environ` without `import os`. String checks see "os.environ" and assume import os is
present; this script actually imports the module to surface NameError at runtime.

Usage: python3 scripts/verify_async_batch.py <scripts_dir>
"""
import ast
import subprocess
import sys
from pathlib import Path


def verify_script(path: Path) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8", errors="replace")

    # 1. Syntax
    try:
        tree = ast.parse(text)
    except SyntaxError as e:
        return False, f"SYNTAX ERROR: {e}"

    # 2. Async pattern (async def OR asyncio.run)
    has_async = any(isinstance(n, ast.AsyncFunctionDef) for n in ast.walk(tree))
    has_run = any(
        isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
        and n.func.attr == "run" and isinstance(n.func.value, ast.Name)
        and n.func.value.id == "asyncio"
        for n in ast.walk(tree)
    )
    if not (has_async or has_run):
        return False, "MISSING async pattern"

    # 3. Runtime smoke test — catches undefined globals + missing imports
    mod = path.stem
    test = subprocess.run(
        [sys.executable, "-c", f"import sys; sys.path.insert(0, r'{path.parent}'); import {mod}"],
        capture_output=True, text=True, timeout=30,
    )
    if test.returncode != 0:
        # Filter expected --help/arg errors from real import errors
        if "NameError" in test.stderr or "ImportError" in test.stderr:
            last = test.stderr.strip().splitlines()[-1]
            return False, f"RUNTIME: {last}"

    return True, "OK"


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("scripts")
    fail = 0
    for f in sorted(target.glob("*.py")):
        ok, msg = verify_script(f)
        if not ok:
            print(f"✗ {f.name}: {msg}")
            fail += 1
    print(f"\n{'✓ ALL PASS' if fail == 0 else f'✗ {fail} FAILED'}")
    sys.exit(1 if fail else 0)
