# Copilot Instructions

Project-wide guidance for the Python scripts collection.

## Source of truth

- `projects/Python-projects/AGENTS.md`
- `README.md`
- individual script files

## Commands

Run from `projects/Python-projects/`:

```bash
pip install -r requirements.txt
ruff check .
mypy *.py
python basic_calculator.py
python qr_code_generator.py
python python_face_detection.py
```

## Architecture

- This is a collection of standalone Python scripts, not an application.
- Each script should remain self-contained and runnable on its own.
- Dependencies are limited to the script’s actual feature set.

## Conventions

- Keep files single-purpose and snake_case.
- Prefer typed annotations where practical.
- Avoid adding cross-script coupling unless the repo already uses it.
- Treat API keys and external requests as sensitive input.

