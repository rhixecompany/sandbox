# rhixecompany-comics
- Keep App Router and server components first; metadata-driven.
- Env-driven backend config; never hardcode secrets/host values.
- Ownership boundaries: `core` health/shared, `comics` catalog/chapters, `users` auth/profile, `scraping` Scrapy/Selenium, `api` routing/versioning.
- Use source repos only as reference; no edits there.
- Prefer small reversible edits; update docs bundle + cross-linking report when behavior changes.
- Keep landing page minimal until backend API grows.
- Stay compatible with `backend/requirements.txt` and `frontend/package.json`.
