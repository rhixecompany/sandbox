# Hermes Project Configuration Guide

**Created**: May 25, 2026  
**Project**: SandBox Hermes Setup  
**Status**: ACTIVE

---

## Overview

This guide documents how to use Hermes Agent within the SandBox project context, including project-level configuration, skills, MCP servers, and workflows.

---

## Quick Start

### Launch Hermes

```bash
# Interactive chat
cd C:\Users\Alexa\Desktop\SandBox
hermes chat

# One-shot query
hermes chat -q "List project files"

# With specific model
hermes chat --model "gpt-4o"
```

### Check Status

```bash
# Verify everything working
hermes doctor

# List MCP servers
hermes mcp list

# View all tools
hermes tools list
```

---

## Project-Level Configuration

### Optional: Create Project Config

To override global settings for this project, create:

**File**: `.hermes/config.yaml` (relative to project root)

```yaml
# Project-specific Hermes configuration
# Overrides ~/AppData/Local/hermes/config.yaml settings

# Model override (optional)
# default_model: "claude-3-5-sonnet"

# Project-specific MCP servers (if needed)
mcp_servers:
  # Add project MCP servers here
  # (global servers still available)

# Project skills (if needed)
bundled_skills:
  - name: "project-specific-skill"
    enabled: true

# Working directory (defaults to current)
# terminal:
#   cwd: "C:/Users/Alexa/Desktop/SandBox"
```

### Use Global Configuration

By default, Hermes uses the global configuration:
- LLM provider: opencode-zen (big-pickle model)
- MCP servers: 7 servers configured
- Skills: 660+ available
- Tools: 250+ tools

No project-level config changes needed unless specific overrides desired.

---

## Available Tools

### Built-in Toolsets (16 Enabled)

All of these are available:

```
✓ web             — Web search & scraping
✓ browser         — Browser automation
✓ terminal        — Shell commands
✓ file            — File operations
✓ code_execution  — Python code
✓ vision          — Image analysis
✓ image_gen       — Image generation
✓ x_search        — X/Twitter search
✓ moa             — Mixture of Agents
✓ tts             — Text-to-speech
✓ skills          — Skill management
✓ todo            — Task planning
✓ memory          — Persistent memory
✓ session_search  — Past sessions
✓ clarify         — Ask clarification
✓ delegation      — Parallel tasks
✓ cronjob         — Scheduled jobs
✓ messaging       — Cross-platform
✓ computer_use    — Screen control
```

### MCP Servers (7 Configured)

```
mcp_filesystem          — File operations
mcp_sequential_thinking — Reasoning analysis
mcp_next_devtools       — Next.js development
mcp_playwright          — Browser automation
mcp_context7            — Documentation lookup
mcp_gh_grep             — GitHub code search
mcp_docker              — Container management
```

**Total Tools Available**: 250+

**Tool Naming Convention**: `mcp_<server>_<function>`

Example: `mcp_filesystem_read_file`

---

## Common Workflows

### 1. Document Exploration

Ask Hermes to explore and understand project structure:

```bash
hermes chat -q "Analyze project structure and list all directories"

hermes chat -q "What files exist in docs/ folder?"

hermes chat -q "Show me all markdown files in the project"
```

### 2. Code Analysis

Use Hermes to analyze code:

```bash
hermes chat -q "Review the content of .hermes.md and summarize"

hermes chat -q "Find all TODO comments in project files"

hermes chat -q "Analyze the implementation plan for completeness"
```

### 3. Git Integration

Work with Git repositories:

```bash
hermes chat -q "What's the git status of this project?"

hermes chat -q "Create a meaningful commit message for these changes"

hermes chat -q "Show recent commits"
```

### 4. Documentation Generation

Create or improve documentation:

```bash
hermes chat -q "Generate a README for this project"

hermes chat -q "Create a quickstart guide"

hermes chat -q "Document all available commands"
```

### 5. Development Tasks

Execute coding tasks:

```bash
hermes chat -q "Create a new Python script that..."

hermes chat -q "Fix the syntax error in this file"

hermes chat -q "Refactor this code for better performance"
```

### 6. Research & Analysis

Gather information:

```bash
hermes chat -q "Search for best practices for MCP servers"

hermes chat -q "Find information about Hermes configuration"

hermes chat -q "Look up Docker command documentation"
```

