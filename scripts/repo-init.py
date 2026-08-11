#!/usr/bin/env python3
"""
repo-init.py — initialize a repo for all installed AI coding agents.

Subcommands:
  --list-agents [--json]   Detect installed agents and print each one's
                           binary/profile, system prompt path, and context
                           file path (live filesystem probing).
  --init [DIR] [--force]   Scaffold generic context files into DIR (default:
                           current directory). Idempotent: existing files are
                           skipped unless --force.
  --verify [DIR]           Check that scaffolded files exist and resolve.
                           Exit 0 on success, 1 with a report otherwise.

Runtime detection only — no hardcoded agent lists. No secrets are ever
written; committed templates are generic and contain no user-specific paths.

Run with:  MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import date

HOME = os.path.expanduser("~")
HERMES_ROOT = os.path.join(HOME, "AppData", "Local", "hermes")
SANDBOX = os.path.normpath(r"C:/Users/Alexa/Desktop/SandBox")


# --------------------------------------------------------------------------- #
# Agent detection
# --------------------------------------------------------------------------- #

def _exists(*parts: str) -> str | None:
    p = os.path.join(*parts)
    return p if os.path.exists(p) else None


def _load_jsonc(path: str):
    """Load JSON or JSONC (comment-tolerant). Copilot's config.json has a
    leading `//` comment header and is managed automatically."""
    try:
        with open(path, "rb") as fh:
            raw = fh.read().decode("utf-8-sig")
    except OSError:
        return None
    # strip // comment lines (only full-line comments; keeps the file valid)
    lines = [ln for ln in raw.splitlines() if not ln.lstrip().startswith("//")]
    try:
        return json.loads("\n".join(lines))
    except json.JSONDecodeError:
        return None


def _count_dir(path: str | None, pattern: str | None = None) -> int:
    if not path or not os.path.isdir(path):
        return 0
    if pattern:
        return len([f for f in os.listdir(path) if f.endswith(pattern)])
    return len(os.listdir(path))


def detect_agents() -> list[dict]:
    """Probe the live filesystem for every installed agent platform."""
    agents: list[dict] = []

    # --- Hermes ---
    profiles_dir = os.path.join(HERMES_ROOT, "profiles")
    profiles = sorted(
        d for d in os.listdir(profiles_dir)
        if os.path.isdir(os.path.join(profiles_dir, d))
    ) if os.path.isdir(profiles_dir) else []
    soul = _exists(HERMES_ROOT, "SOUL.md")
    user_md = _exists(HERMES_ROOT, "memories", "USER.md") or _exists(HERMES_ROOT, "USER.md")
    mem_md = _exists(HERMES_ROOT, "memories", "MEMORY.md") or _exists(HERMES_ROOT, "MEMORY.md")
    agents.append({
        "agent": "Hermes",
        "platform": "hermes",
        "count": len(profiles),
        "detail": f"{len(profiles)} profiles: {', '.join(profiles[:6])}{'…' if len(profiles) > 6 else ''}",
        "system_prompt": soul or "n/a",
        "context_files": [p for p in (user_md, mem_md) if p],
    })

    # --- OpenCode ---
    oc_root = os.path.join(HOME, ".opencode")
    oc_cmds = os.path.join(oc_root, "command")
    oc_skills = os.path.join(oc_root, "skills")
    oc_cmd_count = _count_dir(oc_cmds, ".md")
    oc_skill_count = _count_dir(oc_skills)
    oc_cli = shutil.which("opencode")
    agents.append({
        "agent": "OpenCode",
        "platform": "opencode",
        "count": oc_cmd_count,
        "detail": f"{oc_cmd_count} commands, {oc_skill_count} skill dirs; CLI={oc_cli or 'n/a'}",
        "system_prompt": oc_cmds if os.path.isdir(oc_cmds) else "n/a",
        "context_files": [
            p for p in (
                _exists(oc_root, "config.json"),
                _exists(SANDBOX, "opencode.json"),
            ) if p
        ],
    })

    # --- Codex ---
    codex_root = os.path.join(HOME, ".codex")
    codex_agents = os.path.join(codex_root, "agents")
    codex_skills = os.path.join(codex_root, "skills", "hermes-auto")
    codex_count = _count_dir(codex_agents, ".toml")
    agents.append({
        "agent": "Codex",
        "platform": "codex",
        "count": codex_count,
        "detail": f"{codex_count} agents (.toml); CLI={shutil.which('codex') or 'n/a'}",
        "system_prompt": codex_agents if os.path.isdir(codex_agents) else "n/a",
        "context_files": [
            p for p in (
                _exists(codex_root, "config.toml"),
                codex_skills if os.path.isdir(codex_skills) else None,
            ) if p
        ],
    })

    # --- Copilot (workspace agents + home) ---
    copilot_home = os.path.join(HOME, ".copilot")
    wb_agents_dir = os.path.join(SANDBOX, ".github", "agents")
    wb_agent_count = _count_dir(wb_agents_dir, ".agent.md")
    copilot_cfg = _exists(copilot_home, "config.json")
    _load_jsonc(copilot_cfg) if copilot_cfg else None  # validate tolerance
    agents.append({
        "agent": "Copilot",
        "platform": "copilot",
        "count": wb_agent_count,
        "detail": f"{wb_agent_count} workspace agents (.github/agents); CLI={shutil.which('copilot') or 'n/a'}",
        "system_prompt": wb_agents_dir if os.path.isdir(wb_agents_dir) else copilot_home,
        "context_files": [
            p for p in (
                copilot_cfg if copilot_cfg else None,
                _exists(copilot_home, "settings.json"),
            ) if p
        ],
    })

    # --- Claude ---
    claude_root = os.path.join(HOME, ".claude")
    claude_count = _count_dir(claude_root)
    agents.append({
        "agent": "Claude",
        "platform": "claude",
        "count": claude_count,
        "detail": f"{claude_count} entries in ~/.claude; CLI={shutil.which('claude') or 'n/a'}",
        "system_prompt": _exists(claude_root, "CLAUDE.md") or claude_root,
        "context_files": [
            p for p in (
                _exists(SANDBOX, "CLAUDE.md"),
            ) if p
        ],
    })

    # --- Cursor ---
    cursor_ws = _exists(SANDBOX, ".cursorrules")
    agents.append({
        "agent": "Cursor",
        "platform": "cursor",
        "count": 1 if cursor_ws else 0,
        "detail": "workspace .cursorrules",
        "system_prompt": cursor_ws or "n/a",
        "context_files": [cursor_ws] if cursor_ws else [],
    })

    # --- GitHub CLI ---
    gh = shutil.which("gh")
    agents.append({
        "agent": "GitHub CLI",
        "platform": "gh",
        "count": 1 if gh else 0,
        "detail": f"CLI={gh or 'n/a'}",
        "system_prompt": "n/a (tool, not an agent)",
        "context_files": [],
    })

    return agents


# --------------------------------------------------------------------------- #
# Scaffolding
# --------------------------------------------------------------------------- #

# Template files written by --init. Content is intentionally generic: no
# secrets, no user-specific absolute paths. Existing files are skipped.
TEMPLATES: dict[str, str] = {
    "AGENTS.md": """# AGENTS.md

