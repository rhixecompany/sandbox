# Copilot SDK — Quick Start Template

## Project Setup

- **Language**: {{ TypeScript | Python | Go | .NET }}
- **Runtime**: {{ Node.js 18+ | Python 3.8+ | Go 1.21+ | .NET 8.0+ }}

## Installation

```bash
# {{ package manager command }}
```

## Minimal Example

```{{ language }}
{{ code snippet for creating a client, session, and sending a prompt }}
```

## Configuration

| Option | Value |
|--------|-------|
| model | {{ model name }} |
| streaming | {{ true/false }} |
| sessionId | {{ custom ID }} |
| tools | {{ list of custom tools }} |

## Custom Tools

- **Tool 1**: {{ name }} — {{ description }}
- **Tool 2**: {{ name }} — {{ description }}

## Verification

- [ ] Copilot CLI is installed and authenticated: `copilot --version`
- [ ] SDK client starts without errors
- [ ] Session created successfully
- [ ] Prompt gets a response
- [ ] Cleanup: `client.stop()` is called
- [ ] Errors are handled (ENOENT, ECONNREFUSED)

## Notes

{{ additional context }}