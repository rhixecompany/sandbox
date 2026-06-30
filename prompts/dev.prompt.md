---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Task1
name: dev
description: "The purpose of the prompt is to get my codebase optimized and refactored"
tags:
  - configuration
  - debugging
  - performance
  - playwright
  - prompts
  - refactoring
  - testing
  - typescript
  - authentication
  - ci-cd
  - debugging
  - github
  - nextjs
  - performance
  - playwright
  - refactoring
  - security
  - typescript
metadata:
  hermes:
    related_skills: []
    tags:
    - dev.prompt

trigger: dev

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - dev.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - dev.prompt

## Phase 1

# Task1

- list all test in src/backuptests and src/tests then triage
- if test already exists, merge intelligently - preserve valuable content while updating outdated sections
- Delete src/backuptests and modify playwright.config.mts and vitest.config.mts for this project
- modify src/actions/auth.actions.ts to include a custom signOut function
- modify src/components/layout/navbar.tsx,src/components/layout/navbar-client.tsx,src/components/layout/nav-user.tsx,src/components/layout/nav-secondary.tsx,src/components/layout/nav-main.tsx,src/components/layout/nav-documents.tsx,src/components/layout/app-sidebar.tsx,src/components/layout/site-header.tsx to handle both authenticated and unauthenticated users with next-auth
- list all pages in src/apps and triage
- for each page in the list of pages in src/apps modify all of them to use actions in src/actions not dal in src/actions, create a corresponding vitest for all actions and a corresponding playwright test for all pages all test must be basic with valid page navigation and displaying information skip all pages that need authentication in this phase ensure all vitest and playwright test run successfully if a test fails debug by executing the individual failing test

# Task2

- for each page in the list of pages in src/apps that need authentication create a corresponding playwright test, test must be basic with valid page navigation and displaying information ensure all vitest and playwright test run successfully if a test fails debug by executing the individual failing test


## Template References

Templates in `templates/dev/`:
- `phase_1.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
