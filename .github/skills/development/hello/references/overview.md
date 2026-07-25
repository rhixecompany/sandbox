# hello.py — Overview

## Purpose
Simple example/placeholder script for testing Hermes script integration and validation. Outputs "Hello, Hermes!" (or a customizable greeting) and demonstrates the standard Hermes script interface — exit codes, option parsing, and output formatting.

## Usage

```bash
python hello.py [--name TEXT] [--count N] [--uppercase] [--repeat] [--output FORMAT] [--verbose] [-h]
```

### Options

| Option       | Description                                                    |
|-------------|----------------------------------------------------------------|
| `--name`     | Name to greet (default: "Hermes")                            |
| `--count`    | Number of times to repeat the greeting (default: 1)           |
| `--uppercase` | Print greeting in uppercase                                       |
| `--repeat`   | Repeat the greeting line by line                               |
| `--output`   | Output format: `text`, `json`, `yaml` (default: `text`)      |
| `--verbose`  | Show additional debug information                             |

## Behavior

- Prints a greeting message to stdout.
- Supports JSON output for testing structured output parsing.
- Returns exit code 0 on success, 1 on invalid arguments.
- Serves as a reference implementation for how Hermes scripts should handle CLI args, output, and exit codes.
- Useful for validating that the Hermes script execution environment is properly set up.

## Example

**Default greeting:**
```bash
python hello.py
# Output: Hello, Hermes!
```

**Custom name repeated 3 times in JSON:**
```bash
python hello.py --name "Agent" --count 3 --output json
# Output: {"greeting": "Hello, Agent!", "count": 3}
```

**Uppercase with verbose:**
```bash
python hello.py --uppercase --verbose
```

## Dependencies

- Python 3.6+
- No external dependencies

## See Also

- `hello-world` — variant with different output patterns
- Hermes script execution guide