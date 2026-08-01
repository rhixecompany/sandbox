# 🏗 Technology Stack Blueprint

**Workspace:** `C:\Users\Alexa\Desktop\SandBox`
**Generated:** 2026-07-28
**Depth:** Comprehensive
**Output Format:** Markdown
**Categorization:** Technology Type × Layer

---

## 1. Technology Identification Phase

### 1.1 Languages Detected

| Language       | Version(s)                                         | Projects Using                       | File Extensions               |
| -------------- | -------------------------------------------------- | ------------------------------------ | ----------------------------- |
| **TypeScript** | 5.9 (root), 6.0 (Banking), 5.x (most projects)     | All JS/TS projects                   | `.ts`, `.tsx`, `.mts`, `.cts` |
| **JavaScript** | ES2024 (ESNext modules)                            | Legacy/webpack projects              | `.js`, `.jsx`, `.mjs`, `.cjs` |
| **Python**     | 3.11 (root), 3.12 (Django projects), 3.10 (legacy) | Django projects, scripts, automation | `.py`, `.pyi`                 |
| **Bash**       | POSIX                                              | .github/workflows, scripts           | `.sh`                         |
| **PowerShell** | 5.1+                                               | Windows automation                   | `.ps1`                        |
| **Go**         | Latest (go.mod)                                    | mcp-servers/go                       | `.go`                         |
| **Rust**       | Latest (Cargo.toml)                                | mcp-servers/rust                     | `.rs`                         |
| **Java**       | 17+ (pom.xml)                                      | mcp-servers/java                     | `.java`                       |
| **Kotlin**     | Latest (build.gradle.kts)                          | mcp-servers/kotlin                   | `.kt`                         |
| **PHP**        | 8.x (composer.json)                                | mcp-servers/php                      | `.php`                        |

### 1.2 Runtimes & Package Managers

| Runtime/Manager | Version          | Usage                                                                           |
| --------------- | ---------------- | ------------------------------------------------------------------------------- |
| **Bun**         | 1.3.14           | Primary runtime & package manager (Banking, Bash, Resume_maker, root)           |
| **Node.js**     | 18+ / 22         | Legacy projects (xamehi, selenium_webdriver, Django-Scrapy-Selenium, comicwise) |
| **pnpm**        | 9.12.3           | comicwise project                                                               |
| **npm**         | Latest (bundled) | Legacy JS projects                                                              |
| **pip**         | Latest (bundled) | Python dependency management                                                    |
| **uv**          | Latest           | Alternative Python package management                                           |

---

## 2. Core Technologies Analysis

### 2.1 TypeScript / Bun Stack (Primary)

#### TypeScript Configuration (Root)

| Setting                      | Value            |
| ---------------------------- | ---------------- |
| **target**                   | `ESNext`         |
| **module**                   | `Preserve` (ESM) |
| **moduleResolution**         | `bundler`        |
| **strict**                   | `true`           |
| **jsx**                      | `react-jsx`      |
| **skipLibCheck**             | `true`           |
| **noUncheckedIndexedAccess** | `true`           |
| **noImplicitOverride**       | `true`           |
| **verbatimModuleSyntax**     | `true`           |
| **noEmit**                   | `true`           |

#### Key npm/Bun Dependencies (Workspace Root)

| Package             | Version         | Type   |
| ------------------- | --------------- | ------ |
| `@types/bun`        | 1.3.14 (latest) | dev    |
| `typescript`        | ^5.9.3          | peer   |
| `typescript` (root) | 5.9.3           | pinned |

### 2.2 Python Stack

#### Python Configuration (Root)

| Setting          | Value                       |
| ---------------- | --------------------------- |
| **Version**      | 3.11 (pyrightconfig.json)   |
| **Linter**       | Ruff 0.15.10 (`.ruff.toml`) |
| **Type Checker** | Pyright (basic mode)        |
| **Line Length**  | 120                         |
| **Quote Style**  | Double quotes               |

#### Python Dependencies Categorized (Root `requirements.txt`)

