# RESEARCH_REPORT.md

## Project: mcp-servers
**Type:** Multi-language MCP server implementations
**Tech Stack:** TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C# (MCP Protocol SDK)
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| modelcontextprotocol/typescript-sdk | github.com/modelcontextprotocol/typescript-sdk | Official TS SDK (Tier 1) |
| modelcontextprotocol/python-sdk | github.com/modelcontextprotocol/python-sdk | Official Python SDK (Tier 1) |
| modelcontextprotocol/go-sdk | github.com/modelcontextprotocol/go-sdk | Official Go SDK (Tier 1) |
| modelcontextprotocol/csharp-sdk | github.com/modelcontextprotocol/csharp-sdk | Official C# SDK (Tier 1) |

---

## Key Findings

### MCP Protocol Architecture
- MCP uses client-server architecture with standardized JSON-RPC 2.0 messaging
- Servers expose **Tools** (model-invoked functions), **Resources** (read-only data), and **Prompts** (reusable templates)
- Three transport options: stdio (local), SSE (remote), Streamable HTTP
- Authorization via OAuth 2.1 for remote servers
- Tools use JSON Schema for input validation; outputs are structured results

### SDK Tiering System
- **Tier 1** (TypeScript, Python, Go, C#): Full feature coverage, active maintenance, protocol compliance
- **Tier 2** (Java, Rust): Core features, community contributions accepted
- **Tier 3** (Kotlin, PHP, Ruby, Swift): Community-maintained, basic protocol support
- All SDKs support creating servers (tools, resources, prompts) and clients

### Multi-Language Implementation
- Each lang dir is self-contained with own build system
- Shared JSON-RPC protocol enables cross-language reference
- Key considerations: type safety (TS), memory safety (Rust), ecosystem (Python)
- Testing: MCP Inspector + SDK-provided test utilities

### MCP Registry & Publishing
- Official MCP Registry at modelcontextprotocol.io/registry
- Publish via GitHub Actions; supports npm, pip, nuget
- Versioning with semver; automated moderation pipeline

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| MCP Server Development | modelcontextprotocol.io/docs/develop/build-server | Official Guide |
| SDK Reference | modelcontextprotocol.io/docs/sdk | SDK Overview |
| Protocol Spec (2025-11-25) | modelcontextprotocol.io/specification/2025-11-25 | Specification |
| MCP Inspector | modelcontextprotocol.io/docs/tools/inspector | Debugging Tool |
| Security Best Practices | modelcontextprotocol.io/docs/tutorials/security/security_best_practices | Guide |

---

## Best Practices

1. **SDK Tier Awareness** — Use Tier 1 SDKs (TS, Python, Go, C#) for production; Tier 3 for experimental/community ports
2. **Transport Selection** — stdio for local/desktop use, Streamable HTTP for production remote servers
3. **Tool Idempotency** — Design tool handlers as idempotent where possible; implement idempotency-key pattern for payment/state-changing operations
4. **Error Handling** — Use MCP's built-in error codes (InvalidParams, InternalError, etc.); never expose stack traces
5. **Resource Subscription** — Use `resources/subscribe` for live-updating resources; design for polling fallback

---

## Common Pitfalls

| Pitfall | Avoidance |
|---------|-----------|
| Missing tool validation | Always validate with JSON Schema before execution |
| Blocking handlers in async SDKs | Use async/await throughout |
| Hardcoded transport config | Accept transport via env vars or CLI args |
| No auth for remote servers | Implement OAuth 2.1 per spec |
| Missing cancellation | Handle `$/cancellation` in long-running tools |

---

## Performance

- **Connection pooling**: Reuse HTTP/SSE connections for remote transports
- **Tool throughput**: Keep handlers lightweight; offload heavy compute to workers
- **Resource caching**: Cache reads with TTL; prefer subscription over polling

---

## Security

- **Input sanitization**: Validate/sanitize all tool inputs; never eval user-supplied code
- **Auth**: Remote servers MUST implement OAuth 2.1 or equivalent
- **Rate limiting**: Per-client limits on tool execution
- **Audit logging**: Log all executions with caller identity, sanitized inputs, timestamps

---

## Related Projects (in workspace)

| Project | Shared Technology |
|---------|------------------|
| Banking | TypeScript/Next.js (TS SDK overlap) |
| comicwise | TypeScript/Next.js (TS SDK overlap) |
| rhixe_scans | TypeScript/Next.js (TS SDK overlap) |
| selenium_webdriver | Node.js/TypeScript (TS SDK overlap) |
| university-libary-jsm | TypeScript/Next.js (TS SDK overlap) |

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Official Docs | modelcontextprotocol.io | Protocol documentation |
| MCP GitHub | github.com/modelcontextprotocol | SDK repositories |
| Spec (2025-11-25) | modelcontextprotocol.io/specification/2025-11-25 | Full protocol spec |
| Registry | modelcontextprotocol.io/registry/about | Server publishing |
| Community | modelcontextprotocol.io/community/contributing | SEPs and contributing |

---

*Methodology: Cross-referenced 5 workspace projects + official MCP docs and SDK repos.*