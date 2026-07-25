# Banking — Fintech App Architecture Blueprint

> **Generated:** 2026-07-24
> **Generator:** architecture-blueprint-generator
> **Project:** Banking (Next.js 16 Fintech App)

---

## Project Overview

- **Project Name:** Banking
- **Project Type:** Full-stack fintech web application (banking dashboard)
- **Architecture Pattern:** Next.js 16 App Router — full-stack, Server Components by default
- **License:** Private (no license specified)

---

## System Architecture Diagram

```mermaid
architecture-beta
  group ui[UI Layer]
  group api[API Layer]
  group data[Data Layer]
  group ext[External Services]

  service browser[Browser] in ui
  service nextjs[Next.js 16] in api
  service server_comp[Server Components] in ui
  service client_comp[Client Components] in ui

  service drizzle[Drizzle ORM] in data
  service pg[(PostgreSQL)] in data
  service upstash[(Upstash Redis)] in data

  service plaid[Plaid API] in ext
  service dwolla[Dwolla API] in ext
  service email[Email (Nodemailer)] in ext
  service qstash[Upstash QStash] in ext

  browser --> nextjs
  nextjs --> server_comp
  nextjs --> client_comp
  server_comp --> drizzle
  client_comp --> server_comp
  client_comp --> plaid
  client_comp --> dwolla
  drizzle --> pg
  nextjs --> upstash
  nextjs --> plaid
  nextjs --> dwolla
  nextjs --> email
  nextjs --> qstash
```

---

## Request Flow

```mermaid
sequenceDiagram
    participant User as User Browser
    participant Next as Next.js 16
    participant SC as Server Components
    participant CC as Client Components
    participant SA as Server Actions
    participant AO as API Routes
    participant DZ as Drizzle ORM
    participant PG as PostgreSQL
    participant PL as Plaid API
    participant DW as Dwolla API
    participant RS as Upstash Redis

    %% Authentication Flow
    User->>Next: GET /sign-in
    Next->>SC: Render sign-in page
    SC-->>User: Return HTML
    User->>Next: POST credentials (Server Action)
    Next->>SA: auth.signin()
    SA->>DZ: Query user
    DZ->>PG: SELECT * FROM users WHERE email=?
    PG-->>DZ: user record
    DZ-->>SA: user data
    SA->>SA: Verify bcrypt hash
    SA-->>User: JWT session cookie

    %% Bank Linking Flow
    User->>CC: Click "Link Bank Account"
    CC->>PL: react-plaid-link → Plaid Link
    PL-->>CC: Public token
    CC->>AO: POST /api/plaid/link
    AO->>PL: Exchange public token
    PL-->>AO: Access token + item_id
    AO->>DZ: Store encrypted token
    DZ->>PG: INSERT INTO plaid_items
    AO->>SA: Create Dwolla customer
    SA->>DW: Create customer
    DW-->>SA: Customer URL
    SA->>DZ: INSERT INTO wallets
    RS->>RS: Invalidate cache

    %% Transfer Flow
    User->>CC: Submit transfer form
    CC->>SA: transaction.actions()
    SA->>DW: POST /transfers (ACH)
    DW-->>SA: Transfer URL
    SA->>DZ: INSERT INTO transactions
    SA->>DZ: INSERT INTO dwolla_transfers
    SA-->>User: Success response
    SA->>RS: Rate limit check
    SA->>Email: Send notification

    %% Webhook Flow
    DW->>AO: POST /api/dwolla/webhook
    AO->>DZ: UPDATE transactions SET status
    DZ->>PG: UPDATE
    AO-->>DW: 200 OK
```

---

## Architecture Patterns

### 1. App Router (Next.js 16)

| Pattern | Implementation |
| --- | --- |
| **Server Components** | Default rendering strategy for pages and layouts |
| **Client Components** | Interactive UI (`"use client"` in forms, charts, Plaid Link) |
| **Route Groups** | `(root)`, `(auth)`, `(admin)` for URL-free layout org |
| **Server Actions** | All mutations (login, register, create transfer, link bank) |
| **Route Handlers** | API routes for Plaid/Dwolla webhooks, NextAuth, health checks |

### 2. Data Access Layer (DAL)

```
Server Actions / Route Handlers
       │
       ▼
    DAL functions (src/dal/)
       │
       ▼
 Drizzle ORM (type-safe SQL)
       │
       ▼
    PostgreSQL
```

- All database queries go through `src/dal/` modules
- Schema in `src/database/schema.ts` — 10 tables, 4 enums
- Drizzle Adapter for NextAuth session → user mapping
- Migrations via `drizzle-kit`

### 3. Financial Integration Layer

