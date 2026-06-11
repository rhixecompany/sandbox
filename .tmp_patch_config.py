from pathlib import Path
p = Path(r'C:\Users\Alexa\AppData\Local\hermes\config.yaml')
text = p.read_text(encoding='utf-8')
replace_start = text.index('mcp_servers:\n')
replace_end = text.index('platform_toolsets:\n')
patch = '''mcp_servers:
  mcp-docker:
    args:
      - mcp
      - gateway
      - run
      - --profile
      - adminbot
    command: docker
    enabled: true
    env:
      LOCALAPPDATA: C:\\Users\\Alexa\\AppData\\Local
      ProgramData: C:\\ProgramData
      ProgramFiles: C:\\Program Files
      ProgramFiles(x86): C:\\Program Files (x86)
      USERPROFILE: C:\\Users\\Alexa
  filesystem:
    command: npx
    args:
      - -y
      - '@modelcontextprotocol/server-filesystem'
      - C:/Users/Alexa/Desktop/SandBox
    tools:
      prompts: false
      resources: false
  fetch:
    command: npx
    args:
      - -y
      - mcp-server-fetch-typescript
    tools:
      prompts: false
      resources: false
  memory:
    command: npx
    args:
      - -y
      - '@modelcontextprotocol/server-memory'
    tools:
      prompts: false
      resources: false
  sequential-thinking:
    command: npx
    args:
      - -y
      - '@modelcontextprotocol/server-sequential-thinking'
    tools:
      include:
        - sequentialthinking
      prompts: false
      resources: false
  github:
    command: npx
    args:
      - -y
      - '@modelcontextprotocol/server-github'
    tools:
      prompts: false
      resources: false
  playwright:
    command: npx
    args:
      - -y
      - '@playwright/mcp@latest'
    tools:
      include: []
      prompts: false
      resources: false
  ast-grep:
    command: npx
    args:
      - -y
      - '@notprolands/ast-grep-mcp'
    tools:
      include: []
      prompts: false
      resources: false
  code-sandbox:
    command: npx
    args:
      - -y
      - node-code-sandbox-mcp
    tools:
      include: []
      prompts: false
      resources: false
'''
new = text[:replace_start] + patch + text[replace_end:]
p.write_text(new, encoding='utf-8')
print('patched')
