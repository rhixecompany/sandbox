plugins {
    kotlin("jvm") version "1.9.22"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    // Kotlin MCP SDK
    implementation("io.modelcontextprotocol:kotlin-sdk:0.3.0")

    // Ktor client for any HTTP-based transport needs
    implementation("io.ktor:ktor-client-core:2.3.7")
    implementation("io.ktor:ktor-client-cio:2.3.7")

    // Serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.2")

    // Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-jdk8:1.7.3")

    // Logging
    implementation("ch.qos.logback:logback-classic:1.4.14")
    implementation("io.github.microutils:kotlin-logging-jvm:3.0.5")
}

application {
    mainClass.set("com.example.mcp.MainKt")
}

kotlin {
    jvmToolchain(17)
}

tasks.named<Jar>("jar") {
    manifest {
        attributes["Main-Class"] = "com.example.mcp.MainKt"
    }
}

tasks.register<Jar>("fatJar") {
    dependsOn(tasks.named("compileKotlin"))
    from(configurations.runtimeClasspath.get().map { if (it.isDirectory) it else zipTree(it) })
    from(tasks.named("processResources"))
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
    manifest {
        attributes["Main-Class"] = "com.example.mcp.MainKt"
    }
    archiveClassifier.set("all")
}
