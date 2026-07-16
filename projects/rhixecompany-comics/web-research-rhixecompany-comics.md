# Web Research Report — rhixecompany-comics

> **Type:** Tech-stack targeted research | **Updated:** 2026-07-16
> **Stack:** PostgreSQL, Vite, React, Next.js, DRF (Django REST Framework), Scrapy, Python, Redis, TypeScript, Selenium, Django, Docker, Tailwind CSS

---

## Table of Contents

1. [Research Methodology](#research-methodology)
2. [DRF + Next.js Dual-Stack Architecture](#1-drf--nextjs-dual-stack-architecture)
3. [DRF Performance Optimization & Redis Caching](#2-drf-performance-optimization--redis-caching)
4. [Celery + Redis Production Patterns](#3-celery--redis-production-patterns)
5. [Scrapy + Selenium + Celery Scraping Pipeline](#4-scrapy--selenium--celery-scraping-pipeline)
6. [Docker Multi-Service Deployment](#5-docker-multi-service-deployment)
7. [Next.js Docker & Standalone Mode](#6-nextjs-docker--standalone-mode)
8. [TypeScript + DRF OpenAPI Type Generation](#7-typescript--drf-openapi-type-generation)
9. [Tailwind CSS v4 Migration & Best Practices](#8-tailwind-css-v4-migration--best-practices)
10. [Selenium Automation Best Practices](#9-selenium-automation-best-practices)
11. [PostgreSQL Connection Pooling in Production](#10-postgresql-connection-pooling-in-production)
12. [Common Pitfalls Matrix](#11-common-pitfalls-matrix)
13. [Security Checklist](#12-security-checklist)
14. [Sources](#sources)

---

## Research Methodology

- **Searches performed:** 10 targeted web searches
- **Pages extracted:** 10+ articles, docs, and forum threads
- **Tools used:** web_search, web_extract
- **Date:** 2026-07-16

---

## 1. DRF + Next.js Dual-Stack Architecture

### Key Sources

| Source | URL | Relevance |
|--------|-----|-----------|
| DEV.to — FullStack Django+DRF+Next.js | <https://dev.to/koladev/...> | End-to-end tutorial pattern |
| Django Forum — Architecture Advice | <https://forum.djangoproject.com/t/...42808> | Deployment architecture discussion |
| Reddit r/django — Next.js + DRF | <https://reddit.com/...1jjs4hb> | Community architecture insights |

### Best Practices

1. **Separate servers for frontend and backend (production)**
   - Django/Gunicorn handles API on `:8000`, Nginx in front for static/media
   - Next.js runs on `:3000` or deployed as standalone container
   - Nginx reverse proxy routes: `/api/*` → Django, `/*` → Next.js (or separate domains)
   - WhiteNoise is not recommended for production when Nginx is available

2. **API field drift is the #1 risk**
   - Maintain OpenAPI (drf-spectacular) as the single source of truth
   - Auto-generate TypeScript types from DRF schema
   - Validate on CI with `./manage.py spectacular --validate --fail-on-warn`

3. **CORS configuration**
   - Use `django-cors-headers >=4.3`
   - Explicit `CORS_ALLOWED_ORIGINS` — never use `CORS_ALLOW_ALL_ORIGINS` in production
   - Match frontend domain(s) exactly

4. **Authentication flow**
   - DRF with `djangorestframework-simplejwt` for JWT
   - Next.js middleware reads JWT from `Authorization` header
   - Refresh token rotation for security

### Architecture Decision: Single vs Separate Servers

| Approach | Pros | Cons |
|----------|------|------|
| Single server + Nginx | Simpler deploy, lower cost | Static file serving competes with API |
| Separate servers (API + Frontend) | Independent scaling, better perf | More infra complexity |
| Same server, domain-based routing | Clean separation, single VPS | Need DNS/CORS config |

---

## 2. DRF Performance Optimization & Redis Caching

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| freeCodeCamp — Optimize DRF APIs | <https://www.freecodecamp.org/news/how-to-optimize-django-rest-apis-for-performance/> | Profiling, N+1, caching, pagination |
| ScreamingAtMyScreen — DRF Caching | <https://www.screamingatmyscreen.com/caching-and-django-rest-framework> | JSONField pre-serialization pattern |
| Medium — DRF Redis Caching | <https://medium.com/@alirezazarei51/optimizing-performance-in-drf> | Redis + DRF caching strategies |

### N+1 Query Prevention

```python
# BAD — triggers 101 queries for 100 posts
posts = Post.objects.all()
for post in posts:
    print(post.author.name)

# GOOD — single JOIN query
posts = Post.objects.select_related('author').all()
```

### Critical DRF Performance Rules

1. **Always paginate list endpoints** — DRF has built-in `PageNumberPagination`
2. **Use `select_related`** for FK/O2O relationships (SQL JOIN)
3. **Use `prefetch_related`** for M2M/reverse FK (separate query + Python joining)
4. **Profile before optimizing** — use Django Debug Toolbar or `connection.queries`
5. **Cache strategically** — don't cache everything; identify expensive endpoints

### Redis Caching Patterns

**Pattern A: JSONField pre-serialization** (for read-heavy, slowly-changing data)

- Store pre-serialized JSON directly in a model `JSONField`
- Override `to_representation` in serializer to return cached data
- Update via background Celery task when data changes
- Response time improvement: 30s → <1s (documented)

**Pattern B: django-redis + cache_page decorator**

```python
from django.views.decorators.cache import cache_page

@api_view(['GET'])
@cache_page(60 * 15)  # 15 minute cache
def expensive_list_view(request):
    ...
```

**Pattern C: Manual cache with Redis**

```python
from django.core.cache import cache

def get_comics():
    cache_key = 'comics_list'
    data = cache.get(cache_key)
    if data is None:
        data = ComicSerializer(Comic.objects.all(), many=True).data
        cache.set(cache_key, data, timeout=300)
    return data
```

### Recommended django-redis Configuration

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
            'SERIALIZER': 'django_redis.serializers.json.JSONSerializer',
        }
    }
}
```

**Important:** Use separate Redis DBs for cache, Celery broker, and Celery results to prevent cache eviction from killing task messages.

---

## 3. Celery + Redis Production Patterns

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| Medium — Celery Production Patterns | <https://medium.com/@mmoznu/celery-and-django-in-production> | Queue separation, retry strategy, idempotency |
| Vinta — Advanced Celery for Django | <https://www.vintasoftware.com/blog/guide-django-celery-tasks> | Common pitfalls, task loss, monitoring |
| Adam Johnson — Common Celery Issues | <https://adamj.eu/tech/2020/02/03/common-celery-issues-on-django-projects> | Reliability patterns |

### Production-Ready Celery Configuration

```python
# settings/base.py
CELERY_BROKER_URL = env('REDIS_URL') + '/0'   # Celery broker
CELERY_RESULT_BACKEND = env('REDIS_URL') + '/1'  # Results
# Cache uses /2 — see Redis section above

CELERY_TASK_ACKS_LATE = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_SOFT_TIME_LIMIT = 600  # 10 min
CELERY_TASK_TIME_LIMIT = 660       # 11 min
```

### Queue Separation (Critical)

```python
CELERY_TASK_QUEUES = {
    'critical': {'exchange': 'critical', 'routing_key': 'critical'},
    'default':  {'exchange': 'default',  'routing_key': 'default'},
    'bulk':     {'exchange': 'bulk',     'routing_key': 'bulk'},
}

CELERY_TASK_ROUTES = {
    'comics.tasks.send_password_reset':    {'queue': 'critical'},
    'comics.tasks.process_payment':        {'queue': 'critical'},
    'comics.tasks.process_webhook':        {'queue': 'default'},
    'scraping.tasks.run_spider':           {'queue': 'bulk'},
    'comics.tasks.generate_report':        {'queue': 'bulk'},
}
```

Run separate workers:

```bash
# Docker Compose services
celery -A config worker -Q critical --concurrency=4   # Critical: more workers
celery -A config worker -Q default --concurrency=2    # Default: standard
celery -A config worker -Q bulk --concurrency=1       # Bulk: fewer workers
```

### Task Design Rules

1. **Idempotency first** — always check if work was already done
2. **Pass IDs, not objects** — never serialize model instances; fetch fresh in task
3. **Exponential backoff** — `countdown=2 ** self.request.retries`
4. **Max retries with alerting** — never retry forever; alert on exhaustion
5. **Bind tasks** for self-reference: `@shared_task(bind=True)`
6. **Use `autoretry_for`** with `retry_jitter=True` to prevent thundering herd
7. **Celery Beat** for scheduled scraping — use `django-celery-beat` for DB-backed schedules

### Scrapy + Celery Integration Pitfall

Scrapy's reactor is **not restartable** by default. When running spiders as Celery tasks, use `CrawlerRunner` (not `CrawlerProcess`) and set `stop_after_crawl=True`. With `stop_after_crawl=False`, the reactor keeps running and workers become unresponsive after N crawls (where N = concurrency setting).

---

## 4. Scrapy + Selenium + Celery Scraping Pipeline

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| GroupBWT — Scrapy Architecture 2026 | <https://groupbwt.com/blog/scrapy-tutorial> | Architecture, async, Playwright, distributed |
| LinkedIn — Scrapy + Selenium Deep Dive | <https://www.linkedin.com/pulse/advanced-web-scraping-selenium-scrapy> | Combined usage patterns |
| Stack Overflow — Celery + Scrapy | <https://stackoverflow.com/questions/77053237> | Reactor management |

### Scrapy 2.13+ Key Changes

- `async def start()` replaces `start_requests()` (deprecated)
- `DownloaderAwarePriorityQueue` replaces the default scheduler — better domain fairness
- Playwright integration as a custom download handler for JS rendering
- Python 3.10+ required

### Tool Selection Matrix

| Tool | Best For | Resource Cost |
|------|----------|---------------|
| **Scrapy** | Large-scale data pipelines, crawling millions of pages | Low (HTTP only) |
| **Scrapy + Playwright** | JS-heavy SPAs within Scrapy pipeline | Medium |
| **Selenium** | Interactive testing, form filling, visual checks | High (full browser) |
| **BeautifulSoup** | Quick one-off parsing only (not a framework) | Negligible |

### Production Scrapy Settings

```python
# settings.py (generated by scrapy startproject)
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1  # Conservative by default

# Framework defaults (more aggressive)
# CONCURRENT_REQUESTS = 16
# CONCURRENT_REQUESTS_PER_DOMAIN = 8
```

### Scrapy + Django Integration

- `scrapy-djangoitem` or direct Django ORM usage in pipelines
- Celery tasks to trigger `CrawlerRunner` — spiders run as tasks, not views
- Pipeline chain: Validation → Clean → Transform → Django ORM Save → Dedup
- Item pipelines should be modular — one concern per stage

### Selenium Best Practices

1. **Page Object Model (POM)** — separate page classes for locators/actions
2. **Use explicit waits** — never `time.sleep()`; always `WebDriverWait`
3. **Headless mode** for scraping (faster, less resource)
4. **Parallel WebDriver sessions** via `concurrent.futures` for speed
5. **Proxy rotation** in Scrapy middleware, not Selenium
6. **Browser context cleanup** — always quit drivers in `finally`/context manager

---

## 5. Docker Multi-Service Deployment

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| TestDriven.io — Dockerizing Django | <https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx> | Step-by-step, Nginx+Gunicorn |
| Manish Bhusal — DRF Production Deploy | <https://www.bhusalmanish.com.np/blog/posts/deploy-drf-production.html> | Multi-stage Docker, SSL, security |
| Django Forum — Nginx Architecture | <https://forum.djangoproject.com/t/...42808> | Nginx as reverse proxy |

### Recommended Architecture

```
User Request
      │
      ▼
  ┌──────────────────────────────────────────────┐
  │              Nginx (reverse proxy)            │
  │      :80/443 → SSL termination                │
  │  /api/* → Django/Gunicorn :8000               │
  │  /*     → Next.js :3000                       │
  │  /static/* → served directly (fast)           │
  └──────────────────────────────────────────────┘
```

### Docker Compose Service Layout

| Service | Image | Depends On | Notes |
|---------|-------|------------|-------|
| `nginx` | nginx:alpine | web, nextjs | SSL termination, reverse proxy |
| `web` | django:latest | db, redis | Gunicorn, 5 workers (2-core VPS) |
| `nextjs` | nextjs:latest | — | Standalone mode, `output: 'standalone'` |
| `db` | postgres:16-alpine | — | Volume-mounted data, health check |
| `redis` | redis:7-alpine | — | Broker + cache + results |
| `celery-critical` | django:latest | redis, db | Queues: critical |
| `celery-default` | django:latest | redis, db | Queues: default |
| `celery-bulk` | django:latest | redis, db | Queues: bulk |
| `celery-beat` | django:latest | redis, db | Scheduled tasks |

### Django Dockerfile (Multi-Stage)

```
Stage 1: Builder → Install build deps, create venv, install requirements
Stage 2: Runtime → Copy venv from builder, non-root user, HEALTHCHECK
```

Key points:
- Non-root user (`appuser`) for security
- `CONN_MAX_AGE` for production PostgreSQL connection reuse
- Gunicorn workers formula: `(2 × CPU cores) + 1`
- HEALTHCHECK with curl to `/health/`
- `.dockerignore` to exclude `.git`, `node_modules`, `__pycache__`

### Docker Security Checklist

- [ ] `DEBUG=False` in production (check twice)
- [ ] `SECRET_KEY` unique and not in git
- [ ] `ALLOWED_HOSTS` restricted to your domain
- [ ] `CORS_ALLOWED_ORIGINS` restricted
- [ ] Database password strong and unique
- [ ] Firewall allows ports 22, 80, 443 only
- [ ] SSH key-based auth only
- [ ] SSL certificate valid (Let's Encrypt)
- [ ] Sentry error tracking (optional but recommended)

---

## 6. Next.js Docker & Standalone Mode

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| Next.js Docs — Deploying | <https://nextjs.org/docs/app/getting-started/deploying> | Official deployment guide |
| JavaScript in Plain English — Next.js Docker | <https://javascript.plainenglish.io/next-js-15-self-hosting-with-docker> | Standalone mode, 70-80% image size reduction |
| hmos.dev — Next.js Docker Standalone | <https://hmos.dev/en/nextjs-docker-standalone-and-custom-server> | Custom server + standalone |

### Standalone Output Configuration

```ts
// next.config.ts
const nextConfig = {
  output: 'standalone',  // critical for Docker
  // ...other config
};
export default nextConfig;
```

### Dockerfile Optimization

Multi-stage Docker reduces image from ~800MB to ~180-250MB:

```
Stage 0 (base): node:20-alpine + libc6-compat
Stage 1 (deps): npm ci --omit=dev
Stage 2 (builder): npm run build → .next/standalone/
Stage 3 (runner): Copy standalone/ + static/ + public/, non-root user (nextjs:nodejs)
```

### Environment Variables Strategy

| Type | Prefix | When Set | Example |
|------|--------|----------|---------|
| Build-time | `NEXT_PUBLIC_*` | `docker build --build-arg` | `NEXT_PUBLIC_API_URL` |
| Runtime | No prefix | `docker run -e` or Compose | `DATABASE_URL`, `REDIS_URL` |

### Layer Caching Optimization

Copy files in order of change frequency (least → most):
1. `package.json` + `package-lock.json` → `npm ci`
2. Source code → build
3. This maximizes Docker layer cache hits

---

## 7. TypeScript + DRF OpenAPI Type Generation

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| drf-spectacular docs — Client Generation | <https://drf-spectacular.readthedocs.io/en/latest/client_generation.html> | COMPONENT_SPLIT_REQUEST, CI validation |
| GitHub — tfranzel/drf-spectacular | <https://github.com/tfranzel/drf-spectacular> | OpenAPI 3.0.3/3.1, CLI, CI integration |
| Boston Python 2024 — DRF-Spectacular + TS Codegen | <https://www.youtube.com/watch?v=Rq3Y7-tPmmA> | Workshop on client generation |
| Reddit — Generating TS types for DRF | <https://www.reddit.com/r/django/comments/ooqhdo> | Community tooling discussion |

### Recommended Setup

```python
# settings.py
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'RhixeCompany Comics API',
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True,  # CRITICAL for good client generation
    'SERVE_INCLUDE_SCHEMA': False,
}
```

### CI Validation

```bash
# Generate and validate schema — break CI on warnings
./manage.py spectacular --file schema.yml --validate --fail-on-warn
```

### TypeScript Code Generation Tools

| Tool | Description | Best For |
|------|-------------|----------|
| **openapi-typescript-codegen** | Mature, widely used | DRF + Next.js projects |
| **openapi-typescript** | TypeScript-first, fast | Zod/primitives-focused projects |
| **drf-typescript-generator** | DRF-specific tool | Quick DRF → TS conversion |
| **orval** | Full-stack client generator | React hooks, TanStack Query |

### `COMPONENT_SPLIT_REQUEST` = True

This single setting resolves most client generation issues:
- Splits request components from response components
- Fixes `readOnly`/`required` field conflicts (e.g., `id` in POST)
- Handles `FileField` differences between upload/download
- Fixes `PATCH` vs `POST` `required` property conflicts (enabled by default)

---

## 8. Tailwind CSS v4 Migration & Best Practices

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| Tailwind Official — Upgrade Guide | <https://tailwindcss.com/docs/upgrade-guide> | Official migration steps |
| LogRocket — Tailwind CSS 2026 Guide | <https://blog.logrocket.com/tailwind-css-guide> | v4 features, CSS-first config |
| GitHub Discussion — v4 Issues | <https://github.com/tailwindlabs/tailwindcss/discussions/16517> | Migration pain points |
| Alex Cavender — Upgrade Guide | <https://alexcavender.com/blog/upgrading-tailwind-css-next-js-2025> | Step-by-step Next.js upgrade |

### Key v4 Changes (from v3)

| Feature | v3 | v4 |
|---------|----|----|
| Configuration | `tailwind.config.js` | CSS-first via `@theme` directive |
| Entry point | `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| Custom values | `theme.extend` in JS | `@theme { --color-*: ... }` in CSS |
| Dark mode | Config file | CSS-based (`@variant dark`) |
| Browser support | Older browsers supported | Safari 16.4+, Chrome 111+, Firefox 128+ |
| Performance | PostCSS plugin | Lightning CSS, faster builds |

### Migration Path

```bash
# Use official upgrade tool
npx @tailwindcss/upgrade

# Or manual migration
npm install tailwindcss@latest @tailwindcss/postcss@latest
```

```css
/* v4 CSS-first approach — NO config file needed */
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-primary-dark: #2563eb;
  --font-family-display: "Oswald", sans-serif;
}
```

### v4 Breaking Changes to Watch

1. Default styles removed — some base resets gone
2. Dark mode behavior changed — CSS-based now, not class-based by default
3. Some v3 config properties don't directly translate to `@theme`
4. `@config` directive allows loading legacy `tailwind.config.js` for migration period
5. **Run upgrade tool in a new branch** and diff before merging

---

## 9. Selenium Automation Best Practices

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| BrowserStack — 26 Selenium Best Practices | <https://www.browserstack.com/guide/best-practices-in-selenium-automation> | Locators, waits, parallel testing |
| LinkedIn — Selenium WebDriver 2025 Guide | <https://www.linkedin.com/pulse/mastering-selenium-webdriver-2025> | POM, cross-browser, scalability |

### For Comics Scraping Context

1. **Page Object Model (POM)** — separate page classes for each comic site
2. **Explicit waits** over implicit: `WebDriverWait(driver, 10).until(...)`
3. **Headless mode** for non-interactive scraping
4. **WebDriver management** — use `webdriver-manager` for auto-driver downloads
5. **Parallel execution** — `ThreadPoolExecutor` for multi-site scraping
6. **Driver cleanup** — always run `driver.quit()` in `finally` or `contextlib.closing`
7. **Screenshots on failure** — capture page state for debugging

```python
# Example pattern
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ComicSiteScraper:
    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(options=options)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.driver.quit()

    def scrape_chapter(self, url: str) -> dict:
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        # ... scraping logic
```

---

## 10. PostgreSQL Connection Pooling in Production

### Key Sources

| Source | URL | Key Takeaways |
|--------|-----|---------------|
| Stack Overflow — PgBouncer + Django | <https://stackoverflow.com/questions/27418264> | CONN_MAX_AGE settings |
| Django Forum — PgBouncer Config | <https://forum.djangoproject.com/t/configure-pgbouncer-with-django/43161> | Transaction pooling, server-side cursors |
| OneUptime — PgBouncer Guide | <https://oneuptime.com/blog/post/2026-02-02-postgresql-pgbouncer-pooling> | Pool modes, tuning parameters |

### Critical Settings

```python
# settings/production.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        ...
        'CONN_MAX_AGE': 600,          # Reuse connections for 10 min
        'CONN_HEALTH_CHECKS': True,   # Verify before reuse
        'OPTIONS': {
            'pool': {
                'min_size': 2,
                'max_size': 10,
                'timeout': 30,
            }
        }
    }
}
```

### PgBouncer Gotchas

- **Transaction pooling mode** prevents use of server-side cursors (Django default)
- Disable with `DISABLE_SERVER_SIDE_CURSORS = True` in settings
- PgBouncer max connections must be **less than** PostgreSQL max connections
- `CONN_MAX_AGE` + persistent connections can spike connection count if misconfigured with threaded workers (e.g., Gunicorn eventlet)
- Use `psycopg2` connection pooling OR PgBouncer — not both

### Development vs Production Connection Settings

| Setting | Development | Production |
|---------|-------------|------------|
| `CONN_MAX_AGE` | 0 (fresh per request) | 300-600 (reuse) |
| `CONN_HEALTH_CHECKS` | False | True |
| Pooling | None | PgBouncer or psycopg2 pool |
| `ATOMIC_REQUESTS` | False (for perf) | Depends on workload |

---

## 11. Common Pitfalls Matrix

| Pitfall | Stack Area | Impact | Avoidance |
|---------|-----------|--------|-----------|
| API field drift | DRF ↔ Next.js | Frontend breaks | OpenAPI spec + `COMPONENT_SPLIT_REQUEST` + auto TS types |
| N+1 queries in serializers | DRF | Slow API | `select_related`/`prefetch_related` + Django Debug Toolbar |
| Missing Celery `ack_late` | Celery | Lost tasks on worker crash | Always set `task_acks_late=True` |
| Server Actions in Client Components | Next.js | Runtime errors | Keep Server Actions in Server Components only |
| Tailwind v3→v4 migration | Tailwind | Build breaks | Use upgrade tool, `@import "tailwindcss"`, no `tailwind.config.js` |
| Scrapy reactor not restartable | Scrapy + Celery | Worker deadlock | `CrawlerRunner` with `stop_after_crawl=True` |
| Same queue for slow + fast tasks | Celery | Starvation | Queue separation (critical/default/bulk) |
| Passing model instances to tasks | Celery | Stale data | Always pass IDs, fetch fresh in task body |
| Not paginating list endpoints | DRF | Memory OOM, slow | Always paginate unless strong reason not to |
| Cache without invalidation | DRF + Redis | Stale responses | `TAsk_acks_late` pattern + TTL + manual invalidation |
| Running as root in containers | Docker | Security risk | Non-root user (`appuser`/`nextjs`) with `USER` directive |
| Single-stage Dockerfile | Docker | 800MB+ images | Multi-stage build with standalone output |
| `NEXT_PUBLIC_*` at runtime | Next.js + Docker | Missing env vars | Pass build-time vars via `--build-arg` only |
| Server-side cursors with PgBouncer | PostgreSQL + Django | Broken queries | `DISABLE_SERVER_SIDE_CURSORS = True` |

---

## 12. Security Checklist

| # | Item | Priority | Area |
|---|------|----------|------|
| 1 | `DEBUG=False` in production | Critical | Django |
| 2 | `SECRET_KEY` unique, rotated per env | Critical | Django |
| 3 | `ALLOWED_HOSTS` restricted | Critical | Django |
| 4 | `CORS_ALLOWED_ORIGINS` explicit | Critical | DRF |
| 5 | `SECURE_SSL_REDIRECT = True` | High | Django |
| 6 | `SECURE_HSTS_SECONDS = 31536000` | High | Django |
| 7 | `SESSION_COOKIE_SECURE = True` | High | Django |
| 8 | `CSRF_COOKIE_SECURE = True` | High | Django |
| 9 | Non-root user in Docker containers | High | Docker |
| 10 | Health checks on all services | Medium | Docker |
| 11 | Signed media URLs for paywalled content | Medium | Django |
| 12 | Celery task input validation | Medium | Celery |
| 13 | Rate limiting on auth endpoints | Medium | DRF/NGINX |
| 14 | Firewall: only ports 22, 80, 443 | High | Infrastructure |
| 15 | SSH key-based auth only | Critical | Infrastructure |
| 16 | Let's Encrypt SSL (auto-renew) | Critical | Nginx |
| 17 | Sentry error tracking (optional) | Medium | Django |
| 18 | `retry_jitter=True` to prevent thundering herd | Medium | Celery |

---

## 13. Sources

| # | Title | URL | Type |
|---|-------|-----|------|
| 1 | Building a FullStack with Django, DRF & Next.js | <https://dev.to/koladev/building-a-fullstack-application-with-django-django-rest-nextjs-3e26> | Tutorial |
| 2 | Architecture Advice for DRF + Next.js | <https://forum.djangoproject.com/t/architecture-advice-for-research-portal-drf-next-js/42808> | Forum Discussion |
| 3 | Optimize DRF APIs for Performance | <https://www.freecodecamp.org/news/how-to-optimize-django-rest-apis-for-performance/> | Guide |
| 4 | DRF Caching with JSONField | <https://www.screamingatmyscreen.com/caching-and-django-rest-framework> | Blog Post |
| 5 | Celery + Django in Production | <https://medium.com/@mmoznu/celery-and-django-in-production-the-patterns-that-actually-hold-up-under-real-load-2974fe3fb481> | Production Patterns |
| 6 | Scrapy Architecture & Best Practices 2026 | <https://groupbwt.com/blog/scrapy-tutorial> | Tutorial |
| 7 | Deploy DRF to Production with Docker | <https://www.bhusalmanish.com.np/blog/posts/deploy-drf-production.html> | Deployment Guide |
| 8 | drf-spectacular Client Generation Docs | <https://drf-spectacular.readthedocs.io/en/latest/client_generation.html> | Documentation |
| 9 | drf-spectacular GitHub | <https://github.com/tfranzel/drf-spectacular> | Open Source |
| 10 | Dockerizing Next.js Application 2025 | <https://frontendworld.substack.com/p/dockerizing-a-nextjs-application> | Guide |
| 11 | Next.js Standalone Mode & Docker | <https://javascript.plainenglish.io/next-js-15-self-hosting-with-docker-complete-guide-0826e15236da> | Guide |
| 12 | Tailwind CSS 2026 Guide | <https://blog.logrocket.com/tailwind-css-guide> | Reference |
| 13 | Tailwind v4 Upgrade Guide | <https://tailwindcss.com/docs/upgrade-guide> | Official Docs |
| 14 | Tailwind v4 Migration Discussion | <https://github.com/tailwindlabs/tailwindcss/discussions/16517> | GitHub Discussion |
| 15 | 26 Selenium Best Practices | <https://www.browserstack.com/guide/best-practices-in-selenium-automation> | Guide |
| 16 | PgBouncer + Django Configuration | <https://forum.djangoproject.com/t/configure-pgbouncer-with-django/43161> | Forum Discussion |
| 17 | Celery + Scrapy Integration | <https://stackoverflow.com/questions/77053237> | Stack Overflow |
| 18 | API Client Generation with drf-spectacular | <https://www.youtube.com/watch?v=Rq3Y7-tPmmA> | Video Talk |
| 19 | Next.js Official Deployment Docs | <https://nextjs.org/docs/app/getting-started/deploying> | Official Docs |
| 20 | Dockerizing Django with Postgres, Gunicorn, Nginx | <https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx> | Tutorial |

---

## Synthesis

This dual-stack platform (Django/DRF + Next.js/React) is a mature, well-documented architecture pattern in 2026. The three highest-impact actions for this project are:

1. **OpenAPI-driven type safety** — drf-spectacular with `COMPONENT_SPLIT_REQUEST=True` and CI validation prevents the #1 risk (API field drift) and enables automatic TypeScript client generation.

2. **Celery queue separation** — Split tasks into critical/default/bulk queues with dedicated workers. This single architectural decision eliminates the most common production Celery complaint.

3. **Multi-stage Docker builds** — Both Django (multi-stage builder/runtime) and Next.js (standalone output) can achieve 70-80% image size reduction with proper layering, non-root users, and health checks.

The scraping pipeline (Scrapy → Celery → Django) has well-known integration pitfalls — particularly Scrapy's non-restartable reactor when used as a Celery task — which need explicit handling with `CrawlerRunner` and `stop_after_crawl=True`.

--- 

*Report generated 2026-07-16 from 10 web searches and 10+ extracted pages.*
