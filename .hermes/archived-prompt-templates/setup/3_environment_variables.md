# 3. Environment Variables

> Extracted from `setup.prompt.md`.

## 3. Environment Variables

Create `.env.local` from `.env.local.example`:

```bash
# ── Required ──
DATABASE_URL="postgresql://user:pass@localhost:5432/comicbook"
AUTH_SECRET="$(openssl rand -hex 32)"     # min 32 chars
NEXT_PUBLIC_API_URL="http://localhost:3000"
NODE_ENV="development"

# ── Required for NextAuth ──
AUTH_URL="http://localhost:3000"           # Base URL for auth callbacks

# ── Optional: Neon serverless ──
NEON_DATABASE_URL="postgresql://..."      # Neon serverless connection string

# ── Optional: Debug ──
DEBUG="false"                             # Enable debug logging

# ── OAuth (optional — GitHub) ──
GITHUB_CLIENT_ID="your_client_id"
GITHUB_CLIENT_SECRET="your_client_secret"

# ── OAuth (optional — Keycloak) ──
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="your_secret"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"

# ── Image CDN (optional — only for imagekit seed strategy) ──
IMAGEKIT_PUBLIC_KEY="..."
IMAGEKIT_PRIVATE_KEY="..."
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/youraccount"
```

### Runtime Validation (`src/lib/env.ts`)

**Only 6 fields are actively validated** via Zod: `DATABASE_URL`, `NEON_DATABASE_URL`, `AUTH_SECRET`, `NEXT_PUBLIC_API_URL`, `NODE_ENV`, `DEBUG`. The remaining ~60 fields (OAuth, ImageKit, Sentry, Redis, email, etc.) are commented out as stubs for future integration.

Access validated env through `getEnv()` — never use raw `process.env` in app code.

**Known exception:** `auth-config.ts`, `auth-providers.ts`, and `db.ts` use raw `process.env` because they load before app initialization. This is a pragmatic trade-off, not a pattern to follow elsewhere.

---
