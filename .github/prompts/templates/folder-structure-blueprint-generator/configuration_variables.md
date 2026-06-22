# Configuration Variables

> Extracted from `folder-structure-blueprint-generator.prompt.md`.

## Configuration Variables

${PROJECT_TYPE="Auto-detect|.NET|Java|React|Angular|Python|Node.js|Flutter|Other"}

<!-- Select primary technology -->

${INCLUDES_MICROSERVICES="Auto-detect|true|false"}

<!-- Is this a microservices architecture? -->

${INCLUDES_FRONTEND="Auto-detect|true|false"}

<!-- Does project include frontend components? -->

${IS_MONOREPO="Auto-detect|true|false"}

<!-- Is this a monorepo with multiple projects? -->

${VISUALIZATION_STYLE="ASCII|Markdown List|Table"}

<!-- How to visualize the structure -->

${DEPTH_LEVEL=1-5}

<!-- How many levels of folders to document in detail -->

${INCLUDE_FILE_COUNTS=true|false}

<!-- Include file count statistics -->

${INCLUDE_GENERATED_FOLDERS=true|false}

<!-- Include auto-generated folders -->

${INCLUDE_FILE_PATTERNS=true|false}

<!-- Document file naming/location patterns -->

${INCLUDE_TEMPLATES=true|false}

<!-- Include file/folder templates for new features -->
