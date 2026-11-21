# Antigravity Skills Vault

A modular, multi-domain library of 4,650+ skills organized for AI developer assistants, code agents, and autonomous development environments.

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
├── 03-autonomous-agents-and-ai/            # Agent workflows, orchestration, RTK & Vercel CLI
├── 04-backend-architecture-and-apis/       # Python, Go, Rust, Node, Java, REST & gRPC
├── 05-business-marketing-and-seo/          # Programmatic SEO, growth, copy & writing guidelines
├── 06-code-quality-security-and-compliance/# Red teaming, security audits & SAST/DAST
├── 07-codebase-intelligence-and-graphs/    # Graphify AST graphs, repo mapping & AST parsers
├── 08-databases-and-data-engineering/      # PostgreSQL, Redis, Mongo, ETL & indexing
├── 09-devops-cloud-and-infrastructure/     # Docker, Kubernetes, Terraform, Vercel & CI/CD
├── 10-frontend-uiux-and-design-systems/    # UI/UX Pro Max, React, Vue, Tailwind, Shadcn & UI rules
├── 11-general-developer-utilities/         # General engineering patterns & utilities
├── 12-mobile-and-cross-platform/           # Flutter, React Native guidelines, iOS Swift & Android
├── 13-science-and-bioinformatics/          # Genomics, molecular data & research tools
├── 14-senior-engineering-best-practices/   # Architecture decisions & code standards
├── 15-spec-driven-project-management-gsd/  # Spec-driven workflows & milestone management
├── 16-testing-qa-and-debugging/            # Playwright E2E, RTK test compression, Jest & Pytest
├── 17-ui-animation-and-motion-graphics/    # React View Transitions, GSAP, Framer Motion & canvas
└── 18-video-and-photo-editing-vfx/         # FFmpeg, Remotion, image manipulation & VFX
```

---

## Token-Saving & Performance Power Tools

This repository includes industry-standard tools specifically designed to reduce AI token burn and accelerate coding loops:

### 1. RTK (Rust Token Killer) — `03-autonomous-agents-and-ai/rtk`
* **Purpose:** High-performance Rust CLI proxy that strips verbose build output, progress bars, and passing tests before sending results to the LLM context.
* **Token Savings:** Cuts terminal output tokens by **60% to 90%** on `npm test`, `pytest`, `cargo test`, `git diff`, and linter runs.
* **Commands:** `rtk test <cmd>`, `rtk diff`, `rtk err <cmd>`, `rtk gain`.

### 2. Graphify — `07-codebase-intelligence-and-graphs/graphify`
* **Purpose:** Uses deterministic local Tree-Sitter AST parsers across 28 programming languages to build an offline knowledge graph of your project.
* **Token Savings:** Eliminates the need for the AI to re-read dozens of raw files on every turn, saving **70% to 85%** of codebase exploration tokens.
* **Commands:** `graphify update .`, `graphify explain "<component>"`, `/graphify .`.

### 3. UI/UX Pro Max — `10-frontend-uiux-and-design-systems/ui-ux-pro-max`
* **Purpose:** Pre-indexed local database of 194 UI/UX reasoning rules and 80 searchable design styles with offline Python search scripts.
* **Token Savings:** Prevents trial-and-error design prompting by instantly supplying pre-computed accessible color palettes, typography scales, and responsive layouts.

### 4. Vercel Skills Suite — `vercel-skills`, `react-best-practices`, `web-design-guidelines`
* **Purpose:** The open agent skills ecosystem manager (`npx skills`) paired with Vercel's official engineering guidelines covering 40+ React/Next.js rules and 100+ web design/accessibility rules.

---

## Custom Orchestrator Skills

Located in [`custom-skills/`](./custom-skills/):

### 1. `select-skill`
* **Trigger:** `/select skill <task prompt>`
* **Role:** Universal multi-domain skill router. Analyzes any prompt across all 18 domains, selects the #1 best skill with an in-depth comparative justification of why it beats alternative tools, shows the alternative options, and **pauses for user confirmation** before running.

### 2. `ask-question`
* **Trigger:** `/ask question <project idea>`
* **Role:** Universal Socratic interrogation engine. Dynamically challenges project concepts in any domain (from embedded firmware and 3D graphics to cybersecurity and databases), creates an exhaustive phased blueprint, matches specialized agents, and automatically delegates to `select-skill`.

---

## How to Install and Use

### Option 1: Automated Installer
Run the cross-platform Python installer to copy all skills (or a specific domain) into your global agent directory (`~/.gemini/skills/`):

```bash
# Install all skills globally
python install_skills.py

# Install only a specific domain (e.g. UI/UX or DevOps)
python install_skills.py frontend
python install_skills.py devops
```

> [!TIP]
> **Can you delete the cloned repository after installation?**  
> **Yes!** `install_skills.py` performs a complete standalone physical copy (`shutil.copytree`) into your permanent agent directory (`~/.gemini/skills/`). No symlinks or shortcuts are used. You can safely delete the cloned repository folder immediately after installation to save disk space. If you ever want updates in the future, simply re-clone or pull new releases.

### Option 2: Manual Copy
**Windows PowerShell:**
```powershell
Copy-Item -Recurse "custom-skills\*" "$HOME\.gemini\skills\"
Copy-Item -Recurse "10-frontend-uiux-and-design-systems\*" "$HOME\.gemini\skills\"
```

**macOS / Linux:**
```bash
cp -r custom-skills/* ~/.gemini/skills/
cp -r 10-frontend-uiux-and-design-systems/* ~/.gemini/skills/
```

---

## License

This collection is distributed under the MIT License. Individual skills and playbooks retain their respective upstream specifications.
