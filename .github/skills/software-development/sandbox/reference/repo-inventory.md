---
name: sandbox-repo-inventory
description: "Repo Inventory"
version: 1.0.0
author: Alexa
---
     1|# Repo Inventory
     2|
     3|## 17 Repos Across 2 GitHub Organizations
     4|
     5|### rhixecompany (8 repos)
     6|
     7|| Repo | Priority | Stack | Path | Description |
     8|| --- | --- | --- | --- | --- |
     9|| Banking | HIGH | TypeScript/Node | `rhixecompany/Banking` | Fintech banking app (Next.js 16, Drizzle, PostgreSQL, NextAuth) |
    10|| ecom | MEDIUM | TypeScript/Node | `rhixecompany/ecom` | E-commerce platform (Django) |
    11|| profile | MEDIUM | TypeScript/Node | `rhixecompany/profile` | User profile service (Django) |
    12|| rhixe_scans | HIGH | TypeScript/Node | `rhixecompany/rhixe_scans` | Document scanning service (Next.js + Python backend) |
    13|| selenium_webdriver | MEDIUM | Python | `rhixecompany/selenium_webdriver` | Selenium WebDriver utilities |
    14|| university-libary-jsm | HIGH | TypeScript/Node | `rhixecompany/university-libary-jsm` | University library (Next.js, Drizzle, NextAuth) |
    15|| xamehitv | MEDIUM | TypeScript/Node | `rhixecompany/xamehitv` | Video streaming platform |
    16|| my-opencode-config | LOW | Unknown | `rhixecompany/my-opencode-config` | OpenCode configuration (private) |
    17|| rhixecompany | LOW | Unknown | `rhixecompany/rhixecompany` | Core company repo |
    18|
    19|### Rhixe-company (8 repos)
    20|
    21|| Repo | Priority | Stack | Path | Description |
    22|| --- | --- | --- | --- | --- |
    23|| comicwise | CRITICAL | TypeScript/Node | `Rhixe-company/comicwise` | Comic management system (Next.js, Drizzle) — 148 issues |
    24|| cookiecutter-django-tailwind | MEDIUM | Python | `Rhixe-company/cookiecutter-django-tailwind` | Django cookiecutter template |
    25|| Django-Scrapy-Selenium | MEDIUM | Python | `Rhixe-company/Django-Scrapy-Selenium` | Web scraping framework |
    26|| Python-projects | MEDIUM | Python | `Rhixe-company/Python-projects` | Python utilities collection |
    27|| youtube-downloader | MEDIUM | Python | `Rhixe-company/youtube-downloader` | YouTube video downloader |
    28|| rhixe.company | LOW | Unknown | `Rhixe-company/rhixe.company` | Company website (private) |
    29|| xamehi | LOW | Unknown | `Rhixe-company/xamehi` | Media platform (private) |
    30|| xamehi.tv | LOW | Unknown | `Rhixe-company/xamehi.tv` | Video streaming service (private) |
    31|
    32|### Standalone
    33|
    34|| Repo | Path | Description |
    35|| --- | --- | --- |
    36|| Resume_maker | `Resume_maker/` | TypeScript resume generator (Bun runtime) |
    37|| Bash | `Bash/` | Cache cleanup and upgrade scripts (bat/ps1/sh) |
    38|
    39|## Priority Distribution
    40|
    41|- **CRITICAL (1)**: comicwise — 148 expected issues
    42|- **HIGH (3)**: Banking (5), rhixe_scans (8), university-libary-jsm (12)
    43|- **MEDIUM (8)**: cookiecutter (8), Django-Scrapy (6), Python-projects (5), youtube-downloader (4), ecom (7), profile (6), selenium_webdriver (5), xamehitv (6)
    44|- **LOW (5)**: rhixe.company (2), xamehi (2), xamehi.tv (2), my-opencode-config (1), rhixecompany (1)
    45|
    46|## Stack Detection
    47|
    48|The audit system (`scripts/lib/repo-scanner.js`) auto-detects stack by presence of:
    49|
    50|- `package.json` → typescript-node
    51|- `requirements.txt` or `pyproject.toml` → python
    52|- Neither → unknown
    53|
    54|## Private Repos (3)
    55|
    56|- `rhixecompany/my-opencode-config`
    57|- `Rhixe-company/rhixe.company`
    58|- `Rhixe-company/xamehi`
    59|- `Rhixe-company/xamehi.tv`
    60|