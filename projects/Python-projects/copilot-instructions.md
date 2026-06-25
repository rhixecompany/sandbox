# Python-projects — 18 Beginner Scripts

**Naming**: `snake_case` for Python file names, variables, and functions; `PascalCase` for classes; `UPPER_SNAKE_CASE` for constants; `kebab-case` for directories.

**Patterns**: Standalone single-file scripts (no project-level imports); shebang lines (`#!/usr/bin/env python3`); modular functions within each file; `if __name__ == "__main__":` guard for all scripts; minimal dependencies per script.

**Structure**: Root-level Python files; each file is an independent utility/script; `requirements.txt` lists all dependencies; no formal test suite; scripts documented via inline comments and README.

**Python**: Python 3.x; PEP 8 style via ruff linter; type hints via mypy; standard library usage preferred; no frameworks; scripts include: calculator, games, face detection, QR generator, web scraper, dictionary tool, scheduler.

**Key Libraries**: `requests` (HTTP), `opencv-python` (face detection), `matplotlib` (plots), `pillow` (images), `qrcode` (QR generation), `beautifulsoup4` (scraping), `PyDictionary` (dictionary), `schedule` (task scheduling).

**Linting**: `ruff check .` for linting; `mypy *.py` for type checking; README documents each script's purpose and usage.

**Security**: No secrets committed; avoid running untrusted input; validate URLs before scraping; rate-limit external requests.

**Commands**: `pip install -r requirements.txt` (setup); `python basic_calculator.py` (run specific script); `python qr_code_generator.py`; `ruff check .` (lint); `mypy *.py` (type check).