---

## Skills System

### Browse Available Skills

```bash
# List all installed skills
hermes skills list

# Search for a skill
hermes skills add nous/dev/    # Shows available dev skills

# Install a skill
hermes skills add code-review

# Reset to bundled skills
hermes skills reset
```

### Useful Skills for Development

| Skill | Purpose |
|-------|---------|
| `code-review` | Code review assistance |
| `documentation` | Doc generation |
| `git-helper` | Git workflows |
| `debugging` | Error troubleshooting |
| `test-creation` | Unit test generation |

### Use Skills in Chat

Skills are available as context for the agent:

```bash
hermes chat -q "Review this code change" -s code-review

hermes chat -q "Generate documentation" -s documentation
```

---

## Memory System

### How Memory Works

Hermes maintains persistent memory across sessions:

**Global Memory**: `~/AppData/Local/hermes/memories/`
- MEMORY.md — Agent's knowledge about environment & preferences
- USER.md — User profile information

**Session-Specific**: `~/AppData/Local/hermes/sessions/`
- All past conversations preserved
- Searchable with `session_search` tool
- Auto-learning from interactions

### Search Past Sessions

```bash
# Find past discussions about MCP
hermes chat -q "What was I working on regarding MCP configuration?"

# Recall specific task
/session_search "configuration plan"

# Or from chat
"What did we do with the documentation last week?"
```

### Update Memory

Memory is updated automatically, but you can edit directly:

```bash
# View memory
cat ~/AppData/Local/hermes/memories/MEMORY.md

# Edit memory (add notes about project)
# Edit ~/AppData/Local/hermes/memories/MEMORY.md
```

---

## Scheduling Jobs

### Create Scheduled Tasks

```bash
# List scheduled jobs
hermes cron list

# Create a new job
hermes cron add

# Remove a job
hermes cron remove <name>

# Run a job manually
hermes cron run <name>
```

### Example: Daily Briefing

Schedule a daily project status check:

```bash
# Create cron job
hermes cron add \
  --name "daily-project-check" \
  --schedule "0 9 * * MON-FRI" \
  --prompt "Generate a status report for SandBox project"
```

---

## Configuration Files Reference

### Global Configuration

**Location**: `~/AppData/Local/hermes/config.yaml`  
**Edits**: Use `hermes config set` or `hermes config edit`

Key sections:
- `model` — LLM provider/model
- `mcp_servers` — External tool servers
- `terminal` — Shell execution settings
- `web` — Web search backend
- `browser` — Browser automation settings
- `agent` — Agent behavior tuning

### Project Configuration (Optional)

**Location**: `.hermes/config.yaml`  
**Edits**: Direct file editing

Override any global settings for project scope.

### Environment Variables

**Location**: `~/AppData/Local/hermes/.env`  
**Contains**: API keys (NOT in git)

Required:
- LLM API keys (OPENROUTER_API_KEY, etc.)
- Service credentials (GitHub, Docker, etc.)

---

## Troubleshooting

### Issue: Tool not found

**Solution**: Check if tool is available

```bash
hermes tools list | grep <tool_name>
```

If missing, enable in config or install skill:

```bash
hermes config set toolsets cli "[tool1, tool2...]"
hermes skills add <missing_skill>
```

### Issue: MCP server not responding

**Solution**: Verify server is running

```bash
hermes mcp list                      # Check status
hermes doctor                        # Diagnostics
```

Reconnect:

```bash
hermes mcp remove <server>           # Remove
hermes mcp add <server>              # Re-add
```

### Issue: Chat timeout

**Solution**: Increase timeout in config

```bash
hermes config set agent.gateway_timeout 5000   # 5 seconds
```

Or increase max turns:

```bash
hermes config set agent.max_turns 120
```

### Issue: Memory not persisting

**Solution**: Check memory configuration

```bash
ls ~/AppData/Local/hermes/memories/               # Check files exist
cat ~/AppData/Local/hermes/memories/MEMORY.md     # Verify content
```

Enable memory:

```bash
hermes config set memory.enabled true
```

### Issue: Skills not installing

**Solution**: Clear cache and retry

```bash
hermes skills cache clean
hermes skills add <skill_name>
```

---

## Best Practices

