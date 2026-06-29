# GitHub Copilot Instructions — Python-projects

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Script-based** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability and readability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `requirements.txt` for library compatibility
   - **Python 3.x** (Python 2 not supported)

2. **Framework Versions**: Identify the exact versions of all frameworks
   - No web frameworks — standalone scripts only
   - Standard library + third-party packages

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **requests** for HTTP operations
   - **opencv-python** for face detection
   - **matplotlib** for graph plotting
   - **pillow** for image processing
   - **qrcode** for QR code generation
   - **beautifulsoup4** for web scraping
   - **schedule** for task scheduling

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar scripts to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: snake_case for files and functions
   - **Code organization**: Single-file scripts, import-free except for standard library + requirements
   - **Error handling**: Try/except blocks for network and I/O operations
   - **CLI patterns**: Simple command-line interface, input/output via stdin/stdout
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 and use typed annotations (mypy configured)
- Use ruff for linting

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior

## Testing Approach

- No formal test framework — each script is self-contained
- Manual testing via execution

## Technology-Specific Guidelines

### Python
- PEP 8 conventions with ruff linting
- Type hints encouraged (mypy configured)
- Standalone, single-file scripts
- Use standard library first, third-party packages only when needed

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never embed API keys or credentials directly in scripts
- Review any network calls for data privacy

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Collection of beginner-friendly Python scripts for learning and automation
- Each script is standalone and self-contained (single file)
- Covers calculators, games, face detection, QR code generation, and more
- No build/deployment needed — run with `python script_name.py`
