# Add SpringDoc, Redis, JPA and MongoDB configurations

> Extracted from `create-spring-boot-java-project.prompt.md`.

## Add SpringDoc, Redis, JPA and MongoDB configurations

- Insert SpringDoc configurations into `application.properties` file

```properties
# SpringDoc configurations
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

- Insert Redis configurations into `application.properties` file

```properties
# Redis configurations
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

- Insert JPA configurations into `application.properties` file

```properties
# JPA configurations
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=rootroot
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
```

- Insert MongoDB configurations into `application.properties` file

```properties
# MongoDB configurations
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```
