# Python-projects — Architecture

## Overview
A collection of 18 beginner-friendly Python scripts for learning, automation, and experimentation. Each script is self-contained and demonstrates a specific programming concept.

## Architecture Pattern
- **Type:** Script Collection
- **Pattern:** Standalone single-file scripts
- **Structure:** Flat directory, no shared modules or packages

## Components
- **Scripts (18 total)** — Each is a standalone `.py` file:
  - Calculators: `basic_calculator.py`, `interest_payment_calculator.py`, `currency_converter.py`
  - Games: `rock_paper_scissors.py`, `dice_rolling_simulator.py`, `quiz_program.py`
  - Utilities: `qr_code_generator.py`, `random_password_generator.py`, `email_sender.py`, `email_slicer.py`
  - Data Processing: `word_replacement.py`, `word_dictionary.py`, `binary_search_algorithm.py`
  - Visualization: `graph_plotter.py`, `image_resizer.py`
  - Automation: `site_connectivity_checker.py`, `leap_year_checker.py`, `python_face_detection.py`

## Cross-Cutting Concerns
- All scripts use standard library except those requiring `pip install -r requirements.txt`
- No formal test framework — each script is manually executable
- `ruff` and `mypy` configured for linting and type checking
