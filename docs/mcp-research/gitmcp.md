# GitMCP (git-mcp)

**Source:** https://github.com/idosal/git-mcp

## Overview

**Tagline:** "Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project"

## What Is GitMCP?

GitMCP transforms **any GitHub repository or GitHub Pages site** into a documentation hub accessible via the **Model Context Protocol (MCP)**. It enables AI assistants (Cursor, Claude, Windsurf, VSCode, Cline, Highlight AI, Augment Code, Msty) to fetch up-to-date docs and code—eliminating hallucinations when the LLM hasn't seen the project.

**Core value:** AI gets *actual* project documentation/code on demand, not stale training data.

## Supported URL Formats (Two Flavors)

| Format | Use Case |
|--------|----------|
| `https://gitmcp.io/{owner}/{repo}` | Standard GitHub repo |
| `https://{owner}.gitmcp.io/{repo}` | GitHub Pages sites (e.g., `langchain-ai.gitmcp.io/langgraph`) |
| `https://gitmcp.io/docs` | **Dynamic endpoint** — AI picks any repo on the fly |

**Example:** `https://gitmcp.io/microsoft/typescript` or `https://microsoft.gitmcp.io/typescript`

## Quick Start — Connect Your AI Assistant

### 1. Pick Your URL Format

Replace `{owner}` and `{repo}` with actual values.

### 2. Add to Your AI Tool's Config

#### **Cursor** (`~/.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

#### **Windsurf** (`~/.codeium/windsurf/mcp_config.json`)

```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

#### **VSCode** (`.vscode/mcp.json`)

```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

#### **Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS)

```json
{
  "mcpServers": {
    "gitmcp": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://gitmcp.io/{owner}/{repo}"]
    }
  }
}
```

#### **Cline** (`~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`)

```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

#### **Highlight AI**

- Plugin name: `gitmcp`
- SSE URL: `https://gitmcp.io/{owner}/{repo}`

#### **Augment Code**

- Server name: `git-mcp Docs`
- Command: `npx -y mcp-remote https://gitmcp.io/{owner}/{repo}`

#### **Msty AI**

See [Augment Code docs](https://docs.augmentcode.com/setup-augment/mcp) for MCP config.

## How It Works

1. **AI requests context** via MCP
2. **GitMCP fetches** from GitHub (prioritizing `llms.txt`, then `README.md`, other docs)
3. **Returns structured data** to AI
4. **AI answers** with accurate, current info

**Flow example:** `gitmcp.io/microsoft/typescript` → fetches TypeScript repo docs → AI uses them

## Tools Provided to AI

| Tool | Purpose | When Useful |
|------|---------|-------------|
| `fetch_<repo>_documentation` | Gets primary docs (`llms.txt` preferred) | General project questions, getting started |
| `search_<repo>_documentation` | Searches docs with a query | Specific feature/function questions |
| `fetch_url_content` | Retrieves linked external content | Docs reference external resources |
| `search_<repo>_code` | Searches actual code via GitHub Code Search | Implementation details, code examples |

> **Dynamic endpoint (`gitmcp.io/docs`)** uses generic names: `fetch_generic_documentation`, `search_generic_code`, `search_generic_documentation` — requires repo info in the call.

## Supported Documentation (Priority Order)

1. `llms.txt` (if present)
2. `README.md`
3. Other documentation pages
4. Future: dynamic generation, more formats

## Usage Examples

### Example 1: Windsurf + Playwright MCP

```
Repo: https://github.com/microsoft/playwright-mcp
MCP URL: https://gitmcp.io/microsoft/playwright-mcp
Prompt: "How do I use the Playwright MCP"
```
→ Windsurf pulls docs via GitMCP → correct implementation

### Example 2: Cursor + LangGraph (GitHub Pages)

```
Site: langchain-ai.github.io/langgraph
MCP URL: https://langchain-ai.gitmcp.io/langgraph
Prompt: "Add memory to my LangGraph agent"
```
→ Cursor fetches GitHub Pages docs → accurate code

### Example 3: Claude Desktop + Dynamic Endpoint

```
MCP URL: https://gitmcp.io/docs
Prompt: "I want to learn about the OpenAI Whisper speech recognition model. Explain how it works."
```
→ Claude picks repo on the fly → answers from live docs

## Repository Badge

Add to your `README.md` to show GitMCP access + view count:

```markdown
[![GitMCP](https://gitmcp.io/badge/OWNER/REPO)](https://gitmcp.io/OWNER/REPO)
```

**Customization:**

| Param | Default | Example |
|-------|---------|---------|
| `color` | `aquamarine` | `?color=green` |
| `label` | `GitMCP` | `?label=Documentation` |

**View count:** Increments per tool call on that repo.

## Hermes Integration

For Hermes Agent (remote HTTP mode):

```yaml
mcp_servers:
  gitmcp:
    url: "https://gitmcp.io/{owner}/{repo}"
    transport: "streamable-http"
    tools:
      include: [fetch_documentation, search_documentation, fetch_url_content, search_code]
```

For dynamic endpoint:
```yaml
mcp_servers:
  gitmcp-dynamic:
    url: "https://gitmcp.io/docs"
    transport: "streamable-http"
    tools:
      include: [fetch_generic_documentation, search_generic_code, search_generic_documentation]
```

Then run:
```bash
hermes mcp test gitmcp
/reload-mcp
```

## References

- GitHub: https://github.com/idosal/git-mcp
- GitMCP Service: https://gitmcp.io
- mcpservers.org: https://mcpservers.org/servers/DanyelKirsch/git-mcp-server
- Augment Code: https://www.augmentcode.com/mcp/git-mcp