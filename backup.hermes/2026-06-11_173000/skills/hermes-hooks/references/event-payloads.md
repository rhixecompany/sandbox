# Hook Event Payloads

## sessionStart
```json
{
  "event": "sessionStart",
  "session_id": "abc123",
  "profile": "default",
  "timestamp": "2026-01-15T10:30:00Z",
  "cwd": "/home/user/project"
}
```

## sessionEnd
```json
{
  "event": "sessionEnd",
  "session_id": "abc123",
  "profile": "default",
  "timestamp": "2026-01-15T11:45:00Z",
  "duration_seconds": 4500,
  "message_count": 42,
  "tool_calls": 18
}
```

## userPromptSubmitted
```json
{
  "event": "userPromptSubmitted",
  "session_id": "abc123",
  "profile": "default",
  "timestamp": "2026-01-15T10:35:00Z",
  "prompt": "Help me debug this TypeScript error",
  "toolsets": ["web", "terminal", "file"]
}
```

## Field Descriptions
| Field | Type | Description |
|-------|------|-------------|
| `event` | string | Event type: sessionStart, sessionEnd, userPromptSubmitted |
| `session_id` | string | Unique session identifier |
| `profile` | string | Active Hermes profile name |
| `timestamp` | string | ISO 8601 timestamp |
| `cwd` | string | Working directory (sessionStart only) |
| `duration_seconds` | integer | Session duration (sessionEnd only) |
| `message_count` | integer | Total messages in session (sessionEnd only) |
| `tool_calls` | integer | Total tool calls (sessionEnd only) |
| `prompt` | string | User's prompt text (userPromptSubmitted only) |
| `toolsets` | array | Active toolsets (userPromptSubmitted only) |

## Parsing in Hook Script
```bash
event=$(echo "$input" | jq -r '.event')
session_id=$(echo "$input" | jq -r '.session_id')
prompt=$(echo "$input" | jq -r '.prompt // empty')
```