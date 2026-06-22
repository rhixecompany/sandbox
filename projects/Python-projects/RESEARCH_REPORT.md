# RESEARCH_REPORT.md

## Project: Python-projects
**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| youtube-downloader | `projects/youtube-downloader` | Shared Python CLI + network scripts and requirements practices. |
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation with Selenium patterns. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Scrapy + Selenium + BeautifulSoup scraping patterns. |

## Key Findings
### Python CLI Scripts Best Practices (2026)
- **argparse (stdlib)** — zero deps, solid for simple CLIs; subcommands via `add_subparsers()`; auto-generates `--help` [1]
- **Typer** — "FastAPI of CLIs": function parameters → CLI args, type hints → validation, auto-completion, rich help [2]
- **Click** — mature, decorator-based, nested commands, `click-completion` for shell autocomplete [3]
- **Recommendation 2026**: `argparse` for single-file scripts (no deps); `Typer` for multi-command tools with type safety; `Click` for complex nested CLIs [2]
- **Project structure**: `src/cli/main.py` + `pyproject.toml` with `[project.scripts]` entry points; `uv` for fast installs [1]
### yt-dlp + curl_cffi Video Downloading Ethics (2026)
- **yt-dlp is gold standard** — actively maintained, daily updates, 1800+ sites; install `yt-dlp[curl-cffi]` for Chrome TLS fingerprint bypass [4]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| argparse CLI | https://oneuptime.com/blog/post/2026-02-03-python-argparse-cli/view | Guide |

## Best Practices
1. **Run scripts in virtual environments** — `uv venv` + `uv pip install -r requirements.txt` prevents global conflicts
2. **Fail loudly with actionable errors** — log URLs, error reasons, upgrade commands (`pip install --upgrade yt-dlp`)
3. **Explicit dependencies** — `requirements.txt` pins minimum runtime; `requirements-dev.txt` for test/lint tools

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned OpenCV builds | Binary mismatch errors | Pin known-good `opencv-python` wheels in requirements |

## Performance
1. **`requests.Session` reuse** — TCP connection pooling avoids handshake per request
2. **QR code caching** — `lru_cache(maxsize=128)` on payload → image generation

## Security
1. **Validate URLs before network calls** — `validators.url()`, allowlist domains, reject `file://`, `localhost`
2. **No embedded credentials** — teach `os.environ['API_KEY']` + `.env` from day one

## Related Projects (in workspace)
- **youtube-downloader** — shared Python CLI and requirements maintenance pattern
- **selenium_webdriver** — browser automation patterns
- **Django-Scrapy-Selenium** — Scrapy + Selenium + BeautifulSoup scraping patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | https://docs.python.org/3/ | Language docs |
