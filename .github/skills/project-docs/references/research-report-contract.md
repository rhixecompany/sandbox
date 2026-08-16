# RESEARCH_REPORT.md — Contract & Verification Recipe

## The contract (hard gate)
- **9+ `##` (H2) sections.** Below 9 fails.
- **Final on-disk size: 1024–5120 bytes (1 KB–5 KB).**
- Structure: H1 title → `>` blockquote (Type / Stack / Status / Updated) → `---` → `##` sections → trailing one-line methodology note.
- Methodology note format: `**Methodology:** N web queries + source extraction. <verified claims>.` (do NOT also keep a separate `### Research Methodology` footer block — it wastes ~150 bytes and pushes over the gate).

## Verification recipe (run after writing)
```bash
cd /c/Users/Alexa/Desktop/SandBox/projects
for f in profile rhixe_scans Python-projects selenium_webdriver rhixecompany-comics; do
  bytes=$(wc -c < $f/RESEARCH_REPORT.md)
  secs=$(grep -c '^## ' $f/RESEARCH_REPORT.md)
  printf "%-22s %5s bytes | %d sections\n" "$f" "$bytes" "$secs"
done
```
- If `bytes > 5120` but content looks fine → **CRLF bloat**. Normalize: `sed -i 's/\r$//' $f/RESEARCH_REPORT.md`. LF content is normally already < 5120.
- If still over: drop `### Research Methodology` footer, shorten Resources tables (keep 4–6 rows), tighten prose.
- If `bytes < 1024`: add a Cheatsheets & Quick Reference + Resources section.

## Trimming playbook (to get under 5 KB)
1. Remove the redundant `### Research Methodology` bullet/footer block.
2. Cut resource-table rows to the 4–6 most essential.
3. Compress finding bullets (drop parenthetical examples already covered elsewhere).
4. Re-normalize CRLF→LF as the final step, then re-measure.

## Condensed verified 2026 framework facts (reusable bank)
Cite these when updating any comic / Django / Python / Next.js report. All confirmed via web_search + web_extract in July 2026.

### Django (profile, rhixecompany-comics)
- **4.2 LTS EOL: April 7, 2026** — no upstream security patches. Migrate to 5.2 LTS urgently.
- **5.2 LTS**: current prod target; supports Python 3.10–3.14; `CompositePrimaryKey`, async auth (`acreate_user`, `alogin`), PBKDF2 1,000,000.
- **6.0** (released Dec 3, 2025): Python **3.12–3.14 only** (drops 3.10/3.11). New: built-in **CSP** (`ContentSecurityPolicyMiddleware`, `SECURE_CSP` + `django.utils.csp` constants + nonce context processor), **template partials** (`{% partialdef %}`/`{% partial %}`), **Tasks framework** (`@task` decorator; external worker still required), modern Python email API.
- GCS: Django 4.2+ unified `STORAGES` dict → `GoogleCloudStorage`; separate buckets; `GS_IAM_SIGN_BLOB=True` for signed URLs.
- CKEditor: `django-ckeditor` (v4) deprecated w/ CVEs → use `django-ckeditor-5` (github.com/hvlads/django-ckeditor-5; image upload support). Library warns uploaded files are **not validated server-side by default** → sanitize with `nh3` (Rust, fast) / `bleach`.

### Python (Python-projects)
- **3.12** security-only (EOL Oct 2028). **3.13** bugfix, JIT experimental + free-threaded opt-in. **3.14** (Oct 7 2025) bugfix: free-threaded now officially supported, opt-in JIT in Win/macOS binaries, template strings (t-strings), deferred annotations, subinterpreters, `compression.zstd`. **3.15** prerelease.
- **uv**: 8–100× faster than pip (Real Python ~8×; HN 38s→3s). Replaces pip/virtualenv/pyenv/Poetry. PEP 723 `# /// script` for inline deps.
- OpenSSF pyscg (May 2026): no `shell=True`, no hardcoded secrets, `requests.get(url, timeout=10)`, `bandit` + `pip-audit`.

### Next.js / React (rhixe_scans, rhixecompany-comics)
- **Next.js 16** (Oct 21 2025): **Turbopack default bundler** (2–5× faster prod builds, up to 10× Fast Refresh); explicit caching APIs (`revalidateTag`/`updateTag`/`refresh`) replace implicit ISR; bundles React 19.2.
- **16.2** (Mar 18 2026): Server Fast Refresh (400–900% faster compile in real apps), Subresource Integrity (SRI) for JS, tree-shaking of dynamic imports.
- **Tailwind v4**: CSS-first (`@import "tailwindcss"` + `@theme`), Rust engine (3–10× faster builds), drops `tailwind.config.js`, no PostCSS plugin (standalone CLI / Vite plugin).

### Prisma (rhixe_scans)
- **Prisma 6**: global singleton on `globalThis`; set `connection_limit` + `pool_timeout` in DATABASE_URL; PgBouncer transaction pooling for serverless; CUID over UUID; `relationLoadStrategy: "join"`. 6.19 added pooled Postgres connections.
- Dual payments: Stripe `request.text()` raw body before `constructEvent()`; PayPal `POST /v2/checkout/orders/{id}/capture` + verify `COMPLETED`; unify in `Subscription` with `@@unique([provider, providerId])`; idempotency via DB event-id dedup + `PayPal-Request-Id` (6h). 2026: ack webhook fast, process async, wrap idempotency+business logic in one tx, daily reconciliation.

### Selenium (selenium_webdriver)
- **Selenium 4.x** is the 2026 mainstream default; teams pilot **Selenium 5** previews for richer BiDi.
- **WebDriver BiDi** = official CDP replacement (W3C, cross-browser). Enable `options.setCapability('webSocketUrl', true)`. CDP "temporary until BiDi implemented."
- **Selenium Manager** (4.6+): zero-config driver resolution; removes `webdriver-manager`.
- Headless: `headless()` removed in 4.10; use `--headless=new`.
- Stealth: override `navigator.webdriver`, `--headless=new`, rotate UAs; **Playwright** recommended for new scrapers (2–3× faster, harder to detect).

## URL verification notes (July 2026)
- `docs.djangoproject.com/en/6.0/releases/6.0` ✓ (Django 6.0 notes)
- `docs.djangoproject.com/en/6.0/releases/5.2` ✓ (5.2 notes)
- `github.com/hvlads/django-ckeditor-5` ✓ (PyPI extract 404'd; repo is live)
- `nextjs.org/blog/next-16-2-turbopack` ✓ (16.2 blog)
- `nextjs.org/docs` ✓
- `selenium.dev/documentation/webdriver/bidi` ✓ (BiDi docs)
