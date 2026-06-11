# 🤖 AI Agent Setup & Instructions - ComicWise Project

**Status**: ✅ Complete | **Date**: Phase 3.5 | **Quality**: All Gates Passing

---

## Overview

This is the definitive documentation package for working on ComicWise with AI agents (GitHub Copilot, Claude, Cursor Composer, etc.). It describes the project structure, patterns, and all guidance systems available.

---

## 📚 Start Here

### For Quick Start (5 minutes)

👉 **Read**: `docs/QUICK_START.md`

### For Complete Project Overview (10 minutes)

👉 **Read**: `AGENTS.md`

### For Full AI Agent Guidance (10 minutes)

👉 **Read**: `.github/AI_AGENT_SETUP_GUIDE.md`

### For Comprehensive Developer Reference (30+ minutes)

👉 **Read**: `.github/copilot-instructions.md`

---

## 📖 Documentation Structure

```
ComicWise Documentation/
│
├── QUICK REFERENCE (5-10 min reads)
│   ├── docs/QUICK_START.md              ← Start here
│   ├── AGENTS.md                        ← Project overview
│   └── .github/AI_AGENT_SETUP_GUIDE.md  ← AI guidance (NEW)
│
├── COMPREHENSIVE GUIDES (30-60 min reads)
│   ├── .github/copilot-instructions.md  ← 800+ lines complete ref
│   ├── docs/dev.content.md              ← 26 sections with examples
│   ├── docs/database-context-map.md     ← Schema relationships
│   └── docs/PHASE3-5-COMPLETE-SESSION.md ← Latest features
│
├── PATTERN-SPECIFIC FILES (As needed)
│   └── .github/instructions/            ← 16 auto-loaded guides
│       ├── typescript.instructions.md
│       ├── nextjs-2026.instructions.md
│       ├── reactjs.instructions.md
│       ├── testing.instructions.md
│       ├── security-and-owasp.instructions.md
│       └── ... (11 more)
│
├── WORKFLOW AUTOMATION (On demand)
│   └── .github/skills/                  ← 15 custom skills
│       ├── polyglot-test-agent/
│       ├── architecture-blueprint-generator/
│       └── ... (13 more)
│
└── PROJECT STATUS & REPORTS
    ├── docs/AI_AGENT_SETUP_COMPLETION_REPORT.md (NEW)
    └── docs/PHASE3-5-COMPLETE-SESSION.md (NEW)
```

---

## 🎯 What Each File Is For

| File | Read Time | Purpose |
| --- | --- | --- |
| `docs/QUICK_START.md` | 5 min | 30-second setup guide |
| `AGENTS.md` | 5 min | Project overview & phases |
| `.github/AI_AGENT_SETUP_GUIDE.md` | 10 min | Complete AI agent reference (NEW) |
| `.github/copilot-instructions.md` | 30 min | Comprehensive developer guide |
| `docs/dev.content.md` | 45 min | 26 sections with code examples |
| `.github/instructions/*` | As needed | Pattern-specific guidance |
| `docs/database-context-map.md` | 15 min | Database schema explanation |
| `docs/PHASE3-5-COMPLETE-SESSION.md` | 20 min | Phase 3.5 feature docs |
| `docs/AI_AGENT_SETUP_COMPLETION_REPORT.md` | 15 min | Session report & summary |

---

## 🚀 Quick Reference

### Setup & Run

```bash
# Install and setup
pnpm install
cp .env.local.example .env.local    # Edit with your env vars
pnpm db:push
pnpm dev

# Access on http://localhost:3000
```

### Quality Gates (Before Every PR)

```bash
pnpm type-check          # Must be 0 errors
pnpm lint:fix            # ESLint + Prettier
pnpm test                # Vitest unit tests (186/186)
pnpm build               # Production build
```

### Common Commands

```bash
# Development
pnpm dev                 # Start dev server
pnpm dev --turbo         # With Turbopack beta features

# Database
pnpm db:push            # Apply schema changes
pnpm db:studio          # Visual DB editor
pnpm seed:all           # Seed test data

# Testing
pnpm test               # Unit tests
pnpm test:ui            # E2E tests

# Code Quality
pnpm lint:fix           # Fix linting issues
pnpm format             # Format code
pnpm type-check:watch   # Watch mode type-checking
```

---

## 🎓 Learning Path

### Level 1: Understand the Codebase

1. Read `docs/QUICK_START.md` (5 min)
2. Read `AGENTS.md` (5 min)
3. Skim `.github/copilot-instructions.md` sections 1-5 (10 min)

