# Cursor AI Agent Cheatsheets Research

**Compiled from:** Official Cursor Docs (cursor.com), design.dev cheatsheet, cursorcheatsheet.com, GitHub repo (knz/cursor-vscode-cheatsheets)

---

## 📋 Official Keyboard Shortcuts (cursor.com/docs/reference/keyboard-shortcuts)

### General
| Shortcut | Action |
|---|---|
| `Cmd I` / `Ctrl I` | Toggle Sidepanel |
| `Cmd L` / `Ctrl L` | Toggle Sidepanel |
| `Cmd E` / `Ctrl E` | Toggle Agent layout |
| `Cmd .` / `Ctrl .` | Mode Menu |
| `Cmd /` / `Ctrl /` | Loop between AI models |
| `Cmd Shift J` / `Ctrl Shift J` | Cursor settings |
| `Cmd Shift Space` / `Ctrl Shift Space` | Toggle Voice Mode |
| `Cmd ,` / `Ctrl ,` | General settings |
| `Cmd Shift P` / `Ctrl Shift P` | Command palette |

### Chat
| Shortcut | Action |
|---|---|
| `Return` / `Enter` | Nudge (default) |
| `Ctrl Return` / `Ctrl Enter` | Queue message |
| `Cmd Return` / `Ctrl Enter` (typing) | Force send message |
| `Cmd Shift Backspace` / `Ctrl Shift Backspace` | Cancel generation |
| `Tab` | Cycle to next message |
| `Shift Tab` | Rotate between Agent modes |
| `Cmd Opt /` / `Ctrl Alt /` | Model toggle |
| `Cmd N` / `Cmd R` | New chat |
| `Cmd T` | New chat tab |
| `Cmd [` / `Cmd ]` | Previous/Next chat |
| `Cmd W` | Close chat |
| `Esc` | Unfocus field |

### Inline Edit
| Shortcut | Action |
|---|---|
| `Cmd K` / `Ctrl K` | Open |
| `Cmd Shift K` / `Ctrl Shift K` | Toggle input focus |
| `Return` / `Enter` | Submit |
| `Cmd Shift Backspace` / `Ctrl Shift Backspace` | Cancel |
| `Opt Return` / `Alt Enter` | Ask quick question |

### Code Selection & Context
| Shortcut | Action |
|---|---|
| `@` | @-mentions |
| `/` | Shortcut Commands |
| `Cmd Shift L` / `Ctrl Shift L` | Add selection to Chat |
| `Cmd Shift K` / `Ctrl Shift K` | Add selection to Edit |
| `Cmd L` / `Ctrl L` | Add selection to new chat |
| `Cmd M` / `Ctrl M` | Toggle file reading strategies |
| `Cmd ArrowRight` / `Ctrl Arrow Right` | Accept next word of suggestion |
| `Cmd Return` / `Ctrl Enter` | Search codebase in chat |
| `Cmd C` / `Ctrl C`, `Cmd V` / `Ctrl V` | Add copied reference code as context |
| `Cmd C` / `Ctrl C`, `Cmd Shift V` / `Ctrl Shift V` | Add copied code as text context |

### Tab
| Shortcut | Action |
|---|---|
| `Tab` | Accept suggestion |
| `Cmd ArrowRight` / `Ctrl Arrow Right` | Accept next word |

### Terminal
| Shortcut | Action |
|---|---|
| `Cmd K` / `Ctrl K` | Open terminal prompt bar |
| `Cmd Return` / `Ctrl Enter` | Run generated command |
| `Esc` | Accept command |

---

## 🎯 Cursor AI Commands (from design.dev cheatsheet)

### Open Agent / Composer
- **Mac:** `Cmd` + `I`
- **Windows/Linux:** `Ctrl` + `I`
- Toggles AI side panel for agent/multi-file edits

### Open Chat
- **Mac:** `Cmd` + `L`
- **Windows/Linux:** `Ctrl` + `L`
- Toggle AI side panel to ask questions about code

### Inline Edit
- **Mac:** `Cmd` + `K`
- **Windows/Linux:** `Ctrl` + `K`
- Open inline AI editor to generate/modify code in place

### Switch Mode (Agent / Ask / Plan)
- **Mac:** `Cmd` + `.`
- **Windows/Linux:** `Ctrl` + `.`
- Open mode menu to switch AI behavior

### Cycle AI Model
- **Mac:** `Cmd` + `/`
- **Windows/Linux:** `Ctrl` + `/`
- Loop between available AI models

### Add Selection to Chat
- **Mac:** `Cmd` + `Shift` + `L`
- **Windows/Linux:** `Ctrl` + `Shift` + `L`
- Send selected code into current chat as context

