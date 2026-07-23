# Template Structure

> Extracted from `typespec-create-agent.prompt.md`.

## Template Structure

```typescript
import "@typespec/http";
import "@typespec/openapi3";
import "@microsoft/typespec-m365-copilot";

using TypeSpec.Http;
using TypeSpec.M365.Copilot.Agents;

@agent({
  name: "[Agent Name]",
  description: "[Agent Description]"
})
@instructions("""
  [Detailed instructions about agent behavior, role, and guidelines]
""")
@conversationStarter(#{
  title: "[Starter Title 1]",
  text: "[Example query 1]"
})
@conversationStarter(#{
  title: "[Starter Title 2]",
  text: "[Example query 2]"
})
namespace [AgentName] {
  // Add capabilities as operations here
  op capabilityName is AgentCapabilities.[CapabilityType]<[Parameters]>;
}
````
