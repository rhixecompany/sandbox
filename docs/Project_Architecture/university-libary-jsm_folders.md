# university-libary-jsm — Folder Structure

```
university-libary-jsm/
├── app/                  # Next.js App Router pages
├── assets/               # Static assets
├── components/           # shadcn/ui + Radix UI components
├── constants/            # Application constants
├── database/             # Drizzle schema, migrations, seeds
├── docs/                 # Documentation
├── emails/               # React Email templates
├── hooks/                # Custom React hooks
├── lib/                  # Utility functions
├── migrations/           # Database migration files
├── node_modules/         # Dependencies
├── public/               # Public static files
├── styles/               # CSS and Tailwind styles
├── middleware.ts         # Next.js middleware (auth)
├── next.config.ts       # Next.js configuration
├── drizzle.config.ts    # Drizzle configuration
├── next-auth.d.ts       # NextAuth type declarations
├── types.d.ts           # TypeScript type declarations
├── package.json         # Node dependencies
└── tsconfig.json        # TypeScript config
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `app/` | Next.js App Router pages, layouts, API routes |
| `components/` | Reusable UI components (shadcn/ui) |
| `database/` | Drizzle ORM schema definitions and migrations |
| `lib/` | Shared utilities, API clients, helpers |
| `emails/` | Transactional email templates |
