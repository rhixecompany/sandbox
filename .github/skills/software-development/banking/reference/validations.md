---
name: validations
description: "# Validation & Server Actions Reference"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# Validation & Server Actions Reference
     2|
     3|**Quick Reference**: [NEVER List](#validation-anti-patterns) | [Schemas](#zod-schemas) | [Strategy](#before-writing-a-validation-schema) | [Actions](#action-files) | [Patterns](#server-actions-pattern) | [Errors](#error-handling)
     4|
     5|---
     6|
     7|## Validation Anti-Patterns
     8|
     9|**NEVER** use `.parse()` without try-catch (crashes on invalid input):
    10|
    11|```typescript
    12|// ❌ WRONG - throws exception, no graceful handling
    13|const user = signUpSchema.parse(input);
    14|
    15|// ✅ CORRECT - returns error object, graceful error handling
    16|const parsed = signUpSchema.safeParse(input);
    17|if (!parsed.success) return { error: "Invalid input", ok: false };
    18|```
    19|
    20|**Why**: `.parse()` throws exceptions on validation failure. `.safeParse()` returns structured errors safe to return to users.
    21|
    22|---
    23|
    24|**NEVER** expose raw Zod error objects to users (leaks implementation details):
    25|
    26|```typescript
    27|// ❌ WRONG - exposes internals, confusing to users
    28|return { ok: false, errors: parsed.error.errors };
    29|
    30|// ✅ CORRECT - humanized, user-friendly error
    31|const message = parsed.error.issues[0].message;
    32|return { ok: false, error: message };
    33|```
    34|
    35|**Why**: Raw Zod errors contain field paths and type information; users need clear, actionable messages. Limit to 1–3 error messages per response.
    36|
    37|---
    38|
    39|**NEVER** validate monetary amounts as strings (precision loss and injection risks):
    40|
    41|```typescript
    42|// ❌ WRONG - string math causes precision issues
    43|const amount = z.string().transform(x => parseFloat(x));
    44|
    45|// ✅ CORRECT - validate as number with explicit bounds
    46|const amount = z.number().positive().finite().max(10000);
    47|```
    48|
    49|**Why**: Floating-point strings introduce rounding errors. Numbers enforce type safety; use `.max()` to prevent transfer limit bypass.
    50|
    51|---
    52|
    53|**NEVER** skip transfer limit validation at the schema level (security risk):
    54|
    55|```typescript
    56|// ❌ WRONG - no limit enforcement
    57|const transferSchema = z.object({
    58|  amount: z.number().positive()
    59|});
    60|
    61|// ✅ CORRECT - explicit limit in schema
    62|const transferSchema = z.object({
    63|  amount: z.number().positive().max(10000)
    64|});
    65|```
    66|
    67|**Why**: Validation happens in Server Actions, before DAL. Schema-level limits prevent even invalid requests from reaching the database.
    68|
    69|---
    70|
    71|**NEVER** reuse schemas across contexts without modification (security + UX):
    72|
    73|```typescript
    74|// ❌ WRONG - admin and user schemas identical
    75|export const createUserSchema = z.object({ email, password, role });
    76|
    77|// ✅ CORRECT - separate schemas by context
    78|export const userSignUpSchema = z.object({ email, password }); // Users can't set role
    79|export const adminCreateUserSchema = z.object({
    80|  email,
    81|  password,
    82|  role
    83|}); // Admins can
    84|```
    85|
    86|**Why**: User roles affect what fields are allowed. Admin schemas should enforce stricter validation (no user role escalation).
    87|
    88|---
    89|
    90|## Before Writing a Validation Schema
    91|
    92|Ask yourself these questions:
    93|
    94|- **Strictness**: Should this validate strictly for security (transfers, auth) or loosely for UX (optional fields)?
    95|- **User Feedback**: Will validation errors be immediately obvious? Should message be for users or developers?
    96|- **Security**: Does this schema prevent injection, limit bypass, or unintended field modification?
    97|- **Edge Cases**: How do you handle max Int values, empty strings vs. null, timezone-aware dates?
    98|- **Extensibility**: Will this schema need new fields? How will you version it?
    99|- **Consistency**: Do error shapes match everywhere? Is error handling pattern reused?
   100|
   101|---
   102|
   103|## Zod Schemas
   104|
   105|Location: `lib/validations/`
   106|
   107|**signUpSchema** (`auth.ts`):
   108|
   109|```typescript
   110|export const signUpSchema = z.object({
   111|  email: z.string().email(),
   112|  password: z.string().min(8).max(100),
   113|  firstName: z.string().min(1).max(50),
   114|  lastName: z.string().min(1).max(50),
   115|  address1: z.string().optional()
   116|});
   117|```
   118|
   119|**signInSchema** (`auth.ts`):
   120|
   121|```typescript
   122|export const signInSchema = z.object({
   123|  email: z.string().email(),
   124|  password: z.string().min(1)
   125|});
   126|```
   127|
   128|**transferSchema** (`transfer.ts`):
   129|
   130|```typescript
   131|export const transferSchema = z.object({
   132|  amount: z.number().positive().max(10000),
   133|  fromWalletId: z.string().uuid(),
   134|  toRecipientId: z.string().uuid(),
   135|  memo: z.string().max(200).optional()
   136|});
   137|```
   138|
   139|## Server Actions Pattern
   140|
   141|All actions in `actions/*.ts` follow this flow:
   142|
   143|```typescript
   144|"use server";
   145|import { z } from "zod";
   146|import { userDal } from "@/dal";
   147|import { someSchema } from "@/lib/validations/some";
   148|
   149|export async function doSomething(input: unknown): Promise<{
   150|  ok: boolean;
   151|  data?: SomeType;
   152|  error?: string;
   153|}> {
   154|  // 1. Validate input (ALWAYS use safeParse)
   155|  const parsed = someSchema.safeParse(input);
   156|  if (!parsed.success) {
   157|    const errors = parsed.error.issues
   158|      .slice(0, 3)
   159|      .map(i => i.message)
   160|      .join("; ");
   161|    return { error: errors, ok: false };
   162|  }
   163|
   164|  // 2. Auth check (if protected)
   165|  const session = await auth();
   166|  if (!session?.user?.id) {
   167|    return { error: "Unauthorized", ok: false };
   168|  }
   169|
   170|  // 3. Use DAL helper
   171|  const result = await someDal.doSomething(parsed.data);
   172|  if (!result.ok) return { error: result.error, ok: false };
   173|
   174|  // 4. Revalidate cache (if needed)
   175|  revalidatePath("/dashboard");
   176|  return { ok: true, data: result.data };
   177|}
   178|```
   179|
   180|## Action Files
   181|
   182|| File                             | Purpose                |
   183|| -------------------------------- | ---------------------- |
   184|| `actions/register.ts`            | User registration      |
   185|| `actions/auth.signin.ts`         | Sign in                |
   186|| `actions/user.actions.ts`        | User profile updates   |
   187|| `actions/updateProfile.ts`       | Profile updates        |
   188|| `actions/wallet.actions.ts`      | Wallet CRUD            |
   189|| `actions/transaction.actions.ts` | Transaction operations |
   190|| `actions/plaid.actions.ts`       | Plaid bank linking     |
   191|| `actions/dwolla.actions.ts`      | ACH transfers          |
   192|| `actions/recipient.actions.ts`   | Transfer recipients    |
   193|| `actions/admin.actions.ts`       | Admin operations       |
   194|| `actions/admin-stats.actions.ts` | Admin statistics       |
   195|
   196|## Error Handling
   197|
   198|Always return consistent error shape:
   199|
   200|```typescript
   201|// Success
   202|return { ok: true, user: result.user };
   203|
   204|// Error (always include message)
   205|return { error: "Email already registered", ok: false };
   206|```
   207|
   208|**Rules**:
   209|
   210|- Limit error messages to 1–3 per response (focus user attention)
   211|- Never expose raw Zod errors
   212|- Never leak sensitive details (avoid "user ID 42 not found" — use "Invalid request")
   213|
   214|## TypeScript Types
   215|
   216|Export inferred types from Zod schemas for type-safe forms:
   217|
   218|```typescript
   219|export type RegisterInput = z.infer<typeof signUpSchema>;
   220|```
   221|
   222|This allows callers to import and use the type without duplicating validation logic.
   223|