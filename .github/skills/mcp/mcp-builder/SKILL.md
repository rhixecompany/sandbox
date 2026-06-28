---
author: Alexa
description: Use when creating MCP servers that enable LLMs to interact with external
  services through well-designed tools in Python (FastMCP) or Node/TypeScript.
license: MIT
name: mcp-builder
tags:
- imported
title: MCP Builder
version: 1.0.0

---
## Description

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Building MCP servers for external APIs
- Integrating external services with LLMs
- Creating custom tools for AI agents
- Building Python (FastMCP) or Node/TypeScript (MCP SDK) servers
- Designing tool interfaces for LLM consumption

## When NOT to Use

- Using existing MCP servers
- Non-MCP integrations
- Simple API calls without MCP
- Real-time streaming services

## Workflow

### Phase 1: Design Tools

- Identify external service capabilities
- Design tool interfaces
- Plan parameter schemas
- Define return types

### Phase 2: Implement Server

- Choose language (Python/Node)
- Set up MCP SDK
- Implement tool handlers
- Add error handling

### Phase 3: Test & Validate

- Test tool execution
- Verify parameter validation
- Test error cases
- Validate schemas

### Phase 4: Deploy & Document

- Deploy MCP server
- Document tool usage
- Create examples
- Set up monitoring

## Tools & References

- **Related Skills**: customize-opencode
- **FastMCP**: Python MCP framework
- **MCP SDK**: Node/TypeScript framework
- **Tool Design**: Schema validation, error handling

## Best Practices

- Design clear, focused tools
- Validate all parameters
- Provide helpful error messages
- Document tool behavior
- Test edge cases
- Version your tools
- Monitor tool usage



## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

