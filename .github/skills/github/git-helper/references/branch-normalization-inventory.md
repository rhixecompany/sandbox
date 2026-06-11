# Branch Normalization Inventory — Rhixe-company workspace

Live inventory from 2026-05-29 session. Source branch = branch to rename to `production`.

| Project | Source Branch | Extra branches (pre-cleanup) |
|---------|--------------|------------------------------|
| Banking | main | dev, fix-validation, audit/docs-20260515 |
| comicwise | main | master, feat/mocks-refactor, quality-gate-refactor |
| comicwise_push_clean | (merge into comicwise then delete repo) | — |
| cookiecutter-django-tailwind | main | master |
| Django-Scrapy-Selenium | main | master, main-new, main-next |
| ecom | main | audit/docs-20260515 |
| profile | master | audit/docs-20260515 |
| Python-projects | main | master |
| rhixe_scans | main | audit/docs-20260515, dependabot/docker (x2) |
| selenium_webdriver | main | master, audit/docs-20260515 |
| university-libary-jsm | main | audit/docs-20260515 |
| xamehi | main | — |
| xamehi.tv | main | — |
| youtube-downloader | main | master |

Notes:
- `profile` is the only project where `master` (not `main`) is the canonical source branch.
- Temporary workflow branches (chore/*, audit/*) should be deleted during normalization.
- `comicwise_push_clean` is a diverged clone pointing to the same remote as `comicwise`; merge unique assets, then delete the local directory.