### Accept / Reject AI Changes
- **Mac:** `Cmd` + `Enter` (Accept all), `Cmd` + `Delete` (Reject all)
- **Windows/Linux:** `Ctrl` + `Enter` (Accept all), `Ctrl` + `Backspace` (Reject all)

### Accept Tab Suggestion
- **All platforms:** `Tab` (Accept), `Esc` (Dismiss)

### Accept Next Word
- **Mac:** `Cmd` + `→`
- **Windows/Linux:** `Ctrl` + `→`
- Accept just the next word of a Tab suggestion

### Terminal AI Command
- **Mac:** `Cmd` + `K` (Prompt), `Cmd` + `Enter` (Run)
- **Windows/Linux:** `Ctrl` + `K` (Prompt), `Ctrl` + `Enter` (Run)
- In integrated terminal: generate shell command from natural language, then run

---

## ⚡ Workflow Combinations (design.dev)

1. **Targeted edit:** Select code → `Cmd` + `K` → describe change → `Enter` → `Cmd` + `Enter` to accept diff
2. **Ground question in codebase:** `Cmd` + `L` → type `@Codebase` then question → semantic search with citations
3. **Generate terminal command:** Focus terminal → `Cmd` + `K` → describe in plain English → `Cmd` + `Enter` to run

> **All shortcuts are remappable:** `Cmd` + `Shift` + `P` → "Keyboard Shortcuts", or edit `keybindings.json` directly

---

## 📁 Essential Editing (design.dev)

### Cut, Copy, Paste Line (no selection = entire line)
- **Mac:** `Cmd` + `X`/`C`/`V`
- **Windows/Linux:** `Ctrl` + `X`/`C`/`V`

### Duplicate Line
- **Mac:** `Shift` + `Option` + `↑` / `↓`
- **Windows/Linux:** `Shift` + `Alt` + `↑` / `↓`

### Move Line Up/Down
- **Mac:** `Option` + `↑` / `↓`
- **Windows/Linux:** `Alt` + `↑` / `↓`

### Delete Line
- **Mac:** `Cmd` + `Shift` + `K`
- **Windows/Linux:** `Ctrl` + `Shift` + `K`

### Insert Line Below/Above
- **Mac:** `Cmd` + `Enter` (Below), `Cmd` + `Shift` + `Enter` (Above)
- **Windows/Linux:** `Ctrl` + `Enter` (Below), `Ctrl` + `Shift` + `Enter` (Above)

### Comment/Uncomment Line
- **Mac:** `Cmd` + `/`
- **Windows/Linux:** `Ctrl` + `/`

### Block Comment
- **Mac:** `Shift` + `Option` + `A`
- **Windows/Linux:** `Shift` + `Alt` + `A`

### Indent/Outdent
- **Mac:** `Cmd` + `]` / `[`
- **Windows/Linux:** `Ctrl` + `]` / `[`

### Format Document
- **Mac:** `Shift` + `Option` + `F`
- **Windows/Linux:** `Shift` + `Alt` + `F`

### Format Selection
- **Mac:** `Cmd` + `K` then `Cmd` + `F`
- **Windows/Linux:** `Ctrl` + `K` then `Ctrl` + `F`

---

## 🖱️ Multi-Cursor Editing (design.dev)

### Add Cursor Above/Below
- **Mac:** `Cmd` + `Option` + `↑` / `↓`
- **Windows/Linux:** `Ctrl` + `Alt` + `↑` / `↓`

### Add Cursor at Click Position
- **Mac:** `Option` + Click
- **Windows/Linux:** `Alt` + Click

### Select All Occurrences
- **Mac:** `Cmd` + `Shift` + `L`
- **Windows/Linux:** `Ctrl` + `Shift` + `L`

### Select Next Occurrence
- **Mac:** `Cmd` + `D`
- **Windows/Linux:** `Ctrl` + `D`

### Skip Next Occurrence
- **Mac:** `Cmd` + `K` then `Cmd` + `D`
- **Windows/Linux:** `Ctrl` + `K` then `Ctrl` + `D`

### Column (Box) Selection
- **Mac:** `Shift` + `Option` + Drag
- **Windows/Linux:** `Shift` + `Alt` + Drag

---

## 🧭 Navigation (design.dev)

### Go to File
- **Mac:** `Cmd` + `P`
- **Windows/Linux:** `Ctrl` + `P`
- Prefixes: `@` (in file), `#` (workspace), `:` (line), `>` (command palette)

### Go to Symbol in File
- **Mac:** `Cmd` + `Shift` + `O`
- **Windows/Linux:** `Ctrl` + `Shift` + `O`

