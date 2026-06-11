# Architecture — youtube-downloader

## Overview
A CLI-based YouTube video downloader with multiple operational modes.

## Architecture

### Script Architecture
Each main script follows this pattern:
```
User Input (URL) → yt-dlp download engine → curl_cffi HTTP → YouTube → Download file
                                                                           ↓
                                                                     Loop? → Yes → Repeat
                                                                       ↓ No
                                                                     Exit
```

### Script Variants
| Variant | Input | Behavior |
|---------|-------|----------|
| noplaylist | Single URL | Downloads one video, then exits |
| playlist | Playlist URL | Downloads all videos in playlist |
| loop_noplaylist | Single URL | Downloads video, then prompts for next |
| loop_playlist | Playlist URL | Downloads playlist, then prompts for next |

### Key Design Decisions
1. **yt-dlp** as the download engine (successor to youtube-dl)
2. **curl_cffi** for improved HTTP compatibility
3. Separate scripts for different use cases
4. CLI-based, no web interface
5. Error handling with try/except for network failures

## Data Flow
```
CLI Input → URL Validation → yt-dlp Options → Download Request → Progress Output → File Save
```
