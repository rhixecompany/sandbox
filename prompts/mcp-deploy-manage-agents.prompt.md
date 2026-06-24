---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Deploy and Manage MCP-Based Agents
name: mcp-deploy-manage-agents
description: "mcp-deploy-manage-agents.prompt"
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

> ### Published by Organization
> - Built with predefined instructions and actions

> **Full content:** `templates/mcp-deploy-manage-agents/agent_types.md`

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
- View agent details (name, creator, date, host products, status)

**Deploy Agents**
Options for distribution:
1. **Agent Store**: Submit to Partner Center for validation and public availability
2. **Organization Deployment**: IT admin deploys to all or selected employees

**Manage Agent Lifecycle**
- **Publish**: Make agent available to organization
- **Deploy**: Assign to specific users or groups
- **Block**: Prevent agent from being used
- **Remove**: Delete agent from organization

**Configure Access**
- Set availability for specific user groups
- Manage permissions per agent
- Control which agents appear in Copilot

## Deployment Workflows

> ### Publish to Organization
> **For Agent Developers:**

> **Full content:** `templates/mcp-deploy-manage-agents/deployment_workflows.md`

## User Experience

### Agent Discovery
Users find agents in:
- Microsoft 365 Copilot hub
- Agent picker in Copilot interface
- Organization's agent catalog

### Agent Access Control
Users can:
- Toggle agents on/off during interactions
- Add/remove agents from their experience
- Right-click agents to manage preferences
- Only access admin-allowed agents

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
- Agent adoption rates
- User feedback and satisfaction
- Error rates and performance
- Security incidents or violations

## MCP-Specific Management

### MCP Agent Characteristics
- Connect to external systems via Model Context Protocol
- Use tools exposed by MCP servers
- Require OAuth 2.0 or SSO authentication
- Support same governance as REST API agents

### MCP Agent Validation
Verify:
- MCP server URL is accessible
- Authentication configuration is secure
- Tools imported are appropriate
- Response data doesn't expose sensitive info
- Server follows security best practices

### MCP Agent Deployment
Same process as REST API agents:
1. Review in admin center
2. Validate MCP server compliance
3. Test authentication flow
4. Deploy to users/groups
5. Monitor performance

## Agent Settings and Configuration

### Organizational Settings
Configure at tenant level:
- Enable/disable agent creation
- Set default permissions
- Configure approval workflows
- Define compliance policies

### Per-Agent Settings
Configure for individual agents:
- Availability (on/off)
- User assignment (all/groups/individuals)
- Permission scopes
- Usage limits or quotas

### Environment Routing
For Power Platform-based agents:
- Configure default environment
- Enable environment routing for Copilot Studio
- Manage flows via Power Platform admin center

## Shared Agent Management

### View Shared Agents
Admins can see:
- List of all shared agents
- Creator information
- Creation date
- Host products
- Availability status

### Manage Shared Agents
Admin actions:
- Search for specific shared agents
- View agent capabilities
- Block unsafe or non-compliant agents
- Monitor agent lifecycle

### User Access to Shared Agents
Users access through:
- Microsoft 365 Copilot on various surfaces
- Agent-specific tasks and assistance
- Creator-defined capabilities

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

- [Microsoft 365 admin center](https://admin.microsoft.com/)
- [Power Platform admin center](https://admin.powerplatform.microsoft.com/)
- [Partner Center](https://partner.microsoft.com/) for agent submissions
- [Microsoft Agent 365 Overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)
- [Agent Registry Documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry)

## Workflow

Ask the user:
1. Is this agent ready for deployment or still in development?
2. Who should have access (all users, specific groups, individuals)?
3. Are there compliance or security requirements to address?
4. Should this be published to the organization or the public store?
5. What monitoring and reporting is needed?

Then provide:
- Step-by-step deployment guide
- Admin center configuration steps
- User assignment recommendations
- Governance and compliance checklist
- Monitoring and reporting plan

````


## Template References

Detailed templates in `templates/mcp-deploy-manage-agents/`:
- `agent_types.md`
- `deployment_workflows.md`
