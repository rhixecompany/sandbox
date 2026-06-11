# Setup Guide

## Prerequisites

- Python 3.8+
- pip
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Python-projects
```

2. Create virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Available Scripts

Each script can be run directly with Python:
```bash
python <script_name>.py
```

See README.md for the list of available scripts and their purposes.

## Common Commands

| Command | Description |
| --- | --- |
| `python -m pytest` | Run tests |
| `ruff check .` | Run linter |
| `mypy .` | Run type checker |

## Troubleshooting

If you encounter issues:
1. Verify Python version (3.8+)
2. Update pip: `pip install --upgrade pip`
3. Reinstall requirements: `pip install -r requirements.txt`