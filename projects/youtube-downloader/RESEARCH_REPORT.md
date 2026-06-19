# RESEARCH_REPORT.md

## Project: youtube-downloader

**Type:** YouTube CLI download tool
**Tech Stack:** Python 3.x, yt-dlp, curl_cffi, pytest, mypy, ruff, black
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Python-projects | `projects/Python-projects` | Shared Python CLI + requirements hygiene pattern. |
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation alternatives for scraping. |

---

## Key Findings

### yt-dlp + curl_cffi Best Practices (2026)

- **yt-dlp is the gold standard** — actively maintained with daily updates (March 2026); 1800+ sites supported; best open-source option for YouTube [1]
- **Always install `yt-dlp[curl-cffi]`** — preserves compatibility with YouTube bot protection/throttling; Chrome TLS fingerprint impersonation [1]
- **Rate limiting is aggressive** — YouTube enforces 5-6s sleeps, 75% block rate for yt-dlp; JDownloader handles better via different client impersonation [2]
- **Fix for "Sign in to confirm you're not a bot"**: `yt-dlp --cookies-from-browser chrome --extractor-args "youtube:player_client=tv"` [1]
- **Version pinning** — pin `yt-dlp` in requirements or auto-upgrade in `main()` on validation failure; `--no-update` for reproducible builds [1]

### Python CLI Design: typer vs click vs argparse (2026)

- **argparse (stdlib)** — zero deps; best for single-file scripts, simple flags; subcommands via `add_subparsers()` [4]
- **Typer** — "FastAPI of CLIs": type hints → validation, auto-completion, rich help, nested commands; built on Click [4]
- **Click** — mature, decorator-based, nested subcommands, `click-completion` for shell autocomplete [4]
- **Recommendation for youtube-downloader**: **Typer** — 4 distinct commands (single, playlist, loop-single, loop-playlist) map perfectly to subcommands; type hints validate quality selection [4]
- **Migration from interactive prompts** → explicit CLI flags: `yt-dlp single --url URL --quality 1080p` vs current prompt flow [4]

### YouTube Downloading Ethics + Legal (2026)

- **YouTube ToS prohibits downloading** unless "download" link displayed (Premium); technical prohibition, not necessarily criminal [5]
- **Personal archiving** — many jurisdictions: time-shifting/fair use for personal offline viewing of legally-accessed content [5]
- **Legal avenues**: YouTube Premium (official), Creative Commons licensed content, owner permission, educational transformative use [5]
- **Best practice for tools**: surface ToS warning, restrict to allowlisted domains (`youtube.com`, `youtu.be`), provide policy README [5]
- **Emerging standards**: `ai.txt`/`llms.txt` for AI scraping control; `robots.txt` voluntary but honored by ethical scrapers [8]

### Python Quality Pipeline: pytest + ruff + mypy + black (2026)

- **Modern stack (2026)**: `uv` (package manager, 10-100x faster than pip) + `ruff` (replaces Black + isort + flake8 + pyupgrade) + `mypy` (strict) + `pytest` [6]
- **Ruff config**: `target-version = "py311"`, `line-length = 100`, select `E,W,F,I,N,UP,B,C4,SIM,TCH`; ignores `E501` [6]
- **mypy strict**: `strict = true`, `warn_return_any = true`, `disallow_untyped_defs = true`; catches real bugs pre-runtime [6]
- **CI pipeline**: `uv run pre-commit run --all-files` → `uv run ruff check` → `uv run mypy` → `uv run pytest` [6]
- **Project config**: `pyproject.toml` with `[tool.ruff]`, `[tool.mypy]`, `[tool.pytest.ini_options]`, `[project.scripts]` entry points [6]

### FFmpeg + Python Video Post-Processing (2026)