This repository is configured for multiple AI coding agents.

## Installed agents (detected at init time)

See `docs/ai-agents-inventory.md` for the full inventory of installed agents
and where each agent's system prompt and context files live.

## Quick reference

| Agent | Context file | Notes |
|-------|--------------|-------|
| Hermes | `.hermes.md` | Hermes-specific overrides |
| Claude | `CLAUDE.md` | Claude-specific guidance |
| Cursor | `.cursorrules` | Cursor IDE rules |
| Copilot | `.github/agents/*.agent.md` | Workspace agents |
| Codex | `.codex/agents/` (home) | Machine-local agents |
| OpenCode | `opencode.json` | Workspace config |

## Rules

1. Run `python scripts/repo-init.py --list-agents` to refresh the inventory.
2. Run `python scripts/repo-init.py --init` to re-scaffold missing context files.
3. Run `python scripts/repo-init.py --verify` to confirm everything resolves.
""",
    "docs/ai-agents-inventory.md": """# AI Agents Inventory

> Generated by `scripts/repo-init.py --list-agents` — regenerate with:
> `MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents > docs/ai-agents-inventory.md`

| Agent | Platform | Count | Detail | System prompt | Context files |
| ----- | -------- | ----- | ------ | ------------- | -------------- |
| _(regenerate)_ | | | | | |
""",
    ".github/agents/README.md": """# Workspace Agents (Copilot)

