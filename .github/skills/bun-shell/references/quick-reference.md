# Bun Shell Scripting Reference

## Common Patterns
```typescript
// Run a command and capture output
const output = await Bun.$`echo hello`
console.log(output.text())

// Pipe commands
const result = await Bun.$`ls -la | wc -l`

// With arguments (safe interpolation)
const arg = "world"
await Bun.$`echo ${arg}`
```

## Key Features
- Cross-platform shell scripting from TypeScript/JavaScript
- Template literal syntax with `Bun.$`
- Automatic pipe handling
- Safe variable interpolation (no shell injection)
