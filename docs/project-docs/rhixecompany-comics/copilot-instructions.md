# Copilot Instructions — rhixecompany-comics

- Treat `projects/rhixecompany-comics` as the target of the consolidation work.
- Keep the frontend App Router-first, server-component-first, and metadata-driven.
- Keep backend configuration env-driven; do not hardcode secrets or host-specific values.
- Preserve the `backend/apps/` ownership boundaries:
  - `core` for health / shared API wiring
  - `comics` for catalog and chapter domain logic
  - `users` for auth/profile logic
  - `scraping` for Scrapy and Selenium orchestration
  - `api` for shared API routing and versioning
- Use the source repositories only as reference material; do not edit them as part of this target.
- Prefer small, reversible edits and update docs when behavior changes.
- If adding a new route, update the docs bundle and keep the cross-linking report in sync.
- Keep the frontend landing page minimal until the backend API grows.
- Maintain compatibility with the versions in `backend/requirements.txt` and `frontend/package.json`.
