#!/usr/bin/env python3
"""hermes_diagnostic.py — orchestrate the full Hermes diagnostic battery.

Runs: hermes doctor + doctor --fix + security audit + status + insights +
      logs (list/errors/desktop/gateway/gui/agent) + bun run check.

Emits: .hermes/plans/diagnostic-YYYYMMDD-HHMMSS/{report.md,report.json,
       failures.md,sweep.log}.

Usage:
  python scripts/hermes_diagnostic.py [--no-bun] [--no-fix] [--output DIR]

Exit codes:
  0  no failures detected
  1  one or more diagnostic commands failed
  2  internal script error
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Commands in strict-sequential order. Each entry: (label, argv, timeout_sec).
COMMANDS: list[tuple[str, list[str], int]] = [
    ("doctor",         ["hermes", "doctor"], 120),
    ("doctor-fix",     ["hermes", "doctor", "--fix"], 180),
    ("security",       ["hermes", "security", "audit"], 60),
    ("status",         ["hermes", "status"], 30),
    ("insights",       ["hermes", "insights"], 60),
    ("logs-list",      ["hermes", "logs", "list"], 30),
    ("logs-errors",    ["hermes", "logs", "errors"], 30),
    ("logs-desktop",   ["hermes", "logs", "desktop"], 30),
    ("logs-gateway",   ["hermes", "logs", "gateway"], 30),
    ("logs-gui",       ["hermes", "logs", "gui"], 30),
    ("logs-agent",     ["hermes", "logs", "agent"], 30),
    ("bun-check",      ["bun", "run", "check"], 300),
]


def run_one(label: str, argv: list[str], timeout: int, cwd: str) -> dict:
    start = time.monotonic()
    record: dict = {
        "label": label,
        "argv": argv,
        "start": datetime.now(timezone.utc).isoformat(),
    }
    try:
        proc = subprocess.run(
            argv,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd,
            shell=False,
        )
        elapsed = int((time.monotonic() - start) * 1000)
        record.update({
            "exit": proc.returncode,
            "elapsed_ms": elapsed,
            "stdout_tail": proc.stdout[-4000:] if proc.stdout else "",
            "stderr_tail": proc.stderr[-2000:] if proc.stderr else "",
            "ok": proc.returncode == 0,
        })
    except subprocess.TimeoutExpired:
        elapsed = int((time.monotonic() - start) * 1000)
        record.update({
            "exit": 124,
            "elapsed_ms": elapsed,
            "stdout_tail": "",
            "stderr_tail": f"TIMEOUT after {timeout}s",
            "ok": False,
        })
    except FileNotFoundError as e:
        record.update({
            "exit": 127,
            "elapsed_ms": 0,
            "stdout_tail": "",
            "stderr_tail": f"command not found: {e}",
            "ok": False,
        })
    except Exception as e:  # noqa: BLE001
        record.update({
            "exit": 2,
            "elapsed_ms": 0,
            "stdout_tail": "",
            "stderr_tail": f"script error: {type(e).__name__}: {e}",
            "ok": False,
        })
    return record


def classify_findings(results: list[dict]) -> list[str]:
    """Heuristic scan of each result for warning/error patterns."""
    findings: list[str] = []
    for r in results:
        if r["ok"]:
            continue
        findings.append(f"{r['label']}: exit={r['exit']}")
        # Look for known-warning substrings
        combined = (r["stdout_tail"] + r["stderr_tail"]).lower()
        for marker in ("insufficient credits", "not authenticated", "disabled",
                       "warn", "warning", "timeout", "refused"):
            if marker in combined:
                findings.append(f"  ↳ {marker!r} in {r['label']}")
    return findings


def render_markdown(results: list[dict], findings: list[str], elapsed_total: int) -> str:
    lines: list[str] = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines.append(f"# Hermes Diagnostic Report — {ts}\n")
    lines.append(f"Total elapsed: {elapsed_total/1000:.1f}s | "
                 f"Commands: {len(results)} | "
                 f"Failures: {sum(1 for r in results if not r['ok'])}\n")
    lines.append("## Per-command results\n")
    lines.append("| # | Label | Exit | OK | Elapsed |")
    lines.append("|---|---|---|---|---|")
    for i, r in enumerate(results, 1):
        ok = "✓" if r["ok"] else "✗"
        lines.append(f"| {i} | `{r['label']}` | {r['exit']} | {ok} | "
                     f"{r['elapsed_ms']/1000:.1f}s |")
    lines.append("")
    if findings:
        lines.append("## Findings\n")
        for f in findings:
            lines.append(f"- {f}")
        lines.append("")
    else:
        lines.append("## Findings\n\n_None — all commands passed._\n")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-bun", action="store_true",
                    help="skip `bun run check` step")
    ap.add_argument("--no-fix", action="store_true",
                    help="skip `hermes doctor --fix` (read-only mode)")
    ap.add_argument("--output", type=Path, default=None,
                    help="output directory (default: .hermes/plans/diagnostic-<ts>)")
    ap.add_argument("--cwd", default="C:/Users/Alexa/Desktop/SandBox",
                    help="working directory for bun check (default: SandBox root)")
    args = ap.parse_args()

    cmds = [c for c in COMMANDS
            if not (args.no_bun and c[0] == "bun-check")
            and not (args.no_fix and c[0] == "doctor-fix")]

    ts_dir = args.output or Path(
        f"C:/Users/Alexa/Desktop/SandBox/.hermes/plans/diagnostic-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    )
    ts_dir.mkdir(parents=True, exist_ok=True)

    print(f"== Hermes Diagnostic: {len(cmds)} commands, output={ts_dir} ==", flush=True)
    overall_start = time.monotonic()
    results: list[dict] = []
    for label, argv, timeout in cmds:
        print(f"  → {label} ...", end="", flush=True)
        r = run_one(label, argv, timeout, args.cwd)
        results.append(r)
        mark = "✓" if r["ok"] else f"✗ exit={r['exit']}"
        print(f" {mark} ({r['elapsed_ms']/1000:.1f}s)")

    elapsed_total = int((time.monotonic() - overall_start) * 1000)
    findings = classify_findings(results)

    report_json = ts_dir / "report.json"
    report_md = ts_dir / "report.md"
    failures_md = ts_dir / "failures.md"
    sweep_log = ts_dir / "sweep.log"

    report_json.write_text(
        json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(),
            "elapsed_ms": elapsed_total,
            "cwd": args.cwd,
            "commands": results,
            "findings": findings,
            "summary": {
                "total": len(results),
                "ok": sum(1 for r in results if r["ok"]),
                "failed": sum(1 for r in results if not r["ok"]),
            },
        }, indent=2),
        encoding="utf-8",
    )

    report_md.write_text(render_markdown(results, findings, elapsed_total), encoding="utf-8")

    if findings:
        failures_md.write_text(
            "# Failures\n\n" + "\n".join(f"- {f}" for f in findings),
            encoding="utf-8",
        )
    else:
        failures_md.write_text("# Failures\n\n_None_\n", encoding="utf-8")

    sweep_log.write_text(
        "\n".join(f"[{r['label']}] exit={r['exit']} elapsed={r['elapsed_ms']}ms ok={r['ok']}"
                  for r in results),
        encoding="utf-8",
    )

    n_fail = sum(1 for r in results if not r["ok"])
    print(f"\n== Done: {len(results) - n_fail}/{len(results)} OK, {n_fail} failed, "
          f"{elapsed_total/1000:.1f}s total ==")
    print(f"   Report: {report_md}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
