# university-libary-jsm - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\university-libary-jsm`
**Generated:** 2026-07-10
**Stack:** Next.js

## Directory Tree

```
university-libary-jsm/
├── .editorconfig
├── .github/
│   └── copilot-instructions.md
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── app/
│   ├── (auth)/
│   │   ├── layout.tsx
│   │   ├── sign-in/
│   │   │   └── page.tsx
│   │   └── sign-up/
│   │       └── page.tsx
│   ├── (root)/
│   │   ├── books/
│   │   │   └── [id]/
│   │   │       └── page.tsx
│   │   ├── layout.tsx
│   │   ├── library/
│   │   │   └── page.tsx
│   │   ├── my-profile/
│   │   │   └── page.tsx
│   │   └── page.tsx
│   ├── admin/
│   │   ├── account-requests/
│   │   │   ├── [id]/
│   │   │   │   └── page.tsx
│   │   │   ├── new/
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── book-requests/
│   │   │   ├── [id]/
│   │   │   │   └── page.tsx
│   │   │   ├── new/
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── books/
│   │   │   ├── [id]/
│   │   │   │   └── page.tsx
│   │   │   ├── new/
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── data.json
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── users/
│   │       ├── [id]/
│   │       │   └── page.tsx
│   │       ├── new/
│   │       │   └── page.tsx
│   │       └── page.tsx
│   ├── api/
│   │   ├── auth/
│   │   │   └── [...nextauth]/
│   │   │       └── route.ts
│   │   ├── imagekit/
│   │   │   └── route.ts
│   │   └── workflows/
│   │       └── onboarding/
│   │           └── route.ts
│   ├── favicon.ico
│   ├── fonts/
│   │   ├── BebasNeue-Regular.ttf
│   │   ├── IBMPlexSans-Bold.ttf
│   │   ├── IBMPlexSans-Medium.ttf
│   │   ├── IBMPlexSans-Regular.ttf
│   │   └── IBMPlexSans-SemiBold.ttf
│   ├── globals.css
│   ├── layout.tsx
│   ├── loading.tsx
│   ├── not-found.tsx
│   ├── too-fast/
│   │   └── page.tsx
│   └── unauthorized/
│       └── page.tsx
├── assets/
│   ├── loader.gif
│   └── logo.svg
├── auth.ts
├── books.json
├── components/
│   ├── admin/
│   │   ├── app-sidebar.tsx
│   │   ├── books/
│   │   │   ├── cell-viewer.tsx
│   │   │   ├── column-header.tsx
│   │   │   ├── columns.tsx
│   │   │   ├── data-table.tsx
│   │   │   ├── table-pagination.tsx
│   │   │   └── table-toggle.tsx
│   │   ├── chart-area-interactive.tsx
│   │   ├── ColorPicker.tsx
│   │   ├── data-table.tsx
│   │   ├── forms/
│   │   │   └── BookForm.tsx
│   │   ├── nav-main.tsx
│   │   ├── nav-user.tsx
│   │   ├── section-cards.tsx
│   │   └── site-header.tsx
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
│   ├── soner-demo.tsx
│   └── ui/
│       ├── avatar.tsx
│       ├── badge.tsx
│       ├── breadcrumb.tsx
│       ├── button.tsx
│       ├── card.tsx
│       ├── chart.tsx
│       ├── checkbox.tsx
│       ├── collapsible.tsx
│       ├── drawer.tsx
│       ├── dropdown-menu.tsx
│       ├── form.tsx
│       ├── input.tsx
│       ├── label.tsx
│       ├── select.tsx
│       ├── separator.tsx
│       ├── sheet.tsx
│       ├── sidebar.tsx
│       ├── skeleton.tsx
│       ├── sonner.tsx
│       ├── table.tsx
│       ├── tabs.tsx
│       ├── textarea.tsx
│       ├── toggle-group.tsx
│       ├── toggle.tsx
│       └── tooltip.tsx
├── components.json
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
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   ├── DEVELOPER_GUIDE.md
│   ├── README.md
│   └── USER_GUIDE.md
├── drizzle.config.ts
├── dummybooks.json
├── emails/
│   ├── reset-password.tsx
│   ├── user-invite.tsx
│   ├── user-welcome.tsx
│   └── weekly-digest.tsx
├── eslint.config.mjs
├── hooks/
│   └── use-mobile.tsx
├── lib/
│   ├── actions/
│   │   ├── auth.ts
│   │   ├── book.ts
│   │   └── user.ts
│   ├── admin/
│   │   └── actions/
│   │       ├── book.ts
│   │       └── user.ts
│   ├── auth-guard.ts
│   ├── config.ts
│   ├── encrypt.ts
│   ├── queries/
│   │   ├── delete.ts
│   │   ├── insert.ts
│   │   ├── select.ts
│   │   └── update.ts
│   ├── ratelimit.ts
│   ├── utils.ts
│   ├── validations.ts
│   └── workflow.ts
├── middleware.ts
├── migrations/
│   ├── 0000_supreme_vampiro.sql
│   └── meta/
│       ├── 0000_snapshot.json
│       └── _journal.json
├── next-auth.d.ts
├── next.config.ts
├── package.json
├── postcss.config.mjs
├── public/
│   ├── icons/
│   │   ├── admin/
│   │   │   ├── book.svg
│   │   │   ├── bookmark.svg
│   │   │   ├── calendar.svg
│   │   │   ├── caret-down.svg
│   │   │   ├── caret-up.svg
│   │   │   ├── close.svg
│   │   │   ├── edit.svg
│   │   │   ├── eye.svg
│   │   │   ├── home.svg
│   │   │   ├── info.svg
│   │   │   ├── link.svg
│   │   │   ├── logo.svg
│   │   │   ├── plus.svg
│   │   │   ├── receipt.svg
│   │   │   ├── search.svg
│   │   │   ├── tick.svg
│   │   │   ├── trash.svg
│   │   │   ├── user.svg
│   │   │   └── users.svg
│   │   ├── book-2.svg
│   │   ├── book.svg
│   │   ├── calendar.svg
│   │   ├── clock.svg
│   │   ├── heart.svg
│   │   ├── home.svg
│   │   ├── id.svg
│   │   ├── logo.svg
│   │   ├── logout.svg
│   │   ├── receipt.svg
│   │   ├── search-fill.svg
│   │   ├── star.svg
│   │   ├── tick.svg
│   │   ├── upload.svg
│   │   ├── user-fill.svg
│   │   ├── user.svg
│   │   ├── verified.svg
│   │   └── warning.svg
│   └── images/
│       ├── auth-illustration.png
│       ├── no-books.png
│       ├── pattern.webp
│       └── shadcn.jpg
├── README.md
├── RESEARCH_REPORT.md
├── styles/
│   └── admin.css
├── tsconfig.json
└── types.d.ts
```

## Key Directories

| Directory | Purpose | Convention |
| ----------- | --------- | ------------ |
| `app/` | Next.js App Router pages & layouts | Feature-based subdirectories |
| `components/` | React components | PascalCase, co-located with feature |
| `lib/` | Shared utilities | camelCase files |
| `db/` / `prisma/` / `drizzle/` | Database schema & ORM | Standard conventions |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---
*Generated by agents-system-prompt-context-fix-runner*