### 1. Use Meaningful Prompts

✅ **Good**: "Analyze the implementation plan and identify missing steps"  
❌ **Bad**: "What do you think?"

### 2. Break Complex Tasks into Steps

```bash
# Instead of one massive query:
hermes chat -q "Step 1: Read the plan. Step 2: Find gaps. Step 3: Report."
```

### 3. Leverage Session History

```bash
# Let Hermes remember past context
hermes chat -q "Continue working on the configuration from where we left off"
```

### 4. Use Project-Specific Context

```bash
# Reference project files
hermes chat -q "Based on .hermes.md, what's next?"
```

### 5. Combine Tools Effectively

```bash
# Use multiple toolsets
hermes chat -q "Search for docs, read files, and generate summary" \
  --toolsets web,file,code_execution
```

### 6. Review Output Before Acting

```bash
# One-shot final answer
hermes -z "Generate a critical command" 

# Then verify before executing
```

---

## Performance Tips

### 1. Use Fallback Models

If primary model is slow/unavailable, fallback activates:

```yaml
fallback_providers:
  - provider: openrouter
    model: meta-llama/llama-3.3-70b:free
```

### 2. Enable Context Compression

For long conversations (already enabled):

```bash
hermes config get compression.enabled
# true (already optimized)
```

### 3. Set Reasonable Timeouts

For slow networks:

```bash
hermes config set terminal.timeout 600     # 10 minutes
hermes config set agent.gateway_timeout 5000  # 5 seconds
```

### 4. Use Tool Filtering

Disable unused tools:

```bash
hermes config set agent.disabled_toolsets "homeassistant,spotify"
```

---

## Integration with Other Tools

### Git Workflow

```bash
# Check git status before changes
hermes chat -q "Show git status and suggest next steps"

# Generate commit message
hermes chat -q "Based on changes, create a meaningful commit message"
```

### Docker Workflow

```bash
# Inspect Docker setup
hermes chat -q "List running containers and their status"

# Run Docker commands
hermes chat -q "Create a Dockerfile for Python 3.11"
```

### Browser Automation

```bash
# Automated testing
hermes chat -q "Navigate to site and verify page loads"

# Web scraping
hermes chat -q "Scrape and save data from URL"
```

---

## Links to Documentation

| Document | Purpose |
|----------|---------|
| [06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md](06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md) | Complete Hermes reference |
| [07-MCP_SECURITY_BEST_PRACTICES.md](07-MCP_SECURITY_BEST_PRACTICES.md) | Security hardening guide |
| [HERMES_CONFIGURATION_STATUS.md](HERMES_CONFIGURATION_STATUS.md) | Current system status |
| [hermes-configuration-plan.md](hermes-configuration-plan.md) | Implementation plan |
| [hermes-configuration-spec.md](hermes-configuration-spec.md) | Requirements specification |

---

## Advanced Topics

### Custom MCP Servers

To add custom MCP servers:

1. Create/install MCP server
2. Add to `.hermes/config.yaml`:

```yaml
mcp_servers:
  my-custom:
    command: "npx"
    args: ["my-custom-mcp"]
    enabled: true
```

3. Restart Hermes
4. Tools available as `mcp_my_custom_*`

### Custom Skills

To write custom skills:

1. Create `SKILL.md` in `~/AppData/Local/hermes/skills/` or `./skills/`
2. Define name, description, triggers
3. Add implementation steps
4. Use with `/skill-name` in chat

### Profiles

Use multiple Hermes profiles for different projects:

```bash
# Create profile
hermes profile create myproject

# Use profile
hermes chat --profile myproject

# Switch default
hermes profile switch myproject
```

---

## Support & Resources

### Quick Help

```bash
hermes help                    # General help
hermes <command> --help        # Command-specific help
hermes doctor                  # Diagnostics
```

### Documentation

- Official: https://hermes-agent.nousresearch.com/docs
- GitHub: https://github.com/NousResearch/hermes-agent
- Community: https://reddit.com/r/hermesagent

### Debugging

```bash
hermes dump                    # Setup summary for support
hermes debug                   # Upload logs
hermes logs                    # View log files
```

---

**Document Version**: 1.0  
**Created**: May 25, 2026  
**Status**: Active  
**Author**: Alexa
