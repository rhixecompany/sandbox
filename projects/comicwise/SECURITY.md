# ComicWise — Security Guide

## Security Architecture

ComicWise implements defense-in-depth with multiple security layers.

## 1. Authentication & Authorization

### NextAuth.js v5
- **Providers**: Credentials (bcrypt), GitHub OAuth, Keycloak OIDC
- **Session**: Database sessions, 30-day expiry
- **Password Storage**: bcryptjs hashing (cost factor 12)
- **Rate Limiting**: Upstash Redis — 5 attempts per 15 minutes on login

### Route Protection
```typescript
// proxy.ts middleware
- Protected routes: /profile, /bookmarks, /ratings, /admin
- Auth-to-guest redirect: /sign-in → /comics if already authenticated
- Admin routes: require USER role == 'ADMIN' or 'MODERATOR'
```

## 2. Input Validation

- **Zod schemas** at every Server Action entry point
- **25 validation schemas** covering all operations
- **Type coercion** for numeric/date inputs
- **String sanitization**: trim, length limits, regex patterns

```typescript
const SignUpSchema = z.object({
  email: z.string().trim().email(),
  username: z.string().trim().min(3).max(100),
  password: z.string().trim().min(8).max(128),
});
```

## 3. Database Security

- **Parameterized queries** via Drizzle ORM (no SQL injection)
- **No raw SQL** — Drizzle query builders only
- **Soft-delete** on `users` and `comments` (data recovery)
- **Cascade deletes** on most FK relationships (referential integrity)
- **4 pgEnums** enforce valid values at database level

## 4. CSRF & XSS Protection

- **CSRF**: All mutations use Server Actions (POST-only, built-in CSRF)
- **No API routes** exposed for CRUD operations
- **XSS**: React escapes output by default; no `dangerouslySetInnerHTML`
- **Content Security Policy** headers in production

## 5. Data Privacy

- Password hashes never logged
- Email addresses validate-only on signup
- No PII exposed in URLs (UUID-based IDs)
- User data export available via profile settings
- Account deletion (soft-delete) with data retention policy

## 6. API Security

- **Rate Limiting**: Upstash Redis + `@upstash/ratelimit`
  - Sign-in: 5 req/15min
  - Sign-up: 3 req/60min
  - API: 100 req/min general
- **No CORS** issues (same-origin Server Actions)
- **Input size limits** enforced via Zod

## 7. Infrastructure Security

- **Dependencies**: `pnpm audit` in CI, Dependabot configured
- **Environment Variables**: Validated via `@t3-oss/env-nextjs`
- **Secrets**: Never committed, managed via hosting platform
- **HTTPS**: Enforced in production

## Security Checklist

- [ ] Zod validation on every Server Action
- [ ] Auth check on every protected action (`await auth()`)
- [ ] Rate limiting on auth endpoints
- [ ] No `any` types (ESLint enforced)
- [ ] Soft-delete on user and comment tables
- [ ] SQL injection prevention (Drizzle query builder only)
- [ ] CSRF protection (Server Actions)
- [ ] No secrets in code (`.env.local` gitignored)
- [ ] Dependabot configured for dependency updates
- [ ] Content Security Policy set in production
