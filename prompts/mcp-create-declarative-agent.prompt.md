---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create MCP-based Declarative Agent for Microsoft 365 Copilot
name: mcp-create-declarative-agent
description: "mcp-create-declarative-agent.prompt"
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
  - agents
  - ai-assistant
  - documentation
  - microsoft
  - orchestration
  - planning
  - specification
  - typespec
  - workflow
metadata:
  hermes:
    related_skills: []
    tags:
    - mcp-create-declarative-agent.prompt

trigger: mcp-create-declarative-agent

---
metadata:
  hermes:
    related_skills: []
    tags:
    - mcp-create-declarative-agent.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - mcp-create-declarative-agent.prompt

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
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

> Generate the following project structure using Microsoft 365 Agents Toolkit:
> 1. **Scaffold declarative agent** via Agents Toolkit

> **Full content:** `templates/mcp-create-declarative-agent/requirements.md`

## MCP Server Integration

> ### Supported MCP Endpoints
> The MCP server must provide:

> **Full content:** `templates/mcp-create-declarative-agent/mcp_server_integration.md`

## Response Semantics

### Define Data Mapping
Use `response_semantics` to extract relevant fields from API responses:

```json
"capabilities": {
  "response_semantics": {
    "data_path": "$.results",
    "properties": {
      "title": "$.name",
      "subtitle": "$.description",
      "url": "$.link"
    }
  }
}
```

### Add Adaptive Cards (Optional)
See the `mcp-create-adaptive-cards` prompt for adding visual card templates.

## Environment Configuration

Create `.env.local` or `.env.dev` for credentials:

```env
OAUTH_REFERENCE_ID=your-oauth-reference-id
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
```

## Testing & Deployment

### Local Testing
1. **Provision** agent in Agents Toolkit
2. **Start debugging** to sideload in Teams
3. Test in Microsoft 365 Copilot at https://m365.cloud.microsoft/chat
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
URL: https://api.githubcopilot.com/mcp/
Tools: search_repositories, search_users, get_repository
Auth: OAuth 2.0
```

### Jira MCP Server
```
URL: https://your-domain.atlassian.net/mcp/
Tools: search_issues, create_issue, update_issue
Auth: OAuth 2.0
```

### Custom Service
```
URL: https://api.your-service.com/mcp/
Tools: Custom tools exposed by your service
Auth: OAuth 2.0 or SSO
```

## Workflow

Ask the user:
1. What MCP server are you integrating with (URL)?
2. What tools should be exposed to Copilot?
3. What authentication method does the server support?
4. What should the agent's primary purpose be?
5. Do you need response semantics or Adaptive Cards?

Then generate:
- Complete appPackage/ structure (manifest.json, declarativeAgent.json, ai-plugin.json)
- mcp.json configuration
- .env.local template
- Provisioning and testing instructions

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
- Test with more specific queries

````


## Template References

Detailed templates in `templates/mcp-create-declarative-agent/`:
- `mcp_server_integration.md`
- `requirements.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