- **`ffmpeg-python` wrapper** — clean Pythonic API: `ffmpeg.input('in.mp4').output('out.webm').run()` [9]
- **Common operations**: format conversion, audio extraction (`output('audio.mp3')`), trimming (`ss`, `t`), thumbnails (`vframes=1`), 2-pass encoding [9]
- **yt-dlp integrates FFmpeg** — `--ffmpeg-location`, `--audio-format mp3`, `--embed-thumbnail`, `--convert-thumbnails` handled internally [1]
- **Subprocess fallback** — `subprocess.run(['ffmpeg', '-i', 'in.mp4', '-c:v', 'libx264', 'out.mp4'], check=True)` for complex filters [9]
- **Async/parallel** — `asyncio.create_subprocess_exec` for concurrent conversions; limit concurrency to CPU cores [9]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| yt-dlp 2026 guide | https://www.devkantkumar.com/blog/yt-dlp-ultimate-guide-2026 | Guide |
| yt-dlp tutorial | https://ostechnix.com/yt-dlp-tutorial | Tutorial |
| yt-dlp rate limits | https://www.reddit.com/r/youtubedl/comments/1mx9kh4/why_is_ytdlp_getting_ratelimited_so_hard_lately | Discussion |
| yt-dlp GitHub issues | https://github.com/yt-dlp/yt-dlp/issues/10525 | Issue tracker |
| Curl_cffi + yt-dlp | https://www.reddit.com/r/youtubedl/comments/1qaqnj1/how_to_utilize_curl_cffi_on_dnf_rpm_ytdlp | Discussion |
| Python video downloader | https://karchunt.com/blog/youtube-video-downloader-using-python | Tutorial |
| Typer vs Click vs argparse | https://medium.com/@mohd_nass/navigating-the-cli-landscape-in-python-a-comparative-study-of-argparse-click-and-typer-480ebbb7172f | Comparison |
| Typer docs | https://typer.tiangolo.com/alternatives | Docs |
| YouTube legal 2026 | https://www.bitbrowser.net/blog/download-youtube-videos | Guide |
| Lynote legal guide | https://lynote.ai/blog/download-youtube-videos-legally | Guide |
| TechSmith legal | https://www.techsmith.com/blog/download-youtube-videos | Guide |
| Modern Python tooling | https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026 | Guide |
| Python project setup 2026 | https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars | Guide |
| Ruff vs Black | https://www.packetcoders.io/whats-the-difference-black-vs-ruff | Comparison |
| FFmpeg Python | https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples | Tutorial |
| FFmpeg Python guide | https://templated.io/blog/ffmpeg-in-python-a-practical-guide-with-code-examples | Guide |
| ffmpeg-python GitHub | https://github.com/kkroening/ffmpeg-python | Package |

---

## Best Practices

1. **Explicit CLI commands over interactive prompts** — `download single --url URL --quality 1080p` enables automation/pipelines
2. **Pin `yt-dlp` with auto-upgrade fallback** — `yt-dlp==2026.3.15` in requirements; `main()` checks version on validation failure
3. **Install `yt-dlp[curl-cffi]`** — Chrome TLS fingerprint bypasses YouTube bot protection
4. **Isolated temp directories** — `tempfile.mkdtemp()` per download; atomic move on success; cleanup on failure
5. **Playlist metadata caching** — JSON cache `{playlist_id: {videos: [], timestamp}}` avoids re-resolving channel pages
6. **Non-interactive mode flags** — `--no-prompt`, `--quality 1080p`, `--format bestvideo+bestaudio` for CI/CD
7. **Quality selection caching** — parse available formats once per URL; reuse for batch downloads
8. **FFmpeg via `ffmpeg-python`** — `ffmpeg.input().output().run()` for post-processing; `subprocess` only for complex filters
9. **Structured logging** — `logging` module with levels; `--verbose` flag increases to DEBUG
10. **Dependency audit in CI** — `uv run pip-audit` + `uv run bandit -r .` on every PR

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unbounded output filenames | FS conflicts, overwrites | Sanitize + prefix: `{type}_{timestamp}_{sanitized_title}.{ext}` |
| Interactive prompts in automation | Failed pipelines | Explicit CLI flags (`--url`, `--quality`, `--format`) |
| Long-lived FFmpeg handles | Memory leak | `subprocess.run(check=True)` + context managers; limit concurrency |
| Ignoring ToS changes | Legal/account risk | Display ToS warning on startup; link to policy README |
| No rate limit handling | 429 blocks, IP bans | `--sleep-interval 2-5`, `--max-sleep-interval 30`, exponential backoff |
| Unvalidated URLs | SSRF, arbitrary domains | Allowlist `youtube.com`, `youtu.be`, `youtube-nocookie.com` |
| Cookies not rotated | Auth expiration | `--cookies-from-browser chrome` + periodic refresh |
| No metadata cache | Slow playlist re-resolves | JSON cache with TTL (24h); invalidate on `--force-refresh` |
| Single-threaded playlist | Slow batch downloads | `ThreadPoolExecutor(max_workers=4)` for independent videos |
| Missing `--no-overwrites` | Re-downloads waste bandwidth | Always set; skip existing files by ID |

