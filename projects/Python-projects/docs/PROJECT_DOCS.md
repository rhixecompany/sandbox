# Python Projects Documentation

## Overview

A collection of 18 standalone Python utility scripts for common automation, data processing, and system administration tasks. Each script is self-contained, has minimal dependencies, and can be used independently.

**Repository:** https://github.com/Rhixe-company/Python-projects  
**Stack:** Python 3.8+ | Standard Library + Optional Dependencies  
**Status:** Stable / Maintenance

---

## Script Index

| # | Script | Category | Dependencies | Lines |
|---|--------|----------|-------------|-------|
| 1 | site_connectivity_checker.py | Network | requests | ~80 |
| 2 | server_status_checker.py | Network | socket (stdlib) | ~60 |
| 3 | qr_code_generator.py | Image | qrcode, Pillow | ~70 |
| 4 | image_resizer.py | Image | Pillow | ~90 |
| 5 | image_to_pdf_converter.py | Image | Pillow | ~60 |
| 6 | currency_converter.py | Data | requests (optional) | ~100 |
| 7 | csv_json_converter.py | Data | csv, json (stdlib) | ~70 |
| 8 | json_formatter.py | Data | json (stdlib) | ~50 |
| 9 | file_organizer.py | Files | os, shutil (stdlib) | ~110 |
| 10 | duplicate_finder.py | Files | hashlib (stdlib) | ~80 |
| 11 | text_analyzer.py | Text | collections, re (stdlib) | ~90 |
| 12 | markdown_to_html_converter.py | Text | markdown (optional) | ~70 |
| 13 | web_scraper.py | Automation | requests, beautifulsoup4 | ~100 |
| 14 | email_sender.py | Automation | smtplib (stdlib) | ~80 |
| 15 | password_generator.py | Security | secrets (stdlib) | ~60 |
| 16 | disk_usage_analyzer.py | System | os (stdlib) | ~90 |
| 17 | system_info_collector.py | System | psutil | ~100 |
| 18 | batch_file_renamer.py | System | os, re (stdlib) | ~120 |

---

## Quick Start

### Prerequisites

```bash
# Python 3.8+
python --version

# Install common dependencies (varies by script)
pip install requests Pillow qrcode beautifulsoup4 psutil yt-dlp
```

### Running a Script

```bash
# Most scripts support command-line arguments
python site_connectivity_checker.py https://example.com

python qr_code_generator.py "https://example.com" -o myqr.png

python currency_converter.py 100 USD EUR

python file_organizer.py ~/Downloads --dry-run

python password_generator.py --length 20 --no-symbols

python batch_file_renamer.py ./photos "IMG_(\d+)" "vacation_\1" --dry-run
```

### Using as a Module

```python
# Scripts can be imported and their core functions reused
from qr_code_generator import generate_qr
from currency_converter import convert_currency
from password_generator import generate_password

qr_path = generate_qr("https://example.com", "myqr.png")
converted = convert_currency(100, "USD", "EUR", {"USD": 1.0, "EUR": 0.85})
password = generate_password(length=20)
```

---

## Usage Guide

### Network Scripts

**Connectivity Checker:**
```bash
# Single URL check
python site_connectivity_checker.py https://example.com

# Batch check from file
python site_connectivity_checker.py --file urls.txt

# Custom timeout
python site_connectivity_checker.py https://example.com --timeout 30
```

**Server Status Checker:**
```bash
# Check a specific port
python server_status_checker.py example.com --port 443

# Scan common ports
python server_status_checker.py example.com --common-ports
```

### Image Scripts

**QR Code Generator:**
```bash
# Basic QR code
python qr_code_generator.py "https://example.com"

# Custom colors
python qr_code_generator.py "https://example.com" --fill red --back lightyellow
```

**Image Resizer:**
```bash
# Resize to specific dimensions
python image_resizer.py input.jpg output.jpg --width 800 --height 600

# Maintain aspect ratio
python image_resizer.py input.jpg output.jpg --width 400 --maintain-aspect
```

### Data Scripts

**Currency Converter:**
```bash
# Convert with live rates
python currency_converter.py 100 USD EUR

# Interactive mode
python currency_converter.py --interactive
```

**CSV/JSON Converter:**
```bash
# CSV to JSON
python csv_json_converter.py data.csv data.json

# JSON to CSV
python csv_json_converter.py data.json data.csv
```

### File Management Scripts

**File Organizer:**
```bash
# Preview organization
python file_organizer.py ~/Downloads --dry-run

# Execute organization
python file_organizer.py ~/Downloads

# Custom rules
python file_organizer.py ~/Downloads --config rules.json
```

**Duplicate Finder:**
```bash
# Scan directory
python duplicate_finder.py ~/Documents

# Output report
python duplicate_finder.py ~/Documents --output duplicates.json

# Delete duplicates (with confirmation)
python duplicate_finder.py ~/Documents --delete
```

**Batch File Renamer:**
```bash
# Replace text in filenames
python batch_file_renamer.py ./photos "old_" "new_"

# Add numbering
python batch_file_renamer.py ./files "" "photo_###" --counter

# Dry run (no changes)
python batch_file_renamer.py ./files ".txt" ".md" --dry-run
```

### Security Scripts

**Password Generator:**
```bash
# Default 16-char password
python password_generator.py

# Custom options
python password_generator.py --length 24 --no-symbols

# Batch generate
python password_generator.py --count 5 --length 20
```

---

## Installing Dependencies

```bash
# Install all optional dependencies
pip install -r requirements.txt

# Or install per category:
# Network scripts
pip install requests

# Image scripts
pip install Pillow qrcode

# Web scraping
pip install beautifulsoup4 requests

# System monitoring
pip install psutil

# Media
pip install yt-dlp
```

### requirements.txt

```
requests>=2.28.0
Pillow>=9.4.0
qrcode>=7.4.0
beautifulsoup4>=4.11.0
psutil>=5.9.0
yt-dlp>=2023.0.0
```

---

## Development

### Adding a New Script

1. Create a new `.py` file following the established pattern:
   - Module docstring at top
   - `argparse`-based CLI interface
   - Core function with typed Python signature
   - `if __name__ == "__main__": main()` block
2. Add the script to this documentation index
3. Test with sample inputs

### Code Style

- Follow PEP 8 conventions
- Use type hints for all function signatures
- Write Google-style docstrings
- Keep scripts under 200 lines
- Minimize external dependencies

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Install missing dependency with pip |
| `ConnectionError` | Check internet connection and URL validity |
| `PermissionError` | Check file write permissions |
| `FileNotFoundError` | Verify input file path exists |

### Debug Mode

```bash
# Most scripts support verbose/debug output
python web_scraper.py https://example.com --verbose
python system_info_collector.py --debug
```
