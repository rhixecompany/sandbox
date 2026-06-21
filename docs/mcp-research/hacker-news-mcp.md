# Hacker News MCP Server (mcp-hn)

**Source:** <https://github.com/erithwik/mcp-hn>

## Repository Overview

| Property        | Details                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **Repository**  | `erithwik/mcp-hn`                                                                                   |
| **Description** | A Model Context Protocol (MCP) server that provides tools for fetching information from Hacker News |
| **Commits**     | 15                                                                                                  |
| **License**     | See [LICENSE](https://github.com/erithwik/mcp-hn/blob/main/LICENSE)                                 |
| **Badges**      | [Smithery](https://smithery.ai/server/mcp-hn) • [Glama](https://glama.ai/mcp/servers/e0rco8dfgt)    |

## Available Tools

| Tool             | Purpose                                                              |
| ---------------- | -------------------------------------------------------------------- |
| `get_stories`    | Fetch top/current stories from Hacker News                           |
| `get_story_info` | Get detailed information about a specific story (including comments) |
| `search_stories` | Search Hacker News for stories matching a query                      |
| `get_user_info`  | Retrieve user profile and activity information                       |

## Repository Structure

```
mcp-hn/
├── src/mcp_hn/          # Main source code
├── .gitignore
├── Dockerfile           # Container configuration
├── LICENSE
├── README.md
├── pyproject.toml       # Python project configuration
├── smithery.yaml        # Smithery deployment config
└── uv.lock              # UV package lock file
```

## Quickstart: Installation via Smithery

### For Claude Desktop

**Configuration file locations:**

| OS          | Path                                                              |
| ----------- | ----------------------------------------------------------------- |
| **macOS**   | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%/Claude/claude_desktop_config.json`                     |

**Production configuration:**

```json
{
	"mcpServers": {
		"mcp-hn": {
			"command": "npx",
			"args": [
				"-y",
				"@smithery/cli@latest",
				"run",
				"mcp-hn",
				"--key",
				"YOUR_SMITHERY_API_KEY"
			]
		}
	}
}
```

> **Note:** Replace `YOUR_SMITHERY_API_KEY` with your actual Smithery API key from [smithery.ai/server/mcp-hn](https://smithery.ai/server/mcp-hn)

## Example Usage Patterns

### Basic Interactions

```
User: Get the top stories of today
Output: Uses `get_stories` tool and returns a story about AI

User: What does the details of the story today that talks about the future of AI
Output: Uses `get_story_info` tool based on the results of the previous tool

User: What has the user `pg` been up to?
Output: Uses `get_user_info` tool and returns a summary of the user's activity

User: What does hackernews say about careers in AI?
Output: Uses `search_stories` tool and returns a summary of the comments
```

### Advanced: Combined with Puppeteer MCP Server

```
User: What are the top stories of today?
Output: Uses `get_stories` tool and returns a story about AI

User: Can you use the puppeteer tool to read the article about <AI> and also use the hackernews tool to view the comments and give me a summary of what the main comments are about the article?
Output: Uses puppeteer tool to read the article about AI and then uses the `get_story_info` hn tool to get the comments and returns a summary of the comments
```

## Technical Details

- **Protocol:** Model Context Protocol (MCP)
- **Language:** Python (indicated by `pyproject.toml` and `uv.lock`)
- **Deployment:** Docker support via `Dockerfile`
- **Package Manager:** UV (modern Python package manager)
- **Distribution:** Available via Smithery for easy Claude Desktop integration

## Alternative Implementation: paabloLC/mcp-hacker-news

**Source:** <https://github.com/paabloLC/mcp-hacker-news>

TypeScript implementation with similar features:

- Integrates with the official Hacker News API
- Built with TypeScript
- Compatible with Claude and Cursor

## Hermes Integration

For Hermes Agent (Smithery mode):

```yaml
mcp_servers:
  mcp-hn:
    command: "npx"
    args:
      [
        "-y",
        "@smithery/cli@latest",
        "run",
        "mcp-hn",
        "--key",
        "${SMITHERY_API_KEY}",
      ]
    env:
      SMITHERY_API_KEY: "${SMITHERY_API_KEY}"
    tools:
      include: [get_stories, get_story_info, search_stories, get_user_info]
```

For Docker mode:

```yaml
mcp_servers:
  mcp-hn:
    command: "docker"
    args: ["run", "-i", "--rm", "erithwik/mcp-hn:latest"]
    tools:
      include: [get_stories, get_story_info, search_stories, get_user_info]
```

Then run:

```bash
hermes mcp test mcp-hn
/reload-mcp
```

## Key Resources

- **Smithery Page:** <https://smithery.ai/server/mcp-hn>
- **Glama Listing:** <https://glama.ai/mcp/servers/e0rco8dfgt>
- **Repository:** <https://github.com/erithwik/mcp-hn>
- **MCP Specification:** <https://modelcontextprotocol.io/>

## Summary

**mcp-hn** is a production-ready MCP server that bridges Hacker News data with AI assistants (particularly Claude Desktop). It provides four core tools for story retrieval, story details, search, and user info — enabling natural language queries like "top stories today" or "what's user pg up to?" The server installs cleanly via Smithery with a one-line config update, supports Docker deployment, and can be combined with other MCP servers (e.g., Puppeteer) for richer workflows like "read the article + summarize HN comments."

**mcp-hn** is a production-ready MCP server that bridges Hacker News data with AI assistants (particularly Claude Desktop). It provides four core tools for story retrieval, story details, search, and user info — enabling natural language queries like "top stories today" or "what's user pg up to?" The server installs cleanly via Smithery with a one-line config update, supports Docker deployment, and can be combined with other MCP servers (e.g., Puppeteer) for richer workflows like "read the article + summarize HN comments."
