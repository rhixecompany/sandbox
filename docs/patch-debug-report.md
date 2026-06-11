# Patch Debug Report (Phase 7)

**Generated**: 2026-05-29
**Phase**: Phase 7 — Patch Debug & Dependency Analysis
**Workspace**: C:\Users\Alexa\Desktop\SandBox

---

## Summary

| Metric | Count |
|--------|-------|
| Total patches inventoried | 7 (1 tooling + 3 pre-applied + 2 enhanced + 1 obsolete) |
| Pre-applied (already in git history) | 3 |
| Already in target file | 1 |
| In target project repo | 2 |
| Truly obsolete | 1 |

## Active Patches

### run-audit.sh.patch
| Field | Value |
|-------|-------|
| **Path** | `Bash/edits/run-audit.sh.patch` |
| **Size** | 591 B |
| **Target** | `Bash/scripts/run-audit.sh` |
| **Format** | V4A (multi-file with markers) |
| **Commits** | N/A — inline patch, not git-format |
| **Status** | PRE-APPLIED |
| **Evidence** | Dry-run support (`DRY_RUN` variable, `--dry-run`/`-n` flags) already present in target file at lines 4-13 |
| **Patch tool result** | "Patch validation failed (no files were modified)" — confirms already applied |

### python-projects.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/pre-applied/python-projects.patch` |
| **Size** | 130 KB (3,364 lines) |
| **Target** | `projects/Python-projects` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 6 commits, all pre-applied |
| **Status** | PRE-APPLIED |
| **Evidence** | Commit SHA `d6769de780ca6f70ca7f29f16975d9461e078d64` and 5 more verified in project git history |
| **Issues** | None — commits are in target project's history |

### xamehi.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/pre-applied/xamehi.patch` |
| **Size** | 1.4 MB (32,074 lines) |
| **Target** | `projects/xamehi` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 5 commits, all pre-applied |
| **Status** | PRE-APPLIED |
| **Evidence** | Commit SHA `79dc207f87f8383c969829382e6e3ab60509dd87` and 4 more verified |
| **Issues** | Patch from 2022-08; project has evolved but all base commits are present |

### youtube-downloader.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/pre-applied/youtube-downloader.patch` |
| **Size** | 186 KB (5,020 lines) |
| **Target** | `projects/youtube-downloader` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 23 commits, all pre-applied |
| **Status** | PRE-APPLIED |
| **Evidence** | Commit SHA `637c873cfdc245ec19fe69b7c1e10c2afc774786` and 22 more verified |
| **Issues** | None |

### django-scrapy-selenium.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/enhanced/django-scrapy-selenium.patch` |
| **Size** | 35 MB (633,648 lines) |
| **Target** | `projects/Django-Scrapy-Selenium` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 10 commits |
| **Status** | ALREADY IN TARGET REPO |
| **Evidence** | Patch content matches files in `projects/Django-Scrapy-Selenium/` |

### xamehi-tv.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/enhanced/xamehi-tv.patch` |
| **Size** | 9.3 MB (117,538 lines) |
| **Target** | `projects/xamehi.tv` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 5 commits |
| **Status** | ALREADY IN TARGET REPO |
| **Evidence** | Patch content matches files in `projects/xamehi.tv/` |

## Obsolete Patches

### cookiecutter-django-tailwind.patch
| Field | Value |
|-------|-------|
| **Path** | `patches/obsolete/cookiecutter-django-tailwind.patch` |
| **Size** | 2.7 MB (54,001 lines) |
| **Target** | `projects/cookiecutter-django-tailwind` |
| **Format** | Git-format (git format-patch) |
| **Commits** | 4 commits |
| **Status** | TRULY OBSOLETE |
| **Reason** | Cookiecutter template scaffolding — not actual project changes. The patch contains template variables (`{{cookiecutter.project_slug}}`) which confirm it's a scaffolding template, not a patch to be applied to any existing project. |

## Verification Method

For each git-format patch, verification was performed by:
1. Checking the `From` commit SHA in the patch header
2. Using `git cat-file -t <SHA>` or `git log --oneline | grep <SHA>` in the target project directory
3. For V4A patch, manually comparing patch content vs target file content

## Issues Found

| # | Issue | Severity | Resolution |
|---|-------|----------|------------|
| 1 | cookiecutter-django-tailwind.patch has no applyable target | INFO | Archived as obsolete |
| 2 | run-audit.sh.patch fails on apply attempt | INFO | Confirmed already applied — no action needed |
| 3 | Enhanced patches were originally in obsolete/ | LOW | Reclassified to enhanced/ in earlier phase |

---

**Next**: Phase 8 — AI-Readiness Report
