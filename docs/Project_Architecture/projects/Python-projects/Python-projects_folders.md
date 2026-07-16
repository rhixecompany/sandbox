# projects/Python-projects — Folder Structure Blueprint

## Overview
- Namespace: `projects/Python-projects`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
