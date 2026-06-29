# Adaptive Card Template Language

> Extracted from `mcp-create-adaptive-cards.prompt.md`.

## Adaptive Card Template Language

### Conditional Rendering
```json
{
  "type": "TextBlock",
  "text": "${if(field, field, 'N/A')}"  // Show field or 'N/A'
}
```

### Number Formatting
```json
{
  "type": "TextBlock",
  "text": "${formatNumber(amount, 2)}"  // Two decimal places
}
```

### Data Binding
```json
{
  "type": "Container",
  "$data": "${$root}",  // Break to root context
  "items": [ ... ]
}
```

### Conditional Display
```json
{
  "type": "Image",
  "url": "${imageUrl}",
  "$when": "${imageUrl != null}"  // Only show if imageUrl exists
}
```
