# Per-Repo Implementation Plans

> Generated: 2026-05-30 | Refreshed: live scan (ignore files, branch state, dirtiness)
> **Note:** All 14 repos except comicwise are normalized to production/development (default=production) on origin.

---

## xamehi (Django DRF + Express.js + React 18)

**Status:** Normalized (production/development branches, default=production). **1 untracked file** (AGENTS.md).

**Ignore Files:** Only `.gitignore` exists. Missing `__pycache__/`, `*.pyc`, `.venv/`, `db.sqlite3`, `staticfiles/`. `.env.example` exists but `.env` is in `.gitignore`.

**Tech Actions:**
1. Add `__pycache__/`, `*.pyc`, `.venv/`, `db.sqlite3` to `.gitignore` (currently only has Node.js patterns)
2. Define API boundary between Express (auth proxy) and Django (business logic) — currently overlapping
3. Split `requirements.txt` from `package.json` deps — clarify which backend owns what
4. Add `.prettierignore` if Prettier configured (check for .prettierrc)
5. Consider dual-backend consolidation or clear separation documentation
6. Stage + commit or ignore AGENTS.md

**Priority:** Medium

---

## xamehi.tv (Django DRF + React 17, MUI, Redux)

**Status:** Normalized (production/development branches, default=production). No push issues.

**Ignore Files:** Only `.gitignore` exists in root. Frontend has separate `.gitignore`. Missing `.dockerignore`, `.prettierignore`, `.eslintignore`.

**Tech Actions:**
1. Assess React 17 → 18 upgrade path (MUI v4 compatibility, breaking changes in React 18)
2. Add `.dockerignore` if Docker is used (check for Dockerfile)
3. Add `.prettierignore` if Prettier configured
4. Add `.eslintignore` if ESLint configured
5. Verify Django settings for production deployment

**Priority:** Medium

---

## youtube-downloader (Python CLI, yt-dlp, curl_cffi)

**Status:** Normalized (production/development branches, default=production). No push issues.

**Ignore Files:** Only `.gitignore` exists (auto-generated Python template). Covers `__pycache__/`, `.env`, `*.pyc`, `build/`. Missing `.dockerignore`, `.prettierignore`.

**Tech Actions:**
1. Verify yt-dlp and curl_cffi compatibility with latest versions
2. Check if `downloads/` or output directories exist — ensure they're in `.gitignore`
3. Add `.prettierignore` if Prettier configured for Python files
4. No Docker needed unless containerization is planned
5. Standalone tool — maintain as-is

**Priority:** Low

---

## python-projects (18 standalone Python scripts)

**Status:** Normalized (production/development branches, default=production). No push issues.

**Ignore Files:** Only `.gitignore` exists. Covers Python essentials.

**Tech Actions:**
1. Verify ruff + mypy configuration exists
2. Assess modernization needs (Python 3.11+ compatibility)
3. Add `.prettierignore` if Prettier configured
4. Standalone collection — maintain as-is

**Priority:** Low

---

## cookiecutter-django-tailwind (Django 5 template)

**Status:** Normalized (production/development branches, default=production). **1 modified file** (AGENTS.md — unstaged).

**Ignore Files:** `.gitignore` + `.dockerignore` present. Template also has nested `{{cookiecutter.project_slug}}/.gitignore` and `{{cookiecutter.project_slug}}/.dockerignore`. Missing `.prettierignore`.

**Tech Actions:**
1. Verify cookiecutter template structure and post-generation hooks
2. Update for Django 5.x compatibility
3. Stage + commit AGENTS.md modification

**Priority:** Low

---

## ecom (Django 3.1 DRF + React 18)

**Status:** Normalized (production/development branches, default=production). No push issues.

**Ignore Files:** Only `.gitignore` exists. Missing `.dockerignore`, `.prettierignore`, `.eslintignore`.

**Tech Actions:**
1. **HIGH PRIORITY:** Assess Django 3.1 → 5.x upgrade path. Django 3.1 is EOL with known CVEs.
2. Add `.dockerignore` if Docker is used
3. Add `.prettierignore` if Prettier configured
4. Add `.eslintignore` if ESLint configured
5. Plan phased migration: 3.1 → 4.2 LTS → 5.x

**Priority:** HIGH (security risk — Django 3.1 EOL)

---

## selenium_webdriver (Node.js 18+ selenium-webdriver)

**Status:** Normalized (production/development branches, default=production). **1 untracked file** (AGENTS.md).

**Ignore Files:** `.gitignore`, `.dockerignore`, `.prettierignore`, `.eslintignore` all present. Good coverage but each is thin — mostly just `node_modules`.

**Tech Actions:**
1. Expand ignore coverage beyond `node_modules` if browser/runtime artifacts exist
2. Stage + commit AGENTS.md
3. Consolidation source for rhixecompany-comics — ongoing maintenance only

---

## profile (Django 3, CKEditor, GCS)

**Status:** Normalized (production/development branches, default=production). Remote is `rhixecompany/rhixecompany.git` (not `profile.git`).

**Ignore Files:** `.gitignore` + `.gcloudignore` present. Missing `.dockerignore`, `.prettierignore`, `.eslintignore`.

**Tech Actions:**
1. Clarify remote naming — `rhixecompany/rhixecompany.git` vs renaming to `profile` or keeping as-is
2. Add `.dockerignore` (exclude CKEditor uploads, media, GCS credentials)
3. Add `.prettierignore` for migration files
4. Add `.eslintignore` if any front-end linting exists
5. Verify GCS credentials are not tracked in version control

**Priority:** Low
