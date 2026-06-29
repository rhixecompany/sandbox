# ComicWise — Deployment Guide

## Deployment Options

### 1. Vercel (Recommended)

ComicWise is optimized for Vercel deployment:

```bash
# Install Vercel CLI
pnpm add --global vercel

# Deploy
vercel --prod
```

Configure environment variables in Vercel Dashboard:

- `DATABASE_URL` — Neon PostgreSQL connection string
- `AUTH_SECRET` — NextAuth secret
- `AUTH_GITHUB_ID` / `AUTH_GITHUB_SECRET` — GitHub OAuth
- `AUTH_KEYCLOAK_ID` / `AUTH_KEYCLOAK_SECRET` / `AUTH_KEYCLOAK_ISSUER` — Keycloak OIDC
- `SENTRY_AUTH_TOKEN` (optional) — Error tracking

### 2. Docker

Multi-stage Dockerfile included:

```bash
docker build -t comicwise:latest .
docker run -p 3000:3000 --env-file .env.production comicwise:latest
```

### 3. Railway.app

Railway supports Next.js + PostgreSQL natively:

```bash
# Deploy via GitHub connection
# Railway auto-detects Next.js and PostgreSQL
```

### 4. AWS

Deploy via ECS, Lambda (with Next.js adapter), or EC2.

## Production Build

```bash
pnpm build     # ~35s production build
pnpm start     # Run production server
```

## Database Migrations

In production, migrations run as part of the build process:

```bash
pnpm db:migrate   # Apply pending migrations
pnpm db:push      # Direct push (dev only)
```

## Environment Configuration

```env
NODE_ENV=production
DATABASE_URL=postgresql://user:***@neon-host/comicwise
AUTH_SECRET=<generated-secret>
AUTH_URL=https://yourdomain.com

# OAuth (optional)
AUTH_GITHUB_ID=...
AUTH_GITHUB_SECRET=...
AUTH_KEYCLOAK_ID=...
AUTH_KEYCLOAK_SECRET=...
AUTH_KEYCLOAK_ISSUER=...
```

## Pre-Deployment Checklist

- [ ] All migrations applied
- [ ] Production build succeeds (`pnpm build`)
- [ ] Environment variables configured in hosting platform
- [ ] Database connection string set to production
- [ ] OAuth providers configured with production callback URLs
- [ ] Sentry/error monitoring enabled (optional)
- [ ] CDN configured for comic images (Cloudinary/ImageKit)
- [ ] Rate limiting configured for production
- [ ] SSL/HTTPS enabled
- [ ] Database backups scheduled

## CI/CD Pipeline

GitHub Actions on push/PR:

1. `pnpm lint:strict` — Zero ESLint errors
2. `pnpm type-check` — Zero TypeScript errors
3. `pnpm test` — All unit tests pass
4. `pnpm test:ui` — Playwright E2E tests
5. `pnpm build` — Production build
6. Auto-deploy on main branch
