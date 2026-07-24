# rhixecompany-comics - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\rhixecompany-comics`
**Generated:** 2026-07-10
**Stack:** Django + Next.js

## Directory Tree

```
rhixecompany-comics/
├── .editorconfig
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       ├── ci.yml
│       └── test.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── architecture.md
├── backend/
│   ├── apps/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── admin.py
│   │   │   │   ├── apps.py
│   │   │   │   ├── filters.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── migrations/
│   │   │   │   ├── models.py
│   │   │   │   ├── scripts/
│   │   │   │   ├── signals.py
│   │   │   │   ├── tables.py
│   │   │   │   ├── templatetags/
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls/
│   │   │   │   ├── utils.py
│   │   │   │   ├── validators.py
│   │   │   │   └── views/
│   │   │   ├── apps.py
│   │   │   ├── conftest.py
│   │   │   ├── contrib/
│   │   │   │   ├── __init__.py
│   │   │   │   └── sites/
│   │   │   ├── home/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── admin.py
│   │   │   │   ├── apps.py
│   │   │   │   ├── context_processors.py
│   │   │   │   ├── migrations/
│   │   │   │   ├── models.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   ├── src/
│   │   │   │   ├── alpine_init.ts
│   │   │   │   ├── backtotop.ts
│   │   │   │   ├── carousel.ts
│   │   │   │   ├── dark-mode.ts
│   │   │   │   ├── htmx_init.ts
│   │   │   │   ├── hyper_init.ts
│   │   │   │   ├── navbar.ts
│   │   │   │   ├── project.ts
│   │   │   │   ├── sass/
│   │   │   │   ├── sidebar.ts
│   │   │   │   ├── types/
│   │   │   │   └── vendors.ts
│   │   │   ├── static/
│   │   │   │   ├── ckeditor/
│   │   │   │   ├── fonts/
│   │   │   │   ├── images/
│   │   │   │   ├── img/
│   │   │   │   ├── js/
│   │   │   │   └── main.js
│   │   │   ├── templates/
│   │   │   │   ├── 403.html
│   │   │   │   ├── 403_csrf.html
│   │   │   │   ├── 404.html
│   │   │   │   ├── 505.html
│   │   │   │   ├── account/
│   │   │   │   ├── allauth/
│   │   │   │   ├── base.html
│   │   │   │   ├── bookmark/
│   │   │   │   ├── chapters/
│   │   │   │   ├── comics/
│   │   │   │   ├── error.html
│   │   │   │   ├── home/
│   │   │   │   ├── partials/
│   │   │   │   └── users/
│   │   │   ├── urls.py
│   │   │   └── users/
│   │   │       ├── __init__.py
│   │   │       ├── adapters.py
│   │   │       ├── admin.py
│   │   │       ├── apps.py
│   │   │       ├── context_processors.py
│   │   │       ├── decorators.py
│   │   │       ├── forms.py
│   │   │       ├── migrations/
│   │   │       ├── models.py
│   │   │       ├── signals.py
│   │   │       ├── tasks.py
│   │   │       ├── tests/
│   │   │       ├── urls.py
│   │   │       ├── utils.py
│   │   │       ├── views.py
│   │   │       └── widgets.py
│   │   ├── comics/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── scraping/
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── management/
│   │   │   │   ├── __init__.py
│   │   │   │   └── commands/
│   │   │   └── tasks.py
│   │   └── users/
│   │       ├── __init__.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       └── urls.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── docker-compose.yml
├── docs/
│   ├── architecture.md
│   ├── consolidation-patterns.md
│   ├── migration-status.md
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── sandbox-projects-list-context.md
│   ├── sandbox-projects-merge-plan.md
│   └── sandbox-projects-merge-prompt.md
├── execution-summary.md
├── folder-structure.md
├── frontend/
│   ├── Dockerfile
│   ├── next-env.d.ts
│   ├── next.config.ts
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.mjs
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── sign-in/
│   │   │   │   └── sign-up/
│   │   │   ├── (root)/
│   │   │   │   ├── analytics/
│   │   │   │   ├── authors/
│   │   │   │   ├── bookmarks/
│   │   │   │   ├── browse/
│   │   │   │   ├── comics/
│   │   │   │   ├── comments/
│   │   │   │   ├── feed/
│   │   │   │   ├── genres/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── notifications/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── profile/
│   │   │   │   ├── ratings/
│   │   │   │   ├── reading-progress/
│   │   │   │   ├── search/
│   │   │   │   └── settings/
│   │   │   ├── admin/
│   │   │   │   ├── artists/
│   │   │   │   ├── audit-logs/
│   │   │   │   ├── authors/
│   │   │   │   ├── chapters/
│   │   │   │   ├── comics/
│   │   │   │   ├── genres/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── page.tsx
│   │   │   │   ├── permissions/
│   │   │   │   ├── roles/
│   │   │   │   ├── types/
│   │   │   │   └── users/
│   │   │   ├── api/
│   │   │   │   ├── auth/
│   │   │   │   └── seed/
│   │   │   ├── favicon.ico
│   │   │   ├── global-error.tsx
│   │   │   ├── globals.css
│   │   │   ├── layout.tsx
│   │   │   ├── loading.tsx
│   │   │   └── not-found.tsx
│   │   ├── auth-adapter.ts
│   │   ├── auth-config.ts
│   │   ├── auth-providers.ts
│   │   ├── auth.ts
│   │   ├── components/
│   │   │   ├── activity/
│   │   │   │   └── activity-feed.tsx
│   │   │   ├── admin/
│   │   │   │   ├── admin-artists-wrapper.tsx
│   │   │   │   ├── admin-audit-logs-wrapper.tsx
│   │   │   │   ├── admin-authors-wrapper.tsx
│   │   │   │   ├── admin-chapters-wrapper.tsx
│   │   │   │   ├── admin-comics-wrapper.tsx
│   │   │   │   ├── admin-genres-wrapper.tsx
│   │   │   │   ├── admin-permissions-wrapper.tsx
│   │   │   │   ├── admin-roles-wrapper.tsx
│   │   │   │   ├── admin-types-wrapper.tsx
│   │   │   │   ├── admin-users-wrapper.tsx
│   │   │   │   └── admin-wrapper.tsx
│   │   │   ├── analytics/
│   │   │   │   ├── reading-dashboard.tsx
│   │   │   │   ├── reading-goals-widget.tsx
│   │   │   │   ├── reading-history-timeline.tsx
│   │   │   │   └── reading-stats-card.tsx
│   │   │   ├── auth/
│   │   │   │   ├── sign-in/
│   │   │   │   └── sign-up/
│   │   │   ├── bookmarks/
│   │   │   │   ├── bookmark-card.tsx
│   │   │   │   ├── bookmarks-filter.tsx
│   │   │   │   ├── bookmarks-wrapper.tsx
│   │   │   │   ├── index.ts
│   │   │   │   ├── resume-button.tsx
│   │   │   │   └── status-editor.tsx
│   │   │   ├── browse/
│   │   │   │   └── browse-wrapper.tsx
│   │   │   ├── comics/
│   │   │   │   ├── bookmark-button.tsx
│   │   │   │   ├── comic-card.tsx
│   │   │   │   ├── comic-detail-wrapper.tsx
│   │   │   │   ├── comic-filters.tsx
│   │   │   │   ├── comic-list-skeleton.tsx
│   │   │   │   ├── comic-pagination-controls.tsx
│   │   │   │   ├── comics-wrapper.tsx
│   │   │   │   ├── empty-state.tsx
│   │   │   │   ├── index.ts
│   │   │   │   └── share-button.tsx
│   │   │   ├── comments/
│   │   │   │   ├── chapter-comments-section.tsx
│   │   │   │   ├── comment-card.tsx
│   │   │   │   ├── comment-form.tsx
│   │   │   │   ├── comment-list.tsx
│   │   │   │   ├── comments-wrapper.tsx
│   │   │   │   └── index.ts
│   │   │   ├── feed/
│   │   │   │   └── feed-wrapper.tsx
│   │   │   ├── genres/
│   │   │   │   └── genre-detail-wrapper.tsx
│   │   │   ├── home/
│   │   │   │   ├── continue-reading-section.tsx
│   │   │   │   └── home-wrapper.tsx
│   │   │   ├── layout/
│   │   │   │   ├── app-sidebar.tsx
│   │   │   │   ├── chart-area-interactive.tsx
│   │   │   │   ├── current-year-client.tsx
│   │   │   │   ├── current-year.tsx
│   │   │   │   ├── data-table.tsx
│   │   │   │   ├── Footer.tsx
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── layout-provider.tsx
│   │   │   │   ├── logo.tsx
│   │   │   │   ├── nav-documents.tsx
│   │   │   │   ├── nav-main.tsx
│   │   │   │   ├── nav-secondary.tsx
│   │   │   │   ├── nav-user.tsx
│   │   │   │   ├── navbar-client.tsx
│   │   │   │   ├── navbar.tsx
│   │   │   │   ├── section-cards.tsx
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   └── site-header.tsx
│   │   │   ├── notifications/
│   │   │   │   ├── notification-bell.tsx
│   │   │   │   └── notifications-wrapper.tsx
│   │   │   ├── profile/
│   │   │   │   ├── change-password-form.tsx
│   │   │   │   ├── delete-account-form.tsx
│   │   │   │   ├── index.ts
│   │   │   │   ├── profile-edit-form.tsx
│   │   │   │   ├── profile-wrapper.tsx
│   │   │   │   └── settings-form.tsx
│   │   │   ├── providers.tsx
│   │   │   ├── ratings/
│   │   │   │   ├── comic-ratings-display.tsx
│   │   │   │   ├── comic-ratings-section.tsx
│   │   │   │   ├── index.ts
│   │   │   │   ├── rating-button.tsx
│   │   │   │   ├── rating-form.tsx
│   │   │   │   ├── rating-stats.tsx
│   │   │   │   └── ratings-wrapper.tsx
│   │   │   ├── reading/
│   │   │   │   ├── chapter-reader-wrapper.tsx
│   │   │   │   ├── chapter-reader.tsx
│   │   │   │   ├── continue-reading-card.tsx
│   │   │   │   ├── continue-reading-section.tsx
│   │   │   │   ├── image-viewer.tsx
│   │   │   │   ├── index.ts
│   │   │   │   ├── progress-bar.tsx
│   │   │   │   ├── reader-controls.tsx
│   │   │   │   ├── reader-settings.tsx
│   │   │   │   └── reader-view.tsx
│   │   │   ├── reading-progress/
│   │   │   │   └── reading-progress-wrapper.tsx
│   │   │   ├── recommendations/
│   │   │   │   └── recommended-section.tsx
│   │   │   ├── search/
│   │   │   │   ├── advanced-search-form.tsx
│   │   │   │   ├── index.ts
│   │   │   │   ├── search-input.tsx
│   │   │   │   ├── search-results-content.tsx
│   │   │   │   ├── search-results.tsx
│   │   │   │   ├── search-suggestions-dropdown.tsx
│   │   │   │   └── search-wrapper.tsx
│   │   │   ├── settings/
│   │   │   │   ├── index.ts
│   │   │   │   └── settings-form.tsx
│   │   │   ├── theme/
│   │   │   │   └── theme-toggle.tsx
│   │   │   ├── theme-provider.tsx
│   │   │   ├── ui/
│   │   │   │   ├── accordion.tsx
│   │   │   │   ├── action-button.tsx
│   │   │   │   ├── alert-dialog.tsx
│   │   │   │   ├── alert.tsx
│   │   │   │   ├── aspect-ratio.tsx
│   │   │   │   ├── avatar.tsx
│   │   │   │   ├── badge.tsx
│   │   │   │   ├── breadcrumb.tsx
│   │   │   │   ├── button-group.tsx
│   │   │   │   ├── button.tsx
│   │   │   │   ├── calendar.tsx
│   │   │   │   ├── card.tsx
│   │   │   │   ├── carousel.tsx
│   │   │   │   ├── chart.tsx
│   │   │   │   ├── checkbox.tsx
│   │   │   │   ├── collapsible.tsx
│   │   │   │   ├── combobox.tsx
│   │   │   │   ├── command.tsx
│   │   │   │   ├── context-menu.tsx
│   │   │   │   ├── data-table.tsx
│   │   │   │   ├── dialog.tsx
│   │   │   │   ├── direction.tsx
│   │   │   │   ├── drawer.tsx
│   │   │   │   ├── dropdown-menu.tsx
│   │   │   │   ├── empty.tsx
│   │   │   │   ├── field.tsx
│   │   │   │   ├── form.tsx
│   │   │   │   ├── hover-card.tsx
│   │   │   │   ├── input-group.tsx
│   │   │   │   ├── input-otp.tsx
│   │   │   │   ├── input.tsx
│   │   │   │   ├── item.tsx
│   │   │   │   ├── kbd.tsx
│   │   │   │   ├── label.tsx
│   │   │   │   ├── loading-swap.tsx
│   │   │   │   ├── menubar.tsx
│   │   │   │   ├── multi-select.tsx
│   │   │   │   ├── native-select.tsx
│   │   │   │   ├── navigation-menu.tsx
│   │   │   │   ├── number-input.tsx
│   │   │   │   ├── pagination.tsx
│   │   │   │   ├── password-input.tsx
│   │   │   │   ├── popover.tsx
│   │   │   │   ├── progress.tsx
│   │   │   │   ├── radio-group.tsx
│   │   │   │   ├── resizable.tsx
│   │   │   │   ├── scroll-area.tsx
│   │   │   │   ├── select.tsx
│   │   │   │   ├── separator.tsx
│   │   │   │   ├── sheet.tsx
│   │   │   │   ├── sidebar.tsx
│   │   │   │   ├── skeleton.tsx
│   │   │   │   ├── slider.tsx
│   │   │   │   ├── sonner.tsx
│   │   │   │   ├── spinner.tsx
│   │   │   │   ├── switch.tsx
│   │   │   │   ├── table.tsx
│   │   │   │   ├── tabs.tsx
│   │   │   │   ├── textarea.tsx
│   │   │   │   ├── toggle-group.tsx
│   │   │   │   ├── toggle.tsx
│   │   │   │   └── tooltip.tsx
│   │   │   └── users/
│   │   │       ├── follow-button.tsx
│   │   │       └── follow-stats.tsx
│   │   ├── database/
│   │   │   ├── db.ts
│   │   │   ├── drizzle/
│   │   │   │   ├── 0000_dry_lady_bullseye.sql
│   │   │   │   └── meta/
│   │   │   └── schema.ts
│   │   ├── lib/
│   │   │   ├── accessibility.ts
│   │   │   ├── api.ts
│   │   │   ├── image-optimization.ts
│   │   │   ├── image-processor.ts
│   │   │   ├── performance-metrics.ts
│   │   │   ├── query-client.ts
│   │   │   ├── types.ts
│   │   │   └── utils.ts
│   │   ├── proxy.ts
│   │   ├── scripts/
│   │   │   ├── audit-scripts.ts
│   │   │   ├── cache-stats.ts
│   │   │   ├── camelCaseConverter2025.ts
│   │   │   ├── check-db-counts.ts
│   │   │   ├── clear-cache.ts
│   │   │   ├── fix-duplicate-paths.ts
│   │   │   ├── fix-line-endings.ts
│   │   │   ├── git-commit.ts
│   │   │   ├── git-init.ts
│   │   │   ├── master-setup.ts
│   │   │   ├── optimize-performance.ts
│   │   │   ├── rename-to-kebab-case.ts
│   │   │   ├── scaffold.ts
│   │   │   ├── seed/
│   │   │   │   ├── config.ts
│   │   │   │   ├── data-loader.ts
│   │   │   │   ├── database/
│   │   │   │   ├── dependency-graph.ts
│   │   │   │   ├── helpers/
│   │   │   │   ├── index.ts
│   │   │   │   ├── logger.ts
│   │   │   │   ├── README.md
│   │   │   │   ├── run.ts
│   │   │   │   ├── seed-orchestrator.ts
│   │   │   │   ├── seeders/
│   │   │   │   └── types.ts
│   │   │   ├── shared/
│   │   │   │   ├── colors.ts
│   │   │   │   ├── confirm.ts
│   │   │   │   ├── confirmAction.ts
│   │   │   │   ├── logger.ts
│   │   │   │   └── spinner.ts
│   │   │   ├── triage-quality-gate.ts
│   │   │   ├── unified-db-operations.ts
│   │   │   ├── unified-dev-setup.ts
│   │   │   ├── unified-performance-ops.ts
│   │   │   ├── unified-project-health.ts
│   │   │   ├── unified-schema-refactor.ts
│   │   │   ├── uninstall-unused-packages.ts
│   │   │   └── updateAnyTypes.ts
│   │   ├── storages/
│   │   │   ├── image-downloader.ts
│   │   │   ├── image-kit-uploader.ts
│   │   │   ├── image-strategy.ts
│   │   │   └── index.ts
│   │   └── styles/
│   │       ├── fonts/
│   │       │   ├── Bebas_Neue/
│   │       │   ├── BebasNeue-Regular.ttf
│   │       │   ├── Fira_Mono/
│   │       │   ├── Fira_Sans/
│   │       │   ├── Fira_Sans_Condensed/
│   │       │   ├── IBM_Plex_Sans/
│   │       │   ├── IBMPlexSans-Bold.ttf
│   │       │   ├── IBMPlexSans-Medium.ttf
│   │       │   ├── IBMPlexSans-Regular.ttf
│   │       │   ├── IBMPlexSans-SemiBold.ttf
│   │       │   ├── Martian_Mono/
│   │       │   └── Schibsted_Grotesk/
│   │       └── globals.css
│   ├── tsconfig.json
│   └── tsconfig.tsbuildinfo
├── project-workflow.md
├── README.md
├── RESEARCH_REPORT.md
├── scripts/
│   └── scraper/
│       ├── package.json
│       ├── scrape.js
│       ├── scrape2.js
│       ├── test.js
│       ├── test1.js
│       └── utils.js
├── tech-stack.md
├── technology-stack.md
└── validation-report.md
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
