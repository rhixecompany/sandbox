---
name: mcp-create-declarative-agent
title: Create MCP-based Declarative Agent for Microsoft 365 Copilot
description: mcp-create-declarative-agent.prompt.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - agents
  - ai-assistant
  - generator
  - mcp
  - ml
  - prompts
  - specification
  - typescript
  - workflow
trigger: /mcp-create-declarative-agent
dependencies: []
metadata:
  hermes: {}
---

## Goal

Use this prompt to handle the create mcp based declarative agent for microsoft 365 copilot workflow.

## Context

Use when you need to create mcp based declarative agent for microsoft 365 copilot for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Requirements

> Generate the following project structure using Microsoft 365 Agents Toolkit:>
>
> 1. **Scaffold declarative agent** via Agents Toolkit

## MCP Server Integration

### Supported MCP Endpoints

> The MCP server must provide:

## Response Semantics

### Define Data Mapping

Use `response_semantics` to extract relevant fields from API responses:```json"capabilities": {  "response_semantics": {    "data_path": "$.results",    "properties": {      "title": "$.name",      "subtitle": "$.description",      "url": "$.link"    }  }}```

### Add Adaptive Cards (Optional)

See the `mcp-create-adaptive-cards` prompt for adding visual card templates.

## Environment Configuration

Create `.env.local` or `.env.dev` for credentials:```envOAUTH_REFERENCE_ID=your-oauth-reference-idCLIENT_ID=your-client-idCLIENT_SECRET=your-client-secret```

## Test

ing & Deployment

### Local Testing

1. **Provision** agent in Agents Toolkit
2. **Start debugging** to sideload in Teams
3. Test in Microsoft 365 Copilot at <https://m365.cloud.microsoft/chat>
4. Authenticate when prompted
5. Query the agent using natural language

### Validation

- Verify tool imports in ai-plugin.json
- Check authentication configuration
- Test each exposed function
- Validate response data mapping

## Best Practices

### Tool Design

- **Focused functions**: Each tool should do one thing well
- **Clear descriptions**: Help the model understand when to use each tool
- **Minimal scoping**: Only import tools the agent needs
- **Descriptive names**: Use action-oriented function names

### Security

- **Use OAuth 2.0** for production scenarios
- **Store secrets** in environment variables
- **Validate inputs** on the MCP server side
- **Limit scopes** to minimum required permissions
- **Use reference IDs** for OAuth registration

### Instructions

- **Be specific** about the agent's purpose and capabilities
- **Define behavior** for both successful and error scenarios
- **Reference tools** explicitly in instructions when applicable
- **Set expectations** for users about what the agent can/cannot do

### Performance

- **Cache responses** when appropriate on MCP server
- **Batch operations** where possible
- **Set timeouts** for long-running operations
- **Paginate results** for large datasets

## Common MCP Server Examples

### GitHub MCP Server

```
URL: https://api.githubcopilot.com/mcp/Tools: search_repositories, search_users, get_repositoryAuth: OAuth 2.0
```

### Jira MCP Server

```

URL: https://your-domain.atlassian.net/mcp/Tools: search_issues, create_issue, update_issueAuth: OAuth 2.0
```

### Custom Service

```

URL: https://api.your-service.com/mcp/Tools: Custom tools exposed by your serviceAuth: OAuth 2.0 or SSO
```

## Workflow

Ask the user:1. What MCP server are you integrating with (URL)?2. What tools should be exposed to Copilot?3. What authentication method does the server support?4. What should the agent's primary purpose be?5. Do you need response semantics or Adaptive Cards?Then generate:- Complete appPackage/ structure (manifest.json, declarativeAgent.json, ai-plugin.json)- mcp.json configuration- .env.local template- Provisioning and testing instructions

## Troubleshooting

### MCP Server Not Responding

- Verify server URL is correct
- Check network connectivity
- Validate MCP server implements required endpoints

### Authentication Fails

- Verify OAuth credentials are correct
- Check reference ID matches registration
- Confirm scopes are requested properly
- Test OAuth flow independently

### Tools Not Appearing

- Ensure mcp.json points to correct server
- Verify tools were selected during import
- Check ai-plugin.json has correct function definitions
- Re-fetch actions from MCP if server changed

### Agent Not Understanding Queries

- Review instructions in declarativeAgent.json
- Check function descriptions are clear
- Verify response_semantics extract correct data
- Test with more specific queries````

## Template References

Detailed templates in `templates/mcp-create-declarative-agent/`:- `mcp_server_integration.md`- `requirements.md`

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
