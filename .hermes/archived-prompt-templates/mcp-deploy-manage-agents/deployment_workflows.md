# Deployment Workflows

> Extracted from `mcp-deploy-manage-agents.prompt.md`.

## Deployment Workflows

### Publish to Organization

**For Agent Developers:**
1. Build agent with Microsoft 365 Agents Toolkit
2. Test thoroughly in development
3. Submit agent for approval
4. Wait for admin review

**For Admins:**
1. Review submitted agent in admin center
2. Validate compliance and security
3. Approve for organizational use
4. Configure deployment settings
5. Publish to selected users or organization-wide

### Deploy via Agent Store

**Developer Steps:**
1. Complete agent development and testing
2. Package agent for submission
3. Submit to Partner Center
4. Await validation process
5. Receive approval notification
6. Agent appears in Copilot store

**Admin Steps:**
1. Discover agents in Copilot store
2. Review agent details and permissions
3. Assign to organization or user groups
4. Monitor usage and feedback

### Deploy Organizational Agent

**Admin Deployment Options:**
```
Organization-wide:
- All employees with Copilot license
- Automatically available in Copilot

Group-based:
- Specific departments or teams
- Security group assignments
- Role-based access control
```

**Configuration Steps:**
1. Navigate to Agents page in admin center
2. Select agent to deploy
3. Choose deployment scope:
   - All users
   - Specific security groups
   - Individual users
4. Set availability status
5. Configure permissions if applicable
6. Deploy and monitor
