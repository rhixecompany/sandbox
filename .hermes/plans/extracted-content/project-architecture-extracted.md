# Project Architecture — Extracted Content

> Generated from all 51 files in `docs/Project_Architecture/`
> 17 projects, each with architecture + folders + techstack

---

## 1. Banking

### Banking_architecture.md
```markdown
# Banking Architecture Blueprint

## Overview
- **Project**: Banking
- **Path**: projects/Banking
- **Stack**: Next.js, React, TypeScript

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### Banking_folders.md
```markdown
# Banking Folder Structure

## Root: projects/Banking

### Key Directories
- src/ — source code
- public/ — static assets
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### Banking_techstack.md
```markdown
# Banking Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Next.js | Detected from project files |
| React | Detected from project files |
| TypeScript | Detected from project files |

## Build & Test Commands
```bash
npm run dev
npm run build
npm run lint
```
```

---

## 2. Bash

### Bash_architecture.md
```markdown
# Bash Architecture Blueprint

## Overview
- **Project**: Bash
- **Path**: Bash
- **Stack**: TypeScript, Bun

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### Bash_folders.md
```markdown
# Bash Folder Structure

## Root: Bash

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### Bash_techstack.md
```markdown
# Bash Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| TypeScript | Detected from project files |
| Bun | Detected from project files |

## Build & Test Commands
```
```

---

## 3. comicwise

### comicwise_architecture.md
```markdown
# comicwise Architecture Blueprint

## Overview
- **Project**: comicwise
- **Path**: projects/comicwise
- **Stack**: Next.js, React, TypeScript

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### comicwise_folders.md
```markdown
# comicwise Folder Structure

## Root: projects/comicwise

### Key Directories
- src/ — source code
- public/ — static assets
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### comicwise_techstack.md
```markdown
# comicwise Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Next.js | Detected from project files |
| React | Detected from project files |
| TypeScript | Detected from project files |

## Build & Test Commands
```bash
npm run dev
npm run build
npm run lint
```
```

---

## 4. cookiecutter_django_tailwind

### cookiecutter_django_tailwind_architecture.md
```markdown
# cookiecutter-django-tailwind Architecture Blueprint

## Overview
- **Project**: cookiecutter-django-tailwind
- **Path**: projects/cookiecutter-django-tailwind
- **Stack**: Python

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### cookiecutter_django_tailwind_folders.md
```markdown
# cookiecutter-django-tailwind Folder Structure

## Root: projects/cookiecutter-django-tailwind

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### cookiecutter_django_tailwind_techstack.md
```markdown
# cookiecutter-django-tailwind Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Python | Detected from project files |

## Build & Test Commands
```
```

---

## 5. Django_Scrapy_Selenium

### Django_Scrapy_Selenium_architecture.md
```markdown
# Django-Scrapy-Selenium Architecture Blueprint

## Overview
- **Project**: Django-Scrapy-Selenium
- **Path**: projects/Django-Scrapy-Selenium
- **Stack**: TailwindCSS, TypeScript

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### Django_Scrapy_Selenium_folders.md
```markdown
# Django-Scrapy-Selenium Folder Structure

## Root: projects/Django-Scrapy-Selenium

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### Django_Scrapy_Selenium_techstack.md
```markdown
# Django-Scrapy-Selenium Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| TailwindCSS | Detected from project files |
| TypeScript | Detected from project files |

## Build & Test Commands
```
```

---

## 6. docs

### docs_architecture.md
```markdown
# docs Architecture Blueprint

## Overview
- **Project**: docs
- **Path**: docs
- **Stack**: Unknown

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### docs_folders.md
```markdown
# docs Folder Structure

## Root: docs

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### docs_techstack.md
```markdown
# docs Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Unknown | Detected from project files |

## Build & Test Commands
```
```

---

## 7. ecom

### ecom_architecture.md
```markdown
# ecom Architecture Blueprint

## Overview
- **Project**: ecom
- **Path**: projects/ecom
- **Stack**: Django, Python

## Layer Analysis
- **Presentation**: Django templates + optional DRF API
- **Business Logic**: Django views, models, serializers
- **Data Layer**: Django ORM with PostgreSQL/SQLite

## Cross-Cutting Concerns
- **Auth**: Django Auth
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
```

