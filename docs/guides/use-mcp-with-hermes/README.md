# Use MCP with Hermes — Comprehensive Guide

> **Source:** [Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
> **Purpose:** Practical guide for using MCP (Model Context Protocol) with Hermes Agent in daily workflows.

---

## 🎯 When to Use MCP

| ✅ **Use MCP When** | ❌ **Don't Use MCP When** |
|---------------------|---------------------------|
| Need to connect to external systems (GitHub, filesystem, APIs, browsers) | Task is purely conversational or self-contained |
| Want bounded, auditable tool access | You need unrestricted, dynamic tool discovery |
| Building multi-system workflows | Simplicity outweighs integration value |

> **Mental Model:** MCP is an **adapter layer** — "connect the right thing, with the smallest useful surface." Not "connect everything."

---

## 📦 Step 1: Install MCP Support

**Standard install** (already includes MCP):
```bash
uv pip install -e ".[all]"
```

**Add MCP to existing install:**
```bash
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]"
```

**Prerequisites:**
- `npx` for npm-based servers
- `uvx` for Python MCP servers (recommended default)

---

## 🚀 Step 2: Add Your First Server

**Start small — one safe server.** Example: filesystem access to a single project.

```yaml
mcp_servers:
  project_fs:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/my-project"]
```

**Start Hermes:**
```bash
hermes chat
```

**Test prompt:**
> `Inspect this project and summarize the repo layout.`

---

## ✅ Step 3: Verify MCP Loaded

| Method | Command |
|--------|---------|
| Reload MCP config | `/reload-mcp` |
| List available tools | `Tell me which MCP-backed tools are available right now.` |

---

## 🔒 Step 4: Filter Tools Immediately

**Don't wait.** Filter aggressively from the start.

### Whitelist (Recommended for Sensitive Systems)
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [list_issues, create_issue, search_code]
```

### Blacklist (For Dangerous Actions)
```yaml
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    headers:
      Authorization: "Bearer ***"
    tools:
      exclude: [delete_customer, refund_payment]
```

### Disable Utility Wrappers
```yaml
mcp_servers:
  docs:
    url: "https://mcp.docs.example.com"
    tools:
      prompts: false
      resources: false
```

---

## 🌉 WSL2: Bridge Hermes (WSL) → Chrome (Windows)

**Use when:** Hermes runs in WSL2, Chrome runs on Windows.

### Setup
```bash
# Add the bridge server
hermes mcp add chrome-devtools-win \
  --command cmd.exe \
  --args "/c npx -y chrome-devtools-mcp@latest --autoConnect --no-usage-statistics"

# Test connection
hermes mcp test chrome-devtools-win

# Reload in Hermes
/reload-mcp
```

### Mental Model
```
Hermes (WSL) → MCP stdio bridge → Windows Chrome
```

### Typical Prompt
> `调用 MCP 工具 mcp_chrome_devtools_win_list_pages，列出当前浏览器标签页。`

### When `/browser connect` Fails
- Use `/browser connect` for **same-environment** setups
- Use MCP bridge for **WSL→Windows** browser access

### Known Pitfalls
| Issue | Solution |
|-------|----------|
| Path mapping (`/mnt/c/Users/...` vs `C:\Users\...`) | Use `chrome-devtools-mcp --autoConnect` |
| UNC paths | Avoid; use local Windows paths |
| WSL root (`/root`) vs home (`/home/...`) | Ensure server runs in correct context |

---

## 🎛️ What Filtering Actually Affects

Two categories of MCP functionality in Hermes:

| Category | Config Keys | Utility Wrappers |
|----------|-------------|------------------|
| **Tools** | `tools.include`, `tools.exclude` | — |
| **Capabilities** | `tools.resources`, `tools.prompts` | `list_resources`, `read_resource`, `list_prompts`, `get_prompt` |

> Wrappers **only appear** if the server actually exposes resources/prompts AND you haven't disabled them.

---

## 📋 Common Patterns

### Pattern 1: Local Project Assistant
```yaml
mcp_servers:
  fs:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/project"]
  git:
    command: "uvx"
    args: ["mcp-server-git", "--repository", "/home/user/project"]
```
**Prompts:**
- `Review the project structure and identify where configuration lives.`
- `Check the local git state and summarize what changed recently.`

### Pattern 2: GitHub Triage Assistant
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
    prompts: false
    resources: false
```
**Prompts:**
- `List open issues about MCP, cluster them by theme, and draft a high-quality issue for the most common bug.`
- `Search the repo for uses of _discover_and_register_server and explain how MCP tools are registered.`

### Pattern 3: Internal API Assistant
```yaml
mcp_servers:
  internal_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ${INTERNAL_API_TOKEN}"
    tools:
      include: [query_db, call_service]
```

---

## 🔄 Reloading & Debugging

| Action | Command |
|--------|---------|
| Reload MCP config | `/reload-mcp` |
| Test specific server | `hermes mcp test <name>` |
| View server logs | Check `~/.hermes/logs/mcp/` |
| Probe available tools | `hermes mcp configure <name>` (shows checklist) |

---

## 📚 Related Documentation

- [MCP Feature Overview](/docs/user-guide/features/mcp)
- [OAuth over SSH / Remote Hosts](/docs/guides/oauth-over-ssh#mcp-servers)
- [MCP Server Catalog](https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps)

---

**Source:** [Hermes Agent Docs - Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)  
**Extracted:** 2026-06-08