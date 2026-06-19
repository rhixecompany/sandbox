# youtube-downloader
## Architecture

- **Blueprint**: [youtube-downloader Architecture](../docs/Project_Architecture/youtube_downloader_architecture.md)
- **Folders**: [youtube-downloader Folder Structure](../docs/Project_Architecture/youtube_downloader_folders.md)
- **Tech Stack**: [youtube-downloader Technology Stack](../docs/Project_Architecture/youtube_downloader_techstack.md)
- **Stack Type**: Unknown


Python 3.x CLI downloader (yt-dlp + curl_cffi): single video, playlist, loop mode.

## Commands
```bash
pip install yt-dlp curl_cffi
python main_noplaylist.py || python main_playlist.py
python main_loop_playlist.py  # batch loop
python test.py
ruff check . && mypy *.py  # optional
```

## Notes
- Single CLI tool; no web deployment
- `.env` / URLs never commit
- Keep yt-dlp updated; FFmpeg for conversions
- Add delays to respect rate limits