### Level 2: Learn the Patterns

1. Study `.github/copilot-instructions.md` fully (30 min)
2. Review `docs/dev.content.md` sections 1-10 (30 min)
3. Look at example files in `src/app/`, `src/dal/`, `src/actions/` (20 min)

### Level 3: Master the System

1. Deep dive `docs/dev.content.md` sections 11-26 (30 min)
2. Review `.github/instructions/*` files relevant to your task (as needed)
3. Study actual implementations in codebase (30 min)

### Level 4: Contribute Confidently

1. Use `/skill` or `/agent` for complex tasks
2. Follow established patterns from existing code
3. Run quality gates before submitting
4. Reference instruction files during code review

---

## ✨ Key Features of This Setup

### 1. Auto-Loading Instructions

Instruction files automatically apply based on file patterns:

- Edit `.tsx` → TypeScript + React + Next.js instructions apply
- Edit `src/dal/` → Database pattern instructions apply
- Edit `*.test.ts` → Testing instructions apply
- And so on... (16 pattern files total)

**Benefit**: Get relevant guidance automatically without asking

### 2. Custom Skills (On Demand)

Invoke with `/skill <skill-name>`:

```bash
/skill create-implementation-plan    # Plan your feature
/skill polyglot-test-agent          # Generate tests
/skill architecture-blueprint-generator  # Document architecture
/skill refactor                     # Code improvement
# ... 11 more available
```

### 3. Specialized Agents (For Complex Work)

Invoke with `/agent <agent-name>`:

```bash
/agent architect                    # Complex design
/agent Next.js Expert              # Next.js specific
/agent SWE                         # General development
/agent reviewer                    # Code review
/agent Debug Mode Instructions     # Troubleshooting
# ... 9 more available
```

---

## 📊 Project Metrics

### Code Quality

- **Type Errors**: 0 ✅
- **Lint Errors**: 0 ✅
- **Test Coverage**: 186/186 ✅
- **Build Status**: Production Ready ✅

### Architecture

- **Phases Complete**: 1, 2, 3
- **Tables**: 27 (with proper relations)
- **Components**: 50+
- **DAL Classes**: 18
- **Server Actions**: 30+

### Documentation

- **Total Lines**: 8000+
- **Instruction Files**: 16
- **Skills Available**: 15
- **Agents Available**: 14

---

## 🔐 Coding Rules (Enforced)

1. **No `any` types** — ESLint enforces
2. **No manual memoization** — React Compiler handles it
3. **No raw `process.env`** — Use `getEnv()`
4. **No N+1 queries** — Always use `.with()` for eager loading
5. **No API routes for mutations** — Use Server Actions
6. **Async params required** — Next.js v16 breaking change
7. **ActionResult<T> pattern** — Server Actions return typed results
8. **Auth first** — Check `await auth()` first line
9. **Always validate** — Zod validation before DB
10. **Update timestamps** — Every mutation updates `updatedAt`

---

## 📋 Project Structure at a Glance

```
src/
├── app/                    # Pages & routes (Next.js 16 App Router)
├── components/             # React components (Server + Client)
├── dal/                    # Data Access Layer (all queries)
├── actions/                # Server Actions (mutations)
├── database/               # Drizzle ORM + schema (27 tables)
├── schemas/                # Zod validation schemas
├── lib/                    # Utilities & helpers
├── hooks/                  # Custom React hooks
└── scripts/                # CLI tools & seeders

.github/
├── copilot-instructions.md # Complete developer guide
├── AI_AGENT_SETUP_GUIDE.md # AI agent reference (NEW)
├── instructions/           # 16 pattern-specific guides
└── skills/                 # 15 workflow automation scripts

docs/
├── QUICK_START.md          # 30-second setup
├── dev.content.md          # 26 sections with examples
├── database-context-map.md # Schema explanation
├── PHASE3-5-COMPLETE-SESSION.md (NEW)
└── AI_AGENT_SETUP_COMPLETION_REPORT.md (NEW)
```

---

## 🎯 Success Criteria

You'll know you're using this setup correctly when:

✅ Type-check passes (`pnpm type-check` → 0 errors) ✅ Linting passes (`pnpm lint` → no errors) ✅ Tests pass (`pnpm test` → 186/186) ✅ Build succeeds (`pnpm build` → ready for prod) ✅ Code follows patterns from existing files ✅ New code is fully typed (no `any`) ✅ Performance is optimized (images, fonts, etc.) ✅ Security is maintained (Zod validation, auth checks)

