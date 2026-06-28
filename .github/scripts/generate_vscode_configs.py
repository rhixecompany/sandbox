"""
VS Code Workspace Configurator — Batch generate .vscode/ configs for all 29 repos.
Phase 2: Create missing .vscode/ directories.
Phase 3: Augment partial configs.
Phase 4: Validate all JSON.
"""

import json
import os
import subprocess

SANDBOX = r"C:\Users\Alexa\Desktop\SandBox"

# ─── Template Builders ───────────────────────────────────────────────────────

def settings_nextjs():
    """Next.js / React / TypeScript with Tailwind (no django-html leakage)"""
    return {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "files.associations": {"*.css": "tailwindcss"},
        "tailwindCSS.emmetCompletions": True,
        "tailwindCSS.includeLanguages": {
            "css": "css",
            "scss": "scss",
            "javascript": "jsx",
            "typescript": "tsx"
        },
        "[javascript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescriptreact]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[css]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[scss]": {"editor.defaultFormatter": "esbenp.prettier-vscode"}
    }


def settings_django():
    """Django / Python backend"""
    return {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "python.languageServer": "Pylance",
        "python.analysis.typeCheckingMode": "basic",
        "python.analysis.autoImportCompletions": True,
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
        "python-envs.alwaysUseUv": True,
        "python-envs.autoActivate": True,
        "python-envs.venvFolders": [".venv", "env", "venv", ".env", "envs", "venvs"],
        "files.associations": {
            "**/*.{txt,in}": "django-txt",
            "**/requirements/**/*.{txt,in}": "pip-requirements"
        },
        "[python]": {"editor.defaultFormatter": "ms-python.python", "editor.formatOnSave": True},
        "[html]": {"editor.defaultFormatter": "vscode.html-language-features"},
        "[django-html]": {"editor.defaultFormatter": "vscode.html-language-features"},
        "[css]": {"editor.defaultFormatter": "vscode.css-language-features"},
        "[javascript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_dualdjango_nextjs():
    """Django + Next.js dual-stack: merge Django + Next.js settings"""
    return {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "python.languageServer": "Pylance",
        "python.analysis.typeCheckingMode": "basic",
        "python.analysis.autoImportCompletions": True,
        "python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/Scripts/python.exe",
        "python-envs.alwaysUseUv": True,
        "python-envs.autoActivate": True,
        "python-envs.venvFolders": [".venv", "env", "venv", ".env", "envs", "venvs"],
        "files.associations": {
            "*.css": "tailwindcss",
            "**/*.{txt,in}": "django-txt",
            "**/requirements/**/*.{txt,in}": "pip-requirements"
        },
        "tailwindCSS.emmetCompletions": True,
        "tailwindCSS.includeLanguages": {
            "css": "css", "scss": "scss",
            "javascript": "jsx", "typescript": "tsx"
        },
        "[python]": {"editor.defaultFormatter": "ms-python.python", "editor.formatOnSave": True},
        "[django-html]": {"editor.defaultFormatter": "vscode.html-language-features"},
        "[javascript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescriptreact]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[css]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[scss]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[html]": {"editor.defaultFormatter": "vscode.html-language-features"}
    }


def settings_bun():
    """Bun / TypeScript scripts"""
    return {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "[typescript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[javascript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[shellscript]": {"editor.defaultFormatter": "foxundermoon.shell-format"}
    }


def settings_node():
    """Node.js"""
    return {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "[javascript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[typescript]": {"editor.defaultFormatter": "esbenp.prettier-vscode"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_python():
    """Pure Python standalone"""
    return {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
        "editor.inlineSuggest.enabled": True,
        "python.languageServer": "Pylance",
        "python.analysis.typeCheckingMode": "basic",
        "python.analysis.autoImportCompletions": True,
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
        "python-envs.alwaysUseUv": True,
        "python-envs.autoActivate": True,
        "python-envs.venvFolders": [".venv", "env", "venv", ".env", "envs", "venvs"],
        "[python]": {"editor.defaultFormatter": "ms-python.python", "editor.formatOnSave": True},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_go():
    """Go language"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
        "[go]": {"editor.defaultFormatter": "golang.go"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_rust():
    """Rust"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "editor.codeActionsOnSave": {"source.organizeImports": "explicit"},
        "[rust]": {"editor.defaultFormatter": "rust-lang.rust-analyzer"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_java():
    """Java"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "java.configuration.updateBuildConfiguration": "automatic",
        "[java]": {"editor.defaultFormatter": "redhat.java"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_kotlin():
    """Kotlin"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "[kotlin]": {"editor.defaultFormatter": "fwcd.kotlin"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_php():
    """PHP"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "[php]": {"editor.defaultFormatter": "bmewburn.vscode-intelephense-client"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_ruby():
    """Ruby"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "[ruby]": {"editor.defaultFormatter": "rebornix.ruby"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_swift():
    """Swift"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "[swift]": {"editor.defaultFormatter": "sswg.swift-lang"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


def settings_csharp():
    """C#"""
    return {
        "editor.formatOnSave": True,
        "editor.inlineSuggest.enabled": True,
        "[csharp]": {"editor.defaultFormatter": "ms-dotnettools.csharp"},
        "[json]": {"editor.defaultFormatter": "vscode.json-language-features"},
        "[jsonc]": {"editor.defaultFormatter": "vscode.json-language-features"}
    }


# ─── Launch.json Builders ────────────────────────────────────────────────────

def launch_nextjs():
    return {
        "version": "0.2.0",
        "configurations": [
            {"command": "npm run dev", "name": "Next.js: Dev Server", "request": "launch", "type": "node-terminal"},
            {"command": "npm run build", "name": "Next.js: Build", "request": "launch", "type": "node-terminal"},
            {"command": "npm run lint", "name": "Next.js: Lint", "request": "launch", "type": "node-terminal"},
            {"command": "npx tsc --noEmit", "name": "TypeScript: Type Check", "request": "launch", "type": "node-terminal"}
        ]
    }


def launch_nextjs_bun():
    return {
        "version": "0.2.0",
        "configurations": [
            {"command": "bun run dev", "name": "Next.js: Dev Server", "request": "launch", "type": "node-terminal"},
            {"command": "bun run build", "name": "Next.js: Build", "request": "launch", "type": "node-terminal"},
            {"command": "bun run lint", "name": "Next.js: Lint", "request": "launch", "type": "node-terminal"},
            {"command": "bun run type-check", "name": "TypeScript: Type Check", "request": "launch", "type": "node-terminal"},
            {"name": "Bun: Current File", "type": "node", "request": "launch", "runtimeExecutable": "bun", "program": "${file}", "console": "integratedTerminal"}
        ]
    }


def launch_django():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Django: Runserver", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/manage.py", "args": ["runserver"], "django": True, "justMyCode": True},
            {"name": "Django: Test", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/manage.py", "args": ["test", "--keepdb", "--verbosity=2"], "django": True, "justMyCode": True},
            {"name": "Python: Current File", "type": "debugpy", "request": "launch", "program": "${file}", "console": "integratedTerminal"}
        ]
    }


def launch_dualdjango_nextjs():
    """Django + Next.js combined launch configs"""
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Django: Runserver", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/backend/manage.py", "args": ["runserver"], "django": True, "justMyCode": True},
            {"name": "Django: Test", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/backend/manage.py", "args": ["test", "--keepdb", "--verbosity=2"], "django": True, "justMyCode": True},
            {"command": "npm run dev", "name": "Frontend: Dev Server", "request": "launch", "type": "node-terminal"},
            {"command": "npm run build", "name": "Frontend: Build", "request": "launch", "type": "node-terminal"},
            {"name": "Python: Current File", "type": "debugpy", "request": "launch", "program": "${file}", "console": "integratedTerminal"}
        ]
    }


def launch_dualdjango_node():
    """Django + Node.js (Express) combined"""
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Django: Runserver", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/manage.py", "args": ["runserver"], "django": True, "justMyCode": True},
            {"name": "Django: Test", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/manage.py", "args": ["test", "--keepdb", "--verbosity=2"], "django": True, "justMyCode": True},
            {"name": "Node.js: Current File", "type": "node", "request": "launch", "program": "${file}", "console": "integratedTerminal"},
            {"name": "Python: Current File", "type": "debugpy", "request": "launch", "program": "${file}", "console": "integratedTerminal"}
        ]
    }


