---
author: Hermes Agent
description: Use when receiving code review feedback, before implementing suggestions.
  Requires technical rigor and verification, not blind implementation.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: receiving-code-review
tags:
- code-review
- feedback
- collaboration
- quality
title: Receiving Code Review
version: 1.0.0

---
# Receiving Code Review

## Overview

Process code review feedback with technical rigor — evaluate suggestions critically, verify against requirements, and implement changes thoughtfully. This skill ensures you don't blindly accept feedback or dismiss valid concerns.

## When to Use

- Receiving code review feedback on a pull request
- Evaluating suggestions before deciding to implement
- Clarifying unclear review comments
- Challenging technically questionable feedback
- Deciding between alternative approaches suggested by reviewers

## When NOT TO USE

- Accepting all feedback without evaluation
- Implementing changes without understanding the reasoning
- Dismissing all feedback defensively
- Real-time pair programming (use requesting-code-review for async review)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `requesting-code-review` | Understand the review process |
| `systematic-debugging` | Verify feedback against actual behavior |

## Workflow

### Phase 1: Read & Understand

1. Read ALL review comments before responding
2. For each comment, identify:
   - **The issue:** What problem is being raised?
   - **The suggestion:** What change is being proposed?
   - **The severity:** Is this a blocker, suggestion, or nit?

### Phase 2: Evaluate Each Suggestion

For each piece of feedback, classify:

| Classification | Criteria | Action |
|---------------|----------|--------|
| **Must fix** | Bug, security issue, incorrect behavior | Implement immediately |
| **Should fix** | Best practice, significant improvement | Implement unless strong counterargument |
| **Consider** | Style preference, alternative approach | Evaluate trade-offs, discuss if needed |
| **Decline** | Incorrect understanding, out of scope | Respond with explanation |

### Phase 3: Respond & Implement

1. **Accept valid feedback:**
   ```bash
   git add .
   git commit -m "fix: address review feedback - [specific change]"
   ```

2. **Discuss questionable feedback:**
   - Respond with specific technical reasoning
   - Provide evidence (tests, docs, benchmarks)
   - Propose an alternative if applicable
   - Be respectful — the reviewer may have context you don't

3. **For disagreements:**
   - Don't argue in comments — schedule a sync
   - Bring data, not opinions
   - Accept if the reviewer has final authority

### Phase 4: Verify Changes

1. After implementing, verify:
   ```bash
   npm test  # or equivalent
   ```
2. Respond to each comment indicating it's addressed
3. Request re-review if significant changes were made

## Verification Checklist

- [ ] All review comments read and classified
- [ ] Each comment responded to (accepted, discussed, or declined with reasoning)
- [ ] Changes implemented and tested
- [ ] Reviewer notified of changes
- [ ] No comments left unaddressed

## Pitfalls

- **Blind implementation:** Don't accept feedback without understanding why
- **Defensive dismissal:** Don't reject feedback just because it's critical
- **Ignoring context:** The reviewer may know about requirements you don't
- **Forgetting to reply:** Always respond to comments even if just "Done"
- **Mixing refactoring:** Don't mix review fixes with unrelated refactors in the same PR
- **Not learning:** Patterns in review feedback indicate areas for skill improvement
