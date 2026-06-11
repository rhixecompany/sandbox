Prompt instructions file:

1. Conversation Overview:

- Primary Objectives: "Fix only issues surfaced by pnpm lint:fix and pnpm build. Tests are excluded. Goal: Achieve zero warnings and zero errors from those scripts." "Audit and Review all .vscode/_.json files then backup them up and then create a new clean enhanced .vscode/_.json files for optimization, consistency and correctness, use nextjs@latest best practices and dry practices." "Search the web for docs on next-auth@latest,@auth/drizzle-adapter@latest,@auth/core@latest and read them if found then generate or update all src/auth.ts, src/auth-config.ts, src/auth-providers.ts, src/auth-adapter.ts, src/actions/auth-actions.ts, src/proxy.ts, src/app/api/auth/[...nextauth]/route.ts, files for consistency and correctness, use nextjs@latest best practices and dry practices."
- Session Context: The agent followed a batch-fix prompt, ran lint/build, triaged errors, applied targeted fixes, audited VSCode JSON, and responded to a request for a comprehensive modernization plan. The latest focus was on VSCode JSON cleanup and lint error reduction.
- User Intent Evolution: Initial focus was on batch lint/build fixes and documentation. Later, the user expanded scope to include ESLint plugin installation, config generation, VSCode optimization, and auth integration.

2. Technical Foundation:

- Next.js 16+: App Router, Cache Components, strict linting, modular structure.
- TypeScript: Strong typing, no-explicit-any, no-empty-object-type, preserve-caught-error.
- Tailwind CSS: Linting for class order, integration with VSCode.
- Drizzle ORM: Database code in `src/database/`.
- ESLint/Prettier: Multiple plugins, strict config, auto-formatting.
- VSCode: Settings and extensions optimized for Next.js, TypeScript, Tailwind, and DRY practices.

3. Codebase Status:

- `src/app/(root)/application-shell-01/page.tsx`: Fixed React Suspense usage, now imports Suspense directly.
- `src/components/shadcn-studio/blocks/footer-component-01/footer-component-01.tsx`: Same Suspense fix applied.
- `src/app/(root)/page.tsx` and `src/app/admin/page.tsx`: Removed empty object type props for lint compliance.
- `src/lib/env.ts`: Updated error handling to preserve original error as cause.
- `.vscode/extensions.json` and `.vscode/settings.json`: JSONC comments removed, parsing errors fixed, settings optimized.
- Planned: `eslint.config.mts` (to be generated), multiple auth files (to be created/updated).

4. Problem Resolution:

- Issues Encountered: React Suspense UMD global error, empty object type lint errors, preserve-caught-error, JSONC parsing errors in VSCode configs.
- Solutions Implemented: Import Suspense directly, remove empty object type props, attach error cause, remove JSONC comments, optimize VSCode settings.
- Debugging Context: Repeated lint/build runs to verify fixes; parsing errors in VSCode configs resolved.
- Lessons Learned: Strict linting and config validation are essential; DRY and modular practices improve maintainability.

5. Progress Tracking:

- Completed Tasks: Initial lint/build run, triage, targeted code fixes, VSCode JSON audit and cleanup.
- Partially Complete Work: ESLint plugin check/install, config generation, VSCode JSON optimization, NextAuth/Drizzle/Auth Core research, auth file generation.
- Validated Outcomes: Lint/build errors reduced, VSCode configs now parse correctly.

6. Active Work State:

- Current Focus: VSCode JSON cleanup, lint error reduction, preparing for ESLint plugin/config and auth modernization.
- Recent Context: Last few exchanges involved editing VSCode JSON, fixing lint errors, and planning next steps.
- Working Code: Suspense import fixes, empty object type removal, error cause attachment, VSCode JSON cleanup.
- Immediate Context: Agent was actively working on VSCode JSON cleanup and lint error reduction when token budget was exceeded.

7. Recent Operations:

- Last Agent Commands: Read and edit `.vscode/extensions.json` and `.vscode/settings.json` to remove JSONC comments; edit `src/app/(root)/page.tsx`, `src/app/admin/page.tsx`, `src/lib/env.ts` for lint compliance; re-run `pnpm lint`.
- Tool Results Summary: Parsing errors resolved, lint errors reduced, some remain in references and project files.
- Pre-Summary State: Agent was cleaning up VSCode JSON and reducing lint errors, preparing for ESLint/config and auth modernization.
- Operation Context: These commands directly support the user's goal of zero lint/build errors, repo consistency, and modernization.

## Plan: Full ESLint, VSCode, Auth Modernization

This plan covers plugin verification/installation, ESLint config generation, VSCode JSON audit/backup/optimization, and NextAuth/Drizzle/Auth Core integration for a Next.js 16+ project. Steps are sequenced for speed and minimal redundancy.

**Steps**

    - Check if each plugin (`eslint-config-prettier`, `eslint-plugin-better-tailwindcss`, `eslint-plugin-jsx-a11y`, `@typescript-eslint/eslint-plugin`, etc.) is installed.
    - Install any missing plugins with `pnpm add -D ...`.
    - Use batch install for speed.

    - Create a config with all plugins, recommended settings, and rules for Next.js, TypeScript (`@typescript-eslint/eslint-plugin`), Tailwind, security, and DRY practices.
    - Include best practices for React, accessibility (`eslint-plugin-jsx-a11y`), import order, and testing.

3. **Audit, Backup, Optimize `.vscode/*.json`**
   - Review all `.vscode/*.json` files for errors, duplication, and outdated settings.
   - Backup originals to `.vscode/backup/`.
   - Generate new, clean, DRY, and Next.js-optimized versions (settings, extensions, etc.).

4. **Research NextAuth, Drizzle Adapter, Auth Core**
   - Search web for docs on `next-auth@latest`, `@auth/drizzle-adapter@latest`, `@auth/core@latest` and read them if found.
   - Summarize key integration patterns and best practices.

5. **Generate/Update Auth Files**
   - Create/update: `src/auth.ts`, `src/auth-config.ts`, `src/auth-providers.ts`, `src/auth-adapter.ts`, `src/actions/auth-actions.ts`, `src/proxy.ts`, `src/app/api/auth/[...nextauth]/route.ts`.
   - Use latest Next.js, NextAuth, Drizzle, and Auth Core patterns.
   - Ensure DRY, modular, and consistent structure.

6. **Verification**
   - Run `pnpm lint`, `pnpm build`, and manual checks for VSCode settings.
   - Test auth endpoints and integration.

**Decisions**

- Batch install for speed.
- Backup before replacing VSCode configs.
- Use latest Next.js and NextAuth docs for auth files.
- Prioritize DRY and modularity in all configs.

---

This plan is optimized for speed, correctness, and maintainability. Each step is actionable and minimizes redundant work.
