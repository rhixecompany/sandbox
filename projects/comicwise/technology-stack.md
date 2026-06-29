# Technology Stack — comicwise

## Overview

Next.js-based comic streaming frontend with TypeScript, Tailwind CSS, Prisma ORM, and NextAuth v5.

## Frontend

| Technology | Version | Purpose |
| --- | --- | --- |
| Next.js | 16.1.6 | React framework (App Router, Turbopack) |
| React | 19.2.4 | UI library |
| TypeScript | 5.9.3 | Type safety |
| Tailwind CSS | 4.0.0 | Utility-first styling |
| shadcn/ui | 4.0.6 | Component library |
| Zustand | 5.0.11 | State management |
| Zod | 4.3.6 | Schema validation |
| React Hook Form | 7.71.2 | Form handling |
| TanStack Query | 5.90.21 | Data fetching |
| TanStack Table | 8.21.3 | Data tables |
| Recharts | 3.8.0 | Charts |

## Backend & Database

| Technology    | Version       | Purpose               |
| ------------- | ------------- | --------------------- |
| NextAuth v5   | 5.0.0-beta.30 | Authentication        |
| Drizzle ORM   | 0.45.1        | Database ORM          |
| PostgreSQL    | —             | Database              |
| Upstash Redis | 1.37.0        | Rate limiting/caching |
| BullMQ        | 5.71.0        | Job queues            |

## Integrations

| Integration | Purpose            |
| ----------- | ------------------ |
| ImageKit    | Image optimization |
| Cloudinary  | Image storage      |
| Stripe      | Payment processing |
| Resend      | Email delivery     |
| Sentry      | Error tracking     |

## Dev & Quality

| Tool       | Version | Purpose         |
| ---------- | ------- | --------------- |
| pnpm       | —       | Package manager |
| ESLint     | 9.0.0   | Linting         |
| Prettier   | 3.8.1   | Formatting      |
| Vitest     | 4.1.0   | Testing         |
| Playwright | 1.58.2  | E2E testing     |
| Husky      | 9.1.7   | Git hooks       |
