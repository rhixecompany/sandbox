# Execution Process

> Extracted from `containerize-aspnet-framework.prompt.md`.

## Execution Process

1. Review the containerization settings above to understand the containerization requirements
2. Create a `progress.md` file to track changes with check marks
3. Determine the .NET Framework version from the project's .csproj file by checking the `TargetFrameworkVersion` element
4. Select the appropriate Windows Server container image based on:
   - The .NET Framework version detected from the project
   - The Windows Server SKU specified in containerization settings (Core or Full)
   - The Windows Server version specified in containerization settings (2016, 2019, or 2022)
   - Windows Server Core tags can be found at: https://github.com/microsoft/dotnet-framework-docker/blob/main/README.aspnet.md#full-tag-listing
5. Ensure that required NuGet packages are installed. **DO NOT** install these if they are missing. If they are not installed, the user must install them manually. If they are not installed, pause executing this prompt and ask the user to install them using the Visual Studio NuGet Package Manager or Visual Studio package manager console. The following packages are required:
   - `Microsoft.Configuration.ConfigurationBuilders.Environment`
6. Modify the `web.config` file to add configuration builders section and settings to read app settings and connection strings from environment variables:
   - Add ConfigBuilders section in configSections
   - Add configBuilders section in the root
   - Configure EnvironmentConfigBuilder for both appSettings and connectionStrings
   - Example pattern:
     ```xml
     <configSections>
       <section name="configBuilders" type="System.Configuration.ConfigurationBuildersSection, System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" restartOnExternalChanges="false" requirePermission="false" />
     </configSections>
     <configBuilders>
       <builders>
         <add name="Environment" type="Microsoft.Configuration.ConfigurationBuilders.EnvironmentConfigBuilder, Microsoft.Configuration.ConfigurationBuilders.Environment" />
       </builders>
     </configBuilders>
     <appSettings configBuilders="Environment">
       <!-- existing app settings -->
     </appSettings>
     <connectionStrings configBuilders="Environment">
       <!-- existing connection strings -->
     </connectionStrings>
     ```
7. Create a `LogMonitorConfig.json` file in the folder where the Dockerfile will be created by copying the reference `LogMonitorConfig.json` file at the end of this prompt. The file's contents **MUST NOT** not be modified and should match the reference content exactly unless instructions in containerization settings specify otherwise.
   - In particular, make sure the level of issues to be logged is not changed as using `Information` level for EventLog sources will cause unnecessary noise.
8. Create a Dockerfile in the root of the project directory to containerize the application
   - The Dockerfile should use multiple stages:
     - Build stage: Use a Windows Server Core image to build the application
       - The build stage MUST use a `mcr.microsoft.com/dotnet/framework/sdk` base image unless a custom base image is specified in the settings file
       - Copy sln, csproj, and packages.config files first
       - Copy NuGet.config if one exists and configure any private feeds
       - Restore NuGet packages
       - Then, copy the rest of the source code and build and publish the application to C:\publish using MSBuild
     - Final stage: Use the selected Windows Server image to run the application
       - The final stage MUST use a `mcr.microsoft.com/dotnet/framework/aspnet` base image unless a custom base image is specified in the settings file
       - Copy the `LogMonitorConfig.json` file to a directory in the container (e.g., C:\LogMonitor)
       - Download LogMonitor.exe from the Microsoft repository to the same directory
         - The correct LogMonitor.exe URL is: https://github.com/microsoft/windows-container-tools/releases/download/v2.1.1/LogMonitor.exe
       - Set the working directory to C:\inetpub\wwwroot
       - Copy the published output from the build stage (in C:\publish) to the final image
       - Set the container's entry point to run LogMonitor.exe with ServiceMonitor.exe to monitor the IIS service
         - `ENTRYPOINT [ "C:\\LogMonitor\\LogMonitor.exe", "C:\\ServiceMonitor.exe", "w3svc" ]`
   - Be sure to consider all requirements in the containerization settings:
     - Windows Server SKU and version
     - Exposed ports
     - User account for container
     - IIS settings
     - GAC assembly registration
     - MSI installation
     - COM component registration
     - Registry keys
     - Environment variables
     - Windows roles and features
     - File/directory copying
   - Model the Dockerfile after the example provided at the end of this prompt, but ensure it is customized to the specific project requirements and settings.
   - **IMPORTANT:** Use a Windows Server Core base image unless the user has **specifically requested** a full Windows Server image in the settings file
9. Create a `.dockerignore` file in the root of the project directory to exclude unnecessary files from the Docker image. The `.dockerignore` file **MUST** include at least the following elements as well as additional patterns as specified in the containerization settings:
   - packages/
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
10. Configure health checks if specified in the settings:

- Add HEALTHCHECK instruction to Dockerfile if health check endpoint is provided

11. Add the dockerfile to the project by adding the following item to the project file: `<None Include="Dockerfile" />`
12. Mark tasks as completed: [ ] → [✓]
13. Continue until all tasks are complete and Docker build succeeds
