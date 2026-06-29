# RESEARCH_REPORT.md

<!-- Template version: 1.0.0 — size gate: 1KB-5KB -->

## Project: Python-projects
**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| youtube-downloader | `projects/youtube-downloader` | Shared Python CLI + requirements practices. |
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation with Selenium patterns. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Scrapy + Selenium + BeautifulSoup scraping patterns. |

---

## Key Findings

### Python CLI Scripts Best Practices (2026)
- **argparse (stdlib)** — zero deps, ideal for single-file scripts; subcommands via `add_subparsers()`; auto-generates `--help` [OneUptime 2026]
- **Typer** — "FastAPI of CLIs": function params → CLI args, type hints → validation, auto-completion; best for multi-command tools [Typer docs]
- **Click** — mature, decorator-based, nested commands; `click-completion` for shell autocomplete; best for complex nested CLIs [r/learnpython]
- **2026 recommendation**: `argparse` for single-file (no deps); `Typer` for multi-command; `Click` for complex nesting

### OpenCV Face Detection (2026)
- **YuNet (CPU)** — recommended for speed/real-time; 75K params; 300×300 input; pre-trained via OpenCV Zoo [Python's Gurus]
- **RetinaFace (GPU)** — highest accuracy; watch for large occluded faces; filter smallest quartile to cut false positives [Python's Gurus]
- **No model combines high accuracy + speed** — test on your own data; WIDER FACE benchmarks may not reflect real-world [Python's Gurus]

### Python Tooling 2026: uv + Ruff + mypy
- **uv** replaces pip + venv + pip-tools + poetry — 10-100x faster, Rust, lock files, workspace support [Softaims 2026]
- **Ruff** replaces black + flake8 + isort + pyupgrade — 800+ rules, runs in ms; used by FastAPI, LangChain [Softaims 2026]
- **mypy strict mode** is the baseline for production type checking; `pyproject.toml` centralizes all config [Softaims 2026]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| argparse CLI | https://oneuptime.com/blog/post/2026-02-03-python-argparse-cli/view | Guide |
| Typer docs | https://typer.tiangolo.com/alternatives | Official docs |
| Python tooling 2026 | https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026 | Guide |

---

## Best Practices

1. **Run scripts in virtual environments** — `uv venv` avoids global conflicts; `uv` is the 2026 standard
2. **Fail loudly with actionable errors** — log URLs, error reasons, upgrade commands
3. **Explicit dependencies** — `requirements.txt` for runtime; `requirements-dev.txt` for lint/test
4. **Adopt pyproject.toml** — single config for Ruff, mypy, pytest; eliminates setup.cfg, .flake8
5. **Pre-commit hooks** — run Ruff + mypy on every commit; catch issues before CI

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned OpenCV builds | Binary mismatch errors | Pin known-good `opencv-python` wheels |
| Deprecated Haar cascades | Poor accuracy | Prefer YuNet via `cv2.FaceDetectorYN_create()` |

---

## Performance

1. **`requests.Session` reuse** — TCP connection pooling avoids handshake per request
2. **YuNet over Haar cascades** — faster and more accurate for CPU face detection

---

## Security

1. **Validate URLs before network calls** — `validators.url()`, allowlist domains, reject `file://`
2. **No embedded credentials** — `os.environ['API_KEY']` + `.env` from day one

---

## Related Projects (in workspace)

- **youtube-downloader** — shared Python CLI and requirements pattern
- **selenium_webdriver** — browser automation patterns
- **Django-Scrapy-Selenium** — Scrapy + Selenium + BeautifulSoup scraping

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | https://docs.python.org/3/ | Language docs |
| Typer docs | https://typer.tiangolo.com/ | Modern Python CLI framework |
| uv package manager | https://docs.astral.sh/uv/ | Fast Python package manager |
| Ruff linter | https://docs.astral.sh/ruff/ | Python linter and formatter |
| OpenCV Zoo | https://github.com/opencv/opencv_zoo | Pre-trained models (YuNet) |
