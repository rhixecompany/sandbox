# Node.js Debugging Reference

## Common Commands
```bash
# Start with inspector
node --inspect app.js
node --inspect-brk app.js  # Break on first line

# Connect Chrome DevTools
chrome://inspect

# Debug in terminal
node inspect app.js
```

## Key Features
- Breakpoints, stepping, watch expressions
- Heap snapshots and CPU profiling
- Async stack traces for Promise chains
- Memory leak detection via heap comparison
