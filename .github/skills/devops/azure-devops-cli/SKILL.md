---
author: Hermes Agent
description: Use when working with Azure DevOps resources via Azure CLI — repos, pipelines,
  boards, artifacts, service endpoints, and project administration.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: azure-devops-cli
tags:
- azure
- devops
- cli
- pipelines
- repos
- boards
- artifacts
title: Azure DevOps CLI
version: 1.0.0

---
# Azure DevOps CLI

## Overview

Manage Azure DevOps resources via `az` CLI after installing the Azure DevOps extension. Use this skill for projects, repos, pipelines, PRs, work items, artifacts, service endpoints, and administration tasks.

## When to Use

- Managing Azure DevOps organizations or projects
- Automating repo, pipeline, or work-item operations
- Creating PRs and configuring pipeline artifacts
- Administering service endpoints, permissions, or teams
- Troubleshooting Azure DevOps auth or extension issues

## When NOT to Use

- Non-Azure Git platforms
- One-off Git commands without Azure DevOps context
- Local-only Git workflows that don’t touch Azure DevOps

## Skills Required

| Skill | Purpose |
|-------|---------|
| `git-helper` | Branching and repository operations outside CLI-specific flows |
| `task-management` | Track work-item and pipeline tasks |

## Workflow

### Phase 1: Install and Configure

```bash
# Install Azure CLI
brew install azure-cli

# Install Azure DevOps extension
az extension add --name azure-devops
az extension show --name azure-devops

# Configure organization and project defaults
az devops configure --defaults organization=https://dev.azure.com/{org} project={project}
```

### Phase 2: Manage Repos and PRs

```bash
# Create repo
az repos create --name myapp --project MyProject

# Create PR
az repos pr create \
  --repository myapp \
  --source-branch feature/login \
  --target-branch main \
  --title "feat: login flow" \
  --description "Adds login form and validation"

# List PRs
az repos pr list --repository myapp --status active --output table
```

### Phase 3: Manage Pipelines

```bash
# List pipelines
az pipelines list --output table

# Run pipeline
az pipelines run --name MyPipeline --branch main --open

# View artifact
az pipelines runs artifact list --run-id {run-id}
```

### Phase 4: Projects and Boards

```bash
# Create project
az devops project create \
  --name MyNewProject \
  --organization https://dev.azure.com/{org} \
  --source-control git \
  --visibility private

# View work item
az boards work-item show --id 123
```

### Phase 5: Service Endpoints and Permissions

```bash
# List service endpoints
az devops service-endpoint list --project MyProject

# List security groups
az devops security group list --project MyProject
```

## Verification Checklist

- [ ] Azure CLI and Azure DevOps extension installed
- [ ] Organization and project defaults configured
- [ ] Repo or pipeline operation completed successfully
- [ ] PR or work item updated as intended
- [ ] Service endpoint or permission change verified
- [ ] Commands run against expected org and project

## Pitfalls

- Missing org or project defaults causes failed runs.
- PAT-based login may require reauthentication after expiry.
- Avoid broad permission changes without security review.
- Avoid cloning or editing extraneous template content.