| Category           | Key Packages                                                           | Versions                          |
| ------------------ | ---------------------------------------------------------------------- | --------------------------------- |
| **AI/LLM SDKs**    | `anthropic`, `openai`                                                  | 0.87.0, 2.24.0                    |
| **Web Framework**  | `fastapi`, `starlette`, `uvicorn`, `httptools`                         | 0.139.0, 1.3.1, 0.51.0, 0.8.0     |
| **MCP Protocol**   | `mcp`                                                                  | 1.28.1                            |
| **HTTP Clients**   | `httpx`, `httpx-sse`, `requests`, `aiohttp`                            | 0.28.1, 0.4.3, 2.33.0, 3.14.1     |
| **Cloud SDKs**     | `boto3`, `botocore`, `google-api-python-client`, `google-auth`         | 1.42.89, 1.42.97, 2.194.0, 2.55.1 |
| **Chat/Messaging** | `discord-py`, `slack-bolt`, `slack-sdk`, `python-telegram-bot`         | 2.7.1, 1.27.0, 3.40.1, 22.6       |
| **MS Teams**       | `microsoft-teams-api`, `microsoft-teams-apps`, `microsoft-teams-cards` | 2.0.13.4                          |
| **Auth**           | `msal`, `oauthlib`, `pyjwt`, `google-auth-oauthlib`                    | 1.37.0, 3.3.1, 2.13.0, 1.3.1      |
| **Validation**     | `pydantic`, `pydantic-core`, `pydantic-settings`                       | 2.13.4, 2.46.4, 2.14.2            |
| **Data**           | `youtube-transcript-api`, `pillow`, `tabulate`, `tqdm`                 | 1.2.4, 12.3.0, 0.10.0, 4.68.4     |
| **Testing**        | `pytest`, `pytest-asyncio`                                             | 9.0.3, 1.3.0                      |
| **Dev Tooling**    | `ruff`                                                                 | 0.15.10                           |

#### Root Hermes Agent Dependency

- `hermes-agent` installed as editable (`file:///C:/Users/Alexa/AppData/Local/hermes/hermes-agent`)

### 2.3 Frontend Frameworks

| Framework        | Version          | Projects                                      | Features                        |
| ---------------- | ---------------- | --------------------------------------------- | ------------------------------- |
| **Next.js**      | 16.2.4           | Banking, rhixecompany-comics (frontend)       | App Router, React 19, Turbopack |
| **Next.js**      | 15.x (15.3-15.4) | comicwise, rhixe_scans, university-libary-jsm | App Router, React 19            |
| **React**        | 19.x             | All Next.js projects                          | Server Components, Hooks        |
| **React**        | 18.2             | xamehi (CRA)                                  | Legacy CRA                      |
| **React**        | 17.x             | xamehi.tv (CRA)                               | Legacy CRA, Material-UI 4       |
| **Tailwind CSS** | v3/v4            | All Next.js projects                          | Utility-first CSS               |
| **Radix UI**     | Latest           | Banking, rhixe_scans, university-libary-jsm   | Headless UI primitives          |
| **shadcn/ui**    | ^4               | Various                                       | Component library on Radix      |
| **daisyUI**      | ^4.12            | Django-Scrapy-Selenium                        | Tailwind component library      |
| **Alpine.js**    | ^3.14            | Django-Scrapy-Selenium                        | Lightweight JS framework        |

### 2.4 Backend Frameworks & APIs

| Framework                 | Version      | Projects                                               |
| ------------------------- | ------------ | ------------------------------------------------------ |
| **Django**                | 5.x          | rhixecompany-comics                                    |
| **Django**                | 4.x          | profile                                                |
| **Django**                | 3.1          | ecom                                                   |
| **Django REST Framework** | 3.13+        | ecom, xamehi, xamehi.tv, rhixecompany-comics           |
| **Django REST Framework** | 3.15+        | rhixecompany-comics                                    |
| **Express.js**            | ^4.18        | xamehi                                                 |
| **FastAPI**               | 0.139.0      | Root automation services                               |
| **Drizzle ORM**           | 0.44-0.45    | Banking, university-libary-jsm                         |
| **Prisma**                | 6.x / Latest | comicwise, rhixe_scans, rhixecompany-comics            |
| **NextAuth.js**           | v4/v5        | Banking, comicwise, rhixe_scans, university-libary-jsm |
| **Auth.js**               | v5           | rhixe_scans                                            |

### 2.5 Databases & Storage

| Technology               | Version    | Projects                                                | Purpose                                  |
| ------------------------ | ---------- | ------------------------------------------------------- | ---------------------------------------- |
| **PostgreSQL**           | Latest     | All Django/Next.js apps                                 | Primary database                         |
| **Neon**                 | Serverless | university-libary-jsm                                   | Serverless PostgreSQL                    |
| **SQLite**               | Recent     | Dev environments                                        | Lightweight dev DB                       |
| **Redis**                | Latest     | rhixe_scans, university-libary-jsm, rhixecompany-comics | Caching, sessions, Celery broker         |
| **Upstash Redis**        | ^1.37      | Banking, comicwise, university-libary-jsm               | Serverless Redis (QStash, Rate Limiting) |
| **Google Cloud Storage** | -          | profile                                                 | Media file storage                       |
| **UploadThing**          | ^7         | rhixe_scans                                             | File upload service                      |
| **ImageKit**             | ^6         | comicwise, university-libary-jsm                        | Image optimization, CDN                  |
| **Cloudinary**           | ^2.9       | comicwise                                               | Image hosting                            |

### 2.6 Payment / Fintech

| Service    | Projects                                    | Integration                   |
| ---------- | ------------------------------------------- | ----------------------------- |
| **Plaid**  | Banking                                     | Account linking, transactions |
| **Dwolla** | Banking                                     | ACH transfers                 |
| **Stripe** | comicwise, rhixe_scans, rhixecompany-comics | Subscriptions, payments       |
| **PayPal** | rhixe_scans, xamehi.tv, ecom                | Payment processing            |

