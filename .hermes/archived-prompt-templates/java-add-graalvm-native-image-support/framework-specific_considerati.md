# Framework-Specific Considerations

> Extracted from `java-add-graalvm-native-image-support.prompt.md`.

## Framework-Specific Considerations

### Spring Boot

- Spring Boot 3.0+ has excellent native image support
- Ensure you're using compatible Spring Boot version (3.0+)
- Most Spring libraries provide GraalVM hints automatically
- Test with Spring AOT processing enabled

**When to Add Custom RuntimeHints:**

Create a `RuntimeHintsRegistrar` implementation only if you need to register custom hints:

```java
import org.springframework.aot.hint.RuntimeHints;
import org.springframework.aot.hint.RuntimeHintsRegistrar;

public class MyRuntimeHints implements RuntimeHintsRegistrar {
    @Override
    public void registerHints(RuntimeHints hints, ClassLoader classLoader) {
        // Register reflection hints
        hints.reflection().registerType(
            MyClass.class,
            hint -> hint.withMembers(MemberCategory.INVOKE_DECLARED_CONSTRUCTORS,
                                     MemberCategory.INVOKE_DECLARED_METHODS)
        );

        // Register resource hints
        hints.resources().registerPattern("custom-config/*.properties");

        // Register serialization hints
        hints.serialization().registerType(MySerializableClass.class);
    }
}
```

Register it in your main application class:

```java
@SpringBootApplication
@ImportRuntimeHints(MyRuntimeHints.class)
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**Common Spring Boot Native Image Issues:**

1. **Logback Configuration**: Add to `application.properties`:

   ```properties
   # Disable Logback's shutdown hook in native images
   logging.register-shutdown-hook=false
   ```

   If using custom Logback configuration, ensure `logback-spring.xml` is in resources and add to `RuntimeHints`:

   ```java
   hints.resources().registerPattern("logback-spring.xml");
   hints.resources().registerPattern("org/springframework/boot/logging/logback/*.xml");
   ```

2. **Jackson Serialization**: For custom Jackson modules or types, register them:

   ```java
   hints.serialization().registerType(MyDto.class);
   hints.reflection().registerType(
       MyDto.class,
       hint -> hint.withMembers(
           MemberCategory.DECLARED_FIELDS,
           MemberCategory.INVOKE_DECLARED_CONSTRUCTORS
       )
   );
   ```

   Add Jackson mix-ins to reflection hints if used:

   ```java
   hints.reflection().registerType(MyMixIn.class);
   ```

3. **Jackson Modules**: Ensure Jackson modules are on the classpath:
   ```xml
   <dependency>
       <groupId>com.fasterxml.jackson.datatype</groupId>
       <artifactId>jackson-datatype-jsr310</artifactId>
   </dependency>
   ```

### Quarkus

- Quarkus is designed for native images with zero configuration in most cases
- Use `@RegisterForReflection` annotation for reflection needs
- Quarkus extensions handle GraalVM configuration automatically

**Common Quarkus Native Image Tips:**

1. **Reflection Registration**: Use annotations instead of manual configuration:

   ```java
   @RegisterForReflection(targets = {MyClass.class, MyDto.class})
   public class ReflectionConfiguration {
   }
   ```

   Or register entire packages:

   ```java
   @RegisterForReflection(classNames = {"com.example.package.*"})
   ```

2. **Resource Inclusion**: Add to `application.properties`:

   ```properties
   quarkus.native.resources.includes=config/*.json,templates/**
   quarkus.native.additional-build-args=--initialize-at-run-time=com.example.RuntimeClass
   ```

3. **Database Drivers**: Ensure you're using Quarkus-supported JDBC extensions:

   ```xml
   <dependency>
       <groupId>io.quarkus</groupId>
       <artifactId>quarkus-jdbc-postgresql</artifactId>
   </dependency>
   ```

4. **Build-Time vs Runtime Initialization**: Control initialization with:

   ```properties
   quarkus.native.additional-build-args=--initialize-at-build-time=com.example.BuildTimeClass
   quarkus.native.additional-build-args=--initialize-at-run-time=com.example.RuntimeClass
   ```

5. **Container Image Build**: Use Quarkus container-image extensions:
   ```properties
   quarkus.native.container-build=true
   quarkus.native.builder-image=mandrel
   ```

### Micronaut

- Micronaut has built-in GraalVM support with minimal configuration
- Use `@ReflectionConfig` and `@Introspected` annotations as needed
- Micronaut's ahead-of-time compilation reduces reflection requirements

**Common Micronaut Native Image Tips:**

1. **Bean Introspection**: Use `@Introspected` for POJOs to avoid reflection:

   ```java
   @Introspected
   public class MyDto {
       private String name;
       private int value;
       // getters and setters
   }
   ```

   Or enable package-wide introspection in `application.yml`:

   ```yaml
   micronaut:
     introspection:
       packages:
         - com.example.dto
   ```

2. **Reflection Configuration**: Use declarative annotations:

   ```java
   @ReflectionConfig(
       type = MyClass.class,
       accessType = ReflectionConfig.AccessType.ALL_DECLARED_CONSTRUCTORS
   )
   public class MyConfiguration {
   }
   ```

3. **Resource Configuration**: Add resources to native image:

   ```java
   @ResourceConfig(
       includes = {"application.yml", "logback.xml"}
   )
   public class ResourceConfiguration {
   }
   ```

4. **Native Image Configuration**: In `build.gradle`:

   ```groovy
   graalvmNative {
       binaries {
           main {
               buildArgs.add("--initialize-at-build-time=io.micronaut")
               buildArgs.add("--initialize-at-run-time=io.netty")
               buildArgs.add("--report-unsupported-elements-at-runtime")
           }
       }
   }
   ```

5. **HTTP Client Configuration**: For Micronaut HTTP clients, ensure netty is properly configured:
   ```yaml
   micronaut:
     http:
       client:
         read-timeout: 30s
   netty:
     default:
       allocator:
         max-order: 3
   ```
