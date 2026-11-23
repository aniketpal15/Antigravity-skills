---
name: skillspector
description: >-
  Security scanner and vulnerability auditor for AI agent skills and MCP tools
  by NVIDIA. Detects prompt injection, malicious shell commands, token exfiltration,
  reverse shells, supply chain threats, and permission overreach before installation.
metadata:
  argument-hint: "[skill_path_or_repo] — security scan and audit"
  triggers:
    - "skillspector"
    - "scan skill"
    - "audit skill"
    - "check skill security"
    - "skill safety"
    - "inspect skill"
    - "is skill safe"
---

# NVIDIA SkillSpector

SkillSpector is an enterprise-grade security scanner and static/semantic vulnerability analysis framework engineered by NVIDIA specifically for AI agent skills, plugins, and Model Context Protocol (MCP) servers.

## Key Capabilities

- **Vulnerability Scanning**: Analyzes `SKILL.md`, source scripts (Python, Bash, PowerShell), and configuration files for known threat vectors.
- **Malicious Pattern Detection**: Identifies reverse shells, unauthorized token/credential exfiltration, outbound curl/wget hooks, and obfuscated payloads.
- **Prompt Injection Defense**: Detects indirect prompt injection vectors, jailbreak sequences, and malicious steering instructions hidden inside system prompts and documentation.
- **Supply Chain Analysis**: Verifies external dependencies, unpinned requirements, and suspicious network calls.
- **Risk Scoring & Decision Engine**: Evaluates risks on a 0-100 scale:
  - `0 - 20`: **LOW** -> Safe to install
  - `21 - 50`: **MEDIUM** -> Review findings before installation
  - `51 - 80`: **HIGH** -> Do NOT install
  - `81 - 100`: **CRITICAL** -> Block immediately

## CLI Commands

```bash
# Scan a local skill directory
skillspector scan path/to/skill

# Scan with structured JSON output for automated pipelines
skillspector scan path/to/skill --format json

# Scan an external Git repository directly
skillspector scan https://github.com/org/repo.git

# Launch as a persistent MCP security server
skillspector mcp

# Create a baseline exception suppression file
skillspector baseline path/to/skill
```

## Agent Integration

Whenever you are asked to install, import, or audit a new third-party skill or MCP tool, always invoke SkillSpector first to guarantee that no unsafe code or credentials risk entering the local environment.
