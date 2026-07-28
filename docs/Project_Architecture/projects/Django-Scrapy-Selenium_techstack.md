# 🏗 Technology Stack Blueprint - Django-Scrapy-Selenium

**Project Path:** `projects/Django-Scrapy-Selenium`
**Generated:** 2026-07-28
**Status:** Consolidation Target (scraping moved to rhixecompany-comics)

---

## Architecture Overview

**Pattern:** Full-stack dual-stack (Django backend + Node.js frontend/tooling)
**Components:**
- Django 4.x + DRF backend API
- Scrapy spiders for structured scraping
- Selenium WebDriver for JavaScript-heavy sites
- Celery + Redis for async task processing
- Alpine.js + Tailwind (daisyUI) frontend dashboard
- Webpack + Babel for JS bundling

---

## Backend Stack (Python/Django)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Django | 4.x | BSD |
| **API** | Django REST Framework | 3.15+ | MIT |
| **Language** | Python | 3.12 | PSF |
| **Scraping** | Scrapy | ^2.11 | BSD |
| **Browser Automation** | Selenium WebDriver | ^4.20 | Apache 2.0 |
| **HTML Parsing** | BeautifulSoup4 | Latest | MIT |
| **Async Tasks** | Celery | ^5.3 | BSD |
| **Message Broker** | Redis | ^5.0 | BSD |
| **Database** | PostgreSQL (prod) / SQLite (dev) | Latest | PostgreSQL |
| **WSGI** | Gunicorn | ^22.0 | MIT |
| **Static Files** | WhiteNoise | ^6.6 | MIT |
| **Env Config** | python-dotenv | ^1.0 | BSD |

### Python Quality Tools (`pyproject.toml`)
| Tool | Version | Config |
|------|---------|--------|
| **pytest** | Latest | Django test settings, coverage |
| **mypy** | Latest | Django plugin, strict |
| **djLint** | Latest | Django/Jinja templates |
| **ruff** | Latest | Comprehensive lint (F,E,W,C90,I,N,UP,YTT,ASYNC,S,BLE,FBT,B,A,COM,C4,DTZ,T10,DJ,EM,EXE,FA,ISC,ICN,G,INP,PIE,T20,PYI,PT,Q,RSE,RET,SLF,SLOT,SIM,TID,TCH,INT,PTH,ERA,PD,PGH,PL,TRY,FLY,PERF,RUF) |

---

## Frontend Stack (Node.js/TypeScript)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Runtime** | Node.js | ^22.13 | MIT |
| **Language** | TypeScript | ^5.4.5 | Apache 2.0 |
| **Framework** | Alpine.js | ^3.14 | MIT |
| **UI Kit** | daisyUI | ^4.12 | MIT |
| **CSS** | Tailwind CSS | ^3.4 | MIT |
| **Bundler** | Webpack | ^5.82 | MIT |
| **Transpiler** | Babel | ^7.16 | MIT |
| **CSS Processing** | PostCSS + PostCSS Preset Env | ^8.5 / ^10.0 | MIT |
| **Sass** | Dart Sass | ^1.77 | MIT |

### Frontend Dependencies
```json
{
  "dependencies": {
    "@alpinejs/collapse": "^3.14.3",
    "@alpinejs/focus": "^3.14.3",
    "@alpinejs/mask": "^3.14.3",
    "@alpinejs/morph": "^3.14.3",
    "@alpinejs/persist": "^3.14.3",
    "alpinejs": "^3.14.8",
    "axios": "^1.7.7",
    "flowbite-datepicker": "^1.3.2",
    "highlight.js": "^11.10.0",
    "htmx.org": "^1.9.12",
    "hyperscript.org": "^0.9.13",
    "jquery": "^3.7.1",
    "select2": "^4.1.0-rc.0",
    "sortablejs": "^1.15.3",
    "sweetalert2": "^11.6.14",
    "tw-elements": "^2.0.0"
  }
}
```

### Frontend Dev Dependencies
```json
{
  "devDependencies": {
    "@babel/core": "^7.16.5",
    "@babel/preset-env": "^7.16.5",
    "@fortawesome/fontawesome-free": "^6.5.2",
    "@popperjs/core": "^2.11.8",
    "@types/alpinejs": "^3.13.10",
    "@types/jquery": "^3.5.30",
    "@types/select2": "^4.0.63",
    "@types/sortablejs": "^1.15.8",
    "@typescript-eslint/eslint-plugin": "^5.62.0",
    "@typescript-eslint/parser": "^5.62.0",
    "autoprefixer": "^10.4.20",
    "babel-loader": "^9.1.2",
    "cross-env": "^7.0.3",
    "css-loader": "^7.1.2",
    "css-minimizer-webpack-plugin": "^7.0.0",
    "daisyui": "^4.12.23",
    "eslint": "^8.57.1",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-import": "^2.31.0",
    "file-loader": "^6.2.0",
    "flowbite": "^2.5.2",
    "flowbite-typography": "^1.0.3",
    "mini-css-extract-plugin": "^2.4.5",
    "node-sass-tilde-importer": "^1.0.2",
    "pixrem": "^5.0.0",
    "postcss": "^8.5.1",
    "postcss-import": "^16.1.0",
    "postcss-loader": "^8.1.1",
    "postcss-nested": "^7.0.2",
    "postcss-nesting": "^13.0.1",
    "postcss-preset-env": "^10.0.3",
    "postcss-simple-vars": "^7.0.1",
    "prettier": "^3.3.2",
    "prettier-plugin-tailwindcss": "^0.6.5",
    "resolve-url-loader": "^5.0.0",
    "rimraf": "^5.0.7",
    "sass": "1.77.6",
    "sass-loader": "^16.0.1",
    "source-map-loader": "^5.0.0",
    "style-loader": "^4.0.0",
    "tailwindcss": "^3.4.17",
    "ts-loader": "^9.5.1",
    "tsconfig-paths-webpack-plugin": "^4.2.0",
    "typescript": "^5.4.5",
    "url-loader": "^4.1.1",
    "webpack": "^5.82.0",
    "webpack-bundle-tracker": "^3.0.1",
    "webpack-cli": "^6.0.1",
    "webpack-dev-server": "^5.0.2",
    "webpack-merge": "^6.0.1"
  }
}
```

