---
name: context7-readme
description: "Context7 Skill"
version: 1.0.0
author: Alexa
---
     1|# Context7 Skill
     2|
     3|## Purpose
     4|
     5|Fetches **live, version-specific documentation** for external libraries and frameworks using the Context7 API. Ensures you always get current API patterns instead of potentially outdated training data.
     6|
     7|**Golden Rule**: Always fetch live docs for external libraries—training data may be outdated.
     8|
     9|## Quick Start
    10|
    11|### Recommended: Use ExternalScout Subagent
    12|
    13|The **ExternalScout** subagent is the recommended way to fetch external documentation. It handles:
    14|
    15|- Library detection
    16|- Query optimization
    17|- Documentation filtering and sorting
    18|- Formatted results with code examples
    19|
    20|**Invocation**:
    21|
    22|```
    23|Use ExternalScout to fetch documentation for [Library Name]: [your specific question]
    24|```
    25|
    26|**Example**:
    27|
    28|```
    29|Use ExternalScout to fetch documentation for Drizzle ORM: How do I set up modular schemas with PostgreSQL?
    30|```
    31|
    32|### Alternative: Direct Skill Usage
    33|
    34|You can also invoke the Context7 skill directly via bash:
    35|
    36|```bash
    37|# Step 1: Search for library
    38|curl -s "https://context7.com/api/v2/libs/search?libraryName=LIBRARY&query=TOPIC" | jq '.results[0]'
    39|
    40|# Step 2: Fetch documentation
    41|curl -s "https://context7.com/api/v2/context?libraryId=LIBRARY_ID&query=OPTIMIZED_QUERY&type=txt"
    42|```
    43|
    44|See `SKILL.md` for detailed API documentation.
    45|
    46|## Supported Libraries
    47|
    48|See `library-registry.md` for the complete list of supported libraries including:
    49|
    50|- **Database & ORM**: Drizzle, Prisma
    51|- **Authentication**: Better Auth, NextAuth.js, Clerk
    52|- **Frontend**: Next.js, React, TanStack Query/Router/Start
    53|- **Infrastructure**: Cloudflare Workers, AWS Lambda, Vercel
    54|- **UI**: Shadcn/ui, Radix UI, Tailwind CSS
    55|- **State**: Zustand, Jotai
    56|- **Validation**: Zod, React Hook Form
    57|- **Testing**: Vitest, Playwright
    58|
    59|## Workflow
    60|
    61|```
    62|User Query
    63|    ↓
    64|ContextScout (searches internal context)
    65|    ↓
    66|No internal context found
    67|    ↓
    68|ContextScout recommends ExternalScout
    69|    ↓
    70|ExternalScout invoked
    71|    ├─ Reads library-registry.md
    72|    ├─ Detects library
    73|    ├─ Loads query patterns
    74|    ├─ Fetches from Context7 API
    75|    ├─ Filters & sorts results
    76|    └─ Returns formatted documentation
    77|    ↓
    78|User receives current, actionable docs
    79|```
    80|
    81|## Files
    82|
    83|- **`SKILL.md`** - Context7 API documentation and usage
    84|- **`library-registry.md`** - Supported libraries, aliases, and query patterns
    85|- **`README.md`** - This file (overview and quick start)
    86|
    87|## Adding New Libraries
    88|
    89|To add a new library to the registry:
    90|
    91|1. Edit `library-registry.md`
    92|2. Add entry under appropriate category:
    93|
    94|   ```markdown
    95|   #### Library Name
    96|
    97|   - **Aliases**: `alias1`, `alias2`, `package-name`
    98|   - **Docs**: https://example.com/docs
    99|   - **Context7**: `use context7 for library-name`
   100|   - **Common topics**: topic1, topic2, topic3
   101|   ```
   102|
   103|3. (Optional) Add query optimization patterns
   104|4. ExternalScout will automatically detect the new library
   105|
   106|## Related
   107|
   108|- **ExternalScout**: `.opencode/agents/subagents/core/externalscout.md`
   109|- **ContextScout**: `.opencode/agents/subagents/core/contextscout.md`
   110|