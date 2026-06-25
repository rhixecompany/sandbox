# CSharpMcpServer

A C# implementation of a **Model Context Protocol (MCP)** server using .NET 8 and the `ModelContextProtocol` SDK.

## Overview

This project demonstrates how to build an MCP server in C#. It exposes tools that AI hosts (like Claude for Desktop, GitHub Copilot, or custom MCP clients) can discover and invoke over the stdio transport.

## Project Structure

```
CSharpMcpServer/
├── CSharpMcpServer.csproj   # Project file with NuGet dependencies
├── Program.cs                # Entry point with Host builder pattern
├── appsettings.json          # Configuration (logging, MCP settings)
├── README.md                 # This file
└── Tools/
    ├── GreetTool.cs          # Greeting tool
    └── CalculateTool.cs      # Calculator tool
```

## Prerequisites

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later

## Build & Run

```bash
# Restore dependencies
dotnet restore

# Build the project
dotnet build

# Run the server (stdio transport)
dotnet run
```

The server listens on **stdin/stdout** (stdio transport), which is the standard MCP transport for local client-server communication.

## Tools

### greet
Greets a user by name with a friendly message.

| Parameter | Type   | Required | Description                  |
|-----------|--------|----------|------------------------------|
| `Name`    | string | Yes      | The person's name            |
| `Title`   | string | No       | Optional honorific (Mr./Ms.) |

### calculate
Performs basic arithmetic operations.

| Parameter   | Type   | Required | Description                                    |
|-------------|--------|----------|------------------------------------------------|
| `A`         | number | Yes      | First operand                                  |
| `B`         | number | Yes      | Second operand                                 |
| `Operation` | string | Yes      | One of: add, subtract, multiply, divide, power, modulo |

## Configuration

Edit `appsettings.json` to adjust logging levels and MCP server metadata.

## Adding More Tools

1. Create a new class in the `Tools/` directory.
2. Decorate it with `[McpTool("toolname")]` and implement the tool interface.
3. The server auto-discovers it via `AddToolsFromAssembly()`.

## Resources

- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP .NET SDK on NuGet](https://www.nuget.org/packages/ModelContextProtocol/)
