# Antigravity Skills Vault

A modular, multi-domain library of 4,600+ skills organized for AI developer assistants, code agents, and autonomous development environments.

---

## Repository Structure

The skills are structured into specialized domains to allow selective installation or full-stack utilization:

```
Antigravity skills/
├── custom-skills/                          # Universal Orchestration Skills
│   ├── select-skill/                       # Multi-domain skill router & confirmation gate
│   └── ask-question/                       # Socratic interrogation & planning engine
├── 01-3d-modeling-and-rendering/           # 3D, Blender, Three.js, WebGL & Mesh tools
├── 02-audio-and-sound-engineering/         # Audio processing, stems, SFX & voice
├── 03-autonomous-agents-and-ai/            # Agent workflows, orchestration & LLM tools
├── 04-backend-architecture-and-apis/       # Python, Go, Rust, Node, Java, REST & gRPC
├── 05-business-marketing-and-seo/          # Programmatic SEO, growth, copy & analytics
├── 06-code-quality-security-and-compliance/# Red teaming, security audits & SAST/DAST
├── 07-codebase-intelligence-and-graphs/    # Repo mapping, ASTs & knowledge graphs
├── 08-databases-and-data-engineering/      # PostgreSQL, Redis, Mongo, ETL & indexing
├── 09-devops-cloud-and-infrastructure/     # Docker, Kubernetes, Terraform & CI/CD
├── 10-frontend-uiux-and-design-systems/    # React, Vue, Tailwind, Shadcn & UI systems
├── 11-general-developer-utilities/         # General engineering patterns & utilities
├── 12-mobile-and-cross-platform/           # Flutter, React Native, iOS Swift & Android
├── 13-science-and-bioinformatics/          # Genomics, molecular data & research tools
├── 14-senior-engineering-best-practices/   # Architecture decisions & code standards
├── 15-spec-driven-project-management-gsd/  # Spec-driven workflows & milestone management
├── 16-testing-qa-and-debugging/            # Playwright E2E, Jest, Pytest & debugging
├── 17-ui-animation-and-motion-graphics/    # GSAP, Framer Motion, transitions & canvas
└── 18-video-and-photo-editing-vfx/         # FFmpeg, Remotion, image manipulation & VFX
```

---

## Highlighted Custom Orchestrators

Located in [`custom-skills/`](./custom-skills/):

### 1. `select-skill`
* **Trigger:** `/select skill <task prompt>`
* **Role:** Analyzes any complex task prompt, detects the required capability domains (e.g. Backend + UI/UX + Database), picks the top-ranked skill per domain, presents alternative options, and pauses for user confirmation before executing.

### 2. `ask-question`
* **Trigger:** `/ask question <project idea>`
* **Role:** Socratic interrogation engine. Challenges assumptions and asks targeted questions across architecture, visuals, data models, and edge cases until requirements are clear, then produces a phased blueprint and delegates to `select-skill`.

---

## How to Install and Use

### Option 1: Global Antigravity / Claude Code Installation
To use these skills globally, copy the desired domain folders (or all folders) into your local agent skills directory:

**Windows:**
```powershell
# Copy custom orchestrator skills
Copy-Item -Recurse "custom-skills\*" "$HOME\.gemini\skills\"

# Copy a specific domain (example: UI/UX)
Copy-Item -Recurse "10-frontend-uiux-and-design-systems\*" "$HOME\.gemini\skills\"
```

**macOS / Linux:**
```bash
# Copy custom orchestrator skills
cp -r custom-skills/* ~/.gemini/skills/

# Copy a specific domain
cp -r 10-frontend-uiux-and-design-systems/* ~/.gemini/skills/
```

### Option 2: Project-Local Skills
Place any domain folder directly inside your project repository under `.skills/` or `.agent/skills/` to enable domain-specific capabilities for that repository.

---

## Quickstart Examples

```text
# Interrogate a project concept and build a roadmap
/ask question I want to build a real-time multiplayer whiteboard application

# Intelligently select and confirm skills before running
/select skill Implement a high-performance Go microservice with Redis caching
```

---

## License

This collection is distributed under the MIT License. Individual skills and playbooks retain their respective upstream specifications.
