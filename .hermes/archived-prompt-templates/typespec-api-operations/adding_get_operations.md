# Adding GET Operations

> Extracted from `typespec-api-operations.prompt.md`.

## Adding GET Operations

### Simple GET - List All Items

```typescript
/**
 * List all items.
 */
@route("/items")
@get op listItems(): Item[];
```

### GET with Query Parameter - Filter Results

```typescript
/**
 * List items filtered by criteria.
 * @param userId Optional user ID to filter items
 */
@route("/items")
@get op listItems(@query userId?: integer): Item[];
```

### GET with Path Parameter - Get Single Item

```typescript
/**
 * Get a specific item by ID.
 * @param id The ID of the item to retrieve
 */
@route("/items/{id}")
@get op getItem(@path id: integer): Item;
```

### GET with Adaptive Card

```typescript
/**
 * List items with adaptive card visualization.
 */
@route("/items")
@card(#{
  dataPath: "$",
  title: "$.title",
  file: "item-card.json"
})
@get op listItems(): Item[];
```

**Create the Adaptive Card** (`appPackage/item-card.json`):

```json
{
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View Details",
      "url": "https://example.com/items/${id}"
    }
  ],
  "body": [
    {
      "type": "Container",
      "$data": "${$root}",
      "items": [
        {
          "type": "TextBlock",
          "text": "**${if(title, title, 'N/A')}**",
          "wrap": true
        },
        {
          "type": "TextBlock",
          "text": "${if(description, description, 'N/A')}",
          "wrap": true
        }
      ]
    }
  ],
  "type": "AdaptiveCard",
  "version": "1.5"
}
```
