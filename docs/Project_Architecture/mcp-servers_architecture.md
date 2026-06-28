# MCP Servers — Architecture

## Overview
Multi-language Model Context Protocol (MCP) server implementations. Each subdirectory contains a complete, buildable MCP server demonstrating the protocol in a different programming language.

## Architecture Pattern
- **Type:** Multi-language Protocol Implementations
- **Pattern:** Independent per-language servers, each self-contained
- **Protocol:** Model Context Protocol (MCP) — standardized server/client communication

## Components
- **typescript/** — TypeScript MCP server (Node.js)
- **python/** — Python MCP server
- **go/** — Go MCP server
- **rust/** — Rust MCP server
- **java/** — Java MCP server
- **kotlin/** — Kotlin MCP server
- **php/** — PHP MCP server
- **ruby/** — Ruby MCP server
- **swift/** — Swift MCP server
- **csharp/** — C# MCP server
- **copilot-studio/** — Copilot Studio integration server

## Cross-Cutting Concerns
- All servers implement the same MCP protocol specification
- Each language directory is fully self-contained with its own build system
- Shared documentation at `AGENTS.md`, `architecture.md`, `folder-structure.md`, `tech-stack.md`

## Data Flow
1. Client connects via stdin/HTTP transport
2. Server processes JSON-RPC protocol messages
3. Server registers tools, resources, and prompts
4. Responses returned via same transport
