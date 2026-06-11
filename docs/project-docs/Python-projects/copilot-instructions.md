# Copilot Instructions — Python-projects

## Python Style
- PEP 8 conventions
- snake_case for files and functions
- Type annotations encouraged (mypy configured)
- ruff for linting

## Script Structure
- Each script is standalone and self-contained
- Use `if __name__ == "__main__":` entry point
- Keep imports organized: stdlib, then third-party
- Add docstring at the top of each script

## Security
- Never embed API keys or credentials in scripts
- Validate HTTP responses when using requests
- Process images locally when possible