### ecom_folders.md
```markdown
# ecom Folder Structure

## Root: projects/ecom

### Key Directories
- .vscode/ — VS Code configuration
- src/ or app/ — Django apps
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### ecom_techstack.md
```markdown
# ecom Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Django | Detected from project files |
| Python | Detected from project files |

## Build & Test Commands
```bash
python manage.py runserver
python manage.py test
```
```

---

## 8. profile

### profile_architecture.md
```markdown
# profile Architecture Blueprint

## Overview
- **Project**: profile
- **Path**: projects/profile
- **Stack**: Django, Python

## Layer Analysis
- **Presentation**: Django templates + optional DRF API
- **Business Logic**: Django views, models, serializers
- **Data Layer**: Django ORM with PostgreSQL/SQLite

## Cross-Cutting Concerns
- **Auth**: Django Auth
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
```

### profile_folders.md
```markdown
# profile Folder Structure

## Root: projects/profile

### Key Directories
- .vscode/ — VS Code configuration
- src/ or app/ — Django apps
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### profile_techstack.md
```markdown
# profile Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Django | Detected from project files |
| Python | Detected from project files |

## Build & Test Commands
```bash
python manage.py runserver
python manage.py test
```
```

---

## 9. Python_projects

### Python_projects_architecture.md
```markdown
# Python-projects Architecture Blueprint

## Overview
- **Project**: Python-projects
- **Path**: projects/Python-projects
- **Stack**: Python

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### Python_projects_folders.md
```markdown
# Python-projects Folder Structure

## Root: projects/Python-projects

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### Python_projects_techstack.md
```markdown
# Python-projects Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Python | Detected from project files |

## Build & Test Commands
```
```

---

## 10. Resume_maker

### Resume_maker_architecture.md
```markdown
# Resume_maker Architecture Blueprint

## Overview
- **Project**: Resume_maker
- **Path**: Resume_maker
- **Stack**: Bun

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### Resume_maker_folders.md
```markdown
# Resume_maker Folder Structure

## Root: Resume_maker

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### Resume_maker_techstack.md
```markdown
# Resume_maker Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Bun | Detected from project files |

## Build & Test Commands
```
```

---

## 11. rhixe_scans

### rhixe_scans_architecture.md
```markdown
# rhixe_scans Architecture Blueprint

## Overview
- **Project**: rhixe_scans
- **Path**: projects/rhixe_scans
- **Stack**: Dual-stack (Django + Next.js)

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
```

### rhixe_scans_folders.md
```markdown
# rhixe_scans Folder Structure

## Root: projects/rhixe_scans

### Key Directories
- backend/ — Django/Python backend
- frontend/ — Next.js frontend
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### rhixe_scans_techstack.md
```markdown
# rhixe_scans Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Dual-stack (Django + Next.js) | Detected from project files |

## Build & Test Commands
```bash
npm run dev
npm run build
npm run lint
```
```bash
python manage.py runserver
python manage.py test
```
```

---

## 12. rhixecompany_comics

### rhixecompany_comics_architecture.md
```markdown
# rhixecompany-comics Architecture Blueprint

## Overview
- **Project**: rhixecompany-comics
- **Path**: projects/rhixecompany-comics
- **Stack**: Dual-stack (Django + Next.js)

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
```

### rhixecompany_comics_folders.md
```markdown
# rhixecompany-comics Folder Structure

## Root: projects/rhixecompany-comics

### Key Directories
- backend/ — Django/Python backend
- frontend/ — Next.js frontend
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### rhixecompany_comics_techstack.md
```markdown
# rhixecompany-comics Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Dual-stack (Django + Next.js) | Detected from project files |

## Build & Test Commands
```bash
npm run dev
npm run build
npm run lint
```
```bash
python manage.py runserver
python manage.py test
```
```

---

## 13. selenium_webdriver

### selenium_webdriver_architecture.md
```markdown
# selenium_webdriver Architecture Blueprint

## Overview
- **Project**: selenium_webdriver
- **Path**: projects/selenium_webdriver
- **Stack**: Unknown

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### selenium_webdriver_folders.md
```markdown
# selenium_webdriver Folder Structure

## Root: projects/selenium_webdriver

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### selenium_webdriver_techstack.md
```markdown
# selenium_webdriver Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Unknown | Detected from project files |

## Build & Test Commands
```
```

---

## 14. university_libary_jsm

### university_libary_jsm_architecture.md
```markdown
# university-libary-jsm Architecture Blueprint