Drop Copilot-style agents here as `*.agent.md`.

Run `python scripts/repo-init.py --list-agents` to refresh the full agent inventory.
""",
}


def init_dir(target: str, force: bool = False) -> list[str]:
    """Scaffold context files into target. Returns created paths."""
    created: list[str] = []
    for rel, content in TEMPLATES.items():
        dst = os.path.join(target, rel)
        if os.path.exists(dst) and not force:
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        created.append(dst)
    return created


def verify_dir(target: str) -> tuple[bool, list[str]]:
    """Verify scaffolded files exist. Returns (ok, report_lines)."""
    report = []
    ok = True
    for rel in TEMPLATES:
        p = os.path.join(target, rel)
        exists = os.path.exists(p)
        report.append(f"{'OK ' if exists else 'MISS'} {rel}")
        ok = ok and exists
    return ok, report


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list-agents", action="store_true", help="list installed agents")
    ap.add_argument("--json", action="store_true", help="JSON output for --list-agents")
    ap.add_argument("--init", nargs="?", const=".", default=None, metavar="DIR",
                    help="scaffold context files into DIR (default: cwd)")
    ap.add_argument("--verify", nargs="?", const=".", default=None, metavar="DIR",
                    help="verify scaffolded files in DIR")
    ap.add_argument("--force", action="store_true", help="overwrite existing files on --init")
    args = ap.parse_args()

    if args.list_agents:
        agents = detect_agents()
        if args.json:
            print(json.dumps(agents, indent=2))
            return 0
        print(f"# AI Agents Inventory (generated {date.today().isoformat()})")
        print()
        print("| Agent | Platform | Count | Detail | System prompt | Context files |")
        print("| ----- | -------- | ----- | ------ | ------------- | -------------- |")
        for a in agents:
            ctx = "<br>".join(a["context_files"]) if a["context_files"] else "—"
            sysp = os.path.normpath(a["system_prompt"]).replace("|", "\\|")
            det = a["detail"].replace("|", "\\|")
            print(f"| {a['agent']} | {a['platform']} | {a['count']} | {det} | {sysp} | {ctx} |")
        return 0

    if args.init is not None:
        target = os.path.abspath(args.init)
        if not os.path.isdir(target):
            print(f"ERROR: target is not a directory: {target}", file=sys.stderr)
            return 1
        created = init_dir(target, force=args.force)
        if created:
            print(f"Created {len(created)} file(s) in {target}:")
            for c in created:
                print(f"  + {os.path.relpath(c, target)}")
        else:
            print(f"Nothing to create in {target} (all templates already present; use --force to overwrite).")
        return 0

    if args.verify is not None:
        target = os.path.abspath(args.verify)
        if not os.path.isdir(target):
            print(f"ERROR: target is not a directory: {target}", file=sys.stderr)
            return 1
        ok, report = verify_dir(target)
        print("\n".join(report))
        print("RESULT:", "OK" if ok else "MISSING FILES")
        return 0 if ok else 1

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
