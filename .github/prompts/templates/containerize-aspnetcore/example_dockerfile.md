# Example Dockerfile

> Extracted from `containerize-aspnetcore.prompt.md`.

## Example Dockerfile

An example Dockerfile for an ASP.NET Core (.NET) application using a Linux base image.

```dockerfile
# ============================================================
# Stage 1: Build and publish the application
# ============================================================

# Base Image - Select the appropriate .NET SDK version and Linux distribution
# Possible tags include:
# - 8.0-bookworm-slim (Debian 12)
# - 8.0-noble (Ubuntu 24.04)
# - 8.0-alpine (Alpine Linux)
# - 9.0-bookworm-slim (Debian 12)
# - 9.0-noble (Ubuntu 24.04)
# - 9.0-alpine (Alpine Linux)
# Uses the .NET SDK image for building the application
FROM mcr.microsoft.com/dotnet/sdk:8.0-bookworm-slim AS build
ARG BUILD_CONFIGURATION=Release

WORKDIR /src

# Copy project files first for better caching
COPY ["YourProject/YourProject.csproj", "YourProject/"]
COPY ["YourOtherProject/YourOtherProject.csproj", "YourOtherProject/"]

# Copy NuGet configuration if it exists
COPY ["NuGet.config", "."]

# Restore NuGet packages
RUN dotnet restore "YourProject/YourProject.csproj"

# Copy source code
COPY . .

# Perform custom pre-build steps here, if needed
# RUN echo "Running pre-build steps..."

# Build and publish the application
WORKDIR "/src/YourProject"
RUN dotnet build "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/build

# Publish the application
RUN dotnet publish "YourProject.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# Perform custom post-build steps here, if needed
# RUN echo "Running post-build steps..."

# ============================================================
# Stage 2: Final runtime image
# ============================================================

# Base Image - Select the appropriate .NET runtime version and Linux distribution
# Possible tags include:
# - 8.0-bookworm-slim (Debian 12)
# - 8.0-noble (Ubuntu 24.04)
# - 8.0-alpine (Alpine Linux)
# - 8.0-noble-chiseled (Ubuntu 24.04 Chiseled)
# - 8.0-azurelinux3.0 (Azure Linux)
# - 9.0-bookworm-slim (Debian 12)
# - 9.0-noble (Ubuntu 24.04)
# - 9.0-alpine (Alpine Linux)
# - 9.0-noble-chiseled (Ubuntu 24.04 Chiseled)
# - 9.0-azurelinux3.0 (Azure Linux)
# Uses the .NET runtime image for running the application
FROM mcr.microsoft.com/dotnet/aspnet:8.0-bookworm-slim AS final

# Install system packages if needed (uncomment and modify as needed)
# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     ca-certificates \
#     libgdiplus \
#     && rm -rf /var/lib/apt/lists/*

# Install additional .NET tools if needed (uncomment and modify as needed)
# RUN dotnet tool install --global dotnet-ef --version 8.0.0
# ENV PATH="$PATH:/root/.dotnet/tools"

WORKDIR /app

# Copy published application from build stage
COPY --from=build /app/publish .

# Copy additional files if needed (uncomment and modify as needed)
# COPY ./config/appsettings.Production.json .
# COPY ./certificates/ ./certificates/

# Set environment variables
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS=http://+:8080

# Add custom environment variables if needed (uncomment and modify as needed)
# ENV CONNECTIONSTRINGS__DEFAULTCONNECTION="your-connection-string"
# ENV FEATURE_FLAG_ENABLED=true

# Configure SSL/TLS certificates if needed (uncomment and modify as needed)
# ENV ASPNETCORE_Kestrel__Certificates__Default__Path=/app/certificates/app.pfx
# ENV ASPNETCORE_Kestrel__Certificates__Default__Password=your_password

# Expose the port the application listens on
EXPOSE 8080
# EXPOSE 8081  # Uncomment if using HTTPS

# Install curl for health checks if not already present
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Configure health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Create volumes for persistent data if needed (uncomment and modify as needed)
# VOLUME ["/app/data", "/app/logs"]

# Switch to non-root user for security
USER $APP_UID

# Set the entry point for the application
ENTRYPOINT ["dotnet", "YourProject.dll"]
```
