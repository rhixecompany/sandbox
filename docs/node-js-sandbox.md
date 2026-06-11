# Node.js Sandbox MCP Server

**Source:** https://github.com/alfonsograziano/node-code-sandbox-mcp

> **Repository**: [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp)
> **Purpose**: A Node.js–based Model Context Protocol (MCP) server that executes arbitrary JavaScript in ephemeral Docker containers with on-the-fly npm dependency installation.
> **License**: MIT
> **Docker Hub**: [mcp/node-code-sandbox](https://hub.docker.com/r/mcp/node-code-sandbox)
> **Official Website**: [jsdevai.com](https://jsdevai.com/)

---

## 🔧 Key Features

- Runs **arbitrary JavaScript** in **disposable Docker containers**
- Supports **on-the-fly npm dependency installation**
- Containers run with **controlled CPU/memory limits**
- Enables **file persistence** via mounted host directories
- Integrates with **Claude Desktop**, **VS Code**, and other MCP-compatible clients

---

## ⚠️ Prerequisites

- **Docker must be installed and running**
- Pre-pull recommended Docker images to avoid first-run delays

---

## 🚀 Getting Started

### 1. Connect to an MCP Client (e.g., Claude Desktop)

#### Option A: Using `npx`
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "node-code-sandbox": {
      "command": "npx",
      "args": ["-y", "node-code-sandbox-mcp"]
    }
  }
}
```

#### Option B: Using Docker
```bash
docker run -d \
  --name node-sandbox \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /your/host/output:/your/host/output \
  -e FILES_DIR=/your/host/output \
  mcp/node-code-sandbox
```

> 💡 **Note**: The host directory is bind-mounted into the container at the **same absolute path**, and `FILES_DIR` is exposed to the MCP server.

---

### 2. Test the Setup

**Test 1: Basic Execution**
> Prompt: *"Run a console.log('Hello World')"*

✅ Expected: Tool response includes `Hello World`

**Test 2: Install Dependencies & Save Files**
> Prompt: *"Generate a QR code and save it as qrcode.png on my Desktop"*

✅ Expected: `qrcode.png` appears in the mounted directory (e.g., Desktop)

---

## 🛠️ API Tools

### `run_js_ephemeral`
Run a one-off JS script in a **brand-new disposable container**.

**Inputs**:
- `image` (default: `node:lts-slim`)
- `code`: JavaScript code to execute
- `dependencies`: Array of `{ name, version }` (optional)

**Behavior**:
- Creates `index.js` and `package.json`
- Installs dependencies
- Executes script
- Returns stdout and any generated files (e.g., `.txt`, `.json`, images)

**Example Call**:
```js
// Save a file during execution
const fs = require('fs');
fs.writeFileSync('hello.txt', 'Hello from sandbox!');
console.log('File saved.');
```
✅ Returns: Console output + `hello.txt` as a resource

---

### `sandbox_initialize`
Start a persistent sandbox container.

**Inputs**:
- `image` (default: `node:lts-slim`)
- `port` (optional)

**Output**: `container_id`

---

### `sandbox_exec`
Run shell commands inside a running sandbox.

**Inputs**:
- `container_id` (from `sandbox_initialize`)
- `commands`: Shell command(s) to execute

---

### `run_js`
Install npm packages and run JS in an existing sandbox.

**Inputs**:
- `container_id`
- `code`
- `dependencies` (optional)
- `listenOnPort` (optional, for background services)

**Behavior**:
- Runs `npm install --omit=dev --ignore-scripts --no-audit --loglevel=error`
- Executes `node index.js`
- Returns stdout or background execution notice

---

### `sandbox_stop`
Terminate and remove a sandbox container.

**Input**: `container_id`

---

### `search_npm_packages`
Search npm registry for packages.

**Inputs**:
- `searchTerm`
- Optional qualifiers: `author`, `maintainer`, `scope`, `keywords`, `not`, `is`, `boostExact`

**Output**: JSON array with `name`, `description`, and `README snippet`

---

## 💡 Usage Tips

| Use Case | Recommended Workflow |
|--------|----------------------|
| One-time script | `run_js_ephemeral` |
| Multi-step development | `sandbox_initialize` → `run_js` / `sandbox_exec` → `sandbox_stop` |
| File generation | Save files during script execution; they appear in `FILES_DIR` |

> ✅ **Pro Tip**: Use `run_js_ephemeral` for simplicity, persistent sandboxes for complex workflows.

---

## 🖥️ VS Code Integration

### Quick Install (Buttons)
- [Install js-sandbox-mcp (NPX)](https://vscode.dev/redirect?url=vscode://alfonsograziano.node-code-sandbox-mcp/install?npx)
- [Install js-sandbox-mcp (Docker)](https://vscode.dev/redirect?url=vscode://alfonsograziano.node-code-sandbox-mcp/install?docker)

### Manual Setup
Add to `.vscode/mcp.json` or `settings.json`:
```json
{
  "mcp": {
    "servers": {
      "node-code-sandbox": {
        "command": "npx",
        "args": ["-y", "node-code-sandbox-mcp"]
      }
    }
  }
}
```

---

## 🌐 Explore Use Cases

Visit [jsdevai.com/#use-cases](https://jsdevai.com/#use-cases) for:
- Creative prompt ideas
- Real-world examples
- Advanced experiments (e.g., chart generation, data processing, API mocking)

---

## 📦 Build & Development

To compile and bundle:
```bash
npm run build
```
