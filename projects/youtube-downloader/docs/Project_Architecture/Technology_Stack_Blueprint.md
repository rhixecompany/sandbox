# Technology Stack Blueprint

## Project: youtube-downloader — CLI Downloader

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A Python CLI tool for downloading YouTube videos (single, playlist, and loop mode) using yt-dlp and curl_cffi. Designed for simplicity with no web deployment.

**Project Type:** CLI Utility Tool  
**Stack Type:** Python

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.x | Primary language |

### Dependencies

| Library | Version | Purpose |
|---|---|---|
| yt-dlp | latest | YouTube video/audio download |
| curl_cffi | latest | HTTP requests with fingerprinting |

### Development Tools

| Tool | Purpose |
|---|---|
| ruff | Optional linting |
| mypy | Optional type checking |
| FFmpeg | Video/audio format conversions (external) |

---

## Licensing

| Component | License |
|---|---|
| youtube-downloader | (not specified) |

---

## Project Files

| File | Purpose |
|---|---|
| `main_noplaylist.py` | Single video download |
| `main_playlist.py` | Playlist download |
| `main_loop_playlist.py` | Batch loop mode for playlists |
| `test.py` | Basic test script |

---

## Key Commands

| Command | Description |
|---|---|
| `pip install yt-dlp curl_cffi` | Install dependencies |
| `python main_noplaylist.py` | Download single video |
| `python main_playlist.py` | Download playlist |
| `python main_loop_playlist.py` | Batch loop download |
| `python test.py` | Run test |
| `ruff check . && mypy *.py` | Lint & type check |

---

## Coding Conventions

- **PEP 8**: Python style guide
- **Single CLI tool**: No web deployment
- **Environment**: `.env`/URLs never committed
- **Rate limiting**: Built-in delays to respect YouTube rate limits
- **FFmpeg**: Required for format conversions

---

## Architecture

```
youtube-downloader/
├── main_noplaylist.py     # Single video downloader
├── main_playlist.py       # Playlist downloader
├── main_loop_playlist.py  # Batch loop downloader
├── test.py                # Test script
└── AGENTS.md
```

---

## Dependencies

| Library | Purpose |
|---|---|
| yt-dlp | YouTube downloading (active fork of youtube-dl) |
| curl_cffi | Advanced HTTP fingerprinting |

---

## Notes

- Keep yt-dlp updated for continued functionality
- FFmpeg required for audio extraction and format conversion
- Respect rate limits with built-in delays
- No web deployment — pure CLI tool
