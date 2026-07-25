# hello_world.py — Overview

## Purpose
Simple example/placeholder script demonstrating standard Hermes script patterns. Outputs "Hello, World!" (or a customizable greeting with various output modes) and serves as a reference template for new Hermes script authors.

## Usage

```bash
python hello_world.py [--greeting TEXT] [--name TEXT] [--count N] [--capitalize] [--output FORMAT] [--file PATH] [--append] [-h]
```

### Options

| Option        | Description                                                    |
|--------------|----------------------------------------------------------------|
| `--greeting` | Greeting word to use (default: "Hello")                       |
| `--name`     | Name to address (default: "World")                            |
| `--count`    | Number of repetitions (default: 1)                            |
| `--capitalize` | Capitalize the output                                      |
| `--output`   | Output format: `text`, `json`, `yaml`, `csv`                  |
| `--file`     | Write output to a file instead of stdout                    |
| `--append`   | Append to file (when `--file` is used) instead of overwriting  |

## Behavior

- Constructs and prints a greeting string.
- Supports structured output formats (JSON, YAML) for testing integration with other tools.
- When `--file` is specified, redirects output to the given path.
- Exits with code 0 on success, 1 on invalid args, 2 on file write errors.
- Serves as a minimal working example for understanding Hermes script structure, conventions, and best practices.

## Example

**Default greeting:**
```bash
python hello_world.py
# Output: Hello, World!
```

**Custom greeting to file:**
```bash
python hello_world.py --greeting "Greetings" --name "Agent" --file output.txt
```

**JSON output for integration:**
```bash
python hello_world.py --greeting "Hi" --name "Test" --output json
# Output: {"greeting": "Hi", "name": "Test", "message": "Hi, Test!"}
```

## Dependencies

- Python 3.6+
- No external dependencies
- For YAML output: `pyyaml` (optional)

## See Also

- `hello` — similar script with different patterns
- Hermes script interface specification