### 2.7 MCP Server Ecosystem

| Server                    | SDK/Implementation   | Purpose                         |
| ------------------------- | -------------------- | ------------------------------- |
| **ast-grep**              | ast-grep-rs          | AST-based code search & replace |
| **code-sandbox**          | Node.js Docker       | Isolated code execution         |
| **fetch**                 | Python               | Web page content extraction     |
| **filesystem**            | Python               | Sandboxed file operations       |
| **github**                | Python               | GitHub API operations           |
| **memory**                | Python               | Persistent agent memory         |
| **playwright**            | Node.js              | Browser automation              |
| **sequential-thinking**   | TypeScript           | Structured reasoning            |
| **mcp-docker**            | Go                   | Container management            |
| **tooling-config**        | Python               | Pre-commit, git-cliff           |
| **tooling-lint**          | Python               | ESLint, Prettier, markdownlint  |
| **python-quality**        | Python               | Ruff + Pyright integration      |
| **mindstudio**            | Cloud                | Multi-modal AI tools            |
| **smithery**              | Cloud                | MCP registry                    |
| **linear**                | Cloud                | Project management              |
| **mcp-server-typescript** | TypeScript (SDK 1.8) | Reference implementation        |

---

## 3. Per-Project Technology Stack Analysis

### 3.1 Banking (`projects/Banking`)

| Category            | Technology                | Version      | License    |
| ------------------- | ------------------------- | ------------ | ---------- |
| **Runtime**         | Node.js                   | 18+          | MIT        |
| **Package Manager** | Bun                       | 1.3.14       | MIT        |
| **Framework**       | Next.js                   | 16.2.4       | MIT        |
| **Language**        | TypeScript                | 6.0.3        | Apache 2.0 |
| **UI Library**      | React                     | 19.2.5       | MIT        |
| **ORM**             | Drizzle ORM               | 0.45.2       | Apache 2.0 |
| **Database**        | PostgreSQL                | Latest       | PostgreSQL |
| **Auth**            | NextAuth.js               | ^4.24.14     | ISC        |
| **Payments**        | Plaid + Dwolla            | ^42.2 / ^3.4 | MIT        |
| **Styling**         | Tailwind CSS              | 4.2.4        | MIT        |
| **State Mgt**       | Zustand                   | ^5.0.12      | MIT        |
| **UI Components**   | Radix UI / shadcn/ui      | Latest       | MIT        |
| **Form Validation** | react-hook-form + zod     | ^7.75 / ^4.4 | MIT        |
| **Charts**          | Chart.js + recharts       | ^4.5 / 3.8   | MIT        |
| **Email**           | nodemailer                | ^8.0         | MIT        |
| **Rate Limiting**   | Upstash Redis + Ratelimit | ^1.37 / ^2.0 | MIT        |
| **Table**           | TanStack React Table      | ^8.21        | MIT        |
| **DnD**             | dnd-kit                   | ^6.3         | MIT        |
| **Testing**         | Vitest + Playwright       | ^4.1 / ^1.59 | MIT        |
| **Linting**         | ESLint 10 + Prettier 3    | ^10.3 / ^3.8 | MIT        |
| **Security**        | bcrypt, zxcvbn-ts         | ^6.0 / ^3.0  | MIT        |
| **Deploy**          | Docker + Vercel           | Latest       | -          |

**Dependencies:** ~140 packages (80 prod + 60 dev) | **Package Manager:** Bun | **Lockfile:** bun.lock (via bun install)

---

### 3.2 Bash (`projects/Bash`)

| Category            | Technology                           | Version      | License    |
| ------------------- | ------------------------------------ | ------------ | ---------- |
| **Runtime**         | Node.js                              | 18+          | MIT        |
| **Package Manager** | Bun                                  | 1.3.14       | MIT        |
| **Language**        | TypeScript (strict)                  | Latest       | Apache 2.0 |
| **Linting**         | ESLint 10 + Prettier 3               | ^10.4 / ^3.8 | MIT        |
| **Testing**         | Vitest                               | ^4.1         | MIT        |
| **Shell**           | Bash + PowerShell 5.1+               | -            | -          |
| **YAML**            | yaml                                 | ^2.9         | ISC        |
| **Validation**      | zod                                  | ^4.4         | MIT        |
| **CI**              | GitHub Actions (bash-scripts-ci.yml) | -            | -          |

**Dependencies:** ~70 dev packages | **Package Manager:** Bun | **Lockfile:** bun.lock

---

### 3.3 comicwise (`projects/comicwise`)

