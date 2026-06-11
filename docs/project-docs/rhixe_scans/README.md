# rhixe_scans — Comic Reading Platform

A full-featured web application for reading comics online with Stripe/PayPal payment integration.

## Tech Stack
- **Frontend**: Next.js 15, React 19, TypeScript, Tailwind CSS 3, Radix UI
- **Database**: PostgreSQL via Prisma ORM 6
- **Auth**: NextAuth v5
- **Payments**: Stripe + PayPal
- **Storage**: UploadThing

## Quick Start
```bash
npm install
cp .env.example .env
npx prisma migrate dev
npm run db:seed
npm run dev
```

## Documentation Links
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Code Exemplars](code-exemplars.md)
