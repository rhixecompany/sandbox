# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| youtube-downloader | `projects/youtube-downloader` | Shared Python CLI + network scripts and requirements practices. |
| selenium_webdriver | `projects/selenium_webdriver` | Browser automation with Selenium patterns. |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | Scrapy + Selenium + BeautifulSoup scraping patterns. |

---

## Key Findings

### Python CLI Scripts Best Practices (2026)

- **argparse (stdlib)** — zero deps, solid for simple CLIs; subcommands via `add_subparsers()`; auto-generates `--help` [1]
- **Typer** — "FastAPI of CLIs": function parameters → CLI args, type hints → validation, auto-completion, rich help [2]
- **Click** — mature, decorator-based, nested commands, `click-completion` for shell autocomplete [3]
- **Recommendation 2026**: `argparse` for single-file scripts (no deps); `Typer` for multi-command tools with type safety; `Click` for complex nested CLIs [2]
- **Project structure**: `src/cli/main.py` + `pyproject.toml` with `[project.scripts]` entry points; `uv` for fast installs [1]

### yt-dlp + curl_cffi Video Downloading Ethics (2026)

- **yt-dlp is gold standard** — actively maintained, daily updates, 1800+ sites; install `yt-dlp[curl-cffi]` for Chrome TLS fingerprint bypass [4]
- **Rate limiting reality** — YouTube aggressively rate-limits yt-dlp (5-6s sleeps, 75% blocks); JDownloader handles better via different client impersonation [5]
- **Ethical/legal boundaries** — YouTube ToS prohibits downloading unless "download" link shown (Premium); personal archiving may fall under fair use/time-shifting in some jurisdictions [8]
- **Best practices**: respect `robots.txt`, add delays (`--sleep-interval`), use `--no-overwrites` + cached metadata for playlists [4]
- **curl_cffi** — impersonates Chrome/Browser TLS fingerprint; `--impersonate chrome` for better speeds & fewer blocks [4]

### OpenCV Python Face Detection (2026)

- **Haar cascades** — classic, fast, CPU-only; `haarcascade_frontalface_default.xml` from `opencv/data/`; struggles with angles/lighting [6]
- **DNN face detector** — `cv2.dnn.readNetFromCaffe/TensorFlow` + pre-trained models (ResNet, YuNet); better accuracy, GPU optional [6]
- **YuNet (OpenCV 4.7+)** — lightweight (1.7MB), fast, accurate; `cv2.FaceDetectorYN_create()`; recommended for 2026+ [7]
- **Comparison**: YuNet > DNN > MTCNN > Haar for accuracy/speed tradeoff; Dlib HOG + CNN most accurate but slow [7]
- **Liveness detection** — separate concern; iBeta Level 2 certified solutions (Seventh Sense) for anti-spoofing [7]

### Python Code Quality Pipeline: ruff + mypy + black (2026)

- **Ruff replaces Black + isort + flake8 + pyupgrade + 15+ tools** — single Rust binary, milliseconds on large codebases [9]
- **Modern stack (2026)**: `uv` (package manager) + `ruff` (lint/format) + `mypy` (type check) + `pytest` + `pre-commit` — all in `pyproject.toml` [9]
- **Ruff config**: `target-version = "py311"`, `line-length = 100`, select `E,W,F,I,N,UP,B,C4,SIM,TCH`; ignore `E501` (formatter handles) [9]
- **mypy strict mode** — `strict = true`, `warn_return_any = true`, `disallow_untyped_defs = true`; catches real bugs pre-runtime [9]
- **CI pipeline**: `uv run pre-commit run --all-files` → `uv run ruff check` → `uv run mypy` → `uv run pytest` — all must pass [9]

### matplotlib + pillow Image Processing (2026)

- **Pillow (PIL fork)** — core image manipulation: open, resize, crop, rotate, filters, format conversion; `Image.open()`, `thumbnail()`, `resize()` [10]
- **matplotlib** — plotting + visualization; `plt.imshow()`, `plt.savefig()` for programmatic charts; `Agg` backend for headless servers [10]
- **Combined workflow**: Pillow for preprocessing (crop/resize) → matplotlib for annotation/plotting → Pillow for final save [10]
- **Memory management** — `with Image.open() as img:`, `plt.close(fig)` to prevent leaks in batch scripts [10]
- **Performance**: `ImageChops` for pixel ops, `ImageFilter` for blur/edge detection; avoid nested Python loops on pixels [10]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| argparse CLI | https://oneuptime.com/blog/post/2026-02-03-python-argparse-cli/view | Guide |
| Typer comparison | https://medium.com/codrift/stop-struggling-with-argparse-why-pythons-typer-library-instantly-fixed-my-cli-headaches-a9d2ebc0585e | Guide |
| Click vs Typer | https://www.reddit.com/r/learnpython/comments/1j16v6j/cli_package_recommendations_click_or_typer | Discussion |
| Typer docs | https://typer.tiangolo.com/alternatives | Docs |
| yt-dlp 2026 guide | https://www.devkantkumar.com/blog/yt-dlp-ultimate-guide-2026 | Guide |
| yt-dlp tutorial | https://ostechnix.com/yt-dlp-tutorial | Tutorial |
| yt-dlp rate limits | https://www.reddit.com/r/youtubedl/comments/1mx9kh4/why_is_ytdlp_getting_ratelimited_so_hard_lately | Discussion |
| OpenCV face detection | https://www.theknowledgeacademy.com/blog/face-detection-with-opencv | Guide |
| Best face detector | https://medium.com/pythons-gurus/what-is-the-best-face-detector-ab650d8c1225 | Comparison |
| Modern Python tooling | https://softaims.com/blog/modern-python-tooling-uv-ruff-mypy-2026 | Guide |
| Python project setup 2026 | https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars | Guide |
| Ruff vs Black | https://www.packetcoders.io/whats-the-difference-black-vs-ruff | Comparison |
| Pillow image processing | https://blog.logrocket.com/image-processing-in-python-using-pillow | Tutorial |
| Real Python Pillow | https://realpython.com/image-processing-with-the-python-pillow-library | Guide |

