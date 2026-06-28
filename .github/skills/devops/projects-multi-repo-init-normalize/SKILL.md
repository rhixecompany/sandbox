---
name: projects-multi-repo-init-normalize
title: "Multi-Repo Init + Normalize"
description: "Use when bringing multiple project repos into a sandbox workspace: finish git setup, set remotes, initialize, normalize branch model, and verify."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [git, multi-repo, init, normalize, workspace]
metadata:
  hermes:
    tags: [imported]
---
# Multi-Repo Init + Normalize

## Overview

Finish git setup for multiple project directories and normalize branch layout across a workspace.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `git-helper` | Git operations and branch management |
| `github` | GitHub repo operations and default branch settings |
- A workspace has many project folders without working trees
- Local `.git` is missing but a manifest/`.gitmodules` mapping exists
- Need consistent `production`/`development` branches across repos

## Repo List Shape
```
projects/
  Banking
  comicwise
  cookiecutter-django-tailwind
  Django-Scrapy-Selenium
  ecom
  profile
  Python-projects
  rhixe_scans
  rhixecompany-comics
  selenium_webdriver
  university-libary-jsm
  xamehi
  xamehi.tv
  youtube-downloader
```

## Workflow
### Phase 1: Initialize
For each project or mapped batch:
- `git init`
- `git remote add origin <url>`
- `git add -A`
- `git commit -m "chore: setup <project>"`

### Phase 2: Push Initial State
- `git push -u origin HEAD`
Confirm with `git branch -r`.

### Phase 3: Normalize
Per project:
1. Confirm source branch: prefer `master`, then `main`.
2. `git checkout -b production`
3. `git push -u origin production`
4. Set GitHub default:
   - With gh:
     ```
     OWNER_REPO=$(git remote get-url origin | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
     gh api "repos/$OWNER_REPO" -X PATCH -f default_branch=production
     ```
5. `git checkout -b development`
6. `git push -u origin development`
7. Optional: delete other branches.

### Phase 4: Verify
Check per project:
- `.git` exists
- Remote prints expected URL
- `origin/master` or expected source shows
- `production` and `development` exist

## Pitfalls
- Never normalize across all target repos unless every project is explicitly listed.
- Batch loops with URL expansion can fail for mixed owner/repo formats; prefer explicit project lists.
- Set remote default before deleting default branch.

## Related Skills
- git-helper
- github-pr-workflow
- github-issues

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

