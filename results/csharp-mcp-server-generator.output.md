# C# MCP Server — Scaffold (DRY-RUN)

**Prompt:** `csharp-mcp-server-generator.prompt.md`
**Mode:** Dry-run / structure scaffold. No external dependencies installed, no `dotnet` build executed (deps are external/network → labeled dry-run). Code below is the authoritative scaffolding that would be written to disk.
**Date:** 2026-07-09

> ⚠️ Skipped references:
> - `templates/csharp-mcp-server-generator/implementation_details.md` — referenced by the prompt (line 44, 65) but **does not exist** in the workspace. Inline body is authoritative; implementation details were synthesized from the prompt's explicit requirements.

---

## 1. Project Structure (would be created on disk)

```
CsharpMcpServer/
├── CsharpMcpServer.csproj
├── Program.cs
├── appsettings.json
├── Tools/
│   └── FileOperationsTool.cs
├── Models/
│   └── ToolResults.cs
├── Properties/
│   └── launchSettings.json
├── README.md
└── CsharpMcpServer.sln
```

---

## 2. `CsharpMcpServer.csproj`

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <RootNamespace>CsharpMcpServer</RootNamespace>
    <AssemblyName>CsharpMcpServer</AssemblyName>
    <InvariantGlobalization>true</InvariantGlobalization>
  </PropertyGroup>

  <ItemGroup>
    <!-- MCP SDK (prerelease at time of authoring) -->
    <PackageReference Include="ModelContextProtocol" Version="0.1.0-preview.1" />
    <PackageReference Include="Microsoft.Extensions.Hosting" Version="8.0.0" />
    <PackageReference Include="Microsoft.Extensions.Logging.Console" Version="8.0.0" />
  </ItemGroup>

</Project>
```

> Note: `ModelContextProtocol` version pin should be confirmed against the current NuGet prerelease feed (`dotnet add package ModelContextProtocol --prerelease`).

---

## 3. `Program.cs` — Host builder + DI + stderr logging

```csharp
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using ModelContextProtocol;
using CsharpMcpServer.Tools;

// All logs MUST go to stderr so they never corrupt the stdio transport (stdout).
var builder = Host.CreateApplicationBuilder(args);

builder.Logging
    .ClearProviders()
    .AddConsole(o => o.LogToStandardErrorThreshold = LogLevel.Trace);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();

await builder.Build().RunAsync();
```

---

## 4. `Tools/FileOperationsTool.cs` — sample tool with attributes + error handling

```csharp
using System.ComponentModel;
using System.Text.Json;
using ModelContextProtocol.Server;
using CsharpMcpServer.Models;

namespace CsharpMcpServer.Tools;

[McpServerToolType]
public sealed class FileOperationsTool
{
    private readonly ILogger<FileOperationsTool> _logger;

    public FileOperationsTool(ILogger<FileOperationsTool> logger)
        => _logger = logger;

    [McpServerTool, Description("Reads a UTF-8 text file and returns its contents.")]
    public FileReadResult ReadFile(
        [Description("Absolute or relative path of the file to read.")] string path)
    {
        try
        {
            if (string.IsNullOrWhiteSpace(path))
                return new FileReadResult(false, null, "Path must not be empty.");

            if (!File.Exists(path))
                return new FileReadResult(false, null, $"File not found: {path}");

            var content = File.ReadAllText(path);
            _logger.LogInformation("Read {ByteCount} bytes from {Path}", content.Length, path);
            return new FileReadResult(true, content, null);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to read file {Path}", path);
            return new FileReadResult(false, null, ex.Message);
        }
    }

    [McpServerTool, Description("Searches a directory for files whose name matches a pattern.")]
    public FileSearchResult SearchFiles(
        [Description("Directory to search.")] string directory,
        [Description("Search pattern, e.g. '*.cs'.")] string pattern = "*")
    {
        try
        {
            if (!Directory.Exists(directory))
                return new FileSearchResult(false, Array.Empty<string>(), "Directory not found.");

            var matches = Directory.GetFiles(directory, pattern, SearchOption.AllDirectories);
            return new FileSearchResult(true, matches, null);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Search failed in {Dir}", directory);
            return new FileSearchResult(false, Array.Empty<string>(), ex.Message);
        }
    }
}
```

---

## 5. `Models/ToolResults.cs`

```csharp
namespace CsharpMcpServer.Models;

public sealed record FileReadResult(bool Success, string? Content, string? Error);
public sealed record FileSearchResult(bool Success, string[] Matches, string? Error);
```

---

## 6. `appsettings.json`

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.Hosting.Lifetime": "Warning"
    }
  }
}
```

---

## 7. `Properties/launchSettings.json`

```json
{
  "profiles": {
    "CsharpMcpServer": {
      "commandName": "Project",
      "commandLineArgs": "",
      "environmentVariables": {
        "DOTNET_ENVIRONMENT": "Production"
      }
    }
  }
}
```

---

## 8. `README.md`

# CsharpMcpServer

A Model Context Protocol (MCP) server written in C# (.NET 8) exposing file-operation tools over the stdio transport.

## Requirements
- .NET 8 SDK
- Network access to NuGet (for `ModelContextProtocol` prerelease)

## Build & Run

```bash
dotnet restore
dotnet build --configuration Release
dotnet run --project CsharpMcpServer.csproj
```

The server speaks the MCP stdio protocol on its standard streams. **All diagnostic logging is sent to stderr**, so stdout stays reserved for the protocol.

## Testing with an MCP client

```json
{
  "mcpServers": {
    "csharp-files": {
      "command": "dotnet",
      "args": ["run", "--project", "CsharpMcpServer.csproj"]
    }
  }
}
```

Then call the `ReadFile` / `SearchFiles` tools from any MCP-compatible client.

## Troubleshooting
- **Client receives garbage / no handshake** → verify nothing writes to stdout except the MCP SDK. Check custom `Console.Write` usage.
- **Tool not discovered** → ensure the tool class carries `[McpServerToolType]` and is registered via `.WithToolsFromAssembly()`.
- **Package restore fails** → confirm the `ModelContextProtocol` prerelease feed is reachable; run `dotnet nuget locals all --clear`.

---

## 9. Verification (dry-run status)

| Step | Status |
|------|--------|
| Project structure defined | ✅ in this document |
| `csproj` / packages pinned | ✅ (version to confirm at install) |
| stderr logging wired | ✅ |
| Host builder + DI | ✅ |
| ≥1 tool with attributes | ✅ `FileOperationsTool` |
| Error handling / validation | ✅ guard clauses + try/catch |
| `dotnet` build executed | ⏭️ skipped (external deps / network) — labeled dry-run |
| `dotnet` restore executed | ⏭️ skipped (external deps / network) — labeled dry-run |

**To promote to a real build:** run `dotnet restore && dotnet build` inside `CsharpMcpServer/`. That step requires network access to NuGet and was intentionally not performed in this dry-run.
