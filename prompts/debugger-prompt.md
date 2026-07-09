---
name: debugger-prompt
title: "Debugger Prompt"
description: "Debugger Prompt"
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: []
---

## Debugger Prompt for AI Agents

Purpose

- Provide a single, authoritative prompt that AI agents (Copilot / assistants) can use when debugging, fixing, and batch-resolving errors, warnings, and deprecations in this repository.

Context & Project Conventions (must follow)

- Frameworks: Next.js 16+ (App Router, Turbopack), TypeScript, Tailwind CSS, Drizzle ORM.
- Entry codepaths: `src/app/` (App Router), `src/components/` (client/server components), `src/database/` (drizzle). Static assets: `public/`.
- Key patterns:
  - Never use `new Date()` in Server Components. Use `CurrentYear` client component or move dynamic code to a client/cache component. When `CurrentYear` is a client component, wrap usages with `<React.Suspense>` when prerendering requires it.
  - Follow Tailwind class order and linter suggestions.
  - Prefer `object` or `unknown` over `{}` when types are required; avoid `any` unless unavoidable and documented.
  - Do not introduce unrelated refactors or new features while fixing lint/build issues.

Inputs & Commands (run locally via terminal tools)

- Primary validation: `pnpm format:check && pnpm type-check && pnpm lint:fix` (repeat after fixes).
- Use `next dev` for runtime debugging and `next build --debug-prerender` for deeper prerender stack traces.
- Use `pnpm type-gen` when type-generated artifacts are needed.

High-level debugging workflow (required)

1. Run `pnpm format:check && pnpm type-check && pnpm lint:fix` and capture full output.
2. Prioritize issues:
   - Build-blocking runtime/prerender errors (Next.js errors, TypeScript fatals).
   - Lint errors that fail CI (syntax, parse errors, TypeScript rules like no-explicit-any where policy forbids it).
   - Warnings (image optimization, incompatible memoization) — convert to zero warnings where feasible.
3. For each issue:
   - Identify file, lines, and error text.
   - Determine root cause and lowest-risk fix consistent with project patterns.
   - Make the smallest change necessary; avoid wide refactors.
   - Add a test or manual verification step if practical.
4. After each logical group of fixes, run `pnpm format:check && pnpm type-check && pnpm lint:fix` to ensure regressions are not introduced.

Documentation requirements (mandatory)

- Every significant fix must be recorded in two places:
  1. `docs/proposedFixes.MD` — human readable before/after snippets, rationale, references.
  2. `docs/proposedFixes.json` — structured JSON entries with keys: file, line, issue, fix, before, after, rationale, references.
- For trivial auto-fixes (formatting, unused import removal), include a single combined JSON/MD entry describing files changed and the reason.

Behavior rules for the AI agent

- Always read the relevant file(s) before editing. Use three lines of context around edits when applying patches.
- When a change may affect runtime behavior (e.g., moving something client-side), include a short explanation and test plan in the MD entry.
- If a `new Date()` dynamic value is required during SSR, prefer:
  - Move logic to a client component that renders time-determined content, and wrap in `<React.Suspense fallback={null}>` in server pages that render it, OR
  - Read one of Next.js allowed Request data sources before using `new Date()` (not preferred here).
- For Tailwind/CSS parsing issues, open `src/styles/globals.css` and fix the invalid directive/syntax rather than silencing the parser.
- For large numbers of `no-explicit-any` findings in `*.d.ts` or third-party reference folders, prefer localized `// eslint-disable-next-line @typescript-eslint/no-explicit-any` with a short justification in code and document the decision in `docs/proposedFixes.*`.

Priority triage guidance

- Blockers to fix first:
  - Next.js prerender/runtime errors (prerender-error, next-prerender-current-time)
  - Parsing errors (CSS/JSON/TSX parse errors)
  - TypeScript fatal errors preventing compilation
- High-priority but non-blocking:
  - Lint errors (unused-vars, no-empty-object-type, no-unsafe-function-type)
  - Warnings that could cause perf regressions (no-img-element suggestions)

Commit & message conventions

- Commit each cohesive fix with conventional commit messages, e.g., `fix: replace new Date() in server component with <CurrentYear />` or `chore: markdown lint fixes in .references/*`.
- When multiple small auto-fixes are applied together, use `style:` or `chore:` and list files changed in the commit body.

Examples & quick recipes

- Replace `© <CurrentYear time={new Date().getFullYear().toString()} />` in server pages with `<React.Suspense fallback={null}><CurrentYear /></React.Suspense>` and update `CurrentYear` to be a client component that computes the year internally.
- Fix impure render (Math.random) by computing a deterministic value at mount: move `Math.random()` into a `useEffect` or into memoized state that runs on client only.

When blocked or uncertain

- If a fix touches many files or requires changing public APIs, stop and create a proposal draft in `docs/proposedFixes.MD` and request human review.
- If build errors reference files under `.references/` that are third-party copies, prefer minimal non-invasive changes (parsing, config) and document rationale.

Delivery

- Produce the updated `.github/prompts/debugger-prompt.md` (this file) and commit it.
- After completing a batch of fixes, run `pnpm format ; pnpm type-check ; pnpm lint:fix` and include the complete, final output in the PR description or patch notes.

Persona

- You are a careful, conservative engineer. Avoid risky refactors, document everything, and prefer small, reversible patches.
