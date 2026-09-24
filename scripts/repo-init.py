#!/usr/bin/env python3
"""
Repo Init for All Installed AI Agents
Detects installed AI coding agents and scaffolds a repo to be agent-ready.
"""

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class AgentInfo:
    platform: str
    cli: str
    installed: bool
    system_prompt: str | None = None
    context_files: list = field(default_factory=list)
    notes: str = ""

def expand_user(path: str) -> Path:
    """Expand ~ to user home directory."""
    return Path(os.path.expanduser(path))

def detect_hermes() -> AgentInfo:
    hermes_root = expand_user("~/AppData/Local/hermes")
    soul = hermes_root / "SOUL.md"
    memories = hermes_root / "memories"
    profiles = hermes_root / "profiles"

    context_files = []
    if memories.exists():
        for f in ["USER.md", "MEMORY.md"]:
            p = memories / f
            if p.exists():
                context_files.append(str(p))
    if profiles.exists():
        for p in profiles.iterdir():
            if p.is_dir():
                for f in ["SOUL.md", "USER.md"]:
                    fp = p / f
                    if fp.exists():
                        context_files.append(str(fp))

    return AgentInfo(
        platform="Hermes",
        cli="hermes",
        installed=hermes_root.exists(),
        system_prompt=str(soul) if soul.exists() else None,
        context_files=context_files[:10],  # cap for readability
        notes="Profile-based identity system"
    )

def detect_opencode() -> AgentInfo:
    opencode_root = expand_user("~/.opencode")
    command_dir = opencode_root / "command"
    opencode_root / "skills"

    prompts = []
    if command_dir.exists():
        for f in command_dir.glob("*.md"):
            prompts.append(str(f))

    return AgentInfo(
        platform="OpenCode",
        cli="opencode",
        installed=opencode_root.exists(),
        system_prompt=str(prompts[0]) if prompts else None,
        context_files=prompts[:5],
        notes="Command-based prompts"
    )

def detect_codex() -> AgentInfo:
    codex_root = expand_user("~/.codex")
    agents_dir = codex_root / "agents"

    agents = []
    if agents_dir.exists():
        for f in agents_dir.glob("*.toml"):
            agents.append(str(f))

    return AgentInfo(
        platform="Codex",
        cli="codex",
        installed=codex_root.exists(),
        system_prompt=str(agents[0]) if agents else None,
        context_files=agents[:5],
        notes="TOML-based agent config"
    )

def detect_copilot() -> AgentInfo:
    copilot_root = expand_user("~/.copilot")
    gh_agents = Path(".github/agents")

    agents = []
    if gh_agents.exists():
        for f in gh_agents.glob("*.agent.md"):
            agents.append(str(f))

    return AgentInfo(
        platform="Copilot",
        cli="copilot",
        installed=copilot_root.exists() or gh_agents.exists(),
        system_prompt=str(agents[0]) if agents else None,
        context_files=agents[:5],
        notes=".github/agents/ for repo-level agents"
    )

def detect_claude() -> AgentInfo:
    claude_root = expand_user("~/.claude")
    workspace_claude = Path("CLAUDE.md")

    return AgentInfo(
        platform="Claude",
        cli="claude",
        installed=claude_root.exists() or workspace_claude.exists(),
        system_prompt=str(workspace_claude) if workspace_claude.exists() else None,
        context_files=[str(workspace_claude)] if workspace_claude.exists() else [],
        notes="CLAUDE.md in workspace root"
    )

def detect_cursor() -> AgentInfo:
    cursor_rules = Path(".cursorrules")
    cursor_mdc = Path(".cursor/rules/sandbox.mdc")

    files = []
    if cursor_rules.exists():
        files.append(str(cursor_rules))
    if cursor_mdc.exists():
        files.append(str(cursor_mdc))

    return AgentInfo(
        platform="Cursor",
        cli="cursor",
        installed=cursor_rules.exists() or cursor_mdc.exists(),
        system_prompt=str(cursor_rules) if cursor_rules.exists() else None,
        context_files=files,
        notes=".cursorrules + .cursor/rules/*.mdc"
    )

def detect_gh_cli() -> AgentInfo:
    import shutil
    gh_path = shutil.which("gh")
    return AgentInfo(
        platform="GitHub CLI",
        cli="gh",
        installed=gh_path is not None,
        notes="Tool, not an agent — no system prompt"
    )

ALL_DETECTORS = [
    detect_hermes,
    detect_opencode,
    detect_codex,
    detect_copilot,
    detect_claude,
    detect_cursor,
    detect_gh_cli,
]

