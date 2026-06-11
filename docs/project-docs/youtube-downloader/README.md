# youtube-downloader — YouTube Video Downloader

A Python-based YouTube video downloader with playlist support and continuous loop mode.

## Tech Stack
- **Language**: Python 3.x
- **Download Engine**: yt-dlp with curl_cffi
- **Docs**: Sphinx

## Quick Start
```bash
pip install yt-dlp curl_cffi
python main_noplaylist.py
```

## Scripts
| Script | Purpose |
|--------|---------|
| main_noplaylist.py | Single video download |
| main_playlist.py | Playlist download |
| main_loop_noplaylist.py | Loop mode (single) |
| main_loop_playlist.py | Loop mode (playlist) |

## Documentation
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Code Exemplars](code-exemplars.md)
