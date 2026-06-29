# 11. 📋 Phase Execution Checklists

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 11. 📋 Phase Execution Checklists

### Phase 1: Foundation

- [ ] `pnpm install` — dependencies installed
- [ ] `.env.local` — configured with `DATABASE_URL`, `AUTH_SECRET`
- [ ] `pnpm db:push` — schema applied
- [ ] `pnpm type-check` — zero errors
- [ ] `pnpm dev` — server starts on port 3000

### Phase 2: Core Features

- [ ] Auth flow (sign-in, sign-up, sign-out, session)
- [ ] Comic CRUD (DAL + Server Actions + Pages)
- [ ] Chapter CRUD with image handling
- [ ] Reading progress tracking (see `docs/dev.content.md` Section 23.2)
- [ ] Bookmark management (composite key upsert)
- [ ] Rating system (see `docs/dev.content.md` Section 23.1)
- [ ] Comment system with threading

### Phase 3: Advanced Features

- [ ] Full-text search (see `docs/dev.content.md` Section 22.4)
- [ ] Admin dashboard with RBAC
- [ ] Notification system
- [ ] Image optimization pipeline
- [ ] Batch seeding (CLI + REST API)

### Phase 4: Quality & Polish

- [ ] Unit tests — Vitest (80%+ coverage)
- [ ] E2E tests — Playwright (critical paths)
- [ ] Performance audit (Core Web Vitals)
- [ ] Security review (auth, XSS, CSRF)
- [ ] Accessibility check (WCAG 2.1 AA)

### Phase 5: Deployment

- [ ] Production build: `pnpm build`
- [ ] Sentry integration (error tracking)
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Database backup strategy
- [ ] Monitoring & alerting

### Pre-Implementation Checklist (Every Feature)

- [ ] Feature requirements are clear and documented
- [ ] Database schema is designed and validated
- [ ] Cascade delete implications understood
- [ ] N+1 query risks identified and mitigated
- [ ] Similar patterns found in codebase
- [ ] Task broken down into manageable pieces

---
