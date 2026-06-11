# Model Context Protocol (MCP) Servers Repository - Summary

## Overview

This is the official **Model Context Protocol servers** repository maintained by the MCP steering group. It contains reference implementations for MCP servers that demonstrate how to give Large Language Models (LLMs) secure, controlled access to tools and data sources.

> **Important:** For a comprehensive list of MCP servers, browse the [MCP Registry](https://registry.modelcontextprotocol.io/). This repository only contains reference servers maintained by the MCP steering group.

> **Warning:** These servers are **reference implementations** meant as educational examples, not production-ready solutions. Developers should evaluate their own security requirements.

---

## Getting Started

### Running TypeScript Servers
Use `npx` to run TypeScript-based servers directly:
```bash
npx
```
Example: Starting the Memory server

### Running Python Servers
Use `uvx` (recommended) or `pip`:
```bash
uvx
pip
```
Example: Starting the Git server

**Installation:**
- Install `uv`/`uvx`: [Astral docs](https://docs.astral.sh/uv/getting-started/installation/)
- Install `pip`: [pip installation guide](https://pip.pypi.org/en/stable/installation/)

### Configuring MCP Clients
Servers should be configured into an MCP client (e.g., Claude Desktop).

**Windows Configuration:**
- Wrap `npx` commands with `cmd /c`
- Change `"command"` to `"cmd"` and prepend `"/c", "npx"` to `args`
- Leave `uvx` entries unchanged

---

## Repository Structure

### Key Files
| File | Purpose |
|------|---------|
| `README.md` | Main documentation |
| `CONTRIBUTING.md` | Contribution guidelines |
| `SECURITY.md` | Security vulnerability reporting |
| `LICENSE` | Apache 2.0 (new) / MIT (existing) |
| `ADDITIONAL.md` | Frameworks and resources list |
| `CODE_OF_CONDUCT.md` | Community standards |

### Directories
- `src/` - Source code for reference servers
- `.github/` - GitHub configuration
- `scripts/` - Utility scripts

---

## Archived Servers
Previously maintained reference servers have been moved to [servers-archived](https://github.com/modelcontextprotocol/servers-archived).

---

## Creating Your Own MCP Server
Visit [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction) for comprehensive guides, best practices, and technical details.

---

## Community & Support
- **Managed by:** Anthropic
- **License:** Apache 2.0 (new contributions) / MIT (existing code)
- **Contributions:** Encouraged from the community
- **Repository Stats:** 4,108 commits, 24 releases

---

## Key Resources
- **Official Docs:** [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **MCP Registry:** [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/)
- **Archived Servers:** [servers-archived](https://github.com/modelcontextprotocol/servers-archived)
