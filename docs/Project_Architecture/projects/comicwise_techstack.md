# 🏗 Technology Stack Blueprint - comicwise

**Project Path:** `projects/comicwise`
**Generated:** 2026-07-28
**Type:** Comic Streaming Platform — Next.js 15 + Prisma + Stripe

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Runtime** | Node.js | 18+ | MIT |
| **Package Manager** | pnpm | 9.12.3 | MIT |
| **Framework** | Next.js | 16.1.6 | MIT |
| **Language** | TypeScript (strict) | ^5.9.3 | Apache 2.0 |
| **UI Library** | React | 19.2.4 | MIT |
| **ORM** | Drizzle ORM | 0.45.1 | Apache 2.0 |
| **Database** | PostgreSQL | Latest | PostgreSQL |
| **Auth** | NextAuth.js v5 (beta) | 5.0.0-beta.30 | ISC |
| **Payments** | Stripe | ^18.2.1 | MIT |
| **Media** | ImageKit + Cloudinary | ^6.0.0 / ^2.9.0 | MIT |
| **Real-time** | Upstash QStash / Workflow | ^2.9.0 / ^1.1.1 | MIT |
| **Email** | nodemailer + Resend | ^8.0.2 / ^4.6.0 | MIT |
| **State Mgt** | Zustand + TanStack Query | ^5.0.11 / ^5.90.21 | MIT |
| **Styling** | Tailwind CSS v4 | ^4 | MIT |
| **UI Components** | Radix UI / shadcn/ui | Latest | MIT |
| **Animation** | Framer Motion | ^12.36.0 | MIT |
| **Charts** | recharts | 3.8.0 | MIT |
| **Testing** | Vitest + Playwright | ^4.1.0 / ^1.58.2 | MIT |
| **Linting** | ESLint 9 + Prettier 3 | ^9.0.0 / ^3.8.1 | MIT |
| **Package Manager** | pnpm | 9.12.3 | MIT |

---

## Architecture Pattern

**Next.js App Router** with:
- Server Components by default
- Client Components only when needed (interactivity)
- Route Groups for layout separation
- Server Actions for mutations

### Data Flow
```
Client → Server Components (RSC) → Drizzle ORM → PostgreSQL
         ↓
    Server Actions → Stripe/PayPal APIs
         ↓
    Upstash QStash → Background Jobs
```

---

## Key Dependencies

### Production (~100 packages)

| Category | Key Packages |
|----------|-------------|
| **Framework** | `next@16.1.6`, `react@19.2.4`, `react-dom@19.2.4` |
| **Auth** | `next-auth@5.0.0-beta.30`, `@auth/drizzle-adapter@1.11.1` |
| **Database** | `drizzle-orm@0.45.1`, `drizzle-zod@0.8.3`, `postgres@3.4.8` |
| **Payments** | `stripe@18.2.1`, `@stripe/react-stripe-js@3.7.0`, `@stripe/stripe-js@7.3.1` |
| **Media** | `imagekit@6.0.0`, `cloudinary@2.9.0`, `@imagekit/next@2.1.5` |
| **Real-time** | `@upstash/qstash@2.9.0`, `@upstash/workflow@1.1.1`, `@upstash/redis@1.37.0`, `@upstash/ratelimit@2.0.8` |
| **Email** | `nodemailer@8.0.2`, `resend@4.6.0`, `@react-email/components@1.0.9` |
| **State** | `zustand@5.0.11`, `@tanstack/react-query@5.90.21`, `@tanstack/react-table@8.21.3` |
| **UI** | `@radix-ui/*` (15+ packages), `class-variance-authority@0.7.1`, `clsx@2.1.1`, `tailwind-merge@3.5.0` |
| **Forms** | `react-hook-form@7.71.2`, `@hookform/resolvers@5.2.2`, `zod@4.3.6` |
| **Animation** | `framer-motion@12.36.0`, `embla-carousel-react@8.6.0` |
| **Utilities** | `date-fns@4.1.0`, `slugify@1.6.8`, `lucide-react@0.577.0` |

### Development (~60 packages)

| Category | Key Packages |
|----------|-------------|
| **TypeScript** | `typescript@^5.9.3`, `@types/react@^19`, `@types/node@^25` |
| **ESLint** | `eslint@^9`, `eslint-config-next@16.1.6`, `typescript-eslint@^8.57`, 15+ plugins |
| **Prettier** | `prettier@^3.8.1`, `prettier-plugin-tailwindcss@^0.7.2` |
| **Testing** | `vitest@^4.1.0`, `@playwright/test@^1.58.2`, `@testing-library/*` |
| **Database** | `drizzle-kit@^0.31.9`, `tsx@^4.21.0` |
| **Utilities** | `ts-morph@^27`, `jscodeshift@^17.3`, `cross-env@^10.1` |

---

## Database Schema (Drizzle)

