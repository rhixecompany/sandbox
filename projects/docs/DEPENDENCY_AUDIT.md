# DEPENDENCY_AUDIT.md

## Scope
14 projects under `C:\Users\Alexa\Desktop\SandBox\projects`

## Findings

### Python
- `Banking/requirements.txt` is binary/garbled and unsuitable for install.
- `Python-projects/requirements.txt`, `profile/requirements.txt`, and `xamehi.tv/requirements.txt` are unpinned/semantic-only.
- `rhixe_scans/requirements.txt` is a Heroku redirect to `requirements/production.txt`; the referenced target is missing.
- `xamehi` has no Python requirements manifest.

### Node/package manager
- `Banking` declares `bun` in `packageManager`.
- `comicwise` uses `pnpm-lock.yaml`.
- 5 projects use `package-lock.json`: `Django-Scrapy-Selenium`, `rhixe_scans`, `selenium_webdriver`, `university-libary-jsm`, `xamehi`.
- No lockfile discovered for `Banking` and `comicwise` save for `Banking/package.json` manager field and `comicwise/pnpm-lock.yaml`.

## Risk Summary
- unreproducible Python installs
- potential CI/deploy breakage from missing requirements path
- mixed JS toolchains increasing onboarding/CI complexity