---

## Best Practices

1. **Run scripts in virtual environments** — `uv venv` + `uv pip install -r requirements.txt` prevents global conflicts
2. **Fail loudly with actionable errors** — log URLs, error reasons, upgrade commands (`pip install --upgrade yt-dlp`)
3. **Explicit dependencies** — `requirements.txt` pins minimum runtime; `requirements-dev.txt` for test/lint tools
4. **Pin major versions in dev** — `opencv-python==4.9.*` reduces surprise breakage for learners
5. **`if __name__ == "__main__"` guards** — keeps modules importable for reuse/testing
6. **Reuse `requests.Session`** — connection pooling for repeated HTTP scripts
7. **Cache QR codes** — dictionary `{payload: qr_image}` avoids regenerating same payload
8. **Release OpenCV resources** — `cap.release()`, `cv2.destroyAllWindows()` in `finally` blocks
9. **Detect headless environments** — `matplotlib.use('Agg')` before `pyplot` import for server scripts
10. **Scan dependencies** — `pip-audit` + `uv run pip-audit` in CI; Renovate for auto-updates

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned OpenCV builds | Binary mismatch errors | Pin known-good `opencv-python` wheels in requirements |
| Network scripts in unsandboxed env | Privacy/credential risk | Require explicit user action before sending messages/requests |
| Implicit matplotlib GUI backend | Headless server failures | `matplotlib.use('Agg')` before any `pyplot` import |
| Long-lived secrets in scripts | Credential exposure | Read API keys from `os.environ`, `.env` via `python-dotenv` |
| Ignoring `robots.txt`/ToS | Legal/ethical violation | Check `robots.txt`; add delays; respect rate limits |
| No type hints | Runtime bugs in production | `mypy --strict` in CI; gradual typing for legacy |
| Mixed formatter configs | Inconsistent style | Ruff config in `pyproject.toml` replaces Black/isort |
| `print()` for logging | Unstructured, no levels | `logging` module with `INFO`/`ERROR` levels |
| No entry points | Users can't run `script-name` | `[project.scripts]` in `pyproject.toml` |
| Global installs | Version conflicts | Always `uv venv` / `python -m venv` |

---

## Performance

1. **`requests.Session` reuse** — TCP connection pooling avoids handshake per request
2. **QR code caching** — `lru_cache(maxsize=128)` on payload → image generation
3. **OpenCV resource management** — context managers (`with cv2.VideoCapture() as cap:`) prevent memory growth
4. **Batch matplotlib** — single figure, multiple subplots; `plt.savefig()` once per batch
5. **Pillow `ImageChops`** — C-accelerated pixel ops vs Python loops
6. **yt-dlp `--no-overwrites` + metadata cache** — skips already-downloaded playlist items
7. **Parallel downloads** — `concurrent.futures.ThreadPoolExecutor(max_workers=4)` for independent URLs

---

## Security

1. **Validate URLs before network calls** — `validators.url()`, allowlist domains, reject `file://`, `localhost`
2. **No embedded credentials** — teach `os.environ['API_KEY']` + `.env` from day one
3. **QR output sanitization** — timestamp/UUID prefix prevents path traversal (`../../etc/passwd.png`)
4. **Respect `robots.txt`** — `robotparser.RobotFileParser()` check before scraping
5. **Scan outputs** — `pip-audit` on CI; `bandit` for static analysis of scripts
6. **File permissions** — `os.chmod(output, 0o600)` for sensitive generated files
7. **Subprocess safety** — `subprocess.run(cmd, shell=False, check=True)`; never `shell=True` with user input

---

## Related Projects (in workspace)

- **youtube-downloader** — shared Python CLI and requirements maintenance pattern
- **selenium_webdriver** — browser automation patterns
- **Django-Scrapy-Selenium** — Scrapy + Selenium + BeautifulSoup scraping patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | https://docs.python.org/3/ | Language docs |
| requests docs | https://requests.readthedocs.io | HTTP library |
| OpenCV docs | https://docs.opencv.org | Vision library |
| pip-audit docs | https://pypa.github.io/pip-audit/ | Security audit |
| Ruff docs | https://docs.astral.sh/ruff | Linting/formatting |
| yt-dlp docs | https://github.com/yt-dlp/yt-dlp#readme | CLI documentation |
| curl_cffi docs | https://curl-cffi.readthedocs.io | TLS fingerprint docs |
| matplotlib docs | https://matplotlib.org/stable/users/ | Plotting |
| Pillow docs | https://pillow.readthedocs.io | Image processing |
| uv docs | https://docs.astral.sh/uv/ | Package manager |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*