# Quick Start Guide - ComicWise Development

**TL;DR:** Get ComicWise running in 30 seconds

## 1️⃣ Install Dependencies

```bash
pnpm install
```

## 2️⃣ Configure Database

### Option A: Local PostgreSQL (Recommended for Development)

```bash
# Ensure PostgreSQL is running
# Windows: Start PostgreSQL service
# macOS: brew services start postgresql
# Linux: sudo systemctl start postgresql

# Create database
psql -U postgres -c "CREATE DATABASE comicbook;"
psql -U postgres -c "CREATE USER comicwise WITH PASSWORD 'dev123';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE comicbook TO comicwise;"
```

### Option B: Neon Cloud (Free tier available)

1. Sign up: [https://console.neon.tech](https://console.neon.tech)
2. Create project and copy connection string

## 3️⃣ Setup Environment

```bash
# Copy template
cp .env.local.example .env.local

# Edit .env.local:
# - DATABASE_URL="postgresql://comicwise:dev123@localhost:5432/comicbook"
# - AUTH_SECRET=(run: openssl rand -hex 32)
```

## 4️⃣ Run Migrations

```bash
pnpm db:push
```

## 5️⃣ Start Development Server

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser ✅

---

## Helpful Commands

```bash
# Type checking
pnpm type-check

# Linting & formatting
pnpm lint:fix

# Run tests
pnpm test

# Database migration status
pnpm db:migration-status

# Reset database (development only)
pnpm db:reset && pnpm db:push

# View database in browser
# (if using Neon: https://console.neon.tech)
```

---

## Common Issues

### "Connection refused"

→ PostgreSQL not running. Try: `brew services start postgresql` (macOS) or start service (Windows)

### "password authentication failed"

→ Wrong database credentials. Check `.env.local` DATABASE_URL

### "Database does not exist"

→ Run setup commands above to create database

### TypeScript errors

→ Run `pnpm type-check` and `pnpm lint:fix`

---

## Full Setup (with Guide)

For detailed instructions: [DATABASE_SETUP.md](DATABASE_SETUP.md)

Setup checklist: [DEV_SETUP_CHECKLIST.md](DEV_SETUP_CHECKLIST.md)

---

## Next Steps

✅ Server running?

1. **Explore the app:**
   - [http://localhost:3000](http://localhost:3000) - Main page
   - [http://localhost:3000/auth/signin](http://localhost:3000/auth/signin) - Login page

2. **Read the code:**
   - `src/app/` - Pages & routes
   - `src/dal/` - Database access layer
   - `src/actions/` - Server actions
   - `src/components/` - React components

3. **Start developing:**
   - [View Implementation Master Plan](IMPLEMENTATION_MASTER.md)
   - [Code Review Guidelines](../.github/instructions/code-review.instructions.md)
   - [TypeScript Standards](../.github/instructions/typescript.instructions.md)

---

**Questions?** Check the docs folder or the GitHub issues
