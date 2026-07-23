# Phase 3: Pattern Selection

> Extracted from `dataverse-python-usecase-builder.prompt.md`.

## Phase 3: Pattern Selection

Choose appropriate patterns based on use case:

### Pattern 1: Transactional (CRUD Operations)

- Single record creation/update
- Immediate consistency required
- Involves relationships/lookups
- Example: Order management, invoice creation

### Pattern 2: Batch Processing

- Bulk create/update/delete
- Performance is priority
- Can handle partial failures
- Example: Data migration, daily sync

### Pattern 3: Query & Analytics

- Complex filtering and aggregation
- Result set pagination
- Performance-optimized queries
- Example: Reporting, dashboards

### Pattern 4: File Management

- Upload/store documents
- Chunked transfers for large files
- Audit trail required
- Example: Contract management, media library

### Pattern 5: Scheduled Jobs

- Recurring operations (daily, weekly, monthly)
- External data synchronization
- Error recovery and resumption
- Example: Nightly syncs, cleanup tasks

### Pattern 6: Real-time Integration

- Event-driven processing
- Low latency requirements
- Status tracking
- Example: Order processing, approval workflows
