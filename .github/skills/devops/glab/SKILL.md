---
name: glab
title: Glab
description: "Use when managing GitLab resources from terminal — merge requests, issues, pipelines, repositories, and CI/CD automation via GitLab CLI."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [gitlab, glab, cli, ci-cd, issues, merge-requests]
metadata:
  hermes:
    tags: [imported]
---
# Glab

## Overview

Manage GitLab resources from the terminal using the `glab` CLI. Covers merge requests, issues, pipelines, repositories, and CI/CD automation.

## When to Use

- Creating or reviewing merge requests
- Managing GitLab issues and epics
- Monitoring or triggering CI/CD pipelines
- Cloning or forking repositories
- Automating GitLab workflows
- Troubleshooting authentication

## When NOT to Use

- GitHub (use GitHub CLI instead)
- Web-based GitLab interface
- Non-GitLab repositories
- Local git operations only

## Skills Required

| Skill | Purpose |
|-------|---------|
| `git-helper` | Git operations and branching |
| `jira` | Ticket/issue management |

## Workflow

### Phase 1: Setup & Auth

```bash
# Install
brew install glab  # macOS
# or download from https://github.com/profclems/glab/releases

# Auth
glab auth login

# Verify
glab auth status
```

### Phase 2: Issues

```bash
# Create issue
glab issue create --title "Bug: login fails" --label bug

# List issues
glab issue list --assignee @me --label bug

# View issue
glab issue view 42

# Close issue
glab issue close 42
```

### Phase 3: Merge Requests

```bash
# Create MR
glab mr create --title "feat: add new endpoint" --source-branch feature/api

# Checkout MR locally
glab mr checkout 123

# Approve MR
glab mr approve 123

# Merge
glab mr merge 123 --squash
```

### Phase 4: Pipelines

```bash
# List pipelines
glab ci list

# View job logs
glab ci view 456

# Retry failed job
glab ci retry 456 --job 3
```

## Verification Checklist

- [ ] glab installed and authenticated
- [ ] Correct project/repo context set
- [ ] Issue/MR operations completed
- [ ] Pipeline access verified
- [ ] CI/CD automation tested

## Pitfalls

- **Wrong context:** Set project with `glab repo view` before operations
- **Rate limits:** CI operations can hit Lambda Labs limits
- **Auth expiry:** Re-auth if token expires
- **Self-hosted GitLab:** Must set `GITLAB_HOST` env var
