# ComicWise Security Audit Report

**Repository:** Rhixe-company/comicwise  
**Audit Date:** 2026-05-21  
**Priority:** CRITICAL  
**Auditor:** Automated Security Scan

---

## Executive Summary

The ComicWise codebase has **critical security issues requiring immediate attention**. The most severe finding is that `.env.local` contains **15+ real production credentials** including database URLs, API secrets, and authentication tokens. While `.gitignore` correctly excludes `.env*` files, there is a risk these secrets may exist in git history from before the ignore rule was added.

**Risk Score: 9.5/10** — Active credentials exposed in plaintext on disk.

---

## Critical Findings

### CRITICAL: Real Production Credentials in .env.local

**Category:** Secret Exposure  
**Severity:** 🔴 CRITICAL  
**Status:** ❌ Unresolved

The `.env.local` file contains live credentials for 15+ services:

| Service | Credentials Exposed | Risk |
| --- | --- | --- |
| **PostgreSQL (Neon)** | Full connection URLs with username/password | Database read/write access |
| **GitHub OAuth** | Client ID + Client Secret | OAuth account compromise |
| **Gmail SMTP** | Email address + App Password | Email account takeover |
| **ImageKit** | Public Key + Private Key + URL Endpoint | Image storage access |
| **Cloudinary** | Cloud name | CDN account access |
| **Redis** | Connection URL (may contain password) | Cache data exposure |
| **QStash** | Current + Next signing keys | Queue manipulation |
| **Sentry** | Auth Token + DSN | Error data exposure |
| **Upstash Redis** | REST URL + Token | Remote cache access |

**Remediation:**

1. Rotate ALL credentials immediately
2. Use `direnv`, `sops`, or `1password CLI` for secret management
3. Add pre-commit hook to detect committed secrets

### CRITICAL: Secrets May Be in Git History

**Category:** Secret Exposure  
**Severity:** 🔴 CRITICAL  
**Status:** ⚠️ Needs Investigation

The `.gitignore` currently excludes `.env*` files, but if `.env.local` was committed before the ignore rule was added, secrets are permanently accessible in git history.

**Remediation:**

1. Run `git log --diff-filter=A --follow -p -- .env.local` to check
2. If found, use `git filter-repo` or `git filter-branch` to purge
3. Force-push to all remotes after cleanup
4. Rotate all credentials regardless

---

## High Findings

### HIGH: Exposed Database URL in Code References

**Category:** Information Disclosure  
**Severity:** 🟠 HIGH  
**Status:** ⚠️ Needs Investigation

Database connection strings may be referenced in config files or documentation. Search for any hardcoded database URLs in:

- `drizzle.config.ts`
- Test configuration
- CI/CD pipeline variables

**Remediation:** Use `appConfig.ts` pattern to centralize all configuration reads. Never hardcode credentials in source files.

### HIGH: Exposed OAuth Callback URLs

**Category:** Configuration  
**Severity:** 🟠 HIGH  
**Status:** ✅ Mitigated

OAuth callback URLs in `.env.local` use `localhost:3000`. This is acceptable for development but MUST be restricted in production environments.

**Remediation:** Ensure GitHub OAuth app and Google Cloud Console have production callback URLs registered and development URLs are removed from these services.

---

## Medium Findings

### MEDIUM: No Rate Limiting on Auth Endpoints

**Category:** Denial of Service  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved

The auth endpoints (`sign-in`, `sign-up`) lack rate limiting, making them vulnerable to:

- Brute-force password attacks
- Account enumeration
- Registration spam

**Remediation:** Implement rate limiting using Upstash Redis or middleware on auth routes.

### MEDIUM: Audit Log Rotation Strategy Missing

**Category:** Operations  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved

The `auditLog` table captures all user actions with IP address, user agent, and session data. Without a retention/rotation strategy:

- Table will grow unbounded, impacting performance
- Old data may violate data privacy regulations

