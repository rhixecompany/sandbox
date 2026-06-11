# 📦 shadcn-ui-mcp-server — Comprehensive Summary

> **A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to shadcn/ui v4 components, blocks, demos, and metadata. Supports React, Svelte, Vue, and React Native.**

**Repository:** [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server)
**License:** MIT
**Author:** [Janardhan Polle](https://github.com/Jpisnice)
**npm package:** `@jpisnice/shadcn-ui-mcp-server`

---

## ✨ Key Features

- Provides AI assistants with full access to **shadcn/ui v4** components, blocks, demos, and metadata
- Supports **React, Svelte, Vue, and React Native** implementations
- Compatible with **Claude Desktop**, **Claude Code**, and other MCP-compatible tools
- Offers **stdio**, **SSE**, and **dual** transport modes
- Docker-ready with production deployment support
- One-click `.mcpb` installation for Claude Desktop

---

## 🚀 Quick Start

### One-Click Installation (Claude Desktop)

1. Download the `.mcpb` file: `shadcn-ui-mcp-server.mcpb`
2. Double-click to install, or manually navigate:
   `Claude Desktop → Settings → MCP → Add Server → Browse → Select .mcpb file`

### Prerequisites

- **GitHub Personal Access Token** (recommended for higher rate limits)
  - Setup guide: `docs/getting-started/github-token.md`

---

## 🌐 Transport Modes

| Mode | Description |
|------|-------------|
| `stdio` | Standard input/output (default for local tools) |
| `sse` | Server-Sent Events (for multi-client/production) |
| `dual` | Both stdio and SSE simultaneously |

### Key Environment Variables

| Variable | Purpose |
|----------|---------|
| `MCP_TRANSPORT_MODE` | Set transport mode (`stdio`, `sse`, `dual`) |
| `MCP_PORT` | Port for SSE mode |
| `MCP_HOST` | Host binding for SSE mode |
| `MCP_CORS_ORIGINS` | Allowed CORS origins |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | GitHub API token |
| `UI_LIBRARY` | React primitives: `radix` (default) or `base` |

---

## 🎨 Framework Support

| Framework | Repository | Maintainer |
|-----------|------------|------------|
| **React** (default) | [shadcn/ui](https://ui.shadcn.com/) | [shadcn](https://github.com/shadcn) |
| **Svelte** | [shadcn-svelte](https://www.shadcn-svelte.com/) | [huntabyte](https://github.com/huntabyte) |
| **Vue** | [shadcn-vue](https://www.shadcn-vue.com/) | [unovue](https://github.com/unovue) |
| **React Native** | [react-native-reusables](https://github.com/founded-labs/react-native-reusables) | [Founded Labs](https://github.com/founded-labs) |

### React UI Library Options

shadcn/ui v4 supports two primitive libraries:
- **Radix UI** (default)
- **Base UI**

---

## 💻 Claude Code Integration

### Quick Add (CLI)
```bash
claude mcp add shadcn-ui -- npx @jpisnice/shadcn-ui-mcp-server
```

### SSE Transport (Production)
```bash
claude mcp add shadcn-ui-sse --transport sse --url http://localhost:3000/sse
```

📖 See [Claude Code Integration Guide](docs/integration/claude-code.md) for framework-specific commands.

---

## 🔨 Building from Source

### Build Steps
```bash
npm install
npm run build
```

### Run Locally
```bash
npm start
```

### Building MCPB Package
The `.mcpb` file is a ZIP archive containing the server, dependencies, and `manifest.json` following the [MCPB specification](https://github.com/modelcontextprotocol/mcpb).

---

## 📚 Documentation Structure

| Section | Description |
|---------|-------------|
| [Getting Started](docs/getting-started) | Installation, setup, first steps |
| [Configuration](docs/configuration) | Framework selection, tokens, options |
| [Integration](docs/integration) | Editor and tool integrations |
| [Usage](docs/usage) | Examples, tutorials, use cases |
| [Frameworks](docs/frameworks) | Framework-specific docs |
| [Troubleshooting](docs/troubleshooting) | Common issues and solutions |
| [API Reference](docs/api) | Tool reference and technical details |

---

## 🔗 Quick Links

- [shadcn/ui v4](https://ui.shadcn.com/)
- [Anthropic Desktop Extensions](https://www.anthropic.com/engineering/desktop-extensions)
- [Building MCPB](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)
- [Claude Code MCP Docs](https://code.claude.com/docs/en/mcp)
- [MCPB Specification](https://github.com/modelcontextprotocol/mcpb)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