| Category            | Technology                | Version       | License    |
| ------------------- | ------------------------- | ------------- | ---------- |
| **Runtime**         | Node.js                   | 18+           | MIT        |
| **Package Manager** | pnpm                      | 9.12.3        | MIT        |
| **Framework**       | Next.js                   | 16.1.6        | MIT        |
| **Language**        | TypeScript                | ^5.9.3        | Apache 2.0 |
| **UI Library**      | React                     | 19.2.4        | MIT        |
| **ORM**             | Drizzle ORM               | 0.45.1        | Apache 2.0 |
| **Database**        | PostgreSQL                | Latest        | PostgreSQL |
| **Auth**            | NextAuth.js v5 (beta)     | 5.0.0-beta.30 | ISC        |
| **Payments**        | Stripe                    | ^18.2         | MIT        |
| **Media**           | ImageKit, Cloudinary      | ^6.0 / ^2.9   | MIT        |
| **State Mgt**       | Zustand + TanStack Query  | ^5.0 / ^5.90  | MIT        |
| **Styling**         | Tailwind CSS v4           | ^4            | MIT        |
| **UI Kit**          | Radix UI / shadcn/ui      | Latest        | MIT        |
| **Animation**       | Framer Motion             | ^12.36        | MIT        |
| **Real-time**       | Upstash QStash / Workflow | ^2.9 / ^1.1   | MIT        |
| **Email**           | nodemailer + Resend       | ^8.0 / ^4.6   | MIT        |
| **Charts**          | recharts                  | 3.8.0         | MIT        |
| **Testing**         | Vitest + Playwright       | ^4.1 / ^1.58  | MIT        |
| **Linting**         | ESLint 9 + Prettier 3     | ^9.0 / ^3.8   | MIT        |

**Dependencies:** ~160 packages (100 prod + 60 dev) | **Package Manager:** pnpm | **Lockfile:** pnpm-lock.yaml

---

### 3.4 cookiecutter-django-tailwind (`projects/cookiecutter-django-tailwind`)

| Category      | Technology                                    | Version | License |
| ------------- | --------------------------------------------- | ------- | ------- |
| **Language**  | Python                                        | 3.12+   | PSF     |
| **Framework** | Django                                        | 5.x     | BSD     |
| **Template**  | Cookiecutter                                  | 2.6.0   | BSD     |
| **Frontend**  | django-tailwind + Alpine.js/htmx              | Latest  | MIT     |
| **Styling**   | Tailwind CSS                                  | v3/v4   | MIT     |
| **Database**  | PostgreSQL (prod) / SQLite (dev)              | Latest  | -       |
| **Infra**     | Docker Compose, Gunicorn, WhiteNoise, Sentry  | Latest  | MIT     |
| **Quality**   | pytest, pre-commit, Black, ruff, mypy, djlint | Latest  | MIT     |
| **CI**        | tox                                           | ^4.16   | MIT     |

**Type:** Cookiecutter template (generates Django projects) | **Not run directly**

---

### 3.5 Django-Scrapy-Selenium (`projects/Django-Scrapy-Selenium`)

| Category       | Technology                                   | Version              | License      |
| -------------- | -------------------------------------------- | -------------------- | ------------ |
| **Backend**    | Django + DRF                                 | 4.x / 3.15+          | BSD / MIT    |
| **Language**   | Python                                       | 3.12                 | PSF          |
| **Scraping**   | Scrapy + Selenium WebDriver + BeautifulSoup4 | ^2.11 / ^4.20        | BSD / Apache |
| **Async**      | Celery + Redis                               | ^5.3 / ^5.0          | BSD / MIT    |
| **Database**   | PostgreSQL (prod) / SQLite (dev)             | Latest               | -            |
| **Infra**      | Docker Compose, Gunicorn                     | Latest               | MIT          |
| **Frontend**   | Alpine.js + daisyUI (Tailwind)               | ^3.14 / ^4.12        | MIT          |
| **JS Build**   | Webpack + Babel + PostCSS                    | ^5.82 / ^7.16 / ^8.5 | MIT          |
| **Linting**    | ESLint 8 + Prettier + ruff                   | ^8.57 / ^3.3 / 0.5   | MIT          |
| **Type Check** | mypy                                         | Latest               | MIT          |
| **Node**       | Node.js                                      | ^22.13               | MIT          |

**Status:** Consolidation target — scraping moved to rhixecompany-comics | **Complexity:** High (dual-stack)

---

### 3.6 ecom (`projects/ecom`)

| Category     | Technology                     | Version | License    |
| ------------ | ------------------------------ | ------- | ---------- |
| **Backend**  | Django 3.1 + DRF 3.13          | 3.1.14  | BSD        |
| **Language** | Python                         | 3.10    | PSF        |
| **Database** | PostgreSQL                     | Latest  | PostgreSQL |
| **Payments** | PayPal                         | Latest  | -          |
| **Frontend** | React + Redux Toolkit          | Latest  | MIT        |
| **Infra**    | Gunicorn, WhiteNoise, boto3/S3 | Latest  | MIT        |
| **Auth**     | SimpleJWT                      | 5.2.0   | MIT        |
| **Storage**  | django-storages + S3           | ^1.12   | MIT        |
| **Admin**    | django-ckeditor                | ^6.3    | BSD        |

