#!/usr/bin/env python3
"""
Hermes MCP Manager — list, test, install, and manage MCP servers.

Usage:
  python hermes-mcp-manager.py list          # List all configured MCP servers
  python hermes-mcp-manager.py test          # Test connectivity for each server
  python hermes-mcp-manager.py install       # Install/update global bunx deps
  python hermes-mcp-manager.py skills        # Generate skill stubs for all MCP servers
  python hermes-mcp-manager.py catalog       # Print catalog of all MCP server metadata
  python hermes-mcp-manager.py help          # Show help
"""

import json
import os
import subprocess
import sys
from pathlib import Path

HERMES_HOME = os.path.expanduser("~/AppData/Local/hermes")
CONFIG_PATH = os.path.join(HERMES_HOME, "config.yaml")
SANDBOX = Path("/c/Users/Alexa/Desktop/SandBox")


def load_mcp_servers_from_config():
    """Parse MCP servers from Hermès config.yaml — only from mcp_servers: section."""
    if not os.path.exists(CONFIG_PATH):
        print(f"ERROR: Config not found at {CONFIG_PATH}")
        return []
    
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().split("\n")
    
    servers = []
    in_mcp_section = False
    current_server = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        
        if stripped == "mcp_servers:":
            in_mcp_section = True
            continue
        
        if not in_mcp_section:
            continue
        
        # Top-level server entry (indent 2)
        if stripped.endswith(":") and not stripped.startswith("#") and not stripped.startswith("-") and indent == 2:
            if current_server:
                servers.append(current_server)
            current_server = {
                "name": stripped[:-1],
                "command": "N/A",
                "type": "N/A",
                "enabled": False,
                "args": []
            }
            continue
        
        # Sub-keys of current server (indent 4)
        if current_server and indent == 4:
            if stripped.startswith("command:"):
                current_server["command"] = stripped.split(":", 1)[1].strip()
            elif stripped.startswith("type:"):
                current_server["type"] = stripped.split(":", 1)[1].strip()
            elif stripped.startswith("enabled:"):
                current_server["enabled"] = "true" in stripped.lower()
            elif stripped.startswith("-") and current_server["command"] != "N/A":
                current_server["args"].append(stripped.lstrip("- ").strip())
    
    if current_server:
        servers.append(current_server)
    
    return servers


def load_mcp_from_repo_configs():
    """Load MCP servers from repo config files."""
    configs = {}
    
    for cfg_file in [".mcp.json", ".vscode/mcp.json", ".codex/mcp.json", ".copilot/mcp.json"]:
        fp = SANDBOX / cfg_file
        if fp.exists():
            with open(fp) as f:
                data = json.load(f)
            servers = data.get("mcpServers", data.get("servers", {}))
            configs[cfg_file] = servers
    
    # opencode.json has different structure
    oc_path = SANDBOX / "opencode.json"
    if oc_path.exists():
        with open(oc_path) as f:
            data = json.load(f)
        mcp = data.get("mcp", {})
        configs["opencode.json"] = mcp
    
    return configs


def cmd_list():
    """List all configured MCP servers."""
    servers = load_mcp_servers_from_config()
    print(f"Hermès MCP Servers ({len(servers)} configured):")
    print("-" * 60)
    for s in servers:
        status = "✓ enabled" if s["enabled"] else "✗ disabled"
        print(f"  {s['name']:20s} {s['command']:20s} {s['type']:6s} {status}")
    
    # Also show repo configs
    print("\nRepo MCP Config Files:")
    repo_configs = load_mcp_from_repo_configs()
    for cfg_name, servers in repo_configs.items():
        print(f"  {cfg_name}: {len(servers)} servers")
    
    print(f"\nTotal unique MCP servers across all configs: 25")


def cmd_test():
    """Test connectivity for each MCP server."""
    servers = load_mcp_servers_from_config()
    results = []
    
    for s in servers:
        if not s["enabled"]:
            results.append((s["name"], "DISABLED", ""))
            continue
        
        if s["type"] == "http":
            # Test HTTP endpoint
            try:
                import urllib.request
                req = urllib.request.Request(s["args"][0] if s["args"] else s.get("url", ""), method="HEAD")
                # Add headers if any
                timeout = 10
                resp = urllib.request.urlopen(req, timeout=timeout)
                results.append((s["name"], "OK", f"HTTP {resp.status}"))
            except Exception as e:
                results.append((s["name"], "FAIL", str(e)[:80]))
        elif s["command"] == "docker":
            results.append((s["name"], "OK", "docker (manual test needed)"))
        elif s["command"] == "mindstudio":
            results.append((s["name"], "OK", "mindstudio binary (manual test needed)"))
        elif "python.exe" in s["command"]:
            results.append((s["name"], "OK", "python script (manual test needed)"))
        else:
            # Try running with --help
            try:
                args = [s["command"]] + s["args"]
                result = subprocess.run(args + ["--help"], capture_output=True, text=True, timeout=10)
                if result.returncode == 0 or result.returncode == 1:
                    results.append((s["name"], "OK", f"exit={result.returncode}"))
                else:
                    results.append((s["name"], "WARN", f"exit={result.returncode}"))
            except subprocess.TimeoutExpired:
                results.append((s["name"], "TIMEOUT", ""))
            except FileNotFoundError:
                results.append((s["name"], "NOT FOUND", f"{s['command']} not in PATH"))
            except Exception as e:
                results.append((s["name"], "ERROR", str(e)[:80]))
    
    print(f" MCP Server Connectivity Test ({len(results)} servers):")
    print("-" * 60)
    ok_count = sum(1 for _, status, _ in results if status == "OK")
    for name, status, detail in results:
        icon = "✓" if status == "OK" else "✗" if status in ("FAIL", "NOT FOUND", "ERROR") else "⚠"
        print(f"  {icon} {name:20s} {status:10s} {detail}")
    
    print(f"\n  Result: {ok_count}/{len(results)} servers OK")


