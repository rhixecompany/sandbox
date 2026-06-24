# Development Workflow & Quality Gates

> Extracted from `plan-dev.prompt.md`.

## Development Workflow & Quality Gates

### Before Each Feature Implementation

1. **Create Zod Schema** (validation)

   ```typescript
   // src/schemas/feature-schema.ts
   export const createSchema = z.object({
     field1: z.string().min(1),
     field2: z.number()
   });
   export type CreateInput = z.infer<typeof createSchema>;
   ```

2. **Create DAL Class** (if new entity)

   ```typescript
   // src/dal/feature-dal.ts
   export class FeatureDal extends BaseDal<FeatureType> {
     async create(data: CreateInput) {
       /* ... */
     }
   }
   ```

3. **Create Server Actions** (mutations)

   ```typescript
   // src/actions/feature-actions.ts
   "use server";
   export async function createFeatureAction(input: unknown) {
     const parsed = schema.safeParse(input);
     if (!parsed.success) return { ok: false, error: "..." };
     try {
       const result = await featureDal.create(parsed.data);
       revalidatePath("/feature");
       return { ok: true, data: result };
     } catch (error) {
       return { ok: false, error: "Failed to create" };
     }
   }
   ```

4. **Create UI Components** (server + client)

   ```typescript
   // src/components/feature-list.tsx (Server Component)
   async function FeatureList() {
     const items = await featureDal.list();
     return <FeatureListClient items={items} />;
   }

   // src/components/feature-list-client.tsx ('use client')
   export function FeatureListClient({ items }) {
     return <div>{items.map(...)}</div>;
   }
   ```

5. **Add Tests** (unit + component)
   ```typescript
   // src/tests/feature.spec.ts
   describe("Feature", () => {
     it("validates correctly", () => {
       /* ... */
     });
   });
   ```

### Quality Gate Checklist (Before Each Commit)

```bash
# Type safety
pnpm type-check          # Must: 0 errors

# Code quality
pnpm lint:fix            # Must: auto-fix all issues
pnpm format              # Auto-format code

# Testing
pnpm test                # Must: all tests pass
                         # Goal: 80%+ coverage

# Build validation
pnpm build --debug-prerender  # Must: succeeds

# Performance checks
pnpm analyze             # Verify bundle size
```

### Token Management Strategy

To avoid rate limiting:

1. **Work in focused batches** - Group 3-4 related edits per batch
2. **Use efficient prompts** - Be specific about what you need
3. **Cache context** - Reference files once, reuse knowledge
4. **Complete features** - Finish one feature before moving to next
5. **Batch fixes** - Group similar fixes together
6. **Monitor token usage** - Check copilot status periodically

---
