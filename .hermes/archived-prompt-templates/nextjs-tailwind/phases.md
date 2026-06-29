# Phases

> Extracted from `nextjs-tailwind.prompt.md`.

## Phases

### Phase 1: Architecture and Type Planning

| Field | Details |
| --- | --- |
| Goal | Define route, component, and type architecture before coding. |
| Inputs | Feature requirements, route map, data dependencies, existing components. |
| Outputs | Component hierarchy, server/client split, and type contracts. |
| Validation | Boundaries are explicit and avoid unnecessary client-side execution. |

### Phase 2: Implementation and Styling

| Field | Details |
| --- | --- |
| Goal | Build robust Next.js behavior and Tailwind UI with safe defaults. |
| Inputs | Planned architecture, schemas, data handlers, design requirements. |
| Outputs | Implemented pages/components with responsive styling and error handling. |
| Validation | UI is responsive, semantics are preserved, and runtime paths are safe. |

### Phase 3: Performance and Security Validation

| Field | Details |
| --- | --- |
| Goal | Validate optimization, caching, and secure API/data flow behavior. |
| Inputs | Bundle characteristics, image/font usage, API route logic, auth checks. |
| Outputs | Verified implementation with performance and security notes. |
| Validation | No obvious anti-patterns in bundle usage, caching, or input handling. |
