# projects/Python-projects — Architecture Blueprint

## Overview
- Detected stack: Python
- Architectural pattern: Python service or utility project
- Top-level components: docs

## Component Map
- `docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
Python-projects/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── copilot-instructions.md
├── .ruff_cache/
│   ├── 0.15.10/
│   └── CACHEDIR.TAG
├── AGENTS.md
├── AUDIT_Python-projects.md
├── automate_morning_text.py
├── basic_calculator.py
├── binary_search_algorithm.py
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── currency_converter.py
├── dice_rolling_simulator.py
├── email_sender.py
├── email_slicer.py
├── graph_plotter.py
├── image_resizer.py
├── interest_payment_calculator.py
├── leap_year_checker.py
├── LICENSE
├── python_face_detection.py
├── qr_code_generator.py
├── quiz_program.py
├── random_password_generator.py
├── README.md
├── REPOSITORY_SUMMARY.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── rock_paper_scissors.py
├── site_connectivity_checker.py
├── THE_STORY_OF_THIS_REPO.md
├── web-research-python-projects.md
├── word_dictionary.py
└── word_replacement.py
```

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
