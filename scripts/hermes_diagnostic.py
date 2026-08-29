#!/usr/bin/env python3
"""Hermes Agent diagnostic harness.

Orchestrates the full hermes diagnostic sweep:
  hermes doctor
  hermes doctor --fix
  hermes security audit
  hermes status
  hermes insights
  hermes logs list
  hermes logs errors
  hermes logs desktop
  hermes logs gateway
  hermes logs gui
  hermes logs agent
  bun run check  (if package.json exists)

Each command runs with a timeout; failures are recorded in the report (not raised).
Outputs JSON + markdown to .hermes/plans/hermes-diagnostic-<date>/.

Usage:
  python scripts/hermes_diagnostic.py [--out DIR] [--timeout 60] [--skip-fix]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SANDBOX = Path("C:/Users/Alexa/Desktop/SandBox")


def run(cmd: list[str], timeout: int, cwd: Path | None = None) -> dict:
    """Run a command, capture output, return {exit, elapsed_s, stdout_tail, stderr_tail, ok}."""
    start = time.monotonic()
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd) if cwd else None,
        )
        elapsed = time.monotonic() - start
        return {
            "cmd": cmd,
            "exit": result.returncode,
            "elapsed_s": round(elapsed, 2),
            "stdout_tail": (result.stdout or "")[-1500:],
            "stderr_tail": (result.stderr or "")[-500:],
            "ok": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "cmd": cmd, "exit": -1, "elapsed_s": round(time.monotonic() - start, 2),
            "stdout_tail": "", "stderr_tail": f"TIMEOUT after {timeout}s", "ok": False,
        }
    except FileNotFoundError as e:
        return {
            "cmd": cmd, "exit": -1, "elapsed_s": 0.0,
            "stdout_tail": "", "stderr_tail": f"NOT FOUND: {e}", "ok": False,
        }
    except Exception as e:
        return {
            "cmd": cmd, "exit": -1, "elapsed_s": round(time.monotonic() - start, 2),
            "stdout_tail": "", "stderr_tail": f"EXCEPTION: {type(e).__name__}: {e}", "ok": False,
        }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=None)
    p.add_argument("--timeout", type=int, default=120)
    p.add_argument("--skip-fix", action="store_true", help="Skip `hermes doctor --fix`")
    args = p.parse_args()

    out_dir = Path(args.out) if args.out else (
        Path(".hermes/plans") / f"hermes-diagnostic-{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H%M%S')}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    cmds: list[dict] = [
        {"label": "doctor",       "argv": ["hermes", "doctor"]},
        {"label": "doctor-fix",   "argv": ["hermes", "doctor", "--fix"], "skip": args.skip_fix},
        {"label": "security",     "argv": ["hermes", "security", "audit"]},
        {"label": "status",       "argv": ["hermes", "status"]},
        {"label": "insights",     "argv": ["hermes", "insights"]},
        {"label": "logs-list",    "argv": ["hermes", "logs", "list"]},
        {"label": "logs-errors",  "argv": ["hermes", "logs", "errors"]},
        {"label": "logs-desktop", "argv": ["hermes", "logs", "desktop"]},
        {"label": "logs-gateway", "argv": ["hermes", "logs", "gateway"]},
        {"label": "logs-gui",     "argv": ["hermes", "logs", "gui"]},
        {"label": "logs-agent",   "argv": ["hermes", "logs", "agent"]},
    ]
    # Add bun run check if package.json exists
    if (SANDBOX / "package.json").exists():
        cmds.append({"label": "bun-run-check", "argv": ["bun", "run", "check"], "cwd": str(SANDBOX)})

    results: list[dict] = []
    print(f"Running {len(cmds)} diagnostic commands (timeout {args.timeout}s each)...")
    for spec in cmds:
        if spec.get("skip"):
            print(f"[skip] {spec['label']}")
            continue
        label = spec["label"]
        argv = spec["argv"]
        cwd = spec.get("cwd")
        print(f"[{label:14}] {' '.join(argv[:3])} ...", end=" ", flush=True)
        r = run(argv, args.timeout, Path(cwd) if cwd else None)
        r["label"] = label
        r["ts"] = datetime.now(timezone.utc).isoformat()
        results.append(r)
        print(f"exit={r['exit']} ({r['elapsed_s']}s) {'OK' if r['ok'] else 'FAIL'}")
        if not r["ok"] and r["stderr_tail"]:
            print(f"  stderr: {r['stderr_tail'][:200]}")

    ok = sum(1 for r in results if r["ok"])
    fail = sum(1 for r in results if not r["ok"])
    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "timeout_s": args.timeout,
        "total": len(results),
        "ok_count": ok,
        "fail_count": fail,
        "results": results,
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2))

    md = [f"# Hermes Diagnostic Report\n",
          f"Generated: {report['ts']}",
          f"Total: {report['total']} | OK: {ok} | FAIL: {fail}\n",
          "## Per-command",
          "",
          "| # | Label | Exit | Elapsed (s) | OK |",
          "|---|---|---|---|---|"]
    for i, r in enumerate(results, 1):
        md.append(f"| {i} | {r['label']} | {r['exit']} | {r['elapsed_s']} | {'✓' if r['ok'] else '✗'} |")

    md.append("\n## Failures (stderr tail)")
    for r in results:
        if not r["ok"]:
            md.append(f"### {r['label']}")
            md.append(f"```\n{r['stderr_tail']}\n```")

    (out_dir / "report.md").write_text("\n".join(md))
    print()
    print(f"OK: {ok} / FAIL: {fail}")
    print(f"Report: {out_dir}/report.md")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
