# Architecture Blueprint: youtube-downloader

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Language** | Python 3.x |
| **Download Engine** | yt-dlp |
| **HTTP Library** | curl_cffi (improved compatibility) |
| **Testing** | Python unittest (`test.py`) |
| **Documentation** | Sphinx (docutils, alabaster theme) |
| **Dev Tools** | djlint, Faker, pre-commit hooks |
| **Package Manager** | pip |

### Architectural Pattern Detected

**Pattern:** CLI Utility with Variant Scripts  
The project follows a **script variant pattern** — four main entry points, each handling a different use case:

| Variant | Input | Behavior |
|---|---|---|
| `main_noplaylist.py` | Single URL | Download one video, then exit |
| `main_playlist.py` | Playlist URL | Download all videos in playlist |
| `main_loop_noplaylist.py` | Single URL | Download, prompt for next URL |
| `main_loop_playlist.py` | Playlist URL | Download playlist, prompt for next |

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      Script Architecture                      │
│                                                              │
│  User Input (URL)                                             │
│       ↓                                                      │
│  URL Validation                                               │
│       ↓                                                      │
│  yt-dlp Download Engine                                       │
│       ↓                                                      │
│  curl_cffi HTTP Layer → YouTube API                          │
│       ↓                                                      │
│  Download File (MP4/MP3)                                      │
│       ↓                                                      │
│  Loop? → Yes → Repeat                                        │
│    ↓ No                                                      │
│  Exit                                                        │
└──────────────────────────────────────────────────────────────┘
```

### Script Flow (All Variants)

```
Start → Parse URL → Create yt-dlp options → Download → Handle result → Loop/Exit
```

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| yt-dlp over youtube-dl | Active development, more features, better site support |
| curl_cffi for HTTP | Improved TLS fingerprinting compatibility |
| Separate scripts per use case | Clear, focused code for each scenario |
| Loop mode for batch processing | Continuous download without restarting |
| CLI-based, no web interface | Simple, scriptable, resource-efficient |

---

## 4. Key Features

- **Quality Selection**: Multiple quality options (720p, 1080p, etc.)
- **Playlist Support**: Download entire playlists
- **Loop Mode**: Continuous download with user prompts
- **Error Handling**: Try/except for network and download failures
- **curl_cffi**: Improved compatibility with YouTube's CDN

---

## 5. Implementation Patterns

### Basic Download Pattern
```python
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best[height<=1080]',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
```

### Loop Pattern
```python
while True:
    url = input("Enter URL (or 'quit'): ")
    if url.lower() == 'quit':
        break
    download_video(url)
```

---

## 6. Extensibility Points

1. **New download formats**: Add format options to yt-dlp configuration
2. **GUI interface**: Wrap scripts with Tkinter or PyQt
3. **Metadata extraction**: Extend to extract video metadata (subtitles, thumbnails)
4. **Queue management**: Add persistent download queue with database storage
5. **Audio-only mode**: Configure yt-dlp for MP3 extraction

---

*End of architecture blueprint.*
