#!/usr/bin/env bash
# Instruction Personality Quick Commands
# Source: source scripts/instruction-quick-commands.sh
#
# Generated from 186 .instructions.md files in 19 categories


# Switch to design-ux instruction personality set (6 files)
use-design-ux() {
    hermes config set agent.personality design-ux
    echo "Now using 'design-ux' knowledge base (6 instruction files)"
}

# Switch to prompt-engineering instruction personality set (8 files)
use-prompt-engineering() {
    hermes config set agent.personality prompt-engineering
    echo "Now using 'prompt-engineering' knowledge base (8 instruction files)"
}

# Switch to frontend instruction personality set (10 files)
use-frontend() {
    hermes config set agent.personality frontend
    echo "Now using 'frontend' knowledge base (10 instruction files)"
}

# Switch to infra-devops instruction personality set (7 files)
use-infra-devops() {
    hermes config set agent.personality infra-devops
    echo "Now using 'infra-devops' knowledge base (7 instruction files)"
}

# Switch to other instruction personality set (31 files)
use-other() {
    hermes config set agent.personality other
    echo "Now using 'other' knowledge base (31 instruction files)"
}

# Switch to dotnet instruction personality set (20 files)
use-dotnet() {
    hermes config set agent.personality dotnet
    echo "Now using 'dotnet' knowledge base (20 instruction files)"
}

# Switch to java-jvm instruction personality set (14 files)
use-java-jvm() {
    hermes config set agent.personality java-jvm
    echo "Now using 'java-jvm' knowledge base (14 instruction files)"
}

# Switch to shell-tooling instruction personality set (6 files)
use-shell-tooling() {
    hermes config set agent.personality shell-tooling
    echo "Now using 'shell-tooling' knowledge base (6 instruction files)"
}

# Switch to quality instruction personality set (8 files)
use-quality() {
    hermes config set agent.personality quality
    echo "Now using 'quality' knowledge base (8 instruction files)"
}

# Switch to copilot instruction personality set (6 files)
use-copilot() {
    hermes config set agent.personality copilot
    echo "Now using 'copilot' knowledge base (6 instruction files)"
}

# Switch to systems instruction personality set (6 files)
use-systems() {
    hermes config set agent.personality systems
    echo "Now using 'systems' knowledge base (6 instruction files)"
}

# Switch to databases instruction personality set (4 files)
use-databases() {
    hermes config set agent.personality databases
    echo "Now using 'databases' knowledge base (4 instruction files)"
}

# Switch to dataverse instruction personality set (14 files)
use-dataverse() {
    hermes config set agent.personality dataverse
    echo "Now using 'dataverse' knowledge base (14 instruction files)"
}

# Switch to power-platform instruction personality set (30 files)
use-power-platform() {
    hermes config set agent.personality power-platform
    echo "Now using 'power-platform' knowledge base (30 instruction files)"
}

# Switch to ci-cd instruction personality set (2 files)
use-ci-cd() {
    hermes config set agent.personality ci-cd
    echo "Now using 'ci-cd' knowledge base (2 instruction files)"
}

# Switch to python instruction personality set (3 files)
use-python() {
    hermes config set agent.personality python
    echo "Now using 'python' knowledge base (3 instruction files)"
}

# Switch to typescript instruction personality set (4 files)
use-typescript() {
    hermes config set agent.personality typescript
    echo "Now using 'typescript' knowledge base (4 instruction files)"
}

# Switch to php-ruby instruction personality set (5 files)
use-php-ruby() {
    hermes config set agent.personality php-ruby
    echo "Now using 'php-ruby' knowledge base (5 instruction files)"
}

# Switch to security instruction personality set (2 files)
use-security() {
    hermes config set agent.personality security
    echo "Now using 'security' knowledge base (2 instruction files)"
}

# List all instruction personalities
list-instructions() {
    echo "Available instruction personality categories:"
    for cat in ci-cd copilot databases dataverse design-ux dotnet frontend infra-devops java-jvm other php-ruby power-platform prompt-engineering python quality security shell-tooling systems typescript; do
        n=$(hermes config show 2>/dev/null | grep -c "agent.personalities.${cat}_" 2>/dev/null || echo 0)
        echo "  $cat ($n files)"
    done
}
# Aliases
for cat in ci-cd copilot databases dataverse design-ux dotnet frontend infra-devops java-jvm other php-ruby power-platform prompt-engineering python quality security shell-tooling systems typescript; do
    alias "$cat"="use-$cat"
done
