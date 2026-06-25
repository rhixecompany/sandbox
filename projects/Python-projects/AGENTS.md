# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

A collection of 18 beginner-friendly Python scripts for learning and automation. Covers a wide range of use cases from calculators and games to face detection and QR code generation.

**Tech Stack:**
- **Language**: Python 3.x (Python 2 not supported)
- **Key Libraries**: requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule
- **Linting**: ruff, mypy (type checking)
- **Template**: GitHub issue/PR templates included

<<<<<<< HEAD
=======
## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `projects/Python-projects/`; this
  file is the local fallback.
- `projects/Python-projects/.github/copilot-instructions.md` is the primary
  Copilot guidance file for this collection.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep this file, the local Copilot instructions, and the README aligned when
  adding or changing scripts.

>>>>>>> 0433dab (chore: initial local project setup for Python-projects)
## Setup Commands

```bash
# Clone and enter directory
cd Python-projects

# Install dependencies
pip install -r requirements.txt
```

## Development Workflow

```bash
# Run any script directly
python basic_calculator.py
python qr_code_generator.py
python python_face_detection.py
# ... and 15 more scripts

# Lint check
ruff check .

# Type check
mypy *.py
```

## Testing Instructions

No formal test framework — each script is self-contained and can be run directly. Manual testing via execution.

## Code Style

- **Python**: PEP 8, typed annotations encouraged (mypy configured), ruff for linting
- **Docs**: README documents each script's purpose
- **Each script**: Standalone, single-file, import-free (except standard library + requirements)
- **Naming**: snake_case for files and functions

## Build/Deployment

No build/deployment needed — these are standalone scripts. Run with `python script_name.py`.

## Security

- Never embed API keys or credentials directly in scripts
- scripts making HTTP requests (requests) should validate responses
- QR code generator does not store scanned data
- Face detection processes images locally
- Review any network calls for data privacy

## Troubleshooting

- **ModuleNotFoundError**: Run `pip install -r requirements.txt`
- **OpenCV errors**: Ensure opencv-python is installed and system has required visual libraries
- **Matplotlib not showing plots**: Use `plt.show()` or configure backend
- **Requests failing**: Check internet connection and target URL validity
- **Schedule not running**: Verify system time and schedule configuration
