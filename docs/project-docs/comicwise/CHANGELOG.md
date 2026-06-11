# ComicWise — Changelog

## [0.1.0] — 2026-05-27

### Added
- Next.js 16.1.6 App Router with Turbopack
- React 19 Server Components with React Compiler
- TypeScript 5.9 strict mode
- 27 PostgreSQL database tables with Drizzle ORM
- 4 pgEnums: userRole, comicStatus, resourceEnum, actionEnum
- Authentication system with NextAuth.js v5
  - Credentials (bcryptjs)
  - GitHub OAuth
  - Keycloak OIDC
- 28 DAL files with eager loading via `.with()`
- 21 Server Action files with ActionResult pattern
- 62 shadcn/ui components
- 7 Zustand stores for client state
- 25 Zod validation schemas
- Comic browsing with genre/status/rating filtering
- Immersive chapter reader with progress tracking
- Personal recommendations based on reading history
- Bookmarks and reading list management
- Rating system (1-5 stars with aggregated averages)
- Comments and discussion on chapters
- Reading history and reading goals
- Notification system with preferences
- User profiles with customizable settings
- Admin panel with RBAC (User/Admin/Moderator)
- Admin content management (comics, chapters, images)
- Full audit trail for admin actions
- Responsive design with Tailwind CSS 4
- Dark/light theme support
- Sentry error tracking integration
- Upstash Redis rate limiting
- TanStack React Query for server state
- Image optimization with Sharp
- Docker support with multi-stage build
- CI/CD pipeline with GitHub Actions
- 260+ unit tests (Vitest)
- 45+ E2E test scenarios (Playwright)
- ESLint + Prettier code quality
- Husky pre-commit hooks
- Comprehensive project scripts (23 scripts)

### Security
- bcrypt password hashing
- Zod validation on all inputs
- CSRF protection via Server Actions
- Route protection via middleware
- Rate limiting on auth endpoints
- Soft-delete for user and comment data
- SQL injection prevention (parameterized queries)
