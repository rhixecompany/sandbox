# Architecture Blueprint: rhixe_scans

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Frontend Framework** | Next.js 15 (App Router, Turbopack), React 19 |
| **Language** | TypeScript (strict) |
| **Database** | PostgreSQL via Prisma ORM 6 |
| **Authentication** | NextAuth v5 with Prisma adapter |
| **Payments** | Stripe (react-stripe-js), PayPal (@paypal/react-paypal-js) |
| **File Storage** | UploadThing |
| **Email** | Resend + React Email |
| **Real-time** | WebSocket (ws) |
| **UI Components** | Radix UI primitives, shadcn/ui style |
| **Styling** | Tailwind CSS 3 |
| **Data Tables** | @tanstack/react-table |
| **Charts** | recharts |
| **Drag-and-Drop** | @dnd-kit |
| **Testing** | Jest + ts-jest |
| **Backend** | Python (Django or FastAPI in `backend/`) |
| **Infrastructure** | Docker Compose, systemd |

### Architectural Pattern Detected

**Pattern:** Full-Stack Next.js + Python Backend with Dual Payments  
The project combines a modern Next.js frontend with a Python backend, supporting:

- **Frontend**: Next.js 15 App Router with Server Components
- **Backend**: Python API server (in `backend/` directory)
- **Payments**: Dual payment providers (Stripe + PayPal)
- **Database**: PostgreSQL via Prisma ORM
- **Real-time**: WebSocket support

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Next.js 15 Frontend                        │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────┐ │
│  │ App Router │  │ Prisma ORM │  │ WebSocket  │  │ Auth   │ │
│  │ (Turbopack)│  │ (PostgreSQL)│  │ (ws)       │  │ NAuth  │ │
│  └────────────┘  └────────────┘  └────────────┘  └────────┘ │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────┐   │
│  │ Stripe     │  │ PayPal     │  │ UploadThing (Files)  │   │
│  │ Payments   │  │ Payments   │  │ Resend (Email)       │   │
│  └────────────┘  └────────────┘  └──────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Python Backend (backend/)                  │
│                    Django / FastAPI API                       │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Prisma ORM for frontend DB access | Type-safe database queries with excellent Next.js integration |
| Dual payments (Stripe + PayPal) | Maximum payment flexibility |
| Python backend alongside Next.js | Backend processing separate from frontend rendering |
| UploadThing for file storage | Serverless-friendly file uploads |
| WebSocket support | Real-time scan processing updates |

---

## 4. Data Flow

### Scan Processing Flow
```
User Upload → UploadThing → Next.js Server Action → Prisma → PostgreSQL
                                                            ↓
                                          Python Backend (processing)
                                                            ↓
                                          WebSocket notification → User
```

### Payment Flow
```
User Checkout → Stripe/PayPal → Webhook → Next.js API → Prisma → Database
```

---

## 5. Implementation Patterns

### Prisma Schema Pattern
```prisma
model Scan {
  id        String   @id @default(cuid())
  title     String
  fileUrl   String
  status    ScanStatus
  createdAt DateTime @default(now())
}
```

### Server Action Pattern
```typescript
"use server";
import { prisma } from "@/lib/prisma";
export async function createScan(data: ScanInput) {
  // Zod validation → Prisma create → return result
}
```

---

## 6. Extensibility Points

1. **New scan processing pipeline**: Add Python processing modules
2. **Additional payment providers**: Follow Stripe/PayPal patterns
3. **Enhanced real-time features**: Extend WebSocket implementation
4. **New frontend features**: Add pages under App Router route groups

---

*End of architecture blueprint.*
