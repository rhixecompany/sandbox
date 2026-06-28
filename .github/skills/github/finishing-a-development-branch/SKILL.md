---
author: Alexa
description: Use when implementation is complete, all tests pass, and you need to
  decide how to integrate work — merge, PR, or cleanup.
license: MIT
name: finishing-a-development-branch
tags:
- imported
title: Finishing A Development Branch
version: 1.0.0

---
## Description

Guide completion of development work by presenting structured options for merge, PR, or cleanup. Helps decide how to integrate finished work into main codebase.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Implementation is complete and all tests pass
- Ready to integrate work into main branch
- Need to decide between merge, PR, or cleanup
- Completing feature branches
- Finishing development work

## When NOT to Use

- Work is incomplete or tests failing
- Still in active development
- Exploratory or experimental branches
- Hotfixes (use different process)

## Workflow

### Phase 1: Verify Completion

- Confirm all tests pass
- Verify implementation meets requirements
- Check code quality standards
- Review documentation

### Phase 2: Evaluate Options

- Assess merge vs PR vs cleanup
- Consider team workflow
- Check for conflicts
- Plan integration

### Phase 3: Execute Integration

- Create PR if needed
- Request reviews
- Address feedback
- Merge to main

### Phase 4: Cleanup

- Delete feature branch
- Archive work if needed
- Document decisions
- Update tracking

## Tools & References

- **Related Skills**: git-helper, requesting-code-review
- **Git Workflow**: Merge, PR, rebase strategies
- **Code Review**: PR review process

## Best Practices

- Verify all tests pass before integration
- Get code review before merging
- Use meaningful commit messages
- Clean up branches after merge
- Document integration decisions
- Keep main branch stable
- Use consistent merge strategy



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

