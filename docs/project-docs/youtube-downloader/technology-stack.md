# Technology Stack — youtube-downloader

## Overview
Python-based YouTube video downloader with playlist support and loop mode. Uses yt-dlp and curl_cffi.

## Core Technologies
| Technology | Purpose |
|------------|---------|
| Python 3.x | Runtime |
| yt-dlp | Download engine (YouTube video/playlist) |
| curl_cffi | HTTP client for improved compatibility |

## Features
| Feature | Description |
|---------|-------------|
| Single video download | Download individual videos |
| Playlist download | Download entire playlists |
| Loop mode | Continuous batch processing |
| Quality options | 720p, 1080p, and other formats |

## Dev Tools
| Tool | Purpose |
|------|---------|
| djlint | HTML template linting |
| Faker | Test data generation |
| pre-commit | Git hooks |
| Sphinx | Documentation generation |

## Scripts
| File | Purpose |
|------|---------|
| main_noplaylist.py | Single video download |
| main_playlist.py | Playlist download |
| main_loop_noplaylist.py | Loop mode (single video) |
| main_loop_playlist.py | Loop mode (playlist) |
| test.py | Test suite |
