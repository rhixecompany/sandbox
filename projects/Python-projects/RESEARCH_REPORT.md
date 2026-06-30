# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy, uv
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Awesome Python Scripts | https://github.com/mahmoud/awesome-python-scripts | curated utility script collection |
| Python CLI Examples | https://github.com/realpython/command-line-interfaces-python-argparse | argparse examples |
| Hitchhiker's Guide | https://docs.python-guide.org/writing/structure | canonical project structure |

---

## Key Findings

### PEP 723 Inline Script Metadata
- `# /// script` block embeds dependencies directly in standalone scripts
- Eliminates separate requirements.txt for single-file tools
- Emerging 2026 standard for script packaging

### CLI Framework Comparison (2026)
- **argparse** — stdlib, zero deps; ideal for single-file scripts
- **Typer** — "FastAPI of CLIs"; type hints → validation; best for multi-command
- **Click** — mature decorator-based; nested commands; shell autocomplete
- 2026 recommendation: argparse for single-file; Typer for multi-command

### Python Tooling 2026
- **uv** replaces pip + venv + poetry — 10-100x faster, Rust-based
- **Ruff** replaces black + flake8 + isort — 800+ rules, runs in ms
- **mypy strict mode** — production baseline; `pyproject.toml` centralizes config

### OpenCV Face Detection (2026)
- **YuNet (CPU)** — recommended for speed; 75K params; 300×300 input; OpenCV Zoo
- **RetinaFace (GPU)** — highest accuracy; filter smallest quartile for false positives
- No model combines high accuracy + speed — test on your own data

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Python project structure | https://docs.python-guide.org/writing/structure | Guide |
| argparse CLI | https://realpython.com/command-line-interfaces-python-argparse | Tutorial |
| Typer docs | https://typer.tiangolo.com/alternatives | Docs |
| uv package manager | https://docs.astral.sh/uv/ | Docs |
| OpenCV Zoo | https://github.com/opencv/opencv_zoo | Pre-trained models |

---

## Best Practices

1. **Use `uv` for all Python tooling** — faster than pip, built-in venv, lock files
2. **`if __name__ == "__main__"` guard** — all scripts; enables import safety
3. **Pathlib over os.path** — cross-platform, object-oriented
4. **Type hints** — required for mypy strict mode; document intent
5. **Logging over print** — structured logging for production scripts

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mutable default args | subtle bugs | `def foo(x=None): x = x or []` |
| No `__main__` guard | unintended execution on import | always add guard |
| Hardcoded paths | cross-platform breaks | `pathlib.Path(__file__).parent` |
| `eval()`/`exec()` on input | code injection | never use on untrusted input |
| Missing shebang | can't run directly | `#!/usr/bin/env python3` |

---

## Performance

1. **`requests.Session` reuse** — TCP connection pooling avoids per-request handshake
2. **YuNet over Haar cascades** — faster and more accurate for CPU face detection
3. **List comprehensions** — faster than explicit loops for transformations
4. **`functools.lru_cache`** — memoize expensive pure functions
5. **Profile with `cProfile`** — optimize hotspots, not guesses

---

## Security

1. **Validate URLs before network calls** — `validators.url()`; allowlist domains
2. **No embedded credentials** — `os.environ['API_KEY']` + `.env`
3. **Path traversal prevention** — `Path.resolve()` + check within allowed dirs
4. **`shlex.quote()` for shell commands** — prevent injection
5. **`pip-audit` for dependency scanning** — catch known vulnerabilities

---

## Related Projects (in workspace)

- **youtube-downloader** — shared Python CLI pattern
- **selenium_webdriver** — browser automation with Selenium
- **Django-Scrapy-Selenium** — Scrapy + Selenium + BeautifulSoup scraping

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | https://docs.python.org/3/ | Language docs |
| Typer docs | https://typer.tiangolo.com/ | Modern Python CLI |
| uv docs | https://docs.astral.sh/uv/ | Fast Python package manager |
| Ruff linter | https://docs.astral.sh/ruff/ | Python linter/formatter |
