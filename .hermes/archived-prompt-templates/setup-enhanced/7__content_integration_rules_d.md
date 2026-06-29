# 7. 🔗 Content Integration Rules (DRY Enforcement)

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 7. 🔗 Content Integration Rules (DRY Enforcement)

### When Adding Documentation

- ✅ Link to relevant sections in existing docs rather than duplicating content
- ✅ Reference specific code in `src/` with file paths
- ✅ Add new patterns to `.github/instructions/` only if they don't already exist
- ✅ Update `docs/database-context-map.md` when schema changes

### When Finding Reference Code

- ✅ Copy implementation **patterns**, not full files — adapt for your entity
- ✅ Always extend `BaseDal<T>` rather than creating a new base class
- ✅ Use same `ActionResult<T>` structure for all server actions
- ✅ Import types: `type CreateInput = z.infer<typeof CreateSchema>`

### When Writing New Code

- ✅ If similar code exists elsewhere, ask why — it might be a DRY violation
- ✅ Extract common logic to utilities/DAL/actions before shipping
- ✅ Use file paths in comments to reference context when helpful
- ✅ Document in `docs/` why a new pattern was created if it diverges from existing ones

### Time-Saving Tips

1. **Copy-Paste Strategy:** Copying existing code is faster than reading docs when you need an exact pattern match — just adapt entity names and imports
2. **Two-Document Reading:** Read `.github/copilot-instructions.md` (WHY) alongside `src/` code (HOW)
3. **Grep for Patterns:**
   ```bash
   grep -r "ActionResult" src/actions/        # Find all actions
   grep -r "extends BaseDal" src/dal/         # Find all DAL classes
   grep -r "safeParse" src/actions/           # Find validation usage
   ```

---
