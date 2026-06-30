---
toolsets:
  - vscode
  - execute
  - read
  - agent
  - edit
  - search
  - web
  - context7/*
  - modelcontextprotocol-servers-sequentialthinking/*
  - next-devtools/*
  - nextjs-docs-mcp/*
  - sentry/*
  - shadcn/*
  - github/*
  - github/*
  - io.github.chromedevtools/chrome-devtools-mcp/*
  - io.github.upstash/context7/*
  - playwright/*
  - vscode.mermaid-chat-features/renderMermaidDiagram
  - github.vscode-pull-request-github/issue_fetch
  - github.vscode-pull-request-github/suggest-fix
  - github.vscode-pull-request-github/searchSyntax
  - github.vscode-pull-request-github/doSearch
  - github.vscode-pull-request-github/renderIssues
  - github.vscode-pull-request-github/activePullRequest
  - github.vscode-pull-request-github/openPullRequest
  - ms-azuretools.vscode-containers/containerToolsConfig
  - prisma.prisma/prisma-migrate-status
  - prisma.prisma/prisma-migrate-dev
  - prisma.prisma/prisma-migrate-reset
  - prisma.prisma/prisma-studio
  - prisma.prisma/prisma-platform-login
  - prisma.prisma/prisma-postgres-create-database
  - todo
license: MIT
author: Hermes Agent
version: 1.0.0
title: ComicWise - Feature Implementation Guide
name: features

description: Complete feature implementation tasks for profiles, comics, chapters, bookmarks
tags:
  - backend
  - frontend
  - performance
  - prompts
  - security
  - specification
  - typescript
  - ci-cd
  - database
  - drizzle
  - github
  - nextjs
  - performance
  - planning
  - security
  - specification
  - typescript
metadata:
  hermes:
    related_skills: []
    tags:
    - features.prompt

trigger: features

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - features.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - features.prompt

## Validation Commands

```bash
# Type check all feature files
pnpm type-check

# Lint feature components
pnpm lint src/app/\(root\) src/components

# Run feature-related tests
pnpm test:unit:run tests/unit/features

# E2E test user flows
pnpm test:e2e tests/e2e/user-flows.spec.ts
```

---

## Success Criteria

- [ ] All pages accessible and responsive
- [ ] TypeScript: 0 errors (`pnpm type-check`)
- [ ] ESLint: 0 errors (`pnpm lint`)
- [ ] Tests: All passing, 80%+ coverage
- [ ] Build: Successful (`pnpm build`)
- [ ] Performance: Core Web Vitals in green

---

**Document Version:** 1.0.0 | **Last Updated:** 2026-02-01


## Template References

Detailed templates in `templates/features/`:
- `phase_2_user_profile_features.md`
- `phase_3_comic_features.md`
- `phase_4_chapter_reader.md`
- `root_pages.md`
- `server_actions_reference.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
