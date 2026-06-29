# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Beginner Python scripts collection
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, schedule
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| 30-Days-Of-Python | https://github.com/Asabeneh/30-Days-Of-Python | Comprehensive Python curriculum for beginners |
| Internet Made Coder's Python Course | https://github.com/InternetMadeCoder/Python-Projects | Similar beginner automation projects |

## Key Findings

### Python Scripts Packaging (2026)
- `pyproject.toml` with `[project.scripts]` is now the standard for distributing CLI tools via pip
- Ruff has become the dominant linter, replacing flake8 (pypi.org/project/ruff, 2026)
- Beginner script collections benefit from virtual environment best practices documented in README

### OpenCV Face Detection
- Haar Cascade classifiers remain the simplest approach for face detection (docs.opencv.org, 2026)
- MediaPipe offers higher accuracy with comparable simplicity — recommended upgrade path
- OpenCV 4.x maintains backward compatibility with the cascade XML format

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Python Packaging | https://packaging.python.org | Guide |
| Ruff Linter | https://docs.astral.sh/ruff | Docs |
| OpenCV Python | https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html | Tutorial |

## Best Practices

1. **Add `if __name__ == '__main__'` guards** — Prevents accidental execution on import
2. **Use environment variables for secrets** — Already done in email_sender.py (model for others)
3. **Replace `eval()` with typed input** — `currency_converter.py` uses `eval(input())` — switch to `float()`
4. **Declare dependencies in pyproject.toml** — Enables `pip install` and dependency resolution
5. **Organize scripts into categories** — Group by domain (math, networking, CV) for discoverability

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| eval(input()) in calculator | Arbitrary code execution risk | Use type-specific parsing (float, int) |
| Missing haar cascade XML | Face detection crashes | Bundle XML or switch to MediaPipe |
| Duplicate file content | Confusing codebase | Deduplicate files (6 scripts affected) |

## Performance

1. **OpenCV Haar cascade** runs in real-time on modern CPUs (30+ FPS on 720p)
2. **QR code generation** is near-instant with `qrcode` library
3. **Image resizing** with Pillow handles 4K images in under 100ms
4. **matplotlib plots** benefit from non-blocking backend for responsive UX

## Security

1. **Replace eval()** in `currency_converter.py` with numeric parsing
2. **Validate scraped content** in scripts using beautifulsoup4
3. **Use environment variables** for email credentials (already done, extend to other secrets)
4. **Rate-limit network requests** to avoid IP-based blocking

## Related Projects (in workspace)

- **youtube-downloader** — Python-based CLI, similar packaging and testing patterns
- **Django-Scrapy-Selenium** — Shares Python toolchain and ruff linting

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python Packaging | https://packaging.python.org | Official Python packaging guide |
| Ruff Docs | https://docs.astral.sh/ruff | Python linter documentation |
| OpenCV Python Tutorials | https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html | Computer vision with Python |
