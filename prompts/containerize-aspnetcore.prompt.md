---
toolsets: ["search/codebase", "edit/editFiles", "terminalCommand"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: ASP.NET Core Docker Containerization Prompt
name: containerize-aspnetcore
description: "Containerize an ASP.NET Core project by creating Dockerfile and .dockerfile files customized for the project."
tags: []
---

# ASP.NET Core Docker Containerization Prompt

## Containerization Request

Containerize the ASP.NET Core (.NET) project specified in the settings below, focusing **exclusively** on changes required for the application to run in a Linux Docker container. Containerization should consider all settings specified here.

Abide by best practices for containerizing .NET Core applications, ensuring that the container is optimized for performance, security, and maintainability.

## Containerization Settings

> This section of the prompt contains the specific settings and configurations req
> Any settings that are not specified will be set to default values. The default v

> **Full content:** `templates/containerize-aspnetcore/containerization_settings.md`

## Scope

- ✅ App configuration modification to ensure application settings and connection strings can be read from environment variables
- ✅ Dockerfile creation and configuration for an ASP.NET Core application
- ✅ Specifying multiple stages in the Dockerfile to build/publish the application and copy the output to the final image
- ✅ Configuration of Linux container platform compatibility (Alpine, Ubuntu, Chiseled, or Azure Linux (Mariner))
- ✅ Proper handling of dependencies (system packages, native libraries, additional tools)
- ❌ No infrastructure setup (assumed to be handled separately)
- ❌ No code changes beyond those required for containerization

## Execution Process

> 1. Review the containerization settings above to understand the containerization
> 2. Create a `progress.md` file to track changes with check marks

> **Full content:** `templates/containerize-aspnetcore/execution_process.md`

## Build and Runtime Verification

Confirm that Docker build succeeds once the Dockerfile is completed. Use the following command to build the Docker image:

```bash
docker build -t aspnetcore-app:latest .
```

If the build fails, review the error messages and make necessary adjustments to the Dockerfile or project configuration. Report success/failure.

## Progress Tracking

Maintain a `progress.md` file with the following structure:

```markdown
# Containerization Progress

## Environment Detection

- [ ] .NET version detection (version: \_\_\_)
- [ ] Linux distribution selection (distribution: \_\_\_)

## Configuration Changes

- [ ] Application configuration verification for environment variable support
- [ ] NuGet package source configuration (if applicable)

## Containerization

- [ ] Dockerfile creation
- [ ] .dockerignore file creation
- [ ] Build stage created with SDK image
- [ ] csproj file(s) copied for package restore
- [ ] NuGet.config copied if applicable
- [ ] Runtime stage created with runtime image
- [ ] Non-root user configuration
- [ ] Dependency handling (system packages, native libraries, tools, etc.)
- [ ] Health check configuration (if applicable)
- [ ] Special requirements implementation

## Verification

- [ ] Review containerization settings and make sure that all requirements are met
- [ ] Docker build success
```

Do not pause for confirmation between steps. Continue methodically until the application has been containerized and Docker build succeeds.

**YOU ARE NOT DONE UNTIL ALL CHECKBOXES ARE MARKED!** This includes building the Docker image successfully and addressing any issues that arise during the build process.

## Example Dockerfile

> An example Dockerfile for an ASP.NET Core (.NET) application using a Linux base 
> # ============================================================

> **Full content:** `templates/containerize-aspnetcore/example_dockerfile.md`

## Adapting this Example

**Note:** Customize this template based on the specific requirements in containerization settings.

When adapting this example Dockerfile:

1. Replace `YourProject.csproj`, `YourProject.dll`, etc. with your actual project names
2. Adjust the .NET version and Linux distribution as needed
3. Modify the dependency installation steps based on your requirements and remove any unnecessary ones
4. Configure environment variables specific to your application
5. Add or remove stages as needed for your specific workflow
6. Update the health check endpoint to match your application's health check route

## Linux Distribution Variations

> For smaller image sizes, you can use Alpine Linux:
> FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build

> **Full content:** `templates/containerize-aspnetcore/linux_distribution_variations.md`

## Notes on Stage Naming

- The `AS stage-name` syntax gives each stage a name
- Use `--from=stage-name` to copy files from a previous stage
- You can have multiple intermediate stages that aren't used in the final image
- The `final` stage is the one that becomes the final container image

## Security Best Practices

- Always run as a non-root user in production
- Use specific image tags instead of `latest`
- Minimize the number of installed packages
- Keep base images updated
- Use multi-stage builds to exclude build dependencies from the final image


## Template References

Detailed templates in `templates/containerize-aspnetcore/`:
- `containerization_settings.md`
- `example_dockerfile.md`
- `execution_process.md`
- `linux_distribution_variations.md`