| Service | Role | SDK | Webhook |
| --- | --- | --- | --- |
| **Plaid** | Bank account linking, transaction sync, identity verification | `plaid` + `react-plaid-link` | Plaid webhooks (item updates, transactions) |
| **Dwolla** | ACH transfer processing, customer creation, funding sources | `dwolla-v2` | Dwolla webhooks (transfer status changes) |

- Plaid access tokens encrypted with AES-256-GCM at rest
- Dwolla transfer idempotency via UUID keys
- Plaid sandbox mode for development

### 4. State Management

| Store | Purpose | Technology |
| --- | --- | --- |
| **UI Store** | Sidebar, theme, mobile nav | Zustand |
| **Transfer Store** | Transfer form state | Zustand |
| **Filter Store** | Transaction list filters | Zustand |
| **Toast Store** | Notification queue | Zustand |
| **Session Store** | Auth session (React context) | React Context |
| **Plaid Context** | Plaid Link lifecycle | React Context |

### 5. Authentication & Authorization

- **Framework:** NextAuth.js v4 with JWT strategy
- **Adapters:** `@auth/drizzle-adapter` for DB-backed sessions
- **Providers:** Credentials (email/password with bcrypt) + OAuth-ready
- **Roles:** `user`, `admin`, `moderator` via `user_role` enum
- **Password strength:** `@zxcvbn-ts/core` integration
- **Rate limiting:** Upstash Redis + `@upstash/ratelimit`

---

## Database Schema

```mermaid
erDiagram
    users ||--o{ account : "has OAuth"
    users ||--o{ session : "has sessions"
    users ||--o{ user_profiles : "has profile"
    users ||--o{ plaid_items : "has plaid items"
    users ||--o{ wallets : "owns wallets"
    users ||--o{ transactions : "initiates"
    users ||--o{ recipients : "saves recipients"
    users ||--o{ dwolla_transfers : "has transfers"
    users ||--o{ audit_logs : "audit trail"
    users ||--o{ errors : "error logs"
    wallets ||--o{ transactions : "source/destination"
    wallets ||--o{ dwolla_transfers : "source/destination"
    wallets ||--o{ recipients : "bank account reference"

    users {
        text id PK
        varchar email UK
        varchar password
        varchar name
        varchar image
        boolean isActive
        boolean isAdmin
        user_role role
        timestamp deletedAt
    }

    wallets {
        text id PK
        text accessToken
        varchar accountId
        varchar accountType
        varchar accountSubtype
        varchar institutionId
        varchar institutionName
        varchar sharableId UK
        varchar routingNumber
        text fundingSourceUrl
        varchar customerUrl
        text userId FK
    }

    transactions {
        text id PK
        numeric amount
        varchar name
        varchar category
        transaction_type type
        transaction_status status
        varchar plaidTransactionId UK
        text senderWalletId FK
        text receiverWalletId FK
        text userId FK
    }
```

### Tables (10 total)

| Table | Description | Key Columns |
| --- | --- | --- |
| `users` | Core user authentication & profile | email, password, isAdmin, role |
| `account` | NextAuth OAuth account links | provider, providerAccountId |
| `session` | NextAuth session storage (unused with JWT) | sessionToken |
| `verificationToken` | Email verification tokens | identifier, token |
| `authenticator` | WebAuthn passkey storage | credentialID, userId |
| `user_profiles` | KYC data (address, SSN encrypted, DOB) | userId |
| `plaid_items` | Plaid item registry | itemId, accessTokenEncrypted |
| `wallets` | Linked bank accounts + Dwolla integration | sharableId, fundingSourceUrl |
| `transactions` | Financial ledger (Plaid + internal ACH) | amount, status, plaidTransactionId |
| `dwolla_transfers` | Dwolla ACH transfer metadata | idempotencyKey, dwollaTransferId |
| `recipients` | Saved transfer recipients | email, name |
| `errors` | Application error logging | message, severity, stack |
| `audit_logs` | Append-only compliance audit trail | action, metadata, userId |

### Enums (4)

| Enum | Values |
| --- | --- |
| `user_role` | `user`, `admin`, `moderator` |
| `transaction_status` | `pending`, `processing`, `completed`, `failed`, `cancelled` |
| `transaction_type` | `credit`, `debit` |
| `transaction_channel` | `online`, `in_store`, `other` |

---

## Page Routes (App Router)

```mermaid
graph TD
    subgraph Public
        A["/ (Home/Landing)"] --> B["/sign-in"]
        A --> C["/sign-up"]
    end

    subgraph Authenticated
        D["/dashboard"] --> D1[Account Overview]
        D --> E["/my-wallets"]
        D --> F["/payment-transfer"]
        D --> G["/transaction-history"]
        D --> H["/settings"]
    end

    subgraph Admin
        I["/admin"] --> I1[Admin Dashboard]
    end
```

