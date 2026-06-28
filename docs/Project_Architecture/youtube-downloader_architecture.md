# youtube-downloader — Architecture

## Overview
A Python-based YouTube video downloader with playlist support, quality selection, and continuous loop mode. Uses yt-dlp as the download engine with curl_cffi for improved compatibility.

## Architecture Pattern
- **Type:** CLI Tool
- **Pattern:** Single-purpose Python scripts with shared library
- **Interface:** Command-line only (no web UI)

## Components
- **`main_noplaylist.py`** — Single video download
- **`main_playlist.py`** — Playlist download
- **`main_loop_noplaylist.py`** — Loop mode for single videos
- **`main_loop_playlist.py`** — Loop mode for playlists
- **`test.py`** — Test harness
- **`requirements/`** — Split requirement files (base, local)

## Cross-Cutting Concerns
- **Quality Options:** Multiple quality levels (720p, 1080p, etc.)
- **Error Handling:** Network failure and download error management
- **Rate Limiting:** Built-in delays to avoid YouTube throttling

## Data Flow
1. User passes video/playlist URL to script
2. yt-dlp engine handles download negotiation
3. Video saved to local filesystem with specified quality
4. In loop mode, script continues to next URL after completion