**Status:** Maintenance mode (legacy) | **Dual-stack:** Backend (`backend/`) + Frontend (`frontend/`)

---

### 3.7 profile (`projects/profile`)

| Category          | Technology                 | Version | License    |
| ----------------- | -------------------------- | ------- | ---------- |
| **Backend**       | Django                     | 4.x     | BSD        |
| **Language**      | Python                     | 3.11+   | PSF        |
| **Database**      | PostgreSQL                 | Latest  | PostgreSQL |
| **Media Storage** | Google Cloud Storage (GCS) | -       | -          |
| **Editor**        | CKEditor 5                 | Latest  | GPL        |
| **Infra**         | Gunicorn, Docker + GCP     | Latest  | MIT        |
| **Styling**       | django-crispy-forms        | Latest  | MIT        |

**Status:** Maintenance | **Type:** Blog/CMS

---

### 3.8 Python-projects (`projects/Python-projects`)

| Category      | Technology                                                                     | Version              | License |
| ------------- | ------------------------------------------------------------------------------ | -------------------- | ------- |
| **Language**  | Python                                                                         | 3.x                  | PSF     |
| **Libraries** | beautifulsoup4, opencv-python, matplotlib, pillow, qrcode, numpy, PyDictionary | Latest               | Various |
| **Testing**   | pytest, mypy, ruff, black, coverage, pre-commit                                | ^8.3 / ^1.15 / ^0.11 | MIT     |
| **Type:**     | 18 standalone beginner Python scripts                                          | -                    | -       |

**Status:** Archive candidate | **No framework** — pure scripts

---

### 3.9 Resume_maker (`projects/Resume_maker`)

| Category           | Technology                      | Version              | License    |
| ------------------ | ------------------------------- | -------------------- | ---------- |
| **Runtime**        | Bun                             | 1.3.14+              | MIT        |
| **Language**       | TypeScript (strict)             | ^5                   | Apache 2.0 |
| **PDF Generation** | markdown-pdf                    | ^11.0                | BSD        |
| **Linting**        | ESLint 10 + Prettier 3 + cspell | ^10.3 / ^3.8 / ^10.0 | MIT        |
| **Markdown Lint**  | markdownlint-cli2               | ^0.22                | MIT        |
| **Type Check**     | tsc --noEmit                    | -                    | -          |
| **Format**         | JSON → Markdown → PDF           | -                    | -          |

**Type:** CLI tool | **Package Manager:** Bun | **Lockfile:** bun.lock

---

### 3.10 rhixe_scans (`projects/rhixe_scans`)

| Category        | Technology                  | Version                         | License    |
| --------------- | --------------------------- | ------------------------------- | ---------- |
| **Framework**   | Next.js                     | ^15.3.3                         | MIT        |
| **Language**    | TypeScript (strict)         | ^5                              | Apache 2.0 |
| **UI**          | React                       | ^19.1                           | MIT        |
| **ORM**         | Prisma                      | 6.10.0                          | Apache 2.0 |
| **Database**    | PostgreSQL                  | Latest                          | PostgreSQL |
| **Auth**        | NextAuth.js v5 (beta)       | ^5.0.0-beta.25                  | ISC        |
| **Payments**    | Stripe + PayPal             | ^18.2 / @paypal/react-paypal-js | MIT        |
| **Real-time**   | WebSocket (ws)              | ^8.18                           | MIT        |
| **File Upload** | UploadThing                 | ^7.7                            | MIT        |
| **Email**       | Resend                      | ^4.6                            | MIT        |
| **Styling**     | Tailwind CSS 3.x + Radix UI | ^3.4 / latest                   | MIT        |
| **State Mgt**   | Zustand, TanStack Table     | ^5.0 / ^8.21                    | MIT        |
| **Seo**         | next-sitemap                | ^4.2                            | MIT        |
| **Testing**     | Jest                        | ^30                             | MIT        |
| **Linting**     | ESLint 9 + Prettier 3       | ^9 / ^3.5                       | MIT        |

**Dependencies:** ~80 packages (60 prod + 20 dev) | **Package Manager:** npm | **Complexity:** High

---

### 3.11 rhixecompany-comics (`projects/rhixecompany-comics`)

