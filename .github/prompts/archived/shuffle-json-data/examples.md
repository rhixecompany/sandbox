# Examples

> Extracted from `shuffle-json-data.prompt.md`.

## Examples

Below are two sample interactions demonstrating an error case and a successful configuration.

### Missing File

```text
[user]
> /shuffle-json-data
[agent]
> Please provide a JSON file to shuffle. Preferably as chat variable or attached context.
```

### Custom Configuration

```text
[user]
> /shuffle-json-data #file:funFacts.json ignoreProperties = "year", "category"; requiredProperties = "fact"
```
