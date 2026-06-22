# youtube-downloader
**Python**: PEP 8, `snake_case`, type hints, try/except for network/download failures.
**Scripts**: clear purpose per script (`noplaylist`, `playlist`, `loop` modes); simple CLI.
**Updates**: keep `yt-dlp` current (`pip install -U yt-dlp`).
**Security**: validate URLs (SSRF prevention), respect YouTube ToS, no mass/commercial use, scan downloads for malware.
**Common**: update yt-dlp on failures; install FFmpeg for conversions; add delays to avoid rate limiting.
