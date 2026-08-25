---
title: Goal
description: Prompt for goal
date: '2026-08-25'
tags:
- prompt
version: 1.0.0
author: Hermes Agent
---
# Table of Contents

- [Goal](#goal)
- [Check Java version](#check-java-version)
- [Download Spring Boot project template](#download-spring-boot-project-template)
- [Unzip the downloaded file](#unzip-the-downloaded-file)
- [Remove the downloaded zip file](#remove-the-downloaded-zip-file)
- [Change directory to the project root](#change-directory-to-the-project-root)
- [Add additional dependencies](#add-additional-dependencies)
- [Add SpringDoc, Redis, JPA and MongoDB configurations](#add-springdoc-redis-jpa-and-mongodb-configurations)
- [Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services](#add-`docker-composeyaml`-with-redis-postgresql-and-mongodb-services)
- [Add `.gitignore` file](#add-`gitignore`-file)
- [Run Maven test command](#run-maven-test-command)
- [Run Maven run command (Optional)](#run-maven-run-command-optional)
- [Let's do this step by step](#let's-do-this-step-by-step)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Check Java version](#check-java-version)
- [Download Spring Boot project template](#download-spring-boot-project-template)
- [Unzip the downloaded file](#unzip-the-downloaded-file)
- [Remove the downloaded zip file](#remove-the-downloaded-zip-file)
- [Change directory to the project root](#change-directory-to-the-project-root)
- [Add additional dependencies](#add-additional-dependencies)
- [Add SpringDoc, Redis, JPA and MongoDB configurations](#add-springdoc-redis-jpa-and-mongodb-configurations)
- [Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services](#add-`docker-composeyaml`-with-redis-postgresql-and-mongodb-services)
- [Add `.gitignore` file](#add-`gitignore`-file)
- [Run Maven test command](#run-maven-test-command)
- [Run Maven run command (Optional)](#run-maven-run-command-optional)
- [Let's do this step by step](#let's-do-this-step-by-step)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)




## Goal

Create Spring Boot Java Project Skeleton.

## Create Spring Boot Java project prompt- Please make sure you have the following software installed on your system: - Java 21 - Docker - Docker Compose- If you need to custom the project name, please change the `artifactId` and the `packageName` in [download-spring-boot-project-template](./create-spring-boot-java-project.prompt.md)- If you need to update the Spring Boot version, please change the `bootVersion` in [download-spring-boot-project-template](./create-spring-boot-java-project.prompt.md#download-spring-boot-project-template)

## Check Java version

- Run following command in terminal and check the version of Java

```shell
java -version
```

## Download Spring Boot project template

- Run following command in terminal to download a Spring Boot project template

```shell
curl https://start.spring.io/starter.zip \
-d artifactId=${input:projectName:demo-java} \
-d bootVersion=3.4.5 \
-d dependencies=lombok,configuration-processor,web,data-jpa,postgresql,data-redis,data-mongodb,validation,cache,testcontainers \
-d javaVersion=21 \
-d packageName=com.example \
-d packaging=jar \
-d type=maven-project \
-o starter.zip
```

## Unzip the downloaded file

- Run following command in terminal to unzip the downloaded file

```shell
unzip starter.zip -d ./${input:projectName:demo-java}
```

## Remove the downloaded zip file

- Run following command in terminal to delete the downloaded zip file

```shell
rm -f starter.zip
```

## Change directory to the project root

- Run following command in terminal to change directory to the project root

```shell
cd ${input:projectName:demo-java}
```

## Add additional dependencies

- Insert `springdoc-openapi-starter-webmvc-ui` and `archunit-junit5` dependency into `pom.xml` file```xml<dependency> <groupId

> org.springdoc</groupId
> <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId
> <version>2.8.6</version></dependency><dependency
> <groupId>com.tngtech.archunit</groupId
> <artifactId>archunit-junit5</artifactId
> <version>1.2.1</version
> <scope>test</scope></dependency>```

## Add SpringDoc, Redis, JPA and MongoDB configurations

> - Insert SpringDoc configurations into `application.properties` file>
>
> # SpringDoc configurations
>
> **Full content:**

## Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services

- Create `docker-compose.yaml` at project root and add following services: `redis:6`, `postgresql:17` and `mongo:8`. - redis service should have - password `rootroot` - mapping port 6379 to 6379 - mounting volume `./redis_data` to `/data` - postgresql service should have - password `rootroot` - mapping port 5432 to 5432 - mounting volume `./postgres_data` to `/var/lib/postgresql/data` - mongo service should have - initdb root username `root` - initdb root password `rootroot` - mapping port 27017 to 27017 - mounting volume `./mongo_data` to `/data/db`

## Add `.gitignore` file

- Insert `redis_data`, `postgres_data` and `mongo_data` directories in `.gitignore` file

## Run Maven test command

- Run maven clean test command to check if the project is working

```shell
./mvnw clean test
```

## Run Maven run command (Optional)

- (Optional) `docker-compose up -d` to start the services, `./mvnw spring-boot:run` to run the Spring Boot project, `docker-compose rm -sf` to stop the services.

## Let's do this step by step

## Template References

Templates in `templates/create-spring-boot-java-project/`:- `add_additional_dependenci.md`- `add_docker-composeyaml_wi.md`- `add_springdoc_redis_jpa_a.md`- `download_spring_boot_proj.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings .
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`create-agentsmd.prompt.md`](create-agentsmd.prompt.md)
- [`create-architectural-decision-record.prompt.md`](create-architectural-decision-record.prompt.md)
- [`create-github-action-workflow-specification.prompt.md`](create-github-action-workflow-specification.prompt.md)
- [`create-github-issue-feature-from-specification.prompt.md`](create-github-issue-feature-from-specification.prompt.md)
- [`create-github-issues-feature-from-implementation-plan.prompt.md`](create-github-issues-feature-from-implementation-plan.prompt.md)
- [`create-github-issues-for-unmet-specification-requirements.prompt.md`](create-github-issues-for-unmet-specification-requirements.prompt.md)
- [`create-github-pull-request-from-specification.prompt.md`](create-github-pull-request-from-specification.prompt.md)
- [`create-implementation-plan.prompt.md`](create-implementation-plan.prompt.md)
- [`create-llms.prompt.md`](create-llms.prompt.md)
- [`create-oo-component-documentation.prompt.md`](create-oo-component-documentation.prompt.md)
- [`create-readme.prompt.md`](create-readme.prompt.md)
- [`create-specification.prompt.md`](create-specification.prompt.md)
- [`create-spring-boot-kotlin-project.prompt.md`](create-spring-boot-kotlin-project.prompt.md)
- [`create-technical-spike.prompt.md`](create-technical-spike.prompt.md)
- [`create-tldr-page.prompt.md`](create-tldr-page.prompt.md)