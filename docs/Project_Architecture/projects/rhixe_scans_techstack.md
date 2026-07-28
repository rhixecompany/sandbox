# 🏗 Technology Stack Blueprint - rhixe_scans

**Project Path:** `projects/rhixe_scans`
**Generated:** 2026-07-28
**Status:** Active — Comic Reader Platform

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Next.js | ^15.3.3 | MIT |
| **Language** | TypeScript (strict) | ^5 | Apache 2.0 |
| **UI Library** | React | ^19.1.0 | MIT |
| **Package Manager** | npm | Latest | - |
| **ORM** | Prisma | 6.10.0 | Apache 2.0 |
| **Database** | PostgreSQL | Latest | PostgreSQL |
| **Auth** | NextAuth.js v5 (beta) | ^5.0.0-beta.25 | ISC |
| **Styling** | Tailwind CSS 3.x | ^3.4.1 | MIT |
| **UI Components** | Radix UI + shadcn/ui | Latest | MIT |
| **State Management** | Zustand + TanStack Table | ^5.0.11 / ^8.21.3 | MIT |
| **Charts** | Recharts | ^2.15.3 | MIT |
| **Payments** | Stripe + PayPal | ^18.2.1 / @paypal/react-paypal-js | MIT |
| **Real-time** | WebSocket (ws) | ^8.18.2 | MIT |
| **File Upload** | UploadThing | ^7.7.2 | MIT |
| **Email** | Resend | ^4.6.0 | MIT |
| **Caching/Queue** | Upstash Redis + QStash + Workflow | ^1.37.0 / ^2.9.0 / ^1.1.1 | MIT |
| **Testing** | Jest | ^30.0.0 | MIT |
| **Linting** | ESLint 9 + Prettier 3 | ^9 / ^3.5.3 | MIT |

---

## Architecture

**Next.js App Router** with:
- Server Components by default
- Client Components for interactivity
- Server Actions for mutations
- Middleware for auth protection

### Data Flow
```
Client → Server Components → Prisma → PostgreSQL
    ↓
Server Actions → Stripe/PayPal/Resend/UploadThing
    ↓
Upstash QStash → Workflow → Background Jobs
    ↓
WebSocket (ws) → Real-time notifications
```

---

## Key Dependencies

### Production (~60 packages)

| Category | Packages |
|----------|----------|
| **Framework** | `next@15.3.3`, `react@19.1.0`, `react-dom@19.1.0` |
| **Auth** | `next-auth@5.0.0-beta.25`, `@auth/prisma-adapter@2.9.1` |
| **Database** | `@prisma/client@6.10.0`, `prisma@6.10.0` |
| **Payments** | `stripe@18.2.1`, `@stripe/react-stripe-js@3.7.0`, `@stripe/stripe-js@7.3.1`, `@paypal/react-paypal-js@8.8.3` |
| **Real-time** | `ws@8.18.2`, `bufferutil@4.0.9` |
| **Upload** | `@uploadthing/react@7.3.1`, `uploadthing@7.7.2` |
| **Email** | `resend@4.6.0`, `@react-email/components@0.1.0`, `react-email@4.0.16` |
| **Cache/Queue** | `@upstash/redis@1.37.0`, `@upstash/ratelimit@2.0.5`, `@upstash/qstash@2.9.0`, `@upstash/workflow@1.1.1` |
| **UI** | `@radix-ui/*` (15+ packages), `class-variance-authority@0.7.1`, `clsx@2.1.1`, `tailwind-merge@3.3.1`, `tailwindcss-animate@1.0.7`, `lucide-react@0.516.0`, `sonner@2.0.5`, `vaul@1.1.2`, `cmdk@1.1.1` |
| **Forms** | `react-hook-form@7.58.1`, `@hookform/resolvers@5.1.1`, `zod@3.25.67` |
| **Data** | `@tanstack/react-table@8.21.3`, `recharts@2.15.3`, `dayjs@1.11.13` |
| **Utils** | `slugify@1.6.6`, `uuid@11.1.0`, `use-debounce@10.0.5`, `query-string@9.2.1`, `pretty-bytes@7.0.0` |

### Development (~20 packages)

| Category | Packages |
|----------|----------|
| **TypeScript** | `typescript@^5`, `@types/node@^24`, `@types/react@^19`, `@types/react-dom@^19`, `@types/ws@^8.18.1` |
| **ESLint** | `eslint@^9`, `eslint-config-next@15.3.3`, `@eslint/eslintrc@^3` |
| **Prettier** | `prettier@^3.5.3`, `prettier-plugin-tailwindcss@^0.6.12` |
| **Testing** | `jest@^30`, `ts-jest@^29.4.0`, `@types/jest@^30` |
| **Database** | `tsx@^4.20.3`, `shx@^0.4.0` |
| **Supabase** | `supabase@^2.26.9` |

---

## Database Schema (Prisma)

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  name          String?
  password      String?   // hashed
  image         String?
  role          Role      @default(READER)
  emailVerified DateTime?
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  accounts      Account[]
  sessions      Session[]
  comics        Comic[]
  chapters      Chapter[]
  comments      Comment[]
  ratings       Rating[]
  readingHistory ReadingHistory[]
  notifications Notification[]
}

