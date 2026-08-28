#!/usr/bin/env python3
"""
fanout.py — Multi-agent / multi-provider fanout orchestrator.

Reads scripts/.runtime/provider_inventory.json, builds the (provider, agent)
cell matrix, runs each cell non-interactively with a prompt, and writes a
structured report to .hermes/plans/multi-agent-fanout-<date>/fanout-report.json.

Output schema (per cell):
    {
      "provider": str,
      "model": str,
      "agent": str,
      "context_window": int,
      "max_output_tokens": int,
      "capabilities": {vision, tools, json_mode, streaming, system_prompt},
      "status": "ok" | "fail" | "auth_failed" | "skip",
      "latency_ms": int,
      "output_text": str,
      "output_tokens": int | None,
      "prompt_tokens": int | None,
      "error": str | None
    }

Usage:
    python scripts/fanout.py --smoke                          # 1-2 cells
    python scripts/fanout.py --provider openrouter --smoke    # 1 cell on openrouter
    python scripts/fanout.py --prompt "Summarize this..."      # full fanout
    python scripts/fanout.py --dry-run                        # build report skeleton only
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Make scripts/ importable
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from fanout.providers import openai_compat  # noqa: E402
from fanout.agents import codex, copilot, hermes, opencode  # noqa: E402


# Default smoke cell: 1 openrouter call through the in-tree package
SMOKE_CELLS = [
    {
        "provider": "openrouter",
        "model": "minimax/minimax-m3:free",
        "agent": "openai-compat (matches openrouter-client-py protocol)",
        "env_var": "OPENROUTER_API_KEY",
        "kind": "provider",
    },
]


def build_cells(inventory: dict, smoke: bool = False, only_provider: str | None = None) -> list[dict]:
    """
    Build the (provider, agent) cell matrix.

    - smoke=True: return only SMOKE_CELLS
    - only_provider: filter to that provider
    - otherwise: every provider × its default agent
    """
    if smoke:
        return SMOKE_CELLS

    cells: list[dict] = []
    for prov in inventory["providers"]:
        if only_provider and prov["name"] != only_provider:
            continue
        caps = prov.get("capabilities_static") or {}
        # Determine agent + cell kind from provider type
        if prov["name"] == "openrouter":
            cells.append({
                "provider": "openrouter",
                "model": caps.get("default_model", "openrouter/auto"),
                "agent": "openai-compat (matches in-tree openrouter-client-py protocol)",
                "env_var": "OPENROUTER_API_KEY",
                "kind": "provider",
            })
        elif prov["name"] == "openai-codex":
            cells.append({
                "provider": "openai-codex",
                "model": caps.get("default_model", "gpt-4o"),
                "agent": "codex-cli",
                "env_var": None,
                "kind": "agent",
            })
        elif prov["name"] == "copilot":
            cells.append({
                "provider": "copilot",
                "model": caps.get("default_model", "gpt-4o"),
                "agent": "copilot-cli",
                "env_var": "GITHUB_TOKEN",
                "kind": "agent",
            })
        else:
            # OpenAI-compatible providers — use openai_compat adapter
            cells.append({
                "provider": prov["name"],
                "model": caps.get("default_model", ""),
                "agent": "openai-compat",
                "env_var": _env_var_for(prov["name"]),
                "kind": "provider",
                "base_url": caps.get("base_url"),
            })
    return cells


def _env_var_for(provider_name: str) -> str | None:
    return {
        "deepseek": "DEEPSEEK_API_KEY",
        "gemini": "GOOGLE_API_KEY",
        "xai": "XAI_API_KEY",
        "xai-oauth": None,
        "nous": None,
        "opencode-zen": "OPENCODE_ZEN_API_KEY",
        "ollama-cloud": "OLLAMA_API_KEY",
        "huggingface": "HF_TOKEN",
    }.get(provider_name)


def get_api_key(cell: dict) -> str | None:
    if not cell.get("env_var"):
        return None
    return os.environ.get(cell["env_var"])


async def run_cell(cell: dict, prompt: str, inventory: dict | None = None) -> dict[str, Any]:
    """Run one (provider, agent) cell. Returns result dict in the output schema."""
    # Look up static capabilities from inventory if not present on cell
    caps: dict = cell.get("capabilities_static") or {}
    if not caps and inventory is not None:
        for prov in inventory.get("providers", []):
            if prov.get("name") == cell.get("provider"):
                caps = prov.get("capabilities_static") or {}
                break
    base: dict[str, Any] = {
        "provider": cell["provider"],
        "model": cell["model"],
        "agent": cell["agent"],
        "context_window": caps.get("context_window_default"),
        "max_output_tokens": caps.get("max_output_default"),
        "capabilities": {
            "vision": caps.get("vision", False),
            "tools": caps.get("tools", False),
            "json_mode": caps.get("json_mode", False),
            "streaming": caps.get("streaming", False),
            "system_prompt": caps.get("system_prompt", False),
        },
        "status": "pending",
        "latency_ms": 0,
        "output_text": "",
        "output_tokens": None,
        "prompt_tokens": None,
        "error": None,
    }

    api_key = get_api_key(cell)
    if cell["kind"] == "agent":
        # Agent-cell: route through the agent CLI
        adapter = {
            "codex-cli": codex,
            "copilot-cli": copilot,
            "hermes-cli": hermes,
            "opencode-cli": opencode,
        }.get(cell["agent"])
        if adapter is None:
            base["status"] = "skip"
            base["error"] = f"no adapter for agent {cell['agent']}"
            return base
        try:
            r = await adapter.call(prompt, model=cell.get("model"))
        except Exception as e:
            base["status"] = "fail"
            base["error"] = f"{type(e).__name__}: {e}"
            return base
        base["latency_ms"] = r.get("latency_ms", 0)
        base["output_text"] = r.get("output_text", "")
        base["error"] = r.get("error")
        if r.get("exit_code", 0) == 0 and not r.get("error"):
            base["status"] = "ok"
        else:
            base["status"] = "fail" if r.get("exit_code", 0) != 0 else "auth_failed"
        return base

    # Provider-cell
    if not api_key:
        base["status"] = "auth_failed"
        base["error"] = f"env var {cell.get('env_var')!r} not set"
        return base

    # All providers including openrouter are reached via the openai-compat
    # /chat/completions endpoint. (The in-tree openrouter-client-py package is
    # documented and inspected by package_inspector.py but its openrouter SDK
    # dep is not yet installed in this environment, so we call the same
    # OpenAI-compatible protocol directly with stdlib.)
    base_url = cell.get("base_url") or caps.get("base_url") or ""
    if not base_url:
        base["status"] = "fail"
        base["error"] = f"no base_url for provider {cell['provider']}"
        return base
    r = await openai_compat.call(prompt, model=cell["model"], api_key=api_key,
                                 base_url=base_url)
    base["latency_ms"] = r.get("latency_ms", 0)
    base["output_text"] = r.get("output_text", "")
    base["output_tokens"] = r.get("output_tokens")
    base["prompt_tokens"] = r.get("prompt_tokens")
    base["error"] = r.get("error")
    if r.get("error"):
        if "401" in str(r["error"]) or "403" in str(r["error"]) or "auth" in str(r["error"]).lower():
            base["status"] = "auth_failed"
        else:
            base["status"] = "fail"
    else:
        base["status"] = "ok"
    return base


def write_report(results: list[dict], prompt: str, output: Path) -> None:
    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    report = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "prompt": prompt,
        "total": len(results),
        "counts": counts,
        "results": results,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    # Also write a companion markdown report
    md = output.with_suffix(".md")
    lines = [
        f"# Fanout Report — {report['generated']}",
        "",
        f"**Prompt:** `{prompt}`",
        "",
        f"**Total:** {report['total']} cells | " + " | ".join(f"{k}={v}" for k, v in counts.items()),
        "",
        "| # | Provider | Model | Agent | Status | Latency | Output tokens |",
        "|---|----------|-------|-------|--------|---------|---------------|",
    ]
    for i, r in enumerate(results, 1):
        lines.append(
            f"| {i} | `{r['provider']}` | `{r['model']}` | `{r['agent']}` | "
            f"{r['status']} | {r['latency_ms']}ms | {r['output_tokens'] or '-'} |"
        )
    md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✓ Wrote {output}")
    print(f"✓ Wrote {md}")


def load_inventory() -> dict:
    p = SCRIPT_DIR / ".runtime" / "provider_inventory.json"
    if not p.exists():
        print(f"ERROR: {p} not found. Run `python scripts/auth_inventory.py` first.", file=sys.stderr)
        sys.exit(2)
    return json.loads(p.read_text(encoding="utf-8"))


def _load_hermes_env() -> None:
    """Load API keys from hermes .env if not already in os.environ."""
    hermes_env = Path(r"C:\Users\Alexa\AppData\Local\hermes\.env")
    if not hermes_env.exists():
        return
    for line in hermes_env.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip()
        if k and k not in os.environ:
            os.environ[k] = v


def main() -> int:
    ap = argparse.ArgumentParser(description="Multi-agent / multi-provider fanout")
    ap.add_argument("--prompt", default="Reply with only the word OK and your model identifier.")
    ap.add_argument("--smoke", action="store_true", help="Run only 1-2 cells")
    ap.add_argument("--provider", default=None, help="Restrict to one provider")
    ap.add_argument("--output", default=None, help="Report output path")
    ap.add_argument("--dry-run", action="store_true", help="Build cell list and write skeleton, no calls")
    args = ap.parse_args()

    _load_hermes_env()  # ensure API keys are present

    inv = load_inventory()
    cells = build_cells(inv, smoke=args.smoke, only_provider=args.provider)
    if not cells:
        print("ERROR: no cells to run", file=sys.stderr)
        return 2

    out = Path(args.output) if args.output else (
        SCRIPT_DIR / ".." / ".hermes" / "plans" /
        f"multi-agent-fanout-{datetime.now().strftime('%Y-%m-%d')}" / "fanout-report.json"
    ).resolve()

    print(f"Running {len(cells)} cell(s):")
    for c in cells:
        print(f"  - {c['provider']:18s} {c['model']:40s} via {c['agent']}")

    if args.dry_run:
        results = [{**c, "status": "dry-run", "latency_ms": 0, "output_text": "",
                    "output_tokens": None, "prompt_tokens": None, "error": None,
                    "context_window": None, "max_output_tokens": None,
                    "capabilities": {}} for c in cells]
        write_report(results, args.prompt, out)
        return 0

    results = asyncio.run(_gather(cells, args.prompt, inv))
    write_report(results, args.prompt, out)
    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"\nSummary: {counts}")
    return 0 if counts.get("ok", 0) > 0 or args.smoke else 1


async def _gather(cells: list[dict], prompt: str, inventory: dict) -> list[dict]:
    # Run sequentially to avoid hammering providers in parallel; use a semaphore
    # if we want concurrency later. Sequential keeps the smoke test predictable.
    out: list[dict] = []
    for c in cells:
        out.append(await run_cell(c, prompt, inventory))
    return out


if __name__ == "__main__":
    sys.exit(main())
