# Code Exemplars — youtube-downloader

## 1. yt-dlp Download Function

```python
import yt_dlp

def download_video(url, quality="720"):
    ydl_opts = {
        "format": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info["title"]
```

## 2. Playlist Download

```python
import yt_dlp

def download_playlist(playlist_url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(playlist_title)s/%(title)s.%(ext)s",
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
```