def list_agents(as_json: bool = False) -> list[AgentInfo]:
    agents = [det() for det in ALL_DETECTORS]
    if as_json:
        print(json.dumps([asdict(a) for a in agents], indent=2))
    else:
        print(f"{'Platform':<15} {'Installed':<10} {'CLI':<12} {'System Prompt':<40} {'Context Files'}")
        print("-" * 120)
        for a in agents:
            sp = a.system_prompt or "—"
            if len(sp) > 38:
                sp = "..." + sp[-35:]
            cf = f"{len(a.context_files)} file(s)" if a.context_files else "—"
            print(f"{a.platform:<15} {'✓' if a.installed else '✗':<10} {a.cli:<12} {sp:<40} {cf}")
    return agents

def scaffold_repo(target_dir: str, force: bool = False) -> list[str]:
    target = Path(target_dir)
    created = []

    # AGENTS.md
    agents_md = target / "AGENTS.md"
    if agents_md.exists() and not force:
        print(f"  SKIP (exists): {agents_md}")
    else:
        content = """# AGENTS.md — Agent Context for This Repository

## Overview
This file provides context for AI coding agents working in this repository.

## Repository Structure
- **Language**: See package.json / pyproject.toml
- **Build**: See project config
- **Tests**: See project config

## Agent Guidelines
1. Read this file before making changes
2. Follow existing code style and conventions
3. Run tests before committing
4. Do not modify .env or credential files
5. Keep changes minimal and focused

## Installed Agents
Run `python scripts/repo-init.py --list-agents` for current agent inventory.
"""
        agents_md.write_text(content, encoding="utf-8")
        created.append(str(agents_md))
        print(f"  CREATED: {agents_md}")

    # docs/ai-agents-inventory.md
    docs_dir = target / "docs"
    docs_dir.mkdir(exist_ok=True)
    inventory = docs_dir / "ai-agents-inventory.md"
    if inventory.exists() and not force:
        print(f"  SKIP (exists): {inventory}")
    else:
        lines = ["# AI Agents Inventory\n", "Generated by `repo-init.py`\n"]
        agents = list_agents(as_json=False)
        lines.append("\n## Detection Roots\n")
        lines.append("| Platform | CLI | System Prompt | Context Files |")
        lines.append("|----------|-----|---------------|---------------|")
        for a in agents:
            sp = os.path.basename(a.system_prompt) if a.system_prompt else "—"
            cf = f"{len(a.context_files)}" if a.context_files else "0"
            lines.append(f"| {a.platform} | {a.cli} | {sp} | {cf} |")
        inventory.write_text("\n".join(lines), encoding="utf-8")
        created.append(str(inventory))
        print(f"  CREATED: {inventory}")

    # .github/agents/README.md
    gh_agents = target / ".github" / "agents"
    gh_agents.mkdir(parents=True, exist_ok=True)
    readme = gh_agents / "README.md"
    if readme.exists() and not force:
        print(f"  SKIP (exists): {readme}")
    else:
        content = """# GitHub Copilot Agents

Place `.agent.md` files in this directory for GitHub Copilot agent definitions.

See [GitHub Copilot Agents docs](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent) for the format.
"""
        readme.write_text(content, encoding="utf-8")
        created.append(str(readme))
        print(f"  CREATED: {readme}")

    return created

def verify_repo(target_dir: str) -> bool:
    target = Path(target_dir)
    checks = [
        target / "AGENTS.md",
        target / "docs" / "ai-agents-inventory.md",
        target / ".github" / "agents" / "README.md",
    ]
    all_ok = True
    for p in checks:
        if p.exists():
            print(f"  ✓ {p}")
        else:
            print(f"  ✗ MISSING: {p}")
            all_ok = False

    if all_ok:
        print("\nRESULT: OK — All templates present")
    else:
        print("\nRESULT: FAIL — Missing templates")
    return all_ok

def main():
    parser = argparse.ArgumentParser(description="Repo Init for All Installed AI Agents")
    parser.add_argument("--list-agents", action="store_true", help="List all detected agents")
    parser.add_argument("--json", action="store_true", help="Output as JSON (with --list-agents)")
    parser.add_argument("--init", metavar="DIR", help="Scaffold a repo at DIR")
    parser.add_argument("--verify", metavar="DIR", help="Verify repo has all templates")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files with --init")

    args = parser.parse_args()

    if args.list_agents:
        list_agents(as_json=args.json)
    elif args.init:
        print(f"Scaffolding repo at {args.init}...")
        created = scaffold_repo(args.init, force=args.force)
        print(f"\nCreated {len(created)} file(s)")
    elif args.verify:
        ok = verify_repo(args.verify)
        sys.exit(0 if ok else 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
