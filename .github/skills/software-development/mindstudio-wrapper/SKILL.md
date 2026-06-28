---
author: Hermes Assistant
description: Composable wrapper skill for common MindStudio action patterns — text
  generation, image generation, web search, batch operations, and agent orchestration
  via the MindStudio MCP server.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: mindstudio-wrapper
tags:
- mindstudio
- wrapper
- ai
- generation
- search
- batch
- mcp
title: Mindstudio Wrapper
version: 1.0.0

---
# MindStudio Wrapper Skill

This skill provides composable workflows for common MindStudio action patterns. It wraps the MindStudio MCP server tools (177+ actions) into reusable patterns for:

- Text generation with model selection
- Image/video/audio generation with cost estimation
- Web search and research
- Batch parallel execution
- Pre-built agent orchestration
- OAuth connector integrations

## Prerequisites

1. **MindStudio MCP server configured** in Hermes:
   ```yaml
   mcp_servers:
     mindstudio:
       command: node
       args: ["mcp"]
       working_dir: C:/Users/Alexa/AppData/Local/hermes/plugins/mindstudio-agent
       env:
         MINDSTUDIO_API_KEY: ${MINDSTUDIO_API_KEY}
       enabled: true
   ```

2. **MindStudio API key** — Run `mindstudio login` or set `MINDSTUDIO_API_KEY` in `.env`

3. **MCP server reloaded** — Run `hermes /reset` or `/reload-mcp` in session

## Core Patterns

### Pattern 1: Text Generation with Model Selection

```typescript
// Discover available models first
const { models } = await mindstudio.listModelsSummaryByType("llm_chat");
const model = models.find(m => m.name.includes("Claude")) || models[0];

// Generate text with specific model
const { content } = await mindstudio.generateText({
  message: "Your prompt here",
  modelOverride: {
    model: model.id,
    temperature: 0.7,
    maxResponseTokens: 16000,
  },
});
```

### Pattern 2: Image Generation with Cost Estimation

```typescript
// Estimate cost first
const estimate = await mindstudio.estimateActionCost({
  stepType: "generateImage",
  step: { prompt: "A cyberpunk city at sunset" },
});
console.log(`Estimated cost: ${estimate.estimates?.[0]?.cost} credits`);

// Generate image
const { imageUrl } = await mindstudio.generateImage({
  prompt: "A cyberpunk city at sunset",
  imageModelOverride: { model: "flux-max-2" },
});
```

### Pattern 3: Web Search + Research Pipeline

```typescript
// Search the web
const { results } = await mindstudio.searchGoogle({
  query: "TypeScript best practices 2024",
  count: 10,
});

// Deep research with You.com
const research = await mindstudio.youDotComWebResearch({
  input: "Comprehensive analysis of TypeScript 5.5 new features",
  researchEffort: "deep",
});

// Extract full content from URLs
const content = await mindstudio.youDotComGetPageContent({
  urls: results.map(r => r.url).slice(0, 5),
  formats: ["markdown"],
});
```

### Pattern 4: Batch Parallel Execution (50 steps max)

```typescript
const result = await mindstudio.executeStepBatch({
  steps: [
    { stepType: "generateImage", step: { prompt: "A sunset" } },
    { stepType: "textToSpeech", step: { text: "Welcome" } },
    { stepType: "searchGoogle", step: { query: "AI news" } },
    { stepType: "generateVideo", step: { prompt: "Clouds moving" } },
  ],
});

// Each result has: stepType, output?, error?, billingCost?
for (const r of result.results) {
  if (r.error) console.error(`${r.stepType} failed: ${r.error}`);
  else console.log(`${r.stepType}:`, r.output);
}
```

### Pattern 5: Run Pre-built Agent

```typescript
// List available agents
const { apps } = await mindstudio.listAgents();

// Run specific agent (only run agents user explicitly asks for)
const result = await mindstudio.runAgent({
  appId: "your-agent-id",
  variables: { query: "Summarize latest AI news" },
});
console.log(result.result);
```

### Pattern 6: OAuth Connector Actions (requires user connection)

```typescript
// Browse connectors
const { services } = await mindstudio.listConnectors();
// Find Slack connector
const slack = services.find(s => s.id === "slack");

// Get action details
const { action } = await mindstudio.getConnectorAction(
  "slack",
  "slack/send-message"
);

// List user's OAuth connections
const { connections } = await mindstudio.listConnections();
// Use a connection ID from the list
const result = await mindstudio.runFromConnectorRegistry({
  serviceId: "slack",
  actionId: "slack/send-message",
  connectionId: "your-connection-id",
  // ... action-specific fields from getConnectorAction()
  channel: "#general",
  text: "Hello from MindStudio!",
});
```

### Pattern 7: Autonomous Task Agent (multi-step loop)

```typescript
const result = await mindstudio.runTask({
  prompt: "Research this company and create a summary report",
  input: { companyName: "Anthropic" },
  tools: ["searchGoogle", "scrapeUrl", "analyzeImage", "generateText"],
  structuredOutputExample: '{"name": "...", "summary": "...", "keyFacts": [...], "url": "..."}',
  model: "claude-4-6-sonnet",
});
// result.output matches the structuredOutputExample schema
```

