---
category: software-development
title: Context7
name: context7
description: "Use when looking up current library or framework documentation, finding code examples for specific APIs, or verifying correct usage of library functions."
---
## Goal
Use when looking up current library or framework documentation, finding code examples for specific APIs, or verifying correct usage of library functions.


## context7

## Description


Retrieve up-to-date documentation for software libraries, frameworks, and components via the Context7 MCP server. Provides current information about library APIs, features, and usage examples by injecting live docs into agent context.

Context7 runs as an HTTP MCP server. Configure it under `mcp_servers` in the Hermes config with an API key header (`CONTEXT7_API_KEY`). Test with `hermes mcp test context7` — expected output: connected with 2 tools (`resolve-library-id`, `query-docs`). See the `native-mcp` skill for the MCP config format reference.

## Prerequisites

- Context7 API key from context7.com/dashboard (free tier available)
- Hermes MCP client active (the `mcp` Python package must be available)

## Configuration

```yaml
mcp_servers:
  context7:
    url: https://mcp.context7.com/mcp
    headers:
      CONTEXT7_API_KEY: "your-api-key"
    enabled: true
```

Use the literal key string in the headers field — ${VAR} expansion is not guaranteed in MCP headers.

## Testing

After configuring, verify with:
```
hermes mcp test context7
```

Expected: "Connected" with 2 tools discovered. Slow responses may need a higher `connect_timeout`.

## Available Tools

| MCP Tool | Purpose |
|----------|---------|
| `resolve-library-id` | Converts a package name to a Context7 library ID |
| `query-docs` | Fetches documentation and code examples |

Hermes prefixes these as `mcp_context7_resolve_library_id` and `mcp_context7_query_docs`.

## When to Use

- Looking up library or framework documentation
- Finding code examples for specific APIs
- Verifying correct usage of library functions
- Obtaining current information about library APIs
- Checking for API changes or deprecations
- Learning new library features

## When NOT to Use

- General programming questions
- Language standard library usage
- Offline or local documentation lookup
- Historical API versions

## Workflow

### Phase 1: Identify Library

- Determine library name and version
- Confirm library is available in Context7
- Note specific API or feature needed

### Phase 2: Query Documentation

- Search for relevant documentation
- Filter by version if needed
- Review available examples

### Phase 3: Extract Information

- Find API signatures and parameters
- Locate usage examples
- Note any deprecations or warnings

### Phase 4: Apply Learning

- Implement based on documentation
- Test with provided examples
- Verify behavior matches docs

## Tools & References

- **Related Skills**: claude-api, clonedeps
- **Context7 API**: Up-to-date library documentation
- **Supported Libraries**: 1000+ frameworks and packages

## Best Practices

- Always check for version-specific information
- Review examples before implementing
- Note deprecation warnings
- Keep documentation links in code comments
- Update code when library versions change
- Report documentation gaps or errors

