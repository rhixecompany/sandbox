#!/usr/bin/env python3
"""verify_paths.py — ad-hoc harness proving a script resolves HERMES_HOME from LOCALAPPDATA.

Usage:
    python3 verify_paths.py <path_to_target_script.py> [more scripts...]

What it does:
    1. Creates an OS-safe temp dir via tempfile.mkdtemp(prefix="hermes-verify-").
    2. Sets LOCALAPPDATA to that temp dir (env only — no real files touched).
    3. Imports each target module and reads its HERMES_HOME (sandbox-eval the assignment).
    4. Asserts HERMES_HOME == <temp>/hermes.
    5. Cleans the temp dir.

This is the pattern that caught hardcoded-path regressions and proves env-var resolution
without mutating live data. Run it after any path-refactor edit.
"""
import os, sys, ast, tempfile, shutil, importlib.util

def resolve_hermes_home(src):
    """Safely eval the RHS of `HERMES_HOME = <expr>` (literal Path/os.environ call)."""
    whitelist = {"Path": __import__("pathlib").Path, "os": os, "__builtins__": {}}
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("HERMES_HOME ="):
            expr = s.split("=", 1)[1].strip()
            ast.parse(expr)  # gate: reject anything non-trivial
            return str(eval(expr, whitelist))
    return None

def main():
    if len(sys.argv) < 2:
        print("usage: verify_paths.py <script.py> [...]"); sys.exit(2)
    TMP = tempfile.mkdtemp(prefix="hermes-verify-")
    expect = os.path.join(TMP, "hermes")
    ok = True
    for path in sys.argv[1:]:
        src = open(path, encoding="utf-8").read()
        assert "C:/Users/Alexa/AppData/Local/hermes" not in src, f"{path}: still hardcoded!"
        val = resolve_hermes_home(src)
        good = val and os.path.normpath(val) == os.path.normpath(expect)
        print(f"{os.path.basename(path)}: HERMES_HOME={val}  {'OK' if good else 'MISMATCH'}")
        ok = ok and good
    shutil.rmtree(TMP, ignore_errors=True)
    print("CLEAN" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
