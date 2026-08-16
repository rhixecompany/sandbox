#!/usr/bin/env python3
"""
Generate SKILL.md files for all 23 MCP servers from the catalog.
Run: python generate-mcp-skills.py
"""

import json
import os
from pathlib import Path

base = Path("/c/Users/Alexa/Desktop/SandBox")
skills_dir = base / ".github" / "skills"
catalog_path = skills_dir / "mcp-servers" / "references" / "mcp-server-catalog.json"

with open(catalog_path) as f:
    catalog = json.load(f)

servers = catalog["mcp_servers"]

print(f"Generating {len(servers)} MCP skills...")

for name, meta in servers.items():
    skill_dir = skills_dir / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # Build description
    desc = meta["description"]
    # Truncate to ~200 chars for the frontmatter (best practice from agent-skills.instructions.md)
    if len(desc) > 200:
        desc = desc[:197] + "..."
    
    # Build keywords list
    keywords = meta.get("keywords", [])
    
    # Build prerequisites
    prereqs = meta.get("prerequisites", [])
    
    # Build gotchas
    gotchas = meta.get("gotchas", [])
    
    # Build troubleshooting table
    # (derived from gotchas — convert warnings to troubleshooting format)
    troubleshooting_rows = []
    for g in gotchas:
        # Try to extract issue and solution from gotcha format
        if "must be" in g or "requires" in g or "need" in g:
            troubleshooting_rows.append(f"| {g.split('—')[0].strip() if '—' in g else g[:60]}... | See prerequisites — ensure required config is set |")
    
    # Build references
    refs = meta.get("references", [])
    ref_lines = []
    for ref in refs:
        ref_lines.append(f"- [{ref}](../../../../Desktop/instructions/{ref})")
    
    # Build workflow steps (generic for all MCP servers)
    transport = meta.get("type", "stdio")
    cmd = meta.get("command", "N/A")
    pkg = meta.get("package", "N/A")
    
    if transport == "http":
        workflow = f"""1. Verify API key/configuration is set in environment
2. The MCP server connects via HTTP — no local installation needed
3. Use via Hermès: tools are available automatically when MCP is enabled
4. Test: `hermes mcp list` shows {name} as enabled"""
    elif transport == "stdio" and cmd == "bunx":
        workflow = f"""1. Install globally: `bunx -y {pkg}`
2. Verify installation: `bunx -y {pkg} --help`
3. The MCP server is configured in Hermès config.yaml and all agent configs
4. Use via Hermès: `hermes mcp list` to verify, then use tools directly
5. If connection fails, run `bunx -y {pkg}` manually to check for errors"""
    elif transport == "stdio" and cmd == "docker":
        workflow = f"""1. Ensure Docker is installed and running
2. Configure MCP gateway profile (adminbot)
3. Start the MCP gateway: `docker mcp gateway run --profile adminbot`
4. Use via Hermès: `hermes mcp list` to verify"""
    elif "python.exe" in cmd:
        workflow = f"""1. Ensure Python 3.11+ Hermes venv is active
2. Verify the script exists at the configured path
3. The MCP server is pre-configured in Hermès
4. Use via Hermès: `hermes mcp list` to verify"""
    elif cmd == "mindstudio":
        workflow = f"""1. Ensure MindStudio is installed at C:\\\\Users\\\\Alexa\\\\.mindstudio\\\\bin\\\\mindstudio.exe
2. The MCP server is pre-configured in Hermès
3. Use via Hermès: `hermes mcp list` to verify"""
    else:
        workflow = f"""1. The MCP server is pre-configured in Hermès
2. Use via Hermès: `hermes mcp list` to verify, then use tools directly"""
    
    # Build gotchas section
    gotchas_md = ""
    if gotchas:
        gotchas_md = "## Gotchas\n\n" + "\n".join(f"- **{g.split(chr(10))[0]}**" if chr(10) in g else f"- {g}" for g in gotchas[:5])
    
    # Build troubleshooting
    troubleshooting_md = f"""## Troubleshooting

| Issue | Solution |
|-------|----------|
| Server not responding | Run `hermes mcp list` to check status; restart Hermès |
| Connection refused | Check that the required package is installed globally |
| 401 Unauthorized | Verify API key is correct and has required scopes |
| Timeout | Network connectivity or rate limiting — retry with delay |"""
    
    # Build related skills
    related = "- [MCP Server Catalog](./references/mcp-server-catalog.json) — full metadata for all servers\n"
    related += "- [MCP Management Tool](../scripts/hermes-mcp-manager.py) — list, test, install MCP servers\n"
    related += "- [MCP Health Check Hook](../hooks/mcp-health-check.sh) — periodic health monitoring\n"
    
    skill_md = f"""---
name: {name}
description: '{desc} Use when you need {name} functionality via the Model Context Protocol.'
license: Complete terms in LICENSE.txt
---

# {name} — MCP Server Skill

## Overview

{meta['description']}

{name} is an MCP server configured in:

- Hermès: `C:\\\\Users\\\\Alexa\\\\AppData\\\\Local\\\\hermes\\\\config.yaml`
- VS Code: `.vscode/mcp.json`
- OpenCode: `opencode.json`
- Codex: `.codex/mcp.json`
- Copilot: `.copilot/mcp.json`

## When to Use This Skill

Use when you need {name} functionality in an AI agent workflow, or when debugging {name} MCP server connectivity issues.

**Keywords:** {', '.join(keywords)}

## Prerequisites

{chr(10).join(f"- {p}" for p in prereqs) if prereqs else "- Hermès or MCP-compatible agent installed and configured"}

## Configuration

**Transport:** {transport}
**Command:** `{cmd}`
**Package:** `{pkg}`
**Enabled:** yes

## Step-by-Step Workflows

{workflow}

{gotchas_md if gotchas_md else ""}

{troubleshooting_md}

## Testing

Run `hermes mcp list` to verify {name} is enabled and configured correctly.

## Related Skills

{related}

## References

{chr(10).join(ref_lines) if ref_lines else "- agent-skills.instructions.md — SKILL.md format best practices"}
"""
    
    skill_path = skill_dir / "SKILL.md"
    with open(skill_path, "w") as f:
        f.write(skill_md)
    
    print(f"  ✓ {name}/SKILL.md ({len(skill_md)} bytes)")

print(f"\nGenerated {len(servers)} MCP skills in {skills_dir}")
print("Next: run `hermes skills audit` to validate, then `hermes skills check`")
