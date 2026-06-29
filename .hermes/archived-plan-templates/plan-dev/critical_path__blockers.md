# Critical Path & Blockers

> Extracted from `plan-dev.prompt.md`.

## Critical Path & Blockers

### BLOCKER #1: TypeScript Compilation 🔴 CRITICAL

**Status:** Cannot proceed until resolved  
**Affected Files:**

- `src/dal/base-dal.ts` - Base class definition
- `src/dal/comic-dal.ts` - 15+ errors
- `src/dal/rating-dal.ts` - 3+ errors
- `src/dal/comment-dal.ts` - 2+ errors
- `src/auth.ts` - Auth callback signature issues
- `src/components/ui/chart.tsx` - Recharts type issues

**Required Actions:**

1. Fix DAL imports and type definitions
2. Resolve auth callback signatures
3. Add proper Recharts type guards
4. Run `pnpm type-check` - must show 0 errors
5. Unblock remaining features

**Time Estimate:** 1-2 hours

### BLOCKER #2: Feature Verification 🟡 YELLOW

**Status:** Phases 3-5 marked complete but unverified  
**Required Actions:**

1. Run dev server: `pnpm dev`
2. Test all routes manually
3. Verify database connectivity
4. Check API functionality

**Time Estimate:** 1-2 hours

---
