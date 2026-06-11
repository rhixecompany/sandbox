# MCP Best Practices & Security Guide

**Document Type:** Research Compilation  
**Created:** May 25, 2026  
**Source:** Web research, GitHub, industry blogs  
**Purpose:** Comprehensive guide for MCP server implementation and deployment

---

## Table of Contents

1. [MCP Fundamentals](#mcp-fundamentals)
2. [Core Design Principles](#core-design-principles)
3. [Best Practices for MCP Servers](#best-practices-for-mcp-servers)
4. [Security Best Practices](#security-best-practices)
5. [Architecture Patterns](#architecture-patterns)
6. [Implementation Guide](#implementation-guide)
7. [Common Pitfalls](#common-pitfalls)

---

## MCP Fundamentals

### What is MCP?

**Model Context Protocol (MCP)** is an open standard that provides a universal connection between LLMs and external tools, data sources, and services.

**Introduced by:** Anthropic (November 2024)  
**Adoption:** Microsoft, Google, OpenAI, Linux Foundation stewardship

### Three Core Primitives

- **Tools**: Functions the agent can call (`search_documents`, `create_issue`)
- **Resources**: Data the agent can read (files, database records)
- **Prompts**: Pre-built workflows the user or agent can invoke

### Architecture Components

```
┌─────────────────────────┐
│    Host (LLM/Agent)     │
└────────────┬────────────┘
             │
     ┌───────┴────────┐
     │   MCP Client   │
     └───────┬────────┘
             │
    ┌────────────────────┐
    │  JSON-RPC 2.0      │
    │  (stdio/HTTP/SSE)  │
    └────────┬───────────┘
             │
     ┌───────┴──────────┐
     │   MCP Server     │
     └───────┬──────────┘
             │
     ┌───────┴──────────────┐
     │ External Tools/Data  │
     └──────────────────────┘
```

### Protocol Overview

- **Communication:** JSON-RPC 2.0 (stateful)
- **Capability negotiation:** Client/server exchange capabilities
- **Transport Options:**
    - Standard Input/Output (stdio) — local servers
    - HTTP with Server-Sent Events (SSE) — remote servers
    - Custom transports (adhering to Transport interface)

---

## Core Design Principles

### 1. Design for Agents, Not Humans

**Key Difference:** REST API design ≠ MCP server design

| Principle         | REST APIs (Humans)              | MCP (Agents)                        |
| ----------------- | ------------------------------- | ----------------------------------- |
| **Discovery**     | Cheap (read docs once)          | Expensive (schema in every request) |
| **Composability** | Mix small endpoints             | Multi-step calls = slow iteration   |
| **Flexibility**   | Many options = more flexibility | Complexity = hallucination          |

**Rule:** Design tools around what agents want to achieve, not how APIs are structured.

### 2. Outcomes Over Operations

**Bad Approach:**

```
- get_user_by_email()
- list_orders(user_id)
- get_order_status(order_id)
```

→ Forces agent to orchestrate 3 round-trips

**Good Approach:**

```
- track_latest_order(email)
```

→ One high-level tool; orchestration happens in server code

### 3. Flatten Your Arguments

**Bad:**

```python
def search_orders(filters: dict) -> list
```

→ Agent guesses structure

**Good:**

```python
def search_orders(
    email: str,
    status: Literal["pending", "shipped", "delivered"] = "pending",
    limit: int = 10
) -> list
```

→ Clear, typed, constrained choices

### 4. Instructions are Context

**Docstrings matter:**

- When to use the tool
- How to format arguments
- What to expect back

**Error messages matter:**
Instead of Python exceptions, return helpful strings:

```
"User not found. Please try searching by email address instead."
```

→ Agent sees it as an observation and self-corrects

### 5. Data Efficiency

**Bad:** Throw large raw data at agent (bloats context window)

**Good:** Return curated, actionable results

---

## Best Practices for MCP Servers

### Six Core Best Practices

#### 1. **Outcomes, Not Operations**

- Expose high-level tools that accomplish goals
- Hide multi-step orchestration
- Example: `track_order(email)` instead of 3 separate tools

#### 2. **Flatten Arguments**

- Use top-level primitives
- Constrain with `Literal` types
- Provide sensible defaults
- Avoid nested dictionaries

#### 3. **Instructions as Context**

- Write detailed docstrings
- Specify when/how to use tools
- Include formatting requirements
- Return helpful error messages

#### 4. **Scope Minimization**

- Follow least-privilege principle
- Grant only necessary permissions
- Use scopes like `calendar:read` not `admin:*`

#### 5. **Input Validation**

- Treat all MCP inputs as potentially malicious
- Validate request parameters rigorously
- Check for prompt injection patterns
- Implement rate limiting

#### 6. **Clear Tool Design**

- One tool = one business outcome
- Avoid 1:1 REST endpoint mapping
- Pre-filter and curate results
- Return structured, typed responses

### SDK Support

| Language          | Package                       | Notes           |
| ----------------- | ----------------------------- | --------------- |
| **TypeScript/JS** | `@modelcontextprotocol/sdk`   | Primary, mature |
| **Python**        | `modelcontextprotocol-python` | Robust          |
| **Kotlin**        | `modelcontextprotocol-kotlin` | Modern JVM      |
| **Java**          | `modelcontextprotocol-java`   | Enterprise      |
| **C#**            | `ModelContextProtocol.Sdk`    | .NET            |

### Server Lifecycle

1. **Initialization**
    - Client sends: `protocolVersion`, `capabilities`, `clientInfo`
    - Server responds: `protocolVersion`, `capabilities`, `serverInfo`, `instructions`
    - Server sends: `initialized` notification

2. **Message Exchange**
    - Clients call: `tools/call`, `resources/read`, `prompts/get`
    - Servers send: `listChanged`, `progress`, `cancelled`, `logging`

3. **Termination**
    - Connection ends when `shutdown` is called

### Transport Options

#### Standard Input/Output (stdio)

**Use Case:** Local servers launched as subprocesses

```
✓ Lower overhead, simpler setup
✓ OS process security
✗ Local only, tied to client lifecycle
```

#### HTTP with Server-Sent Events (SSE)

**Use Case:** Local or remote, multi-client capable

```
✓ Flexible (local/remote), multi-client
✓ Web-standard protocols, resumable streams
✗ Higher overhead, requires HTTP server
✗ Requires HTTPS for production
```

**Requirements:**

- HTTPS mandatory
- OAuth 2.0 for authentication
- Stateful sessions via `Mcp-Session-Id`
- SSE resumability via `id` and `Last-Event-ID`

---

## Security Best Practices

### Critical Vulnerabilities Found

**Research by Knostic & Backslash Security:**

- Nearly 2,000 public MCP servers with NO authentication
- Hundreds bound to `0.0.0.0` with arbitrary code execution
- Default configurations with excessive permissions

### 8 Essential Security Practices

#### 1. **Separate Authorization Server from Resource Server**

**Architecture:**

- MCP servers = OAuth Resource Servers (validate tokens, enforce access)
- Separate = Authorization Server (user auth, token issuance)

**Benefits:**

- Cleaner, auditable
- Easier to scale
- Simpler compliance

**June 2025 Spec:** Servers publish `.well-known` endpoint; clients discover auth server automatically

#### 2. **Implement OAuth 2.1 and PKCE**

**Non-negotiable:**

- OAuth 2.1 mandated for HTTP-based MCP
- PKCE required for all public clients

**Critical Details:**

- **Resource Indicators (RFC 8707):** Bind specific tokens to specific servers
- **PKCE:** Secures authorization code flow against interception
- **Never:** Store client secrets on client side

#### 3. **Protect with User Authentication & SSO**

**Requirement:** Users authenticate through SSO before agent acts

**Example:** Connecting to shared Google Drive or GitHub org

**Why Model-Level Defenses Fail:**

- Prompt injection and context poisoning bypass model defenses
- Instruction drift has architectural impact
- Infrastructure-level auth is only reliable fix

#### 4. **Build Consent Management into Flow**

**Challenge:** Semi-autonomous agents request access without hands-on-keyboard interaction

**Solution:** Clear consent screens showing:

- Which tools are accessible
- What data may be read/written
- Permission duration

**Critical:** Time-bound consent prevents indefinite access

#### 5. **Enforce Scope-Based Access Control**

**Principle:** Least-privilege at granular level

**Example:**

```
Calendar read ≠ Full Google Workspace access
Agent drafting proposal in Docs ≠ All Google apps
```

**Implementation:**

- Use scopes like `calendar:read`, `email:send`, not `admin:*`
- Token bound to specific MCP server
- Minimal tool exposure

#### 6. **Input Validation & Output Sanitization**

**Input Validation:**

- Treat all MCP inputs as potentially malicious
- Validate request parameters rigorously
- Detect prompt injection patterns
- Implement rate limiting

**Output Sanitization:**

- Don't expose sensitive system information
- Sanitize error messages
- Filter credentials from responses

#### 7. **Prevent Credential Leaks**

**Exposure Vectors:**

- API keys in logs
- Credentials in tool responses
- SSH keys in file outputs

**Mitigation:**

- Never log sensitive data
- Redact secrets from responses
- Implement credential scanning
- Use environment variables for secrets

#### 8. **Local MCP Server Compromise Prevention**

**Risks:**

- Arbitrary code execution via `npx malicious-package`
- Privilege escalation with `sudo`
- Data exfiltration to attacker servers

**Mitigation:**

- Never run MCP servers with `sudo`
- Use subprocess isolation (stdio transport)
- Validate all package dependencies
- Implement sandboxing where possible

### Common Security Mistakes to Avoid

```
❌ scopes_supported: "*"
❌ scopes_supported: "all" or "full-access"
❌ Binding server to 0.0.0.0 without authentication
❌ Storing client secrets on client side
❌ No token validation
❌ Excessive tool permissions
❌ Unvalidated user input
❌ Credentials in error messages
```

### Confused Deputy Problem

**Attack Pattern:**

- Malicious OAuth proxy skips user consent flow
- Request appears authorized but user never consented

**Mitigation:**

- Validate `redirect_uri` in authorization flow
- Protect with `X-Frame-Options: DENY`
- Use secure cookies: `Secure`, `HttpOnly`, `SameSite=Lax`
- Validate `state` parameter in callback

### Server-Side Request Forgery (SSRF) Prevention

**Attack:** Attacker tricks server into accessing internal resources

```
http://192.168.1.1/admin
http://169.254.169.254/  (AWS metadata)
http://localhost:6379/   (Redis)
```

**Mitigation:**

- Block internal IP ranges:
    - `http://`, `https://` not allowed for internal
    - `localhost`, `127.0.0.1`, `::1`
    - `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`
    - `169.254.0.0/16` (link-local)
    - `fc00::/7` (IPv6 private)

---

## Architecture Patterns

### Multi-Client Server (HTTP/SSE)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client 1  │     │   Client 2  │     │   Client 3  │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                   ┌───────▼─────────┐
                   │  HTTP/SSE Mux   │
                   │  Stateful Sessions│
                   └───────┬─────────┘
                           │
                   ┌───────▼─────────┐
                   │  MCP Server     │
                   │  (HTTP Endpoint)│
                   └───────┬─────────┘
                           │
                   ┌───────▼─────────┐
                   │ Resource Server │
                   └─────────────────┘
```

### OAuth 2.1 Flow with PKCE

```
1. Client generates code_verifier & code_challenge
2. Client redirects to Authorization Server with challenge
3. User authenticates & grants consent
4. Auth Server returns authorization code
5. Client exchanges code + verifier for token
6. MCP Server validates token with Auth Server
7. Token bound to specific MCP server (Resource Indicator)
```

---

## Implementation Guide

### Basic TypeScript Server

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
    name: "my-server",
    version: "1.0.0",
});

// Define a tool with clear, typed arguments
server.tool(
    "search_documents",
    "Search across all documents by keyword",
    {
        query: z.string().describe("Search query (case-insensitive)"),
        limit: z
            .number()
            .int()
            .min(1)
            .max(50)
            .default(10)
            .describe("Maximum results to return"),
    },
    async (args) => {
        // Validate inputs
        if (args.query.length === 0) {
            return { error: "Query cannot be empty" };
        }

        // Execute search
        const results = await searchDocs(args.query, args.limit);

        // Return structured result
        return {
            found: results.length,
            documents: results.map((doc) => ({
                id: doc.id,
                title: doc.title,
                excerpt: doc.excerpt,
            })),
        };
    },
);

// Start server
const transport = new StdioServerTransport({
    reader: process.stdin,
    writer: process.stdout,
});

await server.connect(transport);
```

### Key Implementation Points

1. **Clear Tool Descriptions** — Tell agent when/how to use
2. **Typed Arguments** — Use Zod for validation
3. **Error Handling** — Return helpful messages
4. **Result Curation** — Pre-filter and structure data
5. **Security Validation** — Check all inputs

---

## Common Pitfalls

### ❌ Pitfall 1: 1:1 REST Endpoint Mapping

**Problem:**

```python
# Bad: Wraps REST endpoints directly
- get_user(id: int)
- get_user_orders(user_id: int)
- get_order_details(order_id: int)
```

**Solution:**

```python
# Good: Outcome-oriented
- get_customer_order_status(email: str)
```

### ❌ Pitfall 2: Complex Nested Arguments

**Problem:**

```python
def search(filters: {"type": str, "sort": dict, ...})
```

**Solution:**

```python
def search(
    type: Literal["order", "customer", "product"],
    sort_by: Literal["date", "status"],
    sort_order: Literal["asc", "desc"] = "desc"
)
```

### ❌ Pitfall 3: No Error Context

**Problem:**

```python
raise ValueError("Invalid input")
```

**Solution:**

```python
return {"error": "User not found. Try searching by email address instead."}
```

### ❌ Pitfall 4: Data Dumping

**Problem:** Return entire database query result

**Solution:** Curate, filter, and limit results

### ❌ Pitfall 5: Missing Authentication

**Problem:** No OAuth, no token validation

**Solution:** Implement OAuth 2.1 + PKCE, validate every request

### ❌ Pitfall 6: Excessive Permissions

**Problem:** Grant all permissions by default

**Solution:** Implement fine-grained scopes, use least-privilege

---

## Summary Checklist

- [ ] Design tools around agent goals, not API structure
- [ ] Flatten arguments and use typed enums
- [ ] Write clear docstrings and error messages
- [ ] Implement OAuth 2.1 + PKCE for HTTP servers
- [ ] Validate all inputs rigorously
- [ ] Use least-privilege access control
- [ ] Curate and structure results
- [ ] Protect against SSRF and prompt injection
- [ ] Separate Authorization Server from Resource Server
- [ ] Implement consent management for sensitive actions

---

## Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [OAuth 2.1 Standard](https://datatracker.ietf.org/doc/html/rfc6749)
- [OWASP GenAI Security](https://owasp.org/www-project-ai-security/)

---

**Document Version:** 1.0  
**Last Updated:** May 25, 2026  
**Author:** Alexa (Research compilation)
results

### ❌ Pitfall 5: Missing Authentication

**Problem:** No OAuth, no token validation

**Solution:** Implement OAuth 2.1 + PKCE, validate every request

### ❌ Pitfall 6: Excessive Permissions

**Problem:** Grant all permissions by default

**Solution:** Implement fine-grained scopes, use least-privilege

---

## Summary Checklist

- [ ] Design tools around agent goals, not API structure
- [ ] Flatten arguments and use typed enums
- [ ] Write clear docstrings and error messages
- [ ] Implement OAuth 2.1 + PKCE for HTTP servers
- [ ] Validate all inputs rigorously
- [ ] Use least-privilege access control
- [ ] Curate and structure results
- [ ] Protect against SSRF and prompt injection
- [ ] Separate Authorization Server from Resource Server
- [ ] Implement consent management for sensitive actions

---

## Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [OAuth 2.1 Standard](https://datatracker.ietf.org/doc/html/rfc6749)
- [OWASP GenAI Security](https://owasp.org/www-project-ai-security/)

---

**Document Version:** 1.0  
**Last Updated:** May 25, 2026  
**Author:** Alexa (Research compilation)

