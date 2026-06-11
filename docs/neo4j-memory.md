# 🧠 Neo4j Labs MCP Servers — Comprehensive Summary

> **Repository**: [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)
> **Status**: Actively developed under **Neo4j Labs** — experimental, community-supported, no SLAs or backward compatibility guarantees.

---

## 🔍 Overview

This repository hosts **Model Context Protocol (MCP)** servers developed by the **Neo4j Field GenAI team**. MCP is a standardized protocol enabling LLMs to interact with external systems like databases and cloud services.

These servers allow AI assistants (e.g., **Claude Desktop, VS Code, Cursor, Windsurf, Gemini CLI**) to use **natural language** to interact with **Neo4j** and **Neo4j Aura**.

> 💡 **Note**: For the *official* Neo4j MCP server, visit [github.com/neo4j/mcp](https://github.com/neo4j/mcp).

---

## 🛠️ Available MCP Servers

### 1. `mcp-neo4j-cypher` — Natural Language → Cypher Queries
- **Function**: Translates natural language into Cypher queries.
- **Features**:
  - Retrieves database schema.
  - Executes **read and write** Cypher queries.
- **Requirement**: [APOC plugin](https://neo4j.com/docs/apoc/current/installation/) must be installed and enabled on the Neo4j instance.

### 2. `mcp-neo4j-memory` — Knowledge Graph Memory
- **Function**: Stores and retrieves a **personal knowledge graph** in Neo4j.
- **Use Case**: Persistent memory across sessions, conversations, and clients.
- **Storage**: Local or remote Neo4j instance.

### 3. `mcp-neo4j-cloud-aura-api` — Neo4j Aura Cloud Management
- **Function**: Manage **Neo4j Aura** instances via natural language.
- **Capabilities**:
  - Create/destroy instances.
  - Find instances by name.
  - Scale up/down.
  - Enable features.
- **Access**: Directly from AI assistant chat.

### 4. `mcp-neo4j-data-modeling` — Graph Data Modeling & Visualization
- **Function**: Create, validate, and visualize Neo4j graph data models.
- **Features**:
  - Import/export models from [Arrows.app](https://arrows.app).
  - Interactive modeling workflow.

---

## 🌐 Transport Modes

All servers support multiple transport modes, including:

### HTTP Transport
- **Flag**: `--transport http`
- **Environment variables** also supported.
- Designed for **scalable, production-ready deployments**.

---

## ☁️ Cloud Deployment

- All servers are **containerized**.
- Ready for deployment on:
  - **AWS ECS Fargate**
  - **Azure Container Apps**
- Supports **auto-scaling** and **load balancing**.

📘 **[Complete Cloud Deployment Guide →](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README-Cloud.md)**

---

## 🤝 Contributing

- **Contributions welcome!**
- Submit a **Pull Request**.

---

## 📚 Resources

- **Blog Posts**: Available (not detailed in content).
- **License**: [MIT License](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/LICENSE.txt)
- **Security Policy**: [SECURITY.md](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/SECURITY.md)

---

## 📊 Repository Stats

- **Commits**: 345
- **Releases**: 52
- **Contributors**: Multiple (see [contributors graph](https://github.com/neo4j-contrib/mcp-neo4j/graphs/contributors))

---

## ⚠️ Important Notes

- **Not officially supported** by Neo4j product team.
- **No SLAs or backward compatibility guarantees**.
- Part of **Neo4j Labs** — experimental, frequently updated.

---

## 🔗 Key Links

- [Neo4j Labs](https://neo4j.com/labs/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
- [Neo4j Aura Console](https://console.neo4j.io)
- [APOC Plugin Docs](https://neo4j.com/docs/apoc/current/installation/)
- [Arrows.app](https://arrows.app)

---

> ✅ **Summary**: This repo provides **four experimental MCP servers** enabling AI assistants to interact with Neo4j via natural language — for querying, memory, cloud management, and data modeling. All support HTTP transport and cloud deployment. Community contributions encouraged.
