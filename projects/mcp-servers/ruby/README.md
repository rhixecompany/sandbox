# ruby-mcp-server

A Ruby MCP (Model Context Protocol) server built with the `mcp` gem.

## Requirements

- Ruby 3.0+
- Bundler

## Installation

```bash
bundle install
```

## Usage

Start the server:

```bash
bin/mcp-server
```

## Tools

### greet

Greet a person by name with an optional title.

**Parameters:**
- `name` (string, required) — The name of the person to greet
- `title` (string, optional) — Optional title (e.g. Mr., Ms., Dr.)

### calculate

Perform basic arithmetic operations.

**Parameters:**
- `operation` (string, required) — One of `add`, `subtract`, `multiply`, `divide`
- `a` (number, required) — First operand
- `b` (number, required) — Second operand

## Development

Run tests:

```bash
rake test
```

Run style checks:

```bash
rake lint
```

## License

MIT