| Category          | Technology                 | Version              | License            |
| ----------------- | -------------------------- | -------------------- | ------------------ |
| **Backend**       | Django 5.x + DRF 3.15+     | 5.x / 3.15+          | BSD / MIT          |
| **Frontend**      | Next.js 16 App Router      | 16.x                 | MIT                |
| **Language (BE)** | Python                     | 3.10+                | PSF                |
| **Language (FE)** | TypeScript (strict)        | ^5                   | Apache 2.0         |
| **ORM**           | Prisma (FE)                | Latest               | Apache 2.0         |
| **Scraping**      | Scrapy + Selenium + Celery | ^2.11 / ^4.20 / ^5.3 | BSD / Apache / MIT |
| **Async**         | Celery + Redis             | ^5.3 / ^5.0          | BSD / MIT          |
| **Database**      | PostgreSQL                 | Latest               | PostgreSQL         |
| **API Docs**      | drf-spectacular            | ^0.27                | MIT                |
| **Auth**          | SimpleJWT                  | ^5.3                 | MIT                |
| **Infra**         | Docker Compose, Gunicorn   | Latest               | MIT                |
| **Styling**       | Tailwind CSS + shadcn/ui   | Latest               | MIT                |

**Type:** Dual-stack (Django + Next.js) | **Status:** Active | **Complexity:** Very High

---

### 3.12 selenium_webdriver (`projects/selenium_webdriver`)

| Category       | Technology                 | Version | License    |
| -------------- | -------------------------- | ------- | ---------- |
| **Runtime**    | Node.js                    | 18+     | MIT        |
| **Language**   | JavaScript (ESM)           | ES2024  | -          |
| **Library**    | selenium-webdriver         | 4.34.0  | Apache 2.0 |
| **Formatting** | Prettier                   | ^3.6    | MIT        |
| **Type:**      | CLI scraper (comics/manga) | -       | -          |

**Status:** Active | **Dependencies:** 3 packages | **No build step**

---

### 3.13 university-libary-jsm (`projects/university-libary-jsm`)

| Category          | Technology                   | Version        | License    |
| ----------------- | ---------------------------- | -------------- | ---------- |
| **Framework**     | Next.js                      | 15.4.2         | MIT        |
| **Language**      | TypeScript (strict)          | ^5             | Apache 2.0 |
| **UI**            | React                        | 19.1.0         | MIT        |
| **ORM**           | Drizzle ORM                  | 0.44.3         | Apache 2.0 |
| **Database**      | PostgreSQL (Neon serverless) | Latest         | PostgreSQL |
| **Cache**         | Upstash Redis                | ^1.35          | MIT        |
| **Auth**          | NextAuth.js v5 (beta)        | ^5.0.0-beta.25 | ISC        |
| **Styling**       | Tailwind CSS v4              | ^4.1           | MIT        |
| **UI Components** | Radix UI / shadcn/ui         | Latest         | MIT        |
| **Charts**        | recharts                     | ^2.15          | MIT        |
| **Email**         | nodemailer                   | ^7.0           | MIT        |
| **Linting**       | ESLint 9 + Prettier 3        | ^9 / ^3.6      | MIT        |
| **Deploy**        | Vercel + Neon                | -              | -          |

**Dependencies:** ~60 packages (45 prod + 15 dev) | **Package Manager:** npm | **Lockfile:** package-lock.json

---

### 3.14 xamehi (`projects/xamehi`)

| Category      | Technology                | Version      | License    |
| ------------- | ------------------------- | ------------ | ---------- |
| **Backend 1** | Django + DRF              | 3.x / 3.13   | BSD / MIT  |
| **Backend 2** | Express.js                | ^4.18        | MIT        |
| **Frontend**  | React 18 (CRA)            | ^18.2        | MIT        |
| **Language**  | Python 3.10+ / JavaScript | -            | -          |
| **Database**  | PostgreSQL                | Latest       | PostgreSQL |
| **HTTP**      | Axios, cors               | ^0.27 / ^2.8 | MIT        |
| **Dev**       | Nodemon                   | ^2.0         | MIT        |
| **Testing**   | @testing-library/react    | ^13.3        | MIT        |

**Status:** Consolidation target (legacy) | **Pattern:** Three separate services

---

### 3.15 xamehi.tv (`projects/xamehi.tv`)

| Category     | Technology                     | Version       | License   |
| ------------ | ------------------------------ | ------------- | --------- |
| **Backend**  | Django + DRF                   | Latest        | BSD / MIT |
| **Frontend** | React 17 (CRA + Material-UI 4) | ^17 / ^4      | MIT       |
| **Auth**     | SimpleJWT + django-allauth     | ^5.3 / latest | MIT       |
| **Payments** | PayPal                         | Latest        | -         |
| **Media**    | video-react                    | Latest        | MIT       |
| **Infra**    | Gunicorn, WhiteNoise           | Latest        | MIT       |

**Status:** Active | **Pattern:** Dual-stack (DRF + CRA)

---

### 3.16 youtube-downloader (`projects/youtube-downloader`)

| Category      | Technology        | Version | License         |
| ------------- | ----------------- | ------- | --------------- |
| **Language**  | Python            | 3.x     | PSF             |
| **Libraries** | yt-dlp, curl_cffi | Latest  | Unlicense / MIT |
| **Linting**   | ruff, mypy        | Latest  | MIT             |
| **External**  | FFmpeg            | Latest  | GPL             |
| **Type:**     | CLI tool          | -       | -               |

