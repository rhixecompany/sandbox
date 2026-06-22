# Phase 5: Optimization Recommendations

> Extracted from `dataverse-python-usecase-builder.prompt.md`.

## Phase 5: Optimization Recommendations

### For High-Volume Operations

```python
# Use batch operations
ids = client.create("table", [record1, record2, record3])  # Batch
ids = client.create("table", [record] * 1000)  # Bulk with optimization
```

### For Complex Queries

```python
# Optimize with select, filter, orderby
for page in client.get(
    "table",
    filter="status eq 1",
    select=["id", "name", "amount"],
    orderby="name",
    top=500
):
    # Process page
```

### For Large Data Transfers

```python
# Use chunking for files
client.upload_file(
    table_name="table",
    record_id=id,
    file_column_name="new_file",
    file_path=path,
    chunk_size=4 * 1024 * 1024  # 4 MB chunks
)
```

# Use Case Categories
