---
author: Hermes Agent
description: Use when starting work on a Jira ticket — fetching ticket details, creating
  git branch with ticket-based naming, and initiating task planning.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: work-on-ticket
tags: null
title: Work On Ticket
version: 1.0.0

---
# Work On Ticket

## Overview

Start work on a Jira ticket by fetching its details, creating a properly named git branch, and kicking off a minimal planning and tracking workflow tied back to the ticket.

## When to Use

- Starting work on a tracked Jira issue
- Creating ticket-based branch names
- Ensuring ticket metadata and git work stay linked
- Beginning planning work after ticket review

## When NOT to Use

- Non-ticket work streams
- Repositories or tasks not tied to Jira
- Purely exploratory work with no tracked issue
- Historical work that cannot be tied back to the ticket

## Skills Required

| Skill | Purpose |
|-------|---------|
| jira | Fetch ticket details and update issue state |
| git-helper | Create branches and manage git workflow |

## Workflow

### Phase 1: Fetch Ticket Details

1. Identify the ticket ID.
2. Fetch ticket details and acceptance criteria.
3. Review requirements, comments, and current status.
4. Note dependencies and related tickets.

### Phase 2: Prepare Workspace

1. Verify git repository and branch state.
2. Create a feature branch using ticket-based naming.
3. Confirm working tree is clean before checkout.
4. Set local notes or todos if needed.

Example branch naming:

- `feature/PROJ-123-short-description`
- `bugfix/PROJ-456-fix-login-timeout`

### Phase 3: Plan Work

1. Break down acceptance criteria into smaller tasks.
2. Identify dependencies on other tickets or teams.
3. Estimate effort and note technical risks.
4. Plan implementation order and test coverage.

### Phase 4: Execute and Track Progress

1. Implement tasks incrementally in the branch.
2. Commit with references to the ticket in the message.
3. Update ticket status when meaningful progress is made.
4. Keep ticket metadata and commit history aligned.

## Verification Checklist

- [ ] Ticket details are fetched and understood
- [ ] Ticket-based branch is created and checked out
- [ ] Work is organized against ticket criteria
- [ ] Commits reference the ticket ID
- [ ] Ticket status and branch progress stay aligned

## Pitfalls

- Skipping ticket understanding before branching leads to wasted commits.
- Non-descriptive branch names make provenance unclear.
- Forgetting ticket references in commit messages breaks traceability.
- Continuing with an unclean working tree raises merge risk.
