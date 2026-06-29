# Project Workflow — rhixe_scans

## Development Workflow

```bash
# Setup
npm install
cp .env.example .env
npx prisma migrate dev
npm run db:seed

# Development
npm run dev                    # Turbopack dev server
npm run lint                   # ESLint
npx prettier --write .         # Format

# Database Changes
# Edit prisma schema → npx prisma migrate dev --name desc
npm run db:seed                # Re-seed

# Testing
npm test                       # Jest tests
npm run test:watch             # Watch mode

# Build
npm run clean
npm run build
npm start
```

## Adding a Feature
1. Update Prisma schema → 2. Generate migration → 3. Create server action → 4. Build component
