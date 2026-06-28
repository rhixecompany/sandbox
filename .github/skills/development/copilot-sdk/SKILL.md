---
author: Alexa
description: Build agentic applications with GitHub Copilot SDK. Use when embedding
  AI agents in apps, creating custom tools, implementing streaming responses, managing
  sessions, connecting to MCP servers, or creating custom agents. Triggers on Copilot
  SDK, GitHub SDK, agentic app, embed Copilot, programmable agent, MCP server, custom
  agent.
license: MIT
name: copilot-sdk
tags:
- imported
title: Copilot Sdk
version: 1.0.0

---
# GitHub Copilot SDK

Embed Copilot's agentic workflows in any application using Python, TypeScript, Go, or .NET.


## When to Use

- Use this skill when working with copilot sdk tasks
- Triggered by: `copilot-sdk` related operations

## Overview

The GitHub Copilot SDK exposes the same engine behind Copilot CLI: a production-tested agent runtime you can invoke programmatically. No need to build your own orchestration - you define agent behavior, Copilot handles planning, tool invocation, file edits, and more.

## Prerequisites

1. **GitHub Copilot CLI** installed and authenticated ([Installation guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli))
2. **Language runtime**: Node.js 18+, Python 3.8+, Go 1.21+, or .NET 8.0+

Verify CLI: `copilot --version`

## Installation

### Node.js/TypeScript

```bash
mkdir copilot-demo && cd copilot-demo
npm init -y --init-type module
npm install @github/copilot-sdk tsx
```

### Python

```bash
pip install github-copilot-sdk
```

### Go

```bash
mkdir copilot-demo && cd copilot-demo
go mod init copilot-demo
go get github.com/github/copilot-sdk/go
```

### .NET

```bash
dotnet new console -n CopilotDemo && cd CopilotDemo
dotnet add package GitHub.Copilot.SDK
```

## Quick Start

### TypeScript

```typescript
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();
const session = await client.createSession({ model: "gpt-4.1" });

const response = await session.sendAndWait({
  prompt: "What is 2 + 2?"
});
console.log(response?.data.content);

await client.stop();
process.exit(0);
```

Run: `npx tsx index.ts`

### .NET (C#)

```csharp
using GitHub.Copilot.SDK;

await using var client = new CopilotClient();
await using var session = await client.CreateSessionAsync(new SessionConfig { Model = "gpt-4.1" });

var response = await session.SendAndWaitAsync(new MessageOptions { Prompt = "What is 2 + 2?" });
Console.WriteLine(response?.Data.Content);
```

Run: `dotnet run`

## Streaming Responses

Enable real-time output for better UX:

## Custom Tools

Define tools that Copilot can invoke during reasoning. When you define a tool, you tell Copilot:

1. **What the tool does** (description)
2. **What parameters it needs** (schema)
3. **What code to run** (handler)

### TypeScript (JSON Schema)

```typescript
import {
  CopilotClient,
  defineTool,
  SessionEvent
} from "@github/copilot-sdk";

const getWeather = defineTool("get_weather", {
  description: "Get the current weather for a city",
  parameters: {
    type: "object",
    properties: {
      city: { type: "string", description: "The city name" }
    },
    required: ["city"]
  },
  handler: async (args: { city: string }) => {
    const { city } = args;
    // In a real app, call a weather API here
    const conditions = ["sunny", "cloudy", "rainy", "partly cloudy"];
    const temp = Math.floor(Math.random() * 30) + 50;
    const condition =
      conditions[Math.floor(Math.random() * conditions.length)];
    return { city, temperature: `${temp}°F`, condition };
  }
});

const client = new CopilotClient();
const session = await client.createSession({
  model: "gpt-4.1",
  streaming: true,
  tools: [getWeather]
});

session.on((event: SessionEvent) => {
  if (event.type === "assistant.message_delta") {
    process.stdout.write(event.data.deltaContent);
  }
});

await session.sendAndWait({
  prompt: "What's the weather like in Seattle and Tokyo?"
});

await client.stop();
process.exit(0);
```

