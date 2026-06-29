# Plan: Full ESLint, VSCode, Auth Modernization

> Extracted from `plan-setup.prompt.md`.

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
