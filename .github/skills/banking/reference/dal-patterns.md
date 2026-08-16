---
name: dal-patterns
description: "# DAL Patterns Reference"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# DAL Patterns Reference
     2|
     3|## Overview
     4|
     5|Data Access Layer (DAL) in `dal/*.dal.ts` provides typed, reusable database queries with N+1 prevention built-in.
     6|
     7|## When to Use Each Pattern
     8|
     9|| Scenario | Pattern | Example | N+1 Risk |
    10|| --- | --- | --- | --- |
    11|| Single record lookup | Direct query | `findById(id)` | No |
    12|| Multiple records with relations | Batch-fetch | `findByUserIdWithWallets(userId)` | High (prevent with batching) |
    13|| Count/statistics | Aggregation | `countByUserId(userId)` | No |
    14|| Search with JOINs | JOIN query | `findByRecipientName(pattern)` | Depends on implementation |
    15|
    16|## Before You Write a DAL Function, Ask Yourself
    17|
    18|1. **Will I fetch related data?**
    19|   - If yes → Use batch-fetching pattern to prevent N+1
    20|   - If no → Direct single-query is fine
    21|
    22|2. **How many database round-trips will this create?**
    23|   - 1 = optimal
    24|   - 2+ = candidate for optimization
    25|   - If looping and querying for each result = **STOP, this is N+1**
    26|
    27|3. **Could this data have been soft-deleted?**
    28|   - If yes → Include `deletedAt IS NULL` filtering in WHERE clause
    29|   - Check existing findByX functions to follow soft-delete pattern
    30|
    31|4. **Which DAL pattern applies to this query?**
    32|   - Single record → `findById()` or `findByEmail()`
    33|   - Multiple records with relations → `findByXWithY()` using batch-fetch pattern
    34|   - Aggregation/counts → `countByX()`
    35|
    36|## Anti-Patterns: NEVER Do These
    37|
    38|**NEVER #1: Loop-and-query (the N+1 problem)**
    39|
    40|❌ WRONG:
    41|
    42|```typescript
    43|const userIds = [user1, user2, user3];
    44|for (const userId of userIds) {
    45|  const user = await db
    46|    .select()
    47|    .from(users)
    48|    .where(eq(users.id, userId));
    49|  // This creates 3 queries instead of 1
    50|}
    51|```
    52|
    53|✅ RIGHT:
    54|
    55|```typescript
    56|const userIds = [user1, user2, user3];
    57|const users = await db
    58|  .select()
    59|  .from(users)
    60|  .where(inArray(users.id, userIds));
    61|// One query, all data
    62|```
    63|
    64|**WHY**: Each loop iteration triggers a database round-trip. With 100 users, you get 100+ queries instead of 1.
    65|
    66|---
    67|
    68|**NEVER #2: Use raw `db` import directly in components or Server Actions**
    69|
    70|❌ WRONG:
    71|
    72|```typescript
    73|// app/dashboard/page.tsx
    74|import { db } from "@/database/db";
    75|
    76|export default async function Dashboard() {
    77|  const transactions = await db.select().from(transactionsTable);
    78|  return <TransactionList txns={transactions} />;
    79|}
    80|```
    81|
    82|✅ RIGHT:
    83|
    84|```typescript
    85|// app/dashboard/page.tsx
    86|import { transactionDal } from "@/dal";
    87|
    88|export default async function Dashboard() {
    89|  const transactions = await transactionDal.findByUserId(userId);
    90|  return <TransactionList txns={transactions} />;
    91|}
    92|```
    93|
    94|**WHY**: Direct DB imports break the abstraction layer. N+1 prevention rules live in DAL, not components. When developers skip DAL, they skip these protections.
    95|
    96|---
    97|
    98|**NEVER #3: Over-fetch all relations upfront**
    99|
   100|❌ WRONG:
   101|
   102|```typescript
   103|// This loads all wallets, accounts, transactions for every user
   104|async function findByIdWithEverything(id: string) {
   105|  return db
   106|    .select()
   107|    .from(users)
   108|    .leftJoin(wallets, eq(wallets.userId, users.id))
   109|    .leftJoin(accounts, eq(accounts.userId, users.id))
   110|    .leftJoin(transactions, eq(transactions.userId, users.id));
   111|}
   112|```
   113|
   114|✅ RIGHT:
   115|
   116|```typescript
   117|// Load only what the caller needs
   118|async function findById(id: string) {
   119|  return db.select().from(users).where(eq(users.id, id));
   120|}
   121|
   122|async function findByIdWithWallets(id: string) {
   123|  // Separate function if wallets are needed
   124|  return findById(id); // + batch-fetch wallets separately
   125|}
   126|```
   127|
   128|**WHY**: Over-fetching causes cartesian products, duplicate rows, and massive result sets. Load only what you need, when you need it.
   129|
   130|---
   131|
   132|**NEVER #4: Assume relationships always exist**
   133|
   134|❌ WRONG:
   135|
   136|```typescript
   137|// If a wallet was deleted, senderWallet becomes undefined
   138|const txn = {
   139|  ...t,
   140|  senderWallet: walletsMap.get(t.senderWalletId) // Could be undefined!
   141|};
   142|```
   143|
   144|✅ RIGHT:
   145|
   146|```typescript
   147|// Use null-coalescing to safely handle missing data
   148|const txn = {
   149|  ...t,
   150|  senderWallet: walletsMap.get(t.senderWalletId) ?? null
   151|};
   152|```
   153|
   154|**WHY**: Soft-deleted records leave orphaned references. Without null-coalescing, your code crashes or returns undefined, breaking frontend expectations.
   155|
   156|---
   157|
   158|**NEVER #5: Forget to check if your batch is empty**
   159|
   160|❌ WRONG:
   161|
   162|```typescript
   163|const walletIds = new Set<string>();
   164|// ... collect IDs ...
   165|const walletsMap = new Map();
   166|const rows = await db
   167|  .select()
   168|  .from(wallets)
   169|  .where(inArray(wallets.id, Array.from(walletIds)));
   170|// If walletIds is empty, inArray() might error
   171|```
   172|
   173|✅ RIGHT:
   174|
   175|```typescript
   176|const walletIds = new Set<string>();
   177|// ... collect IDs ...
   178|const walletsMap = new Map();
   179|if (walletIds.size > 0) {
   180|  const rows = await db
   181|    .select()
   182|    .from(wallets)
   183|    .where(inArray(wallets.id, Array.from(walletIds)));
   184|  for (const row of rows) walletsMap.set(row.id, row);
   185|}
   186|```
   187|
   188|**WHY**: Empty `inArray()` clauses can cause SQL errors. Guard with a size check first.
   189|
   190|---
   191|
   192|## DAL Files
   193|
   194|### user.dal.ts
   195|
   196|- `findByEmail(email)` — Find user by email, excludes soft-deleted
   197|- `findById(id)` — Find user by ID, excludes soft-deleted
   198|- `findByIdWithProfile(id)` — JOIN query, returns UserWithProfile
   199|- `create(data)` — Insert new user
   200|- `update(id, data)` — Partial update user
   201|- `createWithProfile(data)` — Transactional user + profile creation
   202|- `updateProfile(userId, data)` — Upsert profile
   203|- `toggleAdmin(id)` — Flip isAdmin flag
   204|- `toggleActive(id)` — Flip isActive flag
   205|- `softDelete(id)` — Set deletedAt timestamp
   206|- `hardDelete(id)` — Permanent delete
   207|
   208|### wallet.dal.ts
   209|
   210|- `findByUserId(userId)` — Get user's wallets
   211|- `findById(id)` — Get wallet by ID
   212|- `create(data)` — Create new wallet
   213|- `update(id, data)` — Update wallet
   214|- `delete(id)` — Soft delete wallet
   215|
   216|### transaction.dal.ts
   217|
   218|- `findByUserIdWithWallets(userId, limit, offset)` — N+1 prevention pattern
   219|- `findById(id)` — Get transaction by ID
   220|- `findByWalletId(walletId)` — Transactions for wallet
   221|- `create(data)` — Create transaction
   222|- `updateStatus(id, status)` — Update transaction status
   223|
   224|### recipient.dal.ts
   225|
   226|- `findByUserId(userId)` — User's transfer recipients
   227|- `findById(id)` — Get recipient by ID
   228|- `create(data)` — Add recipient
   229|- `update(id, data)` — Update recipient
   230|- `delete(id)` — Remove recipient
   231|
   232|### dwolla.dal.ts
   233|
   234|- `createFundingSource(data)` — Create Dwolla funding source
   235|- `getFundingSource(id)` — Get funding source details
   236|- `initiateTransfer(data)` — Start ACH transfer
   237|- `getTransfer(id)` — Get transfer status
   238|
   239|## Return Types
   240|
   241|All DAL methods return typed objects, not raw DB results:
   242|
   243|```typescript
   244|// Returns { ok: boolean; user?: User; error?: string }
   245|const result = await userDal.findById(id);
   246|if (!result.ok) {
   247|  return { error: result.error, ok: false };
   248|}
   249|```
   250|
   251|## Transaction Support
   252|
   253|Use `db.transaction()` for atomic operations:
   254|
   255|```typescript
   256|await db.transaction(async (tx) => {
   257|  const [user] = await tx.insert(users).values({...}).returning();
   258|  await tx.insert(user_profiles).values({ userId: user.id, ... });
   259|});
   260|```
   261|
   262|## Soft Delete Pattern
   263|
   264|All find methods automatically filter `deletedAt IS NULL` at the database level:
   265|
   266|```typescript
   267|async findById(id: string) {
   268|  const [user] = await db.select().from(users)
   269|    .where(and(eq(users.id, id), isNull(users.deletedAt)));
   270|  return user;
   271|}
   272|```
   273|
   274|**Standard Filtering Approach (Phase B.2 Standardization):**
   275|
   276|All DAL helpers use database-level filtering with `isNull()` to exclude soft-deleted records. This approach:
   277|
   278|1. **Prevents unnecessary row transfers** — Database filters before returning data
   279|2. **Clarifies SQL intent** — `WHERE deletedAt IS NULL` explicitly shows filter in generated SQL
   280|3. **Unifies pattern across DAL** — All tables follow the same convention
   281|
   282|**Soft-delete across tables:**
   283|
   284|- **users table:** `isNull(users.deletedAt)` in `user.dal.ts` `findByEmail()`, `findById()`, `findByIdWithProfile()`
   285|- **wallets table:** `isNull(wallets.deletedAt)` in `wallet.dal.ts` `findById()`, `findBySharableId()`, `findByAccountId()`
   286|- **transactions table:** `isNull(transactions.deletedAt)` in `transaction.dal.ts` `findByUserId()`, etc.
   287|- **recipients table:** Hard delete only (no `deletedAt` column; use cascade delete instead)
   288|
   289|**NEVER use `where()` without soft-delete check:**
   290|
   291|```typescript
   292|// ❌ WRONG (returns deleted records too)
   293|async findById(id: string) {
   294|  return await db.select().from(users).where(eq(users.id, id));
   295|}
   296|
   297|// ✅ CORRECT (excludes soft-deleted)
   298|async findById(id: string) {
   299|  return await db.select().from(users)
   300|    .where(and(eq(users.id, id), isNull(users.deletedAt)));
   301|}
   302|```
   303|
   304|**Testing soft deletes:**
   305|
   306|See `tests/e2e/soft-delete.spec.ts` for comprehensive E2E tests covering:
   307|
   308|- Soft-deleted users excluded from active queries
   309|- Soft-deleted wallets excluded from active queries
   310|- Soft-deleted transactions excluded from active queries
   311|
   312|## N+1 Prevention Pattern: Batch Fetch Example
   313|
   314|This is the canonical pattern. Follow these 4 steps exactly:
   315|
   316|```typescript
   317|export async function findByUserIdWithWallets(
   318|  userId: string,
   319|  limit = 50,
   320|  offset = 0
   321|) {
   322|  // Step 1: Fetch base records
   323|  const txns = await db
   324|    .select()
   325|    .from(transactions)
   326|    .where(eq(transactions.userId, userId))
   327|    .limit(limit)
   328|    .offset(offset);
   329|
   330|  // Step 2: Collect unique IDs (Set prevents duplicates)
   331|  const walletIds = new Set<string>();
   332|  for (const t of txns) {
   333|    if (t.senderWalletId) walletIds.add(t.senderWalletId);
   334|    if (t.receiverWalletId) walletIds.add(t.receiverWalletId);
   335|  }
   336|
   337|  // Step 3: Batch fetch in single query (guard empty set)
   338|  const walletsMap = new Map<string, Wallet>();
   339|  if (walletIds.size > 0) {
   340|    const rows = await db
   341|      .select()
   342|      .from(wallets)
   343|      .where(inArray(wallets.id, Array.from(walletIds)));
   344|    for (const row of rows) {
   345|      walletsMap.set(row.id, row);
   346|    }
   347|  }
   348|
   349|  // Step 4: Map wallets back onto transactions
   350|  return txns.map(txn => ({
   351|    ...txn,
   352|    senderWallet: walletsMap.get(txn.senderWalletId) ?? null,
   353|    receiverWallet: walletsMap.get(txn.receiverWalletId) ?? null
   354|  }));
   355|}
   356|```
   357|
   358|### Handling Edge Cases
   359|
   360|**Empty result set** — walletIds is empty, so batch-fetch is skipped:
   361|
   362|```typescript
   363|if (walletIds.size > 0) {
   364|  // Only query if we have IDs to fetch
   365|  const rows = await db.select().from(wallets)...
   366|}
   367|// walletsMap remains empty Map, all wallet refs become null
   368|```
   369|
   370|**Orphaned references** — wallet was soft-deleted after transaction created:
   371|
   372|```typescript
   373|// walletsMap.get() returns undefined for deleted wallets
   374|senderWallet: walletsMap.get(txn.senderWalletId) ?? null;
   375|// Safe coalescing to null instead of crashing
   376|```
   377|
   378|**Null/missing relationships** — transaction has no sender wallet initially:
   379|
   380|```typescript
   381|// The guard `if (t.senderWalletId)` prevents adding null/undefined to Set
   382|if (t.senderWalletId) walletIds.add(t.senderWalletId);
   383|// Skipped for null values, no wasted queries
   384|```
   385|
   386|---
   387|
   388|## Quick Decision Flow
   389|
   390|```
   391|Do I need related data? →
   392|  YES → Can I batch-fetch all related records in one query?
   393|    YES → Use N+1 prevention pattern (4 steps above)
   394|    NO  → Use LEFT JOIN or separate queries with grouping
   395|  NO → Use direct single-query (findById, findByEmail, etc.)
   396|```
   397|