### Python (Pydantic)

```python
import asyncio
import random
import sys
from copilot import CopilotClient
from copilot.tools import define_tool
from copilot.generated.session_events import SessionEventType
from pydantic import BaseModel, Field

class GetWeatherParams(BaseModel):
    city: str = Field(description="The name of the city to get weather for")

@define_tool(description="Get the current weather for a city")
async def get_weather(params: GetWeatherParams) -> dict:
    city = params.city
    conditions = ["sunny", "cloudy", "rainy", "partly cloudy"]
    temp = random.randint(50, 80)
    condition = random.choice(conditions)
    return {"city": city, "temperature": f"{temp}°F", "condition": condition}

async def main():
    client = CopilotClient()
    await client.start()

    session = await client.create_session({
        "model": "gpt-4.1",
        "streaming": True,
        "tools": [get_weather],
    })

    def handle_event(event):
        if event.type == SessionEventType.ASSISTANT_MESSAGE_DELTA:
            sys.stdout.write(event.data.delta_content)
            sys.stdout.flush()

    session.on(handle_event)

    await session.send_and_wait({
        "prompt": "What's the weather like in Seattle and Tokyo?"
    })

    await client.stop()

asyncio.run(main())
```

### .NET (Microsoft.Extensions.AI)

```csharp
using GitHub.Copilot.SDK;
using Microsoft.Extensions.AI;
using System.ComponentModel;

var getWeather = AIFunctionFactory.Create(
    ([Description("The city name")] string city) =>
    {
        var conditions = new[] { "sunny", "cloudy", "rainy", "partly cloudy" };
        var temp = Random.Shared.Next(50, 80);
        var condition = conditions[Random.Shared.Next(conditions.Length)];
        return new { city, temperature = $"{temp}°F", condition };
    },
    "get_weather",
    "Get the current weather for a city"
);

await using var session = await client.CreateSessionAsync(new SessionConfig
{
    Model = "gpt-4.1",
    Streaming = true,
    Tools = [getWeather],
});
```

## How Tools Work

When Copilot decides to call your tool:

1. Copilot sends a tool call request with the parameters
2. The SDK runs your handler function
3. The result is sent back to Copilot
4. Copilot incorporates the result into its response

Copilot decides when to call your tool based on the user's question and your tool's description.

## Interactive CLI Assistant

Build a complete interactive assistant:

## MCP Server Integration

Connect to MCP (Model Context Protocol) servers for pre-built tools. Connect to GitHub's MCP server for repository, issue, and PR access:

## Custom Agents

Define specialized AI personas for specific tasks:

## System Message

Customize the AI's behavior and personality:

## External CLI Server

Run the CLI in server mode separately and connect the SDK to it. Useful for debugging, resource sharing, or custom environments.

### Start CLI in Server Mode

```bash
copilot --server --port 4321
```

### Connect SDK to External Server

## Event Types

| Event                       | Description                       |
| --------------------------- | --------------------------------- |
| `user.message`              | User input added                  |
| `assistant.message`         | Complete model response           |
| `assistant.message_delta`   | Streaming response chunk          |
| `assistant.reasoning`       | Model reasoning (model-dependent) |
| `assistant.reasoning_delta` | Streaming reasoning chunk         |
| `tool.execution_start`      | Tool invocation started           |
| `tool.execution_complete`   | Tool execution finished           |
| `session.idle`              | No active processing              |
| `session.error`             | Error occurred                    |

## Client Configuration

| Option | Description | Default |
| --- | --- | --- |
| `cliPath` | Path to Copilot CLI executable | System PATH |
| `cliUrl` | Connect to existing server (e.g., "localhost:4321") | None |
| `port` | Server communication port | Random |
| `useStdio` | Use stdio transport instead of TCP | true |
| `logLevel` | Logging verbosity | "info" |
| `autoStart` | Launch server automatically | true |
| `autoRestart` | Restart on crashes | true |
| `cwd` | Working directory for CLI process | Inherited |

