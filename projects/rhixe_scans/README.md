# rhixe_scans — Comic/Manga Reader Platform

> **Stack:** Next.js 15 + Prisma 6 | **Type:** Full-Stack Comic Reader | **Status:** Active

A full-featured comic/manga reading platform built with Next.js 15, featuring Prisma 6 ORM, authentication, dual payment processing (Stripe + PayPal), file uploads via UploadThing, and real-time capabilities.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Next.js ^15.3.3 (App Router) |
| **Language** | TypeScript ^5 (strict) |
| **UI** | React 19, Radix UI, shadcn/ui, Tailwind CSS 3.4 |
| **State/Data** | TanStack Query, Zustand, TanStack Table |
| **Database** | PostgreSQL via Prisma 6 |
| **Authentication** | NextAuth v5 (beta), Supabase |
| **Payments** | Stripe, PayPal |
| **File Uploads** | UploadThing |
| **Email** | Resend, React Email |
| **Real-time** | WebSocket (ws) |
| **Testing** | Jest + ts-jest |

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│              rhixe_scans (Next.js 15)                     │
├──────────────────────────────────────────────────────────┤
│  App Router Pages                                        │
│  ├── /                    Browse comics                   │
│  ├── /comics/[id]        Reader interface                 │
│  ├── /auth               NextAuth v5                      │
│  ├── /account            User settings                    │
│  └── /admin              Administration                   │
├──────────────────────────────────────────────────────────┤
│  Core Services                                            │
│  ├── Prisma 6 → PostgreSQL                                │
│  ├── NextAuth v5                                          │
│  ├── Stripe + PayPal                                     │
│  ├── UploadThing (file uploads)                           │
│  ├── Resend (email)                                       │
│  └── WebSocket (real-time)                                │
├──────────────────────────────────────────────────────────┤
│  Quality                                                  │
│  ├── Jest + ts-jest                                       │
│  ├── ESLint + Next eslint config                          │
│  └── Prettier + Tailwind plugin                          │
└──────────────────────────────────────────────────────────┘
```

## Project Structure

```
rhixe_scans/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── (auth)/          # Authentication routes
│   │   ├── comics/          # Comic browsing & reader
│   │   ├── account/         # User settings
│   │   ├── admin/           # Admin panel
│   │   └── api/             # API routes
│   ├── components/          # React components
│   ├── db/                  # Prisma schema
│   │   └── schema.prisma    # Database schema
│   ├── lib/                 # Utilities & seed
│   └── styles/              # Global styles
├── public/                  # Static assets
├── tests/                   # Jest test files
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Prerequisites: Node.js 18+, PostgreSQL

# Install dependencies
npm install

# Set up environment
cp .env.example .env
# Configure database, Stripe, PayPal, and other credentials

# Database setup
npx prisma migrate dev
npm run db:seed

# Start development
npm run dev

# Run tests
npm test

# Lint and format
npm run lint
npx prettier --write .
```

## Key Features

- **Comic Browsing** — Browse and discover comics/manga
- **Reader Interface** — Immersive reading experience
- **Dual Payments** — Stripe + PayPal payment processing
- **User Authentication** — NextAuth v5 with Supabase options
- **File Uploads** — UploadThing integration for comic uploads
- **Real-time Updates** — WebSocket-based notifications
- **Admin Panel** — Full administration features
- **Email Notifications** — Resend-powered email delivery

## Development Workflow

```bash
npm run dev              # Next.js dev with Turbopack
npm run build            # Production build
npm run lint             # ESLint
npm run db:migrate       # Prisma migrations
npm run db:seed          # Database seeding
npm run db:studio        # Prisma Studio
npm test                 # Jest tests
npm run clean            # Clean build artifacts
```

## Coding Standards

- **TypeScript strict**: Full type safety
- **Components**: PascalCase naming
- **Hooks/Utils**: camelCase naming
- **Pages**: kebab-case naming
- **Zod validation**: Schema validation at boundaries
- **`cn()` utility**: Tailwind class merging with CVA
- **shadcn/ui**: Radix-based component library
- **Migrations**: Use `prisma migrate` (not `db:push` in production)

## Security

- No `.env` in VCS
- Zod validation at all boundaries
- Stripe/PayPal keys server-side only
- Prisma parameterized queries prevent SQL injection
- Rate limiting configured
- HTTPS required

## Deployment

| Platform | Notes |
|---|---|
| **Vercel** | Primary deployment target |
| **Docker** | Available as alternative |

## License

Private
