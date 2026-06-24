# Add additional dependencies

> Extracted from `create-spring-boot-java-project.prompt.md`.

## Add additional dependencies

- Insert `springdoc-openapi-starter-webmvc-ui` and `archunit-junit5` dependency into `pom.xml` file

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.8.6</version>
</dependency>
<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.2.1</version>
  <scope>test</scope>
</dependency>
```
