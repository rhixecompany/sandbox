# mcp-servers — Folder Structure

> **Stack:** 10 Languages (TypeScript, Python, Go, Rust, Java, Kotlin, C#, PHP, Ruby, Swift)  
> **Type:** Multi-Language MCP Server Collection  
> **Status:** Active

## Directory Tree

```
mcp-servers/
├── .github/workflows/
├── .vscode/
├── copilot-studio/            # Copilot Studio plugin MCP server
│   ├── dist/tools/
│   └── tools/
├── csharp/                    # C# .NET MCP server
│   ├── .vscode/
│   └── Tools/
├── go/                        # Go MCP server
│   ├── config/
│   ├── tools/
│   └── go.mod
├── java/                      # Java MCP server
│   ├── .mvn/wrapper/
│   ├── pom.xml
│   └── src/main/
├── kotlin/                    # Kotlin MCP server
│   ├── build.gradle
│   └── src/main/
├── php/                       # PHP MCP server
│   └── src/Tools/
├── python/                    # Python MCP server
│   ├── .venv/
│   ├── pyproject.toml
│   └── ...
├── ruby/                      # Ruby MCP server
│   ├── bin/
│   ├── lib/my_mcp_server/
│   └── test/tools/
├── rust/                      # Rust MCP server
│   ├── Cargo.toml
│   └── src/tools/
├── swift/                     # Swift MCP server
│   ├── Package.swift
│   └── Sources/MyMCPServer/
└── typescript/                # TypeScript MCP server
    ├── dist/tools/
    ├── src/tools/
    └── package.json
```

## Key Patterns

- **Language per directory:** Each `<language>/` is a standalone MCP server
- **Standard tool-path:** `tools/` or `Tools/` houses MCP tool implementations
- **Ecosystem conventions:** Each language uses its standard build tool (Cargo.toml, pom.xml, Package.swift, package.json, go.mod, pyproject.toml)
- **Naming:** Directory names match language IDs (lowercase), source files follow language conventions (PascalCase for C#, snake_case for Python, etc.)
