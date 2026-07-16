# rhixe_scans - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\rhixe_scans`
**Generated:** 2026-07-10
**Stack:** Next.js

## Directory Tree

```
rhixe_scans/
├── .editorconfig
├── .github/
│   ├── copilot-instructions.md
│   ├── dependabot.yml
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── contrib/
│   │   │   ├── __init__.py
│   │   │   └── sites/
│   │   │       ├── __init__.py
│   │   │       └── migrations/
│   │   ├── home/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── context_processors.py
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── libary/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── constants.py
│   │   │   ├── data_helper.py
│   │   │   ├── decorators.py
│   │   │   ├── filters.py
│   │   │   ├── forms.py
│   │   │   ├── forms_helpers.py
│   │   │   ├── managers.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── 0002_initial.py
│   │   │   │   ├── 0003_alter_comic_user.py
│   │   │   │   ├── 0004_alter_comic_artist_alter_comic_author_and_more.py
│   │   │   │   ├── 0005_alter_chapter_updated_at_alter_comic_updated_at.py
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── pagination.py
│   │   │   ├── serializers.py
│   │   │   ├── signals.py
│   │   │   ├── signals_helpers.py
│   │   │   ├── tables.py
│   │   │   ├── templatetags/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── example.py
│   │   │   │   └── format_json.py
│   │   │   ├── tests.py
│   │   │   ├── urls/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── artist_urls.py
│   │   │   │   ├── author_urls.py
│   │   │   │   ├── category_urls.py
│   │   │   │   ├── chapter_image_urls.py
│   │   │   │   ├── chapter_urls.py
│   │   │   │   ├── comic_image_urls.py
│   │   │   │   ├── comic_urls.py
│   │   │   │   ├── genre_urls.py
│   │   │   │   └── user_urls.py
│   │   │   └── views/
│   │   │       ├── __init__.py
│   │   │       ├── artist_views.py
│   │   │       ├── author_views.py
│   │   │       ├── category_views.py
│   │   │       ├── chapter_image_views.py
│   │   │       ├── chapter_views.py
│   │   │       ├── comic_image_views.py
│   │   │       ├── comic_views copy.py
│   │   │       ├── comic_views.py
│   │   │       ├── comment_views.py
│   │   │       ├── genre_views.py
│   │   │       └── user_views.py
│   │   ├── templates/
│   │   │   ├── 403.html
│   │   │   ├── 403_csrf.html
│   │   │   ├── 404.html
│   │   │   ├── 500.html
│   │   │   ├── account/
│   │   │   │   ├── account_inactive.html
│   │   │   │   ├── base_confirm_code.html
│   │   │   │   ├── base_entrance.html
│   │   │   │   ├── base_manage.html
│   │   │   │   ├── base_manage_email.html
│   │   │   │   ├── base_manage_password.html
│   │   │   │   ├── base_manage_phone.html
│   │   │   │   ├── base_reauthenticate.html
│   │   │   │   ├── confirm_email_verification_code.html
│   │   │   │   ├── confirm_login_code.html
│   │   │   │   ├── confirm_password_reset_code.html
│   │   │   │   ├── confirm_phone_verification_code.html
│   │   │   │   ├── email/
│   │   │   │   ├── email.html
│   │   │   │   ├── email_change.html
│   │   │   │   ├── email_confirm.html
│   │   │   │   ├── login copy.html
│   │   │   │   ├── login.html
│   │   │   │   ├── logout.html
│   │   │   │   ├── messages/
│   │   │   │   ├── password_change.html
│   │   │   │   ├── password_reset.html
│   │   │   │   ├── password_reset_done.html
│   │   │   │   ├── password_reset_from_key.html
│   │   │   │   ├── password_reset_from_key_done.html
│   │   │   │   ├── password_set.html
│   │   │   │   ├── phone_change.html
│   │   │   │   ├── reauthenticate.html
│   │   │   │   ├── request_login_code.html
│   │   │   │   ├── signup copy.html
│   │   │   │   ├── signup.html
│   │   │   │   ├── signup_by_passkey.html
│   │   │   │   ├── signup_closed.html
│   │   │   │   ├── snippets/
│   │   │   │   ├── verification_sent.html
│   │   │   │   └── verified_email_required.html
│   │   │   ├── allauth/
│   │   │   │   ├── elements/
│   │   │   │   └── layouts/
│   │   │   ├── base.html
│   │   │   ├── data_table/
│   │   │   │   ├── 404.html
│   │   │   │   ├── base.html
│   │   │   │   └── index.html
│   │   │   ├── error.html
│   │   │   ├── home/
│   │   │   │   ├── base.html
│   │   │   │   ├── bookmarks.html
│   │   │   │   ├── dmca.html
│   │   │   │   ├── index.html
│   │   │   │   ├── privacy.html
│   │   │   │   ├── series.html
│   │   │   │   └── terms.html
│   │   │   ├── libary/
│   │   │   │   ├── chapterimages/
│   │   │   │   ├── chapters/
│   │   │   │   ├── comicimages/
│   │   │   │   └── comics/
│   │   │   ├── partials/
│   │   │   │   ├── base/
│   │   │   │   ├── bookmarks/
│   │   │   │   ├── chapter/
│   │   │   │   ├── chapterimages/
│   │   │   │   ├── chapters/
│   │   │   │   ├── comic/
│   │   │   │   ├── comicimages/
│   │   │   │   ├── comics/
│   │   │   │   ├── index/
│   │   │   │   ├── series/
│   │   │   │   └── widgets/
│   │   │   └── users/
│   │   │       ├── base.html
│   │   │       ├── user_detail.html
│   │   │       ├── user_form copy.html
│   │   │       └── user_form.html
│   │   └── users/
│   │       ├── __init__.py
│   │       ├── adapters.py
│   │       ├── admin.py
│   │       ├── admin_helpers.py
│   │       ├── apps.py
│   │       ├── context_processors.py
│   │       ├── forms.py
│   │       ├── managers.py
│   │       ├── migrations/
│   │       │   ├── 0001_initial.py
│   │       │   └── __init__.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── signals.py
│   │       ├── signals_helpers.py
│   │       └── tests/
│   │           ├── __init__.py
│   │           ├── factories.py
│   │           ├── test_admin.py
│   │           ├── test_forms.py
│   │           ├── test_managers.py
│   │           ├── test_models.py
│   │           ├── test_tasks.py
│   │           ├── test_urls.py
│   │           └── test_views.py
│   ├── artist.json
│   ├── author.json
│   ├── category.json
│   ├── chapter.json
│   ├── chapterimage.json
│   ├── chaptersdata1.json
│   ├── chaptersdata2.json
│   ├── comic.json
│   ├── comicimage.json
│   ├── comicsdata1.json
│   ├── comicsdata2.json
│   ├── config/
│   │   ├── __init__.py
│   │   ├── celery_app.py
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── local.py
│   │   │   ├── production.py
│   │   │   └── test.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── myhandler.py
│   │   │   └── play/
│   │   │       ├── __init__.py
│   │   │       ├── _utils.py
│   │   │       ├── handler.py
│   │   │       ├── headers.py
│   │   │       ├── memusage.py
│   │   │       └── page.py
│   │   ├── items.py
│   │   ├── main.py
│   │   ├── management/
│   │   │   ├── __init__.py
│   │   │   └── commands/
│   │   │       ├── __init__.py
│   │   │       ├── crawl copy.py
│   │   │       ├── crawl.py
│   │   │       ├── crawls.py
│   │   │       ├── generate.py
│   │   │       ├── loadall.py
│   │   │       ├── loadcsv.py
│   │   │       ├── loadjson.py
│   │   │       ├── loadone.py
│   │   │       ├── read.py
│   │   │       └── runcrawls.py
│   │   ├── middlewares/
│   │   │   ├── __init__.py
│   │   │   ├── default.py
│   │   │   ├── main copy 2.py
│   │   │   ├── main copy.py
│   │   │   ├── main.py
│   │   │   ├── main1.py
│   │   │   ├── mymain.py
│   │   │   ├── retry.py
│   │   │   └── rotate.py
│   │   ├── models.py
│   │   ├── pipelines/
│   │   │   ├── __init__.py
│   │   │   ├── db.py
│   │   │   ├── default.py
│   │   │   ├── download.py
│   │   │   ├── download_images.py
│   │   │   └── redis/
│   │   │       ├── __init__.py
│   │   │       ├── connection.py
│   │   │       ├── defaults.py
│   │   │       └── red.py
│   │   ├── settings.py
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   ├── asuracomic.py
│   │   │   ├── asuracomic1.py
│   │   │   ├── asuracomic2.py
│   │   │   ├── comic.py
│   │   │   ├── comick.py
│   │   │   ├── comick1.py
│   │   │   └── qoutes.py
│   │   └── tasks.py
│   ├── downloader/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── management/
│   │       ├── __init__.py
│   │       └── commands/
│   │           ├── __init__.py
│   │           └── download.py
│   ├── fixtures/
│   │   └── db.json
│   ├── genre.json
│   ├── locale/
│   │   ├── en/
│   │   │   └── LC_MESSAGES/
│   │   │       └── django.po
│   │   ├── fr/
│   │   │   └── LC_MESSAGES/
│   │   │       └── django.po
│   │   ├── ja/
│   │   │   └── LC_MESSAGES/
│   │   │       └── django.po
│   │   ├── pt/
│   │   │   └── LC_MESSAGES/
│   │   │       └── django.po
│   │   └── README.md
│   ├── logs.txt
│   ├── manage.py
│   ├── scrapy.cfg
│   └── superbase.py
├── bash/
│   ├── docker-clean.sh
│   ├── git-setup.sh
│   ├── install_chrome.sh
│   ├── install_firefox.sh
│   ├── prod-dev.sh
│   ├── prod.sh
│   └── setup.sh
├── bun.lock
├── CHANGELOG.md
├── code-exemplars.md
├── components.json
├── compose/
│   └── production/
│       ├── aws/
│       │   ├── Dockerfile
│       │   └── maintenance/
│       │       ├── download
│       │       └── upload
│       ├── django/
│       │   ├── celery/
│       │   │   ├── beat/
│       │   │   ├── flower/
│       │   │   └── worker/
│       │   ├── Dockerfile
│       │   ├── entrypoint
│       │   └── start
│       ├── postgres/
│       │   ├── Dockerfile
│       │   └── maintenance/
│       │       ├── _sourced/
│       │       ├── backup
│       │       ├── backups
│       │       ├── restore
│       │       └── rmbackup
│       ├── redis/
│       │   ├── Dockerfile
│       │   ├── redis.conf
│       │   └── start.sh
│       ├── redis-slave/
│       │   ├── Dockerfile
│       │   ├── redis.conf
│       │   └── start.sh
│       └── traefik/
│           ├── Dockerfile
│           └── traefik.yml
├── CONTRIBUTING.md
├── CONTRIBUTORS.txt
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── docker-compose.docs.yml
├── docker-compose.local.yml
├── docker-compose.production.yml
├── docs/
│   ├── __init__.py
│   ├── ARCHITECTURE.md
│   ├── code-docs/
│   │   └── index.md
│   ├── code-docs.md
│   ├── conf.py
│   ├── CONTRIBUTING.md
│   ├── DEVELOPER_GUIDE.md
│   ├── howto.rst
│   ├── index.rst
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── rhixe_scans-docs.docx
│   ├── USER_GUIDE.md
│   └── users.rst
├── eslint.config.mjs
├── execution-summary.md
├── folder-structure.md
├── jest.config.ts
├── jest.setup.ts
├── justfile
├── LICENSE
├── merge_production_dotenvs_in_dotenv.py
├── next.config.ts
├── package.json
├── postcss.config.mjs
├── Procfile
├── project-workflow.md
├── pyproject.toml
├── README.md
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── requirements.txt
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── src/
│   ├── app/
│   │   ├── (auth)/
│   │   │   ├── logout/
│   │   │   │   └── page.tsx
│   │   │   ├── sign-in/
│   │   │   │   └── page.tsx
│   │   │   └── sign-up/
│   │   │       └── page.tsx
│   │   ├── (root)/
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── admin/
│   │   │   ├── layout.tsx
│   │   │   ├── main-nav.tsx
│   │   │   └── page.tsx
│   │   ├── api/
│   │   │   └── auth/
│   │   │       └── [...nextauth]/
│   │   ├── dashboard/
│   │   │   ├── data.json
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── loading.tsx
│   │   └── not-found.tsx
│   ├── assets/
│   │   ├── loader.gif
│   │   ├── logo.png
│   │   ├── profile-picture.webp
│   │   └── styles/
│   │       └── globals.css
│   ├── auth.config.ts
│   ├── auth.ts
│   ├── components/
│   │   ├── admin/
│   │   │   └── admin-search.tsx
│   │   ├── app-sidebar.tsx
│   │   ├── auth/
│   │   │   ├── credentials-signin-form.tsx
│   │   │   ├── custom-sign-in.tsx
│   │   │   ├── login-form.tsx
│   │   │   ├── sign-up-form.tsx
│   │   │   └── signup-form.tsx
│   │   ├── chart-area-interactive.tsx
│   │   ├── custom-sign-in.tsx
│   │   ├── data-table.tsx
│   │   ├── footer.tsx
│   │   ├── github-sign-in.tsx
│   │   ├── nav-documents.tsx
│   │   ├── nav-main.tsx
│   │   ├── nav-projects.tsx
│   │   ├── nav-secondary.tsx
│   │   ├── nav-user.tsx
│   │   ├── section-cards.tsx
│   │   ├── shared/
│   │   │   ├── delete-dialog.tsx
│   │   │   ├── header/
│   │   │   │   ├── header-menu.tsx
│   │   │   │   ├── header-nav.tsx
│   │   │   │   ├── index.tsx
│   │   │   │   ├── menu.tsx
│   │   │   │   ├── mode-toggle.tsx
│   │   │   │   ├── search-mobile.tsx
│   │   │   │   ├── search.tsx
│   │   │   │   ├── sign-out.tsx
│   │   │   │   ├── user-button.tsx
│   │   │   │   └── user-menu-button.tsx
│   │   │   └── pagination.tsx
│   │   ├── sign-out.tsx
│   │   ├── site-header.tsx
│   │   ├── team-switcher.tsx
│   │   └── ui/
│   │       ├── accordion.tsx
│   │       ├── alert-dialog.tsx
│   │       ├── apple.tsx
│   │       ├── avatar.tsx
│   │       ├── badge.tsx
│   │       ├── breadcrumb.tsx
│   │       ├── button.tsx
│   │       ├── card.tsx
│   │       ├── carousel.tsx
│   │       ├── chart.tsx
│   │       ├── checkbox.tsx
│   │       ├── collapsible.tsx
│   │       ├── command.tsx
│   │       ├── dialog.tsx
│   │       ├── drawer.tsx
│   │       ├── dropdown-menu.tsx
│   │       ├── form.tsx
│   │       ├── github.tsx
│   │       ├── google.tsx
│   │       ├── input.tsx
│   │       ├── label.tsx
│   │       ├── pagination.tsx
│   │       ├── radio-group.tsx
│   │       ├── select.tsx
│   │       ├── separator.tsx
│   │       ├── sheet.tsx
│   │       ├── sidebar.tsx
│   │       ├── skeleton.tsx
│   │       ├── sonner.tsx
│   │       ├── table.tsx
│   │       ├── tabs.tsx
│   │       ├── textarea.tsx
│   │       ├── toast.tsx
│   │       ├── toaster.tsx
│   │       ├── toggle-group.tsx
│   │       ├── toggle.tsx
│   │       └── tooltip.tsx
│   ├── db/
│   │   ├── migrations/
│   │   │   ├── 20250618170353_init/
│   │   │   │   └── migration.sql
│   │   │   └── migration_lock.toml
│   │   └── schema.prisma
│   ├── hooks/
│   │   ├── use-mobile.tsx
│   │   └── use-toast.ts
│   ├── lib/
│   │   ├── actions/
│   │   │   ├── bookmark.actions.ts
│   │   │   ├── chapter.actions.ts
│   │   │   ├── comic.actions.ts
│   │   │   └── user.actions.ts
│   │   ├── constants/
│   │   │   └── index.ts
│   │   ├── data/
│   │   │   ├── artist.ts
│   │   │   ├── author.ts
│   │   │   ├── category.ts
│   │   │   ├── chapter.ts
│   │   │   ├── chapterimage.ts
│   │   │   ├── comic.ts
│   │   │   ├── comicimage.ts
│   │   │   ├── genre.ts
│   │   │   └── user.ts
│   │   ├── db.ts
│   │   ├── executeAction.ts
│   │   ├── prisma.ts
│   │   ├── sample-data.ts
│   │   ├── schema.ts
│   │   ├── seed.ts
│   │   ├── utils.ts
│   │   └── validators.ts
│   ├── middleware.ts
│   └── types/
│       ├── analytics.ts
│       ├── index.ts
│       └── next-auth.d.ts
├── tailwind.config.ts
├── technology-stack.md
├── TESTING_GUIDE.md
├── tests/
│   ├── __init__.py
│   ├── paypal.test.ts
│   ├── test_merge_production_dotenvs_in_dotenv.py
│   ├── test_nodriver.py
│   ├── test_nodriverinfmul.py
│   ├── test_nodrivermul.py
│   ├── test_selenium.py
│   ├── test_selenium1.py
│   ├── test_selenium_driveless.py
│   └── test_selenium_driveless_async.py
├── tsconfig.json
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
