# Project Folder Structure Blueprint

## Project: Python-projects — Collection of Python Scripts

**Generated:** 2026-06-25  
**Project Type:** Python Scripts Collection  
**Auto-detected:** Yes (Python — `.py files`, `.ruff_cache/`, `.github/ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE/`)

---

## Directory Tree

```
Python-projects/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .ruff_cache/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
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
├── automate_morning_text.py
├── basic_calculator.py
├── binary_search_algorithm.py
├── code-exemplars.md
├── copilot-instructions.md
├── cross-linking-report.md
├── currency_converter.py
├── dice_rolling_simulator.py
├── docs/
│   └── Project_Architecture/
├── email_sender.py
├── email_slicer.py
├── execution-summary.md
├── folder-structure.md
├── graph_plotter.py
├── image_resizer.py
├── interest_payment_calculator.py
├── project-workflow.md
├── technology-stack.md
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Python scripts** | snake_case.py | `basic_calculator.py`, `email_sender.py`, `dice_rolling_simulator.py` |
| **Config/setup** | dotted-prefix | `.github/`, `.ruff_cache/`, `.vscode/` |
| **Documentation** | UPPER_CASE.md | `README.md`, `LICENSE`, `CODE_OF_CONDUCT.md` |
| **Reports** | kebab-case.md | `code-exemplars.md`, `folder-structure.md` |

---

## File Placement Patterns

- **Python scripts**: All at root level (flat structure)
- **Docs**: `docs/`
- **Community standards**: `.github/ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE/`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Flat `.py` files | ✅ Python script collection |
| Has `.ruff_cache` | ✅ Ruff linter |
| Has GitHub templates | ✅ Community standards |
| Has comprehensive docs | ✅ Full documentation suite |

---

## Key Architecture Decisions

1. **Flat structure** — All Python scripts at root level, no subdirectories beyond docs.
2. **Educational focus** — Scripts cover fundamental programming concepts (calculator, dice roller, email sender, image resizer, etc.).
3. **Full documentation suite** — Despite being simple scripts, has comprehensive project documentation.
4. **Community-ready** — GitHub issue and PR templates for contributions.
5. **No dependencies** — Individual self-contained scripts.
