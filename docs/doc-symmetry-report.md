---
title: Doc Symmetry Report
description: Generator-orchestrator 11-artifact completeness check per project.
status: final
tags: [documentation, symmetry, generator-orchestrator, quality]
generated: 2026-05-27
---

# Doc Symmetry Report

Verification of generator-orchestrator artifact completeness across all projects.

## Artifact Matrix

| Project | technology-stack | folder-structure | architecture | project-workflow | code-exemplars | copilot-instructions | readme | artifact-manifest | cross-linking-report | validation-report | execution-summary | **Total** |
|---------|---|---|---|---|---|---|---|---|---|---|---|---------|
| Banking | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| Django-Scrapy-Selenium | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| Python-projects | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| comicwise | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| cookiecutter-django-tailwind | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| ecom | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| my-opencode-config | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| profile | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| rhixe_scans | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| selenium_webdriver | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| university-libary-jsm | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| xamehi | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| xamehi.tv | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |
| youtube-downloader | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | **4/11** |

## Summary

| Metric | Value |
|--------|-------|
| Projects checked | 14 |
| Full 11/11 artifact completeness | 0 |
| Incomplete (<8/11) — recommend re-run | 14 |

## Recommendations

No project has full 11/11 artifacts. All projects have 4/11 (the core manifest + cross-linking + validation + execution summary).
To achieve full documentation suite, run the generator-orchestrator for each project with `mode=full`.
