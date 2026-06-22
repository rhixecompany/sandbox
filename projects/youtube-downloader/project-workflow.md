# Project Workflow — youtube-downloader

## Setup

```bash
# Production dependencies
pip install yt-dlp curl_cffi

# Or all dependencies
pip install -r requirements/base.txt
pip install -r requirements/local.txt
```

## Running

```bash
# Single video
python main_noplaylist.py

# Playlist
python main_playlist.py

# Loop mode (single video)
python main_loop_noplaylist.py

# Loop mode (playlist)
python main_loop_playlist.py
```

## Testing
```bash
python test.py
```

## Quality
```bash
mypy *.py    # Type checking
ruff check . # Lint checking
```

## Adding a New Feature
1. Create a new `.py` file or modify existing script
2. Follow PEP 8 with type hints
3. Use try/except for network error handling
4. Update requirements if new dependencies needed
