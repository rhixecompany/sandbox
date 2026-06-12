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

---

## Key Findings

### yt-dlp Maintenance Reality
- yt-dlp is the most reliable downloader library in 2026 because it actively tracks YouTube changes.
- Always install `yt-dlp[curl-cffi]` to preserve compatibility with YouTube bot protection and throttling.

### CLI and Loop UX
- Separate single-video, playlist, and loop flows into explicit commands or modes; avoid asking for URL then mode then quality in interactive prompts.
- Use playlist metadata caching so repeat loop invocations do not re-resolve channel pages.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| yt-dlp docs | https://github.com/yt-dlp/yt-dlp#readme | Repo docs |
| curl_cffi docs | https://curl-cffi.readthedocs.io | TLS fingerprint docs |
| pytest docs | https://docs.pytest.org | Test docs |
| pip-audit docs | https://pypa.github.io/pip-audit/ | Security docs |

---

## Best Practices
1. Pin `yt-dlp` to a recent version or run upgrade in `main()` when validation fails.
2. Run downloads in isolated temp directories and move successful outputs atomically to final path.
3. Use `pytest` parametrization for URL and quality combinations when testing edge cases.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Unbounded output filenames | File system conflicts | Sanitize and prefix filenames by type and timestamp. |
| Interactive prompts in automation | Failed pipelines | Provide non-interactive CLI options or environment flags. |
| Long-lived FFmpeg handles | Memory leak | Reuse process handles and ensure stream closure. |
| Ignoring ToS changes | Legal risk | Provide policy readme guidance to users. |

---

## Performance
1. Reuse `yt-dlp` download handlers when batching playlist downloads.
2. Use `--no-overwrites` and cached metadata to skip already-downloaded playlist items.
3. Cache generated quality options so parsing does not re-scan URL for each batch.

---

## Security
1. Validate all YouTube URLs before passing them to yt-dlp; avoid allowing arbitrary domains in shared deploys.
2. Do not log cookies or session ids in test output.
3. Review ffmpeg/audio outputs for path traversal before saving external metadata files.
4. Surface to users that this tool is for personal/media-rights-compliant usage only.

---

## Related Projects (in workspace)

- **Python-projects** — shared Python CLI scripts and dependency hygiene pattern

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| yt-dlp docs | https://github.com/yt-dlp/yt-dlp#readme | CLI documentation |
| curl_cffi docs | https://curl-cffi.readthedocs.io | TLS compatibility docs |
| pytest docs | https://docs.pytest.org | Test tooling |
| pip-audit docs | https://pypa.github.io/pip-audit/ | Dependency security audit |
| Python packaging guide | https://packaging.python.org | Distribution guidance |
