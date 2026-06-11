export = eslint_plugin_drizzle;

declare const eslint_plugin_drizzle: {
  configs: {
    all: {
      env: {
        es2024: boolean;
      };
      parserOptions: {
        ecmaVersion: string;
        sourceType: string;
      };
      plugins: string[];
      rules: {
        "drizzle/enforce-delete-with-where": string;
        "drizzle/enforce-update-with-where": string;
      };
    };
    recommended: {
      env: {
        es2024: boolean;
      };
      parserOptions: {
        ecmaVersion: string;
        sourceType: string;
      };
      plugins: string[];
      rules: {
        "drizzle/enforce-delete-with-where": string;
        "drizzle/enforce-update-with-where": string;
      };
    };
  };
  meta: {
    name: string;
    version: string;
  };
  rules: {
    "enforce-delete-with-where": {
      create: unknown;
      defaultOptions: {
        drizzleObjectName: unknown[];
      }[];
      meta: {
        docs: {
          description: string;
          url: string;
        };
        fixable: string;
        messages: {
          enforceDeleteWithWhere: string;
        };
        schema: {
          additionalProperties: boolean;
          properties: {
            drizzleObjectName: {
              type: string[];
            };
          };
          type: string;
        }[];
        type: string;
      };
      name: string;
    };
    "enforce-update-with-where": {
      create: unknown;
      defaultOptions: {
        drizzleObjectName: unknown[];
      }[];
      meta: {
        docs: {
          description: string;
          url: string;
        };
        fixable: string;
        messages: {
          enforceUpdateWithWhere: string;
        };
        schema: {
          additionalProperties: boolean;
          properties: {
            drizzleObjectName: {
              type: string[];
            };
          };
          type: string;
        }[];
        type: string;
      };
      name: string;
    };
  };
};
