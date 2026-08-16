---
name: github-workflows
title: GitHub Workflows (umbrella)
description: "Use when working with GitHub: auth, issues, PRs, review."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Pull-Requests, Issues, Code-Review, Authentication, Git, CI]
    related_skills: [systematic-debugging, test-driven-development, repo-management]
---

# GitHub Workflows (umbrella)

Class-level skill for every GitHub interaction: authentication, issue
management, issue-to-PR delivery, the PR lifecycle (branch → CI → merge), and
code review. Every workflow has a `gh` CLI path and a REST/curl fallback for
machines without `gh`. Absorbed 2026-08-11: github-auth, github-issues,
github-issue-to-pr, github-pr-workflow, github-code-review.

## When to Use

- Any task touching GitHub: auth setup, issues, PRs, reviews, CI,
  "fix issue #N and open a PR".
- Start here instead of hunting for per-workflow skills.

## Workflow Sections

| Section | Detail |
|---|---|
| 1. Shared setup | `references/shared-setup.md` — auth-method detection + repo coordinates (also `scripts/gh-env.sh`) |
| 2. Authentication | `references/auth-setup.md` — PAT / SSH key / gh login, troubleshooting |
| 3. Issues | `references/issues.md` + `templates/bug-report.md`, `templates/feature-request.md` |
| 4. Issue → PR | `references/issue-to-pr.md` — end-to-end delivery discipline |
| 5. PR lifecycle | `references/pr-lifecycle.md` + `references/ci-troubleshooting.md`, `references/conventional-commits.md`, `templates/pr-body-*.md` |
| 6. Code review | `references/code-review.md` + `references/review-output-template.md` |
| Scripts | `scripts/gh-env.sh`, `scripts/git-credential-token.py` |

## Pitfalls

- Set up authentication before any workflow; run `scripts/gh-env.sh` first and
  confirm the detected method.
- Verify claimed states (CI green, merged, closed) from live tool output — never
  from assumption.
- A regression test that passes without the fix proves nothing (sabotage run).
- Fix the whole bug class at sibling call sites, not one instance.

## Verification Checklist

- [ ] Auth method detected and owner/repo resolved before acting
- [ ] Issue/PR state changes verified via live output
- [ ] CI state reported from live evidence only
- [ ] Review verdict matches findings (approve only when clean)

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
