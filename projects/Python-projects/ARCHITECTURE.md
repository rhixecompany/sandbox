# Architecture — Python-projects

## Overview
A collection of 18 standalone Python scripts, each self-contained and independently executable.

## Architecture Pattern

Each script follows this pattern:
```
Standalone Script
├── Imports (stdlib + requirements)
├── Helper Functions
├── Main Logic
└── Entry Point (if __name__ == "__main__")
```

## Design Principles
1. **Self-contained**: Each script runs independently
2. **No framework**: No web framework or dependency injection
3. **Minimal dependencies**: Only what's needed for each script
4. **CLI-based**: All scripts run via command line
5. **No tests**: Manual testing via direct execution

## Key Scripts
- `python_face_detection.py`: Uses OpenCV Haar cascades
- `web_scraper.py`: BeautifulSoup + requests
- `qr_code_generator.py`: qrcode library
- `email_sender.py`: smtplib + schedule
- `basic_calculator.py`: Pure Python, no dependencies