def launch_bun():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Bun: Current File", "type": "node", "request": "launch", "runtimeExecutable": "bun", "program": "${file}", "console": "integratedTerminal"},
            {"name": "Bun: Run All Tests", "type": "node", "request": "launch", "runtimeExecutable": "bun", "runtimeArgs": ["test"], "console": "integratedTerminal"}
        ]
    }


def launch_node():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Node.js: Current File", "type": "node", "request": "launch", "program": "${file}", "console": "integratedTerminal"},
            {"name": "npm start", "type": "node", "request": "launch", "runtimeExecutable": "npm", "runtimeArgs": ["start"], "console": "integratedTerminal"}
        ]
    }


def launch_python():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Python: Current File", "type": "debugpy", "request": "launch", "program": "${file}", "console": "integratedTerminal"},
            {"name": "Python: Module", "type": "debugpy", "request": "launch", "module": "${command:extension.commandpack.fileModule}", "console": "integratedTerminal"}
        ]
    }


def launch_go():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Go: Current File", "type": "go", "request": "launch", "mode": "auto", "program": "${file}"},
            {"name": "Go: Test Package", "type": "go", "request": "launch", "mode": "test", "program": "${workspaceFolder}"}
        ]
    }


def launch_rust():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Rust: cargo run", "type": "lldb", "request": "launch", "program": "${workspaceFolder}/target/debug/${workspaceFolderBasename}", "args": [], "cargo": {"args": ["build"]}},
            {"name": "Rust: cargo test", "type": "lldb", "request": "launch", "program": "${workspaceFolder}/target/debug/deps/${workspaceFolderBasename}", "args": [], "cargo": {"args": ["test"]}}
        ]
    }


