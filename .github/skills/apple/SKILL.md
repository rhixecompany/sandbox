---
name: apple
title: "Apple Ecosystem Integration"
description: "Manage Apple Notes, Reminders, Find My, and iMessage from the terminal via macOS CLI wrappers (memo, remindctl, imsg, AppleScript)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [Apple, macOS, Notes, Reminders, iMessage, FindMy, automation]
---

# Apple Ecosystem Integration

Class-level skill for driving native Apple apps from the terminal on **macOS**. Each
section covers one app. The apps share an iCloud-sync model: data created here shows
up on the user's iPhone/iPad/Mac.

| App | CLI / method | Purpose |
|-----|--------------|---------|
| Notes | `memo` | Create / search / edit Apple Notes |
| Reminders | `remindctl` | Add / list / complete Apple Reminders |
| Find My | AppleScript + screenshot | Track devices / AirTags |
| iMessage | `imsg` | Send / read iMessage & SMS |

## Prerequisites (all)
- **macOS** with the relevant Apple app and iCloud signed in.
- Grant the requested privacy permissions when prompted (System Settings → Privacy).

---

## 1. Apple Notes (`memo`)

Install: `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo`
Grant Automation access to Notes.app.

### When to use
- Create / view / search Apple Notes, folders, export to Markdown/HTML.
- Cross-device note sync (iPhone/iPad/Mac).
- **Not** for: Obsidian vaults (use `obsidian`), Bear (unsupported), or agent-only
  scratch notes (use the `memory` tool).

### Quick reference
```bash
memo notes                        # List all notes
memo notes -f "Folder Name"       # Filter by folder
memo notes -s "query"             # Fuzzy search
memo notes -a "Note Title"        # Quick add
memo notes -e                     # Interactive edit
memo notes -d                     # Interactive delete
memo notes -m                     # Move to folder
memo notes -ex                    # Export HTML/Markdown
```
Limitations: cannot edit notes with images/attachments; interactive prompts need a PTY.

---

## 2. Apple Reminders (`remindctl`)

Install: `brew install steipete/tap/remindctl`. Check `remindctl status` / authorize with `remindctl authorize`.

### When to use
- "reminder" / "Reminders app" requests, to-dos with due dates that sync to iOS.
- **Not** for: agent alert scheduling (use a cronjob), calendar events, or project
  task management (GitHub Issues / Notion).

### Quick reference
```bash
remindctl today | tomorrow | week | overdue | all
remindctl list Work --create           # Create list
remindctl add "Buy milk"
remindctl add --title "Call mom" --list Personal --due tomorrow
remindctl add --title "Meeting" --due "2026-02-15 09:00" --alarm "2026-02-15 08:30"
remindctl edit 87354 --due "2026-05-15 14:00"
remindctl complete 1 2 3             # Complete by ID
remindctl delete 4A83 --force
remindctl today --json                 # Machine-readable
```
`-due` sets the due time; `--alarm` sets the notification/nudge trigger. Verify with
`--json` (fields `dueDate` vs `alarmDate`). Date formats: `today`, `YYYY-MM-DD`,
`YYYY-MM-DD HH:mm`, ISO-8601.

---

## 3. Find My (AppleScript + screenshot)

No CLI/API exists for Find My — use UI automation. Optional: `brew install steipete/tap/peekaboo`
for more reliable UI control. Requires Screen Recording permission.

### When to use
- "where is my [device/cat/keys/bag]?", tracking AirTags, monitoring pet/item movement.

```bash
# Open and capture
osascript -e 'tell application "FindMy" to activate'
sleep 3
screencapture -w -o /tmp/findmy.png
# Then read with vision_analyze(image_url="/tmp/findmy.png", question="...")
```
Switch tabs via System Events (`click button "Devices"/"Items" of toolbar 1 of window 1`).
For ongoing AirTag tracking, keep FindMy foreground and use a cronjob to capture periodically.
Respect privacy — only track devices/items the user owns.

---

## 4. iMessage (`imsg`)

Install: `brew install steipete/tap/imsg`. Grant Full Disk Access + Automation for Messages.app.

### When to use
- Send / read iMessage or SMS via Messages.app.
- **Not** for Telegram/Discord/Slack/WhatsApp (use the appropriate gateway) or bulk messaging.

```bash
imsg chats --limit 10 --json
imsg history --chat-id 1 --limit 20 --attachments --json
imsg send --to "+14155551212" --text "Hello!"
imsg send --to "+14155551212" --text "Check this out" --file /path/to/image.jpg
imsg send --to "+14155551212" --text "Hi" --service imessage   # or: sms | auto
imsg watch --chat-id 1 --attachments
```
Rules: always confirm recipient + content before sending; never message unknown numbers
without approval; verify file paths; avoid spam (rate-limit yourself).

---

## Cross-cutting rules
1. Prefer Apple apps when the user wants iCloud cross-device sync.
2. Use the `memory` tool for agent-internal notes that don't need to sync.
3. Use `obsidian` for Markdown-native knowledge management.
4. For agent alerts/scheduling, use the cronjob tool, not Reminders.
