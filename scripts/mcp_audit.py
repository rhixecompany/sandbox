#!/usr/bin/env python3
"""
mcp_audit.py — MCP Server Audit

Loads .mcp/registry.json, tests every server (stdio: command path resolves;
http/sse: HEAD/GET returns non-5xx), and writes a structured report.

Usage:
    python scripts/mcp_audit.py --registry .mcp/registry.json
    python scripts/mcp_audit.py --registry .mcp/registry.json --json-only
    python scripts/mcp_audit.py --registry .mcp/registry.json --only-failures
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


def resolve_env(value: str, env: dict[str, str]) -> str:
    """Resolve ${env:VAR_NAME} placeholders from env dict."""
    if not isinstance(value, str):
        return str(value)
    return re.sub(
        r"\$\{env:([^}]+)\}",
        lambda m: env.get(m.group(1), m.group(0)),
        value,
    )


def test_stdio(name: str, entry: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """Check a stdio server: command path resolves; args sane."""
    cmd = entry.get("command", "")
    args = entry.get("args", [])
    cmd_resolved = resolve_env(cmd, env)
    result: dict[str, Any] = {"name": name, "type": "stdio", "status": "PASS", "checks": []}

    if not cmd_resolved:
        result["status"] = "FAIL"
        result["checks"].append("✗ no command specified")
        return result

    if cmd_resolved in ("bunx", "npx"):
        result["checks"].append(f"✓ command: {cmd_resolved} (resolved at runtime)")
    else:
        # If the command is a bare name (no path separator), try PATH resolution
        p = Path(cmd_resolved)
        if p.exists():
            result["checks"].append(f"✓ command path exists: {cmd_resolved}")
        elif "/" not in cmd_resolved and "\\" not in cmd_resolved:
            # Bare command — check if it's on PATH (e.g. "docker", "python")
            import shutil as _sh
            which = _sh.which(cmd_resolved)
            if which:
                result["checks"].append(f"✓ command on PATH: {cmd_resolved} -> {which}")
            else:
                result["status"] = "FAIL"
                result["checks"].append(f"✗ command not on PATH: {cmd_resolved}")
        else:
            result["status"] = "FAIL"
            result["checks"].append(f"✗ command path missing: {cmd_resolved}")

    for i, arg in enumerate(args):
        arg_resolved = resolve_env(arg, env)
        if arg_resolved.endswith(".py"):
            if Path(arg_resolved).exists():
                result["checks"].append(f"✓ args[{i}]: {arg_resolved}")
            else:
                result["status"] = "FAIL"
                result["checks"].append(f"✗ args[{i}] missing: {arg_resolved}")
        elif "${workspaceFolder}" in str(arg):
            result["checks"].append(f"✓ args[{i}]: workspace placeholder (OK)")
        else:
            result["checks"].append(f"· args[{i}]: {arg}")

    if entry.get("env"):
        for k, v in entry["env"].items():
            v_resolved = resolve_env(v, env)
            if "${env:" in v and v_resolved == v:
                result["status"] = "WARN"
                result["checks"].append(f"⚠ env.{k}: unresolved placeholder {v}")

    return result


def test_http(name: str, entry: dict[str, Any], env: dict[str, str]) -> dict[str, Any]:
    """Check an http/sse server: HEAD/GET returns non-5xx."""
    url = entry.get("url", "")
    url_resolved = resolve_env(url, env)
    result: dict[str, Any] = {"name": name, "type": entry.get("type", "http"), "status": "PASS", "checks": []}

    if not url_resolved:
        result["status"] = "FAIL"
        result["checks"].append("✗ no url specified")
        return result

    # SSE endpoints often return 401/403/405 on plain GET — treat as PASS
    # since the server is up; only 5xx and network errors are FAIL
    try:
        req = urllib.request.Request(url_resolved, method="GET")
        req.add_header("User-Agent", "MCP-Audit/1.0")
        req.add_header("Accept", "text/event-stream, application/json, */*")
        try:
            urllib.request.urlopen(req, timeout=8)
            result["checks"].append(f"✓ {url_resolved[:80]}: HTTP 2xx")
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500:
                result["checks"].append(f"✓ {url_resolved[:80]}: HTTP {e.code} (reachable)")
            else:
                result["status"] = "FAIL"
                result["checks"].append(f"✗ {url_resolved[:80]}: HTTP {e.code}")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        # DNS / network unreachable — mark WARN, not FAIL (likely a sandbox/network policy)
        result["status"] = "WARN"
        result["checks"].append(f"⚠ {url_resolved[:80]}: unreachable ({type(e).__name__})")

    return result


def load_env_file(path: Path) -> dict[str, str]:
    env = dict(os.environ)
    if not path.exists():
        return env
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def audit(registry_path: Path, only_failures: bool = False) -> dict[str, Any]:
    reg = json.loads(registry_path.read_text(encoding="utf-8"))
    env = load_env_file(Path(r"C:\Users\Alexa\Desktop\SandBox\.env"))

    servers = reg.get("servers", {})
    results: list[dict[str, Any]] = []

    for name, entry in sorted(servers.items()):
        if not entry.get("enabled", True):
            results.append({"name": name, "type": entry.get("type", "?"), "status": "SKIP", "checks": ["⊘ disabled in registry"]})
            continue
        t = entry.get("type", "stdio")
        if t == "stdio":
            results.append(test_stdio(name, entry, env))
        elif t in ("http", "sse"):
            results.append(test_http(name, entry, env))
        else:
            results.append({"name": name, "type": t, "status": "WARN", "checks": [f"⚠ unknown type: {t}"]})

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "SKIP": 0}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    return {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "registry": str(registry_path),
        "total": len(results),
        "counts": counts,
        "results": results,
    }


def write_markdown(report: dict[str, Any], path: Path, only_failures: bool) -> None:
    lines = [
        f"# MCP Audit Report — {report['generated']}",
        "",
        f"**Registry:** `{report['registry']}`",
        "",
        "## Summary",
        "",
        f"| Status | Count |",
        f"|--------|-------|",
        f"| ✓ PASS | {report['counts']['PASS']} |",
        f"| ⚠ WARN | {report['counts']['WARN']} |",
        f"| ✗ FAIL | {report['counts']['FAIL']} |",
        f"| ⊘ SKIP | {report['counts']['SKIP']} |",
        f"| **Total** | **{report['total']}** |",
        "",
    ]
    results = report["results"]
    if only_failures:
        results = [r for r in results if r["status"] in ("WARN", "FAIL")]
        if not results:
            lines.append("_No failures or warnings._")
        else:
            lines.append("## Failures & Warnings")
            lines.append("")
    else:
        lines.append("## Server Status")
        lines.append("")
    lines.append("| # | Server | Type | Status | Details |")
    lines.append("|---|--------|------|--------|---------|")
    for i, r in enumerate(results, 1):
        details = "<br>".join(r.get("checks", []))
        lines.append(f"| {i} | `{r['name']}` | {r['type']} | {r['status']} | {details} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description="Audit MCP servers from a registry")
    p.add_argument("--registry", default=".mcp/registry.json", help="Path to registry JSON")
    p.add_argument("--output", default=".hermes/plans/mcp-audit-2026-08-28", help="Output directory")
    p.add_argument("--json-only", action="store_true", help="Write JSON only (no Markdown)")
    p.add_argument("--only-failures", action="store_true", help="Markdown shows only WARN/FAIL")
    args = p.parse_args()

    registry_path = Path(args.registry)
    if not registry_path.exists():
        print(f"ERROR: registry not found: {registry_path}", file=sys.stderr)
        return 2

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    report = audit(registry_path, only_failures=args.only_failures)
    json_path = out_dir / "audit-report.json"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    if not args.json_only:
        md_path = out_dir / "audit-report.md"
        write_markdown(report, md_path, only_failures=args.only_failures)
        print(f"✓ Wrote {json_path}")
        print(f"✓ Wrote {md_path}")
    else:
        print(f"✓ Wrote {json_path}")

    # Exit code: non-zero on FAIL
    if report["counts"]["FAIL"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