---

## Project Structure

```
Django-Scrapy-Selenium/
├── config/                    # Django settings
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   └── celery.py             # Celery config
├── apps/                      # Django apps
│   ├── core/                 # Core functionality
│   ├── scraping/             # Scrapy + Selenium integration
│   └── dashboard/            # Frontend dashboard app
├── scraping/                  # Scrapy project
│   ├── spiders/              # Scrapy spiders
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── frontend/                  # Node.js frontend
│   ├── src/
│   │   ├── js/               # TypeScript/JS source
│   │   ├── scss/             # Styles
│   │   └── templates/        # HTML templates
│   ├── webpack/
│   │   ├── dev.config.js
│   │   └── prod.config.js
│   ├── package.json
│   └── tsconfig.json
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── pyproject.toml            # Python tool config
├── requirements.txt          # Production deps
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
└── manage.py
```

---

## Scraping Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│   Celery Beat   │────▶│  Celery      │────▶│   Scrapy    │
│  (Scheduler)    │     │  Worker      │     │  Spider     │
└─────────────────┘     └──────┬───────┘     └──────┬──────┘
                               │                    │
                               ▼                    ▼
                        ┌──────────────┐     ┌─────────────┐
                        │    Redis     │     │  Selenium   │
                        │   (Broker)   │     │  WebDriver  │
                        └──────────────┘     └─────────────┘
                               │                    │
                               ▼                    ▼
                        ┌──────────────┐     ┌─────────────┐
                        │  PostgreSQL  │     │  Beautiful  │
                        │   (Results)  │     │   Soup 4    │
                        └──────────────┘     └─────────────┘
```

### Scraping Strategies

| Strategy | Tool | Use Case |
|----------|------|----------|
| **Static HTML** | Scrapy | Fast, structured sites |
| **JavaScript-rendered** | Selenium WebDriver | SPAs, dynamic content |
| **Hybrid** | Scrapy + Selenium middleware | Complex sites |
| **API endpoints** | Direct HTTP (axios/requests) | When available |

---

## Key Scripts

### Backend
```bash
# Install deps
pip install -r requirements/local.txt

# Django
python manage.py migrate
python manage.py runserver

# Celery
celery -A config worker -l info
celery -A config beat -l info

# Scrapy
scrapy crawl spider_name

# Quality
pytest
ruff check .
mypy .
djlint .
```

### Frontend
```bash
cd frontend
npm install

# Dev
npm run dev          # webpack serve

# Build
npm run build        # production bundle

# Format
npm run format
npm run format:check
```

---

## Configuration Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | pytest, mypy, djLint, ruff, coverage |
| `requirements/base.txt` | Shared Python deps |
| `requirements/local.txt` | Dev deps (includes base) |
| `requirements/production.txt` | Prod deps (includes base) |
| `frontend/package.json` | Node deps & scripts |
| `frontend/tsconfig.json` | TypeScript config |
| `frontend/webpack/*.config.js` | Webpack configs |
| `config/settings/*.py` | Django settings per env |
| `scrapy/settings.py` | Scrapy settings |

---

## CI/CD

**Workflow:** `.github/workflows/django-scrapy-selenium-ci.yml`

1. **Python**: Install → Ruff → MyPy → djLint → pytest
2. **Node**: Install → TypeScript check → ESLint → Build
3. **Integration**: Django + Scrapy + Selenium test run
4. **Docker**: Build verification

---

## License Summary

| Component | License |
|-----------|---------|
| Django/DRF | BSD / MIT |
| Scrapy | BSD |
| Selenium | Apache 2.0 |
| Celery | BSD |
| Alpine.js/daisyUI/Tailwind | MIT |
| Webpack/Babel/PostCSS | MIT |
| All Python tooling | MIT / BSD |

---

## Consolidation Notes

**Status:** This project is a consolidation target.
- Scraping functionality moved to `rhixecompany-comics/backend/`
- Django-Scrapy-Selenium serves as reference implementation
- New scraping work should use rhixecompany-comics stack

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*