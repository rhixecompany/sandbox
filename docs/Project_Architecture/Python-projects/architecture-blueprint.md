# Architecture Blueprint: Python-projects

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Language** | Python 3.x |
| **Key Libraries** | requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, smtplib |
| **Linting** | ruff, mypy |
| **No Framework** | All scripts are standalone, no web framework |
| **Package Manager** | pip |

### Architectural Pattern Detected

**Pattern:** Standalone Script Collection  
Each of the 18 Python scripts is **self-contained, independently executable**, and follows a consistent pattern:

```
Standalone Script
├── Imports (stdlib + requirements)
├── Helper Functions
├── Main Logic
└── Entry Point (if __name__ == "__main__")
```

---

## 2. Architectural Overview

### Design Principles

1. **Self-contained**: Each script runs independently with no shared state
2. **No framework**: No web framework, dependency injection, or OOP patterns
3. **Minimal dependencies**: Only what's needed for each specific script
4. **CLI-based**: All scripts run via command line (`python script.py`)
5. **No formal testing**: Manual testing via direct execution

### Key Scripts

| Script | Purpose | Dependencies |
|---|---|---|
| `basic_calculator.py` | Arithmetic operations | None (stdlib) |
| `python_face_detection.py` | Face detection via OpenCV | opencv-python |
| `qr_code_generator.py` | Generate QR codes | qrcode, pillow |
| `email_sender.py` | Send scheduled emails | smtplib, schedule |
| `web_scraper.py` | Scrape web content | requests, beautifulsoup4 |
| `currency_converter.py` | Currency conversion | requests (API) |
| `graph_plotter.py` | Plot mathematical graphs | matplotlib |
| `quiz_program.py` | Interactive quiz application | None (stdlib) |
| `dice_rolling_simulator.py` | Simulate dice rolls | None (stdlib) |

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| Single-file scripts | Easy to understand, modify, and share |
| No test framework | Each script is small enough for manual verification |
| Standard entry point pattern | Consistent `if __name__ == "__main__"` guard |

---

## 4. Extensibility Points

1. **New scripts**: Add a new `.py` file following the established pattern
2. **Library upgrades**: Update `requirements.txt` with new versions
3. **GUI wrappers**: Wrap any script with a Tkinter or PyQt interface
4. **CLI arguments**: Add `argparse` for configurable parameters

---

*End of architecture blueprint.*
