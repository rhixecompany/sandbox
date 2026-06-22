# Card Elements

> Extracted from `mcp-create-adaptive-cards.prompt.md`.

## Card Elements

### TextBlock
```json
{
  "type": "TextBlock",
  "text": "Text content",
  "size": "medium",      // small, default, medium, large, extraLarge
  "weight": "bolder",    // lighter, default, bolder
  "color": "attention",  // default, dark, light, accent, good, warning, attention
  "wrap": true
}
```

### FactSet
```json
{
  "type": "FactSet",
  "facts": [
    {
      "title": "Label",
      "value": "Value"
    }
  ]
}
```

### Image
```json
{
  "type": "Image",
  "url": "https://example.com/image.png",
  "size": "medium",  // auto, stretch, small, medium, large
  "style": "default" // default, person
}
```

### Container
```json
{
  "type": "Container",
  "$data": "${items}",  // Iterate over array
  "items": [
    {
      "type": "TextBlock",
      "text": "${name}"
    }
  ]
}
```

### ColumnSet
```json
{
  "type": "ColumnSet",
  "columns": [
    {
      "type": "Column",
      "width": "auto",
      "items": [ ... ]
    },
    {
      "type": "Column",
      "width": "stretch",
      "items": [ ... ]
    }
  ]
}
```

### Actions
```json
{
  "type": "Action.OpenUrl",
  "title": "View Details",
  "url": "https://example.com/item/${id}"
}
```
