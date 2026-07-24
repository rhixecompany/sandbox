# Unacceptable JSON (Default State)

> Extracted from `shuffle-json-data.prompt.md`.

## Unacceptable JSON (Default State)

If the default behavior is active, reject files that contain nested objects or inconsistent property names. For example:

```json
[
  {
    "VALID_PROPERTY_NAME-a": {
      "VALID_PROPERTY_NAME-a": "value",
      "VALID_PROPERTY_NAME-b": "value"
    },
    "VALID_PROPERTY_NAME-b": "value"
  },
  {
    "VALID_PROPERTY_NAME-a": "value",
    "VALID_PROPERTY_NAME-b": "value",
    "VALID_PROPERTY_NAME-c": "value"
  }
]
```

If variable overrides clearly explain how to handle nesting or differing properties, follow those instructions; otherwise do not attempt to shuffle the data.