**Status:** Active | **Pattern:** Single-file scripts | **License file included**

---

### 3.17 mcp-server-typescript (`projects/mcp-server-typescript`)

| Category       | Technology                            | Version | License    |
| -------------- | ------------------------------------- | ------- | ---------- |
| **Runtime**    | Node.js                               | Latest  | MIT        |
| **Language**   | TypeScript                            | ^5.8.3  | Apache 2.0 |
| **SDK**        | @modelcontextprotocol/sdk             | ^1.8.0  | MIT        |
| **Validation** | zod                                   | ^3.24   | MIT        |
| **Dev**        | tsx                                   | ^4.19   | MIT        |
| **Type:**      | MCP server (reference implementation) | -       | -          |

**Status:** Active | **Pattern:** TypeScript MCP server scaffold

---

## 4. Coding Conventions

### 4.1 Workspace-Wide Standards

| Convention               | Rule                                     |
| ------------------------ | ---------------------------------------- |
| **Line Endings**         | CRLF (`.editorconfig`, Windows host)     |
| **Indentation (TS/JS)**  | 2 spaces                                 |
| **Indentation (Python)** | 4 spaces                                 |
| **Indentation (YAML)**   | 2 spaces                                 |
| **Quotes (TS/JS)**       | Single quotes                            |
| **Quotes (Python)**      | Double quotes                            |
| **UTF-8**                | Required everywhere                      |
| **Trailing Whitespace**  | Trimmed                                  |
| **Final Newline**        | Required at EOF                          |
| **Backup Files**         | Forbidden (`.bak`, `.old`, `.backup`)    |
| **Secrets**              | Never committed (`.env` in `.gitignore`) |

### 4.2 TypeScript Conventions

| Rule                    | Standard                                                                    |
| ----------------------- | --------------------------------------------------------------------------- |
| **Strict Mode**         | `strict: true` with `noUncheckedIndexedAccess`, `noImplicitOverride`        |
| **No `any`**            | Banned (use `unknown` and narrow)                                           |
| **Module System**       | ESM (`"type": "module"`)                                                    |
| **No Emit**             | `noEmit: true` (Bun handles transpilation)                                  |
| **Path Aliases**        | `@/` maps to `src/`                                                         |
| **Naming (Components)** | PascalCase (`UserProfile.tsx`)                                              |
| **Naming (Hooks)**      | camelCase (`useAuth.ts`)                                                    |
| **Naming (Utils)**      | camelCase (`formatDate.ts`)                                                 |
| **Naming (Pages)**      | kebab-case (`user-profile/page.tsx`)                                        |
| **Validation**          | zod v4 for all API inputs                                                   |
| **Formatting**          | Prettier 3 (plugins: tailwindcss, organize-imports, packagejson, sort-json) |

### 4.3 React Conventions

| Rule                  | Standard                                                  |
| --------------------- | --------------------------------------------------------- |
| **Components**        | Function components only (no class components)            |
| **Default Export**    | Components default-exported from `page.tsx`               |
| **Server Components** | Default in App Router; Client Components only when needed |
| **State Management**  | Zustand (global), TanStack Query (server state)           |
| **Styling**           | `cn()` utility + CVA for variants                         |
| **Forms**             | react-hook-form + zod resolver                            |
| **Animations**        | Framer Motion (comicwise), embla-carousel (carousels)     |

### 4.4 Python Conventions

| Rule           | Standard                                                       |
| -------------- | -------------------------------------------------------------- |
| **Style**      | PEP 8                                                          |
| **Type Hints** | Required in all new code                                       |
| **Linting**    | Ruff (select: E, F, I, N, W, UP, B, SIM, ARG, RUF)             |
| **Formatting** | Ruff formatter (line-length: 120)                              |
| **Imports**    | isort-style (ruff lint I)                                      |
| **Naming**     | `snake_case` for variables/functions, `PascalCase` for classes |
| **Config**     | Settings hierarchy (base → local → production for Django)      |
| **ORM**        | Django ORM or SQLAlchemy depending on project                  |

### 4.5 Git & Branching Conventions

| Rule                | Standard                                                   |
| ------------------- | ---------------------------------------------------------- |
| **Branch Strategy** | `production` ← `staged` ← `development` ← `feature/*`      |
| **Branch Naming**   | `<type>/<project>/<kebab-case-description>`                |
| **Commit Format**   | Conventional commits: `<type>: <description>`              |
| **Types**           | `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf` |
| **Rebase**          | Prefer rebase over merge (linear history)                  |
| **PR Target**       | `development` (never `production` directly)                |
| **PR Size**         | <100 files recommended                                     |

### 4.6 Testing Conventions

