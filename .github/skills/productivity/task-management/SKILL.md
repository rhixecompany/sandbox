---
author: Alexa
description: Use when tracking and managing feature subtasks with status, dependencies,
  validation, and team coordination via CLI.
license: MIT
name: task-management
tags:
- imported
title: Task Management
version: 1.0.0

---
## Description

Task management CLI for tracking and managing feature subtasks with status, dependencies, and validation.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Tracking feature subtasks
- Managing task dependencies
- Monitoring task status
- Validating task completion
- Organizing complex features
- Team task coordination

## When NOT to Use

- Simple single tasks
- Real-time collaboration
- Non-task work
- Exploratory projects

## Workflow

### Phase 1: Create Tasks

- Define feature tasks
- Identify dependencies
- Set priorities
- Assign owners

### Phase 2: Track Progress

- Update task status
- Monitor dependencies
- Track blockers
- Update estimates

### Phase 3: Validate Completion

- Verify acceptance criteria
- Check dependencies resolved
- Validate quality
- Mark complete

### Phase 4: Report & Archive

- Generate reports
- Document lessons learned
- Archive completed tasks
- Plan next features

## Tools & References

- **Related Skills**: jira
- **Status Tracking**: Task states and transitions
- **Dependencies**: Task relationships and blocking

## Best Practices

- Define clear acceptance criteria
- Track dependencies
- Update status regularly
- Communicate blockers
- Validate before marking complete
- Document decisions
- Archive completed work



## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

