---
name: visual-companion
description: "# Visual Companion Guide"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# Visual Companion Guide
     2|
     3|Browser-based visual brainstorming companion for showing mockups, diagrams, and options.
     4|
     5|## When to Use
     6|
     7|Decide per-question, not per-session. The test: **would the user understand this better by seeing it than reading it?**
     8|
     9|**Use the browser** when the content itself is visual:
    10|
    11|- **UI mockups** — wireframes, layouts, navigation structures, component designs
    12|- **Architecture diagrams** — system components, data flow, relationship maps
    13|- **Side-by-side visual comparisons** — comparing two layouts, two color schemes, two design directions
    14|- **Design polish** — when the question is about look and feel, spacing, visual hierarchy
    15|- **Spatial relationships** — state machines, flowcharts, entity relationships rendered as diagrams
    16|
    17|**Use the terminal** when the content is text or tabular:
    18|
    19|- **Requirements and scope questions** — "what does X mean?", "which features are in scope?"
    20|- **Conceptual A/B/C choices** — picking between approaches described in words
    21|- **Tradeoff lists** — pros/cons, comparison tables
    22|- **Technical decisions** — API design, data modeling, architectural approach selection
    23|- **Clarifying questions** — anything where the answer is words, not a visual preference
    24|
    25|A question _about_ a UI topic is not automatically a visual question. "What kind of wizard do you want?" is conceptual — use the terminal. "Which of these wizard layouts feels right?" is visual — use the browser.
    26|
    27|## How It Works
    28|
    29|The server watches a directory for HTML files and serves the newest one to the browser. You write HTML content to `screen_dir`, the user sees it in their browser and can click to select options. Selections are recorded to `state_dir/events` that you read on your next turn.
    30|
    31|**Content fragments vs full documents:** If your HTML file starts with `<!DOCTYPE` or `<html`, the server serves it as-is (just injects the helper script). Otherwise, the server automatically wraps your content in the frame template — adding the header, CSS theme, selection indicator, and all interactive infrastructure. **Write content fragments by default.** Only write full documents when you need complete control over the page.
    32|
    33|## Starting a Session
    34|
    35|```bash
    36|# Start server with persistence (mockups saved to project)
    37|scripts/start-server.sh --project-dir /path/to/project
    38|
    39|# Returns: {"type":"server-started","port":52341,"url":"http://localhost:52341",
    40|#           "screen_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/content",
    41|#           "state_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/state"}
    42|```
    43|
    44|Save `screen_dir` and `state_dir` from the response. Tell user to open the URL.
    45|
    46|**Finding connection info:** The server writes its startup JSON to `$STATE_DIR/server-info`. If you launched the server in the background and didn't capture stdout, read that file to get the URL and port. When using `--project-dir`, check `<project>/.superpowers/brainstorm/` for the session directory.
    47|
    48|**Note:** Pass the project root as `--project-dir` so mockups persist in `.superpowers/brainstorm/` and survive server restarts. Without it, files go to `/tmp` and get cleaned up. Remind the user to add `.superpowers/` to `.gitignore` if it's not already there.
    49|
    50|**Launching the server by platform:**
    51|
    52|**Claude Code (macOS / Linux):**
    53|
    54|```bash
    55|# Default mode works — the script backgrounds the server itself
    56|scripts/start-server.sh --project-dir /path/to/project
    57|```
    58|
    59|**Claude Code (Windows):**
    60|
    61|```bash
    62|# Windows auto-detects and uses foreground mode, which blocks the tool call.
    63|# Use run_in_background: true on the Bash tool call so the server survives
    64|# across conversation turns.
    65|scripts/start-server.sh --project-dir /path/to/project
    66|```
    67|
    68|When calling this via the Bash tool, set `run_in_background: true`. Then read `$STATE_DIR/server-info` on the next turn to get the URL and port.
    69|
    70|**Codex:**
    71|
    72|```bash
    73|# Codex reaps background processes. The script auto-detects CODEX_CI and
    74|# switches to foreground mode. Run it normally — no extra flags needed.
    75|scripts/start-server.sh --project-dir /path/to/project
    76|```
    77|
    78|**Gemini CLI:**
    79|
    80|```bash
    81|# Use --foreground and set is_background: true on your shell tool call
    82|# so the process survives across turns
    83|scripts/start-server.sh --project-dir /path/to/project --foreground
    84|```
    85|
    86|**Other environments:** The server must keep running in the background across conversation turns. If your environment reaps detached processes, use `--foreground` and launch the command with your platform's background execution mechanism.
    87|
    88|If the URL is unreachable from your browser (common in remote/containerized setups), bind a non-loopback host:
    89|
    90|```bash
    91|scripts/start-server.sh \
    92|  --project-dir /path/to/project \
    93|  --host 0.0.0.0 \
    94|  --url-host localhost
    95|```
    96|
    97|Use `--url-host` to control what hostname is printed in the returned URL JSON.
    98|
    99|## The Loop
   100|
   101|1. **Check server is alive**, then **write HTML** to a new file in `screen_dir`:
   102|   - Before each write, check that `$STATE_DIR/server-info` exists. If it doesn't (or `$STATE_DIR/server-stopped` exists), the server has shut down — restart it with `start-server.sh` before continuing. The server auto-exits after 30 minutes of inactivity.
   103|   - Use semantic filenames: `platform.html`, `visual-style.html`, `layout.html`
   104|   - **Never reuse filenames** — each screen gets a fresh file
   105|   - Use Write tool — **never use cat/heredoc** (dumps noise into terminal)
   106|   - Server automatically serves the newest file
   107|
   108|2. **Tell user what to expect and end your turn:**
   109|   - Remind them of the URL (every step, not just first)
   110|   - Give a brief text summary of what's on screen (e.g., "Showing 3 layout options for the homepage")
   111|   - Ask them to respond in the terminal: "Take a look and let me know what you think. Click to select an option if you'd like."
   112|
   113|3. **On your next turn** — after the user responds in the terminal:
   114|   - Read `$STATE_DIR/events` if it exists — this contains the user's browser interactions (clicks, selections) as JSON lines
   115|   - Merge with the user's terminal text to get the full picture
   116|   - The terminal message is the primary feedback; `state_dir/events` provides structured interaction data
   117|
   118|4. **Iterate or advance** — if feedback changes current screen, write a new file (e.g., `layout-v2.html`). Only move to the next question when the current step is validated.
   119|
   120|5. **Unload when returning to terminal** — when the next step doesn't need the browser (e.g., a clarifying question, a tradeoff discussion), push a waiting screen to clear the stale content:
   121|
   122|   ```html
   123|   <!-- filename: waiting.html (or waiting-2.html, etc.) -->
   124|   <div
   125|     style="display:flex;align-items:center;justify-content:center;min-height:60vh"
   126|   >
   127|     <p class="subtitle">Continuing in terminal...</p>
   128|   </div>
   129|   ```
   130|
   131|   This prevents the user from staring at a resolved choice while the conversation has moved on. When the next visual question comes up, push a new content file as usual.
   132|
   133|6. Repeat until done.
   134|
   135|## Writing Content Fragments
   136|
   137|Write just the content that goes inside the page. The server wraps it in the frame template automatically (header, theme CSS, selection indicator, and all interactive infrastructure).
   138|
   139|**Minimal example:**
   140|
   141|```html
   142|<h2>Which layout works better?</h2>
   143|<p class="subtitle">Consider readability and visual hierarchy</p>
   144|
   145|<div class="options">
   146|  <div class="option" data-choice="a" onclick="toggleSelect(this)">
   147|    <div class="letter">A</div>
   148|    <div class="content">
   149|      <h3>Single Column</h3>
   150|      <p>Clean, focused reading experience</p>
   151|    </div>
   152|  </div>
   153|  <div class="option" data-choice="b" onclick="toggleSelect(this)">
   154|    <div class="letter">B</div>
   155|    <div class="content">
   156|      <h3>Two Column</h3>
   157|      <p>Sidebar navigation with main content</p>
   158|    </div>
   159|  </div>
   160|</div>
   161|```
   162|
   163|That's it. No `<html>`, no CSS, no `<script>` tags needed. The server provides all of that.
   164|
   165|## CSS Classes Available
   166|
   167|The frame template provides these CSS classes for your content:
   168|
   169|### Options (A/B/C choices)
   170|
   171|```html
   172|<div class="options">
   173|  <div class="option" data-choice="a" onclick="toggleSelect(this)">
   174|    <div class="letter">A</div>
   175|    <div class="content">
   176|      <h3>Title</h3>
   177|      <p>Description</p>
   178|    </div>
   179|  </div>
   180|</div>
   181|```
   182|
   183|**Multi-select:** Add `data-multiselect` to the container to let users select multiple options. Each click toggles the item. The indicator bar shows the count.
   184|
   185|```html
   186|<div class="options" data-multiselect>
   187|  <!-- same option markup — users can select/deselect multiple -->
   188|</div>
   189|```
   190|
   191|### Cards (visual designs)
   192|
   193|```html
   194|<div class="cards">
   195|  <div
   196|    class="card"
   197|    data-choice="design1"
   198|    onclick="toggleSelect(this)"
   199|  >
   200|    <div class="card-image"><!-- mockup content --></div>
   201|    <div class="card-body">
   202|      <h3>Name</h3>
   203|      <p>Description</p>
   204|    </div>
   205|  </div>
   206|</div>
   207|```
   208|
   209|### Mockup container
   210|
   211|```html
   212|<div class="mockup">
   213|  <div class="mockup-header">Preview: Dashboard Layout</div>
   214|  <div class="mockup-body"><!-- your mockup HTML --></div>
   215|</div>
   216|```
   217|
   218|### Split view (side-by-side)
   219|
   220|```html
   221|<div class="split">
   222|  <div class="mockup"><!-- left --></div>
   223|  <div class="mockup"><!-- right --></div>
   224|</div>
   225|```
   226|
   227|### Pros/Cons
   228|
   229|```html
   230|<div class="pros-cons">
   231|  <div class="pros">
   232|    <h4>Pros</h4>
   233|    <ul>
   234|      <li>Benefit</li>
   235|    </ul>
   236|  </div>
   237|  <div class="cons">
   238|    <h4>Cons</h4>
   239|    <ul>
   240|      <li>Drawback</li>
   241|    </ul>
   242|  </div>
   243|</div>
   244|```
   245|
   246|### Mock elements (wireframe building blocks)
   247|
   248|```html
   249|<div class="mock-nav">Logo | Home | About | Contact</div>
   250|<div style="display: flex;">
   251|  <div class="mock-sidebar">Navigation</div>
   252|  <div class="mock-content">Main content area</div>
   253|</div>
   254|<button class="mock-button">Action Button</button>
   255|<input class="mock-input" placeholder="Input field" />
   256|<div class="placeholder">Placeholder area</div>
   257|```
   258|
   259|### Typography and sections
   260|
   261|- `h2` — page title
   262|- `h3` — section heading
   263|- `.subtitle` — secondary text below title
   264|- `.section` — content block with bottom margin
   265|- `.label` — small uppercase label text
   266|
   267|## Browser Events Format
   268|
   269|When the user clicks options in the browser, their interactions are recorded to `$STATE_DIR/events` (one JSON object per line). The file is cleared automatically when you push a new screen.
   270|
   271|```jsonl
   272|{"type":"click","choice":"a","text":"Option A - Simple Layout","timestamp":1706000101}
   273|{"type":"click","choice":"c","text":"Option C - Complex Grid","timestamp":1706000108}
   274|{"type":"click","choice":"b","text":"Option B - Hybrid","timestamp":1706000115}
   275|```
   276|
   277|The full event stream shows the user's exploration path — they may click multiple options before settling. The last `choice` event is typically the final selection, but the pattern of clicks can reveal hesitation or preferences worth asking about.
   278|
   279|If `$STATE_DIR/events` doesn't exist, the user didn't interact with the browser — use only their terminal text.
   280|
   281|## Design Tips
   282|
   283|- **Scale fidelity to the question** — wireframes for layout, polish for polish questions
   284|- **Explain the question on each page** — "Which layout feels more professional?" not just "Pick one"
   285|- **Iterate before advancing** — if feedback changes current screen, write a new version
   286|- **2-4 options max** per screen
   287|- **Use real content when it matters** — for a photography portfolio, use actual images (Unsplash). Placeholder content obscures design issues.
   288|- **Keep mockups simple** — focus on layout and structure, not pixel-perfect design
   289|
   290|## File Naming
   291|
   292|- Use semantic names: `platform.html`, `visual-style.html`, `layout.html`
   293|- Never reuse filenames — each screen must be a new file
   294|- For iterations: append version suffix like `layout-v2.html`, `layout-v3.html`
   295|- Server serves newest file by modification time
   296|
   297|## Cleaning Up
   298|
   299|```bash
   300|scripts/stop-server.sh $SESSION_DIR
   301|```
   302|
   303|If the session used `--project-dir`, mockup files persist in `.superpowers/brainstorm/` for later reference. Only `/tmp` sessions get deleted on stop.
   304|
   305|## Reference
   306|
   307|- Frame template (CSS reference): `scripts/frame-template.html`
   308|- Helper script (client-side): `scripts/helper.js`
   309|