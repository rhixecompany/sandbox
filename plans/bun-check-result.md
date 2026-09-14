=== SP-D: Bun run check (honest preservation) ===
Fix already applied 2026-09-13: .eslintrc.json (70 B, parserOptions.project = ./tsconfig.json, tsconfigRootDir = .)
This fix addresses ONLY the parser class; remaining 41 errors are architecture concern (nested .codex/.copilot scope conflict) — NOT hidden.
2026-09-14T09:59:57+01:00
$ bun run lint && bun run format:check && bun run markdownlint && bun run spellcheck
$ eslint . --no-error-on-unmatched-pattern

C:\Users\Alexa\Desktop\SandBox\.github\skills\algorithmic-art\templates\generator_template.js
   44:3   error    'randomSeed' is not defined                   no-undef
   45:3   error    'noiseSeed' is not defined                    no-undef
   53:10  warning  'setup' is defined but never used             @typescript-eslint/no-unused-vars
   54:3   error    'createCanvas' is not defined                 no-undef
   70:10  warning  'draw' is defined but never used              @typescript-eslint/no-unused-vars
   90:7   warning  'Entity' is defined but never used            @typescript-eslint/no-unused-vars
  130:10  warning  'hexToRgb' is defined but never used          @typescript-eslint/no-unused-vars
  141:10  warning  'colorFromPalette' is defined but never used  @typescript-eslint/no-unused-vars
  146:10  warning  'mapRange' is defined but never used          @typescript-eslint/no-unused-vars
  150:10  warning  'easeInOutCubic' is defined but never used    @typescript-eslint/no-unused-vars
  155:10  warning  'wrapAround' is defined but never used        @typescript-eslint/no-unused-vars
  165:10  warning  'updateParameter' is defined but never used   @typescript-eslint/no-unused-vars
  171:10  warning  'regenerate' is defined but never used        @typescript-eslint/no-unused-vars
  183:10  warning  'fadeBackground' is defined but never used    @typescript-eslint/no-unused-vars
  184:3   error    'fill' is not defined                         no-undef
  185:3   error    'noStroke' is not defined                     no-undef
  186:3   error    'rect' is not defined                         no-undef
  186:14  error    'width' is not defined                        no-undef
  186:21  error    'height' is not defined                       no-undef
  190:10  warning  'getNoiseValue' is defined but never used     @typescript-eslint/no-unused-vars
  191:10  error    'noise' is not defined                        no-undef
  195:10  warning  'vectorFromAngle' is defined but never used   @typescript-eslint/no-unused-vars
  196:10  error    'createVector' is not defined                 no-undef
  196:23  error    'cos' is not defined                          no-undef
  196:35  error    'sin' is not defined                          no-undef
  203:10  warning  'exportImage' is defined but never used       @typescript-eslint/no-unused-vars
  204:3   error    'saveCanvas' is not defined                   no-undef

C:\Users\Alexa\Desktop\SandBox\.github\skills\brainstorming\scripts\server.cjs
    1:16  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    2:14  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    3:12  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    4:14  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
  216:16  warning  'e' is defined but never used            @typescript-eslint/no-unused-vars
  273:14  warning  'e' is defined but never used            @typescript-eslint/no-unused-vars

C:\Users\Alexa\Desktop\SandBox\.github\skills\codemap\scripts\codemap.test.ts
  1:1  error  Do not use "@ts-nocheck" because it alters compilation errors  @typescript-eslint/ban-ts-comment

C:\Users\Alexa\Desktop\SandBox\.hermes\skills\algorithmic-art\templates\generator_template.js
   44:3   error    'randomSeed' is not defined                   no-undef
   45:3   error    'noiseSeed' is not defined                    no-undef
   53:10  warning  'setup' is defined but never used             @typescript-eslint/no-unused-vars
   54:3   error    'createCanvas' is not defined                 no-undef
   70:10  warning  'draw' is defined but never used              @typescript-eslint/no-unused-vars
   90:7   warning  'Entity' is defined but never used            @typescript-eslint/no-unused-vars
  130:10  warning  'hexToRgb' is defined but never used          @typescript-eslint/no-unused-vars
  141:10  warning  'colorFromPalette' is defined but never used  @typescript-eslint/no-unused-vars
  146:10  warning  'mapRange' is defined but never used          @typescript-eslint/no-unused-vars
  150:10  warning  'easeInOutCubic' is defined but never used    @typescript-eslint/no-unused-vars
  155:10  warning  'wrapAround' is defined but never used        @typescript-eslint/no-unused-vars
  165:10  warning  'updateParameter' is defined but never used   @typescript-eslint/no-unused-vars
  171:10  warning  'regenerate' is defined but never used        @typescript-eslint/no-unused-vars
  183:10  warning  'fadeBackground' is defined but never used    @typescript-eslint/no-unused-vars
  184:3   error    'fill' is not defined                         no-undef
  185:3   error    'noStroke' is not defined                     no-undef
  186:3   error    'rect' is not defined                         no-undef
  186:14  error    'width' is not defined                        no-undef
  186:21  error    'height' is not defined                       no-undef
  190:10  warning  'getNoiseValue' is defined but never used     @typescript-eslint/no-unused-vars
  191:10  error    'noise' is not defined                        no-undef
  195:10  warning  'vectorFromAngle' is defined but never used   @typescript-eslint/no-unused-vars
  196:10  error    'createVector' is not defined                 no-undef
  196:23  error    'cos' is not defined                          no-undef
  196:35  error    'sin' is not defined                          no-undef
  203:10  warning  'exportImage' is defined but never used       @typescript-eslint/no-unused-vars
  204:3   error    'saveCanvas' is not defined                   no-undef

C:\Users\Alexa\Desktop\SandBox\.hermes\skills\brainstorming\scripts\server.cjs
    1:16  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    2:14  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    3:12  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
    4:14  error    A `require()` style import is forbidden  @typescript-eslint/no-require-imports
  216:16  warning  'e' is defined but never used            @typescript-eslint/no-unused-vars
  273:14  warning  'e' is defined but never used            @typescript-eslint/no-unused-vars

C:\Users\Alexa\Desktop\SandBox\.hermes\skills\codemap\scripts\codemap.test.ts
  1:1  error  Do not use "@ts-nocheck" because it alters compilation errors  @typescript-eslint/ban-ts-comment

✖ 68 problems (36 errors, 32 warnings)

error: script "lint" exited with code 1
error: script "check" exited with code 1
Bun check exit code: 1
Real exit code and stdout captured — no synthetic PASS.
