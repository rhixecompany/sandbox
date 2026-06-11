# Banking — Security Guide

## Security Principles

1. **Never Commit Secrets** — All secrets stored in `.env.local` (gitignored)
2. **Encrypt Sensitive Data** — Plaid access tokens encrypted at rest
3. **Validate All Inputs** — Zod schemas at every Server Action entry point
4. **Use Soft-Delete** — User data preserved for audit/recovery
5. **Idempotency** — All financial transactions use idempotency keys

## Data Protection

### At Rest
- Passwords: bcrypt hashing (cost factor 12)
- Plaid tokens: AES-256-GCM encryption in database
- Dwolla credentials: Stored securely via environment variables

### In Transit
- HTTPS enforced in production
- All API calls to Plaid/Dwolla over TLS
- Server Actions use POST only

### Input Validation
```typescript
// Every Server Action validates inputs with Zod
const ActionSchema = z.object({
  id: z.string().min(1),
  amount: z.string().transform(Number).pipe(z.number().positive())
});
```

## Authentication

- **NextAuth v4** with Credentials provider
- bcrypt password comparison (no plaintext storage)
- Session expiry: 30 days
- Rate limiting on sign-in attempts (Upstash Redis)

## Authorization

- Route protection via Next.js Middleware (`proxy.ts`)
- Admin routes require role check
- Server Actions verify session ownership
- API routes validate authentication tokens

## Rate Limiting

| Endpoint | Limit | Window |
|----------|-------|--------|
| Sign-in | 5 attempts | 15 minutes |
| Registration | 3 attempts | 60 minutes |
| Transfer initiation | 10 per hour | 1 hour |
| Plaid token generation | 20 per hour | 1 hour |

Configured via Upstash Redis + `@upstash/ratelimit`.

## Financial Transaction Security

- **Idempotency Keys**: Prevent duplicate ACH transfers
- **Amount Validation**: Positive amounts only, capped per transaction
- **Recipient Verification**: Only known recipients allowed
- **Audit Trail**: All transfers logged with Dwolla reference IDs

## CSRF Protection

- All mutations use Next.js Server Actions
- No API routes exposed for CRUD operations
- Built-in CSRF protection via POST-only actions

## Secrets Management

```bash
# Local development
cp .env.local.example .env.local
# Edit with your secrets

# Production
# Use Vercel Environment Variables / Docker secrets
```

## Security Checklist

- [ ] All secrets in `.env.*` files (gitignored)
- [ ] Zod validation on every Server Action
- [ ] Rate limiting enabled for auth endpoints
- [ ] Soft-delete configured for user data
- [ ] Idempotency keys for financial transactions
- [ ] HTTPS enabled in production
- [ ] Database backups configured
- [ ] Plaid/Dwolla in production mode (not sandbox)
