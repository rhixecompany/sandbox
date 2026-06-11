# Patch Debug Session — 2026-05-27

## Patches Inventoried (8)

| Patch | Target | Commits | Classification |
|-------|--------|---------|---------------|
| xamehi.patch | projects/xamehi | 5 (all pre-applied) | PRE-APPLIED |
| python-projects.patch | projects/Python-projects | 6 (all pre-applied) | PRE-APPLIED |
| youtube-downloader.patch | projects/youtube-downloader | 23 (all pre-applied) | PRE-APPLIED |
| rhixe-company.patch | projects/profile (was marked rhixe-company) | 3 commits | APPLIED (cleanup) |
| run-audit.sh.patch | Bash/scripts/run-audit.sh | V4A format | PRE-APPLIED (DRY_RUN already present) |
| django-scrapy-selenium.patch | projects/Django-Scrapy-Selenium | 1 commit | RECLASSIFIED: obsolete→enhanced |
| xamehi-tv.patch | projects/xamehi.tv | 1 commit | RECLASSIFIED: obsolete→enhanced |
| cookiecutter-django-tailwind.patch | projects/cookiecutter-django-tailwind | 1 commit | TRULY OBSOLETE (template) |

## Key Commands Used

```bash
# Check if patch applies
cd projects/<target> && git apply --check ../../<patch>.patch

# Verify commit SHAs
grep '^From [a-f0-9]' xamehi.patch
cd projects/xamehi && git cat-file -t <SHA>

# Classify by checking individual commits
cd projects/xamehi && git log --oneline | grep -c <SHA>

# Apply patch to new project
mkdir -p projects/rhixe-company
cd projects/rhixe-company && git init && git apply ../../rhixe-company.patch
git add -A && git commit -m "feat: initial project from patch"

# Apply patch to existing project (cleanup/update)
cd projects/profile && git apply --index ../../rhixe-company.patch
```

## Reclassification Notes

- **django-scrapy-selenium.patch** was in `obsolete/` but its commit was found in `projects/Django-Scrapy-Selenium` git history → moved to `enhanced/`
- **xamehi-tv.patch** was in `obsolete/` but its commit was found in `projects/xamehi.tv` git history → moved to `enhanced/`
- **cookiecutter-django-tailwind.patch** was correctly in `obsolete/` — it's a cookiecutter project template, not project patches

## rhixe-company Mapping

The patch `rhixe-company.patch` targets `projects/profile/` (NOT a separate `projects/rhixe-company/` directory). When applied:
- Result: 301 files changed, 61,668 deletions (pycache cleanup + duplicate static vendor deduplication)
- No source files modified — only generated files (__pycache__) and duplicate vendors
