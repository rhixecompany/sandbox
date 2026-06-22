# Implementation Details

> Extracted from `csharp-mcp-server-generator.prompt.md`.

## Implementation Details

### Basic Project Setup

- Use .NET 8.0 or later
- Create a console application
- Add necessary NuGet packages with --prerelease flag
- Configure logging to stderr

### Server Configuration

- Use `Host.CreateApplicationBuilder` for DI and lifecycle management
- Configure `AddMcpServer()` with stdio transport
- Use `WithToolsFromAssembly()` for automatic tool discovery
- Ensure the server runs with `RunAsync()`

### Tool Implementation

- Use `[McpServerToolType]` attribute on tool classes
- Use `[McpServerTool]` attribute on tool methods
- Add `[Description]` attributes to tools and parameters
- Support async operations where appropriate
- Include proper parameter validation

### Code Quality

- Follow C# naming conventions
- Include XML documentation comments
- Use nullable reference types
- Implement proper error handling with McpProtocolException
- Use structured logging for debugging
