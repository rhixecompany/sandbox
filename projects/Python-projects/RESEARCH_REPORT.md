# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy, uv
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Awesome Python Scripts | <https://github.com/mahmoud/awesome-python-scripts> | curated utility script collection |
| Python CLI Examples | <https://github.com/realpython/command-line-interfaces-python-argparse> | argparse examples |
| Hitchhiker's Guide | <https://docs.python-guide.org/writing/structure> | canonical project structure |

---

## Key Findings

### PEP 723 Inline Script Metadata (2026 Standard)

- `# /// script` block embeds dependencies directly in standalone scripts
- Eliminates separate requirements.txt for single-file tools
- Emerging 2026 standard for script packaging — supported by uv, hatch, pipx
- Format: `# /// script` ... `# ///` with TOML content (dependencies, requires-python, [tool] table)
- Example:
  ```python
  # /// script
  # requires-python = ">=3.11"
  # dependencies = ["requests<3", "rich"]
  # ///
  import requests
  from rich.pretty import pprint
  ```
- uv runs these with `uv run script.py` — auto-creates ephemeral env, installs deps
- Can transition to full project with `pyproject.toml` when script grows

### Python 3.12/3.13/3.14: Version Guidance for 2026

**Python 3.12 (Oct 2023)** — Cleanup release, now security-only (until Oct 2028):
- Type parameter syntax (PEP 695): `class Stack[T]:` instead of `TypeVar`
- F-strings unleashed (PEP 701): nested quotes, backslashes, multiline
- Comprehension inlining (PEP 709): ~2x faster comprehensions, 11% real-world speedup
- Per-interpreter GIL (PEP 684) — foundation for free-threading
- Removed `distutils` — use `setuptools`
- Better error messages (NameError suggests `self.`)

**Python 3.13 (Oct 2024)** — Experimental foundations:
- Free-threaded build (PEP 703) — experimental, separate `python3.13t` binary
- JIT compiler (PEP 744) — experimental, copy-and-patch, not enabled by default
- Many C extensions not thread-safe yet (NumPy needed patches)

**Python 3.14 (Oct 2025)** — Delivery release (recommended for 2026):
- Free-threading officially supported (PEP 779) — no longer experimental
- JIT ships in binary releases
- Template strings / t-strings (PEP 750)
- Deferred annotation evaluation (PEP 649/749)
- Multiple interpreters in stdlib (PEP 734)
- Zstandard compression (PEP 784)
- Mobile platform support (iOS, Android)

**Recommendation for 2026 beginner projects**: Target Python 3.12+ (widely supported) or 3.14 (latest stable with modern features). Use `requires-python = ">=3.12"` in pyproject.toml.

### CLI Framework Comparison (2026)

- **argparse** — stdlib, zero deps; ideal for single-file scripts
- **Typer** — "FastAPI of CLIs"; type hints → validation; best for multi-command
- **Click** — mature decorator-based; nested commands; shell autocomplete
- **2026 recommendation**: argparse for single-file scripts; Typer for multi-command CLI tools

### Python Packaging & Distribution for CLI Tools (2026)

- **pyproject.toml** is the single source of truth — replaces setup.py, setup.cfg, requirements.txt
- Two required tables: `[build-system]` and `[project]`
- Required `[project]` fields: `name`, `version`
- Recommended: `description`, `authors`, `readme`, `license`, `classifiers`, `requires-python`, `dependencies`
- Build backends: hatchling (recommended), setuptools, flit, pdm-backend
- Distribution: `python -m build` → produces sdist + wheel → `twine upload dist/*`
- For CLI tools: add `[project.scripts]` entry points (e.g., `mycli = "mycli.main:main"`)
- uv replaces pip + venv + poetry — 10-100x faster, Rust-based, built-in lockfiles
- `uv init` scaffolds project with pyproject.toml, README, src/ layout
- `uv add package` — resolves, installs, locks in one command
- `uv run` — auto-activates env, runs command

