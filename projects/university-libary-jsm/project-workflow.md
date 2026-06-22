# Project Workflow — university-libary-jsm

## Development

```bash
# Setup
npm install
cp .env.example .env
npm run db:push
npm run db:seed

# Development
npm run dev                    # Turbopack dev server
npm run lint                   # ESLint
npm run format                 # Prettier

# Database Changes
# Edit database/schema.ts → npm run db:generate → npm run db:migrate
npm run db:studio              # Browse database

# Email preview
npm run dev:email

# Build
npm run build
npm start
```

## Adding a Feature
1. Add schema to `database/schema.ts`
2. Generate migration: `npm run db:generate`
3. Apply migration: `npm run db:migrate`
4. Create Server Action in `src/actions/`
5. Build React component
6. Add page route in `src/app/`
