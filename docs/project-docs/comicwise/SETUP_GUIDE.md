# ComicWise — Setup Guide

## Prerequisites

- **Node.js** 18+ 
- **pnpm** 9+ (or npm/yarn)
- **PostgreSQL** 14+ (or [Neon.tech](https://neon.tech) account)

## 1. Clone & Install

```bash
git clone <repo-url>
cd comicbook
pnpm install
```

## 2. Environment Variables

```bash
cp .env.local.example .env.local
```

Edit `.env.local`:

```env
# Core
DATABASE_URL=postgresql://user:*..your-local-neon-serverless
AUTH_SECRET=your-g...n

# OAuth (optional)
AUTH_GITHUB_ID=
AUTH_GITHUB_SECRET=
AUTH_KEYCLOAK_ID=
AUTH_KEYCLOAK_SECRET=
AUTH_KEYCLOAK_ISSUER=

# Third-party (optional)
NEXT_PUBLIC_ANALYTICS_KEY=
SENTRY_AUTH_TOKEN=
```

## 3. Database Setup

```bash
# Push schema
pnpm db:push

# Seed sample data (optional)
pnpm seed:all

# Open Drizzle Studio
pnpm db:studio
```

## 4. Start Development

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000).

## 5. Verify

```bash
pnpm validate
```

This runs: format:check → type-check → lint:strict → imports:check → health:all → test

## Database Commands

| Command | Purpose |
|---------|---------|
| `pnpm db:push` | Push schema to database |
| `pnpm db:generate` | Generate SQL migration |
| `pnpm db:migrate` | Run pending migrations |
| `pnpm db:studio` | Open Drizzle Studio GUI |
| `pnpm db:drop` | Drop database |
| `pnpm db:reset` | Drop → Generate → Push |
| `pnpm db:pull` | Introspect existing DB |
| `pnpm db:check` | Check schema consistency |

## Seeding

```bash
# Seed all data
pnpm seed:all

# Individual entities
pnpm seed:users
pnpm seed:comics
pnpm seed:chapters
pnpm seed:genres
pnpm seed:ratings
pnpm seed:bookmarks
pnpm seed:comments
pnpm seed:reading-history

# Dry run (no writes)
pnpm seed:dry --verbose
```

## Development Scripts

```bash
pnpm dev              # Start dev server
pnpm type-check       # TypeScript validation
pnpm lint:strict      # ESLint (zero warnings)
pnpm test             # Vitest unit tests
pnpm test:ui          # Playwright E2E
pnpm build            # Production build (~35s)
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `pnpm install` fails | Ensure pnpm ≥ 9: `npm i -g pnpm@latest` |
| Database connection | Verify `DATABASE_URL` in `.env.local` |
| `db:push` errors | Check PostgreSQL is running |
| Build fails | `pnpm clean && pnpm build` |
| ESLint warnings | `pnpm lint:fix` for auto-fix |
| Playwright test fails | `pnpm exec playwright install` |
