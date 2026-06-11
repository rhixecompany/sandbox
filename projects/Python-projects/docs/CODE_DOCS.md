# Python Projects Code Documentation

## Overview

A collection of 18 standalone Python utility scripts for various automation and productivity tasks. Each script is self-contained with no shared modules or dependencies beyond the Python standard library and commonly available packages.

**Stack:** Python 3.8+ | Standard Library + Common Packages (requests, Pillow, qrcode, yt-dlp)

---

## Script Catalog

### Network & Connectivity

#### site_connectivity_checker.py
```python
# Purpose: Check website connectivity by sending HTTP requests
def check_site(url: str, timeout: int = 10) -> dict:
    """Check if a website is reachable and return status information.

    Args:
        url: The URL to check (with or without protocol prefix).
        timeout: Request timeout in seconds (default: 10).

    Returns:
        dict with keys: url, status_code, response_time, reachable
    """
```
- Input: URL (optional protocol; http:// prepended if missing)
- Output: JSON-like dict with connectivity status
- Error handling: TimeoutException, ConnectionError, general exceptions
- Dependencies: `requests`

#### server_status_checker.py
```python
def check_server(host: str, port: int) -> dict:
    """Check if a TCP port is open on a remote host."""
```
- TCP port scanning for server availability
- Uses `socket` module for low-level connectivity checks
- Batch host/port scanning support

### Image Processing

#### qr_code_generator.py
```python
import qrcode
from qrcode.image.pil import PilImage

def generate_qr(data: str, filename: str = "qrcode.png",
                fill_color: str = "black", back_color: str = "white") -> str:
    """Generate a QR code image from input data.

    Args:
        data: The data to encode in the QR code (URL, text, etc.).
        filename: Output file path (default: qrcode.png).
        fill_color: QR code foreground color (default: black).
        back_color: QR code background color (default: white).

    Returns:
        Path to the generated QR code image file.
    """
```
- Customizable colors and sizes
- Error correction level configuration
- Dependencies: `qrcode`, `Pillow`

#### image_resizer.py
```python
from PIL import Image

def resize_image(input_path: str, output_path: str,
                 width: int, height: int,
                 maintain_aspect: bool = True) -> str:
    """Resize an image file to specified dimensions.

    Args:
        input_path: Source image path.
        output_path: Destination path.
        width: Target width in pixels.
        height: Target height in pixels.
        maintain_aspect: Whether to preserve aspect ratio (default: True).
    """
```
- Supports JPEG, PNG, GIF, WebP formats
- Aspect ratio preservation mode
- Batch processing support
- Dependencies: `Pillow`

#### image_to_pdf_converter.py
```python
def convert_images_to_pdf(image_paths: list[str], output_path: str) -> str:
    """Convert one or more images to a single PDF document."""
```
- Multiple images merged into a single PDF
- Page ordering and orientation control
- Dependencies: `Pillow`

### Data Processing

#### currency_converter.py
```python
# Uses float arithmetic for currency conversion calculations
def convert_currency(amount: float, from_currency: str,
                     to_currency: str, rates: dict[str, float]) -> float:
    """Convert an amount between currencies using provided exchange rates.

    Args:
        amount: The amount to convert.
        from_currency: Source currency code (e.g., 'USD').
        to_currency: Target currency code (e.g., 'EUR').
        rates: Dict mapping currency codes to their USD exchange rate.

    Returns:
        Converted amount rounded to 2 decimal places.
    """
```
- Manual exchange rate calculation
- Supports common currency codes
- Interactive mode with user input
- Dependencies: `requests` (for live rates)

#### csv_json_converter.py
```python
import csv, json

def csv_to_json(csv_path: str, json_path: str,
                delimiter: str = ',', encoding: str = 'utf-8') -> None:
    """Convert a CSV file to JSON format.

    Args:
        csv_path: Path to input CSV file.
        json_path: Path to output JSON file.
        delimiter: CSV delimiter character.
        encoding: File encoding.
    """
```
- Bidirectional CSV ↔ JSON conversion
- Custom delimiter support
- Encoding handling

#### json_formatter.py
```python
import json

def format_json(input_path: str, output_path: str | None = None,
                indent: int = 2) -> str:
    """Pretty-print a JSON file with configurable indentation."""
```
- Pretty-printing with configurable indentation
- File or stdout output
- Error reporting for malformed JSON

### Text & File Processing

#### file_organizer.py
```python
import os, shutil
from pathlib import Path

def organize_by_extension(directory: str, dry_run: bool = False) -> dict:
    """Organize files into subdirectories by file extension.

    Args:
        directory: Target directory to organize.
        dry_run: If True, only preview changes without moving files.

    Returns:
        dict with counts of files organized by extension category.
    """
```
- Sorts files into extension-based folders (Documents, Images, Audio, Video, Archives, Code)
- Dry-run mode for preview
- Logging of all file operations

#### duplicate_finder.py
```python
import hashlib

def find_duplicates(directory: str, recursive: bool = True) -> list[list[str]]:
    """Find duplicate files in a directory using MD5 hashing.

    Args:
        directory: Root directory to scan.
        recursive: Whether to scan subdirectories.

    Returns:
        List of groups of duplicate file paths.
    """
```
- MD5 hash-based duplicate detection
- Optional SHA-256 for higher reliability
- Size pre-filtering for performance
- JSON report export

#### text_analyzer.py
```python
from collections import Counter
import re

def analyze_text(text: str) -> dict:
    """Analyze text and return statistics.

    Returns:
        dict with keys: word_count, char_count, sentence_count,
        avg_word_length, most_common_words, unique_words
    """
```
- Word, character, sentence, and paragraph counts
- Lexical diversity (unique/ total word ratio)
- Most common words with frequency
- Readability score estimation

#### markdown_to_html_converter.py
```python
def md_to_html(md_path: str, html_path: str,
               css_path: str | None = None) -> None:
    """Convert a Markdown file to HTML."""
```
- Basic Markdown syntax support (headings, lists, code blocks, links, images, tables)
- Optional CSS styling
- Code syntax highlighting (if pygments available)

### Automation

#### web_scraper.py
```python
from bs4 import BeautifulSoup

def scrape_page(url: str, selector: str,
                attribute: str | None = None) -> list[str]:
    """Scrape content from a web page using CSS selectors.

    Args:
        url: Target URL.
        selector: CSS selector for target elements.
        attribute: Specific attribute to extract (None for text content).

    Returns:
        List of extracted content strings.
    """
```
- CSS selector-based extraction
- Attribute or text content extraction
- Pagination support (next page URL pattern)
- Dependencies: `requests`, `beautifulsoup4`

#### email_sender.py
```python
import smtplib
from email.message import EmailMessage

def send_email(smtp_server: str, port: int,
               sender: str, password: str,
               recipient: str, subject: str,
               body: str, html: bool = False) -> bool:
    """Send an email via SMTP.

    Returns:
        True if sent successfully, False otherwise.
    """
```
- SMTP over SSL/TLS
- Plain text and HTML email support
- CC/BCC recipients
- File attachment support

#### password_generator.py
```python
import secrets, string

def generate_password(length: int = 16,
                      use_uppercase: bool = True,
                      use_lowercase: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    """Generate a cryptographically secure random password.

    Args:
        length: Password length (default: 16, min: 8).
        use_uppercase: Include uppercase letters.
        use_lowercase: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include special characters.

    Returns:
        A cryptographically secure random password string.
    """
```
- Uses `secrets` module (not `random`) for cryptographic security
- Configurable character sets
- Entropy estimation display
- Bulk password generation (passphrase mode)

### System & Monitoring

#### disk_usage_analyzer.py
```python
import os

def analyze_disk_usage(path: str, top_n: int = 20) -> list[dict]:
    """Analyze disk usage for a given directory path.

    Returns:
        List of dicts with path, size, type (file/dir), last_modified.
        Sorted by size descending.
    """
```
- Recursive directory size calculation
- Human-readable size formatting (KB, MB, GB, TB)
- Top N largest files/folders
- Export to CSV report

#### system_info_collector.py
```python
import platform, psutil

def collect_system_info() -> dict:
    """Collect comprehensive system information.

    Returns:
        dict with: os, version, cpu_count, cpu_percent, memory_total,
        memory_available, disk_usage, network_interfaces, boot_time
    """
```
- Cross-platform system information (Windows, macOS, Linux)
- CPU, memory, disk, network metrics
- Running processes listing
- Export to JSON/CSV
- Dependencies: `psutil`

#### batch_file_renamer.py
```python
import os, re

def rename_files(directory: str, pattern: str,
                 replacement: str, recursive: bool = False,
                 dry_run: bool = True) -> list[tuple[str, str]]:
    """Batch rename files using regex pattern matching.

    Args:
        directory: Target directory.
        pattern: Regex pattern to match in filenames.
        replacement: Replacement string (supports regex backreferences).
        dry_run: If True, only preview changes.

    Returns:
        List of (original_name, new_name) tuples.
    """
```
- Regex-based pattern matching and replacement
- Numbering sequence insertion (`file_001.jpg`)
- Date-based naming (`2026-05-21_file.txt`)
- Extension change
- Dry-run mode for safety
- Undo/rollback capability

### Media

#### youtube_downloader_standalone.py
```python
import yt_dlp

def download_video(url: str, output_path: str = "downloads",
                   quality: str = "best",
                   audio_only: bool = False) -> dict:
    """Download a video from YouTube or other supported platforms.

    Args:
        url: Video URL.
        output_path: Download directory.
        quality: Video quality preference.
        audio_only: Extract audio only (MP3).

    Returns:
        dict with filename, filesize, duration, format.
    """
```
- yt-dlp integration for multi-platform support (YouTube, Vimeo, etc.)
- Quality selection (best, 1080p, 720p, 480p)
- Audio-only extraction (MP3, M4A)
- Playlist download support
- Subtitle download
- Progress callback for UI integration
- Dependencies: `yt-dlp`

---

## Shared Utilities Pattern

Most scripts follow this pattern:
```python
#!/usr/bin/env python3
"""Module docstring describing the script's purpose."""

import sys
import argparse

def main():
    """Parse arguments and execute the core function."""
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument(...)
    args = parser.parse_args()
    result = core_function(args.input)
    print(result)

def core_function(param: str) -> Any:
    """Core logic, designed to be importable by other scripts."""
    pass

if __name__ == "__main__":
    main()
```

### Testing Pattern

Scripts include a `if __name__ == "__main__"` block with:
- Direct execution mode with CLI arguments
- Example usage in docstring
- No formal test framework — manual testing via CLI
