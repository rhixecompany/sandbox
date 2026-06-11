1|# MCP Server Installation Plan
2|
3|> **Status:** Phase 4 - Install Commands Added
4|> **Date:** 2026-06-08
5|> **Goal:** Research, document, install, and verify 50+ MCP servers for Hermes Agent
6|
7|## Phases
8|
9|| Phase | Task | Status |
||-------|------|--------|
|| 1 | Research all MCP servers via web_search | ✅ Complete |
|| 2 | web_extract all found links → save as markdown in `docs/` | ✅ Complete |
|| 3 | Create INDEX.md catalog | ✅ Complete |
|| 4 | Update plan with install commands per server | ✅ Complete |
|| 5 | Install all MCP servers via `hermes mcp add` | ⏳ Pending |
|| 6 | Verify all installations | ⏳ Pending |
10|
11|## Installation Commands
12|
13|> **Important:** Run these commands in a terminal with your API keys configured in environment variables or `.env` files. Hermes `mcp add` is interactive — where needed, the script pattern `echo "y" | hermes mcp add ...` is provided, but you may still need to paste values for prompts that aren't auto-filled by env vars.
14|
15|### Testing / Quality

````bash
16|
17|# Vitest MCP
18|hermes mcp add vitest --preset vitest
19|
20|# Playwright MCP (official Microsoft)
21|hermes mcp add playwright --command npx --args "-y" "@playwright/mcp@latest"
22|
23|```
24|
25|### Frameworks
```bash
26|
27|# Django MCP Server
28|hermes mcp add django --command pip --args "install django-mcp-server"
29|
30|```
31|
32|### AI / Context / Memory
```bash
33|
34|# Context7 (live docs for LLMs)
35|hermes mcp add context7 --url https://mcp.context7.com/mcp --command npx --args "@upstash/context7-mcp"
36|
37|# Memory MCP (reference implementation)
38|hermes mcp add memory --command npx --args "-y" "@modelcontextprotocol/server-memory"
39|
40|```
41|
42|### Error Tracking
```bash
43|
44|# Sentry MCP
45|hermes mcp add sentry --command npx --args "-y" "@sentry/mcp-server"
46|
47|```
48|
49|### Source Control
```bash
50|
51|# GitHub Official MCP Server
52|hermes mcp add github --command npx --args "-y" "@modelcontextprotocol/server-github"
53|
54|# GitMCP
55|hermes mcp add gitmcp --command npx --args "gitmcp"
56|
57|```
58|
59|### Web Retrieval
```bash
60|
61|# Fetch (Model Context Protocol reference)
62|hermes mcp add fetch --command npx --args "-y" "@modelcontextprotocol/server-fetch"
63|
64|# ScrapeGraph
65|hermes mcp add scrapegraph --command npx --args "-y" "@scrapegraph/mcp-server"
66|
67|```
68|
69|### Time / Scheduling
```bash
70|
71|# Time MCP
72|hermes mcp add time --command npx --args "-y" "@modelcontextprotocol/server-time"
73|
74|```
75|
76|### YouTube / Media
```bash
77|
78|# YouTube Transcripts MCP
79|hermes mcp add youtube-transcripts --command npx --args "-y" "@kyong0612/youtube-mcp"
80|
81|```
82|
83|### Desktop Automation
```bash
84|
85|# Desktop Commander
86|hermes mcp add desktop-commander --command npx --args "-y" "@wonderwhy-er/DesktopCommanderMCP"
87|
88|```
89|
90|### Filesystem / Runtime
```bash
91|
92|# Filesystem MCP (reference implementation)
93|hermes mcp add filesystem --command npx --args "-y" "@modelcontextprotocol/server-filesystem"
94|
95|# Node.js Sandbox
96|hermes mcp add node-js-sandbox --command npx --args "-y" "@alfonsograziano/node-code-sandbox-mcp"
97|
98|```
99|
100|### Databases & Storage
```bash
101|
102|# Redis
103|hermes mcp add redis --command npx --args "-y" "@redis/redis-mcp"
104|
105|# SQLite
106|hermes mcp add sqlite --command npx --args "-y" "@modelcontextprotocol/server-sqlite"
107|
108|# Neo4j Memory
109|hermes mcp add neo4j-memory --command npx --args "-y" "@neo4j-contrib/mcp-neo4j"
110|
111|# Neon (Postgres)
112|hermes mcp add neon --url https://mcp.neon.tech/mcp
113|
114|```
115|
116|### Document / Format Conversion
```bash
117|
118|# MarkItDown
119|hermes mcp add markitdown --command uvx --args "markitdown"
120|
121|# Markdownify
122|hermes mcp add markdownify --command npx --args "-y" "@zcaceres/markdownify-mcp"
123|
124|```
125|
126|### Location
```bash
127|
128|# Google Maps
129|hermes mcp add google-maps --command npx --args "-y" "@cablate/mcp-google-map"
130|
131|```
132|
133|### Code & AST Tooling
```bash
134|
135|# ast-grep
136|hermes mcp add ast-grep --command npx --args "-y" "@nothprolands/ast-grep-mcp"
137|
138|```
139|
140|### Developer Tooling
```bash
141|
142|# npm Sentinel
143|hermes mcp add npm-sentinel --command npx --args "-y" "@mcapio/npm-sentinel-mcp"
144|
145|```
146|
147|### News & Content
```bash
148|
149|# Hacker News
150|hermes mcp add hacker-news --command npx --args "-y" "@mozilla/hacker-news-mcp"
151|
152|```
153|
154|### CI / Cloud
```bash
155|
156|# Postman
157|hermes mcp add postman --command npx --args "-y" "@postmanlabs/postman-mcp-server"
158|
159|# Cloud Run
160|hermes mcp add cloud-run --command npx --args "-y" "@google-cloud/cloud-run-mcp"
161|
162|# APify
163|hermes mcp add apify --command npx --args "-y" "@apify/apify-mcp-server"
164|
165|```
166|
167|### Finance & Payments
```bash
168|
169|# Stripe
170|hermes mcp add stripe --command npx --args "-y" "@stripe/stripe-mcp"
171|
172|```
173|
174|### Search & RAG
```bash
175|
176|# Chroma
177|hermes mcp add chroma --command npx --args "-y" "@chroma-core/chroma-mcp"
178|
179|```
180|
181|### DevEx
```bash
182|
183|# Python Refactoring Assistant
184|hermes mcp add python-refactoring --command uvx --args "python-refactoring-assistant"
185|
186|# API Gateway
187|hermes mcp add api-gateway --command npx --args "-y" "@anthropic-ai/api-gateway-mcp"
188|
189|# Next.js Devtools
190|hermes mcp add nextjs-devtools --command npx --args "-y" "@vercel/next-devtools-mcp"
191|
192|# Python Interpreter
193|hermes mcp add python-interpreter --command uvx --args "mcp-python-interpreter"
194|
195|```
196|
197|### Documentation References
```bash
198|
199|# Gemini API Docs
200|hermes mcp add gemini-api-docs --command npx --args "-y" "@google-gemini/api-docs-mcp"
201|
202|```
203|
204|### Hosting / Infrastructure
```bash
205|
206|# Hostinger API
207|hermes mcp add hostinger-api --command npx --args "-y" "@hostinger/api-mcp-server"
208|
209|# Google Flights
210|hermes mcp add google-flights --command npx --args "-y" "@apify/google-flights-mcp-server"
211|
212|# Shadcn UI
213|hermes mcp add shadcn --command npx --args "-y" "@shadcn-ui/shadcn-ui-mcp-server"
214|
215|# UV
216|hermes mcp add uv --command uvx --args "uv"
217|
218|# Linear
219|hermes mcp add linear --url https://mcp.linear.app/mcp --command npx --args "-y" "mcp-remote"
220|
221|```
222|
223|## Already Configured (from existing config)
224|
225|- ✅ filesystem
226|- ✅ linear
227|- ✅ mcp-docker
228|- ✅ playwright
229|- ✅ sequential-thinking
230|- ⚠️ fetch (disabled)
231|- ⚠️ memory-mcp (disabled)
232|- ⚠️ sqlite (disabled)
233|- ⚠️ time (disabled)
234|- ⚠️ github (disabled, needs token)
235|- ⚠️ desktop-commander (disabled)
236|
237|## Target MCP Servers to Install
238|
239|1. vitest
240|2. django
241|3. context7
242|4. sentry
243|5. github official
244|6. gitmcp
245|7. scrapegraph
246|8. memory
57.| 9. youtube transcripts
58.| 10. Desktop Commander
59.| 11. node.js sandbox
60.| 12. redis
61.| 13. markitdown
62.| 14. google maps
63.| 15. ast-grep
64.| 16. npm sentinel
65.| 17. hacker news
66.| 18. markdownify
67.| 19. postman
68.| 20. cloud run
69.| 21. stripe
70.| 22. apify
71.| 23. chroma
72.| 24. python refactoring assistant
73.| 25. neo4j memory
74.| 26. api gateway
75.| 27. next.js devtools
76.| 28. python interpreter
77.| 29. gemini api docs
78.| 30. hostinger api
79.| 31. google flights
80.| 32. neon
81.| 33. shadcn
82.| 34. uv
83|
84|## Notes
85|
86|- **Secrets/API keys** — Where a server requires an API key (GitHub, Google Maps, Neon, etc.), make sure the key is exported in your shell or passed via `--env KEY=value`. Do **not** paste secrets into this plan file.
87|- **Windows / WSL2** — Some servers (Linux-only tooling) may need WSL2. Install / run inside WSL2 if you hit OS errors on Windows.
88|- **Interactive prompts** — If `hermes mcp add` blocks, try `echo "y" | hermes mcp add ...` or run inside a PTY: `hermes mcp add ...` manually in your own terminal.
````

88|- **Interactive prompts** — If `hermes mcp add` blocks, try `echo "y" | hermes mcp add ...` or run inside a PTY: `hermes mcp add ...` manually in your own terminal.
