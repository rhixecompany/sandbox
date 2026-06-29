# RESEARCH_REPORT.md

<!-- Template version: 1.0.0 — maintained by repo-research-pipeline skill -->
<!-- Required sections: 10 (do not add or remove top-level ##). -->
<!-- Size gate: 1KB minimum, 5KB maximum. -->
<!-- Every finding must trace to a real web_search result. -->

## Project: cookiecutter-django-tailwind

**Type:** Django project template / Cookiecutter generator
**Tech Stack:** Django 5.x, django-tailwind, PostgreSQL, Docker, Celery, pytest, pre-commit, Black, ruff, mypy, djlint
**Status:** Active

---

## Similar Projects

| Project             | URL                                                   | Why Relevant                                                                                   |
| ------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| django-cookiecutter | <https://github.com/cookiecutter/cookiecutter-django> | Reference — the most starred Django project template; this project is a Tailwind-specific fork |
| django-tailwind-cli | <https://pypi.org/project/django-tailwind-cli>        | Standalone Tailwind CSS CLI integration for Django (2026 update)                               |

---

## Key Findings

### Django 5.x Project Structure

- Layered settings pattern (`base.py` → `local.py` → `production.py`) is the industry standard for 2026; never use a single `settings.py` in production (dev.to, 2026)
- Twelve-Factor App methodology is the guiding principle — config from environment, strict separation of build/release/run (dev.to)
- Cookiecutter-Django remains the top-referenced project template structure; this project extends it with Tailwind-specific frontend tooling (Reddit r/django)

### django-tailwind Integration

- `django-tailwind-cli` (May 2026) now provides standalone Tailwind CSS binary integration, eliminating npm as a build dependency (PyPI)
- django-tailwind v2.0 recommends `python manage.py tailwind start` for development and `honcho` for running Django + Tailwind servers concurrently (django-tailwind.readthedocs.io)
- Tailwind utility-first CSS approach pairs naturally with Django templates — minimal custom CSS, HTML class composition (project README)

### Production Security Hardening

- `python manage.py check --deploy` must run before every production deployment — audits HTTPS enforcement, cookie flags, secret key strength (softaims.com, 2026)
- Content Security Policy (CSP) via `django-csp` with REPORT_ONLY mode first is the recommended XSS prevention approach (softaims.com)
- Django 6.0 deployment checklist mandates HSTS, secure cookie flags, DEBUG=False, and proper ALLOWED_HOSTS (docs.djangoproject.com)

---

## Cheatsheets & Quick Reference

| Topic                        | Resource                                                             | Type      |
| ---------------------------- | -------------------------------------------------------------------- | --------- |
| Django 5.x settings layering | <https://docs.djangoproject.com/en/5.2/topics/settings/>             | Docs      |
| django-tailwind CLI          | <https://django-tailwind.readthedocs.io/en/latest/installation.html> | Guide     |
| Django deploy checklist      | <https://docs.djangoproject.com/en/6.0/howto/deployment/checklist>   | Checklist |

---

## Best Practices

1. **Settings layering** — Split settings into base/local/production with django-environ for secrets; never commit `.env`
2. **pre-commit hooks** — Enforce Black, ruff, mypy, djlint before every commit to catch issues early
3. **Docker Compose** — Use `docker compose -f production.yml` for reproducible production deployments
4. **Sentry monitoring** — Integrate Sentry SDK for error tracking in production from day one
5. **Type hints** — Require type hints in all new Django code for mypy validation in CI

---

## Common Pitfalls

| Pitfall                           | Impact                        | Avoidance                                   |
| --------------------------------- | ----------------------------- | ------------------------------------------- |
| Single settings.py                | Security leaks, env confusion | Use 3-tier settings (base/local/production) |
| django-tailwind npm version drift | Broken Tailwind builds        | Use `django-tailwind-cli` standalone binary |
| Missing `check --deploy`          | Production config regressions | Run `check --deploy` in CI/deploy pipeline  |
| No CSP headers                    | XSS vulnerabilities           | Add django-csp with REPORT_ONLY first       |

---

## Performance

1. **django-tailwind standalone CLI** — Eliminates node_modules overhead; faster build times than npm-based setup
2. **WhiteNoise with cache headers** — Serve static files efficiently with far-future Cache-Control headers
3. **PostgreSQL connection pooling** — Use pgbouncer or Django's CONN_MAX_AGE for persistent connections
4. **Gunicorn workers** — Set workers to 2–4 × CPU cores for optimal throughput

---

## Security

1. **CSRF + XSS** — Django's built-in CSRF and XSS escaping are strong by default; enforce CSP via django-csp
2. **Secret management** — django-environ with `.env` never committed; SECRET_KEY rotated regularly
3. **Production checklist** — `manage.py check --deploy` catches 90% of common misconfigurations
4. **HSTS** — Force HTTPS with Strict-Transport-Security header in production

---

## Related Projects (in workspace)

- **ecom** — Also uses DRF + layered Django settings pattern
- **profile** — Django monolith with similar settings layering; media storage on GCS

---

## Resources

| Resource            | URL                                                   | Description                         |
| ------------------- | ----------------------------------------------------- | ----------------------------------- |
| Official Docs       | <https://docs.djangoproject.com/en/5.2/>              | Django 5.x official documentation   |
| django-tailwind     | <https://django-tailwind.readthedocs.io/>             | Tailwind CSS integration for Django |
| Cookiecutter Django | <https://github.com/cookiecutter/cookiecutter-django> | Reference Django project template   |
| Community           | <https://www.reddit.com/r/django/>                    | Django community discussions        |

---

## Project: Django-Scrapy-Selenium

**Type:** Django-based web scraping platform
**Tech Stack:** Django 4.x, DRF, Scrapy, Selenium, BeautifulSoup4, Celery + Redis/RabbitMQ, PostgreSQL
**Status:** Active (legacy — scraping consolidated to rhixecompany-comics)

---

## Similar Projects

| Project                                                | URL                                                                         | Why Relevant                                   |
| ------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------------------------------------- |
| codingforentrepreneurs/Web-Scraping-with-Django-Celery | <https://github.com/codingforentrepreneurs/Web-Scraping-with-Django-Celery> | Reference — Django + Celery scraping scheduler |
| scrapingbee/selenium-python                            | <https://www.scrapingbee.com/blog/selenium-python>                          | Modern Selenium scraping guide (2026)          |

---

## Key Findings

### Scrapy + Django Integration

- Scrapy spiders work best as standalone components called from Celery tasks, not tightly coupled to Django views (medium.com/@yasykur_rafii)
- Django ORM can be used inside Scrapy pipelines for direct data persistence without intermediate files
- Celery beat schedules periodic scraping runs; `django-celery-beat` provides DB-backed periodic task management (oneuptime.com, 2026)

### Selenium Anti-Detection

- Selenium's `navigator.webdriver` flag is the primary detection vector — use `SeleniumBase` or `undetected-chromedriver` to bypass (scrapfly.io, 2026)
- Camoufox (Firefox-based stealth browser) and `playwright-stealth` are the top Python anti-detection tools in 2026 (scrapfly.io)
- Headless mode is increasingly detected; using headed mode or headful disguises reduces blocking (scrapingbee.com, 2026)

### Celery Monitoring

- Redis is the fastest and most common Celery broker; RabbitMQ offers stronger durability guarantees (oneuptime.com, 2026)
- `django-celery-results` stores task results in the database for inspection via Django Admin
- Flower (real-time Celery monitor) is the recommended dashboard for worker/task monitoring in production

---

## Cheatsheets & Quick Reference

| Topic                | Resource                                                                     | Type     |
| -------------------- | ---------------------------------------------------------------------------- | -------- |
| Celery + Django      | <https://oneuptime.com/blog/post/2026-01-26-django-celery-background-tasks/> | Guide    |
| Selenium scraping    | <https://www.scrapingbee.com/blog/selenium-python>                           | Tutorial |
| Anti-detection tools | <https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools>                  | Guide    |

---

## Best Practices

1. **Robots.txt compliance** — Check and respect `robots.txt` before spidering any site
2. **Rate limiting** — Add `DOWNLOAD_DELAY` and `AUTO_THROTTLE` in Scrapy settings; user-agent rotation mandatory
3. **Data sanitization** — Clean scraped data before persistence to prevent XSS in dashboards
4. **Separate concerns** — Scrapy spiders in `crawler/spiders/`, Celery tasks in `tasks.py`, views in separate apps

---

## Common Pitfalls

| Pitfall                            | Impact              | Avoidance                                          |
| ---------------------------------- | ------------------- | -------------------------------------------------- |
| Missing User-Agent rotation        | IP blocking         | Use Scrapy's `RotatingUserAgentMiddleware`         |
| No rate limiting                   | Site overload / ban | Configure `DOWNLOAD_DELAY` + `CONCURRENT_REQUESTS` |
| Selenium `webdriver` flag detected | Anti-bot CAPTCHA    | Use `undetected-chromedriver`                      |
| Celery broker not running          | Tasks silently lost | Always verify Redis/RabbitMQ is up                 |

---

## Performance

1. **Scrapy vs Selenium** — Use Scrapy for static content; Selenium only when JS rendering is needed
2. **Celery worker concurrency** — Set `--concurrency=4` per worker, increase worker count for more throughput
3. **BeautifulSoup4 vs lxml** — lxml parser is 3–5x faster than Python's html.parser for DOM parsing
4. **Async scraping** — Scrapy's `Twisted` reactor handles concurrent requests efficiently without thread overhead

---

## Security

1. **Sanitize scraped data** — Always escape/clean before storage or display (XSS prevention)
2. **Proxy rotation** — Use residential proxies to avoid IP-based blocking at scale
3. **Celery task validation** — Validate task parameters; never execute user-supplied URLs without sanitization
4. **Headless detection** — Keep Selenium browser detection mitigation up to date (evolves with anti-bot tech)

---

## Related Projects (in workspace)

- **rhixecompany-comics** — Scraping functionality consolidated here; same Scrapy + Selenium + Celery pattern
- **profile** — Shares Django + PostgreSQL stack

---

## Resources

| Resource       | URL                                                         | Description                    |
| -------------- | ----------------------------------------------------------- | ------------------------------ |
| Scrapy Docs    | <https://docs.scrapy.org/>                                  | Scrapy framework documentation |
| Selenium Docs  | <https://www.selenium.dev/documentation/>                   | Browser automation docs        |
| Celery Docs    | <https://docs.celeryq.dev/>                                 | Celery task queue docs         |
| Anti-bot tools | <https://scrapfly.io/blog/posts/best-anti-bot-bypass-tools> | 2026 anti-detection comparison |

---

## Project: ecom

**Type:** Dual-stack ecommerce platform
**Tech Stack:** DRF, React/Redux Toolkit, PostgreSQL, PayPal, Docker Compose
**Status:** Active

---

## Similar Projects

| Project                 | URL                                                                       | Why Relevant                                         |
| ----------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| django-react-ecommerce  | <https://github.com/aishwaryaw/E-commerce-website-using-React-and-Django> | Reference — similar Django + React ecommerce pattern |
| JustDjango PayPal guide | <https://justdjango.com/blog/django-react-paypal-payments>                | PayPal webhook + Django integration tutorial         |

---

## Key Findings

### DRF + React Ecommerce Architecture

- DRF ViewSets + Serializers pattern is the standard backend architecture for ecommerce APIs (dev.to, 2026)
- Redux Toolkit + RTK Query provides built-in caching, automatic invalidation, and reduces boilerplate vs classic Redux (medium.com/@mernstackdevbykevin, 2026)
- API at `/api/v1/` prefix with URL path versioning is the recommended versioning strategy (oneuptime.com, 2026)

### PayPal Integration

- PayPal Orders API v2 (create + capture) is the modern approach; integrates via JavaScript SDK buttons + Django webhooks (micropyramid.com)
- `dj-paypal` package provides Django model wrappers for PayPal billing plans and webhooks (github.com/HearthSim/dj-paypal)
- Webhook verification is essential — PayPal signs payloads; verify signature server-side before processing

### Docker Compose Deployment

- Dual dev servers: backend on `:8000`, frontend on `:3000` with proxy for API calls (project README)
- Docker Compose for production with separate backend and frontend services; environment variables shared via `.env`

---

## Cheatsheets & Quick Reference

| Topic              | Resource                                                            | Type     |
| ------------------ | ------------------------------------------------------------------- | -------- |
| DRF API versioning | <https://oneuptime.com/blog/post/2026-02-02-django-api-versioning/> | Guide    |
| PayPal + Django    | <https://justdjango.com/blog/django-react-paypal-payments>          | Tutorial |
| RTK Query          | <https://redux-toolkit.js.org/rtk-query/overview>                   | Docs     |

---

## Best Practices

1. **API versioning** — Use URL path versioning (`/api/v1/`) for clear backward-compatible evolution
2. **Separate backend/frontend** — Maintain independent `backend/` and `frontend/` directories with separate dev servers
3. **PayPal webhooks** — Always verify webhook signatures server-side before fulfilling orders
4. **RTK Query cache** — Use RTK Query for API data fetching with automatic cache invalidation on mutations

---

## Common Pitfalls

| Pitfall                         | Impact                                   | Avoidance                                                |
| ------------------------------- | ---------------------------------------- | -------------------------------------------------------- |
| No API versioning               | Breaking changes affect existing clients | Use `/api/v1/` URL prefix from day one                   |
| PayPal webhook unverified       | Fraudulent order processing              | Verify webhook signature via PayPal SDK                  |
| CORS misconfiguration           | Frontend can't reach API                 | Add django-cors-headers; configure CORS_ORIGIN_WHITELIST |
| No pagination on list endpoints | Slow API responses                       | Add DRF pagination (PageNumberPagination recommended)    |

---

## Performance

1. **RTK Query caching** — Minimizes redundant API calls; configure `keepUnusedDataFor` for stale-while-revalidate
2. **DRF pagination** — Use PageNumberPagination with configurable page size to limit response payloads
3. **PostgreSQL indexes** — Add indexes on frequently filtered fields (category, price, status) in model Meta
4. **Select_related / prefetch_related** — Optimize DRF serializer queries with eager loading

---

## Security

1. **JWT auth** — Use short-lived access tokens + long-lived refresh tokens; store access tokens in memory, not localStorage
2. **PayPal webhook verification** — Validate `PAYPAL-AUTH-ALGO` and webhook ID before processing
3. **CORS hardening** — Restrict `CORS_ALLOWED_ORIGINS` to known frontend domains in production
4. **SQL injection prevention** — DRF Serializer validation + Django ORM queries; never use raw SQL

---

## Related Projects (in workspace)

- **cookiecutter-django-tailwind** — Shares layered Django settings pattern
- **xamehi.tv** — Also uses DRF + PayPal + React (though older React 17)
- **xamehi** — Dual-backend architecture with Django + React; ecom uses single Django backend

---

## Resources

| Resource       | URL                                                | Description                         |
| -------------- | -------------------------------------------------- | ----------------------------------- |
| DRF Docs       | <https://www.django-rest-framework.org/>           | Django REST Framework official docs |
| Redux Toolkit  | <https://redux-toolkit.js.org/>                    | Redux Toolkit official docs         |
| PayPal API     | <https://developer.paypal.com/docs/api/orders/v2/> | PayPal Orders API v2                |
| Docker Compose | <https://docs.docker.com/compose/>                 | Docker Compose documentation        |

---

## Project: profile

**Type:** Django blog/CMS with cloud media storage
**Tech Stack:** Django 4.x, GCS, CKEditor 5, PostgreSQL, Docker, GCP
**Status:** Active

---

## Similar Projects

| Project     | URL                           | Why Relevant                                         |
| ----------- | ----------------------------- | ---------------------------------------------------- |
| django-cms  | <https://www.django-cms.org/> | Enterprise Django CMS with CKEditor 5 support (2026) |
| Wagtail CMS | <https://wagtail.org/>        | The most popular Django CMS alternative              |

---

## Key Findings

### Django Blog/CMS with CKEditor 5

- django CMS now ships `djangocms-text-ckeditor5` package with enhanced CKEditor 5 support (django-cms.org, June 2026)
- CKEditor 5 integrates with Django via `django-ckeditor-5` package; image upload requires custom upload backend or django-filer
- CBVs (ListView, DetailView, CreateView, UpdateView) remain the recommended pattern for CMS views in Django 4.x (docs.djangoproject.com)

### Google Cloud Storage

- GCS bucket naming and object naming conventions affect performance — use hierarchical namespace for better prefix-based listing (cloud.google.com/docs)
- `django-storages[google]` with `GOOGLE_APPLICATION_CREDENTIALS` env var is the standard integration path
- `collectstatic` uploads to GCS bucket; use `GS_DEFAULT_ACL` and `GS_QUERYSTRING_AUTH` for public vs private access control

### Docker + GCP Deployment

- Cloud Run + Cloud SQL PostgreSQL with connection pooling is the recommended GCP deployment pattern (forum.djangoproject.com, 2026)
- Cloud Run scaling can overwhelm database connections — implement Django's `CONN_MAX_AGE` + pgbouncer for pooling (forum.djangoproject.com)

---

## Cheatsheets & Quick Reference

| Topic              | Resource                                                                                                               | Type   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------ |
| GCS best practices | <https://cloud.google.com/storage/docs/best-practices>                                                                 | Guide  |
| Django + Cloud Run | <https://oneuptime.com/blog/post/2026-02-17-how-to-build-a-django-application-with-cloud-sql-and-deploy-to-cloud-run/> | Guide  |
| Django-ckeditor-5  | <https://github.com/solaris17/django-ckeditor-5>                                                                       | GitHub |

## Best Practices

1. **CBVs over FBVs** — Use Class-Based Views (ListView, DetailView) for consistent, reusable CMS views
2. **GCS media separation** — Store user-uploaded media in GCS, static files via WhiteNoise or GCS
3. **Connection pooling** — Set `CONN_MAX_AGE` and use pgbouncer when deploying to Cloud Run
4. **CKEditor 5 upload** — Configure image upload handler for rich text; restrict allowed file types server-side

---

## Common Pitfalls

| Pitfall                            | Impact                                 | Avoidance                                      |
| ---------------------------------- | -------------------------------------- | ---------------------------------------------- |
| No GCS credentials in `.env`       | `collectstatic` fails with auth errors | Use GOOGLE_APPLICATION_CREDENTIALS JSON path   |
| CKEditor 5 upload not configured   | Broken image upload UX                 | Implement custom upload endpoint for CKEditor  |
| Cloud Run DB connection exhaustion | 500 errors under load                  | Set MAX_CONNECTIONS and use connection pooling |
| Missing ALLOWED_HOSTS              | 400 Bad Request errors                 | Configure ALLOWED_HOSTS for GCP domains        |

---

## Performance

1. **GCS CDN** — Buckets behind Cloud CDN cache static/media assets with long TTLs
2. **Django caching** — Use Redis/memcached for template fragment and queryset caching
3. **Database indexes** — Index publication date, slug, author fields in CMS models
4. **select_related** — Use eager loading on foreign keys in blog list views to avoid N+1 queries

---

## Security

1. **GCS bucket permissions** — Use fine-grained IAM; never make buckets publicly writable
2. **CKEditor XSS** — Sanitize HTML output with bleach or django-html-sanitizer before rendering
3. **Django SECRET_KEY** — Rotate in GCP Secret Manager; never in version control
4. **Cloud Run IAM** — Use service accounts with least-privilege; no public Cloud Run invocations without auth

---

## Related Projects (in workspace)

- **cookiecutter-django-tailwind** — Shares layered Django settings; profile uses Django 4.x vs 5.x
- **ecom** — Both use Docker Compose and PostgreSQL; profile adds GCS for media
- **rhixecompany-comics** — Both use Django + Docker + PostgreSQL

---

## Resources

| Resource             | URL                                              | Description                   |
| -------------------- | ------------------------------------------------ | ----------------------------- |
| Django Docs          | <https://docs.djangoproject.com/en/4.2/>         | Django 4.x documentation      |
| Google Cloud Storage | <https://cloud.google.com/storage/docs>          | GCS best practices            |
| django-ckeditor-5    | <https://github.com/solaris17/django-ckeditor-5> | CKEditor 5 Django integration |
| django-storages      | <https://django-storages.readthedocs.io/>        | Django storage backends       |

---

## Project: rhixecompany-comics

**Type:** Dual-stack web platform (Django backend + Next.js frontend)
**Tech Stack:** Django 5.x, Next.js 16, Celery + Redis, Scrapy, Selenium, PostgreSQL, Docker
**Status:** Active

---

## Similar Projects

| Project                             | URL                                                                                                             | Why Relevant                                      |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Django + Next.js cookiecutter       | <https://www.reddit.com/r/django/comments/1cbbmru/django_and_nextjs_cookiecutter_monorepo>                      | Community patterns for Django + Next.js monorepos |
| Next.js + PostgreSQL + Redis Docker | <https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/> | Reference Docker Compose setup                    |

---

## Key Findings

### Django + Next.js Dual-Stack Architecture

- The biggest maintenance risk in a split architecture is drift between Django API responses and Next.js type expectations — maintain a shared OpenAPI/Swagger spec (medium.com/@mmoznu, 2026)
- Two independent stacks sharing a PostgreSQL database is a common pattern; ensure migrations are coordinated (reddit.com/r/django, 2026)
- Django at `/api/` and Next.js at frontend domain; CORS configured on Django side

### Next.js 16 App Router

- Server Components by default, Client Components only when interactivity needed — reduces JS bundle size significantly (tech-insider.org, 2026)
- Turbopack in Next.js 16 delivers ~400% faster dev server startup vs webpack (tech-insider.org, 2026)
- Server Actions simplify form handling and data mutations without boilerplate API endpoints (YouTube, 2026)

### Celery + Redis for Scraping

- `django-celery-beat` provides database-backed periodic task scheduling for scraping jobs (oneuptime.com, 2026)
- Scrapy spiders called from Celery tasks for distributed scraping; results persisted via Django ORM
- Redis serves as both Celery broker and result backend; monitoring via Flower dashboard

---

## Cheatsheets & Quick Reference

| Topic                        | Resource                                                                                                        | Type              |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------- |
| Next.js 16 App Router        | <https://nextjs.org/docs/app>                                                                                   | Official Docs     |
| Celery + Django              | <https://docs.celeryq.dev/en/stable/django/>                                                                    | Integration Guide |
| Docker Compose multi-service | <https://oneuptime.com/blog/post/2026-02-08-how-to-set-up-a-nextjs-postgresql-redis-stack-with-docker-compose/> | Tutorial          |

---

## Best Practices

1. **Shared API contract** — Maintain OpenAPI spec for Django API; generate TypeScript types for Next.js frontend
2. **Server Components by default** — Minimize client-side JS; use Client Components only for interactive UI
3. **Celery beat scheduling** — Use `django-celery-beat` DB-backed scheduler for manageable periodic scraping tasks
4. **Docker Compose orchestration** — Run Django, Next.js, PostgreSQL, and Redis as coordinated services

---

## Common Pitfalls

| Pitfall                       | Impact                            | Avoidance                                                   |
| ----------------------------- | --------------------------------- | ----------------------------------------------------------- |
| API field drift               | Runtime type mismatches           | Generate TypeScript types from OpenAPI spec                 |
| Client Component misuse       | Bloated JS bundles                | Default to Server Component; migrate only interactive parts |
| Celery beat not synced        | Missed or duplicate scraping jobs | Use django-celery-beat scheduler with DB backend            |
| CORS on `/api/` Django routes | Next.js can't fetch               | Configure django-cors-headers for Next.js frontend domain   |

---

## Performance

1. **Turbopack** — Next.js 16's Turbopack provides 400% faster dev server vs webpack-based CRA
2. **Celery worker scaling** — Scale Celery workers independently from web workers for heavy scraping loads
3. **Redis caching** — Cache Django API responses in Redis; Next.js ISR for static content
4. **PostgreSQL connection pooling** — Both stacks share the same DB; pgbouncer prevents connection exhaustion

---

## Security

1. **Shared database concerns** — Both stacks access same PostgreSQL; isolate with separate Django app permissions
2. **CORS for dual domains** — Restrict `CORS_ALLOWED_ORIGINS` to Next.js frontend domain only
3. **Next.js Server Actions** — Validate all server action inputs; don't trust client-side form data
4. **Scraping robots.txt** — Respect robots.txt from both Scrapy spiders and Selenium scrapers

---

## Related Projects (in workspace)

- **Django-Scrapy-Selenium** — Scraping functionality was consolidated from this project
- **xamehi.tv** — Shares DRF + React pattern (though xamehi.tv uses React 17, not Next.js)
- **cookiecutter-django-tailwind** — Django 5.x best practices apply to the backend
- **xamehi** — Another dual-service architecture (Django + Express instead of Django + Next.js)

---

## Resources

| Resource        | URL                                      | Description                      |
| --------------- | ---------------------------------------- | -------------------------------- |
| Next.js 16 Docs | <https://nextjs.org/docs>                | Next.js App Router documentation |
| Django Docs     | <https://docs.djangoproject.com/en/5.2/> | Django 5.x documentation         |
| Celery Docs     | <https://docs.celeryq.dev/>              | Celery task queue documentation  |
| Docker Compose  | <https://docs.docker.com/compose/>       | Multi-service orchestration      |

---

## Project: xamehi

**Type:** Legacy dual-backend app (Django + Express) + React frontend
**Tech Stack:** Django+DRF, Express, React 18/CRA, PostgreSQL
**Status:** Active (legacy — consolidation opportunity)

---

## Similar Projects

| Project               | URL                                                                                                    | Why Relevant                       |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| Django + React guide  | <https://fdcservers.net/blog/how-to-build-a-simple-app-with-django-and-react>                          | Django + React CORS setup patterns |
| CRA migration to Vite | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | CRA deprecation and migration path |

---

## Key Findings

### Dual-Backend Architecture

- Running Django (DRF) and Express as separate backends requires careful CORS configuration — django-cors-headers for Django, `cors` middleware for Express (forum.djangoproject.com, 2026)
- Dual backends increase production complexity: three separate build/deploy steps (React build, Django collectstatic, Express deploy)
- PostgreSQL connection pooling must be coordinated between both backends to avoid connection exhaustion

### React 18 CRA Migration

- Create React App is no longer recommended by the React team — slow builds, no ES module support (dev.to, 2026)
- Migration to Vite is the recommended path: faster HMR, ES-native dev server, simpler config (oneuptime.com, 2026)
- CRA's react-scripts 4.x/5.x has been abandoned; security patches stopped in 2023

### PostgreSQL Dual-Backend Connection Pooling

- Both Django and Express share the same PostgreSQL database — implement pgbouncer for connection pooling
- Django uses `CONN_MAX_AGE` for persistent connections; Express uses `pg-pool` for connection pooling

---

## Cheatsheets & Quick Reference

| Topic                | Resource                                                                                               | Type    |
| -------------------- | ------------------------------------------------------------------------------------------------------ | ------- |
| CRA → Vite migration | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | Guide   |
| Django CORS          | <https://pypi.org/project/django-cors-headers/>                                                        | Package |
| PostgreSQL pooling   | <https://www.pgbouncer.org/>                                                                           | Guide   |

---

## Best Practices

1. **Consolidate backends** — Consider merging Express API routes into Django DRF for simpler deployment
2. **Migrate CRA to Vite** — Faster builds, modern ESM support, active maintenance
3. **pgbouncer for shared DB** — Prevent connection pool exhaustion from dual backends
4. **Unified CORS config** — Single CORS policy shared across Django and Express for consistent security

---

## Common Pitfalls

| Pitfall                     | Impact                           | Avoidance                                                       |
| --------------------------- | -------------------------------- | --------------------------------------------------------------- |
| CRA deprecation             | No security patches, slow builds | Migrate to Vite as soon as possible                             |
| Dual backend drift          | API inconsistency                | Consolidate API surface into DRF                                |
| DB connection exhaustion    | Application outages              | Implement pgbouncer with connection limits                      |
| Port confusion (3 services) | Dev environment errors           | Document port mapping: Express :5000, Django :8000, React :3000 |

---

## Performance

1. **Vite migration** — 10x faster HMR vs CRA's webpack-based dev server
2. **Consolidate API** — Eliminate Express backend to reduce infrastructure overhead if it's low-traffic
3. **PostgreSQL connection pooling** — pgbouncer with transaction pooling for high concurrency
4. **Django caching** — Add Redis caching layer for frequently accessed API endpoints

---

## Security

1. **CORS hardening** — Three services mean three CORS attack surfaces; restrict each to minimal allowed origins
2. **Express dependency audit** — Ensure Express + middleware dependencies are up to date (legacy risk)
3. **JWT shared secret** — If both backends validate JWTs, rotate shared secret regularly
4. **HTTPS required** — Three endpoints (React, Django, Express) all need TLS in production

---

## Related Projects (in workspace)

- **xamehi.tv** — Same Django + React pattern; xamehi adds Express backend
- **ecom** — Simpler architecture (single Django backend + React); xamehi is more complex with dual backends
- **rhixecompany-comics** — Another dual-service architecture (Django + Next.js)

---

## Resources

| Resource              | URL                                                                                                    | Description                  |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------- |
| Vite migration        | <https://dev.to/solitrix02/goodbye-cra-hello-vite-a-developers-2026-survival-guide-for-migration-2a9f> | CRA → Vite guide             |
| Django REST Framework | <https://www.django-rest-framework.org/>                                                               | DRF official docs            |
| Express.js            | <https://expressjs.com/>                                                                               | Express web framework        |
| pgbouncer             | <https://www.pgbouncer.org/>                                                                           | PostgreSQL connection pooler |

---

## Project: xamehi.tv

**Type:** Django REST + React streaming platform
**Tech Stack:** Django DRF, React 17, MUI 4, Redux, SimpleJWT, django-allauth, PostgreSQL, PayPal
**Status:** Active

---

## Similar Projects

| Project               | URL                                                               | Why Relevant                         |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| DRF + SimpleJWT auth  | <https://www.django-rest-framework.org/api-guide/authentication/> | DRF JWT authentication docs          |
| MUI v4 → v5 migration | <https://mui.com/material-ui/migration/migration-v4/>             | Material-UI v4 to v5 migration guide |

---

## Key Findings

### DRF + SimpleJWT Auth

- djangorestframework-simplejwt is the most popular JWT auth package for DRF; supports access + refresh token pattern and token blacklist (django-rest-framework.org, 2026)
- django-allauth provides social auth (Google, GitHub) alongside SimpleJWT; requires careful URL namespace configuration to avoid conflicts
- WorkOS (2026) is emerging as an enterprise auth alternative, offering SSO, SCIM, and directory sync out of the box (workos.com, 2026)

### React 17 + Material-UI 4 Upgrade Path

- Material-UI v4 uses JSS for styling; v5 replaces it with Emotion — this is the biggest breaking change in the migration (mui.com)
- Codemods automate 80% of the MUI v4→v5 migration: `npx @mui/codemod v5.0.0/preset-safe` (mui.com)
- React 17 → React 18 migration: no major breaking changes to existing APIs; upgraded `ReactDOM.createRoot()` and automatic batching are key differences (jahed.dev, 2026)
- Redux Toolkit with RTK Query is recommended over classic Redux + redux-thunk for new development (medium.com/@mernstackdevbykevin, 2026)

### Production Serving

- Gunicorn + WhiteNoise is the standard Django production serving stack for small-to-medium applications (reddit.com/r/django)
- WhiteNoise automatically generates versioned static files with MD5 hashes and appropriate Cache-Control headers (reddit.com/r/django)
- For larger deployments, replace WhiteNoise with nginx/CDN for static/media serving

---

## Cheatsheets & Quick Reference

| Topic               | Resource                                                   | Type            |
| ------------------- | ---------------------------------------------------------- | --------------- |
| MUI v4→v5 migration | <https://mui.com/material-ui/migration/migration-v4/>      | Migration Guide |
| React 18 upgrade    | <https://react.dev/blog/2022/03/08/react-18-upgrade-guide> | Guide           |
| DRF SimpleJWT       | <https://django-rest-framework-simplejwt.readthedocs.io/>  | Docs            |

---

## Best Practices

1. **Upgrade React 17→18** — Automatic batching, Concurrent Features, and Suspense improvements; mostly backward compatible
2. **Migrate MUI v4→v5** — Emotion over JSS, improved theming, better TypeScript support; use codemods for efficiency
3. **Redux Toolkit migration** — Replace redux-thunk with RTK Query for API data fetching and cache management
4. **JWT security** — Short-lived access tokens (5–15 min), long-lived refresh tokens with rotation; store in memory not localStorage

---

## Common Pitfalls

| Pitfall                           | Impact                                  | Avoidance                                                      |
| --------------------------------- | --------------------------------------- | -------------------------------------------------------------- |
| MUI v4 JSS → Emotion breakage     | Styling completely broken after upgrade | Use codemods; run `npx @mui/codemod v5.0.0/preset-safe`        |
| React 17 createRoot missing       | App doesn't render                      | Update to `createRoot()` API for React 18                      |
| SimpleJWT + allauth URL conflicts | Auth routes clash                       | Carefully namespace allauth URLs under `/accounts/`            |
| CORS + proxy confusion            | Frontend can't reach backend            | Document CORS + proxy setup; test with production config early |

---

## Performance

1. **React 18 automatic batching** — Fewer re-renders in promises and timeouts, improving UI responsiveness
2. **RTK Query caching** — Replaces manual redux-thunk fetching; built-in cache invalidation and deduplication
3. **MUI v5 Emotion** — Smaller runtime vs JSS; `styled()` API enables cleaner component composition
4. **Gunicorn + WhiteNoise** — Sufficient for moderate traffic; CDN recommended for video assets

---

## Security

1. **SimpleJWT token blacklist** — Enable blacklist app to revoke compromised refresh tokens server-side
2. **PayPal webhook verification** — Validate PayPal webhook signatures to prevent fraudulent payment callbacks
3. **django-allauth social auth** — Configure callback URL whitelist; restrict allowed social providers
4. **CORS restriction** — django-cors-headers with `CORS_ALLOWED_ORIGINS` limited to frontend domain

---

## Related Projects (in workspace)

- **ecom** — Shares DRF + PayPal + React stack; ecom uses React 18/Redux Toolkit (more modern)
- **xamehi** — Shares Django + React pattern; xamehi has dual backends (Django + Express)
- **rhixecompany-comics** — Dual-stack platform; xamehi.tv is simpler (single Django backend)
- **profile** — Django monolith; both use Django but xamehi.tv adds React frontend

---

## Resources

| Resource         | URL                                                       | Description                  |
| ---------------- | --------------------------------------------------------- | ---------------------------- |
| React 18 Docs    | <https://react.dev/>                                      | React official documentation |
| Material-UI v5   | <https://mui.com/>                                        | MUI v5 documentation         |
| SimpleJWT        | <https://django-rest-framework-simplejwt.readthedocs.io/> | DRF JWT auth docs            |
| django-allauth   | <https://docs.allauth.org/>                               | Social auth integration      |
| PayPal Developer | <https://developer.paypal.com/>                           | PayPal API documentation     |
