# MCP Servers — Folder Structure

```
mcp-servers/
├── copilot-studio/       # Copilot Studio MCP integration
├── csharp/               # C# MCP server (.NET)
├── go/                   # Go MCP server
├── java/                 # Java MCP server
├── kotlin/               # Kotlin MCP server
├── php/                  # PHP MCP server
├── python/               # Python MCP server
├── ruby/                 # Ruby MCP server
├── rust/                 # Rust MCP server
├── swift/                # Swift MCP server
├── typescript/           # TypeScript MCP server
├── AGENTS.md             # Agent context
├── architecture.md       # Architecture overview
├── folder-structure.md   # Folder documentation
└── tech-stack.md         # Tech stack documentation
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| Each `language/` | Self-contained MCP server with its own build system |
| `copilot-studio/` | GitHub Copilot Studio MCP integration server |