```typescript
// src/db/schema.ts
import { pgTable, serial, text, timestamp, integer, boolean, decimal } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  email: text('email').unique().notNull(),
  name: text('name'),
  image: text('image'),
  stripeCustomerId: text('stripe_customer_id'),
  createdAt: timestamp('created_at').defaultNow(),
});

export const comics = pgTable('comics', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  description: text('description'),
  coverImage: text('cover_image'),
  price: decimal('price', { precision: 10, scale: 2 }),
  // ...
});

export const subscriptions = pgTable('subscriptions', {
  id: serial('id').primaryKey(),
  userId: integer('user_id').references(() => users.id),
  stripeSubscriptionId: text('stripe_subscription_id').unique(),
  status: text('status'),
  currentPeriodEnd: timestamp('current_period_end'),
});
```

---

## Authentication Flow

1. **NextAuth.js v5** with Drizzle adapter
2. Providers: Email/Password, OAuth (Google, GitHub)
3. JWT strategy with secure httpOnly cookies
4. Middleware protection for `/dashboard/*`, `/library/*`
5. Session accessed via `auth()` in Server Components

---

## Payment Integration (Stripe)

| Feature | Implementation |
|---------|---------------|
| **Subscriptions** | Stripe Billing + Webhooks |
| **Checkout** | Stripe Checkout Sessions (Server Action) |
| **Portal** | Stripe Billing Portal (manage subscription) |
| **Webhooks** | `/api/webhooks/stripe` → Upstash QStash → Workflow |
| **Products** | Comic series as Stripe Products, issues as Prices |

---

## Real-time Architecture

```
User Action → Server Action → Upstash QStash → Workflow → Background Job
                              ↓
                        Redis (Upstash) → Rate Limiting / Cache
```

- **QStash**: Reliable message delivery, retries, scheduling
- **Workflow**: Multi-step background jobs with state
- **Redis**: Session cache, rate limiting, pub/sub

---

## Key Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| `dev` | `next dev` | Development server |
| `build` | `next build` | Production build |
| `lint` | `eslint .` | Lint check |
| `lint:fix` | `eslint . --fix` | Auto-fix |
| `lint:strict` | `eslint . --max-warnings=0` | Zero-warnings gate |
| `format` | `prettier --write .` | Format code |
| `type-check` | `tsc --noEmit` | Type check |
| `test` | `vitest run` | Unit tests |
| `test:ui` | `playwright test` | E2E tests |
| `db:generate` | `drizzle-kit generate` | Generate migrations |
| `db:push` | `drizzle-kit push` | Push schema (dev) |
| `db:studio` | `drizzle-kit studio` | Database UI |
| `validate` | Full quality gate | Pre-deployment check |

---

## Project Structure

```
projects/comicwise/
├── src/
│   ├── app/                    # App Router pages
│   │   ├── (auth)/            # Auth route group
│   │   ├── (dashboard)/       # Protected routes
│   │   ├── api/               # API routes
│   │   │   ├── auth/          # NextAuth endpoints
│   │   │   ├── webhooks/      # Stripe webhooks
│   │   │   └── comics/        # Comic CRUD
│   │   └── library/           # User library
│   ├── components/            # React components
│   │   ├── ui/               # shadcn/ui components
│   │   ├── comics/           # Comic-specific
│   │   └── forms/            # Form components
│   ├── lib/                  # Utilities
│   │   ├── auth.ts           # NextAuth config
│   │   ├── db.ts             # Drizzle client
│   │   ├── stripe.ts         # Stripe client
│   │   ├── upstash.ts        # Redis/QStash clients
│   │   └── utils.ts          # Helpers (cn, etc.)
│   ├── db/                   # Database
│   │   ├── schema.ts         # Drizzle schema
│   │   └── queries.ts        # Query helpers
│   ├── hooks/                # Custom hooks
│   └── types/                # TypeScript types
├── drizzle.config.ts         # Drizzle config
├── next.config.ts            # Next.js config
├── tailwind.config.ts        # Tailwind config
├── eslint.config.mjs         # ESLint flat config
├── .prettierrc.ts            # Prettier config
├── package.json
├── pnpm-lock.yaml
└── tsconfig.json
```

---

## CI/CD Pipeline

**Workflow:** `.github/workflows/comicwise-ci.yml`

1. **Install** → `pnpm install --frozen-lockfile`
2. **Type Check** → `pnpm run type-check`
3. **Lint** → `pnpm run lint:strict`
4. **Format Check** → `pnpm run format:check`
5. **Test** → `pnpm run test && pnpm run test:ui`
6. **Build** → `pnpm run build`
7. **Deploy** → Vercel (on merge to `staged`)

---

## License Summary

| License | Approx. Count |
|---------|--------------|
| MIT | ~140 |
| Apache 2.0 | ~15 |
| ISC | ~5 |
| BSD | ~5 |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*