### Go to Symbol in Workspace
- **Mac:** `Cmd` + `T`
- **Windows/Linux:** `Ctrl` + `T`

### Go to Line
- **All platforms:** `Ctrl` + `G`

### Go to Definition
- **All platforms:** `F12`

### Peek Definition
- **Mac:** `Option` + `F12`
- **Windows/Linux:** `Alt` + `F12`

### Go to References
- **All platforms:** `Shift` + `F12`

### Navigate Back/Forward
- **Mac:** `Ctrl` + `-` (Back), `Ctrl` + `Shift` + `-` (Forward)
- **Windows/Linux:** `Alt` + `←` (Back), `Alt` + `→` (Forward)

### Next/Previous Editor
- **Mac:** `Cmd` + `Option` + `←` / `→`
- **Windows/Linux:** `Ctrl` + `PageUp` / `PageDown`

### Go to Bracket
- **Mac:** `Cmd` + `Shift` + `\\`
- **Windows/Linux:** `Ctrl` + `Shift` + `\\`

---

## 🔍 Search & Replace (design.dev)

### Find in File
- **Mac:** `Cmd` + `F`
- **Windows/Linux:** `Ctrl` + `F`

### Find & Replace in File
- **Mac:** `Opt` + `Cmd` + `F`
- **Windows/Linux:** `Ctrl` + `H`

### Find in Files
- **Mac:** `Cmd` + `Shift` + `F`
- **Windows/Linux:** `Ctrl` + `Shift` + `F`

### Replace in Files
- **Mac:** `Cmd` + `Shift` + `H`
- **Windows/Linux:** `Ctrl` + `Shift` + `H`

### Find Next/Previous
- **Mac:** `Cmd` + `G` (Next), `Cmd` + `Shift` + `G` (Previous)
- **Windows/Linux:** `F3` (Next), `Shift` + `F3` (Previous)

### Select All Find Matches
- **Mac:** `Opt` + `Enter`
- **Windows/Linux:** `Alt` + `Enter`

---

## 📦 Command Palette (design.dev)

### Show Command Palette
- **Mac:** `Cmd` + `Shift` + `P`
- **Windows/Linux:** `Ctrl` + `Shift` + `P`

### Settings
- **Mac:** `Cmd` + `,`
- **Windows/Linux:** `Ctrl` + `,`

### Keyboard Shortcuts
- **Mac:** `Cmd` + `K` then `Cmd` + `S`
- **Windows/Linux:** `Ctrl` + `K` then `Ctrl` + `S`

---

## ⚡ Terminal (design.dev)

### Toggle Terminal
- **All platforms:** `Ctrl` + `` ``

### Create New Terminal
- **All platforms:** `Ctrl` + `Shift` + `` ``

### Focus Terminal
- **Mac:** `Cmd` + `J`
- **Windows/Linux:** `Ctrl` + `J`

### Kill Terminal
- **Mac:** `Cmd` + `W` (in terminal)
- **Windows/Linux:** `Ctrl` + `W` (in terminal)

### Split Terminal
- **Mac:** `Cmd` + `\\` (in terminal)
- **Windows/Linux:** `Ctrl` + `Shift` + `5`

---

## 📐 Display & Layout (design.dev)

### Toggle Sidebar
- **Mac:** `Cmd` + `B`
- **Windows/Linux:** `Ctrl` + `B`

### Toggle Panel
- **Mac:** `Cmd` + `J`
- **Windows/Linux:** `Ctrl` + `J`

### Zen Mode
- **Mac:** `Cmd` + `K` then `Z`
- **Windows/Linux:** `Ctrl` + `K` then `Z`

### Split Editor
- **Mac:** `Cmd` + `\\`
- **Windows/Linux:** `Ctrl` + `\\`

### Focus Editor Group
- **Mac:** `Cmd` + `1` / `2` / `3`
- **Windows/Linux:** `Ctrl` + `1` / `2` / `3`

### Zoom In/Out
- **Mac:** `Cmd` + `=` (In), `Cmd` + `-` (Out)
- **Windows/Linux:** `Ctrl` + `=` (In), `Ctrl` + `-` (Out)

---

## 📂 File Management (design.dev)

### New File
- **Mac:** `Cmd` + `N`
- **Windows/Linux:** `Ctrl` + `N`

### Save File
- **Mac:** `Cmd` + `S`
- **Windows/Linux:** `Ctrl` + `S`

### Close Editor
- **Mac:** `Cmd` + `W`
- **Windows/Linux:** `Ctrl` + `W`

### Reveal in File Explorer
- **Mac:** `Cmd` + `K` then `R`
- **Windows/Linux:** `Ctrl` + `K` then `R`

