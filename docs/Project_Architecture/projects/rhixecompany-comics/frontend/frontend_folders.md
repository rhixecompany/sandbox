# projects/rhixecompany-comics/frontend — Folder Structure Blueprint

## Overview
- Namespace: `projects/rhixecompany-comics/frontend`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
