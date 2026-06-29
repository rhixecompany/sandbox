# Container Designs

> Extracted from `cosmosdb-datamodeling.prompt.md` for DRY templating.

## Container Designs

🔴 **CRITICAL**: You MUST group indexes with the containers they belong to.

### [ContainerName] Container

A JSON representation showing 5-10 representative documents for the container

```json
[
  {
    "id": "user_123",
    "partitionKey": "user_123",
    "type": "user",
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": "order_456",
    "partitionKey": "user_123",
    "type": "order",
    "userId": "user_123",
    "amount": 99.99
  }
]
```
````

- **Purpose**: [what this container stores and why this design was chosen]
- **Aggregate Boundary**: [what data is grouped together in this container and why]
- **Partition Key**: [field] - [detailed justification including distribution reasoning, whether it's an identifying relationship and if so why]
- **Document Types**: [list document type patterns and their semantics; e.g., `user`, `order`, `payment`]
- **Attributes**: [list all key attributes with data types]
- **Access Patterns Served**: [Pattern #1, #3, #7 - reference the numbered patterns]
- **Throughput Planning**: [RU/s requirements and autoscale strategy]
- **Consistency Level**: [Session/Eventual/Strong - with justification]

### Indexing Strategy

- **Indexing Policy**: [Automatic/Manual - with justification]
- **Included Paths**: [specific paths that need indexing for query performance]
- **Excluded Paths**: [paths excluded to reduce RU consumption and storage]
- **Composite Indexes**: [multi-property indexes for ORDER BY and complex filters]
  ```json
  {
    "compositeIndexes": [
      [
        { "path": "/userId", "order": "ascending" },
        { "path": "/timestamp", "order": "descending" }
      ]
    ]
  }
  ```
- **Access Patterns Served**: [Pattern #2, #5 - specific pattern references]
- **RU Impact**: [expected RU consumption and optimization reasoning]