| Stack                | Framework                       | Location                        | Pattern                     |
| -------------------- | ------------------------------- | ------------------------------- | --------------------------- |
| **TypeScript/Bun**   | Vitest                          | `**/*.test.ts` alongside source | Unit + component tests      |
| **React Components** | Vitest + @testing-library/react | `**/*.test.tsx`                 | Render, fire events, assert |
| **E2E**              | Playwright                      | `tests/` or `e2e/`              | Page-level flows            |
| **Python (Django)**  | pytest + pytest-django          | `tests/` per app                | Test DB, API clients        |
| **Python (scripts)** | pytest                          | `test_*.py` alongside           | Unit + integration          |
| **Shell**            | bash test scripts               | `tests/verify-dryrun.sh`        | Dry-run verification        |

### 4.7 CI/CD Conventions

| Convention             | Detail                                                                  |
| ---------------------- | ----------------------------------------------------------------------- |
| **PR Workflow**        | `pr-ci.yml` — detects changed projects, runs project-appropriate checks |
| **Type Check Gate**    | `tsc --noEmit` (TypeScript) or `pyright` (Python)                       |
| **Lint Gate**          | ESLint `--max-warnings=0` (strict) or `ruff check`                      |
| **Format Gate**        | Prettier `--check` or Ruff `format --check`                             |
| **Spell Gate**         | cspell + codespell                                                      |
| **No Forbidden Files** | Blocks `.env`, credentials, binaries                                    |
| **Deploy**             | Push to `production` triggers deployment workflows                      |

---

## 5. Dependency Map & Cross-Project Relationships

```
SandBox Root
├── .github/workflows/ ────────── CI/CD for ALL projects
│
├── projects/Banking/ ─────────── Next.js 16 + Drizzle ORM + Plaid/Dwolla
├── projects/Bash/ ────────────── Bun/TypeScript automation (6-phase orchestrator)
├── projects/comicwise/ ───────── Next.js 15 + Drizzle ORM + Stripe + pnpm
├── projects/cookiecutter-django-tailwind/ ── Template (not run directly)
├── projects/Django-Scrapy-Selenium/ ──────── Legacy — consolidating into rhixecompany-comics
├── projects/ecom/ ────────────── Legacy — Django 3.1 + DRF + React/Redux
├── projects/mcp-servers/ ─────── MCP examples (10 languages)
├── projects/mcp-server-typescript/ ── Reference MCP server (TypeScript SDK)
├── projects/profile/ ─────────── Django 4.x + GCS + CKEditor
├── projects/Python-projects/ ─── 18 standalone scripts
├── projects/Resume_maker/ ────── Bun CLI: JSON → Markdown → PDF
├── projects/rhixe_scans/ ─────── Next.js 15 + Prisma + WebSocket
├── projects/rhixecompany-comics/ ── Django 5 + Next.js 16 (dual-stack)
│   ├── backend/ ──────────────── Django + DRF + Celery + Scrapy
│   └── frontend/ ─────────────── Next.js 16 App Router
├── projects/selenium_webdriver/ ── Node.js + Selenium 4
├── projects/university-libary-jsm/ ── Next.js 15 + Drizzle + Neon + Redis
├── projects/xamehi/ ──────────── Django + Express + React 18 (legacy)
├── projects/xamehi.tv/ ───────── DRF + React 17 + Material-UI
└── projects/youtube-downloader/ ── Python + yt-dlp CLI
```

---

## 6. Technology Decision Context

### Key Architectural Decisions

1. **Bun as primary runtime** — Chosen for speed, TypeScript-native support, and built-in test runner/toolchain. Used across most active TypeScript projects.

2. **Drizzle vs Prisma** — Drizzle used in newer projects (Banking, university-libary-jsm) for its lighter footprint and SQL-like approach. Prisma retained in rhixe_scans/comicwise for mature GraphQL-like schema.

3. **Next.js 16 (App Router)** — Adopted for all new projects. React 19 Server Components reduce client JS bundle. Turbopack for dev.

4. **Tailwind CSS v4** — v4 adopted in newer projects (Banking) with CSS-first configuration. v3 retained in rhixe_scans.

5. **Dual-stack (Django + Next.js)** — rhixecompany-comics demonstrates hybrid approach: Django for backend/celery/scraping, Next.js for frontend/SSR.

6. **Monorepo with autonomy** — Each subproject is independently configurable with its own toolchain, CI pipeline, and AGENTS.md. Allows gradual migration without breaking other projects.

### Deprecated / Consolidation Targets

| Project                   | Reason                                | Replacement           |
| ------------------------- | ------------------------------------- | --------------------- |
| xamehi                    | Legacy architecture (3 services)      | Consolidation planned |
| ecom                      | Django 3.1 (end-of-life Python 3.10)  | Upgrade to Django 5.x |
| Django-Scrapy-Selenium    | Scraping moved to rhixecompany-comics | rhixecompany-comics   |
| Python-projects (partial) | 18 beginner scripts                   | Archive candidate     |

---

_Generated by Hermes Agent — Technology Stack Blueprint Generator_
