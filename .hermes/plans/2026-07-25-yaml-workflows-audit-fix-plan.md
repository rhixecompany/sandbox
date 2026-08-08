---
status: completed
---

# YAML / Workflow Audit & Fix Plan

**Date:** 2026-07-25
**Goal:** Debug, fix all issues/warnings/errors, enhance, and validate all `.yml/.yaml` files across the workspace.
**Scope:** `.github/workflows/*.yml` (33), `projects/**/*.yml` (29), `projects/**/*.yaml` (8) = **70 files total**

---

## Spec: File Categories

| Category                                | Count   | File Types                                                             | Validation Rules                                                |
| --------------------------------------- | ------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- |
| **A — Root GitHub Actions workflows**   | 34      | `.github/workflows/*.yml`                                              | LF line endings, trailing newline, no trailing spaces, yamllint |
| **B — Sub-project workflows & configs** | 63      | `projects/**/*.yml` (inc. `.github/workflows/*`, docker-compose, etc.) | LF line endings, no trailing spaces, yamllint                   |
| **C — Sub-project .yaml configs**       | 13      | `projects/**/*.yaml` (pre-commit, deploy configs, etc.)                | LF line endings, yamllint                                       |
| **Total**                               | **110** |                                                                        |                                                                 |

---

## Phase 1: Setup Tooling

**Task 1.1** — Create `.yamllint.yaml` workspace-wide config

- Relaxed line-length (120 chars for GHA, 200 for lock files)
- Enforce LF newlines, trailing newlines, no trailing spaces
- Exclude cookiecutter Jinja templates (`projects/cookiecutter-django-tailwind/**`)

**Task 1.2** — Create `.gitattributes` for line-ending normalization

- `*.yml text eol=lf`
- `*.yaml text eol=lf`

**Task 1.3** — Create reusable validation script

- `scripts/validate-yaml.sh` — runs yamllint on all YAML files, returns exit code

---

## Phase 2: Fix `.github/workflows/*.yml` (33 files)

**Issues detected:**

- 6 files with CRLF line endings → convert to LF
- 16 files missing trailing newline → append `\n`
- 1 file with trailing spaces → strip
- Widespread line-length warnings (expected for GHA shell blocks)

**Task 2.1** — Fix CRLF → LF:

- `bash-scripts-ci.yml`
- `copilot-setup-steps.yml`
- `deploy-website.yml`
- `resource-staleness-report.lock.yml`
- `resume-maker-ci.yml`
- `validate-readme.yml`

**Task 2.2** — Add trailing newlines to files missing EOF `\n`:

- `banking-ci.yml`, `comicwise-ci.yml`, `django-scrapy-selenium-ci.yml`, `ecom-ci.yml`
- `mcp-servers-ci.yml`, `profile-ci.yml`, `python-ci.yml`, `python-projects-ci.yml`
- `resource-staleness-report.lock.yml`, `resume-maker-ci.yml`, `rhixe_scans-ci.yml`
- `rhixe-scans-ci.yml`, `rhixecompany-comics-ci.yml`, `selenium-webdriver-ci.yml`
- `university-libary-jsm-ci.yml`, `xamehi-ci.yml`, `xamehi-tv-ci.yml`, `youtube-downloader-ci.yml`

**Task 2.3** — Strip trailing spaces:

- `resource-staleness-report.lock.yml`

**Task 2.4** — Validate all 33 files pass yamllint clean

---

## Phase 3: Fix `projects/**/*.yml` (29 files)

**Issues detected:**

- CRLF in docker-compose files
- Trailing spaces in some Docker-Scrapy-Selenium/rhixe_scans compose files

**Task 3.1** — Fix CRLF → LF:

- `projects/comicwise/docker-compose.yml`
- `projects/Django-Scrapy-Selenium/docker-compose.docs.yml`
- `projects/Django-Scrapy-Selenium/docker-compose.local.yml`
- `projects/Django-Scrapy-Selenium/docker-compose.production.yml`
- `projects/rhixe_scans/docker-compose.docs.yml`
- `projects/rhixe_scans/docker-compose.local.yml`
- `projects/rhixe_scans/docker-compose.production.yml`
- `projects/rhixecompany-comics/docker-compose.yml`

**Task 3.2** — Strip trailing spaces:

- `projects/Django-Scrapy-Selenium/docker-compose.local.yml`
- `projects/Django-Scrapy-Selenium/docker-compose.production.yml`
- `projects/rhixe_scans/docker-compose.production.yml`

**Task 3.3** — Validate all 29 files pass yamllint clean

---

## Phase 4: Fix `projects/**/*.yaml` (8 files)

**Issues detected:**

- CRLF in several files
- Line-length warnings

**Task 4.1** — Fix CRLF → LF:

- `projects/comicwise/pnpm-workspace.yaml`
- `projects/profile/migrate.yaml`

**Task 4.2** — Validate all 8 files pass yamllint clean

---

## Phase 5: Enhance — Add CI Validation

**Task 5.1** — Create reusable validation script `scripts/validate-yaml.sh`

- Runs `yamllint` across all YAML files
- Excludes cookiecutter Jinja templates
- Returns detailed error report

**Task 5.2** — Create `.github/workflows/yaml-validation.yml`

- Runs on push/PR to `development`, `staged`
- Installs yamllint, runs validation
- Fails on yamllint errors

**Task 5.3** — Update `check-line-endings.yml` to also check `.yml`/`.yaml` files (currently only `.md`)

---

## Phase 6: Final Verification

**Task 6.1** — Run full yamllint sweep across all 70 files
**Task 6.2** — Verify yamllint returns exit code 0
**Task 6.3** — Report summary of fixes applied

---

## Acceptance Criteria

- [ ] All 110 YAML files pass `yamllint -c .yamllint.yaml` with 0 errors
- [ ] All files use LF line endings (verified by `.gitattributes`)
- [ ] No trailing spaces in any YAML file
- [ ] All files end with `\n`
- [ ] CI workflow validates YAML on push/PR
- [ ] Reusable validation script exists at `scripts/validate-yaml.sh`
- [ ] `.yamllint.yaml` config handles auto-generated lock files (max: 400)
