---
name: mcp-mindstudio
title: MCP MindStudio — Multi-Platform Service Integration
description: Exposes all MindStudio MCP tools for integrating with Google Workspace, Slack, Airtable, Telegram, Gmail, Particle, ActiveCampaign, and other third-party services via OAuth connectors. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - mindstudio
  - connectors
  - google
  - slack
  - airtable
  - telegram
  - gmail
  - integration
---

# MCP MindStudio

Provides a connector-based integration platform via the MindStudio MCP server. Connects to 20+ third-party services through OAuth — Google Workspace (Docs, Sheets, Gmail, Drive), Slack, Airtable, Telegram, ActiveCampaign, and more.

## Prerequisites

- MCP server: `mindstudio` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `mindstudio mcp`
- Connections: Required per service (set up via MindStudio portal or `listConnectors`)

## Tools

| Tool | Description |
|------|-------------|
| `listConnectors` | List all available OAuth connector services and their actions |
| `ask` | Ask how to use MindStudio SDK — existing actions, model IDs, connector details |
| `runFromConnectorRegistry` | Run a raw API connector (direct third-party API call) |
| `redactPII` | Redact PII from text using Microsoft Presidio |
| `detectPII` | Scan text for PII using Microsoft Presidio |
| **Google:** | |
| `fetchGoogleDoc` | Fetch Google Doc as HTML/Markdown/JSON/Plain |
| `fetchGoogleSheet` | Fetch Google Sheet range as CSV/JSON |
| `createGoogleSheet` | Create a Google Sheet from CSV data |
| `getGoogleSheetInfo` | Get sheet metadata (sheets, dimensions) |
| `sendGmailMessage` | Send Gmail (plain/HTML/markdown) |
| `sendGmailDraft` | Send an existing Gmail draft |
| `searchGoogleDrive` | Search Drive by keyword |
| `listGoogleDriveFiles` | List files in a Drive folder |
| `deleteGmailEmail` | Trash a Gmail email |
| **Slack:** | |
| `fetchSlackChannelHistory` | Get recent channel messages |
| `sendSlackDirectMessage` | DM a user |
| `postToSlackChannel` | Post to a channel |
| **Airtable:** | |
| `airtableGetRecord` | Get single record |
| `airtableGetTableRecords` | List records (paginated, max 1000) |
| `airtableCreateUpdateRecord` | Create or update a record |
| `airtableDeleteRecord` | Delete a record |
| **Telegram:** | |
| `telegramSendImage`, `telegramSendVideo`, `telegramSendFile`, `telegramEditMessage` | Send/edit Telegram messages |
| **Particle:** | |
| `particlePodcastsGetEpisode` | Get podcast episode metadata |
| `particlePodcastsSearchCompanies` | Search company knowledge graph |
| **ActiveCampaign:** | |
| `activeCampaignAddNote` | Add note to contact |

## Workflow

### Phase 1: Verify & List Connectors

```
hermes mcp test mindstudio
listConnectors()  # see what's available
ask(question: "what slack actions are available?")
```

### Phase 2: Google Workspace

```
# Read docs
fetchGoogleDoc(documentId: "abc123", exportType: "markdown")

# Sheets
fetchGoogleSheet(spreadsheetId: "abc123", range: "Sheet1!A1:C10", exportType: "json")
createGoogleSheet(title: "Report", csvData: "a,b,c\n1,2,3")

# Drive
searchGoogleDrive(query: "project plan")
listGoogleDriveFiles(folderId: "folder-123")

# Email
sendGmailMessage(to: "user@example.com", subject: "Hi", body: "Hello", messageType: "plain")
```

### Phase 3: Slack & Comms

```
postToSlackChannel(channelId: "C123", text: "Hello team!")
sendSlackDirectMessage(userId: "U123", text: "DM")
fetchSlackChannelHistory(channelId: "C123", limit: 10)
```

### Phase 4: Test Cases

```bash
# 1. Connectivity
hermes mcp test mindstudio

# 2. List connectors (read-only)
# Call: mcp_mindstudio_listConnectors()

# 3. Ask about capabilities (read-only)
# Call: mcp_mindstudio_ask(question: "What actions are available for Slack?")

# 4. PII detection (safe, no I/O)
# Call: mcp_mindstudio_detectPII(input: "Call me at 555-1234", language: "en", entities: ["PHONE_NUMBER"])

# 5. PII redaction (safe, no I/O)
# Call: mcp_mindstudio_redactPII(input: "Email me at test@example.com", language: "en", entities: ["EMAIL_ADDRESS"])
```

## Best Practices

1. **Always call `listConnectors` first** to confirm which services have active OAuth connections
2. **Use `ask` for discovery** — it's an interactive docs tool for MindStudio capabilities
3. **Use `detectPII` before `redactPII`** to preview what will be redacted
4. **Google Sheets ranges use A1 notation** — e.g., `"Sheet1!A1:C10"`
5. **Slack operations require OAuth** — connections set up via MindStudio, not direct token config
6. **Airtable limit is 1,000 records per call** — paginate with offset for larger tables

## Pitfalls

- All third-party operations require **active OAuth connections** — set up via MindStudio portal first
- `runFromConnectorRegistry` requires knowing the exact `serviceId/actionId` format — use `listConnectors` to discover
- Google Doc IDs come from the URL (`https://docs.google.com/document/d/{ID}/edit`)
- Slack channel/user IDs are not handles — need actual IDs from Slack
- Airtable `updateMode: "all"` clears unspecified fields — use `"onlySpecified"` for surgical updates
- Telegram operations require a bot token configured in the MindStudio connector
- `particlePodcastsSearchCompanies` returns different results based on which identifier you pass (q/ticker/domain/cik/qid)

## Verification Checklist

- [ ] `hermes mcp test mindstudio` passes
- [ ] `listConnectors` returns available services
- [ ] `ask` returns capability documentation
- [ ] `detectPII` / `redactPII` work without connectors
