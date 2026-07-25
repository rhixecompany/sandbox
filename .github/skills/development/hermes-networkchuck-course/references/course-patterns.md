# Hermes NetworkChuck Course Patterns

## Course Structure

| Module | Topic | Skills Gained |
|--------|-------|---------------|
| 1 | Introduction to Hermes | Install, configure, first run |
| 2 | Memory System | SOUL.md, MEMORY.md, USER.md |
| 3 | Skills | Create, install, trigger skills |
| 4 | Automation | Cron jobs, hooks, MCP servers |
| 5 | Advanced | Multi-agent, delegation, profiles |

## Practice Exercises

### Exercise 1: Basic Setup
```bash
# Install Hermes
hermes --version

# Configure provider
hermes config set provider openrouter
hermes config set model qwen/qwen3-coder:free

# Test
hermes "Hello, what can you do?"
```

### Exercise 2: Memory
```bash
# View memory
/memory view

# Add fact
/memory add "User prefers Python over JavaScript"
```

### Exercise 3: Skills
```bash
# List skills
/skills

# Load skill
/skill load systematic-debugging

# Create skill
/skill create my-skill
```

### Exercise 4: Cron
```bash
# Create daily briefing
/cron create "Daily briefing" "0 9 * * *" "Summarize today's tasks"

# List cron jobs
/cron list
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Provider not found | `hermes auth login <provider>` |
| Skill not loading | Check SKILL.md frontmatter |
| Memory not persisting | Check char limits (USER: 1375, MEMORY: 2200) |
| TUI not launching | Check terminal compatibility |