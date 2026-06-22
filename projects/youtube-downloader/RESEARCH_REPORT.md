# RESEARCH_REPORT.md

## Project: youtube-downloader
**Type:** YouTube CLI download tool
**Tech Stack:** Python 3.x, yt-dlp, curl_cffi, pytest, mypy, ruff, black
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| Python-projects | `projects/Python-projects` | Shared Python CLI + requirements hygiene pattern. |
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation alternatives for scraping. |

## Key Findings
### yt-dlp + curl_cffi Best Practices (2026)
- **yt-dlp is the gold standard** — actively maintained with daily updates (March 2026); 1800+ sites supported; best open-source option for YouTube [1]
- **Always install `yt-dlp[curl-cffi]`** — preserves compatibility with YouTube bot protection/throttling; Chrome TLS fingerprint impersonation [1]
- **Rate limiting is aggressive** — YouTube enforces 5-6s sleeps, 75% block rate for yt-dlp; JDownloader handles better via different client impersonation [2]
- **Fix for "Sign in to confirm you're not a bot"**: `yt-dlp --cookies-from-browser chrome --extractor-args "youtube:player_client=tv"` [1]
- **Version pinning** — pin `yt-dlp` in requirements or auto-upgrade in `main()` on validation failure; `--no-update` for reproducible builds [1]
### Python CLI Design: typer vs click vs argparse (2026)
- **argparse (stdlib)** — zero deps; best for single-file scripts, simple flags; subcommands via `add_subparsers()` [4]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| yt-dlp 2026 guide | https://www.devkantkumar.com/blog/yt-dlp-ultimate-guide-2026 | Guide |

## Best Practices
1. **Explicit CLI commands over interactive prompts** — `download single --url URL --quality 1080p` enables automation/pipelines
2. **Pin `yt-dlp` with auto-upgrade fallback** — `yt-dlp==2026.3.15` in requirements; `main()` checks version on validation failure
3. **Install `yt-dlp[curl-cffi]`** — Chrome TLS fingerprint bypasses YouTube bot protection

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unbounded output filenames | FS conflicts, overwrites | Sanitize + prefix: `{type}_{timestamp}_{sanitized_title}.{ext}` |

## Performance
1. **Reuse yt-dlp download handlers** — single `YoutubeDL` instance for playlist batch; avoids re-initialization
2. **`--no-overwrites` + cached metadata** — skips already-downloaded items; `--write-info-json` for metadata

## Security
1. **Validate all YouTube URLs** — regex allowlist `^https?://(www\.)?(youtube\.com|youtu\.be|youtube-nocookie\.com)/` before passing to yt-dlp
2. **No arbitrary domain support** — reject `file://`, `localhost`, internal IPs; prevent SSRF

## Related Projects (in workspace)
- **Python-projects** — shared Python CLI scripts and dependency hygiene pattern
- **selenium_webdriver** — browser automation alternative for JS-heavy sites

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| yt-dlp docs | https://github.com/yt-dlp/yt-dlp#readme | CLI documentation |
