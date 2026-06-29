# rhixe_scans — Comic Reader

## Architecture
- **Type:** Next.js comic reader platform
- **Pattern:** App Router with Prisma, multiple payment providers, real-time features
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Next.js 15 + TypeScript + Prisma 6 + Tailwind CSS + Stripe/PayPal. Full-featured comic reader with uploads, WebSocket notifications, subscriptions, and admin dashboard.

## Stack
- **Frontend:** React 19, TypeScript (strict), Tailwind 3 + Radix/shadcn/ui
- **State:** Zustand, TanStack Query
- **Database:** Prisma 6 / PostgreSQL
- **Auth:** NextAuth v5
- **Media:** UploadThing
- **Realtime:** WebSocket
- **Payments:** Stripe, PayPal
- **Email:** Resend
- **Deploy:** Vercel or Docker

## Commands
```bash
npm install
cp .env.example .env
npx prisma migrate dev && npm run db:seed
npm run dev
npm run lint && npx prettier --write .
npx prisma generate
npm test
```

## Build
```bash
npm run clean && npm run build && npm start
```

## Conventions
- **Naming:** PascalCase for components, camelCase for hooks/utils, kebab-case for pages
- **Validation:** Zod schemas for all API inputs
- **Styling:** `cn()` utility + CVA for component variants
- **Migrations:** Use `prisma migrate dev` (not `db:push`) for schema changes
- **Secrets:** `.env` never committed; use `.env.example` as template

## Notes
- Dual payment providers: Stripe (primary) + PayPal (secondary)
- WebSocket for real-time chapter release notifications
- UploadThing for comic image uploads
- Resend for transactional emails
