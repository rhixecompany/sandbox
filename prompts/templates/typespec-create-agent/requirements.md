# Requirements

> Extracted from `typespec-create-agent.prompt.md`.

## Requirements

Generate a `main.tsp` file with:

1. **Agent Declaration**
   - Use `@agent` decorator with a descriptive name and description
   - Name should be 100 characters or less
   - Description should be 1,000 characters or less

2. **Instructions**
   - Use `@instructions` decorator with clear behavioral guidelines
   - Define the agent's role, expertise, and personality
   - Specify what the agent should and shouldn't do
   - Keep under 8,000 characters

3. **Conversation Starters**
   - Include 2-4 `@conversationStarter` decorators
   - Each with a title and example query
   - Make them diverse and showcase different capabilities

4. **Capabilities** (based on user needs)
   - `WebSearch` - for web content with optional site scoping
   - `OneDriveAndSharePoint` - for document access with URL filtering
   - `TeamsMessages` - for Teams channel/chat access
   - `Email` - for email access with folder filtering
   - `People` - for organization people search
   - `CodeInterpreter` - for Python code execution
   - `GraphicArt` - for image generation
   - `GraphConnectors` - for Copilot connector content
   - `Dataverse` - for Dataverse data access
   - `Meetings` - for meeting content access
