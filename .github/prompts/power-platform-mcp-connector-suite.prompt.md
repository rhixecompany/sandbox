---
name: power-platform-mcp-connector-suite
title: Power Platform MCP Connector Suite
description: 'Generate complete Power Platform custom connector with MCP integration for Copilot Studio - includes schema generation, troubleshooting, and validation.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - agents
  - ai-assistant
  - data
  - frontend
  - generator
  - mcp
  - prompts
  - typescript
trigger: /power-platform-mcp-connector-suite
dependencies: []
metadata:
  hermes: {}
---

## Goal

Generate complete Power Platform custom connector with MCP integration for Copilot Studio - includes schema generation, troubleshooting, and validation.

# Power Platform MCP Connector SuiteGenerate comprehensive Power Platform custom connector implementations with Model Context Protocol integration for Microsoft Copilot Studio.

## MCP Capabilities in Copilot Studio

**Currently Supported:**

- ✅ **Tools**: Functions that the LLM can call (with user approval)- ✅ **Resources**: File-like data that agents can read (must be tool outputs)**Not Yet Supported:**- ❌ **Prompts**: Pre-written templates (prepare for future support)

## Connector Generation

Create complete Power Platform connector with:**Core Files:**

- `apiDefinition.swagger.json` with `x-ms-agentic-protocol: mcp-streamable-1.0`- `apiProperties.json` with connector metadata and authentication- `script.csx` with custom C# transformations for MCP JSON-RPC handling- `readme.md` with connector documentation**MCP Integration:**- POST `/mcp` endpoint for JSON-RPC 2.0 communication- McpResponse and McpErrorResponse schema definitions- Copilot Studio constraint compliance (no reference types, single types)- Resource integration as tool outputs (Resources and Tools supported; Prompts not yet supported)

## Schema Validation & Troubleshooting

**Validate schemas for Copilot Studio compliance:**

- ✅ No reference types (`$ref`) in tool inputs/outputs- ✅ Single type values only (not `["string", "number"]`)- ✅ Primitive types: string, number, integer, boolean, array, object- ✅ Resources as tool outputs, not separate entities- ✅ Full URIs for all endpoints**Common issues and fixes:**- Tools filtered → Remove reference types, use primitives- Type errors → Single types with validation logic- Resources unavailable → Include in tool outputs- Connection failures → Verify `x-ms-agentic-protocol` header

## Context Variables

- **Connector Name**: [Display name for the connector]- **Server Purpose**: [What the MCP server should accomplish]- **Tools Needed**: [List of MCP tools to implement]- **Resources**: [Types of resources to provide]- **Authentication**: [none, api-key, oauth2, basic]- **Host Environment**: [Azure Function, Express.js, etc.]- **Target APIs**: [External APIs to integrate with]

## Generation Modes

### Mode 1: Complete New Connector

Generate all files for a new Power Platform MCP connector from scratch, including CLI validation setup.

### Mode 2: Schema Validation

Analyze and fix existing schemas for Copilot Studio compliance using paconn and validation tools.

### Mode 3: Integration Troubleshooting

Diagnose and resolve MCP integration issues with Copilot Studio using CLI debugging tools.

### Mode 4: Hybrid Connector

Add MCP capabilities to existing Power Platform connector with proper validation workflows.

### Mode 5: Certification Preparation

Prepare connector for Microsoft certification submission with complete metadata and validation compliance.

### Mode 6: OAuth Security Hardening

Implement OAuth 2.0 authentication enhanced with MCP security best practices and advanced token validation.

## Expected Output

**1. apiDefinition.swagger.json**

- Swagger 2.0 format with Microsoft extensions- MCP endpoint: `POST /mcp` with proper protocol header- Compliant schema definitions (primitive types only)- McpResponse/McpErrorResponse definitions**2. apiProperties.json**- Connector metadata and branding (`iconBrandColor` required)- Authentication configuration- Policy templates for MCP transformations**3. script.csx**- JSON-RPC 2.0 message handling- Request/response transformations- MCP protocol compliance logic- Error handling and validation**4. Implementation guidance**- Tool registration and execution patterns- Resource management strategies- Copilot Studio integration steps- Testing and validation procedures

## Validation Checklist

### Technical Compliance

> - [ ] `x-ms-agentic-protocol: mcp-streamable-1.0` in MCP endpoint

## Example Usage

```yaml

Mode: Complete New ConnectorConnector Name: Customer Analytics MCPServer Purpose: Customer data analysis and insightsTools Needed:

- searchCustomers: Find customers by criteria  - getCustomerProfile: Retrieve detailed customer data  - analyzeCustomerTrends: Generate trend analysisResources:  - Customer profiles (JSON data)  - Analysis reports (structured data)Authentication: oauth2Host Environment: Azure FunctionTarget APIs: CRM REST API
```

## Template References

Detailed templates in `templates/power-platform-mcp-connector-suite/`:- `validation_checklist.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
