#!/usr/bin/env python3
"""Provider non-interactive executor.

Enumerate every provider+model configured in ~/AppData/Local/hermes/config.yaml,
run a test prompt against each via `hermes chat -m <model> -q <prompt> --oneshot`,
capture response + latency + error, and emit JSON + markdown report.

Usage:
  python scripts/provider_executor.py [--prompt "Reply with OK"] [--out DIR] [--timeout 30] [--providers deepseek,openrouter]

The script never raises on provider errors — failures are recorded in the report.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
CONFIG_PATH = HERMES_HOME / "config.yaml"


def parse_providers(text: str) -> list[dict]:
    """Extract providers + their default_model from config.yaml. No PyYAML dep."""
    providers: list[dict] = []
    in_providers = False
    current: dict | None = None
    current_indent = 0
    for raw in text.splitlines():
        if raw.startswith("providers:"):
            in_providers = True
            continue
        if not in_providers:
            continue
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        stripped = raw.strip()
        # End of providers block (new top-level key)
        if indent == 0 and ":" in stripped and not stripped.startswith("-"):
            in_providers = False
            if current:
                providers.append(current)
                current = None
            continue
        if indent == 2 and stripped.endswith(":"):
            # New provider
            if current:
                providers.append(current)
            name = stripped.rstrip(":")
            current = {"name": name, "default_model": None}
            current_indent = indent
            continue
        if current and indent > current_indent and ":" in stripped:
            key, _, val = stripped.partition(":")
            if key.strip() == "default_model":
                current["default_model"] = val.strip().strip("'\"")
    if current:
        providers.append(current)
    return providers


def run_oneshot(model: str, prompt: str, timeout: int) -> dict:
    """Run `hermes chat -m MODEL -q PROMPT --oneshot -Q` and capture output."""
    cmd = [
        "hermes", "chat",
        "-m", model,
        "-q", prompt,
        "--oneshot",
        "-Q",  # quiet
    ]
    start = time.monotonic()
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=HERMES_HOME,
        )
        elapsed = time.monotonic() - start
        return {
            "exit_code": result.returncode,
            "stdout": (result.stdout or "")[:2000],
            "stderr": (result.stderr or "")[:1000],
            "elapsed_s": round(elapsed, 2),
            "ok": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "exit_code": -1,
            "stdout": "",
            "stderr": f"TIMEOUT after {timeout}s",
            "elapsed_s": round(time.monotonic() - start, 2),
            "ok": False,
        }
    except FileNotFoundError:
        return {
            "exit_code": -1,
            "stdout": "",
            "stderr": "hermes CLI not found on PATH",
            "elapsed_s": 0.0,
            "ok": False,
        }
    except Exception as e:
        return {
            "exit_code": -1,
            "stdout": "",
            "stderr": f"EXCEPTION: {type(e).__name__}: {e}",
            "elapsed_s": round(time.monotonic() - start, 2),
            "ok": False,
        }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", default="Reply with the single word: OK. Nothing else.")
    p.add_argument("--out", default=None)
    p.add_argument("--timeout", type=int, default=45)
    p.add_argument("--providers", default=None, help="comma-separated whitelist")
    args = p.parse_args()

    if not CONFIG_PATH.exists():
        print(f"Config not found: {CONFIG_PATH}", file=sys.stderr)
        return 2

    out_dir = Path(args.out) if args.out else (
        Path(".hermes/plans") / f"provider-executor-{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H%M%S')}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    text = CONFIG_PATH.read_text(encoding="utf-8", errors="ignore")
    providers = parse_providers(text)
    if args.providers:
        wanted = set(args.providers.split(","))
        providers = [pr for pr in providers if pr["name"] in wanted]

    # Filter to providers with a default_model
    testable = [pr for pr in providers if pr.get("default_model")]
    skipped = [pr["name"] for pr in providers if not pr.get("default_model")]

    print(f"Testing {len(testable)} providers (skipped {len(skipped)} without default_model)")
    print(f"Prompt: {args.prompt!r}")
    print(f"Timeout: {args.timeout}s per provider")
    print()

    results: list[dict] = []
    for pr in testable:
        name = pr["name"]
        model = pr["default_model"]
        print(f"[{name}] model={model} ...", end=" ", flush=True)
        out = run_oneshot(model, args.prompt, args.timeout)
        out["provider"] = name
        out["model"] = model
        out["prompt"] = args.prompt
        out["ts"] = datetime.now(timezone.utc).isoformat()
        results.append(out)
        status = "OK" if out["ok"] else "FAIL"
        print(f"{status} ({out['elapsed_s']}s)")
        if not out["ok"] and out["stderr"]:
            print(f"  stderr: {out['stderr'][:200]}")

    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "prompt": args.prompt,
        "timeout_s": args.timeout,
        "tested": len(testable),
        "skipped": skipped,
        "ok_count": sum(1 for r in results if r["ok"]),
        "fail_count": sum(1 for r in results if not r["ok"]),
        "results": results,
    }

    (out_dir / "report.json").write_text(json.dumps(report, indent=2))

    md = [f"# Provider Executor Report\n",
          f"Generated: {report['ts']}",
          f"Prompt: `{report['prompt']}`",
          f"Timeout: {report['timeout_s']}s\n",
          f"## Summary",
          f"- Tested: {report['tested']}",
          f"- OK: {report['ok_count']}",
          f"- FAIL: {report['fail_count']}",
          f"- Skipped (no default_model): {report['skipped']}\n",
          "## Per-provider results",
          "",
          "| Provider | Model | OK | Elapsed (s) | Exit | Stderr (first 200) |",
          "|---|---|---|---|---|---|"]
    for r in results:
        md.append(f"| {r['provider']} | `{r['model']}` | {'✓' if r['ok'] else '✗'} | {r['elapsed_s']} | {r['exit_code']} | {(r['stderr'] or '')[:200].replace(chr(10), ' ')} |")

    md.append("\n## Successful responses (truncated)")
    for r in results:
        if r["ok"]:
            md.append(f"### {r['provider']} ({r['model']})")
            md.append(f"```\n{r['stdout'][:500]}\n```")
            md.append("")

    (out_dir / "report.md").write_text("\n".join(md))

    print()
    print(f"OK: {report['ok_count']} / FAIL: {report['fail_count']}")
    print(f"Report: {out_dir}/report.md")
    return 0 if report["fail_count"] == 0 else 0  # informational


if __name__ == "__main__":
    sys.exit(main())
