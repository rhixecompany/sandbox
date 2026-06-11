# Architecture — rhixe_scans

## Overview
A full-featured web application for reading comics online with payment integration.

## Architecture Layers

### 1. Presentation Layer
- Next.js App Router with Turbopack for fast refresh
- Radix UI primitives for accessible components
- Embla Carousel for comic page navigation
- TanStack Table for data management

### 2. Data Layer
- Prisma ORM with PostgreSQL
- Database schema-driven development
- Migrations via Prisma Migrate
- Seeding scripts for development data

### 3. Authentication & Authorization
- NextAuth v5 with Prisma adapter
- Session management via JWT
- Role-based access for admin features

### 4. Payment Processing
- Stripe for credit card payments
- PayPal for alternative payments
- Server-side API keys for security

### 5. Real-time Features
- WebSocket support (ws library)
- Live notifications and updates

## Data Flow
```
Browser → Next.js → Prisma ORM → PostgreSQL
            ↓
      Stripe/PayPal API
            ↓
      UploadThing (files)
            ↓
      Resend (email)
```
