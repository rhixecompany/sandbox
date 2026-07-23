# Adding POST Operations

> Extracted from `typespec-api-operations.prompt.md`.

## Adding POST Operations

### Simple POST - Create Item

```typescript
/**
 * Create a new item.
 * @param item The item to create
 */
@route("/items")
@post op createItem(@body item: CreateItemRequest): Item;

model CreateItemRequest {
  title: string;
  description?: string;
  userId: integer;
}
```

### POST with Confirmation

```typescript
/**
 * Create a new item with confirmation.
 */
@route("/items")
@post
@capabilities(#{
  confirmation: #{
    type: "AdaptiveCard",
    title: "Create Item",
    body: """
    Are you sure you want to create this item?
      * **Title**: {{ function.parameters.item.title }}
      * **User ID**: {{ function.parameters.item.userId }}
    """
  }
})
op createItem(@body item: CreateItemRequest): Item;
```
