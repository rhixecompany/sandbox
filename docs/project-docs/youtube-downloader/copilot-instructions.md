# Copilot Instructions — youtube-downloader

## Python Style
- PEP 8 conventions
- snake_case for functions and files
- Type hints encouraged
- Try/except for network and download failures

## Script Organization
- Each main script has a clear purpose
- Single video vs playlist, single vs loop mode
- CLI-based interface
- Keep yt-dlp updated: `pip install -U yt-dlp`

## Security
- Validate URLs before downloading (prevent SSRF)
- Respect YouTube's Terms of Service
- Don't use for mass downloading or commercial purposes
- Scan downloaded content for malware

## Common Issues
- Update yt-dlp if downloads fail
- Install FFmpeg for format conversions
- Add delays between requests to avoid rate limiting
