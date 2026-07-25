---
name: features
title: ComicWise - Feature Implementation Guide
description: Complete feature implementation tasks for profiles, comics, chapters, bookmarks
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
  - todo
scripts: []
skills: []
formatter: default
plan: ''
dependencies: []
tags:
  - frontend
  - linting
  - prompts
  - specification
  - testing
  - typescript
  - frontend
  - linting
  - prompts
  - specification
  - testing
  - typescript
trigger: /features
---

## Validation Commands```bash# Type check all feature filespnpm type-check# Lint feature componentspnpm lint src/app/\(root\) src/components# Run feature-related testspnpm test:unit:run tests/unit/features# E2E test user flowspnpm test:e2e tests/e2e/user-flows.spec.ts```---## Success Criteria- [ ] All pages accessible and responsive- [ ] TypeScript: 0 errors (`pnpm type-check`)- [ ] ESLint: 0 errors (`pnpm lint`)- [ ] Tests: All passing, 80%+ coverage- [ ] Build: Successful (`pnpm build`)- [ ] Performance: Core Web Vitals in green---**Document Version:** 1.0.0 | **Last Updated:** 2026-02-01## Template ReferencesDetailed templates in `templates/features/`:- `phase_2_user_profile_features.md`- `phase_3_comic_features.md`- `phase_4_chapter_reader.md`- `root_pages.md`- `server_actions_reference.md`