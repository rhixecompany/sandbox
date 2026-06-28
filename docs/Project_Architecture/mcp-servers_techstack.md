# MCP Servers — Tech Stack

| Language | Build System | Runtime |
|----------|-------------|---------|
| **TypeScript** | npm/bun | Node.js |
| **Python** | pip/uv | Python 3 |
| **Go** | go mod | Go |
| **Rust** | cargo | Rust |
| **Java** | mvn/gradle | JVM |
| **Kotlin** | gradle | JVM |
| **PHP** | composer | PHP |
| **Ruby** | bundler | Ruby |
| **Swift** | swift build | Swift |
| **C#** | dotnet | .NET |

**Common Protocol:** All servers implement Model Context Protocol (MCP) via JSON-RPC, using stdin/HTTP transport.
