---
name: mcp-deploy-manage-agents
title: Deploy and Manage MCP-Based Agents
description: mcp-deploy-manage-agents.prompt.
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
plan: null
tags:
- agents
- deployment
- mcp
- ml
- prompts
- specification
- typescript
- workflow
- agents
- deployment
- mcp
- ml
- prompts
- specification
- typescript
- workflow
trigger: /mcp-deploy-manage-agents
dependencies: []
metadata:
  hermes: {}
---

## Goal

Use this prompt to handle the deploy and manage mcp based agents workflow.

## Context

Use when you need to deploy and manage mcp based agents for the current workspace or task.

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

## Agent Types

### Published by Organization

> - Built with predefined instructions and actions

## Admin Roles and Permissions

### Required Roles

- **AI Admin**: Full agent management capabilities
- **Global Reader**: View-only access (no editing)

### Best Practices

- Use roles with fewest permissions
- Limit Global Administrator to emergency scenarios
- Follow principle of least privilege

## Agent Management in Microsoft 365 Admin Center

### Access Agent Management

1. Go to [Microsoft 365 admin center](https://admin.microsoft.com/)
2. Navigate to **Agents** page
3. View available, deployed, or blocked agents

### Available Actions

**View Agents**

- Filter by availability (available, deployed, blocked)
- Search for specific agents
- View agent details (name, creator, date, host products, status)**Deploy Agents**Options for distribution:1. **Agent Store**: Submit to Partner Center for validation and public availability2. **Organization Deployment**: IT admin deploys to all or selected employees**Manage Agent Lifecycle**
- **Publish**: Make agent available to organization
- **Deploy**: Assign to specific users or groups
- **Block**: Prevent agent from being used
- **Remove**: Delete agent from organization**Configure Access**
- Set availability for specific user groups
- Manage permissions per agent
- Control which agents appear in Copilot

## Deployment Workflows

### Publish to Organization

> **For Agent Developers:**

## User Experience

### Agent Discovery

Users find agents in:

- Microsoft 365 Copilot hub- Agent picker in Copilot interface- Organization's agent catalog

### Agent Access Control

Users can:

- Toggle agents on/off during interactions- Add/remove agents from their experience- Right-click agents to manage preferences- Only access admin-allowed agents

### Agent Usage

- Agents appear in Copilot sidebar
- Users select agent for context
- Queries routed through selected agent
- Responses leverage agent's capabilities

## Governance and Compliance

### Security Considerations

- **Data access**: Review what data agent can access
- **API permissions**: Validate required scopes
- **Authentication**: Ensure secure OAuth flows
- **External connections**: Assess risk of external integrations

### Compliance Requirements

- **Data residency**: Verify data stays within boundaries
- **Privacy policies**: Review agent privacy statement
- **Terms of use**: Validate acceptable use policies
- **Audit logs**: Monitor agent usage and activity

### Monitoring and Reporting

Track:

- Agent adoption rates- User feedback and satisfaction- Error rates and performance- Security incidents or violations

## MCP-Specific Management

### MCP Agent Characteristics

- Connect to external systems via Model Context Protocol
- Use tools exposed by MCP servers
- Require OAuth 2.0 or SSO authentication
- Support same governance as REST API agents

### MCP Agent ValidationVerify:

- MCP server URL is accessible- Authentication configuration is secure- Tools imported are appropriate- Response data doesn't expose sensitive info- Server follows security best practices

### MCP Agent Deployment

Same process as REST API agents:1. Review in admin center2. Validate MCP server compliance3. Test authentication flow4. Deploy to users/groups5. Monitor performance

## Agent Settings and Configuration

### Organizational Settings

Configure at tenant level:

- Enable/disable agent creation- Set default permissions- Configure approval workflows- Define compliance policies

### Per-Agent Settings

Configure for individual agents:- Availability (on/off)- User assignment (all/groups/individuals)- Permission scopes- Usage limits or quotas

### Environment Routing

For Power Platform-based agents:- Configure default environment- Enable environment routing for Copilot Studio- Manage flows via Power Platform admin center

## Shared Agent Management

### View Shared Agents

Admins can see:

- List of all shared agents- Creator information- Creation date- Host products- Availability status

### Manage Shared Agents

Admin actions:

- Search for specific shared agents- View agent capabilities- Block unsafe or non-compliant agents- Monitor agent lifecycle

### User Access to Shared Agents

Users access through:

- Microsoft 365 Copilot on various surfaces- Agent-specific tasks and assistance- Creator-defined capabilities

## Best Practices

### Before Deployment

- **Pilot test** with small user group
- **Gather feedback** from early adopters
- **Validate security** and compliance
- **Document** agent capabilities and limitations
- **Train users** on agent usage

### During Deployment

- **Phased rollout** to manage adoption
- **Monitor performance** and errors
- **Collect feedback** continuously
- **Address issues** promptly
- **Communicate** availability to users

### Post-Deployment

- **Track metrics**: Adoption, satisfaction, errors
- **Iterate**: Improve based on feedback
- **Update**: Keep agent current with new features
- **Retire**: Remove obsolete or unused agents
- **Review**: Regular security and compliance audits

### Communication

- Announce new agents to users
- Provide documentation and examples
- Share best practices and use cases
- Highlight benefits and capabilities
- Offer support channels

## Troubleshooting

### Agent Not Appearing

- Check deployment status in admin center
- Verify user is in assigned group
- Confirm agent is not blocked
- Check user has Copilot license
- Refresh Copilot interface

### Authentication Failures

- Verify OAuth credentials are valid
- Check user has necessary permissions
- Confirm MCP server is accessible
- Test authentication flow independently

### Performance Issues

- Monitor MCP server response times
- Check network connectivity
- Review error logs in admin center
- Validate agent isn't rate-limited

### Compliance Violations

- Block agent immediately if unsafe
- Review audit logs for violations
- Investigate data access patterns
- Update policies to prevent recurrence

## Resources

- [Microsoft 365 admin center](https://admin.microsoft.com/)- [Power Platform admin center](https://admin.powerplatform.microsoft.com/)- [Partner Center](https://partner.microsoft.com/) for agent submissions- [Microsoft Agent 365 Overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)- [Agent Registry Documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry)

## Workflow

Ask the user:1. Is this agent ready for deployment or still in development?2. Who should have access (all users, specific groups, individuals)?3. Are there compliance or security requirements to address?4. Should this be published to the organization or the public store?5. What monitoring and reporting is needed?Then provide:- Step-by-step deployment guide- Admin center configuration steps- User assignment recommendations- Governance and compliance checklist- Monitoring and reporting plan````

## Template References

Detailed templates in `templates/mcp-deploy-manage-agents/`:- `agent_types.md`- `deployment_workflows.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`mcp-create-adaptive-cards.prompt.md`](mcp-create-adaptive-cards.prompt.md)
- [`mcp-create-declarative-agent.prompt.md`](mcp-create-declarative-agent.prompt.md)
