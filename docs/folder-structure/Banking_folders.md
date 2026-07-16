# Banking - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\Banking`
**Generated:** 2026-07-10
**Stack:** Next.js

## Directory Tree

```
Banking/
├── .editorconfig
├── .github/
│   ├── branch-compare-ignore
│   ├── copilot-instructions.md
│   ├── DOCKER_CI_CD_GUIDE.md
│   ├── GITHUB_ACTIONS_SETUP.md
│   ├── pull_request_template.md
│   └── workflows/
│       ├── auto-add-run-e2e.yml
│       ├── build.yml
│       ├── check-line-endings.yml
│       ├── check-plugin-structure.yml
│       ├── check-pr-target.yml
│       ├── ci-reports.yml
│       ├── ci.yml
│       ├── cli-for-beginners-sync.lock.yml
│       ├── cli-for-beginners-sync.md
│       ├── codeowner-update.lock.yml
│       ├── codeowner-update.md
│       ├── codespell.yml
│       ├── contributors.yml
│       ├── copilot-setup-steps.yml
│       ├── daily-issues-report.md
│       ├── deploy.yml
│       ├── docker-security.yml
│       ├── generate-readme.yml
│       ├── opencode.yml
│       ├── ospo-contributors-report.md
│       ├── ospo-org-health.md
│       ├── ospo-release-compliance-checker.md
│       ├── ospo-stale-repos.md
│       ├── plan-check.yml
│       ├── playwright.yml
│       ├── relevance-check.md
│       ├── relevance-summary.md
│       ├── validate-pr.yml
│       ├── vercel-preview.yml
│       ├── verify-agents.yml
│       └── verify-main-branches.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── API_REFERENCE.md
├── app-config.ts
├── ARCHITECTURE.md
├── bin/
│   ├── cleanup/
│   │   ├── cleanup-docker.bat
│   │   ├── cleanup-docker.ps1
│   │   ├── cleanup-docker.sh
│   │   ├── cleanup-docs.bat
│   │   ├── cleanup-docs.ps1
│   │   └── cleanup-docs.sh
│   ├── deploy/
│   │   ├── compose/
│   │   │   └── traefik/
│   │   │       └── auth/
│   │   ├── deploy.bat
│   │   ├── deploy.ps1
│   │   ├── deploy.sh
│   │   ├── generate-htpasswd.bat
│   │   ├── generate-htpasswd.ps1
│   │   └── generate-htpasswd.sh
│   ├── docker/
│   │   ├── deploy-checklist.bat
│   │   ├── deploy-checklist.ps1
│   │   ├── deploy-checklist.sh
│   │   ├── docker-quickstart.bat
│   │   ├── docker-quickstart.ps1
│   │   ├── docker-quickstart.sh
│   │   ├── entrypoint.sh
│   │   ├── generate-env.bat
│   │   ├── generate-env.ps1
│   │   └── generate-env.sh
│   ├── lib/
│   │   └── repo-root.sh
│   ├── server/
│   │   ├── gen-certs.bat
│   │   ├── gen-certs.ps1
│   │   ├── gen-certs.sh
│   │   ├── server-setup.bat
│   │   ├── server-setup.ps1
│   │   ├── server-setup.sh
│   │   ├── vps-setup.bat
│   │   ├── vps-setup.ps1
│   │   └── vps-setup.sh
│   └── utils/
│       ├── ast/
│       │   └── ts-morph-utils.ts
│       ├── build.bat
│       ├── build.ps1
│       ├── build.sh
│       ├── check-events-detail.bat
│       ├── check-events-detail.ps1
│       ├── check-events.bat
│       ├── check-events.ps1
│       ├── ci-helpers/
│       │   ├── fast-check.ts
│       │   ├── git-commit-helper.ts
│       │   ├── index.ts
│       │   ├── lint-fix-wrapper.ts
│       │   ├── parse-reports.ts
│       │   ├── README.md
│       │   ├── report-parser.ts
│       │   ├── run-with-args.ts
│       │   ├── seed-prep.ts
│       │   └── targeted-test-runner.ts
│       ├── config-parser.ts
│       ├── constants.ts
│       ├── date-utils.ts
│       ├── disable-extensions.bat
│       ├── disable-extensions.ps1
│       ├── disable-extensions.sh
│       ├── fix-line-endings.bat
│       ├── fix-line-endings.ps1
│       ├── fix-line-endings.sh
│       ├── get-connection-string.ts
│       ├── io.ts
│       ├── markdown.ts
│       ├── read-secrets.bat
│       ├── read-secrets.ps1
│       ├── read-secrets.sh
│       ├── run-ci-checks.bat
│       ├── run-ci-checks.ps1
│       ├── run-ci-checks.sh
│       ├── shutdown.ts
│       ├── template.ts
│       ├── validation.ts
│       └── yaml.ts
├── bun.lock
├── bunfig.toml
├── CHANGELOG.md
├── code-exemplars.md
├── CODE_STYLE.md
├── components.json
├── compose/
│   ├── dev/
│   │   └── node/
│   │       └── Dockerfile
│   ├── prod/
│   │   ├── grafana/
│   │   │   └── provisioning/
│   │   │       ├── dashboards/
│   │   │       └── datasources/
│   │   └── prometheus/
│   │       ├── prometheus.yml
│   │       └── rules/
│   │           └── app-alerts.yml
│   └── traefik/
│       ├── auth/
│       │   └── htpasswd
│       ├── dynamic/
│       │   ├── middlewares.yml
│       │   └── tls.yml
│       └── traefik.yml
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── database/
│   └── drizzle/
│       ├── 0000_overconfident_jack_murdock.sql
│       └── meta/
│           ├── 0000_snapshot.json
│           └── _journal.json
├── DATABASE_SCHEMA.md
├── debug-pw.ts
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── docker-compose.yml
├── docs/
│   ├── actions-audit.md
│   ├── api-payments.md
│   ├── app-pages.md
│   ├── Credentials-Provider-context.md
│   ├── custom-components.md
│   ├── dal-audit.md
│   ├── dal-schedule.md
│   ├── db-schema-audit.md
│   ├── deploy-to-hostinger.md
│   ├── deploy-to-railway.md
│   ├── deploy-to-vercel-cli.md
│   ├── deploy-to-vercel.md
│   ├── deployment.md
│   ├── DeveloperDocsIndex.md
│   ├── DockerGuide.md
│   ├── Drizzle-ORM-Adapter-context.md
│   ├── DrizzleORMGuide.md
│   ├── DwollaIntegrationGuide.md
│   ├── env-vars.md
│   ├── eslint-config-next-context.md
│   ├── eslint-config-prettier-context.md
│   ├── ESLintPluginsGuide.md
│   ├── GetStartedWithDrizzleAndNeon-context.md
│   ├── GetStartedWithDrizzleAndPostgreSQL-context.md
│   ├── Getting-Started-Example-context.md
│   ├── github-actions.md
│   ├── Guides-context.md
│   ├── init-awesome-opencode.md
│   ├── mcp/
│   │   └── docker-mcp-adminbot.md
│   ├── my-wallets-audit.md
│   ├── Next-js-context.md
│   ├── nextjs/
│   │   └── app-router-caching.md
│   ├── patterns/
│   │   └── pattern-reference.md
│   ├── per-repo-research-summary.md
│   ├── plaid/
│   │   ├── link-guide.md
│   │   ├── quickstart.md
│   │   └── transactions.md
│   ├── PlaidIntegrationGuide.md
│   ├── plans/
│   │   ├── banking-refactor.md
│   │   ├── codebase-overhaul.md
│   │   ├── e2e-test-fix.md
│   │   ├── mcp-server-install.md
│   │   ├── playwright-test-enhancement.md
│   │   └── rules-audit-fix.md
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── react-bits.md
│   ├── react-plaid-link.md
│   ├── refactor-context.md
│   ├── schema-design.md
│   ├── scripts-context.md
│   ├── scripts.md
│   ├── secrets-management.md
│   ├── sections/
│   │   ├── section-01.md
│   │   ├── section-02.md
│   │   ├── section-03.md
│   │   ├── section-04.md
│   │   ├── section-05.md
│   │   ├── section-06.md
│   │   ├── section-07.md
│   │   ├── section-08.md
│   │   ├── section-09.md
│   │   ├── section-10.md
│   │   ├── section-11.md
│   │   ├── section-12.md
│   │   ├── section-13.md
│   │   ├── section-14.md
│   │   ├── section-15.md
│   │   ├── section-16.md
│   │   ├── section-17.md
│   │   ├── section-18.md
│   │   ├── section-19.md
│   │   ├── section-20.md
│   │   ├── section-21.md
│   │   ├── section-22.md
│   │   ├── section-23.md
│   │   ├── section-24.md
│   │   ├── section-25.md
│   │   ├── section-26.md
│   │   ├── section-27.md
│   │   └── section-28.md
│   ├── security.md
│   ├── services/
│   │   ├── nextjs-docker.md
│   │   ├── react-patterns.md
│   │   ├── shadcn-studio.md
│   │   ├── shadcn-ui.md
│   │   └── traefik.md
│   ├── shadcn-ui-intro.md
│   ├── shadcn.md
│   ├── specs/
│   │   ├── audit-findings.md
│   │   ├── banking-overhaul-spec.md
│   │   ├── codebase-overhaul-v2.md
│   │   ├── e2e-test-catalog.md
│   │   ├── new-rules.md
│   │   ├── playwright-console-errors.md
│   │   ├── playwright-coverage.md
│   │   ├── playwright-debugging.md
│   │   └── playwright-speed-optimization.md
│   ├── superpowers/
│   │   ├── plans/
│   │   │   └── 2026-05-10-e2e-test-fix.md
│   │   └── specs/
│   │       └── 2026-05-10-e2e-test-catalog.md
│   ├── test-context.md
│   ├── TypeScript-context.md
│   ├── typescript-eslint-parser-context.md
│   └── zod-audit.md
├── drizzle.config.ts
├── eslint.config.mts
├── execution-summary.md
├── folder-structure.md
├── init-env.ts
├── install-agents.sh
├── install.sh
├── LICENSE
├── Makefile
├── my-plugin.ts
├── next-env.d.ts
├── next-sitemap.config.ts
├── next.config.ts
├── package.json
├── playwright.config.ts
├── postcss.config.mjs
├── project-workflow.md
├── proxy.ts
├── public/
│   ├── icons/
│   │   ├── a-coffee.svg
│   │   ├── arrow-left.svg
│   │   ├── auth-image.svg
│   │   ├── coins.svg
│   │   ├── connect-bank.svg
│   │   ├── dollar-circle.svg
│   │   ├── gradient-mesh.svg
│   │   ├── hamburger.svg
│   │   ├── home.svg
│   │   ├── logo.svg
│   │   ├── logout.svg
│   │   ├── money-send.svg
│   │   ├── monitor.svg
│   │   ├── shopping-bag.svg
│   │   └── transaction.svg
│   ├── robots.txt
│   ├── sitemap-0.xml
│   └── sitemap.xml
├── railway.json
├── Railway.toml
├── README.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── RESEARCH_UPDATE.md
├── run-tasks.txt
├── run-tasks.txt.backup
├── scripts/
│   ├── aggressive-capture.ps1
│   ├── branch-compare.sh
│   ├── codemap.md
│   ├── codemod/
│   │   ├── find-process-env.ts
│   │   └── run-codemod.ts
│   ├── db/
│   │   ├── apply-migrations.ts
│   │   └── apply-select-migrations.ts
│   ├── debug-pw.ts
│   ├── delete-gone-branches.sh
│   ├── diagnose-and-fix-git.ps1
│   ├── diagnose-and-fix-git.sh
│   ├── export-data.ts
│   ├── export-json.ts
│   ├── generate/
│   │   ├── action.ts
│   │   ├── component.ts
│   │   ├── dal.ts
│   │   ├── docs-gen.ts
│   │   └── feature.ts
│   ├── generate-readme.ts
│   ├── maintenance/
│   │   ├── analyze-lint-scan.ts
│   │   └── lint-fix-runner.ts
│   ├── mcp-runner-lib.ts
│   ├── mcp-runner.ts
│   ├── opencode-mcp.bat
│   ├── opencode-mcp.ps1
│   ├── opencode-mcp.sh
│   ├── opencode-plugin-repair.bat
│   ├── opencode-plugin-repair.ps1
│   ├── opencode-plugin-repair.sh
│   ├── opencode-plugin-verify.bat
│   ├── opencode-plugin-verify.ps1
│   ├── opencode-plugin-verify.sh
│   ├── orchestrator.bat
│   ├── orchestrator.ps1
│   ├── orchestrator.sh
│   ├── orchestrator.ts
│   ├── plan-ensure.bat
│   ├── plan-ensure.sh
│   ├── plan-ensure.ts
│   ├── provenance/
│   │   └── generate-provenance.ts
│   ├── README.md
│   ├── report-parser.ts
│   ├── run-verify-and-validate.ps1
│   ├── seed/
│   │   ├── create-plaid-tokens.ts
│   │   ├── get-planned-seed-summary.ts
│   │   ├── run.ts
│   │   ├── seed-config.ts
│   │   ├── seed-data.ts
│   │   └── seed-ids.ts
│   ├── transform/
│   │   └── zod-meta-to-describe.ts
│   ├── ts/
│   │   ├── aggressive-capture.ts
│   │   ├── branch-compare.ts
│   │   ├── build.ts
│   │   ├── cleanup/
│   │   │   ├── cleanup-docker.ts
│   │   │   └── cleanup-docs.ts
│   │   ├── deploy/
│   │   │   ├── deploy.ts
│   │   │   └── generate-htpasswd.ts
│   │   ├── diagnose-and-fix-git-unix.ts
│   │   ├── diagnose-and-fix-git.ts
│   │   ├── docker/
│   │   │   ├── deploy-checklist.ts
│   │   │   ├── docker-quickstart.ts
│   │   │   ├── entrypoint.ts
│   │   │   └── generate-env.ts
│   │   ├── docs/
│   │   │   └── generate-markdown-catalog.ts
│   │   ├── entrypoints/
│   │   │   ├── deploy-cli.ts
│   │   │   └── run-verify-and-validate-cli.ts
│   │   ├── mcp-runner.ts
│   │   ├── opencode-mcp.ts
│   │   ├── plugin-repair.ts
│   │   ├── plugin-verify.ts
│   │   ├── read-secrets.ts
│   │   ├── run-ci-checks.ts
│   │   ├── run-verify-and-validate.ts
│   │   ├── server/
│   │   │   ├── gen-certs.ts
│   │   │   ├── server-setup.ts
│   │   │   └── vps-setup.ts
│   │   ├── sweep-wrap-remaining.ts
│   │   ├── tools/
│   │   │   ├── create-issues-from-catalog.ts
│   │   │   ├── discover-app-pages.ts
│   │   │   └── generate-inventory.ts
│   │   ├── utils/
│   │   │   ├── ast.ts
│   │   │   ├── check-events-detail.ts
│   │   │   ├── check-events.ts
│   │   │   ├── ci-helpers/
│   │   │   │   └── git-commit-helper-wrapper.ts
│   │   │   ├── cli.ts
│   │   │   ├── disable-extensions-wrapper.ts
│   │   │   ├── disable-extensions.ts
│   │   │   ├── fix-line-endings.ts
│   │   │   ├── fs-safe.ts
│   │   │   ├── plugin-shared.ts
│   │   │   ├── read-secrets-helpers.ts
│   │   │   ├── read-secrets-wrapper.ts
│   │   │   ├── run-ci-checks-wrapper.ts
│   │   │   └── spawn-safe.ts
│   │   └── verify-agents.ts
│   ├── types/
│   │   └── index.ts
│   ├── validate/
│   │   ├── actions.ts
│   │   ├── env.ts
│   │   ├── schema.ts
│   │   └── types.ts
│   ├── validate.ts
│   ├── verify-agent-iterations.ts
│   ├── verify-agents.ps1
│   ├── verify-agents.sh
│   └── verify-rules.ts
├── SECURITY.md
├── setup-tests.ts
├── SETUP_GUIDE.md
├── src/
│   ├── actions/
│   │   ├── admin-stats.actions.ts
│   │   ├── admin.actions.ts
│   │   ├── auth.register.ts
│   │   ├── auth.signin.ts
│   │   ├── dwolla.actions.ts
│   │   ├── plaid.actions.ts
│   │   ├── recipient.actions.ts
│   │   ├── transaction.actions.ts
│   │   ├── user.actions.ts
│   │   ├── user.update-profile.ts
│   │   └── wallet.actions.ts
│   ├── app/
│   │   ├── (admin)/
│   │   │   ├── admin/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   └── layout.tsx
│   │   ├── (auth)/
│   │   │   ├── layout.tsx
│   │   │   ├── sign-in/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   └── sign-up/
│   │   │       ├── error.tsx
│   │   │       ├── loading.tsx
│   │   │       └── page.tsx
│   │   ├── (root)/
│   │   │   ├── dashboard/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── layout.tsx
│   │   │   ├── my-wallets/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── payment-transfer/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── settings/
│   │   │   │   ├── error.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   └── transaction-history/
│   │   │       ├── error.tsx
│   │   │       ├── loading.tsx
│   │   │       └── page.tsx
│   │   ├── __playwright__/
│   │   │   └── set-cookie/
│   │   │       └── route.ts
│   │   ├── api/
│   │   │   ├── __playwright__/
│   │   │   │   └── set-cookie/
│   │   │   ├── auth/
│   │   │   │   ├── [...nextauth]/
│   │   │   │   ├── local-create/
│   │   │   │   └── local-validate/
│   │   │   ├── dwolla/
│   │   │   │   └── webhook/
│   │   │   └── health/
│   │   │       └── route.ts
│   │   ├── global-error.tsx
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── not-found.tsx
│   │   └── page.tsx
│   ├── assets/
│   │   └── svg/
│   │       ├── auth-background-shape.tsx
│   │       ├── bistro-logo.tsx
│   │       └── logo.tsx
│   ├── components/
│   │   ├── admin/
│   │   │   ├── admin-dashboard-content.tsx
│   │   │   ├── admin-dashboard-server-wrapper.tsx
│   │   │   ├── admin-data.tsx
│   │   │   └── index.ts
│   │   ├── animated-counter/
│   │   │   ├── animated-counter.tsx
│   │   │   └── index.ts
│   │   ├── auth-form/
│   │   │   └── auth-form.tsx
│   │   ├── chart-area-interactive/
│   │   │   ├── chart-area-interactive.tsx
│   │   │   └── index.ts
│   │   ├── dashboard/
│   │   │   ├── dashboard-client-wrapper.tsx
│   │   │   ├── dashboard-server-wrapper.tsx
│   │   │   └── index.ts
│   │   ├── doughnut-chart/
│   │   │   ├── doughnut-chart.tsx
│   │   │   └── index.ts
│   │   ├── footer/
│   │   │   ├── footer.tsx
│   │   │   └── index.ts
│   │   ├── global-error/
│   │   │   ├── global-error-client-wrapper.tsx
│   │   │   └── index.ts
│   │   ├── header-box/
│   │   │   ├── header-box.tsx
│   │   │   └── index.ts
│   │   ├── home/
│   │   │   ├── home-server-wrapper.tsx
│   │   │   └── index.ts
│   │   ├── layouts/
│   │   │   ├── admin-dashboard/
│   │   │   │   └── index.tsx
│   │   │   ├── admin-data/
│   │   │   │   └── index.tsx
│   │   │   ├── admin-sidebar.tsx
│   │   │   ├── AdminLayoutWrapper.tsx
│   │   │   ├── auth-form/
│   │   │   │   └── index.tsx
│   │   │   ├── auth-page-wrapper.tsx
│   │   │   ├── AuthLayoutWrapper.tsx
│   │   │   ├── card/
│   │   │   │   └── index.tsx
│   │   │   ├── cta-get-started.tsx
│   │   │   ├── dashboard-client/
│   │   │   │   └── index.tsx
│   │   │   ├── data-table/
│   │   │   │   └── index.tsx
│   │   │   ├── features-grid.tsx
│   │   │   ├── form/
│   │   │   │   ├── form-field.tsx
│   │   │   │   └── index.tsx
│   │   │   ├── generic-card/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-data-table/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-empty-state/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-form/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-modal/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-page-shell/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-skeleton/
│   │   │   │   └── index.tsx
│   │   │   ├── generic-toast/
│   │   │   │   └── index.tsx
│   │   │   ├── home-footer.tsx
│   │   │   ├── index.ts
│   │   │   ├── my-wallets-client/
│   │   │   │   └── index.tsx
│   │   │   ├── page-container/
│   │   │   │   └── index.tsx
│   │   │   ├── PageShell.tsx
│   │   │   ├── payment-transfer-client/
│   │   │   │   └── index.tsx
│   │   │   ├── payment-transfer-form.tsx
│   │   │   ├── plaid-provider.tsx
│   │   │   ├── RootLayoutWrapper.tsx
│   │   │   ├── row/
│   │   │   │   └── index.tsx
│   │   │   ├── section-header/
│   │   │   │   └── index.tsx
│   │   │   ├── settings-client/
│   │   │   │   └── index.tsx
│   │   │   ├── settings-profile-form.tsx
│   │   │   ├── stat-card/
│   │   │   │   └── index.tsx
│   │   │   ├── total-balance/
│   │   │   │   └── index.tsx
│   │   │   ├── transaction-history-client/
│   │   │   │   └── index.tsx
│   │   │   ├── transaction-list.tsx
│   │   │   ├── transfer-summary.tsx
│   │   │   └── wallet-card/
│   │   │       └── index.tsx
│   │   ├── mobile-nav/
│   │   │   ├── index.ts
│   │   │   └── mobile-nav.tsx
│   │   ├── my-wallets/
│   │   │   ├── index.ts
│   │   │   ├── my-wallets-client-wrapper.tsx
│   │   │   └── my-wallets-server-wrapper.tsx
│   │   ├── nav-documents/
│   │   │   ├── index.ts
│   │   │   └── nav-documents.tsx
│   │   ├── nav-secondary/
│   │   │   ├── index.ts
│   │   │   └── nav-secondary.tsx
│   │   ├── not-found/
│   │   │   ├── index.ts
│   │   │   └── not-found-server-wrapper.tsx
│   │   ├── payment-transfer/
│   │   │   ├── index.ts
│   │   │   ├── payment-transfer-client-wrapper.tsx
│   │   │   └── payment-transfer-server-wrapper.tsx
│   │   ├── plaid-context/
│   │   │   ├── index.ts
│   │   │   └── plaid-context.tsx
│   │   ├── plaid-link-button/
│   │   │   ├── index.ts
│   │   │   └── plaid-link-button.tsx
│   │   ├── section-cards/
│   │   │   ├── index.ts
│   │   │   └── section-cards.tsx
│   │   ├── settings/
│   │   │   ├── index.ts
│   │   │   ├── settings-client-wrapper.tsx
│   │   │   └── settings-server-wrapper.tsx
│   │   ├── shadcn-studio/
│   │   │   ├── blocks/
│   │   │   │   ├── account-settings-01/
│   │   │   │   ├── application-shell-01/
│   │   │   │   ├── chart-sales-metrics.tsx
│   │   │   │   ├── dashboard-shell-01/
│   │   │   │   ├── datatable-transaction.tsx
│   │   │   │   ├── dropdown-language.tsx
│   │   │   │   ├── dropdown-profile.tsx
│   │   │   │   ├── hero-section-41/
│   │   │   │   ├── menu-dropdown.tsx
│   │   │   │   ├── menu-navigation.tsx
│   │   │   │   ├── onboarding-feed-01/
│   │   │   │   ├── statistics-card-01.tsx
│   │   │   │   ├── widget-product-insights.tsx
│   │   │   │   └── widget-total-earning.tsx
│   │   │   └── index.ts
│   │   ├── shared/
│   │   │   ├── index.ts
│   │   │   └── wallets-overview.tsx
│   │   ├── sidebar/
│   │   │   ├── index.ts
│   │   │   └── sidebar.tsx
│   │   ├── sign-in/
│   │   │   └── sign-in-server-wrapper.tsx
│   │   ├── sign-up/
│   │   │   └── sign-up-server-wrapper.tsx
│   │   ├── total-balance-box/
│   │   │   └── total-balance-box.tsx
│   │   ├── transaction-history/
│   │   │   ├── transaction-history-client-wrapper.tsx
│   │   │   └── transaction-history-server-wrapper.tsx
│   │   └── ui/
│   │       ├── accordion.tsx
│   │       ├── action-button.tsx
│   │       ├── alert-dialog.tsx
│   │       ├── alert.tsx
│   │       ├── aspect-ratio.tsx
│   │       ├── avatar.tsx
│   │       ├── badge.tsx
│   │       ├── breadcrumb.tsx
│   │       ├── button-group.tsx
│   │       ├── button.tsx
│   │       ├── calendar.tsx
│   │       ├── card.tsx
│   │       ├── carousel.tsx
│   │       ├── chart.tsx
│   │       ├── checkbox.tsx
│   │       ├── collapsible.tsx
│   │       ├── combobox.tsx
│   │       ├── command.tsx
│   │       ├── container.tsx
│   │       ├── context-menu.tsx
│   │       ├── dialog.tsx
│   │       ├── direction.tsx
│   │       ├── drawer.tsx
│   │       ├── dropdown-menu.tsx
│   │       ├── empty.tsx
│   │       ├── field.tsx
│   │       ├── form.tsx
│   │       ├── hover-card.tsx
│   │       ├── input-group.tsx
│   │       ├── input-otp.tsx
│   │       ├── input.tsx
│   │       ├── item.tsx
│   │       ├── kbd.tsx
│   │       ├── label.tsx
│   │       ├── loading-swap.tsx
│   │       ├── menubar.tsx
│   │       ├── multi-select.tsx
│   │       ├── native-select.tsx
│   │       ├── navigation-menu.tsx
│   │       ├── number-input.tsx
│   │       ├── pagination.tsx
│   │       ├── password-input.tsx
│   │       ├── popover.tsx
│   │       ├── progress.tsx
│   │       ├── radio-group.tsx
│   │       ├── resizable.tsx
│   │       ├── scroll-area.tsx
│   │       ├── select.tsx
│   │       ├── separator.tsx
│   │       ├── sheet.tsx
│   │       ├── sidebar.tsx
│   │       ├── skeleton.tsx
│   │       ├── slider.tsx
│   │       ├── sonner.tsx
│   │       ├── spinner.tsx
│   │       ├── switch.tsx
│   │       ├── table.tsx
│   │       ├── tabs.tsx
│   │       ├── textarea.tsx
│   │       ├── toggle-group.tsx
│   │       ├── toggle.tsx
│   │       └── tooltip.tsx
│   ├── constants/
│   │   └── index.ts
│   ├── dal/
│   │   ├── admin.dal.ts
│   │   ├── dwolla.dal.ts
│   │   ├── errors.dal.ts
│   │   ├── health.ts
│   │   ├── index.ts
│   │   ├── recipient.dal.ts
│   │   ├── transaction.dal.ts
│   │   ├── user.dal.ts
│   │   └── wallet.dal.ts
│   ├── database/
│   │   ├── db.ts
│   │   ├── drizzle/
│   │   │   ├── 0000_supreme_legion.sql
│   │   │   └── meta/
│   │   │       ├── 0000_snapshot.json
│   │   │       └── _journal.json
│   │   ├── index.ts
│   │   └── schema.ts
│   ├── hooks/
│   │   ├── use-bank-connection.ts
│   │   ├── use-debounce.ts
│   │   ├── use-mobile.tsx
│   │   ├── use-pagination.ts
│   │   ├── use-transaction-filter.ts
│   │   └── use-wallet-balance.ts
│   ├── lib/
│   │   ├── auth-options.ts
│   │   ├── auth.ts
│   │   ├── dwolla.ts
│   │   ├── email.ts
│   │   ├── encryption.ts
│   │   ├── env.ts
│   │   ├── error-tracking.ts
│   │   ├── logger.ts
│   │   ├── plaid.ts
│   │   ├── playwright/
│   │   │   └── set-cookie.helper.ts
│   │   ├── schemas/
│   │   │   ├── auth.schema.ts
│   │   │   ├── index.ts
│   │   │   ├── profile.schema.ts
│   │   │   └── transfer.schema.ts
│   │   ├── session.ts
│   │   ├── utils.ts
│   │   ├── validation-utils.ts
│   │   └── validations/
│   │       ├── admin.ts
│   │       ├── auth.ts
│   │       ├── index.ts
│   │       └── transfer.ts
│   ├── stores/
│   │   ├── create-filter-store.ts
│   │   ├── create-toast-store.ts
│   │   ├── create-transfer-store.ts
│   │   ├── create-ui-store.ts
│   │   ├── filter-store.tsx
│   │   ├── index.ts
│   │   ├── providers.tsx
│   │   ├── session.tsx
│   │   ├── toast-store.tsx
│   │   ├── transfer-store.tsx
│   │   └── ui-store.tsx
│   ├── tests/
│   │   ├── e2e/
│   │   │   ├── admin.spec.ts
│   │   │   ├── auth.spec.ts
│   │   │   ├── dashboard.spec.ts
│   │   │   ├── global-setup.ts
│   │   │   ├── global-teardown.ts
│   │   │   ├── helpers/
│   │   │   │   ├── auth.ts
│   │   │   │   ├── db.ts
│   │   │   │   ├── dwolla.ts
│   │   │   │   ├── plaid.mock.ts
│   │   │   │   └── plaid.ts
│   │   │   ├── integration/
│   │   │   │   └── link-and-transfer.spec.ts
│   │   │   ├── mock-tokens.spec.ts
│   │   │   ├── my-wallets.spec.ts
│   │   │   ├── payment-transfer.spec.ts
│   │   │   ├── README.md
│   │   │   ├── settings.spec.ts
│   │   │   ├── soft-delete.spec.ts
│   │   │   ├── specs/
│   │   │   │   └── plaid-script.spec.ts
│   │   │   ├── transaction-history.spec.ts
│   │   │   ├── transfer-idempotency.spec.ts
│   │   │   ├── utils/
│   │   │   │   └── auth-fixtures.ts
│   │   │   └── wallet-linking.spec.ts
│   │   ├── fixtures/
│   │   │   ├── auth.ts
│   │   │   ├── combined.ts
│   │   │   ├── console-handler.ts
│   │   │   ├── coverage.ts
│   │   │   ├── index.ts
│   │   │   ├── pages/
│   │   │   │   ├── base.page.ts
│   │   │   │   ├── dashboard.page.ts
│   │   │   │   ├── index.ts
│   │   │   │   ├── my-wallets.page.ts
│   │   │   │   ├── payment-transfer.page.ts
│   │   │   │   ├── sign-in.page.ts
│   │   │   │   ├── sign-up.page.ts
│   │   │   │   └── transaction-history.page.ts
│   │   │   ├── performance.ts
│   │   │   ├── reports/
│   │   │   │   ├── junit.sample.xml
│   │   │   │   ├── playwright.sample.json
│   │   │   │   └── vitest.sample.json
│   │   │   ├── seed-admin.json
│   │   │   ├── seed-user.json
│   │   │   ├── session-reuse.ts
│   │   │   ├── test-utils.ts
│   │   │   ├── transactions.ts
│   │   │   └── wallets.ts
│   │   ├── integration/
│   │   │   └── dal/
│   │   │       └── errors.dal.integration.test.ts
│   │   ├── mocks/
│   │   │   ├── handlers.ts
│   │   │   ├── msw/
│   │   │   │   └── server.ts
│   │   │   └── ui/
│   │   │       └── select.tsx
│   │   ├── setup.ts
│   │   ├── unit/
│   │   │   ├── actions/
│   │   │   │   └── dwolla.actions.test.ts
│   │   │   ├── admin-dashboard-server-wrapper.test.tsx
│   │   │   ├── admin-dashboard.layout.test.tsx
│   │   │   ├── admin.actions.test.ts
│   │   │   ├── auth-form.layout.test.tsx
│   │   │   ├── AuthForm.props.test.tsx
│   │   │   ├── AuthForm.test.tsx
│   │   │   ├── card.test.tsx
│   │   │   ├── components/
│   │   │   │   └── settings-content.test.tsx
│   │   │   ├── cta-get-started.test.tsx
│   │   │   ├── currency-precision.test.ts
│   │   │   ├── dal/
│   │   │   │   ├── admin.dal.test.ts
│   │   │   │   ├── dwolla.dal.test.ts
│   │   │   │   ├── errors.dal.test.ts
│   │   │   │   ├── recipient.dal.test.ts
│   │   │   │   ├── transaction.dal.test.ts
│   │   │   │   ├── user.dal.test.ts
│   │   │   │   └── wallet.dal.test.ts
│   │   │   ├── dashboard-client-wrapper.test.tsx
│   │   │   ├── dashboard-client.layout.test.tsx
│   │   │   ├── dashboard-server-wrapper.test.ts
│   │   │   ├── DashboardClientWrapper.props.test.tsx
│   │   │   ├── data-table.test.tsx
│   │   │   ├── dwolla.dal.test.ts
│   │   │   ├── dwolla.test.ts
│   │   │   ├── error-tracking.test.ts
│   │   │   ├── features-grid.test.tsx
│   │   │   ├── form.test.tsx
│   │   │   ├── generate-markdown-catalog-script.test.ts
│   │   │   ├── generic-components.test.tsx
│   │   │   ├── lib/
│   │   │   │   ├── encryption.test.ts
│   │   │   │   ├── utils.test.ts
│   │   │   │   └── validation-utils.test.ts
│   │   │   ├── markdown-catalog.test.ts
│   │   │   ├── mcp-runner.parse.test.ts
│   │   │   ├── mcp-runner.verify.test.ts
│   │   │   ├── MobileNav.test.tsx
│   │   │   ├── my-wallets-client-wrapper.test.tsx
│   │   │   ├── my-wallets-client.layout.test.tsx
│   │   │   ├── my-wallets-server-wrapper.test.ts
│   │   │   ├── payment-transfer-client.layout.test.tsx
│   │   │   ├── payment-transfer-form.test.tsx
│   │   │   ├── payment-transfer-server-wrapper.test.ts
│   │   │   ├── PaymentTransferClientWrapper.props.test.tsx
│   │   │   ├── plaid.test.ts
│   │   │   ├── plan-ensure-comprehensive.test.ts
│   │   │   ├── plan-ensure.match.test.ts
│   │   │   ├── plan-ensure.scoring.test.ts
│   │   │   ├── recipient.actions.test.ts
│   │   │   ├── register.test.ts
│   │   │   ├── report-parser.test.ts
│   │   │   ├── row.test.tsx
│   │   │   ├── settings-client.layout.test.tsx
│   │   │   ├── settings-profile-form.test.tsx
│   │   │   ├── settings-server-wrapper.test.ts
│   │   │   ├── SettingsClientWrapper.props.test.tsx
│   │   │   ├── Sidebar.test.tsx
│   │   │   ├── signin-wrapper.test.ts
│   │   │   ├── stores/
│   │   │   │   ├── filter-store.test.ts
│   │   │   │   ├── toast-store.test.ts
│   │   │   │   ├── transfer-store.test.ts
│   │   │   │   └── ui-store.test.ts
│   │   │   ├── total-balance.test.tsx
│   │   │   ├── TotalBalanceBox.test.tsx
│   │   │   ├── transaction-history-client-wrapper.test.tsx
│   │   │   ├── transaction-history-client.layout.test.tsx
│   │   │   ├── transaction-history-server-wrapper.test.ts
│   │   │   ├── transaction-list.test.tsx
│   │   │   ├── transaction-mapping.test.ts
│   │   │   ├── transaction.actions.db-error.test.ts
│   │   │   ├── transaction.actions.test.ts
│   │   │   ├── transfer-summary.test.tsx
│   │   │   ├── updateProfile.test.ts
│   │   │   ├── user.actions.test.ts
│   │   │   ├── validations/
│   │   │   │   └── transfer.test.ts
│   │   │   ├── wallet-card.test.tsx
│   │   │   ├── wallet.actions.test.ts
│   │   │   └── wallets-overview.test.tsx
│   │   ├── utils/
│   │   │   └── serverWrapperTestUtils.ts
│   │   └── verify-rules/
│   │       └── verify-rules.test.ts
│   └── types/
│       ├── dwolla.ts
│       ├── eslint-plugin-drizzle.d.ts
│       ├── eslint-plugin-jsx-a11y.d.ts
│       ├── eslint-plugin-security.d.ts
│       ├── index.d.ts
│       ├── next-auth.d.ts
│       ├── plaid.ts
│       ├── recipient.ts
│       ├── transaction.ts
│       ├── user.ts
│       └── wallet.ts
├── SUPPORT.md
├── SYSTEM.md
├── technology-stack.md
├── temp-check.ts
├── temp-check2.ts
├── temp-reset.ts
├── templates/
│   └── README.template.md
├── TESTING_GUIDE.md
├── tsconfig.json
├── tsconfig.tsbuildinfo
├── validation-report.md
├── vercel.json
└── vitest.config.ts
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