## Overview
- **Project**: university-libary-jsm
- **Path**: projects/university-libary-jsm
- **Stack**: Next.js, React, TypeScript

## Layer Analysis
- **Presentation**: Next.js/React frontend with App Router

## Cross-Cutting Concerns
- **Auth**: NextAuth.js
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### university_libary_jsm_folders.md
```markdown
# university-libary-jsm Folder Structure

## Root: projects/university-libary-jsm

### Key Directories
- src/ — source code
- public/ — static assets
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### university_libary_jsm_techstack.md
```markdown
# university-libary-jsm Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Next.js | Detected from project files |
| React | Detected from project files |
| TypeScript | Detected from project files |

## Build & Test Commands
```bash
npm run dev
npm run build
npm run lint
```
```

---

## 15. xamehi.tv

### xamehi.tv_architecture.md
```markdown
# xamehi.tv Architecture Blueprint

## Overview
- **Project**: xamehi.tv
- **Path**: projects/xamehi.tv
- **Stack**: Django, Python

## Layer Analysis
- **Presentation**: Django templates + optional DRF API
- **Business Logic**: Django views, models, serializers
- **Data Layer**: Django ORM with PostgreSQL/SQLite

## Cross-Cutting Concerns
- **Auth**: Django Auth
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- Django apps modular, Celery tasks
```

### xamehi.tv_folders.md
```markdown
# xamehi.tv Folder Structure

## Root: projects/xamehi.tv

### Key Directories
- .vscode/ — VS Code configuration
- src/ or app/ — Django apps
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### xamehi.tv_techstack.md
```markdown
# xamehi.tv Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Django | Detected from project files |
| Python | Detected from project files |

## Build & Test Commands
```bash
python manage.py runserver
python manage.py test
```
```

---

## 16. xamehi

### xamehi_architecture.md
```markdown
# xamehi Architecture Blueprint

## Overview
- **Project**: xamehi
- **Path**: projects/xamehi
- **Stack**: React

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### xamehi_folders.md
```markdown
# xamehi Folder Structure

## Root: projects/xamehi

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### xamehi_techstack.md
```markdown
# xamehi Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| React | Detected from project files |

## Build & Test Commands
```
```

---

## 17. youtube_downloader

### youtube_downloader_architecture.md
```markdown
# youtube-downloader Architecture Blueprint

## Overview
- **Project**: youtube-downloader
- **Path**: projects/youtube-downloader
- **Stack**: Unknown

## Layer Analysis
- **Stack**: Unknown — inspect code for architecture patterns

## Cross-Cutting Concerns
- **Auth**: N/A
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- TypeScript modules, component-based
```

### youtube_downloader_folders.md
```markdown
# youtube-downloader Folder Structure

## Root: projects/youtube-downloader

### Key Directories
- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
```

### youtube_downloader_techstack.md
```markdown
# youtube-downloader Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
| Unknown | Detected from project files |

## Build & Test Commands
```
```

---

## Summary

| # | Project | Stack | Has Source Dir | Has Backend/Frontend Split |
|---|---------|-------|---------------|---------------------------|
| 1 | Banking | Next.js, React, TypeScript | Yes (src/) | No |
| 2 | Bash | TypeScript, Bun | No | No |
| 3 | comicwise | Next.js, React, TypeScript | Yes (src/) | No |
| 4 | cookiecutter_django_tailwind | Python | No | No |
| 5 | Django_Scrapy_Selenium | TailwindCSS, TypeScript | No | No |
| 6 | docs | Unknown | No | No |
| 7 | ecom | Django, Python | Yes (src/ or app/) | No |
| 8 | profile | Django, Python | Yes (src/ or app/) | No |
| 9 | Python_projects | Python | No | No |
| 10 | Resume_maker | Bun | No | No |
| 11 | rhixe_scans | Dual-stack (Django + Next.js) | Yes | Yes (backend/ + frontend/) |
| 12 | rhixecompany_comics | Dual-stack (Django + Next.js) | Yes | Yes (backend/ + frontend/) |
| 13 | selenium_webdriver | Unknown | No | No |
| 14 | university_libary_jsm | Next.js, React, TypeScript | Yes (src/) | No |
| 15 | xamehi.tv | Django, Python | Yes (src/ or app/) | No |
| 16 | xamehi | React | No | No |
| 17 | youtube_downloader | Unknown | No | No |
