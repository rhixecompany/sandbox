# NPM Sentinel MCP Server

**Source:** https://github.com/Nekzus/npm-sentinel-mcp

## Project Overview

**NPM Sentinel MCP** is a powerful **Model Context Protocol (MCP) server** that revolutionizes NPM package analysis through AI integration. Built to work with **Claude and Anthropic AI**, it provides real-time intelligence on package security, dependencies, and performance.

> **Core Value Proposition:** "Delivers instant insights and smart analysis to safeguard and optimize your npm ecosystem, making package management decisions faster and safer for modern development workflows."

### Key Stats & Badges

- **363 Commits** | **134 Releases**
- **Package:** `@nekzus/mcp-server` on npm
- **Docker:** `mcp/npm-sentinel` on Docker Hub
- **Deployable via:** Smithery.ai (HTTP Streamable)
- **License:** MIT © [nekzus](https://github.com/nekzus)

## Features

- **AI-assisted analysis** through MCP integration
- **Real-time package intelligence** (security, deps, performance)
- **Multi-transport support:** STDIO + HTTP Streamable
- **Robust caching** with invalidation strategies
- **Lockfile-aware analysis** (pnpm, npm, yarn)
- **13+ specialized analysis tools** (see API section)

## Installation Methods

### 1. VS Code (One-Click)

```bash
# VS Code Stable
vscode:mcp/install?{"name":"npm-sentinel","config":{"command":"npx","args":["-y","@nekzus/mcp-server@latest"]}}

# VS Code Insiders
vscode-insiders:mcp/install?{"name":"npm-sentinel","config":{"command":"npx","args":["-y","@nekzus/mcp-server@latest"]}}
```

[VS Code MCP Docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

### 2. Smithery.ai (HTTP Streamable)

```yaml
# smithery.yaml configuration
# Deploy directly on Smithery.ai for enhanced scalability
```

**Benefits:** Horizontal scaling, better performance, managed infrastructure

### 3. Docker

```bash
# Build
docker build -t npm-sentinel .

# Run with directory mounting (must be under /projects)
docker run -v /path/to/project:/projects npm-sentinel

# Multiple directories
docker run -v /path1:/projects/project1 -v /path2:/projects/project2 npm-sentinel
```

### 4. NPX (Quick Start)

```bash
npx -y @nekzus/mcp-server@latest
```

### 5. Claude Desktop

Add to `claude_desktop_config.json`:

**Locations:**
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "npm-sentinel": {
      "command": "npx",
      "args": ["-y", "@nekzus/mcp-server@latest"]
    }
  }
}
```

## Configuration

| Environment Variable | CLI Argument | Default | Description |
|---------------------|--------------|---------|-------------|
| `NPM_REGISTRY_URL` | `config.NPM_REGISTRY_URL` | `https://registry.npmjs.org` | NPM registry URL for all requests |

### HTTP Deployment (Smithery/Docker)

Configure via configuration file with the above options.

## Caching & Invalidation

The server implements **robust caching strategies** for performance with data accuracy.

### Supported Lockfiles (Auto-detected)

- `pnpm-lock.yaml`
- `package-lock.json`
- `yarn.lock`

### Cache Invalidation

```json
// Include in tool arguments to bypass cache
{
  "ignoreCache": true
}
```

## API - Available Tools (18+ Tools)

All tools follow standardized MCP response format. Accessible via JSON-RPC.

### Package Analysis Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `npmVersions` | `packages: string[]` | Get all published versions |
| `npmLatest` | `packages: string[]` | Get latest version info |
| `npmDeps` | `packages: string[]` | Analyze dependencies |
| `npmTypes` | `packages: string[]` | TypeScript definitions info |
| `npmSize` | `packages: string[]` | Package size analysis |
| `npmVulnerabilities` | `packages: string[]` | Security vulnerabilities (via deps.dev) |
| `npmTrends` | `packages: string[], period: string` | Download trends over time |
| `npmCompare` | `packages: string[]` | Compare multiple packages |
| `npmMaintainers` | `packages: string[]` | Maintainer information |
| `npmScore` | `packages: string[]` | Quality/security/maintenance scores |
| `npmPackageReadme` | `packages: string[]` | Fetch README content |
| `npmSearch` | `query: string, limit: number` | Search NPM registry |
| `npmLicenseCompatibility` | `packages: string[]` | License compatibility analysis |
| `npmRepoStats` | `packages: string[]` | GitHub repository statistics |
| `npmDeprecated` | `packages: string[]` | Check deprecation status |
| `npmChangelogAnalysis` | `packages: string[]` | Analyze changelog patterns |
| `npmAlternatives` | `packages: string[]` | Find alternative packages |
| `npmQuality` | `packages: string[]` | Code quality metrics |
| `npmMaintenance` | `packages: string[]` | Maintenance health indicators |

## Resources

### Registry Resources

| URI | Description |
|-----|-------------|
| `npm://registry` | NPM registry data |
| `npm://security` | Security advisories |
| `npm://metrics` | Package metrics |

## Hermes Integration

For Hermes Agent (NPX mode):

```yaml
mcp_servers:
  npm-sentinel:
    command: "npx"
    args: ["-y", "@nekzus/mcp-server@latest"]
    tools:
      include: [npmVersions, npmLatest, npmDeps, npmTypes, npmSize, npmVulnerabilities, npmTrends, npmCompare, npmScore, npmSearch, npmLicenseCompatibility, npmAlternatives, npmQuality, npmMaintenance]
```

For Docker mode:

```yaml
mcp_servers:
  npm-sentinel:
    command: "docker"
    args: ["run", "-i", "--rm", "-v", "C:/Users/Alexa/Desktop/SandBox:/projects", "mcp/npm-sentinel"]
    tools:
      include: [npmVersions, npmLatest, npmDeps, npmVulnerabilities, npmScore, npmSearch, npmAlternatives]
```

Then run:
```bash
hermes mcp test npm-sentinel
/reload-mcp
```

## References

- GitHub: https://github.com/Nekzus/npm-sentinel-mcp
- npm: https://www.npmjs.com/package/@nekzus/mcp-server
- Docker Hub: mcp/npm-sentinel
- mcpservers.org: https://mcpservers.org/servers/Nekzus/npm-sentinel-mcp
- Smithery.ai: https://smithery.ai
- mcp.aibase.com: https://mcp.aibase.com/server/1916343683613696002