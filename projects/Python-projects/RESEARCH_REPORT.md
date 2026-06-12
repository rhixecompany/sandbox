# RESEARCH_REPORT.md

## Project: Python-projects

**Type:** Python scripts collection / learning automation
**Tech Stack:** Python 3.x, requests, opencv-python, matplotlib, pillow, qrcode, beautifulsoup4, PyDictionary, schedule, ruff, mypy
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| youtube-downloader | `projects/youtube-downloader` | Python automation + network scripts and requirements practices. |

---

## Key Findings

### Script Maintainability
- Standalone scripts benefit from shared readme metadata and consistent failure reporting.
- `requirements.txt` should pin minimum runtime dependencies and separate dev/test extras when needed.

### Dependency Freshness
- Use `pip list --outdated` plus security advisories (`pip-audit`) periodically; avoid auto-updating core libraries in scripts meant to run unattended.

### Error Handling UX
- CLI scripts should surface actionable errors including upgrade commands or setup notes.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| PEP 8 | https://peps.python.org/pep-0008/ | Style guide |
| requests docs | https://requests.readthedocs.io | Library docs |
| opencv-python | https://docs.opencv.org | Image processing docs |
| ruff | https://docs.astral.sh/ruff | Lint |
| mypy | https://mypy.readthedocs.io | Type checking |

---

## Best Practices
1. **Run scripts in virtual environments** — prevent global package conflicts.
2. **Fail loudly** — let network-enabled scripts log URLs and error reasons during failures.
3. **Avoid implicit dependencies** — list all install needs explicitly in `requirements.txt`.
4. **Pin major library versions in dev** — reduce surprise breakage for learners.
5. **Use `if __name__ == "__main__"` guards** — keep modules importable for reuse.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unpinned OpenCV builds | Binary mismatch errors | Pin known-good `opencv-python` wheels in requirements. |
| Mail or network scripts in unsandboxed env | Privacy risk | Require explicit user action before sending messages or requests. |
| Implicit matplotlib GUI backend | Headless failures | Detect non-interactive environments and save files instead of showing plots. |
| Long-lived secrets in scripts | Credential exposure | Read API keys from env, not source. |

---

## Performance
1. Reuse `requests.Session` for repeated HTTP scripts.
2. Cache QR codes when generating in bulk instead of regenerating the same payload.
3. Release OpenCV image resources using context managers to avoid memory growth.

---

## Security
1. Validate URLs before network calls and avoid injecting untrusted content into requests.
2. Do not embed credentials in beginner scripts; teach env var loading from the start.
3. Scan QR code outputs for path traversal concerns if files are saved without timestamp sanitization.
4. Respect `robots.txt` or site terms when extending web scripts beyond simple connectivity checks.

---

## Related Projects (in workspace)

- **youtube-downloader** — shared Python CLI and requirements maintenance pattern

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Python docs | https://docs.python.org/3/ | Language docs |
| requests docs | https://requests.readthedocs.io | HTTP library |
| OpenCV docs | https://docs.opencv.org | Vision library |
| pip-audit docs | https://pypa.github.io/pip-audit/ | Security audit |
| ruff docs | https://docs.astral.sh/ruff | Linting |