def launch_java():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "Java: Current File", "type": "java", "request": "launch", "mainClass": "${file}", "console": "integratedTerminal"},
            {"name": "Java: Maven Build", "type": "shell", "request": "launch", "command": "mvn clean compile"}
        ]
    }


def launch_csharp():
    return {
        "version": "0.2.0",
        "configurations": [
            {"name": "C#: Launch", "type": "coreclr", "request": "launch", "preLaunchTask": "build", "program": "${workspaceFolder}/bin/Debug/net8.0/${workspaceFolderBasename}.dll", "args": [], "cwd": "${workspaceFolder}", "console": "integratedTerminal", "stopAtEntry": False},
            {"name": "C#: Attach", "type": "coreclr", "request": "attach", "processId": "${command:pickProcess}"}
        ]
    }


# ─── Tasks.json Builders ─────────────────────────────────────────────────────

def tasks_nextjs():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "npm run dev", "label": "Next.js: Dev", "type": "shell", "group": {"kind": "build", "isDefault": True}, "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "npm run build", "label": "Next.js: Build", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "npm run lint", "label": "Next.js: Lint", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "npx tsc --noEmit", "label": "TypeScript: Type Check", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "npm test", "label": "Tests", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "new"}}
        ]
    }


def tasks_nextjs_bun():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "bun run dev", "label": "Next.js: Dev", "type": "shell", "group": {"kind": "build", "isDefault": True}, "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "bun run build", "label": "Next.js: Build", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "bun run lint", "label": "Next.js: Lint", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "bun run type-check", "label": "TypeScript: Type Check", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "bun run test", "label": "Tests", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "new"}}
        ]
    }


