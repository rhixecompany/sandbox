# Patch Dependency Graph (Phase 7)

**Generated**: 2026-05-29
**Phase**: Phase 7 — Dependency Analysis
**Workspace**: C:\Users\Alexa\Desktop\SandBox

---

## Dependency Graph Overview

Since all patches are either pre-applied, already in target repos, or obsolete, there are **no cross-patch dependencies**. Each patch targets a different project or file, and all are already applied to their respective targets.

```
                    ┌───────────────────────────────────────┐
                    │         Workspace Root                 │
                    │     C:\Users\Alexa\Desktop\SandBox     │
                    └───────┬────────┬────────┬─────────────┘
                            │        │        │
          ┌─────────────────┘        │        └─────────────────┐
          │                          │                          │
          ▼                          ▼                          ▼
   ┌─────────────┐          ┌──────────────┐          ┌───────────────┐
   │   Bash/     │          │  projects/   │          │   patches/    │
   │  scripts/   │          │  (14 repos)  │          │  (containers) │
   └──────┬──────┘          └──────┬───────┘          └───────┬───────┘
          │                        │                          │
          ▼                        ▼                          ▼
   ┌──────────────┐      ┌──────────────────┐       ┌──────────────────┐
   │run-audit.sh  │      │Python-projects◄──│───────│ pre-applied/     │
   │(dry-run      │      │xamehi◄───────────│───────│  xamehi.patch    │
   │ already in   │      │youtube-downloader│───────│  python-projects │
   │ file)        │      │  ◄───────────────│       │  youtube-dl.patch│
   └──────────────┘      │Django-Scrapy-Sel │       ├──────────────────┤
                          │  ◄───────────────│───────│ enhanced/        │
                          │xamehi.tv◄───────│───────│  django-scrapy-  │
                          │                  │       │  selenium.patch  │
                          │cookiecutter-dj-  │       │  xamehi-tv.patch │
                          │  tailwind (obs)  │       ├──────────────────┤
                          └──────────────────┘       │ obsolete/        │
                                                      │  cookiecutter-  │
                                                      │  django-tailwind│
                                                      └──────────────────┘
```

## Dependency Matrix

| Patch | Depends On | Required By | Status |
|-------|-----------|-------------|--------|
| run-audit.sh.patch | None | None | Independent — tooling patch |
| python-projects.patch | None | None | Independent — pre-applied |
| xamehi.patch | None | None | Independent — pre-applied |
| youtube-downloader.patch | None | None | Independent — pre-applied |
| django-scrapy-selenium.patch | None | None | Independent — in repo |
| xamehi-tv.patch | None | None | Independent — in repo |
| cookiecutter-django-tailwind.patch | None | None | Independent — obsolete |

## Patch-to-Project Mapping

| Project Directory | Patches Targeting It | Applied? |
|-------------------|---------------------|----------|
| `Bash/scripts/run-audit.sh` | `Bash/edits/run-audit.sh.patch` | Already in file |
| `projects/Python-projects` | `patches/pre-applied/python-projects.patch` | Pre-applied (git history) |
| `projects/xamehi` | `patches/pre-applied/xamehi.patch` | Pre-applied (git history) |
| `projects/youtube-downloader` | `patches/pre-applied/youtube-downloader.patch` | Pre-applied (git history) |
| `projects/Django-Scrapy-Selenium` | `patches/enhanced/django-scrapy-selenium.patch` | Already in repo |
| `projects/xamehi.tv` | `patches/enhanced/xamehi-tv.patch` | Already in repo |
| `projects/cookiecutter-django-tailwind` | `patches/obsolete/cookiecutter-django-tailwind.patch` | Obsolete — no apply target |

## Project-to-Patch Mapping

| Project | Patch Count | Patches |
|---------|-------------|---------|
| Bash/scripts/run-audit.sh | 1 | run-audit.sh.patch |
| projects/Python-projects | 1 | python-projects.patch |
| projects/xamehi | 1 | xamehi.patch |
| projects/youtube-downloader | 1 | youtube-downloader.patch |
| projects/Django-Scrapy-Selenium | 1 | django-scrapy-selenium.patch |
| projects/xamehi.tv | 1 | xamehi-tv.patch |
| projects/cookiecutter-django-tailwind | 1 | cookiecutter-django-tailwind.patch (obsolete) |

## Dependency Conclusion

**No cross-patch dependencies exist.** All patches are independent and target different projects/files. This is expected because:
1. Each git-format patch was generated from a specific project's repository
2. The V4A tooling patch targets a single script file
3. The obsolete patch targets a cookiecutter template, not a live project

This means patches can be applied (or skipped) in any order without conflicts.

---

**Next**: Phase 8 — AI-Readiness Report
