---
title: All Repo Docker Setup
description: Prompt for all repo docker setup
date: '2026-08-25'
tags:
- prompt
version: 1.0.0
author: Hermes Agent
---

for each repo	in the list of repositories by rhixecompany, perform the following steps:
1. Clone the repository to your local machine at <./projects> using the command:
```
```bash
git clone <repository_url>
```
```

2. Navigate into the cloned repository directory:
```
```bash
cd <repository_name>
```
```

3. Check if a Dockerfile exists in the repository. If it doesn`t create it, If it does, debug,fix update to a smaller image and build the Docker image, security scan, suggest,create,implement a cleanup plan, fix all container errors using the command:
```bash
```
docker build -t <image_name> .
```
```

4. If the Dockerfile does not exist, check if a docker-compose.yml file exists. If it does, build the Docker image using the command:
```bash
```
docker-compose build
```
```

5. If neither a Dockerfile nor a docker-compose.yml file exists, log a message indicating that no Docker configuration was found for the repository and create a log file named `docker_setup.log` in the root directory of the repository with the message:
```
No Docker configuration found for this repository.
```text
```

```

6. You will clean up all unused Docker resources with a specific plan:

Remove unused containers
Remove unused images
Remove unused volumes
Remove unused build caches
Report what was freed
