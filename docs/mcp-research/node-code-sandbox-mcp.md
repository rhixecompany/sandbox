# Node.js Sandbox MCP Server

**Source:** https://github.com/alfonsograziano/node-code-sandbox-mcp

## Overview

**Repository:** `alfonsograziano/node-code-sandbox-mcp`
**Description:** A Node.js–based Model Context Protocol (MCP) server that spins up disposable Docker containers to execute arbitrary JavaScript with on-the-fly npm dependency installation.

**Key Links:**
- 🌐 [Official Website](https://jsdevai.com/)
- 📦 [Docker Hub](https://hub.docker.com/r/mcp/node-code-sandbox)
- 📖 [Use Cases](https://jsdevai.com/#use-cases)

## Core Features

- **Ephemeral Docker containers** - Disposable execution environments
- **On-the-fly npm dependency installation** - Install packages dynamically
- **Controlled resource limits** - CPU/memory constraints on containers
- **File I/O support** - Save/return files from container execution
- **Multiple execution modes** - One-off scripts or persistent sandboxes
- **npm package search** - Built-in package discovery

## Prerequisites

> **Docker must be installed and running** on your machine.

**Pro Tip:** Pre-pull Docker images to avoid first-execution delays:
```bash
docker pull node:lts-slim
```

## Getting Started

### Quick Test Prompts

1. **Validate basic execution:** Run `console.log("Hello World")` → should return "Hello World"
2. **Validate dependencies + file I/O:** Create a QR code → saves `qrcode.png` to mounted directory

## Configuration

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "node-code-sandbox": {
      "command": "npx",
      "args": ["-y", "node-code-sandbox-mcp"],
      "env": {
        "FILES_DIR": "/absolute/path/to/output/directory"
      }
    }
  }
}
```

### Docker Deployment

```bash
docker run -d \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /host/output/path:/host/output/path \
  -e FILES_DIR=/host/output/path \
  mcp/node-code-sandbox
```

> **Note:** Bind-mounts host folder at **same absolute path** inside container.

### VS Code

**Quick Install:** [NPX Version](vscode:mcp/install?serverName=js-sandbox-mcp&type=npx) | [Docker Version](vscode:mcp/install?serverName=js-sandbox-mcp&type=docker)

**Manual (`settings.json` or `.vscode/mcp.json`):**
```json
{
  "mcp": {
    "servers": {
      "node-code-sandbox": {
        "command": "npx",
        "args": ["-y", "node-code-sandbox-mcp"],
        "env": { "FILES_DIR": "${workspaceFolder}/output" }
      }
    }
  }
}
```

## API Tools Reference

### 1. `run_js_ephemeral` — One-off Execution

Run a script in a brand-new disposable container.

**Inputs:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image` | string | `node:lts-slim` | Docker image to use |
| `code` | string | *required* | JavaScript code to execute |
| `dependencies` | array | `[]` | npm packages: `{ name, version }` |

**Behavior:**
- Creates `index.js` + `package.json` in container
- Runs `npm install --omit=dev --ignore-scripts --no-audit --loglevel=error`
- Executes `node index.js`
- Returns stdout + any saved files

**Example:**
```javascript
// Save a file during execution
const fs = require('fs');
fs.writeFileSync('hello.txt', 'Hello from sandbox!');
console.log('File saved!');
```
→ Returns console output **and** `hello.txt` file

### 2. `sandbox_initialize` — Persistent Sandbox

Start a fresh sandbox container for multiple operations.

**Inputs:**

| Parameter | Type | Default |
|-----------|------|---------|
| `image` | string | `node:lts-slim` |
| `port` | number | *optional* | Expose port for servers |

**Output:** `container_id` for subsequent calls

### 3. `run_js` — Execute in Persistent Sandbox

Run code inside an existing sandbox container.

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `container_id` | string | From `sandbox_initialize` |
| `code` | string | JavaScript to execute |
| `dependencies` | array | npm packages to install |
| `listenOnPort` | number | *optional* | Keep container running for server |

**Behavior:** Same npm install + execution as ephemeral, but in persistent container

### 4. `sandbox_exec` — Shell Commands

Run arbitrary shell commands in the sandbox.

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `container_id` | string | From `sandbox_initialize` |
| `commands` | string[] | Shell commands to execute |

### 5. `sandbox_stop` — Cleanup

Terminate and remove sandbox container.

**Input:** `container_id` (from `sandbox_initialize`)

### 6. `search_npm_packages` — Package Discovery

Search npm registry.

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchTerm` | string | *required* | Search query |
| `qualifiers` | object | Advanced: `author`, `maintainer`, `scope`, `keywords`, `not`, `is`, `boostExact` |

**Output:** JSON array with `name`, `description`, `readme` snippet

## Usage Patterns

| Workflow | Tools | Best For |
|----------|-------|----------|
| Quick code snippet | `run_js_ephemeral` | One-off calculations, tests |
| Multi-step coding | `sandbox_initialize` → `run_js` × N → `sandbox_stop` | Building, iterative development |
| Server hosting | `sandbox_initialize` with port → `run_js` (long-running) | Web servers, APIs |
| Package discovery | `search_npm_packages` | Finding dependencies |
| System commands | `sandbox_exec` | Native binaries, `git`, `curl`, etc. |

## Docker Hub Image

```bash
docker pull mcp/node-code-sandbox
```

## Hermes Integration

For Hermes Agent (NPX mode):

```yaml
mcp_servers:
  node-code-sandbox:
    command: "npx"
    args: ["-y", "node-code-sandbox-mcp"]
    env:
      FILES_DIR: "C:/Users/Alexa/Desktop/SandBox/sandbox-output"
    tools:
      include: [run_js_ephemeral, sandbox_initialize, run_js, sandbox_exec, sandbox_stop, search_npm_packages]
```

For Docker mode:

```yaml
mcp_servers:
  node-code-sandbox:
    command: "docker"
    args: ["run", "-i", "--rm",
      "-v", "/var/run/docker.sock:/var/run/docker.sock",
      "-v", "C:/Users/Alexa/Desktop/SandBox/sandbox-output:/host/output/path",
      "-e", "FILES_DIR=/host/output/path",
      "mcp/node-code-sandbox"]
    tools:
      include: [run_js_ephemeral, sandbox_initialize, run_js, sandbox_exec, sandbox_stop, search_npm_packages]
```

Then run:
```bash
hermes mcp test node-code-sandbox
/reload-mcp
```

## References

- GitHub: https://github.com/alfonsograziano/node-code-sandbox-mcp
- Docker Hub: https://hub.docker.com/r/mcp/node-code-sandbox
- Official Site: https://jsdevai.com/
- Glama: https://glama.ai/mcp/servers/ssdeanx/node-code-sandbox-mcp/tools