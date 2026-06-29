# Phase 3: Merge Instruction File Conventions (6 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

## Phase 3: Merge Instruction File Conventions (6 items)

### Step 16 — Add TypeScript conventions to §20

From `.github/instructions/typescript.instructions.md`:

- Use `interface` for object shapes, not `type` aliases
- Implement type guards for runtime narrowing (`unknown` → specific type)
- PascalCase component names matching file names
- Export prop interfaces for reusable components
- Create barrel exports (`index.ts`) for directories
- Functional components only — no class components
- No conditional hooks

### Step 17 — Add documentation standards to §20

From `.github/instructions/documentation.instructions.md`:

- TSDoc comments required on functions, classes, hooks, complex types
- Document component props with descriptions
- Comment workarounds with reasons
- Keep docs in sync with code changes

### Step 18 — Add Next.js rules to §14

From `.github/instructions/nextjs.instructions.md`:

- Every route directory needs `loading.tsx` + `error.tsx`
- Never access `Date.now()`, `localStorage`, `window`, `document` in Server Components
- Use Next.js `<Image>` for all images
- Use `next/font` for all fonts
- Prefer static generation over SSR
- All code must be Turbopack-compatible

### Step 19 — Add security rules to §20

From `.github/instructions/security.instructions.md`:

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Rate limiting for API routes
- Never expose stack traces in production
- Escape user-generated content (XSS prevention)
- Don't store sensitive data in localStorage/sessionStorage

### Step 20 — Add testing conventions to §17

From `.github/instructions/testing.instructions.md`:

- Include accessibility checks in component tests
- Use `.env.test` for test configuration
- Tests must clean up after themselves
- Mock auth for unit tests, real auth for E2E
- Use Vitest built-in assertions

### Step 21 — Document React Compiler conflict

Note in §14: `performance.instructions.md` says "Use `React.memo` for expensive components" which **directly contradicts** the React Compiler rule. The setup prompt is authoritative — `memo()`, `useMemo`, `useCallback` are forbidden. The performance instructions file needs updating.

---
