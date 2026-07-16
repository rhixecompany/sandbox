# Project Architecture Blueprint

Generated from workspace: `C:\Users\Alexa\Desktop\SandBox`

## Workspace Overview
- Multi-project monorepo/workspace with Bun/TypeScript, Django/Python, Go, Rust, Java, Kotlin, PHP, and utility examples.
- Root-level shared tooling: `.vscode/`, docs, and workspace configuration files.

## Project Index
| Project | Detected Stack | Architecture Pattern | Docs |
| --- | --- | --- | --- |
| `projects/Banking` | Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier, Python | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/Banking/Banking_architecture.md` |
| `projects/Bash` | Bun, TypeScript, ESLint, Prettier | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/Bash/Bash_architecture.md` |
| `projects/comicwise` | Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/comicwise/comicwise_architecture.md` |
| `projects/cookiecutter-django-tailwind` | Python | Python service or utility project | `docs/Project_Architecture/projects/cookiecutter-django-tailwind/cookiecutter-django-tailwind_architecture.md` |
| `projects/Django-Scrapy-Selenium` | Node.js, TypeScript, Tailwind, ESLint, Prettier, Django, Python | Full-stack dual-stack app (Django backend + JavaScript frontend/tooling) | `docs/Project_Architecture/projects/Django-Scrapy-Selenium/Django-Scrapy-Selenium_architecture.md` |
| `projects/ecom` | Django, Python | Django backend service | `docs/Project_Architecture/projects/ecom/ecom_architecture.md` |
| `projects/profile` | Django, Python | Django backend service | `docs/Project_Architecture/projects/profile/profile_architecture.md` |
| `projects/Python-projects` | Python | Python service or utility project | `docs/Project_Architecture/projects/Python-projects/Python-projects_architecture.md` |
| `projects/Resume_maker` | Bun, TypeScript, ESLint, Prettier | Lightweight utility or scaffold project | `docs/Project_Architecture/projects/Resume_maker/Resume_maker_architecture.md` |
| `projects/rhixe_scans` | Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier, Python | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/rhixe_scans/rhixe_scans_architecture.md` |
| `projects/selenium_webdriver` | Bun, Prettier | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/selenium_webdriver/selenium_webdriver_architecture.md` |
| `projects/university-libary-jsm` | Next.js, React, Node.js, TypeScript, Tailwind, ESLint, Prettier | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/university-libary-jsm/university-libary-jsm_architecture.md` |
| `projects/xamehi` | React, Node.js, Django | Full-stack dual-stack app (Django backend + JavaScript frontend/tooling) | `docs/Project_Architecture/projects/xamehi/xamehi_architecture.md` |
| `projects/xamehi.tv` | Django, Python | Django backend service | `docs/Project_Architecture/projects/xamehi.tv/xamehi.tv_architecture.md` |
| `projects/ecom/frontend` | React, Bun | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/ecom/frontend/frontend_architecture.md` |
| `projects/mcp-servers/copilot-studio` | Bun, TypeScript | Lightweight utility or scaffold project | `docs/Project_Architecture/projects/mcp-servers/copilot-studio/copilot-studio_architecture.md` |
| `projects/mcp-servers/go` | Go | Go service/library | `docs/Project_Architecture/projects/mcp-servers/go/go_architecture.md` |
| `projects/mcp-servers/java` | Java/Maven | Java/Maven module | `docs/Project_Architecture/projects/mcp-servers/java/java_architecture.md` |
| `projects/mcp-servers/kotlin` | Kotlin/Gradle | Kotlin/Gradle module | `docs/Project_Architecture/projects/mcp-servers/kotlin/kotlin_architecture.md` |
| `projects/mcp-servers/php` | PHP/Composer | PHP/Composer project | `docs/Project_Architecture/projects/mcp-servers/php/php_architecture.md` |
| `projects/mcp-servers/python` | Python | Python service or utility project | `docs/Project_Architecture/projects/mcp-servers/python/python_architecture.md` |
| `projects/mcp-servers/rust` | Rust | Rust crate / tool | `docs/Project_Architecture/projects/mcp-servers/rust/rust_architecture.md` |
| `projects/mcp-servers/typescript` | Bun, TypeScript | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/mcp-servers/typescript/typescript_architecture.md` |
| `projects/rhixe_scans/backend` | Django | Django backend service | `docs/Project_Architecture/projects/rhixe_scans/backend/backend_architecture.md` |
| `projects/rhixecompany-comics/backend` | Django, Python | Django backend service | `docs/Project_Architecture/projects/rhixecompany-comics/backend/backend_architecture.md` |
| `projects/rhixecompany-comics/frontend` | Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/rhixecompany-comics/frontend/frontend_architecture.md` |
| `projects/xamehi.tv/frontend` | React, Bun | JavaScript/Bun application with feature-oriented source layout | `docs/Project_Architecture/projects/xamehi.tv/frontend/frontend_architecture.md` |

## Cross-Cutting Architecture
- Shared workspace-level VS Code configuration and generated docs.
- Projects are intentionally isolated by folder, with per-project configs under `.vscode/` where needed.
- Mixed stacks mean architecture docs should be read per project, then as a workspace map.

## Update Notes
- Regenerate when project roots, dependencies, or folder structure change.
- Keep per-project docs aligned with current manifests and top-level directories.