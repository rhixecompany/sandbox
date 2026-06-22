# Folder Structure — university-libary-jsm

```
university-libary-jsm/
├── email/                       # React Email templates
├── public/                      # Static assets
├── src/
│   ├── actions/                 # Server Actions (dot.camelCase)
│   ├── app/                     # Next.js App Router
│   │   ├── (auth)/              # Auth routes
│   │   ├── (dashboard)/         # Main app pages
│   │   └── api/                 # API routes
│   ├── components/              # React components
│   │   └── ui/                  # shadcn/ui components
│   ├── database/                # Drizzle schema & config
│   ├── hooks/                   # Custom React hooks
│   ├── lib/                     # Utilities
│   └── types/                   # TypeScript definitions
├── .env.example                 # Environment template
├── drizzle.config.ts            # Drizzle configuration
├── next.config.ts               # Next.js configuration
├── package.json                 # Dependencies
├── tailwind.config.ts           # Tailwind configuration
├── tsconfig.json                # TypeScript configuration
└── AGENTS.md                    # Agent reference guide
```
