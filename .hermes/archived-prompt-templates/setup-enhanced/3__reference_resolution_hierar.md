# 3. 📚 Reference Resolution Hierarchy

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 3. 📚 Reference Resolution Hierarchy

When implementing features, consult these sources in priority order:

### Tier 1 — Latest Standards (Primary)

| Source | Purpose |
| --- | --- |
| `.github/copilot-instructions.md` | Current architectural standards and coding rules |
| `.github/instructions/*.md` | File-pattern-specific guidelines (TypeScript, Next.js, security, testing, performance) |

### Tier 2 — Entity & Schema Details

| Source | Purpose |
| --- | --- |
| `docs/database-context-map.md` | Entity relationships, constraints, cascade behavior |
| `src/database/schema.ts` | Table definitions, enums, indexes (30+ tables) |

### Tier 3 — Concrete Implementations

| Source | Purpose |
| --- | --- |
| `src/dal/*.ts` | Data Access Layer patterns (`BaseDal<T>`, eager loading) |
| `src/actions/*.ts` | Server Actions with `ActionResult<T>` pattern |
| `src/schemas/*.ts` | Zod validation schemas per domain |
| `src/components/**/*.tsx` | UI components with proper typing |
| `src/app/**/*.tsx` | Page implementations and route structure |

### Context Resolution Rules

1. **Primary Source:** Use patterns from `.github/copilot-instructions.md` (latest approved patterns)
2. **Validation:** Cross-reference with `docs/database-context-map.md` for entity details
3. **Examples:** Find matching patterns in `src/` for concrete implementation
4. **Configuration:** Reference `docs/*` for project-specific settings and conventions
5. **Conflict:** `.github/copilot-instructions.md` is always the source of truth

### DRY Composition Rules

1. **Reuse DAL Patterns** — Extend `BaseDal<T>` from `src/dal/base-dal.ts`, never create new base classes
2. **Common Actions** — Leverage existing `ActionResult<T>` pattern from `src/actions/types.ts`
3. **Schema Validation** — Use established Zod patterns from `src/schemas/` directory
4. **Component Composition** — Build from existing `ui/` components and shadcn primitives
5. **Type Safety** — Extract types with `z.infer<typeof schema>`, never duplicate type definitions

### Merge Strategy

```
❌ WRONG: Duplicating DAL logic in a new class
✅ CORRECT: class NewDal extends BaseDal<T> { /* only new logic */ }
```

When existing code matches your need:

- **Exact Match** → Use as-is, adjust imports
- **Partial Match** → Extract pattern core, adapt schema/types for new entity
- **No Match** → Create new implementation following adjacent code patterns
- **Conflict** → `.github/copilot-instructions.md` wins

### File Reference Lookup

| Need | Search Location | Reference Example |
| --- | --- | --- |
| DAL Pattern | `src/dal/*.ts` | `comic-dal.ts` for eager loading |
| Server Action | `src/actions/*.ts` | `comic.actions.ts` for `ActionResult<T>` |
| Zod Schema | `src/schemas/*.ts` | `comic-schema.ts` for validation |
| UI Component | `src/components/` | Extend from shadcn primitives |
| Page Layout | `src/app/(root)/` | Mirror existing page structure |
| Type Definition | `src/types/` | Use `z.infer<typeof schema>` |

---
