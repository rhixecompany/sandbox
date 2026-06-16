# youtube-downloader

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
