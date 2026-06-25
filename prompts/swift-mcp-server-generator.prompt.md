---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Swift MCP Server Generator
name: swift-mcp-server-generator
description: "Generate a complete Model Context Protocol server project in Swift using the official MCP Swift SDK package."
---

## Goal

Generate a complete Model Context Protocol server project in Swift using the official MCP Swift SDK package.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Project Generation

When asked to create a Swift MCP server, generate a complete project with this structure:

```
my-mcp-server/
├── Package.swift
├── Sources/
│   └── MyMCPServer/
│       ├── main.swift
│       ├── Server.swift
│       ├── Tools/
│       │   ├── ToolDefinitions.swift
│       │   └── ToolHandlers.swift
│       ├── Resources/
│       │   ├── ResourceDefinitions.swift
│       │   └── ResourceHandlers.swift
│       └── Prompts/
│           ├── PromptDefinitions.swift
│           └── PromptHandlers.swift
├── Tests/
│   └── MyMCPServerTests/
│       └── ServerTests.swift
└── README.md
```

## Package.swift Template

> // swift-tools-version: 6.0
> import PackageDescription

> **Full content:** `templates/swift-mcp-server-generator/packageswift_template.md`

## main.swift Template

> import ServiceLifecycle
> struct MCPService: Service {

> **Full content:** `templates/swift-mcp-server-generator/mainswift_template.md`

## Server.swift Template

```swift
import MCP
import Logging

func createServer() async -> Server {
    let server = Server(
        name: "MyMCPServer",
        version: "1.0.0",
        capabilities: .init(
            prompts: .init(listChanged: true),
            resources: .init(subscribe: true, listChanged: true),
            tools: .init(listChanged: true)
        )
    )

    // Register tool handlers
    await registerToolHandlers(server: server)

    // Register resource handlers
    await registerResourceHandlers(server: server)

    // Register prompt handlers
    await registerPromptHandlers(server: server)

    return server
}
```

## ToolDefinitions.swift Template

> func getToolDefinitions() -> [Tool] {
> description: "Generate a greeting message",

> **Full content:** `templates/swift-mcp-server-generator/tooldefinitionsswift_template.md`

## ToolHandlers.swift Template

> private let logger = Logger(label: "com.example.mcp-server.tools")
> func registerToolHandlers(server: Server) async {

> **Full content:** `templates/swift-mcp-server-generator/toolhandlersswift_template.md`

## ResourceDefinitions.swift Template

```swift
import MCP

func getResourceDefinitions() -> [Resource] {
    [
        Resource(
            name: "Example Data",
            uri: "resource://data/example",
            description: "Example resource data",
            mimeType: "application/json"
        ),
        Resource(
            name: "Configuration",
            uri: "resource://config",
            description: "Server configuration",
            mimeType: "application/json"
        )
    ]
}
```

## ResourceHandlers.swift Template

> private let logger = Logger(label: "com.example.mcp-server.resources")
> actor ResourceState {

> **Full content:** `templates/swift-mcp-server-generator/resourcehandlersswift_template.md`

## PromptDefinitions.swift Template

```swift
import MCP

func getPromptDefinitions() -> [Prompt] {
    [
        Prompt(
            name: "code-review",
            description: "Generate a code review prompt",
            arguments: [
                .init(name: "language", description: "Programming language", required: true),
                .init(name: "focus", description: "Review focus area", required: false)
            ]
        )
    ]
}
```

## PromptHandlers.swift Template

> private let logger = Logger(label: "com.example.mcp-server.prompts")
> func registerPromptHandlers(server: Server) async {

> **Full content:** `templates/swift-mcp-server-generator/prompthandlersswift_template.md`

## ServerTests.swift Template

> @testable import MyMCPServer
> final class ServerTests: XCTestCase {

> **Full content:** `templates/swift-mcp-server-generator/servertestsswift_template.md`

## README.md Template

````markdown
# MyMCPServer

A Model Context Protocol server built with Swift.

## Features

- ✅ Tools: greet, calculate
- ✅ Resources: example data, configuration
- ✅ Prompts: code-review
- ✅ Graceful shutdown with ServiceLifecycle
- ✅ Structured logging with swift-log
- ✅ Full test coverage

## Requirements

- Swift 6.0+
- macOS 13+, iOS 16+, or Linux

## Installation

```bash
swift build -c release
```
````

## Usage

Run the server:

```bash
swift run
```

Or with logging:

```bash
LOG_LEVEL=debug swift run
```

## Testing

```bash
swift test
```

## Development

The server uses:

- [MCP Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - MCP protocol implementation
- [swift-log](https://github.com/apple/swift-log) - Structured logging
- [swift-service-lifecycle](https://github.com/swift-server/swift-service-lifecycle) - Graceful shutdown

## Project Structure

- `Sources/MyMCPServer/main.swift` - Entry point with ServiceLifecycle
- `Sources/MyMCPServer/Server.swift` - Server configuration
- `Sources/MyMCPServer/Tools/` - Tool definitions and handlers
- `Sources/MyMCPServer/Resources/` - Resource definitions and handlers
- `Sources/MyMCPServer/Prompts/` - Prompt definitions and handlers
- `Tests/` - Unit tests

## License

MIT

````

## Generation Instructions

1. **Ask for project name and description**
2. **Generate all files** with proper naming
3. **Use actor-based state** for thread safety
4. **Include comprehensive logging** with swift-log
5. **Implement graceful shutdown** with ServiceLifecycle
6. **Add tests** for all handlers
7. **Use modern Swift concurrency** (async/await)
8. **Follow Swift naming conventions** (camelCase, PascalCase)
9. **Include error handling** with proper MCPError usage
10. **Document public APIs** with doc comments

## Build and Run

```bash
# Build
swift build

# Run
swift run

# Test
swift test

# Release build
swift build -c release

# Install
swift build -c release
cp .build/release/MyMCPServer /usr/local/bin/
````

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "/path/to/MyMCPServer"
    }
  }
}
````
```


## Template References

Detailed templates in `templates/swift-mcp-server-generator/`:
- `mainswift_template.md`
- `packageswift_template.md`
- `prompthandlersswift_template.md`
- `resourcehandlersswift_template.md`
- `servertestsswift_template.md`
- `tooldefinitionsswift_template.md`
- `toolhandlersswift_template.md`
