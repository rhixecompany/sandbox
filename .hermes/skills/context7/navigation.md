---
name: context7-navigation
description: "Context7 Skill Navigation"
version: 1.0.0
author: Alexa
---
     1|# Context7 Skill Navigation
     2|
     3|**Purpose**: Live documentation fetching for external libraries via Context7 API
     4|
     5|---
     6|
     7|## Structure
     8|
     9|```
    10|context7/
    11|├── navigation.md              # This file
    12|├── README.md                  # Quick start and workflow
    13|├── SKILL.md                  # Context7 API documentation
    14|└── library-registry.md        # Supported libraries and query patterns
    15|```
    16|
    17|---
    18|
    19|## Quick Routes
    20|
    21|| Task | Path |
    22|| --- | --- |
    23|| **Quick start** | `README.md` |
    24|| **API reference** | `SKILL.md` |
    25|| **Supported libraries** | `library-registry.md` (lines 18-181) |
    26|| **Query patterns** | `library-registry.md` (lines 199-261) |
    27|| **Add new library** | `library-registry.md` (lines 264-279) |
    28|| **ExternalScout integration** | `README.md` (lines 9-26) |
    29|
    30|---
    31|
    32|## By Purpose
    33|
    34|**Using Context7**:
    35|
    36|- Quick start → `README.md`
    37|- API details → `SKILL.md`
    38|
    39|**Adding Libraries**:
    40|
    41|- Template → `library-registry.md` (lines 272-279)
    42|- Supported list → `library-registry.md` (lines 18-181)
    43|
    44|**Integration**:
    45|
    46|- ContextScout workflow → `README.md` (lines 54-73)
    47|- ExternalScout subagent → `.opencode/agents/subagents/core/externalscout.md`
    48|
    49|---
    50|
    51|## Related
    52|
    53|- **ExternalScout**: `.opencode/agents/subagents/core/externalscout.md`
    54|- **ContextScout**: `.opencode/agents/subagents/core/contextscout.md`
    55|