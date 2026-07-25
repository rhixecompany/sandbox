# GitHub Copilot SDK — Reference Overview

## Key Concepts

- **GitHub Copilot SDK** is a multi-language SDK (TypeScript, Python, Go, .NET) that exposes the same agent engine behind Copilot CLI as a programmable API. It enables embedding AI agents in applications with session management, streaming, custom tools, MCP server integration, and custom agent personas.
- **Architecture** — Applications use the SDK Client which communicates with the Copilot CLI (running in server mode) via JSON-RPC over stdio or TCP. The CLI handles auth, model selection, tool orchestration, and planning. The SDK manages CLI process lifecycle automatically (auto-start, auto-restart).
- **Custom Tools** — Tools are user-defined functions that Copilot can invoke during reasoning. Defined with `defineTool` (TypeScript) or `define_tool` (Python), each tool has a description, parameter schema (JSON Schema or Pydantic), and handler function. Copilot decides when to call tools based on user intent.
- **Streaming & Events** — The SDK supports streaming responses via event handlers. Events include `assistant.message_delta` (incremental response), `tool.execution_start/complete`, `session.error`, and `session.idle`. Streaming is recommended for better UX on long responses.
- **Session Persistence** — Sessions can be created with custom IDs, resumed across restarts, listed, and deleted. This enables multi-turn conversations that survive process restarts.
- **MCP Integration** — The SDK supports connecting to MCP servers for pre-built tools (e.g., GitHub MCP server for repo/issue/PR access). MCP servers are configured in the session configuration via `mcpServers`.
- **Status** — The SDK is in Technical Preview and may have breaking changes. Not recommended for production use yet.