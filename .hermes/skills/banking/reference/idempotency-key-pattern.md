---
name: idempotency-key-pattern
description: "# Idempotency Key Pattern"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# Idempotency Key Pattern
     2|
     3|## Overview
     4|
     5|Idempotency ensures that Dwolla transfer requests can be safely retried without creating duplicate transfers. This is critical for handling network failures and timeouts in financial transactions.
     6|
     7|## Implementation
     8|
     9|### Database Schema
    10|
    11|The `dwolla_transfers` table includes a unique idempotency key column:
    12|
    13|```typescript
    14|// database/schema.ts (lines 696-698)
    15|idempotencyKey: varchar("idempotency_key", { length: 255 })
    16|  .notNull()
    17|  .unique(),
    18|```
    19|
    20|The `unique()` constraint at the database level prevents duplicate transfers even if the application layer fails.
    21|
    22|### Server Action Pattern
    23|
    24|All Dwolla transfer actions must:
    25|
    26|1. **Generate a unique idempotency key** (UUID) for each transfer request
    27|2. **Pass the key to Dwolla** in the API call
    28|3. **Store the key in the database** before making the API call
    29|4. **Catch unique constraint violations** and return the existing transfer instead of failing
    30|
    31|**Example:**
    32|
    33|```typescript
    34|// actions/dwolla.actions.ts
    35|"use server";
    36|
    37|import { v4 as uuidv4 } from "uuid";
    38|import { dwollaTransferDal } from "@/dal";
    39|
    40|export async function initiateTransfer(input: unknown) {
    41|  const parsed = TransferSchema.safeParse(input);
    42|  if (!parsed.success) {
    43|    return { ok: false, error: parsed.error.issues[0].message };
    44|  }
    45|
    46|  // 1. Generate unique idempotency key
    47|  const idempotencyKey = uuidv4();
    48|
    49|  // 2. Insert transfer record with idempotency key
    50|  const transferred = await dwollaTransferDal.create({
    51|    ...parsed.data,
    52|    idempotencyKey
    53|  });
    54|
    55|  if (!transferred.ok) {
    56|    return { ok: false, error: transferred.error };
    57|  }
    58|
    59|  // 3. Call Dwolla API with idempotency key
    60|  const dwollaResult = await dwolla.transfers.create({
    61|    _links: {
    62|      source: { href: parsed.data.sourceFundingSourceUrl },
    63|      destination: { href: parsed.data.destinationFundingSourceUrl }
    64|    },
    65|    amount: {
    66|      currency: parsed.data.currency || "USD",
    67|      value: parsed.data.amount
    68|    },
    69|    idempotencyKey // <-- Pass to Dwolla
    70|  });
    71|
    72|  if (!dwollaResult.ok) {
    73|    return { ok: false, error: dwollaResult.error };
    74|  }
    75|
    76|  return { ok: true, transfer: transferred.transfer };
    77|}
    78|```
    79|
    80|## Retry Scenarios
    81|
    82|### Scenario 1: Network Timeout (No Response)
    83|
    84|**Step-by-step:**
    85|
    86|1. Client calls `initiateTransfer()`
    87|2. Server creates `dwolla_transfers` record with idempotencyKey = "abc123"
    88|3. Server calls Dwolla API with idempotencyKey = "abc123"
    89|4. Network timeout; server never receives Dwolla response
    90|5. Client sees error; user retries the same transfer
    91|
    92|**Result with Idempotency:**
    93|
    94|- Second request generates new idempotencyKey = "def456" (different)
    95|- Two separate transfer records created (correct behavior: user initiated twice)
    96|
    97|**Result without Idempotency:**
    98|
    99|- Second request has no idempotencyKey
   100|- Dwolla processes as new transfer
   101|- Duplicate transfer created (bad)
   102|
   103|### Scenario 2: Duplicate Request (Same Button Click)
   104|
   105|**Step-by-step:**
   106|
   107|1. Client calls `initiateTransfer()` with idempotencyKey = "abc123"
   108|2. Server creates `dwolla_transfers` record
   109|3. Dwolla API call succeeds
   110|4. Response is lost; client retries with same idempotencyKey = "abc123"
   111|
   112|**Result:**
   113|
   114|- Database unique constraint on `idempotencyKey` blocks insertion
   115|- Application catches error, returns existing transfer
   116|- No duplicate created
   117|
   118|## Testing
   119|
   120|See `tests/e2e/transfer-idempotency.spec.ts` for comprehensive E2E tests:
   121|
   122|- **Test 1:** Duplicate transfer with same idempotency key is rejected
   123|- **Test 2:** Different idempotency keys allow separate transfers
   124|- **Test 3:** Transaction ledger remains consistent after idempotent retry
   125|
   126|## References
   127|
   128|- **Database schema:** `database/schema.ts` (lines 682–722)
   129|- **DAL pattern:** `dal/dwolla-transfer.dal.ts` (if exists)
   130|- **Server action:** `actions/dwolla.actions.ts`
   131|- **E2E tests:** `tests/e2e/transfer-idempotency.spec.ts`
   132|
   133|## Key Rules
   134|
   135|1. **Never reuse idempotency keys** across different transfer requests
   136|2. **Always generate a new UUID** for each new transfer
   137|3. **Store the key before calling Dwolla** (to catch retries)
   138|4. **Let the database unique constraint handle duplicates** (don't check in app logic)
   139|5. **Return the existing transfer if unique constraint fails** (idempotent behavior)
   140|
   141|---
   142|
   143|**Last Updated:** May 5, 2026  
   144|**Phase:** Phase C (Testing)
   145|