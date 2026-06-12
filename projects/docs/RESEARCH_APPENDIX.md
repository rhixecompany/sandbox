# RESEARCH_APPENDIX.md

## Purpose
Captures research rationale, version caveats, cross-reference notes, and unresolved
questions for the Phase 0–5 `/repo` research run.

## Per-Project Research Notes

### Banking
- Primary risk: mixing Plaid/Dwolla client and server flows.
- Version note: Next.js 16 + Drizzle use current stable configs in project docs.

### comicwise
- Status note: marked as consolidation target; frontend patterns inherited by rhixecompany-comics.
- Cross-reference note: symmetric refs with rhixe_scans and rhixecompany-comics verified.

### cookiecutter-django-tailwind
- Generator debt risk: maintain optional addon versions carefully.
- Windows note: template consumers may hit Windows venv path differences.

### Django-Scrapy-Selenium
- Status note: consolidation source; scraping patterns inherited by rhixecompany-comics.
- Tech note: Scrapy 2.14 async path must replace legacy Twisted chains.

### ecom
- Order flow note: PayPal capture should happen server-side to avoid approval/capture desync.

### profile
- Media note: GCS + CKEditor sanitization must be enforced at render time even with editor-side protection.

### Python-projects
- Maintenance note: consider `pip list --outdated` plus `pip-audit` cadence.
- Dependency note: OpenCV and Matplotlib should be pinned for learner stability.

### rhixe_scans
- Auth note: NextAuth v5 + Prisma adapter is the durable pattern here.
- Payment note: Stripe and PayPal webhooks should be split into distinct handlers.

### rhixecompany-comics
- Consolidation note: inherits from comicwise, Django-Scrapy-Selenium, selenium_webdriver.
- Architecture note: Django remains the data/auth/task source of truth; Next.js owns the reader.

### selenium_webdriver
- Maintenance note: Selenium Manager now handles driver binaries; drop manual ChromeDriver management.
- Status note: consolidation source for browser automation utilities.

### university-libary-jsm
- Infra note: Neon + Redis require serverless-friendly connection pooling and cache TTL discipline.

### xamehi
- Modernization note: dual-backend auth/search should converge to one API layer to eliminate contract drift.

### xamehi.tv
- Upgrade note: React 17 plus legacy Material-UI 4/RethinkDB-era React Bootstrap increases maintenance cost.
- Media note: video deliveries should be CDN-backed; WhiteNoise is not suitable for video.

### youtube-downloader
- ToS note: tool is personal/rights-compliant use only.
- Maintenance note: `yt-dlp[curl-cffi]` is required for current YouTube compatibility.

## Web Research Sources
Research findings were gathered from the following source classes and must be treated
as references, not as owned content:

- Official docs: Next.js, Django, DRF, Drizzle, Prisma, Celery, Scrapy, Selenium, Playwright, shadcn/ui, PayPal, Stripe, Plaid, Dwolla, Neon, Redis, UploadThing, Resend, Material-UI, video-react
- Community guides and blog posts referenced inside each project's `RESEARCH_REPORT.md` Resources table
- Open-source reference repos cited in Similar Projects tables

## Unresolved / Follow-up
- Perform URL spot-checks for all Resource entries before any public release.
- Verify latest version compatibility for legacy React 17 and Material-UI 4 in xamehi.tv.
- Re-run Phase 5 verification after any follow-up changes.
