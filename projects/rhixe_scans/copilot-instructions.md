# rhixe_scans
**TS/React**: strict TS, PascalCase components, `camelCase` utilities, shadcn/ui, React Hook Form + Zod.
**DB**: Prisma schema-first; always generate migrations; NextAuth v5 adapter.
**Style**: Tailwind + `cn()`/`class-variance-authority`; TanStack Query; Zustand; `@dnd-kit`, `recharts`.
**Naming**: PascalCase components, camelCase hooks/utils, kebab-case pages.
**Security**: no `.env`; Zod at boundaries; Stripe/PayPal keys server-side only; Prisma prevents SQL injection; rate limiting; HTTPS.
