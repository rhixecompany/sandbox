# Code Exemplars — university-libary-jsm

## 1. Drizzle Schema with Zod

```typescript
import { pgTable, text, timestamp, uuid } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";

export const books = pgTable("books", {
  id: uuid("id").defaultRandom().primaryKey(),
  title: text("title").notNull(),
  author: text("author").notNull(),
  isbn: text("isbn").unique(),
  createdAt: timestamp("created_at").defaultNow(),
});

export const insertBookSchema = createInsertSchema(books, {
  title: (schema) => schema.title.min(1).max(200),
  author: (schema) => schema.author.min(1).max(100),
});
```

## 2. Server Action with Validation

```typescript
"use server";
import { db } from "@/database/db";
import { books, insertBookSchema } from "@/database/schema";

export async function createBook(input: unknown) {
  const parsed = insertBookSchema.safeParse(input);
  if (!parsed.success) {
    return { error: parsed.error.message, ok: false };
  }
  const [book] = await db.insert(books).values(parsed.data).returning();
  return { ok: true, data: book };
}
```
