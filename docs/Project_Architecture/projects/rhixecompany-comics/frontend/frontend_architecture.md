# projects/rhixecompany-comics/frontend — Architecture Blueprint

## Overview

- Detected stack: Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src

## Component Map

- `src`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure

```text
frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── database/
│   ├── lib/
│   ├── storages/
│   ├── styles/
│   ├── auth-adapter.ts
│   ├── auth-config.ts
│   ├── auth-providers.ts
│   ├── auth.ts
│   └── proxy.ts
├── .env.local
├── bun.lock
├── Dockerfile
├── next-env.d.ts
├── next.config.ts
├── package-lock.json
├── package.json
├── postcss.config.mjs
├── tsconfig.json
└── tsconfig.tsbuildinfo
```

## Cross-Cutting Concerns

- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points

- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes

- Regenerate when component boundaries, package dependencies, or folder structure change.