### Copy Path
- **Mac:** `Cmd` + `K` then `P`
- **Windows/Linux:** `Ctrl` + `K` then `P`

---

## 🛠️ Refactoring (design.dev)

### Rename Symbol
- **All platforms:** `F2`

### Quick Fix
- **Mac:** `Cmd` + `.`
- **Windows/Linux:** `Ctrl` + `.`

### Show Hover
- **Mac:** `Cmd` + `K` then `Cmd` + `I`
- **Windows/Linux:** `Ctrl` + `K` then `Ctrl` + `I`

### Trigger Suggest
- **All platforms:** `Ctrl` + `Space`

### Trigger Parameter Hints
- **Mac:** `Cmd` + `Shift` + `Space`
- **Windows/Linux:** `Ctrl` + `Shift` + `Space`

---

## 🐛 Debugging (design.dev)

### Toggle Breakpoint
- **All platforms:** `F9`

### Start/Continue Debugging
- **All platforms:** `F5`

### Step Over
- **All platforms:** `F10`

### Step Into
- **All platforms:** `F11`

### Step Out
- **All platforms:** `Shift` + `F11`

### Stop Debugging
- **All platforms:** `Shift` + `F5`

### Show Problems
- **Mac:** `Cmd` + `Shift` + `M`
- **Windows/Linux:** `Ctrl` + `Shift` + `M`

---

## 🧩 Emmet Abbreviations (design.dev)

### Expand Abbreviation
- **All platforms:** `Tab`

### Common Patterns
- Child: `> div>ul>li`
- Sibling: `+ div+p+span`
- Climb up: `^ div>ul>li^div`
- Multiply: `* ul>li*3`
- Grouping: `() div>(header>ul>li*2)+footer>p`
- ID & Class: `div#header.container.main`
- Attributes: `a[href="#" title="Link"]`
- Text: `{}`
- Lists: `li{Item $}*3`
- CSS Properties: `m10 → margin: 10px; p20-30 → padding: 20px 30px; w100p → width: 100%`

---

## 💡 Pro Tips (design.dev)

- **Customize shortcuts:** Open Settings → Keyboard Shortcuts → Search for any command
- **Format on Save:** Enable in Settings → "Format on Save"
- **Auto Save:** Settings → Files: Auto Save → "afterDelay"
- **Workspace settings:** Create `.vscode/settings.json` in project root
- **Custom snippets:** `Cmd`/`Ctrl` + `Shift` + `P` → "Configure User Snippets"
- **Cursor AI Tips:** Use `Cmd`+`K` with selected code for targeted inline edits, `Cmd`+`I` to open the agent for multi-file work, and `@-mention` files or `@Codebase` in chat to add context

---

## 📚 Additional Resources (design.dev)

- [VS Code Keyboard Shortcuts Documentation](https://code.visualstudio.com/docs/getstarted/keybindings)
- [Cursor IDE Documentation](https://cursor.com/docs)
- [VS Code Shortcuts PDF (Windows)](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [VS Code Shortcuts PDF (macOS)](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [VS Code Shortcuts PDF (Linux)](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

### Related Tools
- [Cursor Rules Generator](/ai/cursor-rules-generator/)
- [SKILL.md Generator](/ai/skills-generator/)

---

## 📦 GitHub Repository

**knz/cursor-vscode-cheatsheets** — Contains PDF and TeX source for:
- `cursor-cheatsheet.pdf` — Full Cursor cheat sheet (2 pages)
- `cursor-cheatsheet.tex` — Source LaTeX file
- `nav.pdf` / `nav.tex` — Navigation-focused cheat sheet
- `mcx.pdf` / `mcx.tex` — MCX extension for VS Code

[Repository on GitHub](https://github.com/knz/cursor-vscode-cheatsheets)

---

## 🔍 Key Observations

1. **Cross-platform consistency:** Most shortcuts have Mac (`Cmd`) and Windows/Linux (`Ctrl`) variants, with some platform-specific keys
2. **AI-command density:** Cursor has significantly more AI-focused shortcuts than vanilla VS Code (`Cmd`+`K`, `Cmd`+`L`, `Cmd`+`I`, mode switching, accept/reject workflows)
3. **Remappable:** All shortcuts can be customized via Keyboard Shortcuts settings or `keybindings.json`
4. **Command palette as hub:** `Cmd`+`Shift`+`P` is the entry point for discovering all commands
5. **Terminal integration:** Native terminal AI command generation (`Cmd`+`K` in terminal) is a differentiator
6. **Selection-to-context flow:** Multiple shortcuts (`Cmd`+`Shift`+`L`, `Cmd`+`Shift`+`K`, `Cmd`+`L`) for adding code context to chats/edits