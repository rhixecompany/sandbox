---
name: qdrant-vector-search
title: "Qdrant Vector Search"
description: High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast nearest neighbor search, hybrid search with filtering, or scalable vector storage with Rust-powered performance.
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [qdrant-client>=1.12.0]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [RAG, Vector Search, Qdrant, Semantic Search, Embeddings, Similarity Search, HNSW, Production, Distributed]
---

# Qdrant - Vector Similarity Search Engine

High-performance vector database written in Rust for production RAG and semantic search.

## When to use Qdrant
- Building production RAG systems requiring low latency
- Need hybrid search (vectors + metadata filtering)
- Require horizontal scaling with sharding/replication
- Want on-premise deployment with full data control
- Need multi-vector storage per record (dense + sparse)
- Building real-time recommendation systems

**Key features:** Rust-powered, rich filtering, multiple vectors, quantization (scalar/product/binary), distributed (Raft/sharding/replication), REST+gRPC.

**Use alternatives:** Chroma (simpler/embedded), FAISS (max raw speed), Pinecone (fully managed), Weaviate (GraphQL/built-in vectorizers).

## Quick Start

### Install
```bash
pip install qdrant-client
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant  # With storage: -v $(pwd)/qdrant_storage:/qdrant/storage
```

### Basic Usage
```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(host="localhost", port=6333)

client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

client.upsert(collection_name="documents", points=[
    PointStruct(id=1, vector=[0.1, 0.2, ...], payload={"title": "Doc 1", "category": "tech"}),
    PointStruct(id=2, vector=[0.3, 0.4, ...], payload={"title": "Doc 2", "category": "science"})
])

results = client.search(collection_name="documents", query_vector=[0.15, 0.25, ...],
    query_filter={"must": [{"key": "category", "match": {"value": "tech"}}]}, limit=10)

for p in results: print(f"ID: {p.id}, Score: {p.score}, Payload: {p.payload}")
```

## Core Concepts

### Points = ID + Vector(s) + Payload
```python
from qdrant_client.models import PointStruct
point = PointStruct(id=123, vector=[0.1, 0.2, ...],
    payload={"title": "Doc", "category": "tech", "tags": ["python", "ml"]})
client.upsert(collection_name="docs", points=[point1, point2], wait=True)
```

### Collections
```python
from qdrant_client.models import VectorParams, Distance, HnswConfigDiff
client.create_collection(collection_name="documents",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    hnsw_config=HnswConfigDiff(m=16, ef_construct=100, full_scan_threshold=10000),
    on_disk_payload=True)
info = client.get_collection("documents")
print(f"Points: {info.points_count}")
```

### Distance Metrics
| Metric | Use Case | Range |
|--------|----------|-------|
| `COSINE` | Text embeddings | 0 to 2 |
| `EUCLID` | Spatial data | 0 to ∞ |
| `DOT` | Recommendations | -∞ to ∞ |
| `MANHATTAN` | Sparse features | 0 to ∞ |

## Search Operations

### Basic
```python
results = client.search(collection_name="documents", query_vector=[0.1, 0.2, ...],
    limit=10, with_payload=True, with_vectors=False)
```

### Filtered
```python
from qdrant_client.models import Filter, FieldCondition, MatchValue, Range
results = client.search(collection_name="documents", query_vector=query_embedding,
    query_filter=Filter(must=[
        FieldCondition(key="category", match=MatchValue(value="tech")),
        FieldCondition(key="timestamp", range=Range(gte=1699000000))
    ], must_not=[FieldCondition(key="status", match=MatchValue(value="archived"))]),
    limit=10)

# Shorthand
results = client.search(collection_name="documents", query_vector=query_embedding,
    query_filter={"must": [{"key": "category", "match": {"value": "tech"}},
                           {"key": "price", "range": {"gte": 10, "lte": 100}}]},
    limit=10)
```