**Remediation:** Implement log rotation — archive records older than 90 days to cold storage.

### MEDIUM: Incomplete Input Validation Coverage

**Category:** Security  
**Severity:** 🟡 MEDIUM  
**Status:** ⚠️ Partial

While Zod schemas exist for most entities, verify:

- All server actions use `safeParse()` not `parse()` for validation
- File upload endpoints validate file types and sizes
- Pagination parameters have upper bounds
- Search queries are sanitized against injection

**Remediation:** Audit all server actions to ensure consistent Zod validation with error handling.

---

## Low Findings

### LOW: Debug Routes in Production Check Needed

**Category:** Operations  
**Severity:** 🟢 LOW  
**Status:** ⚠️ Needs Investigation

The `api/seed/route.ts` API route exists for database seeding. Verify that this route is:

- Disabled in production builds
- Protected by authentication
- Not accessible on the production deployment

**Remediation:** Gate the seed route behind `NODE_ENV === 'development'` check.

### LOW: CORS Configuration

**Category:** Security  
**Severity:** 🟢 LOW  
**Status:** ⚠️ Needs Investigation

Verify that API routes have proper CORS headers configured in production to prevent unauthorized cross-origin requests.

### LOW: Dependency Vulnerability Scan Needed

**Category:** Supply Chain  
**Severity:** 🟢 LOW  
**Status:** ⚠️ Needs Investigation

The project uses multiple dependencies with known historical CVEs. Specific packages to audit:

- Next.js 16.1.6 — Check for latest patch release
- zod 4.3.6 — Review v4 migration advisory
- next-auth beta — Verify beta stability for production use
- Sharp-based image processing — Ensure image parsing CVEs are patched

**Remediation:** Run `pnpm audit` and `pnpm outdated` weekly. Pin exact versions for critical dependencies.

### LOW: No CSRF Token Validation on API Routes

**Category:** Security  
**Severity:** 🟢 LOW  
**Status:** ✅ Mitigated

While Server Actions have built-in CSRF protection, the `api/seed/route.ts` route uses the standard API Routes pattern (not Server Actions). Verify it includes CSRF validation or is restricted to internal use only.

**Remediation:** Either convert seed route to a Server Action or add a middleware check to restrict it to development environments.

---

## Credential Rotation Checklist

- [ ] **PostgreSQL (Neon)** — Regenerate via Neon console
- [ ] **GitHub OAuth** — Regenerate client secret in GitHub Developer Settings
- [ ] **Google OAuth** — Regenerate in Google Cloud Console
- [ ] **Gmail App Password** — Revoke and regenerate in Google Account
- [ ] **ImageKit Private Key** — Rotate in ImageKit dashboard
- [ ] **Cloudinary API Secret** — Rotate in Cloudinary dashboard
- [ ] **QStash Signing Keys** — Rotate in Upstash console
- [ ] **Sentry Auth Token** — Regenerate in Sentry
- [ ] **Upstash Redis Token** — Rotate in Upstash console
- [ ] **AUTH_SECRET** — Regenerate with `openssl rand -base64 32`

---

## Recommendations

### Immediate (24 hours)

1. Rotate all credentials listed above
2. Check git history for committed secrets
3. Add pre-commit hook: `npx secretlint` or `ggshield`

### Short-term (1 week)

4. Implement rate limiting on auth routes
5. Add audit log rotation policy (archive at 90 days)
6. Audit all server actions for complete Zod validation

### Long-term (1 month)

7. Implement secrets management with HashiCorp Vault or Doppler
8. Add automated secret scanning in CI/CD pipeline
9. Enable branch protection with required PR reviews
10. Conduct penetration testing of auth flows

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [ComicWise Remediation Plan](../Repo_Audit/comicwise_remediation_plan.md)
- [Next.js Security Best Practices](https://nextjs.org/docs/pages/building-your-application/configuring/debugging)