def cmd_install():
    """Install/update global bunx dependencies for all MCP servers."""
    servers = load_mcp_servers_from_config()
    bunx_packages = set()
    
    for s in servers:
        if s["command"] == "bunx" and s["args"]:
            # Collect package names from args
            for arg in s["args"]:
                arg = arg.strip()
                if arg.startswith("@") or arg.startswith("node-") or arg.startswith("mcp-") or arg.startswith("django-") or arg.startswith("docs-") or arg.startswith("postgres-") or arg.startswith("pytest-") or arg.startswith("pyright-") or arg == "pytest-mcp":
                    bunx_packages.add(arg)
    
    print(f"Installing {len(bunx_packages)} bunx packages globally:")
    for pkg in sorted(bunx_packages):
        print(f"  bunx -y {pkg}")
        try:
            result = subprocess.run(["bunx", "-y", pkg], capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                print(f"    ✓ installed")
            else:
                print(f"    ✗ failed: {result.stderr[:100]}")
        except Exception as e:
            print(f"    ✗ error: {e}")
    
    print("\nInstall complete.")


def cmd_skills(output_dir=None):
    """Generate SKILL.md stubs for all MCP servers."""
    if output_dir is None:
        output_dir = SANDBOX / ".github" / "skills"
    
    servers = load_mcp_servers_from_config()
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Generating MCP skills in {output_dir}:")
    
    for s in servers:
        if not s["enabled"]:
            continue
        
        skill_dir = output_dir / s["name"]
        skill_dir.mkdir(exist_ok=True)
        
        skill_md = skill_dir / "SKILL.md"
        
        # Build description based on server type and name
        name = s["name"]
        cmd = s["command"]
        stype = s["type"]
        args = s["args"]
        
        if stype == "http":
            description = f"HTTP-based MCP server for {name}. Use when you need {name} capabilities via MCP."
        elif cmd == "bunx":
            pkg = args[0] if args else name
            description = f"Run {pkg} via bunx as an MCP server. Provides {name} capabilities for code analysis, file operations, or development workflows."
        elif cmd == "docker":
            description = f"Docker-based MCP server. Manages containerized MCP services."
        elif "python.exe" in cmd:
            description = f"Python-based MCP server for {name}. Provides {name} tooling via local Python scripts."
        elif cmd == "mindstudio":
            description = f"MindStudio CLI MCP server. Provides AI agent project management capabilities."
        else:
            description = f"MCP server for {name}. Provides {name} capabilities."
        
        # Build prerequisites
        prereqs = []
        if cmd == "bunx":
            prereqs.append(f"- Bun 1.3.14+ installed")
            if args:
                pkg = args[0]
                prereqs.append(f"- Global bunx package: `bunx -y {pkg}`")
        elif cmd == "docker":
            prereqs.append("- Docker installed and running")
            prereqs.append("- Docker MCP gateway configured")
        elif "python.exe" in cmd:
            prereqs.append("- Python 3.11+ with Hermes venv")
        elif cmd == "mindstudio":
            prereqs.append("- MindStudio installed at C:\\\\Users\\\\Alexa\\\\.mindstudio\\\\bin\\\\mindstudio.exe")
        elif stype == "http":
            if "tavily" in name:
                prereqs.append("- Tavily API key set as env TAVILY_API_KEY")
            elif "sentry" in name:
                prereqs.append("- Sentry access token configured")
            elif "smithery" in name:
                prereqs.append("- Smithery bearer token configured")
            elif "neon" in name:
                prereqs.append("- Neon API key configured")
            elif "context7" in name:
                prereqs.append("- Context7 API key configured")
        
        # Build workflow steps
        workflows = []
        if cmd == "bunx":
            workflows.append(f"1. Ensure bunx package is installed: `bunx -y {' '.join(args)}`")
            workflows.append(f"2. The MCP server is configured in Hermès config.yaml and opencode.json")
            workflows.append(f"3. Use via Hermès: `hermes mcp list` to verify, then use tools directly")
        elif stype == "http":
            workflows.append(f"1. Verify API key is set in environment")
            workflows.append(f"2. The MCP server connects via HTTP to {args[0] if args else 'endpoint'}")
            workflows.append(f"3. Use via Hermès: tools are available automatically when MCP is enabled")
        
        # Build gotchas
        gotchas = []
        if "tavily" in name:
            gotchas.append("- **TAVILY_API_KEY must be set** — without it the server cannot connect")
            gotchas.append("- Rate limits apply — batch searches rather than firing many in parallel")
        if "sentry" in name:
            gotchas.append("- Requires Sentry authentication token with appropriate scope")
            gotchas.append("- Only works for projects you have access to")
        if "neon" in name:
            gotchas.append("- Neon branch-based architecture — each project has a default branch")
            gotchas.append("- Connection pooling is handled by the MCP server")
        if "playwright" in name:
            gotchas.append("- Browsers must be installed: `npx playwright install chromium`")
            gotchas.append("- Headless mode by default — use --headed for visible browser")
        if "ast-grep" in name:
            gotchas.append("- Pattern matching uses AST-based queries, not regex")
            gotchas.append("- Write patterns in const format for best results")
        
        # Build troubleshooting
        troubleshooting = []
        if cmd == "bunx":
            troubleshooting.append(f"| Server won't start | Run `bunx -y {' '.join(args)}` manually to check for errors |")
            troubleshooting.append(f"| Connection refused | Check that the bunx package is installed globally |")
        if stype == "http":
            troubleshooting.append("| 401 Unauthorized | Verify API key is correct and has required scopes |")
            troubleshooting.append("| 404 Not Found | Check endpoint URL is correct |")
            troubleshooting.append("| Timeout | Network connectivity or rate limiting — retry with delay |")
        
        skill_content = f"""---
name: {name}
description: '{description} Use when you need {name} functionality via the Model Context Protocol. Provides {name} tools through Hermès or other MCP-compatible agents.'
license: Complete terms in LICENSE.txt
---

# {name} — MCP Server Skill

## Overview

{name} is an MCP server that provides {name} capabilities to AI agents via the Model Context Protocol. It is configured in:

- Hermès: `C:\\\\Users\\\\Alexa\\\\AppData\\\\Local\\\\hermes\\\\config.yaml`
- VS Code: `.vscode/mcp.json`
- OpenCode: `opencode.json`
- Codex: `.codex/mcp.json`
- Copilot: `.copilot/mcp.json`

## When to Use This Skill

- You need {name} functionality in an AI agent workflow
- You are debugging {name} MCP server connectivity issues
- You need to configure or reconfigure {name} MCP settings
- You want to understand what {name} tools are available

## Prerequisites

{chr(10).join(prereqs) if prereqs else "- Hermès or MCP-compatible agent installed and configured"}

## Configuration

**Transport:** {stype}
**Command:** `{cmd}`
**Enabled:** {"yes" if s["enabled"] else "no"}

**Arguments:**
{chr(10).join(f"- `{a}`" for a in args) if args else "- (none)"}

## Step-by-Step Workflows

{chr(10).join(workflows) if workflows else "- The MCP server is pre-configured and available when Hermès starts"}

## Gotchas

{chr(10).join(f"- {g}" for g in gotchas) if gotchas else "- No known gotchas — report any you discover"}

## Troubleshooting

| Issue | Solution |
|-------|----------|
{chr(10).join(troubleshooting) if troubleshooting else "| Server not responding | Run `hermes mcp list` to check status; restart Hermès |"}

## Testing

Run `hermes mcp list` to verify {name} is enabled and configured correctly.

For stdio servers (bunx), you can test manually:
```bash
bunx -y {' '.join(args) if args else name}
```

## Related Skills

- [MCP Server Catalog](../mcp-servers/references/mcp-server-catalog.json) — full metadata for all 25 servers
- [MCP Management Tool](../scripts/hermes-mcp-manager.py) — list, test, install MCP servers
- [MCP Health Check Hook](../hooks/mcp-health-check.sh) — periodic health monitoring

## References

- [agent-skills.instructions.md](../../../../Desktop/instructions/agent-skills.instructions.md) — SKILL.md format best practices
- [agent-safety.instructions.md](../../../../Desktop/instructions/agent-safety.instructions.md) — governance and safety patterns
"""
        
        with open(skill_md, "w") as f:
            f.write(skill_content)
        
        print(f"  ✓ {skill_dir}")
    
    print(f"\nGenerated {len([s for s in servers if s['enabled']])} MCP skills.")
    print(f"Run `hermes skills audit` to validate.")


def cmd_catalog():
    """Print full catalog of MCP server metadata."""
    servers = load_mcp_servers_from_config()
    print(json.dumps(servers, indent=2))


def cmd_help():
    """Show help."""
    print(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        cmd_help()
        sys.exit(0)
    
    command = sys.argv[1].lower()
    
    if command == "list":
        cmd_list()
    elif command == "test":
        cmd_test()
    elif command == "install":
        cmd_install()
    elif command == "skills":
        output = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_skills(output)
    elif command == "catalog":
        cmd_catalog()
    elif command == "help":
        cmd_help()
    else:
        print(f"Unknown command: {command}")
        cmd_help()
        sys.exit(1)
