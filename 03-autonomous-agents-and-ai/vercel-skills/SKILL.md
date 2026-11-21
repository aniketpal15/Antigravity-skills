---
name: vercel-skills
description: "Vercel Labs Agent Skills CLI and Ecosystem Manager (npx skills). Discovers, searches, installs, updates, and manages open agent skills from skills.sh, GitHub, and npm directly into Antigravity, Claude Code, and coding agents."
metadata:
  argument-hint: "[add <repo> | find <query> | list | update | use <skill>]"
---

# Vercel Labs Agent Skills CLI (`npx skills`)

The official Vercel Labs CLI for the open agent skills ecosystem ([skills.sh](https://skills.sh)). It allows Antigravity to dynamically search, install, update, and manage reusable instruction packs from any GitHub repository, npm package, or community skill registry.

---

## When to Use This Skill

- When the user asks to search for new agent skills (`npx skills find <query>`).
- When installing community skills or packages from GitHub (`npx skills add <owner/repo>`).
- When updating, checking, or listing installed agent skills across the system.
- When creating a new standardized skill template (`npx skills init <name>`).
- When running a skill on the fly without permanently adding it (`npx skills use <source>@<skill>`).

---

## Core Capabilities & Commands

### 1. Discover & Search Skills
Search the global [skills.sh](https://skills.sh) registry and GitHub for capabilities:
```bash
npx -y skills find <query>
```
*Examples:*
- `npx -y skills find react` — Search for React and Next.js optimization skills.
- `npx -y skills find playwright` — Search for browser automation skills.
- `npx -y skills find security` — Search for security auditing and vulnerability skills.

### 2. Install Skills (Global or Project)
Install skills directly from any GitHub repo:
```bash
# Install globally across all Antigravity projects
npx -y skills add <owner/repo> -g

# Install specific skill from a repository
npx -y skills add vercel-labs/agent-skills --skill react-best-practices -g

# Install to current project only
npx -y skills add <owner/repo>
```

### 3. List Installed Skills
Show all active skills, their source repositories, and version locks:
```bash
npx -y skills list
```

### 4. Check for Updates & Upgrade
Check for newer upstream versions of installed skills:
```bash
# Check if any installed skills have updates
npx -y skills check

# Update all or specific skills
npx -y skills update
```

### 5. Use a Skill On-The-Fly (Zero Install)
Execute a skill without permanently cloning it to disk:
```bash
npx -y skills use <owner/repo>@<skill-name>
```

### 6. Scaffold a New Skill Template
Create a new compliant `SKILL.md` scaffold:
```bash
npx -y skills init <my-new-skill>
```

---

## What It Installs on the System

1. **CLI Engine:** Executed dynamically via `npx -y skills` (version 1.9.0+) with zero permanent npm bloat.
2. **Skill Destinations:**
   - **Global (`-g`):** Installs into user agent directory (`~/.gemini/skills/` or `~/.agents/skills/`).
   - **Project Local:** Installs into `./.agents/skills/<skill-name>/` or `./.skills/`.
3. **Lockfile (`skills-lock.json`):** Tracks exact Git commit SHAs and SHA-256 content hashes to guarantee reproducibility and prevent unauthorized upstream code drift.

---

## Instructions for Antigravity

- When asked to find or install skills from GitHub or skills.sh, run the command via `run_command` with `npx -y skills <command>`.
- Use the `-y` flag to bypass interactive CLI prompts when installing non-interactively.
- Always report the installed skill name, target path, and capabilities to the user after installation.
