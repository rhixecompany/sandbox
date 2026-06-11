---
category: devops
title: Work On Ticket
name: work-on-ticket
description: "Use when starting work on a Jira ticket — fetching ticket details, creating git branch with ticket-based naming, and initiating task planning."
---

## work-on-ticket

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Work On Ticket operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Description

Fetch Jira ticket details, create appropriately named git branch, and initiate task planning workflow for ticket-based work. Handles git state verification, branch naming conventions, and error scenarios.

## When to Use

- Starting work on a specific Jira ticket
- Creating git branch for ticket
- Planning ticket-based work
- Organizing work by ticket
- Tracking ticket progress

## When NOT to Use

- Non-ticket work
- Simple bug fixes without tickets
- Exploratory work
- Non-Jira issue tracking

## Workflow

### Phase 1: Fetch Ticket

- Identify ticket ID
- Fetch ticket details
- Review requirements
- Understand acceptance criteria

### Phase 2: Prepare Workspace

- Verify git state
- Create feature branch
- Use ticket-based naming
- Set up environment

### Phase 3: Plan Work

- Break down ticket into tasks
- Identify dependencies
- Estimate effort
- Plan implementation

### Phase 4: Execute & Track

- Implement ticket work
- Update ticket status
- Track progress
- Link commits to ticket

## Tools & References

- **Related Skills**: jira, git-helper
- **Ticket Format**: PROJ-123
- **Branch Naming**: ticket-based conventions
- **Git**: Branch creation and management

## Best Practices

- Use ticket ID in branch name
- Link commits to ticket
- Update ticket status regularly
- Document progress
- Test before marking complete
- Get code review
- Archive completed tickets
