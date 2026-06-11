# Go MCP Server Development Plugin

Complete toolkit for building Model Context Protocol (MCP) servers in Go using the official github.com/modelcontextprotocol/go-sdk. Includes instructions for best practices, a prompt for generating servers, and an expert chat mode for guidance.

## Installation

```bash
# Using Copilot CLI
copilot plugin install go-mcp-development@awesome-copilot
```

## What's Included

### Commands (Slash Commands)

| Command | Description |
| --- | --- |
| `/go-mcp-development:go-mcp-server-generator` | Generate a complete Go MCP server project with proper structure, dependencies, and implementation using the official github.com/modelcontextprotocol/go-sdk. |

### Agents

| Agent | Description |
| --- | --- |
| `go-mcp-expert` | Expert assistant for building Model Context Protocol (MCP) servers in Go using the official SDK. |


## Hermes Usage

Go MCP server development toolkit. Use when building MCP servers in Go.

These plugins are installed in the Copilot plugins directory and provide slash commands, agents, and skills for GitHub Copilot CLI. They are **not** Hermes-native plugins — they do not provide Hermes tools, hooks, or skills directly.

To use: run `copilot <command>` in a terminal, or invoke via Copilot chat in VS Code.

## Source

This plugin is part of [Awesome Copilot](https://github.com/github/awesome-copilot), a community-driven collection of GitHub Copilot extensions.

## License

MIT
