# Your Approach

> Extracted from `java-add-graalvm-native-image-support.prompt.md`.

## Your Approach

Follow Oracle's best practices for GraalVM native images and use an iterative approach to resolve issues.

### Step 1: Analyze the Project

- Check if `pom.xml` exists (Maven) or `build.gradle`/`build.gradle.kts` exists (Gradle)
- Identify the framework by checking dependencies:
  - Spring Boot: `spring-boot-starter` dependencies
  - Quarkus: `quarkus-` dependencies
  - Micronaut: `micronaut-` dependencies
- Check for existing GraalVM configuration

### Step 2: Add Native Image Support

#### For Maven Projects

Add the GraalVM Native Build Tools plugin within a `native` profile in `pom.xml`:

```xml
<profiles>
  <profile>
    <id>native</id>
    <build>
      <plugins>
        <plugin>
          <groupId>org.graalvm.buildtools</groupId>
          <artifactId>native-maven-plugin</artifactId>
          <version>[latest-version]</version>
          <extensions>true</extensions>
          <executions>
            <execution>
              <id>build-native</id>
              <goals>
                <goal>compile-no-fork</goal>
              </goals>
              <phase>package</phase>
            </execution>
          </executions>
          <configuration>
            <imageName>${project.artifactId}</imageName>
            <mainClass>${main.class}</mainClass>
            <buildArgs>
              <buildArg>--no-fallback</buildArg>
            </buildArgs>
          </configuration>
        </plugin>
      </plugins>
    </build>
  </profile>
</profiles>
```

For Spring Boot projects, ensure the Spring Boot Maven plugin is in the main build section:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-maven-plugin</artifactId>
    </plugin>
  </plugins>
</build>
```

#### For Gradle Projects

Add the GraalVM Native Build Tools plugin to `build.gradle`:

```groovy
plugins {
  id 'org.graalvm.buildtools.native' version '[latest-version]'
}

graalvmNative {
  binaries {
    main {
      imageName = project.name
      mainClass = application.mainClass.get()
      buildArgs.add('--no-fallback')
    }
  }
}
```

Or for Kotlin DSL (`build.gradle.kts`):

```kotlin
plugins {
  id("org.graalvm.buildtools.native") version "[latest-version]"
}

graalvmNative {
  binaries {
    named("main") {
      imageName.set(project.name)
      mainClass.set(application.mainClass.get())
      buildArgs.add("--no-fallback")
    }
  }
}
```

### Step 3: Build the Native Image

Run the appropriate build command:

**Maven:**

```sh
mvn -Pnative native:compile
```

**Gradle:**

```sh
./gradlew nativeCompile
```

**Spring Boot (Maven):**

```sh
mvn -Pnative spring-boot:build-image
```

**Quarkus (Maven):**

```sh
./mvnw package -Pnative
```

**Micronaut (Maven):**

```sh
./mvnw package -Dpackaging=native-image
```

### Step 4: Analyze Build Errors

Common issues and solutions:

#### Reflection Issues

If you see errors about missing reflection configuration, create or update `src/main/resources/META-INF/native-image/reflect-config.json`:

```json
[
  {
    "name": "com.example.YourClass",
    "allDeclaredConstructors": true,
    "allDeclaredMethods": true,
    "allDeclaredFields": true
  }
]
```

#### Resource Access Issues

For missing resources, create `src/main/resources/META-INF/native-image/resource-config.json`:

```json
{
  "resources": {
    "includes": [
      { "pattern": "application.properties" },
      { "pattern": ".*\\.yml" },
      { "pattern": ".*\\.yaml" }
    ]
  }
}
```

#### JNI Issues

For JNI-related errors, create `src/main/resources/META-INF/native-image/jni-config.json`:

```json
[
  {
    "name": "com.example.NativeClass",
    "methods": [
      {
        "name": "nativeMethod",
        "parameterTypes": ["java.lang.String"]
      }
    ]
  }
]
```

#### Dynamic Proxy Issues

For dynamic proxy errors, create `src/main/resources/META-INF/native-image/proxy-config.json`:

```json
[["com.example.Interface1", "com.example.Interface2"]]
```

### Step 5: Iterate Until Success

- After each fix, rebuild the native image
- Analyze new errors and apply appropriate fixes
- Use the GraalVM tracing agent to automatically generate configuration:
  ```sh
  java -agentlib:native-image-agent=config-output-dir=src/main/resources/META-INF/native-image -jar target/app.jar
  ```
- Continue until the build succeeds without errors

### Step 6: Verify the Native Image

Once built successfully:

- Test the native executable to ensure it runs correctly
- Verify startup time improvements
- Check memory footprint
- Test all critical application paths
