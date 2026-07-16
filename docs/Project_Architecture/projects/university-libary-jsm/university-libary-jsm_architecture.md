# projects/university-libary-jsm — Architecture Blueprint

## Overview
- Detected stack: Next.js, React, Node.js, TypeScript, Tailwind, ESLint, Prettier
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: app, docs, lib

## Component Map
- `app, docs, lib`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
university-libary-jsm/
├── .github/
│   └── copilot-instructions.md
├── app/
│   ├── (auth)/
│   ├── (root)/
│   ├── admin/
│   ├── api/
│   ├── fonts/
│   ├── too-fast/
│   ├── unauthorized/
│   ├── favicon.ico
│   ├── globals.css
│   ├── layout.tsx
│   ├── loading.tsx
│   └── not-found.tsx
├── assets/
│   ├── loader.gif
│   └── logo.svg
├── components/
│   ├── admin/
│   ├── ui/
│   ├── AuthForm.tsx
│   ├── BookCard.tsx
│   ├── BookCover.tsx
│   ├── BookCoverSvg.tsx
│   ├── BookList.tsx
│   ├── BookOverview.tsx
│   ├── BookVideo.tsx
│   ├── BorrowBook.tsx
│   ├── FileUpload.tsx
│   ├── Header.tsx
│   ├── NavUser.tsx
│   └── soner-demo.tsx
├── constants/
│   └── index.ts
├── database/
│   ├── drizzle.ts
│   ├── dummybooks.ts
│   ├── redis.ts
│   ├── sample-users.ts
│   ├── schema.ts
│   ├── seed.ts
│   └── seedold.ts
├── emails/
│   ├── reset-password.tsx
│   ├── user-invite.tsx
│   ├── user-welcome.tsx
│   └── weekly-digest.tsx
├── hooks/
│   └── use-mobile.tsx
├── lib/
│   ├── actions/
│   ├── admin/
│   ├── queries/
│   ├── auth-guard.ts
│   ├── config.ts
│   ├── encrypt.ts
│   ├── ratelimit.ts
│   ├── utils.ts
│   ├── validations.ts
│   └── workflow.ts
├── migrations/
│   ├── meta/
│   └── 0000_supreme_vampiro.sql
├── public/
│   ├── icons/
│   └── images/
├── styles/
│   └── admin.css
├── .editorconfig
├── .env.example
├── .eslintignore
├── .npmrc
├── .prettierignore
├── .prettierrc
├── AGENTS.md
├── AUDIT_university-libary-jsm.md
├── auth.ts
├── books.json
├── components.json
├── drizzle.config.ts
├── dummybooks.json
├── eslint.config.mjs
├── middleware.ts
├── next-auth.d.ts
├── next.config.ts
├── package.json
├── postcss.config.mjs
├── README.md
├── REPOSITORY_SUMMARY.md
├── RESEARCH_REPORT.md
├── THE_STORY_OF_THIS_REPO.md
├── tsconfig.json
├── types.d.ts
└── web-research-university-libary-jsm.md
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
