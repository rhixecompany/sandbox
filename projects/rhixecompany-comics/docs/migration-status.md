# Migration Status

Tracking what has been consolidated into `rhixecompany-comics` versus what remains pending.

## Completed

- [x] Extracted frontend patterns from `projects/comicwise` into `docs/consolidation-patterns.md`
- [x] Extracted scraping + task-queue patterns from `projects/Django-Scrapy-Selenium` into `docs/consolidation-patterns.md`
- [x] Extracted browser-automation utilities from `projects/selenium_webdriver` into `docs/consolidation-patterns.md`
- [x] Authored architecture decisions in `docs/architecture.md`
- [x] Marked source repos as consolidation targets in their `RESEARCH_REPORT.md` files

## In Progress

- [ ] Branch normalization across all 14 repos
- [ ] Ignore file audit
- [ ] Dependency audit
- [ ] Bun migration for JS/TS repos
- [ ] CI workflow setup for all repos

## Pending

- [ ] Validate live env parity for Django + Next.js services in `rhixecompany-comics`
- [ ] Reconcile payment provider keys between comicwise and rhixecompany-comics
- [ ] Run Phase 5 verification after all repo-management phases complete
