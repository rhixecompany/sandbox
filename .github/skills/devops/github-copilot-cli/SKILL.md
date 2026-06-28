---
name: github-copilot-cli
title: "GitHub Copilot CLI"
description: "Guide for GitHub Copilot CLI — interactive AI coding assistant with MCP server mode (ACP), permission system, and instruction initialization."
version: 1.0.0
author: "Hermes Assistant"
tags: [copilot, ai, cli, github]
---

# GitHub Copilot CLI

## When to Use
- Interactive AI coding assistance (`copilot` without flags)
- One-shot prompts (`copilot --prompt <text>`)
- Running as an MCP/ACP server (`copilot --acp`)
- Initializing repo instructions (`copilot init`)
- Creating `.github/copilot-instructions.md` for project guidance

## Key Commands

### Interactive Mode
```bash
copilot                           # Start interactive session
copilot explain "how does this work"
copilot "fix the bug in main.py"
copilot -p "write a unit test for Calculator"   # One-shot prompt
```

### Code Understanding
```bash
copilot explain ./src/main.py     # Explain a file
copilot explain "the authentication flow"
copilot review                    # Review current changes
```

### MCP/ACP Server Mode
```bash
copilot --acp                     # Start as Agent Client Protocol server
copilot --additional-mcp-config <json>  # Add MCP servers
```

### Permissions
```bash
copilot --allow-dir ~/workspace   # Allow directory access
copilot --allow-all-paths         # Disable path verification
copilot --allow-tool='shell(git:*)'  # Allow specific tools
copilot --allow-tool='write'      # Allow file editing
copilot --allow-all-urls          # Allow all URL access
```

### Repository Setup
```bash
copilot init                      # Generate .github/copilot-instructions.md
```

### Options
```bash
--model <model>                   # Override model (e.g., claude-sonnet-4)
--add-dir <dir>                   # Add allowed directory
--add-github-mcp-tool <tool>      # Enable GitHub MCP tool
```

## Pitfalls
- Interactive mode requires a TTY — use `-p` for scripting
- `--acp` mode listens on stdin/stdout for MCP protocol
- Permissions are strict by default — `--allow-tool='*'` for unrestricted access
- `copilot init` only generates instructions, doesn't commit them
- The ACP mode is what Hermes uses to delegate to Copilot

## Verification
```bash
copilot --help
copilot init
```
