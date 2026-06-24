---
license: MIT
author: Hermes Agent
version: 1.0.0
title: ASP.NET .NET Framework Containerization Prompt
name: containerize-aspnet-framework
agent: "agent"
tools: ["search/codebase", "edit/editFiles", "terminalCommand"]
description: "Containerize an ASP.NET .NET Framework project by creating Dockerfile and .dockerfile files customized for the project."
---

# ASP.NET .NET Framework Containerization Prompt

Containerize the ASP.NET (.NET Framework) project specified in the containerization settings below, focusing **exclusively** on changes required for the application to run in a Windows Docker container. Containerization should consider all settings specified here.

**REMEMBER:** This is a .NET Framework application, not .NET Core. The containerization process will be different from that of a .NET Core application.

## Containerization Settings

> This section of the prompt contains the specific settings and configurations req
> Any settings that are not specified will be set to default values. The default v

> **Full content:** `templates/containerize-aspnet-framework/containerization_settings.md`

## Scope

- ✅ App configuration modification to ensure config builders are used to read app settings and connection strings from the environment variables
- ✅ Dockerfile creation and configuration for an ASP.NET application
- ✅ Specifying multiple stages in the Dockerfile to build/publish the application and copy the output to the final image
- ✅ Configuration of Windows container platform compatibility (Windows Server Core or Full)
- ✅ Proper handling of dependencies (GAC assemblies, MSIs, COM components)
- ❌ No infrastructure setup (assumed to be handled separately)
- ❌ No code changes beyond those required for containerization

## Execution Process

> 1. Review the containerization settings above to understand the containerization
> 2. Create a `progress.md` file to track changes with check marks

> **Full content:** `templates/containerize-aspnet-framework/execution_process.md`

## Build and Runtime Verification

confirm that Docker build succeeds once the Dockerfile is completed. Use the following command to build the Docker image:

```bash
docker build -t aspnet-app:latest .
```

If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a `progress.md` file with the following structure:

```markdown
# Containerization Progress

## Environment Detection

- [ ] .NET Framework version detection (version: \_\_\_)
- [ ] Windows Server SKU selection (SKU: \_\_\_)
- [ ] Windows Server version selection (Version: \_\_\_)

## Configuration Changes

- [ ] Web.config modifications for configuration builders
- [ ] NuGet package source configuration (if applicable)
- [ ] Copy LogMonitorConfig.json and adjust if required by settings

## Containerization

- [ ] Dockerfile creation
- [ ] .dockerignore file creation
- [ ] Build stage created with SDK image
- [ ] sln, csproj, packages.config, and (if applicable) NuGet.config copied for package restore
- [ ] Runtime stage created with runtime image
- [ ] Non-root user configuration
- [ ] Dependency handling (GAC, MSI, COM, registry, additional files, etc.)
- [ ] Health check configuration (if applicable)
- [ ] Special requirements implementation

## Verification

- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success
```

Do not pause for confirmation between steps. Continue methodically until the application has been containerized and Docker build succeeds.

**YOU ARE NOT DONE UNTIL ALL CHECKBOXES ARE MARKED!** This includes building the Docker image successfully and addressing any issues that arise during the build process.

## Reference Materials

> ### Example Dockerfile
> An example Dockerfile for an ASP.NET (.NET Framework) application using a Window

> **Full content:** `templates/containerize-aspnet-framework/reference_materials.md`

## Adapting this Example

**Note:** Customize this template based on the specific requirements in the containerization settings.

When adapting this example Dockerfile:

1. Replace `YourSolution.sln`, `YourProject.csproj`, etc. with your actual file names
2. Adjust the Windows Server and .NET Framework versions as needed
3. Modify the dependency installation steps based on your requirements and remove any unnecessary ones
4. Add or remove stages as needed for your specific workflow

## Notes on Stage Naming

> - The `AS stage-name` syntax gives each stage a name
> - Use `--from=stage-name` to copy files from a previous stage

> **Full content:** `templates/containerize-aspnet-framework/notes_on_stage_naming.md`

## Template References

Detailed templates in `templates/containerize-aspnet-framework/`:
- `containerization_settings.md`
- `execution_process.md`
- `notes_on_stage_naming.md`
- `reference_materials.md`
