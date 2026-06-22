# Execution Process

> Extracted from `containerize-aspnetcore.prompt.md`.

## Execution Process

1. Review the containerization settings above to understand the containerization requirements
2. Create a `progress.md` file to track changes with check marks
3. Determine the .NET version from the project's .csproj file by checking the `TargetFramework` element
4. Select the appropriate Linux container image based on:
   - The .NET version detected from the project
   - The Linux distribution specified in containerization settings (Alpine, Ubuntu, Chiseled, or Azure Linux (Mariner))
   - If the user does not request specific base images in the containerization settings, then the base images MUST be valid mcr.microsoft.com/dotnet images with a tag as shown in the example Dockerfile, below, or in documentation
   - Official Microsoft .NET images for build and runtime stages:
     - SDK image tags (for build stage): https://github.com/dotnet/dotnet-docker/blob/main/README.sdk.md
     - ASP.NET Core runtime image tags: https://github.com/dotnet/dotnet-docker/blob/main/README.aspnet.md
     - .NET runtime image tags: https://github.com/dotnet/dotnet-docker/blob/main/README.runtime.md
5. Create a Dockerfile in the root of the project directory to containerize the application
   - The Dockerfile should use multiple stages:
     - Build stage: Use a .NET SDK image to build the application
       - Copy csproj file(s) first
       - Copy NuGet.config if one exists and configure any private feeds
       - Restore NuGet packages
       - Then, copy the rest of the source code and build and publish the application to /app/publish
     - Final stage: Use the selected .NET runtime image to run the application
       - Set the working directory to /app
       - Set the user as directed (by default, to a non-root user (e.g., `$APP_UID`))
         - Unless directed otherwise in containerization settings, a new user does _not_ need to be created. Use the `$APP_UID` variable to specify the user account.
       - Copy the published output from the build stage to the final image
   - Be sure to consider all requirements in the containerization settings:
     - .NET version and Linux distribution
     - Exposed ports
     - User account for container
     - ASPNETCORE_URLS configuration
     - System package installation
     - Native library dependencies
     - Additional .NET tools
     - Environment variables
     - File/directory copying
     - Volume mount points
     - Health check configuration
6. Create a `.dockerignore` file in the root of the project directory to exclude unnecessary files from the Docker image. The `.dockerignore` file **MUST** include at least the following elements as well as additional patterns as specified in the containerization settings:
   - bin/
   - obj/
   - .dockerignore
   - Dockerfile
   - .git/
   - .github/
   - .vs/
   - .vscode/
   - \*\*/node_modules/
   - \*.user
   - \*.suo
   - \*\*/.DS_Store
   - \*\*/Thumbs.db
   - Any additional patterns specified in the containerization settings
7. Configure health checks if specified in the containerization settings:
   - Add HEALTHCHECK instruction to Dockerfile if health check endpoint is provided
   - Use curl or wget to check the health endpoint
8. Mark tasks as completed: [ ] → [✓]
9. Continue until all tasks are complete and Docker build succeeds
