# rhixe_scans — Comic Reader

Next.js 15 + TypeScript + Prisma 6 + Tailwind + Stripe/PayPal.

## Stack
- React 19, TypeScript strict
- Tailwind 3 + Radix/`shadcn/ui`; Zustand, TanStack Query
- Prisma 6 / PostgreSQL; NextAuth v5
- UploadThing, Resend, WebSocket, Stripe/PayPal

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

## Notes
- Deploy: Vercel or Docker
- PascalCase components; camelCase hooks/utils; kebab-case pages
- Zod validation; `cn()` + CVA; `db:push` not typical; use migrations
