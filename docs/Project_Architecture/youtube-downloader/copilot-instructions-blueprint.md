# GitHub Copilot Instructions — youtube-downloader

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Script-based** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability and reliability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check requirements for compatibility
   - **Python 3.x**

2. **Framework Versions**: Identify the exact versions of all frameworks
   - No web frameworks — CLI utility only
   - **yt-dlp** for YouTube downloading (with curl_cffi support)

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **yt-dlp** with curl_cffi for download operations
   - **djlint** (if present for HTML template linting)
   - **Faker** for test data (if used)
   - **pre-commit** hooks (if configured)
   - **docutils** + **alabaster** for Sphinx documentation

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar scripts to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: snake_case for functions and files
   - **Script organization**: Clear purpose in naming (noplaylist vs playlist, single vs loop)
   - **Error handling**: Try/except blocks for network and download failures
   - **CLI patterns**: Simple command-line interface
   - **Download quality**: Multiple quality options documented
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 conventions
- Use type hints where possible
- Handle network errors gracefully with try/except

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior

## Testing Approach

- Match the exact structure and style of existing tests
- **Manual testing**: `python test.py`
- **Type checking**: mypy (if configured)
- **Lint checking**: ruff (if configured)

## Technology-Specific Guidelines

### Python
- PEP 8 conventions
- snake_case for functions and files
- Each main script has a clear, documented purpose
- Simple CLI interface

### yt-dlp
- Use for YouTube video/playlist downloads
- Support multiple quality options (720p, 1080p, etc.)
- Handle network failures with retry logic
- Keep yt-dlp updated to handle site changes

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns (try/except for network failures)
- Validate URLs before downloading — avoid SSRF via malicious URLs
- Respect YouTube's Terms of Service and copyright
- Keep yt-dlp updated

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Python-based YouTube video downloader with playlist support and continuous loop mode
- Uses yt-dlp for download operations with curl_cffi support
- Multiple quality options available
- Features: single video download, playlist download, loop mode for batch processing
- No build step — run directly with Python
- No deployment configuration — CLI tool, not a web service
- FFmpeg may be required for some format conversions
