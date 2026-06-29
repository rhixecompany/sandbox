# Proposed Implementation

> Extracted from `debugger.prompt.md`.

## Proposed Implementation

### Database Schema

[Show table structure with relationships]

### DAL Methods

[List all CRUD + custom methods]

### Zod Schemas

[Show Create and Update schemas]

### Server Actions

[List all actions to implement]

### React Components

[List UI components needed]
```

### Step 4: Get Approval

```
Wait for user to say "I approve the code so implement the code"
```

### Step 5: Implement Everything

- Add schema to `src/database/schema.ts`
- Create DAL class in `src/dal/`
- Create Zod schemas in `src/schemas/`
- Create server actions in `src/actions/`
- Create React components in `src/components/`
- Create page in `src/app/(root)/`

### Step 6: Validate & Test

```bash
pnpm run type-check
pnpm run lint:fix
pnpm test
pnpm run build
```

---
