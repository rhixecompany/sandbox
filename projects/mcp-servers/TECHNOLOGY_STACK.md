# 🏗 Technology Stack Blueprint - mcp-servers (Parent Directory)

**Project Path:** `projects/mcp-servers`
**Generated:** 2026-07-28
**Status:** Active — Multi-Language MCP Server Collection (11 implementations)

---

## Overview

This directory contains **11 independent MCP (Model Context Protocol) server implementations** across different programming languages. Each subdirectory is a complete, self-contained MCP server with its own build system, dependencies, and entry point.

---

## Language Implementations

| Language | Path | Runtime | Build System | MCP SDK |
|----------|------|---------|--------------|---------|
| **TypeScript** | `mcp-servers/typescript/` | Node.js 18+ | tsc + tsx | @modelcontextprotocol/sdk ^1.9.0 |
| **TypeScript (HTTP)** | `mcp-servers/copilot-studio/` | Node.js 18+ | tsc + ts-node | Custom HTTP transport |
| **Python** | `mcp-servers/python/` | Python 3.11+ | uv/hatchling | mcp[cli] >=1.28.0 |
| **Go** | `mcp-servers/go/` | Go 1.22 | Go Modules | go-sdk v0.0.0-20240617 |
| **Java** | `mcp-servers/java/` | JDK 17 | Maven 3.9+ | mcp 0.8.0 |
| **Kotlin** | `mcp-servers/kotlin/` | JVM 17 | Gradle 8.x (Kotlin DSL) | kotlin-sdk 0.3.0 |
| **PHP** | `mcp-servers/php/` | PHP 8.2+ | Composer 2.x | mcp-php-sdk ^1.0 |
| **Rust** | `mcp-servers/rust/` | Rust 2021 | Cargo | rmcp 0.8.1 |
| **Swift** | `mcp-servers/swift/` | Swift 6, macOS 15 | SwiftPM | swift-mcp (main branch) |
| **C#** | `mcp-servers/csharp/` | .NET 8 | MSBuild/dotnet CLI | ModelContextProtocol 0.1.0-preview |
| **Ruby** | `mcp-servers/ruby/` | Ruby 3.x | Bundler | mcp ~> 0.4.0 |

---

## Common Architecture

All implementations follow the same MCP pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                    MCP Client (Hermes, etc.)                │
└──────────────────────────┬──────────────────────────────────┘
                           │ STDIO Transport
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    MCP Server Process                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Tools      │  │  Resources   │  │   Prompts        │  │
│  │  • greet     │  │  • config    │  │  • templates     │  │
│  │  • calculate │  │  • files     │  │  • workflows     │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Standard Capabilities (per server)

| Capability | Description |
|------------|-------------|
| **Tools** | `greet(name: string)` — Returns greeting message |
| **Tools** | `calculate(operation, a, b)` — Basic arithmetic (where implemented) |
| **Resources** | `mcp://config` — Server configuration |
| **Resources** | `mcp://files/{path}` — File system access (where implemented) |

---

## Quick Start (All Languages)

### TypeScript (mcp-servers/typescript)
```bash
cd mcp-servers/typescript
npm install
npm run dev          # Development with hot reload
npm run build        # Compile to dist/
npm run start        # Run compiled
```

### Python (mcp-servers/python)
```bash
cd mcp-servers/python
uv sync              # or: pip install -e .
python -m main       # Run server
```

### Go (mcp-servers/go)
```bash
cd mcp-servers/go
go mod download
go run main.go       # Run directly
# or: go build && ./go-mcp-server
```

### Java (mcp-servers/java)
```bash
cd mcp-servers/java
mvn package
java -jar target/java-mcp-server.jar
```

### Kotlin (mcp-servers/kotlin)
```bash
cd mcp-servers/kotlin
./gradlew run
# or: ./gradlew fatJar && java -jar build/libs/kotlin-mcp-server-all.jar
```

### PHP (mcp-servers/php)
```bash
cd mcp-servers/php
composer install
php server.php
```

### Rust (mcp-servers/rust)
```bash
cd mcp-servers/rust
cargo run
# or: cargo build --release && ./target/release/rust-mcp-server
```

### Swift (mcp-servers/swift)
```bash
cd mcp-servers/swift
swift run MyMCPServer
```

### C# (mcp-servers/csharp)
```bash
cd mcp-servers/csharp
dotnet run
```

### Ruby (mcp-servers/ruby)
```bash
cd mcp-servers/ruby
bundle install
bundle exec bin/your-server
```

### Copilot Studio (mcp-servers/copilot-studio) — HTTP Transport
```bash
cd mcp-servers/copilot-studio
npm install
npm run dev
# Runs on HTTP :3000 for Copilot Studio integration
```

---

## Transport Protocols

| Server | Transport | Use Case |
|--------|-----------|----------|
| All except copilot-studio | **STDIO** | Local CLI tools, agent integration |
| copilot-studio | **HTTP (Streamable)** | Power Platform / Copilot Studio |

---

## Quality Gates (Per Language)

| Language | Type Check | Lint | Format | Test |
|----------|------------|------|--------|------|
| TypeScript | `tsc --noEmit` | ESLint | Prettier | Vitest/Jest |
| Python | `mypy` / `pyright` | Ruff | Ruff | pytest |
| Go | `go vet` | `gofmt` | `gofmt` | `go test` |
| Java | `mvn compile` | Spotless/Checkstyle | Spotless | `mvn test` |
| Kotlin | `./gradlew compileKotlin` | ktlint | ktlint | `./gradlew test` |
| PHP | PHPStan/Psalm | PHP CS Fixer | PHP CS Fixer | PHPUnit |
| Rust | `cargo check` | Clippy | `cargo fmt` | `cargo test` |
| Swift | `swift build` | swift-format | swift-format | `swift test` |
| C# | `dotnet build` | dotnet format | dotnet format | `dotnet test` |
| Ruby | - | RuboCop | RuboCop | minitest |

---

## License Summary

| Language | License |
|----------|---------|
| TypeScript | MIT |
| Python | MIT |
| Go | MIT / BSD-3-Clause |
| Java | MIT / Apache-2.0 |
| Kotlin | MIT / Apache-2.0 |
| PHP | MIT |
| Rust | MIT / Apache-2.0 |
| Swift | Apache-2.0 / MIT |
| C# | MIT |
| Ruby | MIT |

All implementations use **MIT** or permissive licenses.

---

## Related

- **Reference Implementation:** `projects/mcp-server-typescript/` — Extended TypeScript MCP server with more tools
- **Root Config:** `C:\Users\Alexa\Desktop\SandBox\.mcp.json` — MCP server registry
- **Main Blueprint:** `C:\Users\Alexa\Desktop\SandBox\Technology_Stack_Blueprint.md` — Workspace-wide tech stack

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*