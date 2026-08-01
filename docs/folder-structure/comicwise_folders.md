# comicwise - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\comicwise`
**Generated:** 2026-07-10
**Stack:** Next.js

## Directory Tree

```
comicwise/
├── .editorconfig
├── .github/
│   ├── copilot/
│   │   └── copilot-instructions.md
│   ├── copilot-instructions.md
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── plugin/
│   │   └── marketplace.json
│   ├── PULL_REQUEST_TEMPLATE/
│   │   └── pull_request.md
│   └── workflows/
│       ├── ci.yml
│       ├── copilot-setup-steps.yml.disabled
│       ├── deploy.yml.disabled
│       ├── playwright.yml.disabled
│       └── test.yml.disabled
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── API_REFERENCE.md
├── appConfig.ts
├── ARCHITECTURE.md
├── bun.lock
├── CHANGELOG.md
├── cleanup.ps1
├── cleanup.sh
├── code-exemplars.md
├── CODE_OF_CONDUCT.md
├── components.json
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── dev.ps1
├── dev.sh
├── DEVELOPMENT_GUIDE.md
├── docker-compose.yml
├── Dockerfile
├── docs/
│   ├── architecture.md
│   ├── archive/
│   │   ├── ai-setup-reference.md
│   │   └── architecture-blueprint-detailed.md
│   ├── audit-report.md
│   ├── authentication-guide.md
│   ├── BATCH-IMPLEMENTATION-PLAN.md
│   ├── BATCH-IMPLEMENTATION-SUMMARY.md
│   ├── BATCH_4-3_COMPLETION_REPORT.md
│   ├── BATCH_4-3_DIRECTORY_AUDIT.md
│   ├── CODE_DOCS.md
│   ├── comicwise-triage-context.md
│   ├── database-context-map.md
│   ├── database-migration-guide.md
│   ├── DEPLOYMENT.md
│   ├── dev.content.md
│   ├── DEV_SETUP_CHECKLIST.md
│   ├── MASTER_PHASE_PLAN_4-6.md
│   ├── MASTER_PHASE_PLAN_TRACKING.md
│   ├── personas-list.md
│   ├── PHASE-MASTER-PLAN.md
│   ├── PHASE4D-SECURITY-AUDIT.md
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── PROJECT_DOCS.docx
│   ├── PROJECT_DOCS.md
│   ├── proposedFixes.json
│   ├── proposedFixes.MD
│   ├── QUALITY_GATE_FIX_REPORT.md
│   ├── QUICK_START.md
│   ├── reading-progress-guide.md
│   ├── refactor-context.md
│   ├── SCRIPTS.md
│   ├── SEEDING_GUIDE.md
│   ├── SETUP.md
│   ├── triage-report.md
│   └── TYPE_CHECKED_LINTING.md
├── drizzle.config.ts
├── eslint.config.mts
├── execution-summary.md
├── folder-structure.md
├── install-vscode-extensions.ps1
├── install-vscode-extensions.sh
├── lint-report.json
├── lint-strict.txt
├── next-env.d.ts
├── next-sitemap.config.ts
├── next.config.ts
├── package.json
├── playwright.config.mts
├── pnpm-workspace.yaml
├── postcss.config.mjs
├── project-analysis-report.md
├── project-workflow.md
├── Project_Architecture_Blueprint_Expanded.md
├── Project_Architecture_Summary.md
├── public/
│   ├── file.svg
│   ├── globe.svg
│   ├── next.svg
│   ├── placeholder-comic.jpg
│   ├── robots.txt
│   ├── shadcn.jpg
│   ├── sitemap-0.xml
│   ├── sitemap.xml
│   ├── uploads/
│   ├── vercel.svg
│   └── window.svg
├── quality-gate-triage.json
├── quality-gate.json
├── quality-gate.ps1
├── quality-gate.sh
├── README.md
├── report.20260324.104250.3468.0.001.json
├── report.20260324.104250.3468.0.002.json
├── report.20260324.104250.3468.0.003.json
├── report.20260324.104250.3468.0.004.json
├── report.20260324.104250.3468.0.005.json
├── report.20260324.104250.3468.0.006.json
├── RESEARCH_REPORT.md
├── RESEARCH_UPDATE.md
├── SECURITY.md
├── seed-report-2026-03-20.json
├── seed-urls-report.txt
├── setup-dev.ps1
├── setup-dev.sh
├── SETUP_GUIDE.md
├── src/
│   ├── actions/
│   │   ├── admin/
│   │   │   ├── artist.actions.ts
│   │   │   ├── audit-log.actions.ts
│   │   │   ├── author.actions.ts
│   │   │   ├── chapter.actions.ts
│   │   │   ├── comic.actions.ts
│   │   │   ├── genre.actions.ts
│   │   │   ├── index.ts
│   │   │   ├── permission.actions.ts
│   │   │   ├── role.actions.ts
│   │   │   ├── type.actions.ts
│   │   │   └── user.actions.ts
│   │   ├── admin.actions.ts
│   │   ├── artist.actions.ts
│   │   ├── auth.actions.ts
│   │   ├── author.actions.ts
│   │   ├── bookmark.actions.ts
│   │   ├── browse.actions.ts
│   │   ├── chapter.actions.ts
│   │   ├── comic.actions.ts
│   │   ├── comment-rating.actions.ts
│   │   ├── credentials.actions.ts
│   │   ├── follow.actions.ts
│   │   ├── genre.actions.ts
│   │   ├── goals.actions.ts
│   │   ├── notification.actions.ts
│   │   ├── password-reset.actions.ts
│   │   ├── profile.actions.ts
│   │   ├── rbac.actions.ts
│   │   ├── reading-progress.actions.ts
│   │   ├── reading.actions.ts
│   │   ├── search-filters.actions.ts
│   │   ├── search.actions.ts
│   │   ├── share.actions.ts
│   │   └── user-preferences.actions.ts
│   ├── app/
│   │   ├── (auth)/
│   │   │   ├── layout.tsx
│   │   │   ├── sign-in/
│   │   │   │   └── page.tsx
│   │   │   └── sign-up/
│   │   │       └── page.tsx
│   │   ├── (root)/
│   │   │   ├── analytics/
│   │   │   │   ├── layout.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── authors/
│   │   │   │   └── [id]/
│   │   │   ├── bookmarks/
│   │   │   │   └── page.tsx
│   │   │   ├── browse/
│   │   │   │   └── page.tsx
│   │   │   ├── comics/
│   │   │   │   ├── [slug]/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── comments/
│   │   │   │   └── page.tsx
│   │   │   ├── feed/
│   │   │   │   └── page.tsx
│   │   │   ├── genres/
│   │   │   │   └── [id]/
│   │   │   ├── layout.tsx
│   │   │   ├── notifications/
│   │   │   │   └── page.tsx
│   │   │   ├── page.tsx
│   │   │   ├── profile/
│   │   │   │   ├── [id]/
│   │   │   │   ├── change-password/
│   │   │   │   ├── delete-account/
│   │   │   │   ├── edit/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   ├── page.tsx
│   │   │   │   └── settings/
│   │   │   ├── ratings/
│   │   │   │   └── page.tsx
│   │   │   ├── reading-progress/
│   │   │   │   └── page.tsx
│   │   │   ├── search/
│   │   │   │   ├── error.tsx
│   │   │   │   └── page.tsx
│   │   │   └── settings/
│   │   │       └── page.tsx
│   │   ├── admin/
│   │   │   ├── artists/
│   │   │   │   └── page.tsx
│   │   │   ├── audit-logs/
│   │   │   │   └── page.tsx
│   │   │   ├── authors/
│   │   │   │   └── page.tsx
│   │   │   ├── chapters/
│   │   │   │   └── page.tsx
│   │   │   ├── comics/
│   │   │   │   └── page.tsx
│   │   │   ├── genres/
│   │   │   │   └── page.tsx
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── permissions/
│   │   │   │   └── page.tsx
│   │   │   ├── roles/
│   │   │   │   └── page.tsx
│   │   │   ├── types/
│   │   │   │   └── page.tsx
│   │   │   └── users/
│   │   │       └── page.tsx
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   │   └── [...nextauth]/
│   │   │   └── seed/
│   │   │       └── route.ts
│   │   ├── favicon.ico
│   │   ├── global-error.tsx
│   │   ├── layout.tsx
│   │   ├── loading.tsx
│   │   └── not-found.tsx
│   ├── assets/
│   │   └── svg/
│   │       ├── auth-background-shape.tsx
│   │       └── logo.tsx
│   ├── auth-adapter.ts
│   ├── auth-config.ts
│   ├── auth-providers.ts
│   ├── auth.ts
│   ├── backuptests/
│   │   ├── e2e/
│   │   │   ├── activity-feed.spec.ts
│   │   │   ├── admin.spec.ts
│   │   │   ├── asura.spec.ts
│   │   │   ├── auth.spec.ts
│   │   │   ├── comments.spec.ts
│   │   │   ├── follow.spec.ts
│   │   │   ├── global-setup.ts
│   │   │   ├── helpers/
│   │   │   │   └── snapshots.ts
│   │   │   ├── rbac.spec.ts
│   │   │   ├── reading.spec.ts
│   │   │   ├── search.spec.ts
│   │   │   ├── snapshots.spec.ts
│   │   │   └── snapshots.spec.ts-snapshots/
│   │   │       ├── comics-card-element-element-chromium-win32.png
│   │   │       ├── comics-dark-chromium-win32.png
│   │   │       ├── comics-full-full-chromium-win32.png
│   │   │       ├── comics-mobile-chromium-win32.png
│   │   │       ├── home-full-full-chromium-win32.png
│   │   │       ├── search-full-full-chromium-win32.png
│   │   │       └── search-with-results-chromium-win32.png
│   │   └── unit/
│   │       ├── auth-schema.test.ts
│   │       ├── auth.test.ts
│   │       ├── bookmark-dal.test.ts
│   │       ├── bookmark.test.ts
│   │       ├── comic-dal.test.ts
│   │       ├── comic-features.e2e.ts
│   │       ├── comic.actions.test.ts
│   │       ├── comic.e2e.ts
│   │       ├── comic.schema.test.ts
│   │       ├── comment.actions.test.ts
│   │       ├── comment.test.ts
│   │       ├── fixtures/
│   │       │   ├── chapter.sample.json
│   │       │   ├── comic.create.json
│   │       │   ├── comic.db.json
│   │       │   └── user.sample.json
│   │       ├── follow-dal.test.ts
│   │       ├── permission-dal.test.ts
│   │       ├── profile.actions.test.ts
│   │       ├── profile.e2e.ts
│   │       ├── rating.test.ts
│   │       ├── reading-progress.actions.test.ts
│   │       ├── role-dal.test.ts
│   │       ├── search-dal.test.ts
│   │       ├── search-schema.test.ts
│   │       ├── search.actions.test.ts
│   │       ├── setup-env.ts
│   │       └── share-dal.test.ts
│   ├── components/
│   │   ├── activity/
│   │   │   └── activity-feed.tsx
│   │   ├── admin/
│   │   │   ├── admin-artists-wrapper.tsx
│   │   │   ├── admin-audit-logs-wrapper.tsx
│   │   │   ├── admin-authors-wrapper.tsx
│   │   │   ├── admin-chapters-wrapper.tsx
│   │   │   ├── admin-comics-wrapper.tsx
│   │   │   ├── admin-genres-wrapper.tsx
│   │   │   ├── admin-permissions-wrapper.tsx
│   │   │   ├── admin-roles-wrapper.tsx
│   │   │   ├── admin-types-wrapper.tsx
│   │   │   ├── admin-users-wrapper.tsx
│   │   │   └── admin-wrapper.tsx
│   │   ├── analytics/
│   │   │   ├── reading-dashboard.tsx
│   │   │   ├── reading-goals-widget.tsx
│   │   │   ├── reading-history-timeline.tsx
│   │   │   └── reading-stats-card.tsx
│   │   ├── auth/
│   │   │   ├── sign-in/
│   │   │   │   ├── sign-in-form.tsx
│   │   │   │   └── sign-in-wrapper.tsx
│   │   │   └── sign-up/
│   │   │       ├── sign-up-form.tsx
│   │   │       └── sign-up-wrapper.tsx
│   │   ├── bookmarks/
│   │   │   ├── bookmark-card.tsx
│   │   │   ├── bookmarks-filter.tsx
│   │   │   ├── bookmarks-wrapper.tsx
│   │   │   ├── index.ts
│   │   │   ├── resume-button.tsx
│   │   │   └── status-editor.tsx
│   │   ├── browse/
│   │   │   └── browse-wrapper.tsx
│   │   ├── comics/
│   │   │   ├── bookmark-button.tsx
│   │   │   ├── comic-card.tsx
│   │   │   ├── comic-detail-wrapper.tsx
│   │   │   ├── comic-filters.tsx
│   │   │   ├── comic-list-skeleton.tsx
│   │   │   ├── comic-pagination-controls.tsx
│   │   │   ├── comics-wrapper.tsx
│   │   │   ├── empty-state.tsx
│   │   │   ├── index.ts
│   │   │   └── share-button.tsx
│   │   ├── comments/
│   │   │   ├── chapter-comments-section.tsx
│   │   │   ├── comment-card.tsx
│   │   │   ├── comment-form.tsx
│   │   │   ├── comment-list.tsx
│   │   │   ├── comments-wrapper.tsx
│   │   │   └── index.ts
│   │   ├── feed/
│   │   │   └── feed-wrapper.tsx
│   │   ├── genres/
│   │   │   └── genre-detail-wrapper.tsx
│   │   ├── home/
│   │   │   ├── continue-reading-section.tsx
│   │   │   └── home-wrapper.tsx
│   │   ├── layout/
│   │   │   ├── app-sidebar.tsx
│   │   │   ├── chart-area-interactive.tsx
│   │   │   ├── current-year-client.tsx
│   │   │   ├── current-year.tsx
│   │   │   ├── data-table.tsx
│   │   │   ├── footer.tsx
│   │   │   ├── layout-provider.tsx
│   │   │   ├── logo.tsx
│   │   │   ├── nav-documents.tsx
│   │   │   ├── nav-main.tsx
│   │   │   ├── nav-secondary.tsx
│   │   │   ├── nav-user.tsx
│   │   │   ├── navbar-client.tsx
│   │   │   ├── navbar.tsx
│   │   │   ├── section-cards.tsx
│   │   │   └── site-header.tsx
│   │   ├── notifications/
│   │   │   ├── notification-bell.tsx
│   │   │   └── notifications-wrapper.tsx
│   │   ├── profile/
│   │   │   ├── change-password-form.tsx
│   │   │   ├── delete-account-form.tsx
│   │   │   ├── index.ts
│   │   │   ├── profile-edit-form.tsx
│   │   │   ├── profile-wrapper.tsx
│   │   │   └── settings-form.tsx
│   │   ├── ratings/
│   │   │   ├── comic-ratings-display.tsx
│   │   │   ├── comic-ratings-section.tsx
│   │   │   ├── index.ts
│   │   │   ├── rating-button.tsx
│   │   │   ├── rating-form.tsx
│   │   │   ├── rating-stats.tsx
│   │   │   └── ratings-wrapper.tsx
│   │   ├── reading/
│   │   │   ├── chapter-reader-wrapper.tsx
│   │   │   ├── chapter-reader.tsx
│   │   │   ├── continue-reading-card.tsx
│   │   │   ├── continue-reading-section.tsx
│   │   │   ├── image-viewer.tsx
│   │   │   ├── index.ts
│   │   │   ├── progress-bar.tsx
│   │   │   ├── reader-controls.tsx
│   │   │   ├── reader-settings.tsx
│   │   │   └── reader-view.tsx
│   │   ├── reading-progress/
│   │   │   └── reading-progress-wrapper.tsx
│   │   ├── recommendations/
│   │   │   └── recommended-section.tsx
│   │   ├── search/
│   │   │   ├── advanced-search-form.tsx
│   │   │   ├── index.ts
│   │   │   ├── search-input.tsx
│   │   │   ├── search-results-content.tsx
│   │   │   ├── search-results.tsx
│   │   │   ├── search-suggestions-dropdown.tsx
│   │   │   └── search-wrapper.tsx
│   │   ├── settings/
│   │   │   ├── index.ts
│   │   │   └── settings-form.tsx
│   │   ├── theme/
│   │   │   └── theme-toggle.tsx
│   │   ├── ui/
│   │   │   ├── accordion.tsx
│   │   │   ├── action-button.tsx
│   │   │   ├── alert-dialog.tsx
│   │   │   ├── alert.tsx
│   │   │   ├── aspect-ratio.tsx
│   │   │   ├── avatar.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── breadcrumb.tsx
│   │   │   ├── button-group.tsx
│   │   │   ├── button.tsx
│   │   │   ├── calendar.tsx
│   │   │   ├── card.tsx
│   │   │   ├── carousel.tsx
│   │   │   ├── chart.tsx
│   │   │   ├── checkbox.tsx
│   │   │   ├── collapsible.tsx
│   │   │   ├── combobox.tsx
│   │   │   ├── command.tsx
│   │   │   ├── context-menu.tsx
│   │   │   ├── data-table.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── direction.tsx
│   │   │   ├── drawer.tsx
│   │   │   ├── dropdown-menu.tsx
│   │   │   ├── empty.tsx
│   │   │   ├── field.tsx
│   │   │   ├── form.tsx
│   │   │   ├── hover-card.tsx
│   │   │   ├── input-group.tsx
│   │   │   ├── input-otp.tsx
│   │   │   ├── input.tsx
│   │   │   ├── item.tsx
│   │   │   ├── kbd.tsx
│   │   │   ├── label.tsx
│   │   │   ├── loading-swap.tsx
│   │   │   ├── menubar.tsx
│   │   │   ├── multi-select.tsx
│   │   │   ├── native-select.tsx
│   │   │   ├── navigation-menu.tsx
│   │   │   ├── number-input.tsx
│   │   │   ├── pagination.tsx
│   │   │   ├── password-input.tsx
│   │   │   ├── popover.tsx
│   │   │   ├── progress.tsx
│   │   │   ├── radio-group.tsx
│   │   │   ├── resizable.tsx
│   │   │   ├── scroll-area.tsx
│   │   │   ├── select.tsx
│   │   │   ├── separator.tsx
│   │   │   ├── sheet.tsx
│   │   │   ├── sidebar.tsx
│   │   │   ├── skeleton.tsx
│   │   │   ├── slider.tsx
│   │   │   ├── sonner.tsx
│   │   │   ├── spinner.tsx
│   │   │   ├── switch.tsx
│   │   │   ├── table.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── textarea.tsx
│   │   │   ├── toggle-group.tsx
│   │   │   ├── toggle.tsx
│   │   │   └── tooltip.tsx
│   │   └── users/
│   │       ├── follow-button.tsx
│   │       └── follow-stats.tsx
│   ├── dal/
│   │   ├── artist-dal.ts
│   │   ├── audit-log-dal.ts
│   │   ├── auth-db.ts
│   │   ├── author-dal.ts
│   │   ├── base-dal.ts
│   │   ├── bookmark-dal.ts
│   │   ├── chapter-dal.ts
│   │   ├── chapter-image-dal.ts
│   │   ├── comic-dal.ts
│   │   ├── comic-image-dal.ts
│   │   ├── comment-rating-dal.ts
│   │   ├── follow-dal.ts
│   │   ├── genre-dal.ts
│   │   ├── index.ts
│   │   ├── notification-dal.ts
│   │   ├── password-reset-dal.ts
│   │   ├── permission-dal.ts
│   │   ├── reading-goals-dal.ts
│   │   ├── reading-history-dal.ts
│   │   ├── reading-progress-dal.ts
│   │   ├── recommendation-dal.ts
│   │   ├── role-dal.ts
│   │   ├── search-dal.ts
│   │   ├── share-dal.ts
│   │   ├── type-dal.ts
│   │   ├── user-dal.ts
│   │   ├── user-preferences-dal.ts
│   │   └── user-role-dal.ts
│   ├── data/
│   │   ├── chapter.json
│   │   ├── comic.json
│   │   ├── merge-report.json
│   │   └── user.json
│   ├── database/
│   │   ├── db.ts
│   │   ├── drizzle/
│   │   │   ├── 0000_dry_lady_bullseye.sql
│   │   │   └── meta/
│   │   │       ├── 0000_snapshot.json
│   │   │       └── _journal.json
│   │   └── schema.ts
│   ├── hooks/
│   │   ├── use-debounce.ts
│   │   ├── use-keyboard-navigation.tsx
│   │   ├── use-mobile.ts
│   │   ├── use-now.tsx
│   │   ├── use-pagination.ts
│   │   └── use-performance-monitoring.tsx
│   ├── lib/
│   │   ├── accessibility.ts
│   │   ├── image-optimization.ts
│   │   ├── image-processor.ts
│   │   ├── performance-metrics.ts
│   │   ├── query-client.ts
│   │   └── utils.ts
│   ├── proxy.ts
│   ├── schemas/
│   │   ├── artist.schema.ts
│   │   ├── audit-log.schema.ts
│   │   ├── auth.schema.ts
│   │   ├── author.schema.ts
│   │   ├── bookmark-schema.ts
│   │   ├── chapter.schema.ts
│   │   ├── comic.schema.ts
│   │   ├── comment.schema.ts
│   │   ├── follow.schema.ts
│   │   ├── genre.schema.ts
│   │   ├── goals.schema.ts
│   │   ├── password-reset.schema.ts
│   │   ├── preferences.schema.ts
│   │   ├── profile.schema.ts
│   │   ├── rating.schema.ts
│   │   ├── rbac.schema.ts
│   │   ├── reading-progress.schema.ts
│   │   ├── reading-settings.schema.ts
│   │   ├── reading.schema.ts
│   │   ├── search.schema.ts
│   │   ├── seed/
│   │   │   ├── artist.seed.ts
│   │   │   ├── author.seed.ts
│   │   │   ├── bookmark.seed.ts
│   │   │   ├── chapter.seed.ts
│   │   │   ├── comic.seed.ts
│   │   │   ├── comment.seed.ts
│   │   │   ├── follow.seed.ts
│   │   │   ├── genre.seed.ts
│   │   │   ├── index.ts
│   │   │   ├── notification.seed.ts
│   │   │   ├── permission.seed.ts
│   │   │   ├── rating.seed.ts
│   │   │   ├── reader-settings.seed.ts
│   │   │   ├── reading-goal.seed.ts
│   │   │   ├── reading-history.seed.ts
│   │   │   ├── role.seed.ts
│   │   │   ├── share.seed.ts
│   │   │   ├── type.seed.ts
│   │   │   ├── user-preference.seed.ts
│   │   │   ├── user-role.seed.ts
│   │   │   └── user.seed.ts
│   │   ├── share.schema.ts
│   │   ├── type.schema.ts
│   │   ├── user.schema.ts
│   │   └── validators.ts
│   ├── scripts/
│   │   ├── audit-scripts.ts
│   │   ├── cache-stats.ts
│   │   ├── camelCaseConverter2025.ts
│   │   ├── check-db-counts.ts
│   │   ├── clear-cache.ts
│   │   ├── fix-duplicate-paths.ts
│   │   ├── fix-line-endings.ts
│   │   ├── git-commit.ts
│   │   ├── git-init.ts
│   │   ├── master-setup.ts
│   │   ├── optimize-performance.ts
│   │   ├── rename-to-kebab-case.ts
│   │   ├── scaffold.ts
│   │   ├── seed/
│   │   │   ├── config.ts
│   │   │   ├── data-loader.ts
│   │   │   ├── database/
│   │   │   │   ├── batch-processor.ts
│   │   │   │   ├── conflict-resolver.ts
│   │   │   │   └── transaction-manager.ts
│   │   │   ├── dependency-graph.ts
│   │   │   ├── helpers/
│   │   │   │   ├── chapter-matcher.ts
│   │   │   │   ├── chapter-number-extractor.ts
│   │   │   │   ├── comic-data-extractor.ts
│   │   │   │   ├── creator-name-resolver.ts
│   │   │   │   ├── date-parser.ts
│   │   │   │   ├── html-utils.ts
│   │   │   │   ├── image-deduplicator.ts
│   │   │   │   ├── image-fallback.ts
│   │   │   │   ├── image-migrator.ts
│   │   │   │   ├── image-url-validator.ts
│   │   │   │   └── progress-tracker.ts
│   │   │   ├── index.ts
│   │   │   ├── logger.ts
│   │   │   ├── README.md
│   │   │   ├── run.ts
│   │   │   ├── seed-orchestrator.ts
│   │   │   ├── seeders/
│   │   │   │   ├── artist-seeder.ts
│   │   │   │   ├── author-seeder.ts
│   │   │   │   ├── base-seed.ts
│   │   │   │   ├── bookmark-seeder.ts
│   │   │   │   ├── chapter-image-seeder.ts
│   │   │   │   ├── chapter-seeder.ts
│   │   │   │   ├── comic-image-seeder.ts
│   │   │   │   ├── comic-seeder.ts
│   │   │   │   ├── comment-seeder.ts
│   │   │   │   ├── follow-seeder.ts
│   │   │   │   ├── genre-seeder.ts
│   │   │   │   ├── notification-seeder.ts
│   │   │   │   ├── permission-seeder.ts
│   │   │   │   ├── rating-seeder.ts
│   │   │   │   ├── reader-settings-seeder.ts
│   │   │   │   ├── reading-goal-seeder.ts
│   │   │   │   ├── reading-history-seeder.ts
│   │   │   │   ├── role-seeder.ts
│   │   │   │   ├── share-seeder.ts
│   │   │   │   ├── type-seeder.ts
│   │   │   │   ├── user-preference-seeder.ts
│   │   │   │   ├── user-role-seeder.ts
│   │   │   │   └── user-seeder.ts
│   │   │   └── types.ts
│   │   ├── shared/
│   │   │   ├── colors.ts
│   │   │   ├── confirm.ts
│   │   │   ├── confirmAction.ts
│   │   │   ├── logger.ts
│   │   │   └── spinner.ts
│   │   ├── triage-quality-gate.ts
│   │   ├── unified-db-operations.ts
│   │   ├── unified-dev-setup.ts
│   │   ├── unified-performance-ops.ts
│   │   ├── unified-project-health.ts
│   │   ├── unified-schema-refactor.ts
│   │   ├── uninstall-unused-packages.ts
│   │   └── updateAnyTypes.ts
│   ├── storages/
│   │   ├── image-downloader.ts
│   │   ├── image-kit-uploader.ts
│   │   ├── image-strategy.ts
│   │   └── index.ts
│   ├── stores/
│   │   ├── index.ts
│   │   ├── reader-store.ts
│   │   ├── use-bookmark-store.ts
│   │   ├── use-notification-store.ts
│   │   ├── use-reader-store.ts
│   │   ├── use-reading-progress-store.ts
│   │   └── use-ui-store.ts
│   ├── styles/
│   │   ├── fonts/
│   │   │   ├── Bebas_Neue/
│   │   │   │   ├── BebasNeue-Regular.ttf
│   │   │   │   └── OFL.txt
│   │   │   ├── BebasNeue-Regular.ttf
│   │   │   ├── Fira_Mono/
│   │   │   │   ├── FiraMono-Bold.ttf
│   │   │   │   ├── FiraMono-Medium.ttf
│   │   │   │   ├── FiraMono-Regular.ttf
│   │   │   │   └── OFL.txt
│   │   │   ├── Fira_Sans/
│   │   │   │   ├── FiraSans-Black.ttf
│   │   │   │   ├── FiraSans-BlackItalic.ttf
│   │   │   │   ├── FiraSans-Bold.ttf
│   │   │   │   ├── FiraSans-BoldItalic.ttf
│   │   │   │   ├── FiraSans-ExtraBold.ttf
│   │   │   │   ├── FiraSans-ExtraBoldItalic.ttf
│   │   │   │   ├── FiraSans-ExtraLight.ttf
│   │   │   │   ├── FiraSans-ExtraLightItalic.ttf
│   │   │   │   ├── FiraSans-Italic.ttf
│   │   │   │   ├── FiraSans-Light.ttf
│   │   │   │   ├── FiraSans-LightItalic.ttf
│   │   │   │   ├── FiraSans-Medium.ttf
│   │   │   │   ├── FiraSans-MediumItalic.ttf
│   │   │   │   ├── FiraSans-Regular.ttf
│   │   │   │   ├── FiraSans-SemiBold.ttf
│   │   │   │   ├── FiraSans-SemiBoldItalic.ttf
│   │   │   │   ├── FiraSans-Thin.ttf
│   │   │   │   ├── FiraSans-ThinItalic.ttf
│   │   │   │   └── OFL.txt
│   │   │   ├── Fira_Sans_Condensed/
│   │   │   │   ├── FiraSansCondensed-Black.ttf
│   │   │   │   ├── FiraSansCondensed-BlackItalic.ttf
│   │   │   │   ├── FiraSansCondensed-Bold.ttf
│   │   │   │   ├── FiraSansCondensed-BoldItalic.ttf
│   │   │   │   ├── FiraSansCondensed-ExtraBold.ttf
│   │   │   │   ├── FiraSansCondensed-ExtraBoldItalic.ttf
│   │   │   │   ├── FiraSansCondensed-ExtraLight.ttf
│   │   │   │   ├── FiraSansCondensed-ExtraLightItalic.ttf
│   │   │   │   ├── FiraSansCondensed-Italic.ttf
│   │   │   │   ├── FiraSansCondensed-Light.ttf
│   │   │   │   ├── FiraSansCondensed-LightItalic.ttf
│   │   │   │   ├── FiraSansCondensed-Medium.ttf
│   │   │   │   ├── FiraSansCondensed-MediumItalic.ttf
│   │   │   │   ├── FiraSansCondensed-Regular.ttf
│   │   │   │   ├── FiraSansCondensed-SemiBold.ttf
│   │   │   │   ├── FiraSansCondensed-SemiBoldItalic.ttf
│   │   │   │   ├── FiraSansCondensed-Thin.ttf
│   │   │   │   ├── FiraSansCondensed-ThinItalic.ttf
│   │   │   │   └── OFL.txt
│   │   │   ├── IBM_Plex_Sans/
│   │   │   │   ├── IBMPlexSans-Italic-VariableFont_wdth,wght.ttf
│   │   │   │   ├── IBMPlexSans-VariableFont_wdth,wght.ttf
│   │   │   │   ├── OFL.txt
│   │   │   │   ├── README.txt
│   │   │   │   └── static/
│   │   │   ├── IBMPlexSans-Bold.ttf
│   │   │   ├── IBMPlexSans-Medium.ttf
│   │   │   ├── IBMPlexSans-Regular.ttf
│   │   │   ├── IBMPlexSans-SemiBold.ttf
│   │   │   ├── Martian_Mono/
│   │   │   │   ├── MartianMono-VariableFont_wdth,wght.ttf
│   │   │   │   ├── OFL.txt
│   │   │   │   ├── README.txt
│   │   │   │   └── static/
│   │   │   └── Schibsted_Grotesk/
│   │   │       ├── OFL.txt
│   │   │       ├── README.txt
│   │   │       ├── SchibstedGrotesk-Italic-VariableFont_wght.ttf
│   │   │       ├── SchibstedGrotesk-VariableFont_wght.ttf
│   │   │       └── static/
│   │   └── globals.css
│   ├── tests/
│   │   ├── e2e/
│   │   │   ├── admin/
│   │   │   │   ├── admin.spec.ts
│   │   │   │   └── users.spec.ts
│   │   │   ├── auth-pages/
│   │   │   │   ├── bookmarks.spec.ts
│   │   │   │   ├── notifications.spec.ts
│   │   │   │   ├── profile-edit.spec.ts
│   │   │   │   ├── profile-settings.spec.ts
│   │   │   │   ├── profile.spec.ts
│   │   │   │   └── reading-progress.spec.ts
│   │   │   ├── fixtures/
│   │   │   │   ├── admin.fixture.ts
│   │   │   │   └── auth.fixture.ts
│   │   │   └── pages/
│   │   │       ├── author.spec.ts
│   │   │       ├── browse.spec.ts
│   │   │       ├── comic-detail.spec.ts
│   │   │       ├── comics.spec.ts
│   │   │       ├── genre.spec.ts
│   │   │       ├── home.spec.ts
│   │   │       └── search.spec.ts
│   │   └── unit/
│   │       ├── actions/
│   │       │   ├── author.actions.test.ts
│   │       │   ├── browse.actions.test.ts
│   │       │   ├── genre.actions.test.ts
│   │       │   ├── notification.actions.test.ts
│   │       │   └── search-filters.actions.test.ts
│   │       └── setup-env.ts
│   └── types/
│       ├── actions-types.ts
│       ├── bookmark.ts
│       ├── comic.ts
│       ├── comment-rating.ts
│       ├── comment.ts
│       ├── eslint-plugin-drizzle-generated.d.ts
│       ├── eslint-plugin-drizzle.d.ts
│       ├── eslint-plugin-security.d.ts
│       ├── globals.d.ts
│       ├── index.ts
│       ├── notification.ts
│       ├── profile.ts
│       ├── reading-progress.ts
│       └── user-preferences.ts
├── tech-stack.md
├── technology-stack.md
├── test-report.txt
├── test-ui-report.txt
├── TESTING_GUIDE.md
├── triage-report.txt
├── tsconfig.json
├── validation-report.md
└── vitest.config.mts
```

## Key Directories

| Directory                      | Purpose                            | Convention                          |
| ------------------------------ | ---------------------------------- | ----------------------------------- |
| `app/`                         | Next.js App Router pages & layouts | Feature-based subdirectories        |
| `components/`                  | React components                   | PascalCase, co-located with feature |
| `lib/`                         | Shared utilities                   | camelCase files                     |
| `db/` / `prisma/` / `drizzle/` | Database schema & ORM              | Standard conventions                |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---

_Generated by agents-system-prompt-context-fix-runner_