---

## Performance

1. **Reuse yt-dlp download handlers** — single `YoutubeDL` instance for playlist batch; avoids re-initialization
2. **`--no-overwrites` + cached metadata** — skips already-downloaded items; `--write-info-json` for metadata
3. **Cache generated quality options** — parse formats once per URL; reuse for loop mode
4. **Parallel downloads** — `concurrent.futures.ThreadPoolExecutor(max_workers=4)` for playlist items
5. **FFmpeg 2-pass only when needed** — single-pass `-c:v libx264 -preset fast` for most; 2-pass for archival
6. **Atomic file moves** — download to temp, `os.rename(tmp, final)` on success; prevents partial files
7. **Stream processing** — `yt-dlp -o - URL | ffmpeg -i - -c copy out.mp4` avoids disk I/O for pipes

---

## Security

1. **Validate all YouTube URLs** — regex allowlist `^https?://(www\.)?(youtube\.com|youtu\.be|youtube-nocookie\.com)/` before passing to yt-dlp
2. **No arbitrary domain support** — reject `file://`, `localhost`, internal IPs; prevent SSRF
3. **Don't log cookies/session IDs** — filter sensitive fields from `logging` output; `--no-print-traffic`
4. **Review FFmpeg outputs** — `os.path.basename()` + sanitize before saving external metadata files
5. **Surface ToS compliance** — startup banner: "For personal/media-rights-compliant usage only"
6. **Temp directory isolation** — `tempfile.mkdtemp(prefix='yt-dl-')` per run; cleanup on exit
7. **Dependency scanning** — `uv run pip-audit` + `uv run bandit` in CI; Renovate for `yt-dlp` updates

---

## Related Projects (in workspace)

- **Python-projects** — shared Python CLI scripts and dependency hygiene pattern
- **selenium_webdriver** — browser automation alternative for JS-heavy sites

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| yt-dlp docs | https://github.com/yt-dlp/yt-dlp#readme | CLI documentation |
| curl_cffi docs | https://curl-cffi.readthedocs.io | TLS compatibility docs |
| pytest docs | https://docs.pytest.org | Test tooling |
| pip-audit docs | https://pypa.github.io/pip-audit/ | Dependency security audit |
| Python packaging guide | https://packaging.python.org | Distribution guidance |
| Typer CLI framework | https://typer.tiangolo.com/ | Modern CLI library |
| FFmpeg Python | https://github.com/kkroening/ffmpeg-python | Media processing |
| YouTube ToS | https://www.youtube.com/static?template=terms | Terms of Service |
| Creative Commons | https://creativecommons.org/licenses/ | Legal content |
| uv package manager | https://docs.astral.sh/uv/ | Fast Python pkg mgr |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*