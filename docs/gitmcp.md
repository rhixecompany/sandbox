# GitMCP

**Source:** https://github.com/idosal/git-mcp

## 🧠 What is GitMCP?

**GitMCP** is a **free, open-source, remote Model Context Protocol (MCP) server** that transforms **any GitHub project** (repositories or GitHub Pages) into a documentation hub. It enables AI coding assistants (like Cursor, Claude Desktop, Windsurf, etc.) to access **up-to-date documentation and code**, eliminating **code hallucinations**—a common issue where LLMs generate plausible but incorrect code due to lack of real-world context.

> "Stop vibe-hallucinating and start vibe-coding!"

### Key Benefits:
- Prevents AI from fabricating APIs, functions, or usage patterns.
- Provides real-time access to project docs and source code.
- Works with **any public GitHub repo**—no setup required on the repo side.

---

## 🔗 URL Formats (Endpoints)

GitMCP supports three endpoint formats:

| Format | Use Case |
|-------|--------|
| `gitmcp.io/{owner}/{repo}` | Standard format for any repo |
| `{owner}.gitmcp.io/{repo}` | Custom subdomain-style (e.g., for GitHub Pages) |
| `gitmcp.io/docs` | **Dynamic endpoint**: lets AI choose any repo on-the-fly |

Replace `{owner}` with GitHub username/org and `{repo}` with repository name.

---

## ✨ Features

- **Eliminates code hallucinations** by grounding AI responses in real project data.
- **No authentication required**—fully public and privacy-respecting.
- **Supports all major AI coding tools** via MCP.
- **Prioritizes `llms.txt`** (a proposed standard for machine-readable docs), falls back to `README.md` or other pages.
- **Respects `robots.txt`** for GitHub Pages sites.
- **Open-source and self-hostable**.

---

## 🚀 Getting Started

### Step 1: Choose Your Endpoint
Use one of the URL formats above based on your target repo or dynamic needs.

💡 **Tip**: Use the [GitMCP landing page converter](https://gitmcp.io) to auto-format GitHub URLs into MCP endpoints.

### Step 2: Connect Your AI Assistant

#### Configuration Examples:

**Cursor** (`~/.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

**Windsurf** (`~/.codeium/windsurf/mcp_config.json`)
```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

**VSCode** (`.vscode/mcp.json`)
```json
{
  "mcpServers": {
    "gitmcp": {
      "url": "https://gitmcp.io/{owner}/{repo}"
    }
  }
}
```

**Claude Desktop**
Add via UI or config—supports SSE-based MCP servers.

**Cline**
Settings path:
`~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

**Highlight AI**
- Plugin name: `gitmcp`
- SSE URL: `https://gitmcp.io/{owner}/{repo}`

**Augment Code**
- Name: `git-mcp Docs`
- Use command or config as per [Augment docs](https://docs.augmentcode.com/setup-augment/mcp)

> ✅ **Note**: Replace `{owner}` and `{repo}` with actual values. Use `https://gitmcp.io/docs` for dynamic repo access.

---

## ⚙️ How It Works

GitMCP acts as a bridge between your AI assistant and GitHub repos using the **Model Context Protocol (MCP)**:

1. AI sends a request (e.g., "How does X work in repo Y?").
2. GitMCP fetches relevant documentation (`llms.txt`, `README.md`, etc.) or code.
3. Content is returned in structured format for the AI to use as context.
4. AI generates accurate, grounded responses—**no hallucinations**.

### Supported Documentation (Priority Order):
1. `llms.txt` (ideal for machines)
2. `README.md`
3. Other HTML/Markdown pages (for GitHub Pages)

---

## 🛠️ Tools Provided by GitMCP

When connected, AI assistants gain access to these tools:

| Tool | Purpose |
|------|--------|
| `fetch_<repo-name>_documentation` | Retrieves primary docs (e.g., `llms.txt`) for project overview |
| `search_<repo-name>_documentation` | Searches docs for specific queries (efficient for large projects) |
| `fetch_url_content` | Fetches content from links referenced in docs |
| `search_<repo-name>_code` | Searches actual source code via GitHub code search |

> 🔁 **Dynamic endpoint note**: When using `gitmcp.io/docs`, tools are named:
> - `fetch_generic_documentation`
> - `search_generic_documentation`
> - `search_generic_code`
> These require specifying the target repo at runtime.

---

## 💡 Usage Examples

### Example 1: Windsurf + Playwright MCP
- **Repo**: `https://github.com/microsoft/playwright-mcp`
- **MCP URL**: `https://gitmcp.io/microsoft/playwright-mcp`
- **Prompt**: *"How do I use the Playwright MCP?"*
- ✅ Windsurf pulls real docs to answer accurately.

### Example 2: Cursor + LangGraph (GitHub Pages)
- **Site**: `langchain-ai.github.io/langgraph`
- **MCP URL**: `https://langchain-ai.gitmcp.io/langgraph`
- **Prompt**: *"Add memory to my LangGraph agent"*
- ✅ Cursor uses actual implementation details from the docs.

### Example 3: Dynamic Access with Claude
- **Endpoint**: `https://gitmcp.io/docs`
- **Prompt**: *"Explain how OpenAI Whisper works."*
- ✅ Claude discovers and pulls Whisper repo docs
