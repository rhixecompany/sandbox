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

- Client-server architecture with standardized JSON-RPC 2.0 messaging
- Servers expose **Tools** (model-invoked functions), **Resources** (read-only data), **Prompts** (reusable templates)
- Three transports: stdio (local), SSE (remote), Streamable HTTP
- Authorization via OAuth 2.1 for remote servers
- MCP now sees **97M+ monthly SDK downloads** (early 2026), adopted by 28% of Fortune 500

### SDK Tiering System

- **Tier 1** (TS, Python, Go, C#): Full feature coverage, active maintenance
- **Tier 2** (Java, Rust): Core features, community contributions accepted
- **Tier 3** (Kotlin, PHP, Ruby, Swift): Community-maintained, basic protocol support

### Multi-Language Implementation

- Each lang dir is self-contained with own build system
- Shared JSON-RPC protocol enables cross-language reference
- Key considerations: type safety (TS), memory safety (Rust), ecosystem (Python)
- Testing: MCP Inspector + SDK-provided test utilities

### Security Landscape (2026)

- Astrix Security research found significant proportion of MCP servers exposed plaintext HTTP endpoints
- OWASP Top 10 for Agentic Applications includes MCP-specific tool poisoning
- **Rule**: start every new server in read-only mode; grant write access only after observing usage patterns

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| MCP Server Development | modelcontextprotocol.io/docs/develop/build-server | Official Guide |
| SDK Reference | modelcontextprotocol.io/docs/sdk | SDK Overview |
| Protocol Spec (2025-11-25) | modelcontextprotocol.io/specification/2025-11-25 | Specification |
| MCP Inspector | modelcontextprotocol.io/docs/tools/inspector | Debugging Tool |

---

## Best Practices

1. **SDK Tier Awareness** — Use Tier 1 SDKs (TS, Python, Go, C#) for production
2. **Transport Selection** — stdio for local/desktop use, Streamable HTTP for remote
3. **Tool Idempotency** — idempotency-key pattern for state-changing operations
4. **Error Handling** — Use MCP's built-in error codes (InvalidParams, InternalError); never expose stack traces
5. **Security First** — OAuth 2.1 for remote; read-only mode by default; never reuse prod credentials

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
- **Zero trust**: Use dedicated API keys with minimum required permissions; never reuse prod credentials

---

## Related Projects (in workspace)

| Project | Shared Technology |
|---------|------------------|
| Banking | TypeScript/Next.js (TS SDK overlap) |
| comicwise | TypeScript/Next.js (TS SDK overlap) |
| selenium_webdriver | Node.js/TypeScript (TS SDK overlap) |
| Bash | TypeScript tooling and linting conventions |

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Official Docs | modelcontextprotocol.io | Protocol documentation |
| MCP GitHub | github.com/modelcontextprotocol | SDK repositories |
| Spec (2025-11-25) | modelcontextprotocol.io/specification/2025-11-25 | Full protocol spec |
| Registry | modelcontextprotocol.io/registry/about | Server publishing |

### Methodology

Cross-referenced workspace projects + official MCP docs, SDK repos, and 2026 security research (ASTRIX, OWASP Agentic Top 10).

**Last verified:** 2026-07-28.