model Comic {
  id          String   @id @default(cuid())
  title       String
  slug        String   @unique
  description String?
  coverImage  String?
  authorId    String
  author      User     @relation(fields: [authorId], references: [id])
  genre       Genre?
  status      ComicStatus @default(ONGOING)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  chapters    Chapter[]
  ratings     Rating[]
  comments    Comment[]
  follows     Follow[]
}

model Chapter {
  id        String   @id @default(cuid())
  comicId   String
  comic     Comic    @relation(fields: [comicId], references: [id], onDelete: Cascade)
  number    Float
  title     String?
  pages     String[] // Image URLs
  published Boolean  @default(false)
  publishedAt DateTime?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  readingHistory ReadingHistory[]
}

enum Role { ADMIN EDITOR READER }
enum ComicStatus { ONGOING COMPLETED HIATUS DROPPED }
```

---

## Authentication Flow

```
1. User visits /login
2. NextAuth.js handles:
   - Credentials (email/password + bcrypt)
   - OAuth (Google, GitHub, Discord)
3. JWT strategy with secure httpOnly cookies
4. Middleware protects /dashboard/*, /library/*, /admin/*
5. Session accessed via auth() in Server Components
```

---

## Payment Integration

### Stripe (Primary)
- **Subscriptions**: Monthly/Yearly plans for premium access
- **Webhooks**: `/api/webhooks/stripe` → Upstash QStash → Workflow
- **Customer Portal**: Stripe Billing Portal for self-service

### PayPal (Secondary)
- **@paypal/react-paypal-js** for client-side buttons
- **Server-side**: PayPal SDK for order capture
- **Use case**: Regions where Stripe unavailable

---

## Real-time Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │◀───▶│  WebSocket  │◀───▶│  Upstash    │
│  (Browser)  │     │   Server    │     │  Redis      │
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    ┌──────▼──────┐
                    │  Workflow   │
                    │  (QStash)   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Notification│
                    │  Service    │
                    └─────────────┘
```

- **ws** library for WebSocket server
- **Upstash Redis** for pub/sub and presence
- **QStash** for reliable webhook delivery
- **Workflow** for multi-step background jobs

---

## File Upload (UploadThing)

```typescript
// lib/uploadthing.ts
export const ourFileRouter = {
  comicCover: f({ image: { maxFileSize: "4MB", maxFileCount: 1 } })
    .middleware(async ({ req }) => { /* auth check */ })
    .onUploadComplete(async ({ metadata, file }) => { /* save URL */ }),

  chapterImages: f({ image: { maxFileSize: "8MB", maxFileCount: 50 } })
    .middleware(async ({ req }) => { /* auth + comic ownership */ })
    .onUploadComplete(async ({ metadata, file }) => { /* process images */ }),
};
```

---

## Commands

```bash
# Install
npm install

# Setup
cp .env.example .env
npx prisma migrate dev
npm run db:seed

# Development
npm run dev              # Next.js + Turbopack

# Database
npm run db:generate      # prisma generate
npm run db:push          # prisma db push
npm run db:migrate       # prisma migrate dev
npm run db:studio        # prisma studio
npm run db:seed          # tsx prisma/seed.ts

# Quality
npm run lint             # next lint
npm run format           # prettier --write
npm run format:check     # prettier --check

# Testing
npm run test             # jest
npm run test:watch       # jest --watch

# Build
npm run build            # next build
npm run start            # next start

# Email dev
npm run dev:email        # react-email dev server
npm run dev:upstash      # qstash dev CLI
```

---

## Project Structure

```
rhixe_scans/
├── src/
│   ├── app/                    # App Router pages
│   │   ├── (auth)/            # Auth route group
│   │   ├── (dashboard)/       # Protected routes
│   │   ├── api/               # API routes
│   │   │   ├── auth/          # NextAuth endpoints
│   │   │   ├── webhooks/      # Stripe/PayPal/UploadThing
│   │   │   └── comics/        # Comic CRUD
│   │   ├── library/           # User library
│   │   ├── reading/           # Reader view
│   │   └── admin/             # Admin panel
│   ├── components/
│   │   ├── ui/               # shadcn/ui components
│   │   ├── comics/           # Comic-specific
│   │   ├── reader/           # Reading components
│   │   └── forms/            # Form components
│   ├── lib/
│   │   ├── auth.ts           # NextAuth config
│   │   ├── db.ts             # Prisma client
│   │   ├── stripe.ts         # Stripe client
│   │   ├── upstash.ts        # Redis/QStash clients
│   │   ├── uploadthing.ts    # UploadThing router
│   │   ├── email.ts          # Resend client
│   │   └── utils.ts          # cn(), formatters
│   ├── hooks/                # Custom hooks
│   ├── types/                # TypeScript types
│   └── validations/          # Zod schemas
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
├── public/
├── emails/                   # React Email templates
├── .env.example
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── eslint.config.mjs
├── .prettierrc
├── jest.config.ts
├── package.json
└── package-lock.json
```

---

## CI/CD Pipeline

**Workflow:** `.github/workflows/rhixe_scans-ci.yml`

1. **Install** → `npm ci`
2. **Type Check** → `npx tsc --noEmit`
3. **Lint** → `npm run lint`
4. **Format Check** → `npm run format:check`
5. **Test** → `npm run test`
6. **Build** → `npm run build`
7. **Deploy** → Vercel (on merge to `staged`)

---

## License Summary

| License | Packages |
|---------|----------|
| MIT | ~70 |
| Apache 2.0 | ~10 |
| ISC | ~3 |
| BSD | ~2 |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*