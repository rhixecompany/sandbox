# Folder Structure — comicwise

```
comicwise/
├── .github/                    # GitHub workflows
├── .husky/                     # Git hooks
├── public/                     # Static assets
├── src/
│   ├── actions/                # Server Actions
│   ├── app/                    # Next.js App Router pages
│   ├── components/             # React components
│   │   └── ui/                 # shadcn/ui components
│   ├── db/                     # Drizzle schema & queries
│   ├── hooks/                  # Custom React hooks
│   ├── lib/                    # Utilities
│   ├── scripts/                # Build/dev scripts
│   │   ├── seed/               # Database seeding
│   │   └── ...                 # Various utility scripts
│   ├── stores/                 # Zustand state stores
│   └── types/                  # TypeScript definitions
├── .env.example                # Environment template
├── drizzle.config.ts           # Drizzle configuration
├── next.config.ts              # Next.js configuration
├── package.json                # Dependencies & scripts
├── playwright.config.ts        # Playwright configuration
├── tsconfig.json               # TypeScript configuration
├── vitest.config.ts            # Vitest configuration
└── AGENTS.md                   # Agent reference guide
```
