# RESEARCH_REPORT.md

## Project: youtube-downloader

**Type:** Python desktop YouTube downloader
**Tech Stack:** Python, yt-dlp, tkinter GUI, ffmpeg
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|-------------|
| yt-dlp | https://github.com/yt-dlp/yt-dlp | Core dependency (174k stars, 1,700+ site support) |
| pytube | https://github.com/pytube/pytube | Alternative YouTube download library |

## Key Findings

### yt-dlp Best Practices (2026)
- Use format expressions (`bestvideo[height<=1080]+bestaudio/best[height<=1080]`) instead of numeric format IDs (yt-dlp docs)
- `--download-archive` prevents re-downloading previously downloaded videos in batch mode
- The Python API (`yt_dlp.YoutubeDL`) provides cleaner programmatic access than CLI subprocess calls
- Post-processor system handles format merging, audio extraction, and thumbnail embedding

### Python Desktop Apps
- tkinter remains the standard for lightweight Python desktop UIs (docs.python.org)
- Threading is essential for non-blocking downloads in GUI apps — never call yt-dlp on the main thread
- PyInstaller is the recommended packager for Windows distribution (`--onefile --windowed`)

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| yt-dlp Python API | https://github.com/yt-dlp/yt-dlp#embedding-examples | Integration guide |
| tkinter Docs | https://docs.python.org/3/library/tkinter.html | GUI framework docs |
| ffmpeg Python | https://github.com/kkroening/ffmpeg-python | FFmpeg wrapper |

## Best Practices

1. **Use yt-dlp Python API** over CLI subprocess — Better error handling and integration
2. **Thread downloads** — tkinter GUI freezes during synchronous downloads; use threading or multiprocessing
3. **Validate URLs before downloading** — Prevent wasting time on invalid URLs
4. **Use format selection strings** — Future-proof against format ID changes on YouTube's end
5. **Handle DownloadError gracefully** — User-friendly error messages instead of raw tracebacks

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Subprocess CLI for yt-dlp | No error handling, hard to parse output | Use yt_dlp.YoutubeDL Python API |
| Blocking main thread | GUI freezes during downloads | Use threading.Thread for downloads |
| Missing ffmpeg | Failed format merging | Check ffmpeg presence on startup |
| Fixed format IDs | Broken when YouTube changes formats | Use format selection expressions |

## Performance

1. **Best quality selection** matches desired resolution without downloading unnecessary data
2. **--download-archive** avoids redundant downloads in batch mode
3. **FFmpeg pipe mode** merges video+audio streams efficiently without temp files
4. **Rate limiting** via `--limit-rate` prevents saturating the network connection
5. **Concurrent downloads** possible with multiple YoutubeDL instances

## Security

1. **Never use `--compat-options allow-unsafe-ext`** — RCE risk (yt-dlp security advisory)
2. **Validate download URLs** against expected format before passing to yt-dlp
3. **Sanitize filenames** from video titles to prevent path injection
4. **Run yt-dlp with restricted network access** — Use `--no-check-certificate` only in controlled environments

## Related Projects (in workspace)

- **Python-projects** — Python scripting patterns and packaging setup
- **selenium_webdriver** — Python-based tooling, shares packaging/pyproject patterns
- **comicwise** — Shares CLI tooling patterns (yt-dlp model for CLI design)

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| yt-dlp | https://github.com/yt-dlp/yt-dlp | YouTube downloader library |
| tkinter | https://docs.python.org/3/library/tkinter.html | Python GUI framework |
| PyInstaller | https://pyinstaller.org | Windows distribution packaging |
| ffmpeg | https://ffmpeg.org | Audio/video processing |
