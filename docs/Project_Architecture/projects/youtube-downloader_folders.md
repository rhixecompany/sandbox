# youtube-downloader — Folder Structure

> **Stack:** Python 3.x + yt-dlp  
> **Type:** CLI Utility Tool  
> **Status:** Active

## Directory Tree

```
youtube-downloader/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   └── workflows/
├── .vscode/
├── docs/
├── requirements/
├── main_loop_noplaylist.py     # Loop mode, no playlist
├── main_loop_playlist.py       # Loop mode, with playlist
├── main_noplaylist.py          # Single download, no playlist
├── main_playlist.py            # Single download, with playlist
├── test.py                     # Tests
├── README.md
└── ...
```

## Key Patterns

- **Flat structure** — all scripts at project root
- **Naming scheme:** `main_[mode]_[feature].py`
  - `main` = entry point
  - `_noplaylist` / `_playlist` = playlist mode
  - `_loop` = continuous download mode
- **Single dependency:** yt-dlp via `requirements/`
- **Minimal project** — no web components, no build system
