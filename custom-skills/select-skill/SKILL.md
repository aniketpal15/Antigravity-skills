---
name: select-skill
description: "Universal skill selector and orchestrator covering ALL technical, creative, and engineering domains across 5,000+ installed Antigravity skills. Analyzes any task prompt, maps every required domain, selects the #1 best skill per domain with a detailed description and comparative justification of why it beats the alternatives, presents all available alternative options, and strictly requires user confirmation before execution."
metadata:
  argument-hint: "[task prompt] or [/select skill <task>]"
---

# Select Skill — Universal Multi-Domain Antigravity Skill Orchestrator

`select-skill` is an intelligent skill router and confirmation gate. It operates across **every single installed skill and domain** in Antigravity (5,075+ skills across 19 categories).

For **ANY** prompt or task—regardless of domain or combination of domains—`select-skill` automatically analyzes the requirements, identifies every domain involved, selects the single best primary skill for each domain, **provides an in-depth description of the selected skill and explains exactly why it was chosen as superior to all other alternatives in that domain**, compiles the alternative options, and **always asks for user approval before executing**.

---

## Universal Domain Coverage (All-Encompassing)

`select-skill` actively scans and routes across **ALL** domains:

1. **Backend & Architecture**: Node.js, Python, Go, Rust, Java, C#, PHP, C++, FastAPI, Django, Spring Boot, microservices, gRPC, REST, GraphQL.
2. **Frontend & Web**: React, Next.js, Vue, Nuxt, Svelte, Angular, Modern Web standards, SSR/SSG.
3. **UI/UX & Design Systems**: UI component design, Tailwind, Shadcn, design tokens, responsive layouts, accessibility (WCAG), typography, human interface guidelines.
4. **3D Modeling & Rendering**: Blender automation, Three.js, React Three Fiber (R3F), Spline, WebGL/WebGPU, mesh processing, geometry conversions.
5. **Video Editing & VFX**: FFmpeg processing, Remotion code-based video, HyperFrames, DaVinci Resolve, premiere workflows, shotcraft, camera transitions, subtitle generators.
6. **Photo Editing & Generative Media**: Image manipulation, ImageMagick, OpenCV, Pillow, background removal, photo restoration, AI image synthesis.
7. **Audio & Sound Design**: Audio stem separation, mastering, voice synthesis/cloning, Foley SFX, podcast audio cleanup, MIDI/music generation.
8. **Databases & Data Engineering**: PostgreSQL, MySQL, SQLite, MongoDB, Redis, BigQuery, AlloyDB, Cloud SQL, Firestore, vector databases, ETL pipelines.
9. **DevOps, Cloud & Infrastructure**: Docker, Kubernetes, Terraform, Helm, AWS, Azure, GCP, Cloudflare, Linux server hardening, CI/CD automation.
10. **Cybersecurity & Pen-Testing**: Red-teaming, vulnerability hunting, API security, JWT/OAuth crypto, SAST/DAST, penetration testing, reverse engineering.
11. **Testing & Quality Assurance**: Playwright E2E, Jest, Pytest, Vitest, integration testing, fuzzing, bug hunting, CodeRabbit code auditing.
12. **Mobile & Cross-Platform**: React Native, Expo, Flutter, iOS (Swift/SwiftUI), Android (Kotlin/Jetpack Compose).
13. **AI, ML & LLM Engineering**: RAG pipelines, fine-tuning, embeddings, prompt engineering, agent evaluations, inference optimization.
14. **Game Development & Physics**: Unity, Godot (GDScript/C#), Unreal Engine, 2D/3D physics (Rapier, Matter.js), ECS architecture.
15. **Embedded & Systems Engineering**: Bare-metal C/C++, ESP32, STM32, ARM Cortex, FreeRTOS, Zephyr, firmware auditing.
16. **Blockchain & Web3**: Solidity, EVM, Solana, smart contract security audits, DeFi protocols, Web3 testing.
17. **Business, Marketing, SEO & Content**: Programmatic SEO, conversion rate optimization, technical copywriting, competitor analytics.
18. **Science, Research & Bioinformatics**: AlphaGenome, genomics, protein folding, scientific literature search, statistical analysis.
19. **Project Management & Spec-Driven Development**: GSD (Get Stuff Done), Conductor, architecture decision records, spec-driven development.

---

## The Mandatory 4-Step Operational Pipeline

Whenever `/select skill` or `select skill` is triggered on ANY task:

### Step 1: Multi-Domain Deconstruction
The agent analyzes the user's prompt and identifies **every single domain** necessary to complete the task with high precision. A task may require 1 domain, 2 domains, or 5+ domains simultaneously (e.g., Fullstack App = UI/UX + Frontend + Backend + Database + Security).

### Step 2: Global Skill Scan & Best-in-Class Ranking
The agent searches all installed skills in:
- `C:\Users\anike\.gemini\config\plugins\`
- `C:\Users\anike\Downloads\Antigravity_Master_Skills_Catalog.txt`

For **each** identified domain:
- **Primary Selection (1 Skill):** The absolute #1 most capable, modern, and specific skill for that exact requirement.
- **Skill Profile & Comparative Justification:** 
  1. What the skill does and its specialized capabilities.
  2. Exactly why it was chosen over the alternative skills in that domain (e.g., performance edge, stricter type safety, modern API design, specialized tooling).
- **Alternative Candidates (2 to 5 Skills):** The other top installed skills in that same domain with brief descriptions.

---

### Step 3: Interactive Confirmation Gate with In-Depth Descriptions

**The agent MUST NEVER start executing code, making edits, or running builds before the user confirms.**  
It must output the structured plan, complete with skill descriptions and competitive justification, and pause for user input:

```markdown
### 🎯 Selected Primary Skills for Your Task

#### Domain: [Domain 1 Name]
- **Selected #1 Skill:** `[selected-skill-name]`
- **Skill Overview:** [2-3 sentence description explaining what this skill does and its specialized tools/frameworks]
- **Why It Is Best Over Alternatives:** [Clear comparative explanation of why Antigravity picked this specific skill over the other options in this domain, detailing its advantages for the user's specific prompt]

#### Domain: [Domain 2 Name]
- **Selected #1 Skill:** `[selected-skill-name]`
- **Skill Overview:** [2-3 sentence description explaining what this skill does and its specialized tools/frameworks]
- **Why It Is Best Over Alternatives:** [Clear comparative explanation of why Antigravity picked this specific skill over the other options in this domain, detailing its advantages for the user's specific prompt]

---

### 📋 Alternative Candidates in These Domains

* **[Domain 1 Name] Alternatives:**
  - `[alt-skill-1a]` — [Brief description]
  - `[alt-skill-1b]` — [Brief description]
* **[Domain 2 Name] Alternatives:**
  - `[alt-skill-2a]` — [Brief description]
  - `[alt-skill-2b]` — [Brief description]

---

**I have selected these primary skills for your task. Would you like to proceed with this combination, or swap any skill with an alternative from the list above?**
*(Reply "Yes, continue" to start, or specify: "Don't use [Skill A], use [Skill B] instead")*
```

---

### Step 4: User Confirmation & Execution
- **If User Approves ("Yes", "Proceed", "Continue"):** Immediately activate the confirmed primary skills and execute the user's task to completion.
- **If User Overrides ("Don't use X, use Y instead"):** Swap the skill for that domain to the user's preferred choice, confirm the final setup, and execute immediately.

---

## Trigger Phrases

`select-skill` automatically executes when the prompt includes:
- `/select skill <prompt>`
- `/select-skill <prompt>`
- `select skill for <prompt>`
- `choose the best skills for <prompt>`
- `pick skills and ask me before starting <prompt>`
