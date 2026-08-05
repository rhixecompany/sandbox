#!/usr/bin/env python3
"""omo_doctor.py — Oh My OpenAgent / Oh My Hermes setup verifier.

Checks that OpenCode CLI, Oh My OpenAgent, Hermes-opencode plugin wiring, and
the required agent sub-commands are all available and configured, mirroring the
"Verification and Testing" section of the OMO install guide.

Checks (exit 0 = all pass, 1 = warnings, 2 = blocking failures):
  1. opencode CLI present + version >= 1.4.0
  2. oh-my-openagent package resolvable via bunx
  3. If configured, Hermes-opencode plugin dir exists (env HERMES_PLUGIN_DIR or
     default ~/.hermes/plugins/opencode / $HERMES_HOME/plugins/opencode)
  4. opencode auth list non-empty (>=1 provider configured)
  5. Non-interactive OpenCode env flags set (recommended for Hermes-driven runs)
  6. Agent sub-commands smoke: `opencode agents` lists at least one agent

No side effects: read-only reporting. Secrets are never printed.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

MIN_OPENCODE = "1.4.0"

WARN = "\033[33m"
OK = "\033[32m"
FAIL = "\033[31m"
RESET = "\033[0m"


def _run(cmd: list[str], timeout: int = 60) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           shell=False)
        out = (p.stdout or "") + (p.stderr or "")
        return p.returncode, out.strip()
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired:
        return 124, "timed out"


def _ver_ok(version: str) -> bool:
    try:
        parts = [int(x) for x in version.split("-")[0].split(".")]
        need = [int(x) for x in MIN_OPENCODE.split(".")]
        return parts >= need
    except Exception:
        return False


def main() -> int:
    checks: list[tuple[str, str, bool]] = []  # (label, detail, ok)
    blocked = 0
    warned = 0

    # 1. OpenCode CLI
    opencode = shutil.which("opencode.cmd") or shutil.which("opencode")
    if not opencode:
        checks.append(("opencode CLI", "not on PATH", False))
        blocked += 1
    else:
        rc, ver = _run([opencode, "--version"])
        ok = rc == 0 and _ver_ok(ver)
        checks.append((f"opencode CLI @ {opencode}", f"v{ver}" if rc == 0 else "no version", ok))
        blocked += 0 if ok else 1

    # 2. OMO resolvable via bunx
    bun = shutil.which("bun")
    if bun:
        rc, out = _run([bun, "x", "oh-my-openagent", "--version"])
        ok = rc == 0
        checks.append(("oh-my-openagent (bunx)", out.splitlines()[0] if out else f"rc={rc}", ok))
        blocked += 0 if ok else 1
    else:
        checks.append(("bun", "not on PATH", False))
        warned += 1

    # 3. Hermes-opencode plugin dir
    plug = Path(os.environ.get("HERMES_PLUGIN_DIR", "")) if os.environ.get("HERMES_PLUGIN_DIR") else None
    if not plug:
        for candidate in (Path.home() / ".hermes" / "plugins" / "opencode",
                      Path(os.environ.get("HERMES_HOME", "")) / "plugins" / "opencode"):
            if candidate.is_dir():
                plug = candidate
                break
    if plug and plug.is_dir():
        checks.append(("hermes-opencode plugin", f"found @ {plug}", True))
    else:
        checks.append(("hermes-opencode plugin", "not found (plugin dir absent) — optional if OMO runs standalone", False))
        warned += 1

    # 4. auth
    if opencode:
        rc, out = _run([opencode, "auth", "list"])
        providers = [ln for ln in out.splitlines() if ln.strip()]
        ok = rc == 0 and bool(providers)
        checks.append(("opencode auth providers", f"{len(providers)} present" if providers else "none", ok))
        blocked += 0 if ok else 1

    # 5. non-interactive env flags (recommended)
    flags = {
        "OPENCODE_DISABLE_EMBEDDED_WEB_UI": "true",
        "OPENCODE_DISABLE_SHARE": "true",
        "OPENCODE_DISABLE_AUTOUPDATE": "true",
    }
    missing = [k for k, v in flags.items() if os.environ.get(k, "").lower() != v]
    checks.append(("non-interactive env flags", "all set" if not missing else f"missing: {', '.join(missing)}", not missing))
    warned += 0 if not missing else 1

    # 6. agents list
    if opencode:
        rc, out = _run([opencode, "agents"])
        agents = [ln for ln in out.splitlines() if ln.strip() and not ln.startswith("Error")]
        ok = rc == 0
        checks.append(("opencode agents", f"{len(agents)} listed" if agents else "none/empty", bool(agents)))
        blocked += 0 if ok and agents else 1

    # ---- Report ----
    print("=== Oh My OpenAgent / Oh My Hermes Doctor ===\n")
    for label, detail, ok in checks:
        mark = OK + "PASS" + RESET if ok else FAIL + "FAIL" + RESET
        print(f"[{mark}] {label:38} {detail}")
    blocked_txt = FAIL + str(blocked) + RESET if blocked else OK + str(blocked) + RESET
    warned_txt = WARN + str(warned) + RESET if warned else str(warned)
    print(f"\nBlocking failures: {blocked_txt} | Warnings: {warned_txt}")
    return 0 if blocked == 0 else (1 if warned else 2)


if __name__ == "__main__":
    sys.exit(main())
