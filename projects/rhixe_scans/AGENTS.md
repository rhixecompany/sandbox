# rhixe_scans — Comic Reader
## Architecture

- **Blueprint**: [rhixe_scans Architecture](../docs/Project_Architecture/rhixe_scans_architecture.md)
- **Folders**: [rhixe_scans Folder Structure](../docs/Project_Architecture/rhixe_scans_folders.md)
- **Tech Stack**: [rhixe_scans Technology Stack](../docs/Project_Architecture/rhixe_scans_techstack.md)
- **Stack Type**: Next.js


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
