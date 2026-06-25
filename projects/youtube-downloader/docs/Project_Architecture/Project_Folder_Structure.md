# Project Folder Structure Blueprint

## Project: youtube-downloader — YouTube Video Downloader

**Generated:** 2026-06-25  
**Project Type:** Python YouTube Downloader Scripts  
**Auto-detected:** Yes (Python — `.py` files, `requirements/`, GitHub community templates)

---

## Directory Tree

```
youtube-downloader/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── LICENSE
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── docs/
│   └── Project_Architecture/
├── execution-summary.md
├── folder-structure.md
├── main_loop_noplaylist.py       # Main script: loop, no playlist
├── main_loop_playlist.py         # Main script: loop, with playlist
├── main_noplaylist.py            # Main script: single, no playlist
├── main_playlist.py              # Main script: single, with playlist
├── project-workflow.md
├── requirements/                 # Python requirements files
├── technology-stack.md
├── test.py                       # Test script
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Python scripts** | snake_case.py | `main_loop_noplaylist.py`, `main_loop_playlist.py` |
| **Config** | dotted-prefix | `.github/`, `.vscode/` |
| **Documentation** | UPPER_CASE.md | `README.md`, `LICENSE`, `CHANGELOG.md` |
| **Requirements** | kebab-case | `requirements/` |

---

## File Placement Patterns

- **Entry points**: Root-level `main_*.py` scripts
- **Requirements**: `requirements/` directory
- **Tests**: Root-level `test.py`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Multiple `main_*.py` entry points | ✅ Python CLI scripts |
| Has `requirements/` | ✅ Python dependencies |
| Has `test.py` | ✅ Python tests |
| GitHub community templates | ✅ ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE |

---

## Key Architecture Decisions

1. **Multiple entry points** — Four variants of the main script (with/without playlist, with/without loop).
2. **Flat structure** — All scripts at root level, no deep nesting.
3. **Community standards** — GitHub issue and PR templates.
4. **Comprehensive documentation** — Despite being simple Python scripts, has full project documentation suite.
5. **Modular requirements** — `requirements/` directory for dependency management.
