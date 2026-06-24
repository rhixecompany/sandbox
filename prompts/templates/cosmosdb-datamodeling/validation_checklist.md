# Validation Checklist

> Extracted from `cosmosdb-datamodeling.prompt.md` for DRY templating.

## Validation Checklist

- [ ] Application domain and scale documented ✅
- [ ] All entities and relationships mapped ✅
- [ ] Aggregate boundaries identified based on access patterns ✅
- [ ] Identifying relationships checked for consolidation opportunities ✅
- [ ] Container consolidation analysis completed ✅
- [ ] Every access pattern has: RPS (avg/peak), latency SLO, consistency level, expected result size, document size band
- [ ] Write pattern exists for every read pattern (and vice versa) unless USER explicitly declines ✅
- [ ] Hot partition risks evaluated ✅
- [ ] Consolidation framework applied; candidates reviewed
- [ ] Design considerations captured (subject to final validation) ✅
```

### Multi-Document vs Separate Containers Decision Framework

When entities have 30-70% access correlation, choose between:

**Multi-Document Container (Same Container, Different Document Types):**

- ✅ Use when: Frequent joint queries, related entities, acceptable operational coupling
- ✅ Benefits: Single query retrieval, reduced latency, cost savings, transactional consistency
- ❌ Drawbacks: Shared throughput, operational coupling, complex indexing

**Separate Containers:**

- ✅ Use when: Independent scaling needs, different operational requirements
- ✅ Benefits: Clean separation, independent throughput, specialized optimization
- ❌ Drawbacks: Cross-partition queries, higher latency, increased cost

**Enhanced Decision Criteria:**

- **>70% correlation + bounded size + related operations** → Multi-Document Container
- **50-70% correlation** → Analyze operational coupling:
  - Same backup/restore needs? → Multi-Document Container
  - Different scaling patterns? → Separate Containers
  - Different consistency requirements? → Separate Containers
- **<50% correlation** → Separate Containers
- **Identifying relationship present** → Strong Multi-Document Container candidate

🔴 CRITICAL: "Stay in this section until you tell me to move on. Keep asking about other requirements. Capture all reads and writes. For example, ask: 'Do you have any other access patterns to discuss? I see we have a user login access pattern but no pattern to create users. Should we add one?

### Final Deliverable: cosmosdb_data_model.md

Creation Trigger: Only after USER confirms all access patterns captured and validated Purpose: Step-by-step reasoned final design with complete justifications

📋 Template for cosmosdb_data_model.md:

````markdown
# Azure Cosmos DB NoSQL Data Model
