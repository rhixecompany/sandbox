---
name: mcp-code-sandbox
title: MCP Code Sandbox — Isolated Node.js Execution
description: Exposes all code-sandbox MCP tools for isolated Docker-based JavaScript/Node.js execution, npm package search, sandbox lifecycle management, and ephemeral code runs. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - code-sandbox
  - sandbox
  - nodejs
  - execution
---
# MCP Code Sandbox

Provides isolated Docker container environments for running Node.js code safely. Sandboxes are disposable containers that can be initialized, used across multiple commands, and torn down.

## Overview

Automated reasoning and workflow tool for `mcp-code-sandbox`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `code-sandbox` must be enabled (`hermes mcp list` → `✓ enabled`)
- Docker must be running locally
- Config: `npx -y node-code-sandbox-mcp`

## Tools

| Tool | Description |
|------|-------------|
| `sandbox_initialize` | Start a new isolated Docker container (Node.js) for multi-step work |
| `sandbox_exec` | Run shell commands inside an initialized sandbox |
| `sandbox_stop` | Terminate and remove a sandbox container |
| `run_js` | Install deps + run ESModules JS inside a sandbox (reusable env) |
| `run_js_ephemeral` | One-shot JS execution in a temporary container with auto-cleanup |
| `search_npm_packages` | Search npm registry by keyword — returns name, description, README snippet |

## Workflow

### Phase 1: Verify

```
hermes mcp test code-sandbox
```

### Phase 2: Choose Execution Mode

**Ephemeral (one-shot, auto-cleanup):**
```
run_js_ephemeral(
  code: "import fs from 'fs'; console.log(fs.readdirSync('./').join(', '))",
  dependencies: []
)
```

**Sandbox session (multi-step):**
```
1. sandbox_initialize()
2. sandbox_exec(command: "pwd && ls -la")
3. run_js(code: "const x = 1 + 1; console.log(x)", dependencies: [])
4. sandbox_stop()
```

**Npm discovery:**
```
search_npm_packages(query: "typescript code analysis")
```

### Phase 3: Test Cases

```bash
# 1. Connectivity
hermes mcp test code-sandbox

# 2. Search npm
# Call: mcp_code_sandbox_search_npm_packages(query="express")

# 3. Ephemeral JS
# Call: mcp_code_sandbox_run_js_ephemeral(code="console.log('hello from sandbox')")

# 4. Full sandbox lifecycle
# Call: mcp_code_sandbox_sandbox_initialize()
# Call: mcp_code_sandbox_sandbox_exec(command="node --version")
# Call: mcp_code_sandbox_sandbox_stop()
```

## Best Practices

1. **Prefer `run_js_ephemeral`** for single-shot tasks — no cleanup needed, lower overhead
2. **Use full sandbox lifecycle** when: running multiple commands, installing deps once, iterating on code
3. **Always stop sandboxes** after multi-step work — containers consume resources
4. **ESModules only** — code must use `import/export` syntax, not `require()`
5. **Read/write from `./files` directory** — that's the sandbox's persistent working directory
6. **Search npm first** when you need a package — confirms name and latest version

## Pitfalls

- Code must be **ESModules** (`import`/`export`) — CommonJS `require()` fails
- Sandbox containers are **not preserved** across agent sessions — stop them when done
- File operations use `./files/` subdirectory — absolute paths from the host won't work inside the sandbox
- Docker must be running locally or the sandbox tools will fail to initialize
- `sandbox_stop` must be called explicitly after `sandbox_initialize` — no auto-cleanup on session close
- Ephemeral runs have no persistent state between calls

## Verification Checklist

- [ ] `hermes mcp test code-sandbox` passes
- [ ] `search_npm_packages` returns valid results
- [ ] `run_js_ephemeral` executes and returns output
- [ ] Sandbox lifecycle: initialize → exec → stop completes without errors

## When to Use


- When you need to perform MCP Code Sandbox — Isolated Node.js Execution operations or tasks
- When managing MCP Code Sandbox — Isolated Node.js Execution infrastructure or configurations
- When automating or debugging MCP Code Sandbox — Isolated Node.js Execution workflows
- **Triggers**: "mcp code sandbox — isolated node.js execution" required for a project
