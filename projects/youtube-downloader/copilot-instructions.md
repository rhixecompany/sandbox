# youtube-downloader — Python CLI Downloader

**Naming**: `snake_case` for Python file names, variables, and functions; `PascalCase` for classes; `UPPER_SNAKE_CASE` for constants; `kebab-case` for directories.

**Patterns**: Single-file CLI scripts; modular functions within each script; `if __name__ == "__main__":` guard; yt-dlp for core download functionality; curl_cffi for HTTP requests with fingerprint rotation; separate scripts for different modes (single video, playlist, loop mode); FFmpeg for format conversion.

**Structure**: `main_noplaylist.py` (single video download); `main_playlist.py` (playlist download); `main_loop_playlist.py` (batch loop mode); `test.py` (basic tests); root-level simple layout.

**Python**: Python 3.x; `yt-dlp` (YouTube downloading); `curl_cffi` (HTTP with TLS fingerprint spoofing); `ruff` for linting; `mypy` for optional type checking.

**Download Modes**: Single video (`main_noplaylist.py`); Playlist (`main_playlist.py`); Loop/batch (`main_loop_playlist.py`); configurable output formats.

**Rate Limiting**: Add delays between requests to respect rate limits; respect website terms of service; avoid aggressive parallel downloads.

**Security**: No `.env` or URLs committed; no API keys needed (yt-dlp uses public endpoints); FFmpeg for safe format conversion.

**Updates**: Keep `yt-dlp` updated (frequent YouTube changes); update via `pip install --upgrade yt-dlp curl_cffi`.

**Commands**: `pip install yt-dlp curl_cffi` (setup); `python main_noplaylist.py` (single video); `python main_playlist.py` (playlist); `python main_loop_playlist.py` (batch loop); `python test.py` (basic test); `ruff check . && mypy *.py` (lint/type check).
