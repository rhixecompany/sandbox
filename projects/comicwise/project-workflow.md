# Project Workflow — comicwise

## Development Workflow

```bash
1. Local Setup
   npm install                    # or pnpm install
   cp .env.example .env
   npx prisma migrate dev
   npm run db:seed

2. Development
   npm run dev                    # Turbopack dev server
   npm run format                 # Prettier format
   npm run lint                   # ESLint

3. Database Changes
   # Edit schema in src/db/
   npx prisma migrate dev --name description
   npm run db:seed                # Re-seed after schema changes

4. Quality Checks
   npx tsc --noEmit               # TypeScript check
   npm run lint:strict            # Zero-warnings linting
   npm test                       # Run all tests

5. Build & Deploy
   npm run build                  # Production build
   npm start                      # Production server
```

## Adding a Feature
1. Create DB schema/migration → 2. Create Server Action → 3. Create component → 4. Add route page

## Git Workflow
- Feature branches from `main`
- PR requires lint + type-check + tests passing
- Husky pre-commit hooks run lint-staged
