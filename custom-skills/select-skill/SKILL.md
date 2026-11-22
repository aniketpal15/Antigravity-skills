---
name: select-skill
description: "ULTRA-HIGH SENSITIVITY TRIGGER. Trigger this skill PROACTIVELY and IMMEDIATELY whenever the user writes, mentions, or implies selecting skills, picking tools, routing domains, choosing best agents, or evaluating options across Antigravity's 5,000+ skills. Even a casual keyword or partial phrase (e.g. 'select skill', 'pick skill', 'choose tools', 'which skill', 'route this') MUST instantly activate this skill. Upon activation, it ALWAYS first outputs a comprehensive description of what Antigravity understood from the prompt, what the user wants from Antigravity, and the recognized planning scope. Then, it maps every required domain, selects the #1 best skill per domain with an in-depth description and comparative justification of why it beats the alternatives, presents all available alternative options, and strictly requires user confirmation before execution."
metadata:
  argument-hint: "[task prompt] or [select skill <task>]"
  triggers:
    - "select skill"
    - "select-skill"
    - "/select skill"
    - "/select-skill"
    - "select skills"
    - "choose skill"
    - "choose skills"
    - "pick skill"
    - "pick skills"
    - "which skill"
    - "which skills"
    - "what skill"
    - "what skills"
    - "find skill"
    - "find skills"
    - "best skill"
    - "best skills"
    - "route skill"
    - "route skills"
    - "skill selector"
    - "skill routing"
    - "skill selection"
    - "recommend skill"
    - "recommend skills"
    - "suggest skill"
    - "suggest skills"
    - "select agent"
    - "pick agent"
    - "choose agent"
    - "what tool should I use"
    - "which tool is best"
    - "pick the right skill"
---

# Select Skill — Universal Multi-Domain Antigravity Skill Orchestrator

`select-skill` is an ultra-sensitive, intelligent skill router and confirmation gate. It operates across **every single installed skill and domain** in Antigravity (5,075+ skills across 19 categories).

## ⚡ Ultra-High Sensitivity Triggering
If the user's prompt contains **ANY** keyword, command, or conversational phrase related to selecting or choosing skills/tools (e.g., `select skill`, `pick skill`, `choose skill`, `which skill`, `what skills to use`, `find best skill`), the agent **MUST IMMEDIATELY trigger this skill without hesitation**.

---

## The Mandatory 5-Step Operational Pipeline

Whenever triggered on ANY task:

### Step 1: Prompt Comprehension & Intent Reflection (MANDATORY FIRST STEP)
Before selecting any skill or performing any actions, Antigravity MUST immediately articulate and output a detailed reflection back to the user:
- **🧠 What Antigravity Understood From Your Prompt:** Deep, full breakdown of the user's request, core subject matter, context, constraints, and scope.
- **🎯 What You Want From Antigravity (User Goal & Expectations):** Explicitly states the exact deliverables, goals, and results the user is looking for from Antigravity.
- **🗺️ Recognized Planning & Architectural Scope:** The initial trajectory, challenges, technical/creative domains involved, and high-level strategy Antigravity sees based on the prompt.

Only AFTER presenting this complete comprehension breakdown does Antigravity proceed to Step 2.

### Step 2: Multi-Domain Deconstruction
The agent analyzes the user's prompt and identifies **every single domain** necessary to complete the task with high precision. A task may require 1 domain, 2 domains, or 5+ domains simultaneously (e.g., Fullstack App = UI/UX + Frontend + Backend + Database + Security).

### Step 3: Global Skill Scan & Best-in-Class Ranking
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

### Step 4: Interactive Confirmation Gate with In-Depth Descriptions

**The agent MUST NEVER start executing code, making edits, or running builds before the user confirms.**  
It must output the structured plan, starting with the prompt comprehension summary, complete with skill descriptions and competitive justification, and pause for user input:

```markdown
### 🧠 Step 1: Antigravity Prompt Comprehension & Plan Overview
- **What Antigravity Understood From Your Prompt:** [Thorough explanation of the task, context, and requirements captured]
- **What You Want From Antigravity:** [Clear statement of the expected results, deliverables, and final outcomes]
- **Recognized Planning & Strategy:** [High-level roadmap and architectural scope identified]

---

### 🎯 Step 2: Selected Primary Skills for Your Task

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

**I have analyzed your prompt and selected these primary skills. Would you like to proceed with this combination, or swap any skill with an alternative from the list above?**
*(Reply "Yes, continue" to start, or specify: "Don't use [Skill A], use [Skill B] instead")*
```

---

### Step 5: User Confirmation & Execution
- **If User Approves ("Yes", "Proceed", "Continue"):** Immediately activate the confirmed primary skills and execute the user's task to completion.
- **If User Overrides ("Don't use X, use Y instead"):** Swap the skill for that domain to the user's preferred choice, confirm the final setup, and execute immediately.

---

## Universal Domain Coverage (All-Encompassing)

`select-skill` actively scans and routes across **ALL** 19 domains:
1. Backend & Architecture
2. Frontend & Web
3. UI/UX & Design Systems
4. 3D Modeling & Rendering
5. Video Editing & VFX
6. Photo Editing & Generative Media
7. Audio & Sound Design
8. Databases & Data Engineering
9. DevOps, Cloud & Infrastructure
10. Cybersecurity & Pen-Testing
11. Testing & Quality Assurance
12. Mobile & Cross-Platform
13. AI, ML & LLM Engineering
14. Game Development & Physics
15. Embedded & Systems Engineering
16. Blockchain & Web3
17. Business, Marketing, SEO & Content
18. Science, Research & Bioinformatics
19. Project Management & Spec-Driven Development (GSD)
