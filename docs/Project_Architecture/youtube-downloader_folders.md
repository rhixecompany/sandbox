# youtube-downloader — Folder Structure

```
youtube-downloader/
├── docs/                         # Documentation
├── requirements/                 # Split requirement files
│   ├── base.txt                  # Production dependencies
│   └── local.txt                 # Development dependencies
├── main_noplaylist.py            # Single video download
├── main_playlist.py              # Playlist download
├── main_loop_noplaylist.py       # Loop mode (single)
├── main_loop_playlist.py         # Loop mode (playlist)
├── test.py                       # Test harness
├── AGENTS.md                     # Agent context
├── README.md                     # Project overview
└── requirements.txt              # Combined dependencies
```

## Key Files

| File | Purpose |
|------|---------|
| `main_noplaylist.py` | Single video download entry point |
| `main_playlist.py` | Playlist download entry point |
| `main_loop_*.py` | Loop/batch processing variants |
| `test.py` | Download engine test harness |
