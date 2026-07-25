---
author: Hermes Agent
description: Use when determining the least-privilege Azure RBAC role for a set of
  desired permissions. Use during access reviews, onboarding, or when assigning permissions
  to identities.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: azure-role-selector
tags:
- azure
- rbac
- security
- iam
- least-privilege
title: Azure Role Selector
version: 1.0.0

---
# Azure Role Selector

## Overview

Determine the least-privilege Azure RBAC (Role-Based Access Control) role that matches a set of desired permissions. This skill helps assign the minimal role needed — no more, no less.

## When to Use

- Assigning Azure RBAC roles to users, groups, or service principals
- Determining the least-privilege role for a set of permissions
- Reviewing existing role assignments for over-privilege
- Planning access for new team members or applications
- Converting custom roles to built-in roles where possible

## When NOT TO USE

- Auditing existing role assignments (use rbac-audit-logging)
- Visualizing resource topology (use azure-resource-visualizer)
- Creating custom roles (use Azure Portal or CLI directly)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `rbac-audit-logging` | Audit existing role assignments |
| `azure-resource-visualizer` | Map resource relationships |

## Workflow

### Phase 1: Identify Required Permissions

1. List the specific actions the identity needs:
   - Read resources? Write? Delete?
   - Which resource types? (VMs, storage, databases, etc.)
   - At what scope? (subscription, resource group, individual resource)

2. Document the permission requirements:
   ```
   Need: Read VM list, Start/Stop VMs
   Scope: Resource Group "production-vms"
   Identity: dev-team@company.com
   ```

### Phase 2: Find Matching Built-in Roles

```bash
# List all built-in roles
az role definition list --output table

# Search for roles with specific permissions
az role definition list --query "[?permissions[0].actions[] | contains(@, 'Microsoft.Compute/virtualMachines/read')]" --output table

# Get details of a specific role
az role definition list --name "Virtual Machine Contributor" --output json
```

Common built-in roles by use case:

| Use Case | Built-in Role | Scope |
|----------|--------------|-------|
| Read-only access | Reader | Any |
| VM management | Virtual Machine Contributor | RG or resource |
| Storage management | Storage Account Contributor | RG or resource |
| Database admin | SQL DB Contributor | RG or resource |
| Full resource management | Contributor | RG (avoid subscription) |
| Security admin | Security Admin | Subscription |
| Billing | Billing Reader | Subscription |

### Phase 3: Apply Least Privilege

1. Start with the most restrictive role that covers all required permissions
2. If no single role matches, combine roles at different scopes
3. Prefer resource group scope over subscription scope
4. Prefer resource scope over resource group scope
5. Only use custom roles as a last resort

### Phase 4: Assign the Role

```bash
# Assign role to a user at resource group scope
az role assignment create \
  --assignee dev-team@company.com \
  --role "Virtual Machine Contributor" \
  --resource-group production-vms

# Assign role to a service principal at resource scope
az role assignment create \
  --assignee-object-id <sp-object-id> \
  --role "Storage Blob Data Reader" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<account>

# Verify the assignment
az role assignment list --assignee dev-team@company.com --output table
```

## Verification Checklist

- [ ] All required permissions identified
- [ ] Built-in role found that covers requirements
- [ ] Scope is as narrow as possible (resource > RG > subscription)
- [ ] Role assignment created and verified
- [ ] No over-privilege (identity can't do more than needed)

## Pitfalls

- **Owner/Contributor at subscription level:** These are almost never appropriate — scope down
- **Custom roles over built-in:** Built-in roles are maintained by Microsoft — prefer them
- **Ignoring scope inheritance:** Child resources inherit parent scope permissions
- **Service principals with broad roles:** SPs should have minimal permissions
- **Not reviewing regularly:** Access needs change — review role assignments quarterly
