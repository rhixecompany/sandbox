#!/usr/bin/env python3
"""Hooks Judge — score ~/AppData/Local/hermes/hooks/* on 5 dimensions (max 100).

Usage:
    python judge.py --hooks-dir ~/AppData/Local/hermes/hooks [--output PATH]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

EVENT_PATTERNS = [
    "on_session_start", "on_session_end",
    "pre_tool_call", "post_tool_call",
    "pre_llm_call", "subagent_stop",
    "on_user_interrupt", "on_idle",
    "pre_flight", "pre_exec", "on_error",
    "post_process", "post_exec",
]


def _find_bash() -> list[str] | None:
    """Find bash on Windows (Git Bash/MSYS) or Unix."""
    if sys.platform == "win32":
        # Git Bash paths on Windows
        for path in [
            r"C:\Program Files\Git\usr\bin\bash.exe",
            r"C:\Program Files (x86)\Git\usr\bin\bash.exe",
        ]:
            if Path(path).exists():
                return [path, "-n"]
        # Try where/which
        for cmd in ["bash.exe", "bash"]:
            r = subprocess.run(["where", cmd], capture_output=True, text=True, timeout=5)
            if r.returncode == 0:
                return [r.stdout.strip().splitlines()[0], "-n"]
        return None
    return ["bash", "-n"]


def syntax_check(p: Path) -> tuple[bool, str]:
    suffix = p.suffix.lower()
    try:
        if suffix == ".py":
            r = subprocess.run(
                [sys.executable, "-m", "py_compile", str(p)],
                capture_output=True, text=True, timeout=15,
            )
            return r.returncode == 0, r.stderr[:200]
        if suffix in {".sh", ".bash"}:
            bash_cmd = _find_bash()
            if bash_cmd is None:
                return True, "bash not found on Windows — skipping syntax check"
            r = subprocess.run(
                bash_cmd + [str(p)],
                capture_output=True, text=True, timeout=15,
            )
            return r.returncode == 0, r.stderr[:200]
        return True, ""
    except Exception as e:
        return False, str(e)[:200]


def shellcheck(p: Path) -> tuple[bool, str]:
    """Best-effort shellcheck; OK if shellcheck missing."""
    try:
        r = subprocess.run(
            ["shellcheck", "--severity=warning", str(p)],
            capture_output=True, text=True, timeout=20,
        )
        return r.returncode == 0, (r.stdout + r.stderr)[:300]
    except FileNotFoundError:
        return True, "shellcheck not installed"
    except Exception as e:
        return True, str(e)[:200]


def score_one(p: Path) -> dict:
    text = p.read_text(encoding="utf-8", errors="ignore")

    # Event Coverage (20): declared or referenced
    declared = sum(1 for e in EVENT_PATTERNS if e in text)
    cov_pts = min(declared * 4, 20)

    # Syntax (20)
    ok, err = syntax_check(p)
    syn_pts = 20 if ok else 4

    # Idempotency (20): guard patterns
    idem_patterns = ["mkdir -p", "[[ -f", "[ -f", "touch ", "if [ !", "set -e"]
    idem_pts = sum(3 for pat in idem_patterns if pat in text)
    idem_pts = min(idem_pts, 20)

    # Error Handling (20)
    eh_pts = 0
    if "set -e" in text or "set -euo pipefail" in text:
        eh_pts += 10
    if "trap " in text:
        eh_pts += 5
    if "exit " in text or "sys.exit" in text:
        eh_pts += 5
    eh_pts = min(eh_pts, 20)

    # Logging (20): write to log file
    log_pts = 0
    if "logs/" in text or ".log" in text:
        log_pts += 12
    if "echo " in text or "print(" in text:
        log_pts += 4
    if "2>&1" in text or ">>" in text:
        log_pts += 4
    log_pts = min(log_pts, 20)

    total = cov_pts + syn_pts + idem_pts + eh_pts + log_pts
    return {
        "file": str(p),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "event_coverage": cov_pts,
            "syntax": syn_pts,
            "idempotency": idem_pts,
            "error_handling": eh_pts,
            "logging": log_pts,
        },
        "events_referenced": declared,
        "syntax_ok": ok,
        "syntax_error": err if not ok else "",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Hooks Judge")
    ap.add_argument("--hooks-dir", default=None,
                    help="hooks dir (default: $LOCALAPPDATA/hermes/hooks)")
    ap.add_argument("--output", default="judge_results/hooks_audit")
    ap.add_argument("--threshold", type=int, default=70)
    args = ap.parse_args()

    if args.hooks_dir is None:
        import os
        local = os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local"))
        args.hooks_dir = str(Path(local) / "hermes/hooks")

    hdir = Path(args.hooks_dir)
    if not hdir.is_dir():
        print(f"ERR: hooks dir not found: {hdir}", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for p in sorted(hdir.iterdir()):
        if p.is_file() and p.suffix.lower() in {".py", ".sh", ".bash"}:
            results.append(score_one(p))

    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)

    (out.with_suffix(".json")).write_text(json.dumps({
        "ts": datetime.utcnow().isoformat() + "Z",
        "dir": str(hdir),
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "results": results,
    }, indent=2))

    md = [
        f"# Hooks Audit — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{hdir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        "",
        "| File | Score | Rating | Events | Syntax | Idem | ErrH | Log |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        d = r["dims"]
        md.append(
            f"| `{Path(r['file']).name}` | {r['score']} | {r['rating']} | "
            f"{r['events_referenced']} | {d['syntax']} | {d['idempotency']} | "
            f"{d['error_handling']} | {d['logging']} |"
        )
    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")
    print(f"Hooks Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}")
    print(f"Report: {out.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())