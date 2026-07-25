---
author: Hermes Agent
description: Build agentic applications with GitHub Copilot SDK. Use when embedding Copilot in apps, creating custom agents, connecting to MCP servers, or building interactive CLI assistants.
license: MIT
metadata:
  hermes:
    tags: [imported, github, copilot, sdk, agents, mcp, cli]
name: copilot-sdk
tags:
- imported
- github
- copilot
- sdk
- agents
- mcp
- cli
- scripts
title: GitHub Copilot SDK
version: 1.1.0
---

# GitHub Copilot SDK

## Overview

Build agentic applications with GitHub Copilot SDK. Use when embedding Copilot in apps, creating custom agents, connecting to MCP servers, or building interactive CLI assistants.

## When to Use

- Embedding Copilot in custom applications
- Creating custom AI agents for specific domains
- Connecting to MCP (Model Context Protocol) servers
- Building interactive CLI assistants
- Session persistence across restarts
- Multi-turn conversations with context

## When NOT to Use

- Learning Copilot CLI basics (use `copilot-cli-quickstart`)
- VS Code extension development (use `vscode-extension-playbook`)
- Extension command reference (use `vscode-ext-commands`)

## Quick Start

```bash
# Install SDK
npm install @github/copilot-sdk

# Or use TypeScript directly
npx -y @github/copilot-sdk
```

```typescript
import { CopilotClient } from '@github/copilot-sdk';

const client = new CopilotClient();
const session = await client.createSession({ model: 'gpt-4.1' });
const response = await session.sendAndWait({ prompt: 'Hello!' });
console.log(response.text);
await client.stop();
```

## Workflow

### Phase 1: Initialize Client

```typescript
const client = new CopilotClient({
  cliPath: 'copilot',        // or full path
  cliUrl: 'localhost:4321',  // connect to existing server
  port: 4321,                // server port
  useStdio: true,            // stdio transport
  logLevel: 'info',
  autoStart: true,
  autoRestart: true,
  cwd: process.cwd()
});
```

### Phase 2: Create Session

```typescript
// Basic session
const session = await client.createSession({ model: 'gpt-4.1' });

// Persistent session
const session = await client.createSession({
  sessionId: 'user-123-conversation',
  model: 'gpt-4.1'
});

// Resume existing session
const session = await client.resumeSession('user-123-conversation');
```

### Phase 3: Send Messages

```typescript
// Simple request
const response = await session.sendAndWait({ prompt: 'Explain async/await' }, 30000);

// With file attachment
const response = await session.send({
  prompt: 'Analyze this CSV',
  attachments: [{ type: 'file', path: './data.csv', displayName: 'Sales Data' }]
});

// Streaming
for await (const delta of session.send({ prompt: 'Write a long story' })) {
  if (delta.type === 'assistant.message_delta') process.stdout.write(delta.text);
}
```

### Phase 4: Advanced Features

**MCP Server Integration:**
```typescript
const session = await client.createSession({
  mcpServers: {
    github: { command: 'npx', args: ['-y', '@github/github-mcp-server'] }
  }
});
```

**Custom Agents:**
```typescript
const session = await client.createSession({
  customAgents: [{
    name: 'code-reviewer',
    description: 'Reviews code for security issues',
    tools: ['read', 'grep', 'edit']
  }]
});
```

**System Message:**
```typescript
const session = await client.createSession({
  systemMessage: 'You are a senior Rust developer. Prefer explicit types.'
});
```

### Phase 5: Cleanup

```typescript
try {
  // ... use session
} finally {
  await client.stop(); // Always cleanup
}
```

## Verification Checklist

- [ ] Copilot CLI installed and authenticated
- [ ] Client initializes without ENOENT/ECONNREFUSED
- [ ] Session creates successfully
- [ ] Messages send and receive responses
- [ ] Streaming works (if enabled)
- [ ] Session persistence works (resume by ID)
- [ ] MCP servers connect (if configured)
- [ ] Custom agents load (if configured)
- [ ] Cleanup runs on exit (try/finally)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `github` | GitHub API access |
| `copilot-cli-quickstart` | Basic CLI knowledge |

## Related Skills

- `copilot-cli-quickstart` — Learn Copilot CLI basics
- `vscode-ext-commands` — Extension command reference
- `github` — GitHub API operations
- `suggest-awesome-github-copilot-agents` — Agent recommendations

## Usage Examples

```bash
# Simple chat
copilot-sdk --prompt "How do I read a file in Rust?"

# With file context
copilot-sdk --prompt "Review this" --context src/main.rs

# Interactive mode
copilot-sdk --interactive

# Custom model
copilot-sdk --model gpt-4.1 --prompt "Explain lifetimes"
```

## Error Handling

- **CLI not installed or authenticated:** SDK requires Copilot CLI. If `copilot --version` fails, throws `ENOENT`. Always verify CLI state before initializing.
- **Shutdown is mandatory:** Forgetting `client.stop()` leaves a Copilot CLI server process running. Always use `try/finally` or equivalent.
- **Streaming handlers eat memory:** Without careful handler implementation, streaming delta responses accumulate. Process and flush deltas promptly.
- **Technical Preview instability:** SDK is in Technical Preview and may have breaking changes. Pin version and test after upgrades.
- **Model availability:** Not all models work with SDK. Use `client.getModels()` to check available models at runtime.
- **Session ID collisions:** Custom session IDs must be unique. Use user ID + purpose pattern.

## Pitfalls

- **CLI not installed or authenticated:** The SDK requires Copilot CLI to be installed and authenticated. If `copilot --version` fails, the SDK will throw `ENOENT`. Always verify the CLI state before initializing the client.
- **Shutdown is mandatory:** Forgetting to call `client.stop()` leaves a Copilot CLI server process running. Always use `try/finally` or equivalent to ensure cleanup, even on errors.
- **Streaming handlers eat memory:** Without careful handler implementation, streaming delta responses accumulate in memory. Process and flush deltas promptly rather than buffering the entire response.
- **Technical Preview instability:** The SDK is in Technical Preview and may have breaking changes. Pin your SDK version and test after upgrades. Avoid using in production without thorough testing.
- **Model availability:** Not all models work with the SDK. Use `client.getModels()` to check available models at runtime rather than hardcoding model names.
- **Session ID collisions:** If using custom session IDs, ensure they are unique to avoid accidentally resuming the wrong conversation. Use a combination of user ID and purpose as the session ID pattern.

## References

- GitHub Repository: <https://github.com/github/copilot-sdk>
- Getting Started Tutorial: <https://github.com/github/copilot-sdk/blob/main/docs/tutorials/first-app.md>
- GitHub MCP Server: <https://github.com/github/github-mcp-server>
- MCP Servers Directory: <https://github.com/modelcontextprotocol/servers>
- Cookbook: <https://github.com/github/copilot-sdk/tree/main/cookbook>
- Samples: <https://github.com/github/copilot-sdk/tree/main/samples>