### Route Group Structure

| Route Group | Path | Layout | Description |
| --- | --- | --- | --- |
| `(root)` | `/dashboard`, `/my-wallets`, `/payment-transfer`, `/transaction-history`, `/settings` | RootLayoutWrapper | Authenticated pages |
| `(auth)` | `/sign-in`, `/sign-up` | AuthLayoutWrapper | Public auth pages |
| `(admin)` | `/admin` | AdminLayoutWrapper | Admin panel |

---

## API Routes

| Route | Method | Purpose |
| --- | --- | --- |
| `/api/auth/[...nextauth]` | ALL | NextAuth handler |
| `/api/auth/local-create` | POST | Register new user credentials |
| `/api/auth/local-validate` | POST | Validate sign-in credentials |
| `/api/dwolla/webhook` | POST | Dwolla transfer status updates |
| `/api/health` | GET | Health check endpoint |

---

## Security Architecture

```
┌─────────────────────────────────────────────┐
│              Security Layers                 │
├─────────────────────────────────────────────┤
│   1. NextAuth JWT (HTTP-only cookies)       │
│   2. Rate Limiting (Upstash Redis)          │
│   3. AES-256-GCM Encryption (tokens, SSN)   │
│   4. bcrypt Password Hashing                │
│   5. Zod Schema Validation (forms + API)    │
│   6. ESLint Security Plugins (no-secrets)   │
│   7. Audit Logs (append-only compliance)    │
│   8. Soft Delete (data preservation)        │
│   9. Idempotency Keys (Dwolla transfers)    │
│   10. Webhook HMAC Verification             │
└─────────────────────────────────────────────┘
```

---

## Deployment Architecture

```mermaid
graph LR
    subgraph Dev
        DEV[Next.js Dev Server]
        DB_DEV[PostgreSQL Local]
        PLAID_SB[Plaid Sandbox]
    end

    subgraph CI/CD
        GHA[GitHub Actions]
        LINT[Lint + Type Check]
        TEST[Playwright + Vitest]
    end

    subgraph Prod
        VERCEL[Vercel / Docker]
        DB_PROD[PostgreSQL Cloud]
        REDIS[Upstash Redis]
        PLAID_PROD[Plaid Production]
    end

    DEV --> DB_DEV
    DEV --> PLAID_SB
    DEV --> GHA
    GHA --> LINT
    GHA --> TEST
    TEST --> VERCEL
    VERCEL --> DB_PROD
    VERCEL --> REDIS
    VERCEL --> PLAID_PROD
```

### Deployment Options

| Platform | Config | Notes |
| --- | --- | --- |
| **Vercel** | `vercel.json` + `next.config.ts` | Primary production target |
| **Docker** | `docker-compose.yml` + `compose/prod/` | Self-hosted with Traefik, Grafana, Prometheus |
| **Railway** | `Railway.toml` | Alternative cloud deployment |

### Monitoring

| Tool | Purpose |
| --- | --- |
| **Grafana** | Dashboard visualization (`compose/prod/grafana/`) |
| **Prometheus** | Metrics collection + alerting (`compose/prod/prometheus/`) |
| **Upstash QStash** | Scheduled/async task execution |

---

## Key Architectural Decisions

1. **Server Components by default** — Minimizes client-side JavaScript for better performance on financial dashboards
2. **Drizzle ORM over Prisma** — Type-safe SQL with lower overhead, better migration DX, and Drizzle Studio
3. **Plaid + Dwolla dual API** — Plaid for bank linking/read, Dwolla for write operations (ACH transfers) — industry standard split
4. **Encrypted token storage** — AES-256-GCM for Plaid access tokens and SSNs; decrypted only at point of use
5. **Zustand over Redux** — Lightweight state management for UI state, filter stores, and toast notifications
6. **NextAuth with JWT strategy** — Stateless auth avoids DB lookups on every request; roles embedded in token
7. **Soft deletes everywhere** — All major entities (users, wallets, transactions) support soft delete for audit compliance
8. **Docker Compose for local prod parity** — Full monitoring stack (Grafana + Prometheus) in `compose/`

---

## Extensibility Points

- **New banking features** via App Router route groups in `src/app/(root)/`
- **New financial integrations** via `src/lib/` (add provider, schema, DAL)
- **New UI components** via `npx shadcn add` or `bun run generate:component`
- **New API endpoints** as Route Handlers under `src/app/api/`
- **New DAL modules** in `src/dal/` following the existing pattern
- **New code generators** in `scripts/generate/` (action, component, dal, feature)

---

*Generated by architecture-blueprint-generator — comprehensive analysis*
