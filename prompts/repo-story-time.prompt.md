---
trigger: repo-story-time
name: repo-story-time
title: "Repository Analysis: Story from Git History"
description: >
  Generate a comprehensive repository summary and narrative story from
  commit history. Produces REPOSITORY_SUMMARY.md and THE_STORY_OF_THIS_REPO.md.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, repos, documentation, analysis]
dependencies:
  - skill:code-wiki
  - skill:writing-clearly-and-concisely
skills:
  - code-wiki — Generate wiki docs + diagrams for any codebase
  - writing-clearly-and-concisely — Edit documentation for clarity
metadata:
  hermes:
    related_skills:
      - code-wiki
      - writing-clearly-and-concisely
---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.

## Goal

Transform any repository's git history into two deliverables:
1. **REPOSITORY_SUMMARY.md** — Technical architecture and purpose overview
2. **THE_STORY_OF_THIS_REPO.md** — Narrative story from commit history analysis

## Workflow

### Phase 1: Repository Exploration

```bash
git log --oneline --since="1 year ago" | wc -l        # commit count
git shortlog -sn                                       # contributor stats
git diff --stat origin/main..HEAD | tail -3            # recent changes
ls -la projects/<name>/src                             # structure overview
```

### Phase 2: Analysis

- Identify tech stack, key components, data flow
- Extract contributor patterns, seasonal activity, major themes
- Cross-reference with AGENTS.md and README.md for context

### Phase 3: Write Files

Create both markdown files at the repo root using `write_file`:

| File | Content |
|------|---------|
| `REPOSITORY_SUMMARY.md` | Overview, Architecture, Key Components, Technologies, Data Flow, Team |
| `THE_STORY_OF_THIS_REPO.md` | Year-in-numbers, Contributors, Seasonal Patterns, Themes, Plot Twists, Current Chapter |

## Rules

1. **Be Specific** — Use actual file names, commit messages, and contributor names.
2. **Evidence-Based** — Support observations with actual git data (never fabricate).
3. **Write files, don't print content** — Use `write_file` to create the actual files.
4. **Balance narrative with technical accuracy** — Make it readable for non-technical audiences.

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