### Python Type Hints & mypy for Beginner Codebases (2026)

- **Type hints don't change runtime behavior** — static analysis only
- **mypy strict mode** — production baseline; catches real bugs early
- **Ty** (new from Astral) — faster type checker, configured in pyproject.toml
- Beginner-friendly approach:
  - Start with basic annotations: `def greet(name: str) -> str:`
  - Use `list[str]`, `dict[str, int]` (Python 3.9+ built-in generics)
  - `Optional[T]` = `T | None` (Python 3.10+ union syntax)
  - Annotate function signatures (boundaries); let mypy infer locals
  - Use `# type: ignore` sparingly with specific error codes
- pyproject.toml config:
  ```toml
  [tool.mypy]
  python_version = "3.12"
  strict = true
  warn_return_any = true
  warn_unused_configs = true
  ```

### Ruff Linting Configuration for Python Projects (2026)

- **Ruff replaces Black + Flake8 + isort + pyupgrade** — 800+ rules, runs in ms
- Configured in `pyproject.toml` under `[tool.ruff]`
- **Recommended 2026 baseline config**:
  ```toml
  [tool.ruff]
  line-length = 100
  target-version = "py312"
  
  [tool.ruff.lint]
  select = ["E4", "E7", "E9", "F", "B", "I", "UP", "ANN", "ARG", "PTH", "ERA"]
  ignore = ["E501"]  # line-too-long (formatter handles)
  fixable = ["ALL"]
  unfixable = ["B"]
  
  [tool.ruff.lint.per-file-ignores]
  "__init__.py" = ["E402"]
  "tests/**/*" = ["E402", "ANN001", "ANN002", "ANN003", "ANN201", "ANN202"]
  
  [tool.ruff.format]
  quote-style = "double"
  docstring-code-format = true
  ```
- Rule groups: E/F (pyflakes/pycodestyle), B (flake8-bugbear), I (isort), UP (pyupgrade), ANN (annotations), ARG (unused args), PTH (pathlib), ERA (eradicate)
- Run: `uv run ruff check . --fix` then `uv run ruff format .`
- Pre-commit: `uv run pre-commit run --all-files`

### Python Project Structure for Educational Repositories (2026)

**For 18 standalone beginner scripts (current Python-projects):**
- Keep flat structure — each script is independent, no shared package
- Add `pyproject.toml` at root for tool config (ruff, mypy, pytest)
- Use PEP 723 inline metadata in each script for standalone runnability
- Example structure:
  ```
  Python-projects/
  ├── pyproject.toml           # tool config (ruff, mypy, pytest)
  ├── uv.lock                  # locked deps
  ├── README.md                # project index with script descriptions
  ├── requirements.txt         # optional: for pip users
  ├── basic_calculator.py      # with PEP 723 header
  ├── qr_code_generator.py     # with PEP 723 header
  └── ... (16 more scripts)
  ```

**For growing projects (src layout):**
```
my-project/
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
└── data/
    ├── raw/
    └── processed/
```
- `src/` layout improves imports, packaging, test isolation, type-checker config
- uv init creates this by default

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Python project structure | <https://docs.python-guide.org/writing/structure> | Guide |
| argparse CLI | <https://realpython.com/command-line-interfaces-python-argparse> | Tutorial |
| Typer docs | <https://typer.tiangolo.com/alternatives> | Docs |
| uv package manager | <https://docs.astral.sh/uv/> | Docs |
| OpenCV Zoo | <https://github.com/opencv/opencv_zoo> | Pre-trained models |
| PEP 723 Inline Metadata | <https://peps.python.org/pep-0723/> | Spec |
| Ruff configuration | <https://docs.astral.sh/ruff/configuration> | Docs |
| mypy cheat sheet | <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html> | Reference |
| pyOpenSci packaging guide | <https://www.pyopensci.org/python-package-guide/> | Tutorial |

---

## Best Practices

