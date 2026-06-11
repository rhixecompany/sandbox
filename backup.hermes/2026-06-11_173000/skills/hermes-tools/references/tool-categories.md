# Built-in Tool Categories

| Category | Tools | Description |
|----------|-------|-------------|
| **Web** | `web_search`, `web_extract` | Search the web and extract page content |
| **X Search** | `x_search` | Search X (Twitter) via xAI Responses API (SuperGrok OAuth or `XAI_API_KEY`) |
| **Terminal & Files** | `terminal`, `process`, `read_file`, `patch` | Execute commands and manipulate files |
| **Browser** | `browser_navigate`, `browser_snapshot`, `browser_vision` | Interactive browser automation with text and vision |
| **Media** | `vision_analyze`, `image_generate`, `text_to_speech` | Multimodal analysis and generation |
| **Agent Orchestration** | `todo`, `clarify`, `execute_code`, `delegate_task` | Planning, clarification, code execution, subagent delegation |
| **Memory & Recall** | `memory`, `session_search` | Persistent memory and session search |
| **Automation & Delivery** | `cronjob`, `send_message` | Scheduled tasks + outbound messaging |
| **Integrations** | `ha_*`, MCP server tools | Home Assistant, MCP, and other integrations |

## Tool Gateway (Nous Portal Subscribers)
Paid Nous Portal subscribers can use web search, image generation, TTS, and browser automation through the Tool Gateway — no separate API keys needed.

```bash
hermes model     # Enable via model config
hermes tools     # Configure individual tools
```