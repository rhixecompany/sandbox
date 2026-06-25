package com.example.mcp.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Configuration for the Java MCP Server.
 * <p>
 * Values are loaded from environment variables with sensible defaults.
 * This allows the server to be configured without code changes,
 * suitable for containerized and cloud deployments.
 */
public final class Config {

    private static final Logger logger = LoggerFactory.getLogger(Config.class);

    /** Default server name */
    private static final String DEFAULT_SERVER_NAME = "java-mcp-server";

    /** Default server version */
    private static final String DEFAULT_SERVER_VERSION = "1.0.0";

    /** Default log level if not set via env */
    private static final String DEFAULT_LOG_LEVEL = "INFO";

    private final String serverName;
    private final String serverVersion;
    private final String logLevel;
    private final int port;
    private final boolean stdioTransport;

    private Config(Builder builder) {
        this.serverName = builder.serverName;
        this.serverVersion = builder.serverVersion;
        this.logLevel = builder.logLevel;
        this.port = builder.port;
        this.stdioTransport = builder.stdioTransport;
    }

    /**
     * Loads configuration from environment variables.
     *
     * @return a fully populated Config instance
     */
    public static Config load() {
        Builder builder = new Builder();

        builder.serverName(getEnvOrDefault("MCP_SERVER_NAME", DEFAULT_SERVER_NAME));
        builder.serverVersion(getEnvOrDefault("MCP_SERVER_VERSION", DEFAULT_SERVER_VERSION));
        builder.logLevel(getEnvOrDefault("MCP_LOG_LEVEL", DEFAULT_LOG_LEVEL));
        builder.port(getEnvOrDefaultInt("MCP_PORT", 8080));
        builder.stdioTransport(getEnvOrDefaultBool("MCP_STDIO_TRANSPORT", true));

        Config config = builder.build();
        logger.debug("Configuration loaded: {}", config);
        return config;
    }

    /**
     * Loads configuration with overrides (useful for testing).
     *
     * @param overrides map of config key -> value overrides
     * @return a fully populated Config instance
     */
    public static Config loadWithOverrides(java.util.Map<String, String> overrides) {
        Builder builder = new Builder();

        builder.serverName(overrides.getOrDefault("serverName", getEnvOrDefault("MCP_SERVER_NAME", DEFAULT_SERVER_NAME)));
        builder.serverVersion(overrides.getOrDefault("serverVersion", getEnvOrDefault("MCP_SERVER_VERSION", DEFAULT_SERVER_VERSION)));
        builder.logLevel(overrides.getOrDefault("logLevel", getEnvOrDefault("MCP_LOG_LEVEL", DEFAULT_LOG_LEVEL)));
        builder.port(Integer.parseInt(overrides.getOrDefault("port", String.valueOf(getEnvOrDefaultInt("MCP_PORT", 8080)))));
        builder.stdioTransport(Boolean.parseBoolean(overrides.getOrDefault("stdioTransport", String.valueOf(getEnvOrDefaultBool("MCP_STDIO_TRANSPORT", true)))));

        return builder.build();
    }

    // ---- Getters ----

    public String getServerName() {
        return serverName;
    }

    public String getServerVersion() {
        return serverVersion;
    }

    public String getLogLevel() {
        return logLevel;
    }

    public int getPort() {
        return port;
    }

    public boolean isStdioTransport() {
        return stdioTransport;
    }

    @Override
    public String toString() {
        return "Config{"
                + "serverName='" + serverName + '\''
                + ", serverVersion='" + serverVersion + '\''
                + ", logLevel='" + logLevel + '\''
                + ", port=" + port
                + ", stdioTransport=" + stdioTransport
                + '}';
    }

    // ---- Builder ----

    public static class Builder {
        private String serverName = DEFAULT_SERVER_NAME;
        private String serverVersion = DEFAULT_SERVER_VERSION;
        private String logLevel = DEFAULT_LOG_LEVEL;
        private int port = 8080;
        private boolean stdioTransport = true;

        public Builder serverName(String serverName) {
            this.serverName = serverName;
            return this;
        }

        public Builder serverVersion(String serverVersion) {
            this.serverVersion = serverVersion;
            return this;
        }

        public Builder logLevel(String logLevel) {
            this.logLevel = logLevel;
            return this;
        }

        public Builder port(int port) {
            this.port = port;
            return this;
        }

        public Builder stdioTransport(boolean stdioTransport) {
            this.stdioTransport = stdioTransport;
            return this;
        }

        public Config build() {
            return new Config(this);
        }
    }

    // ---- Helpers ----

    private static String getEnvOrDefault(String key, String defaultValue) {
        String value = System.getenv(key);
        return value != null && !value.isBlank() ? value : defaultValue;
    }

    private static int getEnvOrDefaultInt(String key, int defaultValue) {
        String value = System.getenv(key);
        if (value != null && !value.isBlank()) {
            try {
                return Integer.parseInt(value);
            } catch (NumberFormatException e) {
                logger.warn("Invalid integer for env var {}: '{}', using default {}", key, value, defaultValue);
            }
        }
        return defaultValue;
    }

    private static boolean getEnvOrDefaultBool(String key, boolean defaultValue) {
        String value = System.getenv(key);
        if (value != null && !value.isBlank()) {
            return Boolean.parseBoolean(value);
        }
        return defaultValue;
    }
}
