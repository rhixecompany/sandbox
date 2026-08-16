---
name: mcp-builder-design-principles
description: "Agent-Centric Design Principles for MCP Tools"
version: 1.0.0
author: Alexa
---
     1|# Agent-Centric Design Principles for MCP Tools
     2|
     3|This document contains detailed guidance on designing tools for AI agents. This is supplementary reading; the main SKILL.md focuses on MCP-specific implementation patterns.
     4|
     5|## Build for Workflows, Not Just API Endpoints
     6|
     7|Don't simply wrap existing API endpoints—build thoughtful, high-impact workflow tools that agents can use to accomplish real tasks.
     8|
     9|- **Consolidate related operations**: Create composite tools that combine multiple API calls. Example: `schedule_event` tool that both checks availability AND creates the event, rather than separate `check_availability` and `create_event` tools.
    10|- **Focus on complete tasks**: Design tools that enable agents to accomplish meaningful work, not just expose individual API endpoints.
    11|- **Consider agent workflows**: Think about what multi-step workflows agents actually need to accomplish, then design tools that enable those workflows efficiently.
    12|
    13|## Optimize for Limited Context
    14|
    15|Agents have constrained context windows. Every response token counts. Design your tools with this scarcity in mind.
    16|
    17|- **Return high-signal information only**: Don't return exhaustive data dumps. Return only the information the agent actually needs.
    18|- **Provide response detail options**: Support "concise" and "detailed" response modes. Default to concise.
    19|- **Use human-readable identifiers**: Prefer names over technical IDs in responses. Agents understand "John Smith" better than "user_12847".
    20|- **Consider context budget as a resource**: If pagination is available, use it. If truncation is necessary, truncate intelligently.
    21|
    22|## Design Actionable Error Messages
    23|
    24|Error messages should guide agents toward successful tool usage, not just report failures.
    25|
    26|- **Guide toward correct usage**: Suggest specific next steps. Example: "Try using filter='active_only' to reduce results" instead of "Too many results".
    27|- **Make errors educational**: Help agents learn proper usage patterns through clear, specific feedback.
    28|- **Be actionable**: Every error message should suggest what the agent should try next.
    29|
    30|## Follow Natural Task Subdivisions
    31|
    32|Design tool names and groupings that match how humans think about tasks.
    33|
    34|- **Use consistent prefixes**: Group related tools with consistent naming patterns (`search_*`, `get_*`, `list_*`, `create_*`).
    35|- **Tool names reflect human workflows**: "schedule_meeting" is better than "create_calendar_event" because it matches how users think about the task.
    36|- **Design around workflows, not API structure**: Don't expose the API structure directly; abstract it into natural task workflows.
    37|
    38|## Use Evaluation-Driven Development
    39|
    40|Test your MCP server against realistic agent use cases early and often.
    41|
    42|- **Create evaluation scenarios early**: Before implementation, sketch out realistic questions agents might ask.
    43|- **Let agent feedback drive improvements**: Use agent performance to identify which tools are missing or poorly designed.
    44|- **Prototype and iterate quickly**: Build a basic server, test it with evaluation questions, then improve based on results.
    45|