1. **Use `uv` for all Python tooling** — faster than pip, built-in venv, lock files
2. **`if __name__ == "__main__"` guard** — all scripts; enables import safety
3. **Pathlib over os.path** — cross-platform, object-oriented
4. **Type hints** — required for mypy strict mode; document intent
5. **Logging over print** — structured logging for production scripts
6. **PEP 723 inline metadata** — single-file scripts become self-contained
7. **Target Python 3.12+** — modern syntax, better performance, long support
8. **Centralize config in pyproject.toml** — ruff, mypy, pytest, build all in one file

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mutable default args | subtle bugs | `def foo(x=None): x = x or []` |
| No `__main__` guard | unintended execution on import | always add guard |
| Hardcoded paths | cross-platform breaks | `pathlib.Path(__file__).parent` |
| `eval()`/`exec()` on input | code injection | never use on untrusted input |
| Missing shebang | can't run directly | `#!/usr/bin/env python3` |
| No inline script metadata | can't run with uv directly | add PEP 723 block |
| setup.py instead of pyproject.toml | deprecated, limited tooling | migrate to pyproject.toml |

---

## Performance

1. **`requests.Session` reuse** — TCP connection pooling avoids per-request handshake
2. **YuNet over Haar cascades** — faster and more accurate for CPU face detection
3. **List comprehensions** — faster than explicit loops for transformations
4. **`functools.lru_cache`** — memoize expensive pure functions
5. **Profile with `cProfile`** — optimize hotspots, not guesses
6. **Comprehension inlining (3.12+)** — ~2x faster list/dict/set comprehensions
7. **Free-threading (3.14+)** — true parallel CPU work with ThreadPoolExecutor

---

## Security

1. **Validate URLs before network calls** — `validators.url()`; allowlist domains
2. **No embedded credentials** — `os.environ['API_KEY']` + `.env`
3. **Path traversal prevention** — `Path.resolve()` + check within allowed dirs
4. **`shlex.quote()` for shell commands** — prevent injection
5. **`pip-audit` for dependency scanning** — catch known vulnerabilities
6. **`uv lock --update-package`** — keep dependencies current

---

## Related Projects (in workspace)

- **youtube-downloader** — shared Python CLI pattern
- **selenium_webdriver** — browser automation with Selenium
- **Django-Scrapy-Selenium** — Scrapy + Selenium + BeautifulSoup scraping

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | <https://docs.python.org/3/> | Language docs |
| Typer docs | <https://typer.tiangolo.com/> | Modern Python CLI |
| uv docs | <https://docs.astral.sh/uv/> | Fast Python package manager |
| Ruff linter | <https://docs.astral.sh/ruff/> | Python linter/formatter |
| PEP 723 | <https://peps.python.org/pep-0723/> | Inline script metadata spec |
| pyOpenSci guide | <https://www.pyopensci.org/python-package-guide/> | Packaging tutorial |
| Python 3.12/3.13/3.14 comparison | <https://dev.to/matheus_releaserun/python-312-vs-313-vs-314-what-actually-changed-and-which-should-you-use-4kc0> | Version guide |
| KDnuggets 2026 stack | <https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars> | Modern tooling |

---

## 2026 Research Update Summary

This report was updated with 5 focused research queries covering modern Python 2026 practices:

1. **Python 3.12/3.13/3.14 beginner best practices** — Target 3.12+ for stability or 3.14 for latest features; use modern syntax (union types, generics, match/case)
2. **Python packaging for CLI tools** — pyproject.toml is mandatory; uv is the standard toolchain; PEP 723 enables single-file distribution
3. **Type hints & mypy for beginners** — Start with function signatures; enable strict mode gradually; consider Ty for speed
4. **Ruff configuration** — Single tool replaces 4+; configure in pyproject.toml with recommended rule sets for learning projects
5. **Project structure for education** — Flat layout for standalone scripts; add pyproject.toml + PEP 723 headers; src/ layout for packages