# projects/university-libary-jsm — Folder Structure Blueprint

## Overview

- Namespace: `projects/university-libary-jsm`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

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

## Placement Rules

- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions

- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes

- Refresh after any folder move, rename, or new top-level component.
