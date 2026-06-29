# Tools Required

> Extracted from `boost-prompt.prompt.md`.

## Tools Required

| Tool | Purpose |
| --- | --- |
| `joyride_request_human_input` | Interactive user input via VS Code Joyride extension |
| `vscode.env.clipboard.writeText` | Copy text to system clipboard via Joyride (ClojureScript API) |

### Joyride Setup

**Requirement**: VS Code Joyride extension installed and active

**Installation**:
- Install from VS Code Extensions marketplace: search "Joyride"
- Verify in command palette: `Joyride: Open Prompt Library`

**API Reference**:
- `joyride_request_human_input` - Prompts user for multi-line input via VS Code dialog
- `vscode.env.clipboard.writeText(text)` - Copies text to system clipboard (requires active Joyride context)

**Fallback**: If Joyride is unavailable, manually copy the final prompt from Phase 3 output to your clipboard
