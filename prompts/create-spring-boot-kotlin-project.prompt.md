---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create Spring Boot Kotlin project prompt
name: create-spring-boot-kotlin-project
description: "Create Spring Boot Kotlin Project Skeleton"
tags:
  - docker
  - generator
  - java
  - prompts
  - spring
  - docker
  - documentation
  - generator
  - java
  - kotlin
  - markdown
metadata:
  hermes:
    related_skills: []
    tags:
    - create-spring-boot-kotlin-project.prompt

trigger: create-spring-boot-kotlin-project

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - create-spring-boot-kotlin-project.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - create-spring-boot-kotlin-project.prompt

# Create Spring Boot Kotlin project prompt

- Please make sure you have the following software installed on your system:
  - Java 21
  - Docker
  - Docker Compose

- If you need to custom the project name, please change the `artifactId` and the `packageName` in [download-spring-boot-project-template](./create-spring-boot-kotlin-project.prompt.md#download-spring-boot-project-template)

- If you need to update the Spring Boot version, please change the `bootVersion` in [download-spring-boot-project-template](./create-spring-boot-kotlin-project.prompt.md#download-spring-boot-project-template)

## Check Java version

- Run following command in terminal and check the version of Java

```shell
java -version
```

## Download Spring Boot project template

- Run following command in terminal to download a Spring Boot project template

```shell
curl https://start.spring.io/starter.zip \
  -d artifactId=${input:projectName:demo-kotlin} \
  -d bootVersion=3.4.5 \
  -d dependencies=configuration-processor,webflux,data-r2dbc,postgresql,data-redis-reactive,data-mongodb-reactive,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d language=kotlin \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=gradle-project-kotlin \
  -o starter.zip
```

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

```shell
unzip starter.zip -d ./${input:projectName:demo-kotlin}
```

## Remove the downloaded zip file

- Run following command in terminal to delete the downloaded zip file

```shell
rm -f starter.zip
```

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

```shell
unzip starter.zip -d ./${input:projectName:demo-kotlin}
```

## Add additional dependencies

> - Insert `springdoc-openapi-starter-webmvc-ui` and `archunit-junit5` dependency 
> implementation("org.springdoc:springdoc-openapi-starter-webflux-ui:2.8.6")

> **Full content:** `templates/create-spring-boot-kotlin-project/add_additional_dependenci.md`

## Template References

Templates in `templates/create-spring-boot-kotlin-project/`:
- `add_additional_dependenci.md`
- `download_spring_boot_proj.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
