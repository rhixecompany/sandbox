# Code Exemplars — rhixe_scans

## 1. Prisma Schema

```prisma
model Comic {
  id          String   @id @default(cuid())
  title       String
  slug        String   @unique
  description String?
  coverUrl    String?
  chapters    Chapter[]
  genres      Genre[]
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Chapter {
  id        String   @id @default(cuid())
  number    Float
  pages     String[] // URLs to page images
  comic     Comic    @relation(fields: [comicId], references: [id])
  comicId   String
  createdAt DateTime @default(now())
}
```

## 2. Stripe Integration

```typescript
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function createCheckoutSession(comicId: string) {
  const session = await stripe.checkout.sessions.create({
    line_items: [{ price: "price_id", quantity: 1 }],
    mode: "payment",
    success_url: `${process.env.NEXT_PUBLIC_URL}/success`,
    cancel_url: `${process.env.NEXT_PUBLIC_URL}/cancel`,
  });
  return session;
}
```
