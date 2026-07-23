# Function Capabilities

> Extracted from `typespec-create-api-plugin.prompt.md`.

## Function Capabilities

### Confirmation Dialog

```typescript
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Confirm Action",
    body: """
    Are you sure you want to perform this action?
      * **Parameter**: {{ function.parameters.paramName }}
    """
  }
})
```

### Adaptive Card Response

```typescript
@card(#{
  dataPath: "$.items",
  title: "$.title",
  url: "$.link",
  file: "cards/card.json"
})
```

### Reasoning & Response Instructions

```typescript
@reasoning("""
  Consider user's context when calling this operation.
  Prioritize recent items over older ones.
""")
@responding("""
  Present results in a clear table format with columns: ID, Title, Status.
  Include a summary count at the end.
""")
```
