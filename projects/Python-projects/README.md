# Python-projects — 18 Beginner Scripts

> **Stack:** Python 3.x | **Type:** Script Collection (Educational/Utility) | **Status:** Active

A collection of 18 standalone Python scripts covering various domains: calculators, games, face detection, QR code generation, web scraping, utilities, and more. Designed as learning/utility scripts.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Language** | Python ^3.x |
| **Linting** | ruff |
| **Type Checking** | mypy |

### Dependencies

| Library | Purpose |
|---|---|
| **requests** | HTTP requests |
| **opencv-python** | Face detection, image processing |
| **matplotlib** | Data visualization |
| **pillow** | Image manipulation |
| **qrcode** | QR code generation |
| **beautifulsoup4** | Web scraping |
| **PyDictionary** | Dictionary API |
| **schedule** | Task scheduling |

## Project Structure

```
Python-projects/
├── basic_calculator.py      # Calculator
├── qr_code_generator.py     # QR code generator
├── ... (18 scripts total)
├── requirements.txt
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run any script directly
python basic_calculator.py
python qr_code_generator.py

# Lint and type check
ruff check .
mypy *.py
```

## Key Features

- **Calculator** — Basic arithmetic operations
- **QR Code Generator** — Generate QR codes from text/URLs
- **Face Detection** — OpenCV-based face detection
- **Web Scraping** — BeautifulSoup-based scraping utilities
- **Data Visualization** — Matplotlib-based charts and plots
- **Image Processing** — Pillow-based image manipulation
- **Dictionary Tool** — PyDictionary powered lookups
- **Task Scheduling** — Schedule library for automation

## Coding Standards

- **PEP 8**: Python style guide
- **snake_case**: Variable/function naming
- **Standalone scripts**: Each script is independently executable
- **Type annotations**: Optional type hints via mypy
- **Module docstring**: Each script includes documentation
- **Import order**: Standard library → third-party
- **Entry point**: `if __name__ == "__main__":` guard

## Quality

| Tool | Usage |
|---|---|
| **ruff** | Code linting (all rules) |
| **mypy** | Optional type checking |
| **Manual testing** | No formal test suite (standalone scripts) |

## Security

- No embedded secrets in scripts
- Validate HTTP responses in web scraping scripts
- Prefer local image processing where possible

## License

Not specified.
