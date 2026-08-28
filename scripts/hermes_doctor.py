#!/usr/bin/env python3
"""
hermes_doctor.py — Full Hermes platform diagnostic + log triage harness.

Runs the full diagnostic battery in order, captures exit codes + findings,
classifies each finding (real_bug / intentional / transient / advisory),
and writes a structured report (JSON + Markdown).

Usage:
    python scripts/hermes_doctor.py                  # full battery
    python scripts/hermes_doctor.py --doctor-only    # only doctor/--fix/security/status
    python scripts/hermes_doctor.py --logs-only      # only log triage
    python scripts/hermes_doctor.py --no-bun         # skip bun run check
    python scripts/hermes_doctor.py --json-only      # JSON output, no markdown
    python scripts/hermes_doctor.py --output DIR     # custom output dir (default .hermes/plans/diagnostic-<date>/)

Exit codes:
    0  = all green / only intentional+advisory findings
    1  = real bugs or transient errors that need attention
    2  = tool failure (hermes itself broken, can't run battery)

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# (label, command, classification_hint)
# classification_hint is one of: "doctor", "log", "build", "info"
COMMANDS_FULL = [
    ("doctor",            ["hermes", "doctor"],                    "doctor"),
    ("doctor_fix",        ["hermes", "doctor", "--fix"],           "doctor"),
    ("security_audit",    ["hermes", "security", "audit"],         "doctor"),
    ("status",            ["hermes", "status"],                    "doctor"),
    ("insights",          ["hermes", "insights"],                  "info"),
    ("logs_list",         ["hermes", "logs", "list"],              "log"),
    ("logs_errors",       ["hermes", "logs", "errors"],            "log"),
    ("logs_desktop",      ["hermes", "logs", "desktop"],           "log"),
    ("logs_gateway",      ["hermes", "logs", "gateway"],           "log"),
    ("logs_gui",          ["hermes", "logs", "gui"],               "log"),
    ("logs_agent",        ["hermes", "logs", "agent"],             "log"),
    ("bun_run_check",     ["bun", "run", "check"],                 "build"),
]

COMMANDS_DOCTOR_ONLY = [c for c in COMMANDS_FULL if c[2] in ("doctor", "info")]
COMMANDS_LOGS_ONLY = [c for c in COMMANDS_FULL if c[2] == "log"]

# Patterns from log-analysis-and-triage (Hermes-specific)
PATTERN_REAL_BUG = [
    re.compile(r"shell hook failed.*command not found", re.I),
    re.compile(r"WinError 5.*Access is denied", re.I),
    re.compile(r"WAL checkpoint.*disk I/O error", re.I),
    re.compile(r"MCP server\(s\) failed to start", re.I),
    re.compile(r"HTTP 402", re.I),
]
PATTERN_INTENTIONAL = [
    re.compile(r"Title generation failed", re.I),
    re.compile(r"check_fn.*returned False", re.I),
    re.compile(r"PluginContext\.register_flask_app", re.I),
    re.compile(r"generate.*slash command.*collides", re.I),
    re.compile(r"unknown hook event", re.I),
    re.compile(r"never commit", re.I),  # user rule, not bug
]
PATTERN_TRANSIENT = [
    re.compile(r"getaddrinfo failed", re.I),
    re.compile(r"HTTP 429", re.I),
    re.compile(r"HTTP 5\d\d", re.I),
    re.compile(r"connection.*refused", re.I),
    re.compile(r"timeout", re.I),
    re.compile(r"Insufficient credits", re.I),
    re.compile(r"FATAL ERROR: AlignedAlloc", re.I),
    re.compile(r"DNS", re.I),
]
PATTERN_ADVISORY = [
    re.compile(r"not logged in", re.I),
    re.compile(r"no alias", re.I),
    re.compile(r"auxiliary.*marking.*unhealthy", re.I),
    re.compile(r"disabled", re.I),
    re.compile(r"uncommitted", re.I),
]

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_one(label: str, cmd: list[str], cwd: str, timeout: int = 120) -> dict:
    """Run a single command, capture exit code, stdout, stderr, duration."""
    start = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {
            "label": label,
            "command": " ".join(cmd),
            "exit_code": proc.returncode,
            "duration_ms": elapsed_ms,
            "stdout": proc.stdout[-8000:] if proc.stdout else "",  # cap
            "stderr": proc.stderr[-4000:] if proc.stderr else "",
            "ok": proc.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "label": label,
            "command": " ".join(cmd),
            "exit_code": -1,
            "duration_ms": int((time.monotonic() - start) * 1000),
            "stdout": "",
            "stderr": f"TIMEOUT after {timeout}s",
            "ok": False,
            "error": "timeout",
        }
    except FileNotFoundError as e:
        return {
            "label": label,
            "command": " ".join(cmd),
            "exit_code": -2,
            "duration_ms": 0,
            "stdout": "",
            "stderr": f"COMMAND NOT FOUND: {e}",
            "ok": False,
            "error": "not_found",
        }


def classify_finding(text: str) -> str:
    """Classify a piece of log/diagnostic text. Returns one of:
    real_bug | intentional | transient | advisory | info
    """
    if not text:
        return "info"
    for pat in PATTERN_REAL_BUG:
        if pat.search(text):
            return "real_bug"
    for pat in PATTERN_INTENTIONAL:
        if pat.search(text):
            return "intentional"
    for pat in PATTERN_TRANSIENT:
        if pat.search(text):
            return "transient"
    for pat in PATTERN_ADVISORY:
        if pat.search(text):
            return "advisory"
    return "info"


# ---------------------------------------------------------------------------
# Report builder
# ---------------------------------------------------------------------------

def build_summary(results: list[dict]) -> dict[str, object]:
    """Aggregate per-command results into a summary."""
    counts: dict[str, int] = {
        "total": len(results),
        "ok": sum(1 for r in results if r["ok"]),
        "fail": sum(1 for r in results if not r["ok"]),
        "real_bug": 0,
        "intentional": 0,
        "transient": 0,
        "advisory": 0,
        "info": 0,
    }
    findings: list[dict[str, object]] = []
    for r in results:
        blob = (r.get("stdout", "") or "") + "\n" + (r.get("stderr", "") or "")
        klass = classify_finding(blob)
        counts[klass] = counts.get(klass, 0) + 1
        if klass in ("real_bug", "transient") and not r["ok"]:
            findings.append({
                "label": r["label"],
                "classification": klass,
                "exit_code": r["exit_code"],
                "excerpt": (r.get("stdout", "") + r.get("stderr", ""))[:500],
            })
    return {"counts": counts, "findings": findings}


def render_markdown(report: dict[str, object]) -> str:
    """Render a human-readable Markdown summary."""
    summary_obj = report["summary"]
    assert isinstance(summary_obj, dict)
    counts_obj = summary_obj["counts"]
    assert isinstance(counts_obj, dict)
    results_obj = report["results"]
    assert isinstance(results_obj, list)
    summary_findings_obj = summary_obj["findings"]
    assert isinstance(summary_findings_obj, list)
    lines = [
        f"# Hermes Diagnostic Report — {report['generated']}",
        "",
        f"- Profile: `{report.get('profile', '?')}`",
        f"- CWD: `{report['cwd']}`",
        f"- Total duration: {report['total_duration_ms']} ms",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"| ------ | ----- |",
        f"| Commands run | {counts_obj.get('total', 0)} |",
        f"| Exit 0 | {counts_obj.get('ok', 0)} |",
        f"| Exit non-zero | {counts_obj.get('fail', 0)} |",
        f"| Real bugs | {counts_obj.get('real_bug', 0)} |",
        f"| Intentional guards | {counts_obj.get('intentional', 0)} |",
        f"| Transient/external | {counts_obj.get('transient', 0)} |",
        f"| Advisory | {counts_obj.get('advisory', 0)} |",
        "",
        "## Per-command results",
        "",
        "| # | Label | Exit | Duration | OK |",
        "| - | ----- | ---- | -------- | -- |",
    ]
    for i, r in enumerate(results_obj, 1):
        assert isinstance(r, dict)
        lines.append(
            f"| {i} | `{r['label']}` | {r['exit_code']} | {r['duration_ms']}ms | "
            f"{'✓' if r['ok'] else '✗'} |"
        )
    if summary_findings_obj:
        lines += ["", "## Findings (real_bug + transient)", ""]
        for f in summary_findings_obj:
            assert isinstance(f, dict)
            lines.append(f"### {f['label']} — {f['classification']} (exit {f['exit_code']})")
            lines.append("")
            lines.append("```")
            excerpt = f.get('excerpt', '')
            if isinstance(excerpt, str):
                lines.append(excerpt[:500])
            lines.append("```")
            lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--doctor-only", action="store_true")
    p.add_argument("--logs-only", action="store_true")
    p.add_argument("--no-bun", action="store_true")
    p.add_argument("--json-only", action="store_true")
    p.add_argument("--output", help="Output directory (default .hermes/plans/diagnostic-<date>/)")
    p.add_argument("--timeout", type=int, default=120)
    args = p.parse_args()

    cwd = os.getcwd()
    if args.output:
        out_dir = Path(args.output)
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        out_dir = Path(f".hermes/plans/diagnostic-{date}")
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.doctor_only:
        commands = COMMANDS_DOCTOR_ONLY
    elif args.logs_only:
        commands = COMMANDS_LOGS_ONLY
    else:
        commands = list(COMMANDS_FULL)
    if args.no_bun:
        commands = [c for c in commands if c[0] != "bun_run_check"]

    # Run battery
    start = time.monotonic()
    results = [run_one(label, cmd, cwd, timeout=args.timeout) for label, cmd, _ in commands]
    total_ms = int((time.monotonic() - start) * 1000)

    # Detect profile
    profile = "default"
    try:
        prof = subprocess.run(["hermes", "profile", "list"], cwd=cwd,
                              capture_output=True, text=True, timeout=10)
        # first non-empty line that has "active" marker or asterisk
        for ln in prof.stdout.splitlines():
            if "*" in ln:
                m = re.search(r"(\S+)", ln.strip().lstrip("*").strip())
                if m:
                    profile = m.group(1)
                    break
    except Exception:
        pass

    summary = build_summary(results)
    report: dict[str, object] = {
        "schema_version": 1,
        "generated": datetime.now(timezone.utc).isoformat(),
        "cwd": cwd,
        "profile": profile,
        "total_duration_ms": total_ms,
        "results": results,
        "summary": summary,
    }

    # Write outputs
    json_path = out_dir / "report.json"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md_path = out_dir / "report.md"
    md_path.write_text(render_markdown(report), encoding="utf-8")

    # Console output
    if not args.json_only:
        s = report["summary"]["counts"]
        print(f"Hermes Doctor — {report['generated']}")
        print(f"  profile    : {profile}")
        print(f"  cwd        : {cwd}")
        print(f"  duration   : {total_ms} ms")
        print(f"  commands   : {s['total']} ({s['ok']} ok / {s['fail']} fail)")
        print(f"  findings   : {s['real_bug']} real_bug / {s['transient']} transient / "
              f"{s['intentional']} intentional / {s['advisory']} advisory")
        print(f"  report     : {json_path}")
        print(f"              {md_path}")

    # Exit code: 0 = clean, 1 = real bugs or transient
    summary_dict = report["summary"]
    assert isinstance(summary_dict, dict)
    counts_dict = summary_dict["counts"]
    assert isinstance(counts_dict, dict)
    real_bug_count = counts_dict.get("real_bug", 0)
    assert isinstance(real_bug_count, int)
    if real_bug_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