def tasks_django():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "python manage.py runserver", "label": "Django: Runserver", "type": "shell", "group": {"kind": "build", "isDefault": True}, "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "python manage.py test --keepdb --verbosity=2", "label": "Django: Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "python manage.py makemigrations", "label": "Django: Make Migrations", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "python manage.py migrate", "label": "Django: Migrate", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}}
        ]
    }


def tasks_dualdjango_nextjs():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "cd backend && python manage.py runserver", "label": "Django: Runserver", "type": "shell", "group": {"kind": "build"}, "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "cd frontend && npm run dev", "label": "Frontend: Dev", "type": "shell", "group": {"kind": "build"}, "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "cd backend && python manage.py test --keepdb --verbosity=2", "label": "Django: Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "cd backend && python manage.py makemigrations", "label": "Django: Make Migrations", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "cd backend && python manage.py migrate", "label": "Django: Migrate", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "cd frontend && npm run build", "label": "Frontend: Build", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "new"}},
            {"command": "cd frontend && npm test", "label": "Frontend: Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "new"}}
        ]
    }


def tasks_bun():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "bun run format", "label": "Format", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "bun run typecheck", "label": "Type Check", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "bun test", "label": "Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}}
        ]
    }


def tasks_node():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "npm start", "label": "Start", "type": "shell", "group": {"kind": "build", "isDefault": True}, "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "npm test", "label": "Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "npm run lint", "label": "Lint", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}}
        ]
    }


def tasks_python():
    return {
        "version": "2.0.0",
        "tasks": [
            {"command": "python -m pytest", "label": "Test", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "ruff check .", "label": "Lint", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "mypy .", "label": "Type Check", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}}
        ]
    }


# ─── Extensions.json Builders ────────────────────────────────────────────────

