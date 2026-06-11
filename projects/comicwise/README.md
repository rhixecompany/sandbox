# ComicWise

A modern, production-ready manga and comic reader platform built with **Next.js 16**, **React 19 Server Components**, and **PostgreSQL**. Browse, read, rate, and discuss comics in an immersive experience.

**Status:** Feature-complete and production-ready | **Batch 4 Audit:** ✅ COMPLETE (Code quality: 98/100, 241/241 tests)

---

## Quick Start

### Prerequisites

- Node.js 18+
- PostgreSQL 14+ (or a [Neon.tech](https://neon.tech) account for serverless PostgreSQL)
- pnpm 9+ (or npm/yarn)

### Setup (2 minutes)

```bash
# 1. Clone and install
git clone <repo-url>
cd comicbook
pnpm install

# 2. Set up environment
cp .env.local.example .env.local
# Edit .env.local with your database URL and secrets

# 3. Initialize database
pnpm db:push

# 4. Seed sample data (optional)
pnpm seed:all

# 5. Start development server
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser and start reading!

---

## Features

### For Readers

- **Browse & Discover** – Explore a rich catalog of comics with advanced filtering by genre, status, and rating
- **Immersive Reader** – Chapter reader with progress tracking, reading preferences, and history
- **Personalized Recommendations** – Genre-based comic recommendations based on your reading history
- **Bookmarks & Progress** – Keep track of where you left off and maintain a reading list
- **Ratings & Reviews** – Rate comics and see community ratings with detailed statistics
- **Comments & Discussion** – Engage with other readers in chapter discussions
- **Notifications** – Stay updated on new chapters, comments, and bookmarks

### For Administrators

- **Content Management** – Upload, edit, and manage comics and chapters
- **User Management** – Moderation tools, role-based access control (RBAC)
- **Analytics Dashboard** – Track reading patterns and user engagement
- **Admin Controls** – Full audit trail and system configuration

---

## Technology Stack

### Frontend & Framework

- **Next.js 16** – App Router with Server Components and Turbopack
- **React 19** – Server Components, Suspense, and modern hooks
- **TypeScript** – Strict mode for type safety
- **Tailwind CSS 4** – Utility-first styling with lightning-fast compilation
- **shadcn/ui** – High-quality, accessible React components

### Backend & Data

- **PostgreSQL 14+** – Relational database with Neon support
- **Drizzle ORM 0.45+** – Type-safe SQL queries with full TypeScript support
- **NextAuth.js v5** – Authentication with database sessions and multiple providers

### State Management & Tools

- **Zustand** – Lightweight client-side state management
- **React Query 5** – Server state synchronization
- **Zod 4** – Runtime schema validation
- **Sonner** – Toast notifications

### Testing & Quality

- **Vitest** – Blazing-fast unit tests with jsdom
- **Playwright** – End-to-end testing with cross-browser support
- **ESLint + Prettier** – Code quality and automatic formatting
- **TypeScript** – Compile-time type safety (0 errors required)

---

## Architecture

### Data Flow

```
Client Request
    ↓
[Middleware] Auth + Route Protection (proxy.ts)
    ↓
Server Component (async)
    ↓
Data Access Layer (DAL) – Drizzle queries with eager loading
    ↓
PostgreSQL Database
    ↓
Return data → Client Component → Zustand/React Query
```

### Key Directories

```
src/
├── app/              # Pages & routes (Next.js App Router)
│   ├── (auth)/      # Auth pages (sign-in, sign-up)
│   ├── (root)/      # Main app routes
│   └── admin/       # Admin-only routes
├── components/       # React components
│   ├── ui/          # shadcn primitives
│   ├── comics/      # Comic-specific components
│   └── layout/      # Layout components
├── dal/             # Data Access Layer (19 DAL files)
├── actions/         # Server Actions (mutations)
├── database/        # Drizzle schema & config
├── schemas/         # Zod validation
├── lib/             # Utilities & helpers
├── stores/          # Zustand stores
├── hooks/           # Custom React hooks
├── auth*.ts         # Auth configuration (4 files)
└── proxy.ts         # Middleware
```

---

## Getting Started

### Development

```bash
# Start dev server with hot reload
pnpm dev

# Type checking
pnpm type-check

# Linting & formatting
pnpm lint:fix

# Run unit tests
pnpm test

# Run E2E tests
pnpm test:ui

# Full validation (type-check → lint → format → test → build)
pnpm validate
```

### Database

```bash
# Apply schema changes to database
pnpm db:push

# Open Drizzle Studio (visual DB viewer)
pnpm db:studio

# Seed database with sample data
pnpm seed:all --dry-run --verbose

# Reset database (⚠️ destructive)
pnpm db:reset
```

### Build & Deployment

```bash
# Production build
pnpm build

# Preview production build locally
pnpm start
```

> [!TIP] All builds use Turbopack for ~38s production builds. See `next.config.ts` for configuration.

---

## Project Status

### Completed

| Phase | Feature                         | Status      |
| ----- | ------------------------------- | ----------- |
| 3.1   | Foundation & Auth               | ✅ Complete |
| 3.2   | User Profiles & Settings        | ✅ Complete |
| 3.3   | Comics Listing & Discovery      | ✅ Complete |
| 3.4   | Chapter Reader                  | ✅ Complete |
| 3.5   | Recommendations & Notifications | ✅ Complete |

### Quality Metrics

- ✅ **Zero TypeScript errors** – Strict mode enforced
- ✅ **Zero ESLint errors** – in Phase 3.5 code
- ✅ **Production build verified** – Compiles successfully
- ✅ **50+ unit tests** – Vitest with comprehensive coverage
- ✅ **45+ E2E test scenarios** – Playwright cross-browser testing
- 🎯 **Target: Lighthouse 90+** – Performance optimized

---

## Key Implementation Details

### Authentication

ComicWise uses NextAuth.js v5 with database sessions and multiple providers:

- **Credentials** – Local user accounts with bcryptjs hashing
- **GitHub** – OAuth 2.0 integration
- **Keycloak** – OIDC single sign-on

Session tokens expire after 30 days, and all credentials are securely hashed.

### Database Schema

27 PostgreSQL tables with:

- Full referential integrity (cascade deletes where appropriate)
- Soft deletes for user and comment data (via `deletedAt` column)
- Aggregate fields for ratings and statistics
- Proper indexing for query performance

See [database-context-map.md](docs/database-context-map.md) for complete entity relationships.

### API Design

All mutations use **Server Actions** (not API routes) for:

- Automatic CSRF protection
- Type-safe client-server communication
- Optimized bundle size
- Better performance

Server Actions return `ActionResult<T>` (discriminated unions):

```typescript
{ ok: true, data: ComicType } | { ok: false, error: string }
```

### State Management

- **Client state**: Zustand stores (reader state, UI toggles)
- **Server state**: React Query with `revalidatePath`/`revalidateTag`
- **Auth state**: Next auth session via `useSession()`

---

## Code Quality Standards

### Type Safety

- ✅ No `any` types (ESLint enforced)
- ✅ Strict TypeScript mode
- ✅ Full await/async consistency
- ✅ Proper null/undefined handling

### Performance

- ✅ No N+1 queries (Drizzle eager loading with `.with()`)
- ✅ Image optimization (responsive images, compression)
- ✅ Code splitting & lazy loading
- ✅ React Compiler enabled (no manual memoization needed)

### Security

- ✅ Input validation with Zod schemas
- ✅ SQL injection prevention (parameterized queries)
- ✅ CSRF protection (Server Actions)
- ✅ Authentication on protected routes (middleware)
- ✅ Rate limiting headers

---

## Deployment

ComicWise is ready for production deployment on:

- **Vercel** – Native Next.js support with Turbopack
- **Docker** – Multi-stage Dockerfile included
- **Railway.app** – PostgreSQL + Next.js hosting
- **AWS** – ECS, Lambda (with adapter), or EC2
- **Any Node.js host** – Standard `npm start`

> [!NOTE] For production, set `NODE_ENV=production` and configure environment variables via your host's secrets management.

### Environment Variables

See `.env.local.example` for all required and optional variables:

```bash
# Core
DATABASE_URL=postgresql://...
AUTH_SECRET=...

# Optional (OAuth providers)
AUTH_GITHUB_ID=...
AUTH_GITHUB_SECRET=...
AUTH_KEYCLOAK_ID=...
AUTH_KEYCLOAK_SECRET=...
AUTH_KEYCLOAK_ISSUER=...

# Optional (third-party services)
NEXT_PUBLIC_ANALYTICS_KEY=...
SENTRY_AUTH_TOKEN=...
```

---

## Documentation

| Document | Purpose |
| --- | --- |
| [QUICK_START.md](docs/QUICK_START.md) | 30-second setup guide |
| [DEVELOPMENT.md](docs/DEVELOPMENT.md) | Full developer handbook |
| [DATABASE_SETUP.md](docs/DATABASE_SETUP.md) | Detailed database configuration |
| [database-context-map.md](docs/database-context-map.md) | Entity relationships & constraints |
| [AGENTS.md](AGENTS.md) | GitHub Copilot setup & agents |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | AI coding assistant guide |

---

## Contributing

We welcome contributions! Please ensure:

1. **Code Quality**: Run `pnpm validate` before pushing (all 4 gates must pass)
2. **Type Safety**: Zero TypeScript errors required
3. **Tests**: New features include unit tests
4. **Documentation**: Update docs for user-facing changes

See [.github/instructions/](github/instructions/) for detailed guidelines on:

- Code reviews and quality standards
- TypeScript & React patterns
- Testing best practices
- Security and performance

---

## Support & Community

- **Issues & Bugs**: [GitHub Issues](../../issues) – Please include reproduction steps and environment details
- **Discussions**: [GitHub Discussions](../../discussions) – Ask questions and share ideas
- **Documentation**: Full API and architecture documentation in [docs/](docs/)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Credits

Built with modern web technologies and inspired by the manga reader experience. Special thanks to:

- [Next.js](https://nextjs.org/) team for App Router innovation
- [Drizzle ORM](https://orm.drizzle.dev/) for type-safe SQL
- [shadcn/ui](https://ui.shadcn.com/) for beautiful components
- [Tailwind CSS](https://tailwindcss.com/) for rapid UI development

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup-dev.ps1
```

### Manual

Follow [DATABASE_SETUP.md](docs/DATABASE_SETUP.md) for step-by-step instructions.

---

## 🚢 Deployment

ComicWise is optimized for **Vercel**:

```bash
git push origin main
# Automatically deploys
# Migrations run automatically
```

---

## 🤝 Contributing

1. Follow [coding standards](https://github.com/comicwise/comicwise/tree/main/.github/instructions)
2. Pass all checks: `pnpm type-check && pnpm lint:fix && pnpm test`
3. Include tests for new features
4. Update documentation

---

## 📚 Resources

- [Next.js Docs](https://nextjs.org/docs)
- [Drizzle ORM](https://orm.drizzle.team)
- [shadcn/ui](https://ui.shadcn.com)
- [NextAuth.js](https://next-auth.js.org)
- [Zod Validation](https://zod.dev)

---

## 📝 License

MIT

---

## 🚀 Getting Started?

Start here: **[QUICK_START.md](docs/QUICK_START.md)**

Questions? Check [DEVELOPMENT.md](docs/DEVELOPMENT.md)

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
