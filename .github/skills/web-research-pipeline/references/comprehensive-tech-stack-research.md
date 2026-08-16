# Comprehensive Tech-Stack Research Format

A structured approach for researching **multi-technology project stacks** — used in the rhixe_scans research (2026-07-16). Use this format when researching a project with 4+ distinct technologies (e.g., framework + database + ORM + payments + deployment).

## When to Use This Format

| Research Type | Format |
|--------------|--------|
| Single topic / question | Minimal template (thematic sections) |
| 2-3 technologies | Partial tech sections in Detailed Analysis |
| 4+ technologies (full-stack project) | **Comprehensive** — one section per tech + cross-cutting |

## Structure Overview

```
1. Research Question         ← Framing
2. Source Map                ← Tracked sources table
3. Key Findings              ← Executive summary
4. Detailed Analysis         ← Per-technology deep dives
   ├── Tech 1: Best Practices / Pitfalls / Performance / Security
   ├── Tech 2: (same structure)
   └── Tech N: (same structure)
5. Cross-Cutting Concerns    ← Architecture / Security / Performance
6. Related Projects          ← Comparison table
7. Tools & Resources         ← Quick-reference table
8. Synthesis                 ← Integration summary
9. Confidence Assessment     ← Source diversity, recency, factual foundation
10. Research Methodology     ← Queries, tools, backends, date
11. Follow-up Questions      ← Gaps for next pass
```

## Per-Technology Section Template

Each technology section follows a consistent four-part structure:

```markdown
## Technology X: {Name}

### Best Practices
- {Pattern 1 with code example or config snippet}
- {Pattern 2 with source attribution}
- {Pattern 3 ...}

### Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| {What can go wrong} | {What happens} | {How to prevent} |
| {...} | {...} | {...} |

### Performance Tips
- {Optimization 1}
- {Optimization 2}

### Security Considerations
- {Security measure 1}
- {Security measure 2}
```

## Cross-Cutting Sections

After per-tech sections, cover concerns that span multiple technologies:

### Architecture Patterns
- Data flow diagrams or descriptions
- Integration points between technologies
- Notable architectural decisions (e.g., "SSE over WebSocket for serverless")

### Security (Platform-Wide)
- Webhook signature verification patterns
- Authentication/authorization strategy
- Input validation boundaries
- Content security (paywalls, signed URLs, download protection)

### Performance Optimization
- Caching strategy (database, CDN, application)
- Image/media optimization
- Deployment optimizations (standalone output, multi-stage builds)
- Real-time communication choices

## Live Example

The rhixe_scans research (`projects/rhixe_scans/web-research-rhixe-scans.md`) is a complete worked example using this format for a Next.js 15 + Prisma 6 + PostgreSQL + Stripe + PayPal + Docker + Tailwind stack. It covers:
- 14 sources across official docs, engineering blogs, and community discussions
- 7 per-technology deep dives
- 4 cross-cutting sections
- Full methodology documentation
