# university-libary-jsm — Folder Structure

> **Stack:** Next.js 15 + Drizzle ORM + Neon  
> **Type:** Full-Stack Library Management System  
> **Status:** Active

## Directory Tree

```
university-libary-jsm/
├── .github/workflows/
├── .vscode/
├── app/                          # Next.js App Router
│   ├── (auth)/                   # Auth route group
│   │   ├── sign-in/
│   │   └── sign-up/
│   ├── (root)/                   # Main app route group
│   │   ├── books/
│   │   ├── library/
│   │   └── my-profile/
│   ├── admin/                    # Admin panel
│   │   ├── account-requests/
│   │   ├── book-requests/
│   │   ├── books/
│   │   └── users/
│   ├── api/                      # API routes
│   │   ├── auth/
│   │   ├── imagekit/
│   │   └── workflows/
│   ├── fonts/                    # Font assets
│   ├── too-fast/                 # Rate-limit indicator
│   └── unauthorized/             # Unauthorized page
├── assets/                       # Project assets
├── components/                   # React components
│   ├── admin/
│   │   ├── books/
│   │   └── forms/
│   └── ui/                       # Shadcn/ui primitives
├── constants/                    # App constants
├── database/                     # Drizzle ORM schemas
├── docs/
├── emails/                       # Email templates (react-email)
├── hooks/                        # React hooks
├── lib/                          # Shared utilities
│   ├── actions/                  # Server Actions
│   ├── admin/actions/            # Admin server actions
│   └── queries/                  # Database query helpers
├── migrations/                   # Drizzle migrations
│   └── meta/
├── public/
│   ├── icons/                    # Icon assets
│   │   └── admin/
│   └── images/                   # Image assets
├── styles/                       # Global styles
├── package.json
├── tsconfig.json
└── ...
```

## Key Patterns

- **Next.js App Router** with route groups `(auth)`, `(root)`
- **Server Actions** in `lib/actions/` (user-facing) and `lib/admin/actions/` (admin)
- **Database queries** separated into `lib/queries/`
- **Components organized** by domain (`admin/books/`, `admin/forms/`) with generic `ui/` primitives
- **React-email** templates in `emails/`
- **Drizzle ORM** with `database/` schema + `migrations/`
