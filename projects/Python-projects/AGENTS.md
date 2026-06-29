# Python-projects — 18 Beginner Scripts

## Architecture
- **Type:** Collection of standalone Python scripts
- **Pattern:** Single-file modular scripts, no framework
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Python 3.x scripts collection: calculator, games, face detection, QR code generator, web scraper, and more. Each script is standalone with no shared dependencies.

## Stack
- **Language:** Python 3.x
- **Key Libraries:** `requests`, `opencv-python`, `matplotlib`, `pillow`, `qrcode`, `beautifulsoup4`, `PyDictionary`, `schedule`
- **Quality:** `ruff` (lint), `mypy` (type check)

## Commands
```bash
pip install -r requirements.txt
python basic_calculator.py
python qr_code_generator.py
ruff check .
mypy *.py
```

## Conventions
- PEP 8 style, `snake_case` naming
- Standalone scripts — no formal test framework
- Each script documented in its own header and referenced in README
- `requirements.txt` for shared dependencies
- Type hints encouraged for new scripts

## Notes
- No framework or shared code between scripts
- `opencv-python` requires proper system dependencies
- README documents each script's purpose and usage
