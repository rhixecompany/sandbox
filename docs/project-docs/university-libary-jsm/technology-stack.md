# Technology Stack — university-libary-jsm

## Overview
University Library Management System (BookWise) with Next.js 15, Drizzle ORM, Neon PostgreSQL, Upstash Redis, and ImageKit.

## Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| Next.js | 15.x (Turbopack) | React framework |
| React | 19.x | UI library |
| TypeScript | 5.x | Type safety |
| Tailwind CSS | 4.x | Utility-first styling |
| shadcn/ui | — | Component library (Radix UI primitives) |
| TanStack Table | 8.21.3 | Data tables |
| Recharts | — | Charts |
| Lucide React | — | Icons |
| Framer Motion | — | Animations |

## Backend & Database
| Technology | Version | Purpose |
|------------|---------|---------|
| Drizzle ORM | — | Database ORM with Zod integration |
| Neon PostgreSQL | — | Serverless PostgreSQL |
| Upstash Redis | 1.37.0 | Rate limiting |
| Upstash Workflow | — | Async job processing |
| QStash | — | Job queue messaging |

## Auth & Storage
| Technology | Purpose |
|------------|---------|
| NextAuth v5 (beta) | Authentication |
| ImageKit | Image uploads/storage |
| React Email + Nodemailer | Email delivery |

## Dev & Quality
| Tool | Purpose |
|------|---------|
| ESLint 9 | Linting with Drizzle, Zod, JSX-a11y plugins |
| Prettier | Code formatting |
| TypeScript strict mode | Type safety |

## Key Features
- Book request management
- User account management
- Admin workflow processing
- Email notifications
- Rate limiting
- Server Actions for mutations
