---
name: repo-story-time
...
title: 'Repository Analysis: Story from Git History'
description: Generate a comprehensive repository summary and narrative story from commit history.
  Produces REPOSITORY_SUMMARY.md and THE_STORY_OF_THIS_REPO.md.
...
version: 2.1.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - browser
- code_execution
- file
- mcp
- terminal
- web
scripts: []
skills: - code-wiki
- gh-cli
- git-commit
- writing-clearly-and-concisely
- subagent-driven-development
formatter: default
...
plan: ''
dependencies: - prompt:repo
- skill:code-wiki
- skill:gh-cli
- skill:git-commit
- skill:writing-clearly-and-concisely
- tool:mcp-github
- tool:mcp-sequential-thinking
- skill:subagent-driven-development
tags: - architecture
- generator
- git
- mcp
- ml
- prompts
- typescript
- vscode
- workflow
trigger: /repo-story-time
...
metadata: hermes:
  related_skills:
  - code-wiki
  - gh-cli
  - git-commit
  - writing-clearly-and-concisely
  - tool:mcp-github
  - tool:mcp-sequential-thinking
  related_prompts:
  - repo.prompt.md
---

## Goal

Transform any repository's git history into two deliverables:

1. **REPOSITORY_SUMMARY.md** — Technical architecture and purpose overview
2. **THE_STORY_OF_THIS_REPO.md** — Narrative story from commit history analysis

For a lighter 5-bullet summary instead of a full story, use the
**Quick Repo Onboarding** section in `repo.prompt.md` (Q1: summarize + entrypoint).

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
