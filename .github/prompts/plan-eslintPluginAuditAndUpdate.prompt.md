Plan: ESLint Plugin Audit & Update

Audit, update, and verify all ESLint plugins and config for your Next.js/TypeScript/Drizzle project. This checklist ensures deprecated plugins are removed, missing ones installed, and your config is up-to-date with best practices.

---

Step-by-Step Checklist

- Search the web for docs on all installed ESLint plugins, read and understand all of them, and check for issues, conflicts, or deprecations.
- For each plugin: check if it is deprecated, has issues, or conflicts; install any missing plugins; uninstall any deprecated or problematic plugins.
- Generate or update `eslint.config.mts` with all settings, plugins, and rules configured for this project, referencing `.references/comicwise/eslint.config.ts`, `.references/comicr/eslint.config.mjs`.
- Verify by running `pnpm lint` and resolve any errors or warnings.
- Ask any needed questions to clarify requirements or resolve ambiguities before finalizing the configuration.

1. Review Installed Plugins
   - Check `package.json` for all `eslint-plugin-*` and related packages.
   - Cross-reference with plugins listed in `eslint.config.mts`.

2. Search the web for docs and best practices for all installed ESLint plugins.
   - Read and understand official documentation and community guidance for each plugin.
   - Note any deprecations, issues, or conflicts.

3. Check for Deprecated/Conflicting Plugins
   - Remove `eslint-plugin-prettier` (deprecated).
   - Remove `eslint-plugin-node` (deprecated, use `eslint-plugin-n`).
   - Check for any other deprecated or conflicting plugins (see research summary).

4. Install Missing Plugins
   - For any plugin referenced in `eslint.config.mts` but not in `package.json`, run:
     - `pnpm add -D <plugin-name>`
   - Example: If `eslint-plugin-mdx` is referenced but not installed, add it.

5. Uninstall Deprecated/Conflicting Plugins
   - For any deprecated or conflicting plugin, run:
     - `pnpm remove <plugin-name>`
   - Example: Remove `eslint-plugin-prettier` and `eslint-plugin-node`.

6. Update `eslint.config.mts`
   - Reference `.references/comicwise/eslint.config.ts` and `.references/comicr/eslint.config.mjs` for structure and rules.
   - Use `"extends": ["plugin:<name>/recommended"]` for each active plugin.
   - Remove deprecated/conflicting plugins from config.
   - Add recommended settings for each plugin (see research summary).
   - Ensure TypeScript, React, Drizzle, Tailwind, and Next.js plugins are included and properly configured.
   - Integrate Prettier with ESLint for formatting issues (per user request).

7. Run Lint & Fix Errors
   - Run `pnpm lint` to check for errors/warnings.
   - If errors about missing plugins or config, resolve by installing/removing as needed.
   - If lint passes, run `pnpm lint:fix` to auto-fix and format code.

8. Verify Final Setup
   - Confirm all plugins are installed and active.
   - Ensure no deprecated/conflicting plugins remain.
   - Check that config matches best practices and project requirements.
   - Optionally, document changes in `docs/proposedFixes.MD` and `docs/proposedFixes.json`.

9. Ask any needed questions to clarify requirements, plugin usage, or project-specific rules before finalizing.

---

Decisions

- No custom ESLint rules or plugins unique to this repo.
- Merge best practices from all reference configs and sources.
- Linting will cover all file types: JS, TS, JSX, TSX, MDX, CSS, JSON, etc.
- Prettier will be integrated with ESLint for formatting issues.
- Reference config structure from provided `.references` files and backups.

---

This checklist is ready for implementation. Follow each step in order for a clean, up-to-date ESLint setup!