## SDK Ask Tool (Expert Guidance)

Use the built-in `ask` tool for SDK expertise:

```bash
# From CLI
mindstudio ask "generate an image with FLUX"
mindstudio ask "what models support vision?"
mindstudio ask "how do I send a Slack message with an attachment?"

# From MCP tools
await mindstudio.ask({ question: "generate an image with FLUX" });
```

Returns: Complete TypeScript code with real model IDs, config options, no placeholders.

## Common Action Reference

| Category | Actions |
|----------|---------|
| **Text** | `generateText`, `userMessage`, `analyzeImage`, `analyzeVideo`, `detectPII`, `redactPII` |
| **Image** | `generateImage`, `enhanceImageGenerationPrompt`, `removeBackgroundFromImage`, `upscaleImage`, `watermarkImage`, `imageFaceSwap`, `imageRemoveWatermark` |
| **Video** | `generateVideo`, `generateLipsync`, `addSubtitlesToVideo`, `captureThumbnail`, `mergeVideos`, `resizeVideo`, `upscaleVideo`, `videoFaceSwap`, `videoRemoveBackground`, `watermarkVideo`, `extractAudioFromVideo` |
| **Audio** | `generateMusic`, `textToSpeech`, `transcribeAudio`, `mergeAudio` |
| **3D** | `generate3dModel`, `meshyTextTo3d`, `meshyImageTo3d`, `meshyRig`, `meshyAnimate`, `meshyRemesh`, `meshyTexture` |
| **Web/Search** | `searchGoogle`, `searchPerplexity`, `searchYoutube`, `searchGoogleNews`, `scrapeUrl`, `scrapeXProfile`, `scrapeLinkedInProfile`, `scrapeInstagramProfile`, `screenshotUrl`, `extractText`, `youDotComWebSearch`, `youDotComWebResearch` |
| **Data/RAG** | `createDataSource`, `uploadDataSourceDocument`, `queryDataSource`, `listDataSources`, `fetchDataSourceDocument` |
| **Docs/Sheets** | `createGoogleDoc`, `fetchGoogleDoc`, `updateGoogleDoc`, `createGoogleSheet`, `fetchGoogleSheet`, `updateGoogleSheet`, `getGoogleSheetInfo` |
| **Slack/Discord** | `postToSlackChannel`, `sendSlackDirectMessage`, `fetchSlackChannelHistory`, `discordSendMessage`, `discordEditMessage`, `discordSendFollowUp` |
| **Email** | `sendEmail`, `sendGmailMessage`, `createGmailDraft`, `listGmailEmails`, `searchGmailEmails` |
| **Social** | `postToX`, `postToLinkedIn`, `postToZapier`, `makeDotComRunScenario`, `n8nRunNode` |
| **Workflow** | `runPackagedWorkflow`, `runTask`, `executeStepBatch`, `detectChanges`, `logic`, `checkAppRole`, `listPackagedWorkflows` |
| **Charts/Assets** | `generateChart`, `generateAsset`, `generatePdf` |

## Error Handling

```typescript
import { MindStudioError } from '@mindstudio-ai/agent';

try {
  await mindstudio.generateImage({ prompt: "..." });
} catch (err) {
  if (err instanceof MindStudioError) {
    console.error(err.message);  // Human-readable
    console.error(err.code);     // "invalid_step_config", "api_error", "call_cap_exceeded"
    console.error(err.status);   // HTTP status
    console.error(err.details);  // Raw API error body
  }
}
```

Results include billing metadata:
```typescript
const result = await mindstudio.generateImage({ prompt: "..." });
console.log(result.$billingCost);     // Cost in credits
console.log(result.$billingEvents);   // Itemized billing
console.log(result.$rateLimitRemaining);
```


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] MindStudio MCP server configured in `config.yaml`
- [ ] `MINDSTUDIO_API_KEY` set in `.env` or via `mindstudio login`
- [ ] `hermes mcp list` shows `mindstudio` as enabled
- [ ] `hermes tools list` shows `mindstudio` tools
- [ ] Run `mindstudio whoami` to verify auth
- [ ] Test with `mindstudio generate-text --message "hello"`

## References

- MindStudio SDK: https://github.com/mindstudio-ai/mindstudio-agent
- MCP Server: `mindstudio mcp` (stdio transport)
- Connector Registry: https://github.com/mindstudio-ai/mscr
- Direct API: https://v1.mindstudio-api.com
- llms.txt (full reference): `C:/Users/Alexa/AppData/Local/hermes/plugins/mindstudio-agent/llms.txt`

---

## Usage in Hermes Sessions

Once the MCP server is active, all MindStudio tools are available as native Hermes tools. Call them directly:

```bash
# In Hermes session, use the tools naturally:
# "Search Google for TypeScript best practices"
# "Generate an image of a cyberpunk city with FLUX"
# "Run a batch of: image generation + text-to-speech + web search"
# "Ask the MindStudio SDK how to send a Slack message"
```

The wrapper patterns above can be composed into more complex workflows as needed.