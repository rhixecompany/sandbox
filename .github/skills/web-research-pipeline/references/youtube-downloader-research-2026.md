# YouTube Downloader Research Session (2026-07-10)

## Context
Research for `projects/youtube-downloader` using queries from `docs/per-project-research-queries.md` section 14. Target: update `RESEARCH_REPORT.md` in UPDATE mode.

## Queries Executed (6/6)

| # | Query | Key Sources |
|---|-------|-------------|
| 1 | yt-dlp latest features and API usage 2026 | dev.to guide, yt-dlp releases, Python API docs |
| 2 | curl_cffi for YouTube bot protection bypass patterns | Bright Data blog, curl_cffi GitHub, ScrapingBee guide |
| 3 | Python CLI tool packaging with yt-dlp dependency | Arch Linux package, PyPI deps, uv/ruff/mypy discussions |
| 4 | FFmpeg post-processing for video/audio conversion | yt-dlp post-processing guide, HuntAPI blog, SuperUser |
| 5 | Ruff + mypy type checking for Python CLI projects 2026 | Astral ty beta, Ruff PyPI, migration guides |
| 6 | Rate limiting and polite scraping for YouTube downloaders | yt-dlp rate limit options, StackOverflow, Reddit discussions |

## Additional Queries (Follow-up)
- YouTube Data API vs yt-dlp metadata extraction 2026
- yt-dlp format selector syntax bv*+ba bestvideo bestaudio 2026
- yt-dlp extractor args youtube player client web web_safari
- yt-dlp embed metadata embed thumbnail embed subtitles postprocessing
- YouTube downloading legal considerations DMCA 2026

## Method
1. **Parallel web_search** for all 6 primary queries (batched)
2. **Follow-up searches** for specific technical details (format selectors, extractor args, legal)
3. **Codebase analysis** of existing project files (4 main scripts, requirements, README)
4. **Synthesis** into updated RESEARCH_REPORT.md with:
   - Query → findings mapping table
   - Current codebase review with specific improvement recommendations
   - Concrete implementation plan (Typer CLI, config, defaults, validation, progress, testing)

## Backend Performance
- `web_search`: 10/10 queries succeeded, ~15s total (parallel)
- No MCP fetch needed (search results contained sufficient content)
- No JS-rendered pages encountered

## Project-Specific Pattern: Per-Project Query File
This project used a centralized query file (`docs/per-project-research-queries.md`) with numbered sections per project. The workflow:
1. Read query file → extract section 14 queries
2. Read existing RESEARCH_REPORT.md for baseline
3. Execute searches
4. Read project source files
5. Write updated RESEARCH_REPORT.md

**Reusable pattern**: For any project with a query section in that file, the same 5-step workflow applies.

## Key Technical Findings Summary

### yt-dlp (2026)
- Format selector default: `bv*+ba/b` (best video+audio merged, fallback to best single)
- Quality cap: `bv*[height<=1080]+ba*[ext=m4a]`
- MP4 only: `bv*[ext=mp4]+ba*[ext=m4a]`
- Player client workaround: `--extractor-args "youtube:player_client=web,web_safari"`
- Post-processors: `FFmpegVideoConvertor`, `FFmpegMetadata`, `EmbedThumbnail`, `EmbedSubtitle`, `EmbedChapters`
- Download archive: `--download-archive archive.txt` for idempotent runs
- Cookie support: `--cookies-from-browser firefox` / `--cookies cookies.txt`

### curl_cffi
- Install: `pip install "yt-dlp[curl-cffi]"` or `pip install curl_cffi`
- Usage: `--impersonate chrome` (or `safari`, `safari_ios`)
- Impersonates TLS/JA3/HTTP2 fingerprints, not just User-Agent
- Fails on JS challenges (Cloudflare Turnstile) — needs real browser or scraping API

### Legal (2026)
- DMCA 1201 anti-circumvention ruling: third-party downloading = circumvention
- Personal use defense exists but narrow
- RIAA vs youtube-dl (2020): tool itself not infringing, but distribution for infringement is
- Best practice: rate limit, Creative Commons filter, no commercial use, respect robots.txt

### Python Tooling (2026)
- `uv`: replaces pip+venv+poetry, 10-100x faster, lock files
- `ruff`: replaces black+flake8+isort, 800+ rules, ms runtime
- `mypy` strict mode: production baseline
- `ty` (Astral): new Rust type checker, beta, 20x faster than mypy
- PEP 723: inline script metadata (`# /// script` blocks)

## Files Modified
- `projects/youtube-downloader/RESEARCH_REPORT.md` — completely rewritten with findings, codebase analysis, and implementation plan