### Batch Search
```python
from qdrant_client.models import SearchRequest
results = client.search_batch(collection_name="documents",
    requests=[SearchRequest(vector=[0.1, ...], limit=5),
              SearchRequest(vector=[0.2, ...], limit=5, filter={"must": [...]}),
              SearchRequest(vector=[0.3, ...], limit=10)])
```

## RAG Integration

### Sentence-Transformers
```python
from sentence_transformers import SentenceTransformer
encoder = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="localhost", port=6333)
client.create_collection("knowledge_base", vectors_config=VectorParams(size=384, distance=Distance.COSINE))

documents = [{"id": 1, "text": "Python is a programming language", "source": "wiki"}]
points = [PointStruct(id=d["id"], vector=encoder.encode(d["text"]).tolist(),
    payload={"text": d["text"], "source": d["source"]}) for d in documents]
client.upsert("knowledge_base", points=points)

def retrieve(query: str, top_k: int = 5) -> list[dict]:
    qv = encoder.encode(query).tolist()
    results = client.search("knowledge_base", query_vector=qv, limit=top_k)
    return [{"text": r.payload["text"], "score": r.score} for r in results]
```

### LangChain / LlamaIndex
```python
# LangChain
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
vectorstore = Qdrant.from_documents(docs, HuggingFaceEmbeddings(), url="http://localhost:6333", collection_name="docs")
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# LlamaIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
vector_store = QdrantVectorStore(client=client, collection_name="llama_docs")
index = VectorStoreIndex.from_documents(docs, storage_context=StorageContext.from_defaults(vector_store=vector_store))
```

## Advanced Topics (see [references/advanced-usage.md](references/advanced-usage.md))
- **Multi-vector**: Named vectors (dense+sparse), sparse vectors (BM25/SPLADE)
- **Quantization**: Scalar (INT8, ~4x), Product (PQ, ~16x), Binary (~32x)
- **Distributed**: Raft cluster, sharding, replication, consistency levels
- **Hybrid search**: Dense+sparse with RRF fusion, multi-stage retrieval
- **Recommendations**: Item-to-item, lookup from another collection
- **Advanced filtering**: Nested conditions, geo, full-text
- **Snapshots/aliases**: Collection snapshots, blue-green deployment
- **Scroll/iteration**: Paginated iteration through all points

## Production (Qdrant Cloud)
```python
client = QdrantClient(url="https://your-cluster.cloud.qdrant.io", api_key="your-key")
```

## Performance Tuning
```python
client.update_collection("documents", hnsw_config=HnswConfigDiff(ef_construct=200, m=32))
client.update_collection("documents", optimizer_config={"indexing_threshold": 20000})
```

## Best Practices
1. Batch operations (upsert/search)
2. Payload indexing for filter fields
3. Quantization for >1M vectors
4. Sharding for >10M vectors
5. `on_disk_payload=True` for large payloads
6. Connection pooling (reuse client)

## Common Issues
**Slow search with filters:**
```python
client.create_payload_index("docs", "category", PayloadSchemaType.KEYWORD)
```
**OOM:** Enable quantization + `on_disk_payload`
**Connection issues:** Use timeout, retry, `prefer_grpc=True`

## Skills Required
| Skill | Purpose |
|-------|---------|
| `context7` | Current Qdrant client docs |
| `systematic-debugging` | Indexing/query performance issues |

## Pitfalls
- **Immutable config**: Vector config can't change after creation — plan dimensions
- **Detailed topics**: Moved to `references/advanced-usage.md` and `references/troubleshooting.md`

## Verification Checklist
- [ ] Client installed and connected
- [ ] Collection created with correct vector config
- [ ] Payload indexes for filter fields
- [ ] Vectors upserted successfully
- [ ] Search returns expected results
- [ ] Memory usage acceptable

## References
- **[Advanced Usage](references/advanced-usage.md)** — Multi-vector, quantization, distributed, hybrid search, recommendations, advanced filtering, snapshots, aliases, scroll
- **[Troubleshooting](references/troubleshooting.md)** — Slow filter search, OOM, connection issues