---

## 🆘 Troubleshooting

### "I don't know what pattern to use"

→ Check existing code in `src/app/`, `src/dal/`, `src/actions/` for examples

### "I'm getting type errors"

→ Run `pnpm type-check:watch` and fix as you code

### "I need to understand the architecture"

→ Read `docs/dev.content.md` sections 1-5 (15 minutes)

### "I'm stuck on a complex task"

→ Use `/skill create-implementation-plan` to plan it out

### "I need code review guidance"

→ Check `.github/instructions/code-review.instructions.md`

### "The project isn't building"

→ Try `pnpm clean && pnpm install && pnpm db:push && pnpm build`

---

## 📞 Resources

### For AI Agents

- **Start**: `.github/AI_AGENT_SETUP_GUIDE.md`
- **Reference**: `.github/copilot-instructions.md`
- **Examples**: `docs/dev.content.md`

### For Developers

- **Quick Setup**: `docs/QUICK_START.md`
- **Deep Dive**: `.github/copilot-instructions.md`
- **Examples**: `docs/dev.content.md` sections 7-26

### For Architects

- **Design**: Use `/agent architect` or `/skill architecture-blueprint-generator`
- **Schema**: Check `docs/database-context-map.md`
- **Patterns**: See `.github/copilot-instructions.md` sections 10-20

---

## ✅ What's New

### This Session (Phase 3.5 AI Setup)

✅ **AGENTS.md** — Updated with Phase 3.3-3.5 completions ✅ **AI_AGENT_SETUP_GUIDE.md** — Complete AI agent reference (NEW) ✅ **PHASE3-5-COMPLETE-SESSION.md** — Feature documentation (NEW) ✅ **AI_AGENT_SETUP_COMPLETION_REPORT.md** — Session report (NEW)

### Already Complete

✅ Phase 1: Foundation (Auth, DB, Core Patterns) ✅ Phase 2: User Profiles, Comics, Bookmarks ✅ Phase 3: Infrastructure, Scripts, Notifications, Recommendations

### Coming Next

🔄 Phase 4: UI/UX Polish, Advanced Search, Analytics

---

## 🚀 Next Steps

### For Your Next Feature

1. Read relevant instruction files
2. Check existing code for patterns
3. Use `/skill create-implementation-plan` to plan
4. Code following patterns you see
5. Run `pnpm validate` before PR

### For Complex Architecture

1. Use `/agent architect` for design planning
2. Reference `docs/dev.content.md`
3. Check database schema in `src/database/schema.ts`
4. See existing implementations for examples

### For Bug Fixes

1. Use `/agent Debug Mode Instructions`
2. Run `pnpm type-check:watch` while investigating
3. Write tests that fail first, then fix
4. Verify with `pnpm validate`

---

## 📝 Documentation Maintenance

This documentation is:

- ✅ **Auto-Loading** — Instruction files apply based on file patterns
- ✅ **Comprehensive** — 8000+ lines covering all patterns
- ✅ **Current** — Updated as phases complete
- ✅ **Well-Organized** — Clear structure and navigation
- ✅ **Example-Rich** — Code examples throughout

---

## 🎓 Learning Resources Quick Links

| Topic | Location | Read Time |
| --- | --- | --- |
| Getting Started | `docs/QUICK_START.md` | 5 min |
| Project Overview | `AGENTS.md` | 5 min |
| AI Agent Guide | `.github/AI_AGENT_SETUP_GUIDE.md` | 10 min |
| Complete Reference | `.github/copilot-instructions.md` | 30 min |
| Implementation Patterns | `docs/dev.content.md` | 45 min |
| Database Schema | `src/database/schema.ts` | 20 min |
| Code Examples | Existing files in `src/` | 30 min |

---

## 🏁 Conclusion

ComicWise has **comprehensive AI agent support** with:

✅ 16 auto-loaded instruction files ✅ 15 custom workflow skills ✅ 14 specialized agents ✅ 8000+ lines of documentation ✅ All quality gates passing ✅ Production-ready code

**Status**: Ready for immediate development

---

**For Questions**: Refer to appropriate documentation file **For Complex Tasks**: Use `/skill` or `/agent` **For Code Review**: Check `.github/instructions/code-review.instructions.md`

---

_This documentation was prepared for GitHub Copilot, Claude, Cursor, and all AI agents working on ComicWise._
