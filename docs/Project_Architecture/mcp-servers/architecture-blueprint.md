# Architecture Blueprint: mcp-servers

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technologies |
|---|---|
| **Languages (10)** | TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C# |
| **Protocol** | Model Context Protocol (MCP) |
| **SDK** | MCP Server SDK (per-language) |
| **Build Systems** | npm, pip, dotnet, cargo, go mod, gradle, maven |
| **Pattern** | Multi-language reference implementations |

### Architectural Pattern Detected

**Pattern:** Multi-Language Reference Implementations  
Each subdirectory contains a **complete, buildable MCP server** in its respective language, following the MCP specification. The project serves as a **cross-language reference** for implementing MCP servers.

---

## 2. Architectural Overview

### Repository Structure

```
mcp-servers/
├── typescript/          # TypeScript MCP server
├── python/              # Python MCP server
├── go/                  # Go MCP server
├── rust/                # Rust MCP server
├── java/                # Java MCP server
├── kotlin/              # Kotlin MCP server
├── php/                 # PHP MCP server
├── ruby/                # Ruby MCP server
├── swift/               # Swift MCP server
├── csharp/              # C# MCP server
├── copilot-studio/      # Additional Copilot-related tooling
├── architecture.md      # Architecture overview
└── tech-stack.md        # Technology details
```

### Common MCP Server Pattern

Each language implementation follows the MCP specification:

```
MCP Client ←→ MCP Server (lang-specific)
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
  Tools        Resources      Prompts
  (Actions)    (Data)         (Templates)
```

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| 10 language implementations | Comprehensive reference for all major ecosystems |
| Self-contained directories | Each language has its own build system, no cross-deps |
| MCP specification compliance | All servers implement the standard protocol |
| Minimal dependencies | Each implementation uses only the MCP SDK + stdlib |

---

## 4. Cross-Language Patterns

### Common MCP Features Implemented

1. **Tools**: Callable functions exposed to AI models
2. **Resources**: Readable data endpoints (files, APIs, databases)
3. **Prompts**: Pre-written prompt templates
4. **Transports**: stdio (default), SSE (optional)
5. **Error handling**: Structured error responses per MCP spec

---

## 5. Extensibility Points

1. **New languages**: Add a new `<language>/` directory following the established pattern
2. **New MCP features**: Add to all 10 implementations simultaneously
3. **Additional transports**: Implement SSE or custom transports per language

---

*End of architecture blueprint.*
