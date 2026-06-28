---
author: Hermes Agent
description: Use when auditing RBAC role assignments and logging configurations in
  Azure. Use during security reviews, compliance checks, or when investigating unauthorized
  access.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: rbac-audit-logging
tags:
- azure
- rbac
- security
- audit
- compliance
- iam
title: RBAC Audit Logging
version: 1.0.0

---
# RBAC Audit Logging

## Overview

Audit Azure RBAC (Role-Based Access Control) role assignments and logging configurations to ensure compliance, detect over-privileged accounts, and verify security policies. This skill provides a systematic approach to RBAC security reviews.

## When to Use

- Conducting security reviews of Azure resource access
- Auditing role assignments for compliance (SOC2, ISO 27001, etc.)
- Investigating unauthorized access or privilege escalation
- Reviewing logging configuration for audit trail completeness
- Onboarding/offboarding access verification
- Pre-deployment security validation

## When NOT to Use

- Assigning new roles (use azure-role-selector)
- Visualizing resource topology (use azure-resource-visualizer)
- Analyzing application logs (use log-analysis-and-triage)

## Workflow

### Phase 1: Inventory Role Assignments

```bash
# List all role assignments in a subscription
az role assignment list --all --output table

# List assignments for a specific resource group
az role assignment list --resource-group <rg-name> --output table

# List assignments for a specific user or service principal
az role assignment list --assignee <upn-or-object-id> --output table

# Get detailed assignment info
az role assignment show --id <assignment-id>
```

### Phase 2: Analyze Role Definitions

```bash
# List built-in roles
az role definition list --output table

# Get details of a specific role
az role definition list --name "Contributor" --output json

# List custom roles
az role definition list --custom-role-only true --output table
```

### Phase 3: Identify Risk Patterns

Check for these high-risk patterns:

| Risk Pattern | Description | Severity |
|-------------|-------------|----------|
| **Owner at subscription level** | Full control over all resources | Critical |
| **Global Admin without MFA** | Unrestricted directory access | Critical |
| **Service principal with broad roles** | Non-human account with excessive permissions | High |
| **Stale assignments** | Users/SPs no longer active but still have roles | High |
| **Custom roles with wildcard permissions** | `*` actions in custom role definitions | High |
| **Cross-tenant assignments** | External identities with resource access | Medium |
| **Missing PIM** | Permanent assignments where PIM should be used | Medium |

### Phase 4: Audit Logging Configuration

```bash
# Check if activity log is enabled
az monitor activity-log list --offset 1d --output table

# List diagnostic settings for a resource
az monitor diagnostic-settings list --resource <resource-id>

# Check Azure AD audit logs
az ad audit list --output table

# Verify Log Analytics workspace configuration
az monitor log-analytics workspace list --output table
```

### Phase 5: Generate Audit Report

Document findings:
1. Total role assignments by scope (subscription, resource group, resource)
2. High-risk assignments flagged for review
3. Stale or orphaned assignments
4. Logging configuration gaps
5. Remediation recommendations

## Verification Checklist

- [ ] All role assignments inventoried
- [ ] High-risk patterns identified and flagged
- [ ] Stale assignments documented
- [ ] Logging configuration verified
- [ ] Custom roles reviewed for least-privilege
- [ ] PIM eligibility configured where appropriate
- [ ] Audit report generated and saved

## Skills Required

| Skill | Purpose |
|-------|---------|
| `azure-role-selector` | Choose appropriate roles |
| `azure-resource-visualizer` | Map resource relationships |
| `log-analysis-and-triage` | Analyze audit logs |

## Example Audit Output

```
RBAC Audit Report — Subscription: Production
=============================================
Total role assignments: 247
  - Subscription level: 12
  - Resource group level: 89
  - Resource level: 146

High-risk findings:
  1. Owner at subscription: 3 users (should be ≤2)
  2. Contributor at subscription: 8 users (consider resource-group scope)
  3. Stale SP with Owner: sp-legacy-app (last used: 180 days ago)
  4. Custom role "Deployer" has Microsoft.Resources/subscriptions/* (too broad)

Logging gaps:
  - 3 resource groups missing diagnostic settings
  - Activity log retention: 30 days (recommend 90+)
```

## Pitfalls

- **Scope inheritance:** Child resources inherit parent scope permissions — check all levels
- **Classic vs. Azure RBAC:** Some resources use classic co-admin model — check both
- **Service principals vs. managed identities:** Managed identities are preferred for workloads
- **PIM vs. permanent:** Privileged Identity Management should be used for admin roles
- **Cross-subscription access:** Roles in management groups apply to all child subscriptions
