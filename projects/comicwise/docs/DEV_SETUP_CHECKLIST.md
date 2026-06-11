# Development Environment Checklist

## Pre-Setup Requirements

- [ ] Node.js 18+ installed (`node -v`)
- [ ] pnpm installed (`npm install -g pnpm`)
- [ ] PostgreSQL 14+ or Neon.tech account
- [ ] VS Code with extensions (optional):
  - [ ] Drizzle ORM extension
  - [ ] Thunder Client or Postman for API testing
  - [ ] PostgreSQL extension for DB browsing

## Phase 1: Environment Setup (15 min)

### Step 1: Copy Environment Template

```bash
cp .env.local.example .env.local
```

- [ ] Copied `.env.local.example` to `.env.local`

### Step 2: Install Dependencies

```bash
pnpm install
```

- [ ] All npm dependencies installed
- [ ] node_modules directory created
- [ ] pnpm-lock.yaml validated

### Step 3: Database Configuration

**Choose Option A (Local) or Option B (Cloud):**

#### Option A: Local PostgreSQL

```bash
# Create database
psql -U postgres
CREATE DATABASE comicbook;
CREATE USER comicwise WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE comicbook TO comicwise;
\q
```

- [ ] PostgreSQL service running (`pg_isready`)
- [ ] Database `comicbook` created
- [ ] User `comicwise` created with privileges
- [ ] Connection string: `postgresql://comicwise:password@localhost:5432/comicbook`

#### Option B: Neon Cloud

1. [ ] Created account at neon.tech
2. [ ] Created new project
3. [ ] Copied connection string
4. [ ] Connection string: `postgresql://...@...neon.tech/comicbook`

### Step 4: Configure .env.local

Edit `.env.local`:

```env
DATABASE_URL="postgresql://user:pass@host:5432/comicbook"
AUTH_SECRET="<32+ character secret from openssl rand -hex 32>"
NODE_ENV="development"
```

- [ ] `DATABASE_URL` set correctly
- [ ] `AUTH_SECRET` generated (min 32 chars)
- [ ] `NODE_ENV` set to "development"

## Phase 2: Database Migrations (10 min)

### Step 1: Verify Connection

```bash
psql $DATABASE_URL -c "SELECT version();"
```

- [ ] Database connection successful
- [ ] PostgreSQL version displayed

### Step 2: Run Migrations

```bash
pnpm db:push
```

- [ ] No migration errors
- [ ] All tables created

### Step 3: Verify Schema

```bash
psql $DATABASE_URL -c "\dt"
```

- [ ] Schema contains 30+ tables
- [ ] Tables include: comic, chapter, bookmark, rating, comment, user, etc.

View table structure:

```bash
psql $DATABASE_URL -c "\d comic"
```

- [ ] Primary keys correct
- [ ] Foreign keys present
- [ ] Enums defined (comicStatus, userRole, etc.)

## Phase 3: Type Checking & Validation (10 min)

```bash
pnpm type-check
```

- [ ] Zero TypeScript errors
- [ ] All DAL classes compile

```bash
pnpm lint:fix
```

- [ ] ESLint errors fixed
- [ ] Prettier formatting applied

```bash
pnpm test
```

- [ ] Unit tests pass (if any)
- [ ] Vitest configured

## Phase 4: Development Server (5 min)

```bash
pnpm dev
```

- [ ] Next.js dev server started on http://localhost:3000
- [ ] No build errors in terminal
- [ ] Page loads without errors in browser

### Verify API Routes

```bash
curl http://localhost:3000/api/health
```

- [ ] Health check endpoint responds
- [ ] Response is JSON

## Phase 5: Authentication Testing (10 min)

Visit http://localhost:3000/auth/signin

- [ ] Sign-in page loads
- [ ] Form accepts email input
- [ ] Form accepts password input
- [ ] Submit button is clickable

If database is seeded:

- [ ] Login with test account succeeds
- [ ] Redirect to dashboard works
- [ ] Session cookie created

## Phase 6: Database Testing (5 min)

Test DAL operations:

```bash
# Open Node REPL in project
node --loader tsx
```

```typescript
import { comicDal } from "@/dal/comic-dal";
const comics = await comicDal.list({ limit: 5 });
console.log(comics);
```

- [ ] Query returns results without errors
- [ ] Data structure matches type definitions

## Post-Setup Tasks

### Optional: Seed Test Data

```bash
pnpm seed
```

- [ ] Seed script runs without errors
- [ ] Database populated with test comics/chapters
- [ ] Can login with seeded test account

### Bookmark in Docs

- [ ] [DATABASE_SETUP.md](../docs/DATABASE_SETUP.md) bookmarked
- [ ] Understand local vs. cloud setup
- [ ] Know how to reset database (`pnpm db:reset`)

## Troubleshooting

### If `pnpm db:push` fails:

```bash
# Check migration status
pnpm db:migration-status

# If schema drift detected:
pnpm db:reset
pnpm db:push
```

### If TypeScript errors occur:

```bash
# Ensure all files saved
# Run type-check again
pnpm type-check

# Clear .next cache
rm -rf .next
pnpm build
```

### If dev server won't start:

```bash
# Check port 3000 not in use
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Try different port
pnpm dev -- -p 3001
```

## Final Verification Checklist

- [ ] `pnpm type-check` returns 0 errors
- [ ] `pnpm lint:fix` applies no changes
- [ ] `pnpm dev` starts without errors
- [ ] http://localhost:3000 loads in browser
- [ ] Database has all 30+ tables
- [ ] Auth flow works end-to-end

## Expected Time: 45-60 minutes

If setup takes longer, refer to troubleshooting or ask in #dev-help

---

**Setup Complete?** Next: Read [IMPLEMENTATION_MASTER.md](../docs/IMPLEMENTATION_MASTER.md) for feature development
