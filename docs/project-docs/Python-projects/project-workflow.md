# Project Workflow — Python-projects

## Running Scripts

```bash
# Install dependencies
pip install -r requirements.txt

# Run any script directly
python basic_calculator.py
python qr_code_generator.py
python python_face_detection.py
python web_scraper.py
python email_sender.py
# ... and 13 more scripts
```

## Quality Checks
```bash
ruff check .           # Lint all scripts
mypy *.py              # Type check all scripts
```

## Adding a New Script
1. Create a single `.py` file with snake_case naming
2. Add imports at the top (stdlib first, then third-party)
3. Include `if __name__ == "__main__":` entry point
4. Add dependency to `requirements.txt` if needed
