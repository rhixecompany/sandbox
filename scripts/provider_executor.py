#!/usr/bin/env python3
"""Provider non-interactive executor — enhanced.

Enumerate every authorized provider+model from `hermes auth list` + config.yaml,
run a user request against each via `hermes chat -m <model> -q <prompt> --oneshot`,
capture response + latency + context + capabilities, and emit JSON + markdown report.

Usage:
  python scripts/provider_executor.py --request "Write a haiku" [--out DIR] [--timeout 30] [--providers deepseek,openrouter]
  python scripts/provider_executor.py --prompt "Reply with OK"  # legacy smoke-test mode

The script never raises on provider errors — failures are recorded in the report.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
CONFIG_PATH = HERMES_HOME / "config.yaml"

# Capability metadata per provider (verified 2026-08-31)
CAPABILITIES: dict[str, dict] = {
    "nous": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
    "opencode-zen": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
    "openrouter": {"context": 131072, "max_output": 8192, "vision": True, "reasoning": True, "tools": True},
    "deepseek": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
    "gemini": {"context": 1048576, "max_output": 8192, "vision": True, "reasoning": True, "tools": True},
    "ollama-cloud": {"context": 131072, "max_output": 8192, "vision": True, "reasoning": True, "tools": False},
    "xai": {"context": 131072, "max_output": 8192, "vision": True, "reasoning": True, "tools": True},
    "openai-api": {"context": 131072, "max_output": 8192, "vision": True, "reasoning": True, "tools": True},
    "huggingface": {"context": 131072, "max_output": 8192, "vision": True, "reasoning": True, "tools": False},
    "openai-codex": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
    "copilot": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
    "minimax-oauth": {"context": 131072, "max_output": 8192, "vision": False, "reasoning": True, "tools": True},
}


def parse_providers(text: str) -> list[dict]:
    """Extract providers + their default_model from config.yaml."""
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
        if indent == 0 and ":" in stripped and not stripped.startswith("-"):
            in_providers = False
            if current:
                providers.append(current)
                current = None
            continue
        if indent == 2 and stripped.endswith(":"):
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
        "--ignore-rules",
        "--ignore-user-config",
        "-Q",
    ]
    start = time.monotonic()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, cwd=HERMES_HOME,
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
        return {"exit_code": -1, "stdout": "", "stderr": f"TIMEOUT after {timeout}s",
                "elapsed_s": round(time.monotonic() - start, 2), "ok": False}
    except FileNotFoundError:
        return {"exit_code": -1, "stdout": "", "stderr": "hermes CLI not found",
                "elapsed_s": 0.0, "ok": False}
    except Exception as e:
        return {"exit_code": -1, "stdout": "", "stderr": f"EXCEPTION: {type(e).__name__}: {e}",
                "elapsed_s": 0.0, "ok": False}


def main() -> int:
    p = argparse.ArgumentParser(description="Provider non-interactive executor")
    p.add_argument("--request", default=None, help="User request to send to each provider")
    p.add_argument("--prompt", default="Reply with the single word: OK. Nothing else.", help="Legacy smoke-test prompt")
    p.add_argument("--out", default=None)
    p.add_argument("--timeout", type=int, default=120)
    p.add_argument("--providers", default=None, help="comma-separated whitelist")
    args = p.parse_args()

    user_request = args.request if args.request else args.prompt
    mode = "request" if args.request else "smoke"

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

    testable = [pr for pr in providers if pr.get("default_model")]
    skipped = [pr["name"] for pr in providers if not pr.get("default_model")]

    print(f"Mode: {mode} | Testing {len(testable)} providers (skipped {len(skipped)} without default_model)")
    print(f"Request: {user_request!r}")
    print(f"Timeout: {args.timeout}s per provider\n")

    results: list[dict] = []
    for pr in testable:
        name = pr["name"]
        model = pr["default_model"]
        caps = CAPABILITIES.get(name, {})
        print(f"[{name}] model={model} context={caps.get('context', '?')} ... ", end="", flush=True)
        out = run_oneshot(model, user_request, args.timeout)
        out["provider"] = name
        out["model"] = model
        out["prompt"] = user_request
        out["mode"] = mode
        out["context"] = caps.get("context")
        out["max_output"] = caps.get("max_output")
        out["capabilities"] = caps
        out["ts"] = datetime.now(timezone.utc).isoformat()
        results.append(out)
        status = "OK" if out["ok"] else "FAIL"
        print(f"{status} ({out['elapsed_s']}s)")
        if not out["ok"] and out["stderr"]:
            print(f"  stderr: {out['stderr'][:200]}")

    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "request": user_request,
        "timeout_s": args.timeout,
        "tested": len(testable),
        "skipped": skipped,
        "ok_count": sum(1 for r in results if r["ok"]),
        "fail_count": sum(1 for r in results if not r["ok"]),
        "results": results,
    }

    (out_dir / "report.json").write_text(json.dumps(report, indent=2))

    md = [f"# Provider Executor Report",
          f"Generated: {report['ts']}",
          f"Mode: {mode}",
          f"Request: `{report['request']}`",
          f"Timeout: {report['timeout_s']}s",
          "",
          "## Summary",
          f"- Tested: {report['tested']}",
          f"- OK: {report['ok_count']}",
          f"- FAIL: {report['fail_count']}",
          f"- Skipped (no default_model): {report['skipped']}",
          "",
          "## Per-provider results",
          "",
          "| Provider | Model | Context | Max Output | Vision | Reasoning | OK | Elapsed (s) | Stderr (first 200) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        caps = r.get("capabilities", {})
        md.append(
            f"| {r['provider']} | `{r['model']}` | {caps.get('context', '?')} | {caps.get('output', '?')} | "
            f"{'✓' if caps.get('vision') else '✗'} | {'✓' if caps.get('reasoning') else '✗'} | "
            f"{'✓' if r['ok'] else '✗'} | {r['elapsed_s']} | {(r['stderr'] or '')[:200].replace(chr(10), ' ')} |"
        )

    md.append("\n## Successful responses (truncated)")
    for r in results:
        if r["ok"]:
            md.append(f"### {r['provider']} ({r['model']})")
            md.append(f"```\n{r['stdout'][:500]}\n```")
            md.append("")

    (out_dir / "report.md").write_text("\n".join(md))

    print(f"\nOK: {report['ok_count']} / FAIL: {report['fail_count']}")
    print(f"Report: {out_dir}/report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
