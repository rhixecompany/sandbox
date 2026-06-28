# MindStudio Wrapper Reference

## Common Actions
```
mindstudio_run(action='chat', params={'prompt': '...'})
mindstudio_run(action='generate', params={'prompt': '...'})
```

## Key Patterns
- Wraps MindStudio API calls with consistent error handling
- Supports chat, generation, and embedding actions
- Returns structured responses for downstream processing