def ext_bun():
    return {
        "recommendations": [
            "esbenp.prettier-vscode",
            "oven.bun-vscode",
            "foxundermoon.shell-format",
            "usernamehw.errorlens"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    }


def ext_nextjs():
    return {
        "recommendations": [
            "esbenp.prettier-vscode",
            "bradlc.vscode-tailwindcss",
            "dbaeumer.vscode-eslint",
            "ms-vscode.vscode-typescript-next",
            "formulahendry.auto-rename-tag",
            "usernamehw.errorlens"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    }


def ext_nextjs_bun():
    return {
        "recommendations": [
            "esbenp.prettier-vscode",
            "bradlc.vscode-tailwindcss",
            "dbaeumer.vscode-eslint",
            "ms-vscode.vscode-typescript-next",
            "oven.bun-vscode",
            "formulahendry.auto-rename-tag",
            "usernamehw.errorlens"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    }


def ext_django():
    return {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "batisteo.vscode-django",
            "amannn.vscode-djlint"
        ],
        "unwantedRecommendations": []
    }


def ext_dualdjango():
    return {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "batisteo.vscode-django",
            "amannn.vscode-djlint",
            "esbenp.prettier-vscode",
            "bradlc.vscode-tailwindcss",
            "dbaeumer.vscode-eslint",
            "ms-vscode.vscode-typescript-next",
            "formulahendry.auto-rename-tag",
            "usernamehw.errorlens"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    }


def ext_node():
    return {
        "recommendations": [
            "esbenp.prettier-vscode",
            "dbaeumer.vscode-eslint",
            "christian-kohler.npm-intellisense"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    }


def ext_python():
    return {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "charliermarsh.ruff"
        ],
        "unwantedRecommendations": []
    }


def ext_go():
    return {
        "recommendations": ["golang.go"],
        "unwantedRecommendations": []
    }


def ext_rust():
    return {
        "recommendations": ["rust-lang.rust-analyzer", "tamasfe.even-better-toml"],
        "unwantedRecommendations": []
    }


def ext_java():
    return {
        "recommendations": ["redhat.java", "vscjava.vscode-java-debug", "vscjava.vscode-maven"],
        "unwantedRecommendations": []
    }


def ext_csharp():
    return {
        "recommendations": ["ms-dotnettools.csharp", "ms-dotnettools.csdevkit"],
        "unwantedRecommendations": []
    }


def ext_generic():
    return {
        "recommendations": [],
        "unwantedRecommendations": []
    }


# ─── Repo Definitions ────────────────────────────────────────────────────────

# Each entry: (relative_path, stack_name)
# Stack: 'nextjs', 'nextjs-bun', 'django', 'dualdjango-nextjs', 'dualdjango-node',
#        'bun', 'node', 'python', 'go', 'rust', 'java', 'csharp', 'generic',
#        'existing-nextjs-bun', 'existing-django', 'existing-docs'

REPOS_GENERATE = [
    # ── From scratch (full .vscode/ creation) ──
    ("projects/mcp-servers/typescript", "node"),
    ("projects/mcp-servers/python", "python"),
    ("projects/mcp-servers/go", "go"),
    ("projects/mcp-servers/rust", "rust"),
    ("projects/mcp-servers/java", "java"),
    ("projects/mcp-servers/kotlin", "generic"),
    ("projects/mcp-servers/php", "generic"),
    ("projects/mcp-servers/ruby", "generic"),
    ("projects/mcp-servers/swift", "generic"),
    ("projects/mcp-servers/csharp", "csharp"),
    ("projects/mcp-servers/copilot-studio", "node"),
    ("projects/profile", "django"),
    ("projects/Python-projects", "python"),
    ("projects/cookiecutter-django-tailwind", "django"),
    ("projects/youtube-downloader", "python"),
    ("projects/xamehi", "dualdjango-node"),  # Django + Express + React
]

REPOS_AUGMENT = [
    # ── Partial — add missing files ──
    ("", "root"),                          # Root SandBox — has settings, needs launch/tasks/extensions/mcp.json
    ("Bash", "bun"),                       # Has settings, needs launch/tasks/extensions
    ("Resume_maker", "bun"),               # Has settings, needs launch/tasks/extensions
    ("projects/university-libary-jsm", "nextjs"),  # Has settings+launch, needs extensions+tasks
]

# ─── Helpers ─────────────────────────────────────────────────────────────────

def write_json(path, data):
    """Write data as formatted JSON to path, creating directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"  ✓ {os.path.relpath(path, SANDBOX)}")


def gen_configs(repo_path, stack):
    """Generate settings.json, launch.json, tasks.json, extensions.json for a repo."""
    vscode = os.path.join(SANDBOX, repo_path, ".vscode")

    # settings.json
    fn_map = {
        "nextjs": settings_nextjs,
        "nextjs-bun": settings_nextjs,  # Same base, launch/tasks differ
        "django": settings_django,
        "dualdjango-nextjs": settings_dualdjango_nextjs,
        "dualdjango-node": settings_dualdjango_nextjs,
        "bun": settings_bun,
        "node": settings_node,
        "python": settings_python,
        "go": settings_go,
        "rust": settings_rust,
        "java": settings_java,
        "csharp": settings_csharp,
        "generic": settings_node,  # Minimal Node-like config for obscure languages
    }
    if stack in fn_map:
        write_json(os.path.join(vscode, "settings.json"), fn_map[stack]())

    # launch.json
    launch_map = {
        "nextjs": launch_nextjs,
        "nextjs-bun": launch_nextjs_bun,
        "django": launch_django,
        "dualdjango-nextjs": launch_dualdjango_nextjs,
        "dualdjango-node": launch_dualdjango_node,
        "bun": launch_bun,
        "node": launch_node,
        "python": launch_python,
        "go": launch_go,
        "rust": launch_rust,
        "java": launch_java,
        "csharp": launch_csharp,
        "generic": launch_node,
    }
    if stack in launch_map:
        write_json(os.path.join(vscode, "launch.json"), launch_map[stack]())

    # tasks.json
    tasks_map = {
        "nextjs": tasks_nextjs,
        "nextjs-bun": tasks_nextjs_bun,
        "django": tasks_django,
        "dualdjango-nextjs": tasks_dualdjango_nextjs,
        "dualdjango-node": tasks_dualdjango_nextjs,
        "bun": tasks_bun,
        "node": tasks_node,
        "python": tasks_python,
        "go": lambda: {"version": "2.0.0", "tasks": []},
        "rust": lambda: {"version": "2.0.0", "tasks": []},
        "java": lambda: {"version": "2.0.0", "tasks": [{"command": "mvn clean compile", "label": "Build", "type": "shell", "group": "build"}]},
        "csharp": lambda: {"version": "2.0.0", "tasks": [{"command": "dotnet build", "label": "Build", "type": "shell", "group": "build"}, {"command": "dotnet test", "label": "Test", "type": "shell", "group": "test"}]},
        "generic": lambda: {"version": "2.0.0", "tasks": []},
    }
    if stack in tasks_map:
        write_json(os.path.join(vscode, "tasks.json"), tasks_map[stack]())

    # extensions.json
    ext_map = {
        "nextjs": ext_nextjs,
        "nextjs-bun": ext_nextjs_bun,
        "django": ext_django,
        "dualdjango-nextjs": ext_dualdjango,
        "dualdjango-node": ext_dualdjango,
        "bun": ext_bun,
        "node": ext_node,
        "python": ext_python,
        "go": ext_go,
        "rust": ext_rust,
        "java": ext_java,
        "csharp": ext_csharp,
        "generic": ext_generic,
    }
    if stack in ext_map:
        write_json(os.path.join(vscode, "extensions.json"), ext_map[stack]())


def gen_root_configs():
    """Root workspace — multi-stack root config including mcp.json."""
    vscode = os.path.join(SANDBOX, ".vscode")

    # settings.json already exists — write enhanced version
    root_settings = settings_dualdjango_nextjs()
    root_settings["editor.defaultFormatter"] = "esbenp.prettier-vscode"
    root_settings["terminal.integrated.defaultProfile.windows"] = "PowerShell"
    root_settings["terminal.integrated.profiles.windows"] = {
        "Command Prompt": {"icon": "terminal-cmd", "path": "cmd.exe"},
        "Git Bash": {"icon": "terminal-bash", "source": "Git Bash"},
        "PowerShell": {"icon": "terminal-powershell", "source": "PowerShell"}
    }
    root_settings["workbench.editor.editorActionsLocation"] = "default"
    # Add shellscript formatting
    root_settings["[shellscript]"] = {"editor.defaultFormatter": "foxundermoon.shell-format"}
    write_json(os.path.join(vscode, "settings.json"), root_settings)

    # launch.json — multi-root, covers Bash scripts + Django + Next.js
    write_json(os.path.join(vscode, "launch.json"), {
        "version": "0.2.0",
        "configurations": [
            {"name": "Bun: Current File", "type": "node", "request": "launch", "runtimeExecutable": "bun", "program": "${file}", "console": "integratedTerminal"},
            {"name": "Bun: Run All Tests", "type": "node", "request": "launch", "runtimeExecutable": "bun", "runtimeArgs": ["test"], "console": "integratedTerminal"},
            {"name": "Python: Current File", "type": "debugpy", "request": "launch", "program": "${file}", "console": "integratedTerminal"},
            {"name": "Node.js: Current File", "type": "node", "request": "launch", "program": "${file}", "console": "integratedTerminal"}
        ]
    })

    # tasks.json
    write_json(os.path.join(vscode, "tasks.json"), {
        "version": "2.0.0",
        "tasks": [
            {"command": "python3 -m pytest", "label": "Python: Test All", "type": "shell", "group": "test", "presentation": {"reveal": "always", "panel": "shared"}},
            {"command": "ruff check .", "label": "Python: Lint", "type": "shell", "group": "build", "presentation": {"reveal": "always", "panel": "shared"}}
        ]
    })

    # extensions.json — comprehensive multi-stack
    write_json(os.path.join(vscode, "extensions.json"), {
        "recommendations": [
            "esbenp.prettier-vscode",
            "ms-python.python",
            "ms-python.vscode-pylance",
            "batisteo.vscode-django",
            "bradlc.vscode-tailwindcss",
            "dbaeumer.vscode-eslint",
            "oven.bun-vscode",
            "foxundermoon.shell-format",
            "usernamehw.errorlens",
            "charliermarsh.ruff",
            "davidanson.vscode-markdownlint"
        ],
        "unwantedRecommendations": [
            "ms-vscode.vscode-typescript-tslint-plugin",
            "hookyqr.beautify"
        ]
    })

    # mcp.json — root workspace only
    write_json(os.path.join(vscode, "mcp.json"), {
        "inputs": [
            {"type": "promptString", "id": "workspaceFolder", "description": "Workspace root path"}
        ],
        "servers": {
            "filesystem": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
            }
        }
    })


# ─── Execution ───────────────────────────────────────────────────────────────

def main():
    import os

    print("=" * 60)
    print("VS Code Workspace Configurator — Batch Generation")
    print("=" * 60)

    # Phase 2: Generate from scratch
    print("\n── Phase 2: Create .vscode/ from scratch ──")
    for rpath, stack in REPOS_GENERATE:
        full = os.path.join(SANDBOX, rpath)
        vscode_dir = os.path.join(full, ".vscode")
        if not os.path.isdir(vscode_dir):
            print(f"\n{rpath} [{stack}] — creating .vscode/")
            gen_configs(rpath, stack)
        else:
            print(f"\n{rpath} [{stack}] — .vscode/ already exists, skipping")

    # Phase 3: Root workspace (comprehensive)
    print("\n\n── Phase 3a: Root Workspace ──")
    gen_root_configs()

    # Phase 3: Augment partial repos
    print("\n── Phase 3b: Augment partial .vscode/ ──")
    for rpath, stack in REPOS_AUGMENT:
        if rpath == "":
            continue  # root handled above
        full = os.path.join(SANDBOX, rpath)
        vscode_dir = os.path.join(full, ".vscode")
        # Check which files exist
        existing = set()
        if os.path.isdir(vscode_dir):
            for f in os.listdir(vscode_dir):
                if f.endswith(".json"):
                    existing.add(f)

        needed = {"launch.json", "tasks.json", "extensions.json"}
        missing = needed - existing

        if missing:
            print(f"\n{rpath} [{stack}] — missing: {', '.join(sorted(missing))}")

        # Always write settings as enhancement
        fn_map = {
            "bun": settings_bun,
            "nextjs": settings_nextjs,
        }
        if stack in fn_map:
            write_json(os.path.join(vscode_dir, "settings.json"), fn_map[stack]())

        # Write missing files
        if "launch.json" in missing:
            lmap = {"bun": launch_bun, "nextjs": launch_nextjs}
            write_json(os.path.join(vscode_dir, "launch.json"), lmap[stack]())
        if "tasks.json" in missing:
            tmap = {"bun": tasks_bun, "nextjs": tasks_nextjs}
            write_json(os.path.join(vscode_dir, "tasks.json"), tmap[stack]())
        if "extensions.json" in missing:
            emap = {"bun": ext_bun, "nextjs": ext_nextjs}
            write_json(os.path.join(vscode_dir, "extensions.json"), emap[stack]())

    print("\n\n✅ Phase 2 + 3 complete. Ready for validation.")


if __name__ == "__main__":
    main()
