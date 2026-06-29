# Workflow

> Extracted from `typespec-create-api-plugin.prompt.md`.

## Workflow

Ask the user:

1. What is the API base URL and purpose?
2. What operations are needed (CRUD operations)?
3. What authentication method does the API use?
4. Should confirmations be required for any operations?
5. Do responses need Adaptive Cards?

Then generate:

- Complete `main.tsp` with agent definition
- Complete `actions.tsp` with API operations and models
- Optional `cards/card.json` if Adaptive Cards are needed
