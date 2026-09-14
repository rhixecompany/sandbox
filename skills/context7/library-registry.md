---
name: context7-library-registry
description: "External Library Registry"
version: 1.0.0
author: Alexa
---
     1|# External Library Registry
     2|
     3|## Purpose
     4|
     5|This file lists external libraries/frameworks that should use **ExternalScout** (via Context7) for live documentation instead of relying on potentially outdated training data.
     6|
     7|## When to Use This
     8|
     9|**ContextScout** checks this list when:
    10|
    11|1. User asks about a library/framework
    12|2. No internal context exists in `.opencode/context/development/frameworks/`
    13|3. Query matches a library name below
    14|
    15|**Action**: Recommend **ExternalScout** subagent
    16|
    17|---
    18|
    19|## Supported Libraries
    20|
    21|### Database & ORM
    22|
    23|#### Drizzle ORM
    24|
    25|- **Aliases**: `drizzle`, `drizzle-orm`, `drizzle orm`
    26|- **Docs**: https://orm.drizzle.team/
    27|- **Context7**: `use context7 for drizzle`
    28|- **Common topics**: schema organization, migrations, relational queries, transactions, TypeScript types
    29|
    30|#### Prisma
    31|
    32|- **Aliases**: `prisma`
    33|- **Docs**: https://www.prisma.io/docs
    34|- **Context7**: `use context7 for prisma`
    35|- **Common topics**: schema, migrations, client, relations, TypeScript
    36|
    37|---
    38|
    39|### Authentication
    40|
    41|#### Better Auth
    42|
    43|- **Aliases**: `better-auth`, `better auth`, `betterauth`
    44|- **Docs**: https://www.better-auth.com/docs
    45|- **Context7**: `use context7 for better-auth`
    46|- **Common topics**: Next.js integration, Drizzle adapter, social providers, session management, 2FA
    47|
    48|#### NextAuth.js
    49|
    50|- **Aliases**: `nextauth`, `next-auth`, `nextauth.js`
    51|- **Docs**: https://next-auth.js.org/
    52|- **Context7**: `use context7 for nextauth`
    53|- **Common topics**: providers, callbacks, sessions, JWT
    54|
    55|#### Clerk
    56|
    57|- **Aliases**: `clerk`
    58|- **Docs**: https://clerk.com/docs
    59|- **Context7**: `use context7 for clerk`
    60|- **Common topics**: authentication, user management, organizations
    61|
    62|---
    63|
    64|### Frontend Frameworks
    65|
    66|#### Next.js
    67|
    68|- **Aliases**: `nextjs`, `next.js`, `next`
    69|- **Docs**: https://nextjs.org/docs
    70|- **Context7**: `use context7 for nextjs`
    71|- **Common topics**: App Router, Server Actions, Server Components, routing, middleware, API routes
    72|
    73|#### React
    74|
    75|- **Aliases**: `react`, `reactjs`, `react.js`
    76|- **Docs**: https://react.dev/
    77|- **Context7**: `use context7 for react`
    78|- **Common topics**: hooks, components, state, effects, context
    79|
    80|#### TanStack Query
    81|
    82|- **Aliases**: `tanstack query`, `react query`, `@tanstack/react-query`
    83|- **Docs**: https://tanstack.com/query/latest
    84|- **Context7**: `use context7 for tanstack query`
    85|- **Common topics**: useQuery, useMutation, prefetching, caching, Server Components
    86|
    87|#### TanStack Router
    88|
    89|- **Aliases**: `tanstack router`, `@tanstack/react-router`
    90|- **Docs**: https://tanstack.com/router/latest
    91|- **Context7**: `use context7 for tanstack router`
    92|- **Common topics**: routing, type-safe routes, loaders, navigation
    93|
    94|#### TanStack Start
    95|
    96|- **Aliases**: `tanstack start`, `@tanstack/start`
    97|- **Docs**: https://tanstack.com/start/latest
    98|- **Context7**: `use context7 for tanstack start`
    99|- **Common topics**: full-stack setup, server functions, file routing
   100|
   101|---
   102|
   103|### Infrastructure & Deployment
   104|
   105|#### Cloudflare Workers
   106|
   107|- **Aliases**: `cloudflare workers`, `cloudflare`, `workers`, `cf workers`
   108|- **Docs**: https://developers.cloudflare.com/workers
   109|- **Context7**: `use context7 for cloudflare workers`
   110|- **Common topics**: routing, KV storage, Durable Objects, bindings, middleware
   111|
   112|#### AWS Lambda
   113|
   114|- **Aliases**: `aws lambda`, `lambda`, `aws λ`
   115|- **Docs**: https://docs.aws.amazon.com/lambda
   116|- **Context7**: `use context7 for aws lambda`
   117|- **Common topics**: handlers, layers, environment variables, triggers, TypeScript
   118|
   119|#### Vercel
   120|
   121|- **Aliases**: `vercel`
   122|- **Docs**: https://vercel.com/docs
   123|- **Context7**: `use context7 for vercel`
   124|- **Common topics**: deployment, environment variables, edge functions, serverless
   125|
   126|---
   127|
   128|### UI Libraries & Styling
   129|
   130|#### Shadcn/ui
   131|
   132|- **Aliases**: `shadcn`, `shadcn/ui`, `shadcn-ui`
   133|- **Docs**: https://ui.shadcn.com/
   134|- **Context7**: `use context7 for shadcn`
   135|- **Common topics**: components, installation, theming, customization
   136|
   137|#### Radix UI
   138|
   139|- **Aliases**: `radix`, `radix ui`, `radix-ui`, `@radix-ui`
   140|- **Docs**: https://www.radix-ui.com/
   141|- **Context7**: `use context7 for radix`
   142|- **Common topics**: primitives, accessibility, composition
   143|
   144|#### Tailwind CSS
   145|
   146|- **Aliases**: `tailwind`, `tailwindcss`, `tailwind css`
   147|- **Docs**: https://tailwindcss.com/docs
   148|- **Context7**: `use context7 for tailwind`
   149|- **Common topics**: configuration, utilities, responsive design, dark mode
   150|
   151|---
   152|
   153|### State Management
   154|
   155|#### Zustand
   156|
   157|- **Aliases**: `zustand`
   158|- **Docs**: https://zustand-demo.pmnd.rs/
   159|- **Context7**: `use context7 for zustand`
   160|- **Common topics**: store creation, selectors, middleware, TypeScript
   161|
   162|#### Jotai
   163|
   164|- **Aliases**: `jotai`
   165|- **Docs**: https://jotai.org/
   166|- **Context7**: `use context7 for jotai`
   167|- **Common topics**: atoms, async atoms, utilities
   168|
   169|---
   170|
   171|### Validation & Forms
   172|
   173|#### Zod
   174|
   175|- **Aliases**: `zod`
   176|- **Docs**: https://zod.dev/
   177|- **Context7**: `use context7 for zod`
   178|- **Common topics**: schema validation, TypeScript inference, parsing, refinements
   179|
   180|#### React Hook Form
   181|
   182|- **Aliases**: `react hook form`, `react-hook-form`, `rhf`
   183|- **Docs**: https://react-hook-form.com/
   184|- **Context7**: `use context7 for react hook form`
   185|- **Common topics**: register, validation, errors, TypeScript
   186|
   187|---
   188|
   189|### Testing
   190|
   191|#### Vitest
   192|
   193|- **Aliases**: `vitest`
   194|- **Docs**: https://vitest.dev/
   195|- **Context7**: `use context7 for vitest`
   196|- **Common topics**: configuration, testing, mocking, coverage
   197|
   198|#### Playwright
   199|
   200|- **Aliases**: `playwright`
   201|- **Docs**: https://playwright.dev/
   202|- **Context7**: `use context7 for playwright`
   203|- **Common topics**: browser automation, testing, selectors, assertions
   204|
   205|---
   206|
   207|## Detection Patterns
   208|
   209|ContextScout and ExternalScout should match queries containing:
   210|
   211|- Library name (case-insensitive)
   212|- Common variations (e.g., "next.js" vs "nextjs")
   213|- Package names (e.g., "@tanstack/react-query")
   214|
   215|**Examples**:
   216|
   217|- "How do I use **Drizzle** with PostgreSQL?" → Match: Drizzle ORM
   218|- "Show me **Next.js** App Router setup" → Match: Next.js
   219|- "**TanStack Query** with Server Components" → Match: TanStack Query
   220|- "**Better Auth** integration" → Match: Better Auth
   221|
   222|---
   223|
   224|## Query Optimization Patterns
   225|
   226|### Drizzle ORM
   227|
   228|| User Intent | Optimized Query |
   229|| --- | --- |
   230|| Setup/Installation | `PostgreSQL+setup+configuration+TypeScript+installation` |
   231|| Modular schemas | `modular+schema+organization+domain+driven+design` |
   232|| Relations | `relational+queries+one+to+many+joins+with+relations` |
   233|| Migrations | `drizzle-kit+migrations+generate+push+PostgreSQL` |
   234|| Transactions | `database+transactions+patterns+TypeScript` |
   235|| Type safety | `TypeScript+type+inference+schema+types+inferInsert` |
   236|
   237|### Better Auth
   238|
   239|| User Intent | Optimized Query |
   240|| --- | --- |
   241|| Setup | `setup+configuration+Next.js+TypeScript+installation` |
   242|| Next.js integration | `Next.js+App+Router+integration+setup+configuration` |
   243|| Drizzle adapter | `Drizzle+adapter+PostgreSQL+schema+generation+configuration` |
   244|| Social providers | `social+providers+OAuth+GitHub+Google+setup` |
   245|| Email/password | `email+password+authentication+signup+signin` |
   246|| Session management | `session+management+cookies+JWT+middleware` |
   247|
   248|### Next.js
   249|
   250|| User Intent | Optimized Query |
   251|| --- | --- |
   252|| App Router | `App+Router+file+conventions+layouts+pages+routing` |
   253|| Server Actions | `Server+Actions+form+mutations+revalidation+TypeScript` |
   254|| Server Components | `React+Server+Components+async+data+fetching+patterns` |
   255|| Dynamic routes | `dynamic+routes+params+TypeScript+generateStaticParams` |
   256|| Middleware | `middleware+authentication+redirects+headers+cookies` |
   257|| API routes | `API+routes+route+handlers+TypeScript+POST+GET` |
   258|
   259|### TanStack Query
   260|
   261|| User Intent | Optimized Query |
   262|| --- | --- |
   263|| Setup | `setup+QueryClient+provider+Next.js+TypeScript` |
   264|| Data fetching | `useQuery+data+fetching+TypeScript+patterns+async` |
   265|| Mutations | `useMutation+optimistic+updates+invalidation+TypeScript` |
   266|| Prefetching | `prefetchQuery+Server+Components+hydration+Next.js` |
   267|| Caching | `cache+configuration+staleTime+gcTime+invalidation` |
   268|
   269|### Cloudflare Workers
   270|
   271|| User Intent | Optimized Query |
   272|| --- | --- |
   273|| Setup | `getting+started+setup+TypeScript+wrangler+configuration` |
   274|| Routing | `routing+itty-router+hono+request+handling` |
   275|| KV storage | `KV+storage+key+value+bindings+TypeScript` |
   276|| Durable Objects | `Durable+Objects+state+WebSockets+coordination` |
   277|
   278|### AWS Lambda
   279|
   280|| User Intent | Optimized Query |
   281|| --- | --- |
   282|| Setup | `getting+started+setup+TypeScript+handler+configuration` |
   283|| Handlers | `handler+function+event+context+TypeScript+patterns` |
   284|| Layers | `layers+dependencies+shared+code+deployment` |
   285|| Environment variables | `environment+variables+secrets+configuration+SSM` |
   286|
   287|---
   288|
   289|## Adding New Libraries
   290|
   291|To add a new library:
   292|
   293|1. Add entry under appropriate category
   294|2. Include: Name, aliases, docs link, Context7 command, common topics
   295|3. (Optional) Add query optimization patterns
   296|4. Update ExternalScout if needed (usually automatic)
   297|
   298|**Template**:
   299|
   300|```markdown
   301|#### Library Name
   302|
   303|- **Aliases**: `alias1`, `alias2`, `package-name`
   304|- **Docs**: https://example.com/docs
   305|- **Context7**: `use context7 for library-name`
   306|- **Common topics**: topic1, topic2, topic3
   307|```
   308|
   309|---
   310|
   311|## Usage by ExternalScout
   312|
   313|ExternalScout uses this file to:
   314|
   315|1. **Detect** which library the user is asking about
   316|2. **Load** query optimization patterns for that library
   317|3. **Build** optimized Context7 queries
   318|4. **Fetch** live documentation
   319|5. **Return** filtered, relevant results
   320|