## Session Configuration

| Option | Description |
| --- | --- |
| `model` | LLM to use ("gpt-4.1", "claude-sonnet-4.5", etc.) |
| `sessionId` | Custom session identifier |
| `tools` | Custom tool definitions |
| `mcpServers` | MCP server connections |
| `customAgents` | Custom agent personas |
| `systemMessage` | Override default system prompt |
| `streaming` | Enable incremental response chunks |
| `availableTools` | Whitelist of permitted tools |
| `excludedTools` | Blacklist of disabled tools |

## Session Persistence

Save and resume conversations across restarts:

### Create with Custom ID

```typescript
const session = await client.createSession({
  sessionId: "user-123-conversation",
  model: "gpt-4.1"
});
```

### Resume Session

```typescript
const session = await client.resumeSession("user-123-conversation");
await session.send({ prompt: "What did we discuss earlier?" });
```

### List and Delete Sessions

```typescript
const sessions = await client.listSessions();
await client.deleteSession("old-session-id");
```

## Error Handling

```typescript
try {
  const client = new CopilotClient();
  const session = await client.createSession({ model: "gpt-4.1" });
  const response = await session.sendAndWait(
    { prompt: "Hello!" },
    30000 // timeout in ms
  );
} catch (error) {
  if (error.code === "ENOENT") {
    console.error("Copilot CLI not installed");
  } else if (error.code === "ECONNREFUSED") {
    console.error("Cannot connect to Copilot server");
  } else {
    console.error("Error:", error.message);
  }
} finally {
  await client.stop();
}
```

## Graceful Shutdown

```typescript
process.on("SIGINT", async () => {
  console.log("Shutting down...");
  await client.stop();
  process.exit(0);
});
```

## Common Patterns

### Multi-turn Conversation

```typescript
const session = await client.createSession({ model: "gpt-4.1" });

await session.sendAndWait({ prompt: "My name is Alice" });
await session.sendAndWait({ prompt: "What's my name?" });
// Response: "Your name is Alice"
```

### File Attachments

```typescript
await session.send({
  prompt: "Analyze this file",
  attachments: [
    {
      type: "file",
      path: "./data.csv",
      displayName: "Sales Data"
    }
  ]
});
```

### Abort Long Operations

```typescript
const timeoutId = setTimeout(() => {
  session.abort();
}, 60000);

session.on(event => {
  if (event.type === "session.idle") {
    clearTimeout(timeoutId);
  }
});
```

## Available Models

Query available models at runtime:

```typescript
const models = await client.getModels();
// Returns: ["gpt-4.1", "gpt-4o", "claude-sonnet-4.5", ...]
```

## Best Practices

1. **Always cleanup**: Use `try-finally` or `defer` to ensure `client.stop()` is called
2. **Set timeouts**: Use `sendAndWait` with timeout for long operations
3. **Handle events**: Subscribe to error events for robust error handling
4. **Use streaming**: Enable streaming for better UX on long responses
5. **Persist sessions**: Use custom session IDs for multi-turn conversations
6. **Define clear tools**: Write descriptive tool names and descriptions

## Architecture

```
Your Application
       |
  SDK Client
       | JSON-RPC
  Copilot CLI (server mode)
       |
  GitHub (models, auth)
```

The SDK manages the CLI process lifecycle automatically. All communication happens via JSON-RPC over stdio or TCP.

## Resources

- **GitHub Repository**: https://github.com/github/copilot-sdk
- **Getting Started Tutorial**: https://github.com/github/copilot-sdk/blob/main/docs/tutorials/first-app.md
- **GitHub MCP Server**: https://github.com/github/github-mcp-server
- **MCP Servers Directory**: https://github.com/modelcontextprotocol/servers
- **Cookbook**: https://github.com/github/copilot-sdk/tree/main/cookbook
- **Samples**: https://github.com/github/copilot-sdk/tree/main/samples

## Status

This SDK is in **Technical Preview** and may have breaking changes. Not recommended for production use yet.


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

