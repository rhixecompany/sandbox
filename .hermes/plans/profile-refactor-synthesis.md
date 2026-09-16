# Unified Profile Refactor Synthesis (from 8 feature docs at docs/features/)
- Sources (verified real content): overview, mcp, memory, skills, tools, tool-gateway, kanban, hooks (57-2007 lines each, stat-confirmed)
- Synthesis method: extract frontmatter titles + core concepts; synthesize into identity updates; DRY via shared sections.
- Key unified themes:
  1. Feature awareness (overview): profile knows available Hermes features (memory/browser/vision/fallback/pools/cache).
  2. MCP awareness (mcp): profile understands external server integration, auth, timeouts, identity headers.
  3. Memory discipline (memory): USER.md/USER profile = identity/preferences/communication/style/timezone; MEMORY.md = bounded §-delimited notes; save/skip rules; session DB truth; skills gate.
  4. Skill discipline (skills): SKILL.md structure (YAML frontmatter + body >=10 lines); progressive disclosure; hub state; fallback/requires/requires_toolsets; security gate.
  5. Tool discipline (tools): multi-category tool awareness; orchestration (todo/clarify/execute/delegate); memory/session search.
  6. Gateway awareness (tool-gateway): gateway endpoints, image generation model selection, provider-independent tool access.
  7. Orchestration (kanban): multi-agent board awareness; parallel-collision awareness; run tracking.
  8. Hook awareness (hooks): lifecycle hooks (pre/post/interrupt/start); session/task/turn context; deterministic non-blocking; append-only logs.
- DRY enforcement: shared identity updates referenced by profile routing (default/code-architect/research-analyst/exec-assistant/design/creative/ops/adminbot/teaching); profile-specific customization only in routing table and model/provider choice.
