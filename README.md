# 🌌 Antigravity Skills Vault

[![Total Skills](https://img.shields.io/badge/Total%20Skills-4%2C761%2B-blueviolet?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)
[![Domains](https://img.shields.io/badge/Domains-18%20Specialized-blue?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-orange?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)
[![Agents](https://img.shields.io/badge/Works%20With-Antigravity%20%7C%20Claude%20%7C%20Gemini%20%7C%20Cursor-red?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)

> **The largest open-source modular intelligence library for autonomous AI developer assistants — 4,761 skills across 18 specialized engineering domains.**

The **Antigravity Skills Vault** supercharges any AI coding assistant (Antigravity, Claude Code, Gemini CLI, Cursor, CrewAI) by injecting deep, domain-specific procedural knowledge directly into the agent's execution context. Instead of relying on generic prompt guessing, each skill delivers exact command patterns, idiomatic code rules, security checklists, reference guides, and auto-verification steps — turning your AI assistant into a true domain expert.

---

## 📑 Table of Contents

1. [What You Gain From This Vault](#-what-you-gain-from-this-vault)
2. [Complete Skills Inventory Table](#-complete-skills-inventory-table)
3. [Domain-by-Domain Breakdown](#-domain-by-domain-breakdown)
4. [Token-Saving Power Tools](#-token-saving-power-tools)
5. [Universal Orchestration Skills](#-universal-orchestration-skills)
6. [Global Availability & Multi-Account Persistence](#-global-availability--multi-account-persistence)
7. [How to Install](#-how-to-install)
8. [Anatomy of a Skill](#-anatomy-of-a-skill)
9. [Supported AI Agents & Platforms](#-supported-ai-agents--platforms)
10. [Contributing](#-contributing)
11. [License](#-license)

---

## 🎯 What You Gain From This Vault

Most AI coding assistants fail not because they lack intelligence — they fail because they lack **procedural, domain-specific discipline**. This vault fixes that.

### For Individual Developers
- **Stop writing the same boilerplate.** Every skill contains reusable, production-grade patterns you can drop into any project.
- **Eliminate research time.** Skills embed command references, error handling strategies, and idiomatic patterns so you don't need to look things up.
- **Code with confidence.** Security, performance, and correctness rules are built into every domain skill.

### For AI Agents & Automated Pipelines
- **Zero-shot domain mastery.** Agents injected with these skills know the exact flags, options, and architectural patterns used in production systems.
- **Deterministic behavior.** Skills provide explicit rules rather than suggestions, so agents produce consistent, verifiable outputs.
- **Self-correcting loops.** GSD and RalphLoop-compatible skills verify their own output and retry until all conditions pass.

### For Engineering Teams
- **Shared standards.** Install the same skill set across your team's AI agents to enforce consistent architecture, security, and coding conventions.
- **Faster onboarding.** New members (and their AI tools) inherit years of accumulated best practices on day one.
- **Compliance & audit trails.** Security, accessibility, and compliance skills generate evidence-ready outputs for SOC2, GDPR, and ISO 27001.

---

## 📊 Complete Skills Inventory Table

This table shows every domain in the vault, the exact number of skills it contains, and what each domain helps you accomplish.

| # | Domain | Skills | What It Does For You |
|:---:|:---|:---:|:---|
| 🎛️ | **[Universal Orchestration](./custom-skills/)** (`custom-skills`) | **3** | Routes any task to the right skill domain. `select-skill` deconstructs complex tasks and picks the best tool. `ask-question` acts as a Socratic architect, clarifying your project requirements before writing a single line of code. `save-token` coordinates the Memory-First 5-Pillar Token-Saving Mega-Engine (Anima/AgentKits memory offloading + Ponytail + Graphify + RTK + Headroom + Caveman + Turn Tracker `/compact` alerts) to eliminate 200k+ chat history context re-transmissions and slash token burn by 70–95% across all tasks. |
| 01 | **[3D Modeling & Rendering](./01-3d-modeling-and-rendering/)** | **7** | Automate Blender via Python, convert 3D file formats (GLTF, OBJ, FBX, STL), process meshes, train 3D Gaussian Splats, build Three.js / WebGPU scenes, and generate AI 3D models from text or images. |
| 02 | **[Audio & Sound Engineering](./02-audio-and-sound-engineering/)** | **51** | Separate vocal and instrumental stems, master audio to broadcast loudness standards (LUFS), transcribe with speaker diarization, clone voices, synthesize TTS audiobooks and podcasts, and integrate live audio streaming APIs. |
| 03 | **[Autonomous Agents & AI](./03-autonomous-agents-and-ai/)** | **218** | Design multi-agent swarm architectures, build evaluation and regression benchmarking suites, optimize prompt caching to slash LLM costs, manage agent memory and tool execution sandboxes, and enforce human-in-the-loop approval gates. |
| 04 | **[Backend Architecture & APIs](./04-backend-architecture-and-apis/)** | **156** | Scaffold production microservices in Go, Rust, Python (FastAPI), Java (Spring), and Node.js. Write OpenAPI v3 specs, implement OAuth2/JWT auth, design event-driven CQRS systems, and prevent race conditions with distributed locking. |
| 05 | **[Business, Marketing & SEO](./05-business-marketing-and-seo/)** | **120** | Build programmatic SEO engines, generate JSON-LD schema markup, optimize for AI answer engines (GEO/AEO), audit Core Web Vitals, write high-converting copy, detect and improve AI-generated text, and track content ROI. |
| 06 | **[Code Quality, Security & Compliance](./06-code-quality-security-and-compliance/)** | **164** | Run penetration testing playbooks (SQLi, XSS, SSRF, IDOR, JWT attacks), audit cloud IAM for privilege escalation, harden Docker containers, generate SOC2 / GDPR / ISO 27001 compliance reports, and perform code audits for memory leaks and deadlocks. |
| 07 | **[Codebase Intelligence & Graphs](./07-codebase-intelligence-and-graphs/)** | **11** | Build offline AST knowledge graphs of your entire project (Graphify), onboard AI agents into large codebases instantly, detect architectural violations, generate dependency call graphs, and calculate complexity metrics. |
| 08 | **[Databases & Data Engineering](./08-databases-and-data-engineering/)** | **208** | Tune PostgreSQL indexes and query plans, write zero-downtime schema migrations, build dbt/BigQuery transformation pipelines, optimize vector databases for AI search, set up Redis caching strategies, and automate backup and disaster recovery. |
| 09 | **[DevOps, Cloud & Infrastructure](./09-devops-cloud-and-infrastructure/)** | **87** | Provision cloud infra with Terraform/OpenTofu, build Kubernetes Helm charts, create multi-stage CI/CD pipelines (GitHub Actions, CircleCI), reduce AWS cloud bills by detecting orphaned resources, and configure Vercel deployments and edge functions. |
| 10 | **[Frontend, UI/UX & Design Systems](./10-frontend-uiux-and-design-systems/)** | **262** | Build accessible React / Next.js / Vue / Svelte interfaces, enforce design token systems (Tailwind, Shadcn), audit WCAG 2.1 AA/AAA compliance, implement server-side streaming and React Server Components, and eliminate generic AI visual clichés with high-craft UI patterns. |
| 11 | **[General Developer Utilities](./11-general-developer-utilities/)** | **2,044** | The core engine of the vault. Full specialist playbooks for 20+ programming languages (Python, Go, Rust, TypeScript, C++, Java, Kotlin, C#, PHP, Ruby, Elixir, Scala), 15+ frameworks, shell scripting, documentation generation, file format parsers, and hundreds of daily developer workflow tools. |
| 12 | **[Mobile & Cross-Platform](./12-mobile-and-cross-platform/)** | **51** | Build 60 FPS native mobile UIs with Flutter (Bloc/Riverpod), Android Jetpack Compose, SwiftUI/Swift 6, and React Native. Configure EAS / Fastlane CI/CD pipelines for App Store and Google Play submissions. Handle offline sync, push notifications, and native module bridging. |
| 13 | **[Science, Genomics & Bioinformatics](./13-science-and-bioinformatics/)** | **39** | Query AlphaFold, AlphaGenome, UniProt, ChEMBL, PubMed, Ensembl, and ClinVar databases. Analyze genetic variant impacts, visualize 3D biomolecular structures, perform cheminformatics calculations, and synthesize academic literature from hundreds of preprints. |
| 14 | **[Senior Engineering Best Practices](./14-senior-engineering-best-practices/)** | **25** | Apply defensive minimalism (YAGNI), write immutable architecture decision records (ADRs), prevent context drift in long-running agent sessions, structure cross-team technical initiatives, and conduct constructive senior-level code reviews. |
| 15 | **[Spec-Driven Project Management (GSD)](./15-spec-driven-project-management-gsd/)** | **72** | Run the full Get Stuff Done (GSD) lifecycle: clarify requirements → score ambiguity → plan atomically → execute with Git commits → verify against UAT criteria → ship. Prevents scope creep and guarantees verifiable delivery. |
| 16 | **[Testing, QA & Debugging](./16-testing-qa-and-debugging/)** | **134** | Write flaky-free Playwright E2E suites, set up Jest / Pytest / JUnit with parameterized fixtures and 80%+ coverage gates, run K6 load tests under realistic profiles, debug with hypothesis-driven MREs, and test API contracts across microservices with Pact. |
| 17 | **[UI Animation & Motion Graphics](./17-ui-animation-and-motion-graphics/)** | **44** | Orchestrate complex GSAP timelines and scroll-triggered reveals, implement React View Transitions, design spring-physics-based gestures, integrate Lottie vector animations, run 60 FPS animation performance audits, and build 2D physics simulations with Matter.js. |
| 18 | **[Video, Photo Editing & VFX](./18-video-and-photo-editing-vfx/)** | **958** | Render personalized programmatic videos with Remotion (React-to-video), build complex FFmpeg filter graphs (hardware-accelerated transcoding, audio crossfades, chroma-keying, LUT grading), generate AI UGC ad videos at scale, script DaVinci Resolve and After Effects, and batch-process images. |
| | **📦 Total Across All Domains** | **4,761** | **Complete full-stack, creative, and scientific engineering intelligence in one vault.** |

---

## 🗂️ Domain-by-Domain Breakdown

A detailed walkthrough of what each domain contains and the real-world tasks you can accomplish with it:

---

### 🎛️ Universal Orchestration (`custom-skills/`) — 3 Skills

These three skills act as the **front door** of the entire vault. They are designed to be installed alongside any other domain and work automatically on every task.

| Skill | Trigger | What It Does |
|:---|:---|:---|
| `select-skill` | `/select skill <task>` | Deconstructs any complex task across all 18 domains, selects the top-ranked skill per domain, shows alternatives, and waits for your confirmation before executing. |
| `ask-question` | `/ask question <idea>` | Socratic interrogation engine — asks targeted, numbered clarification questions about architecture, edge cases, data models, and UI flow. Produces a phase-by-phase blueprint and delegates to `select-skill`. |
| `save-token` | `save token`, `/save token`, `headroom`, `caveman` | Memory-First Multi-Engine Token-Saver & Turn Tracker — coordinates **Memory Offloading** (`anima-memory`, `agentkits-memory`, `claude-mem`), **Ponytail** (YAGNI minimalism), **Graphify** (zero-token local AST graph), **RTK** (terminal output compression), **Headroom** (input log pruner), **Caveman** (ultra-terse output protocol), and **Turn Cadence Tracker** (monitors turns and triggers prominent alerts at Turn 10 to run `/compact`). Cuts AI token usage by 70–95% across ALL domains. |

**When to use:**
> You have a complex task like *"Build a real-time collaborative whiteboard with authentication"* but you're not sure where to start. Run `/ask question` and the agent will methodically extract every missing requirement and produce a complete action plan. Then type `save token` before any heavy task to slash token consumption automatically.

---

### 01. 3D Modeling & Rendering — 7 Skills

**What you can build and automate:**
- Run headless Blender Python sessions to batch-render product shots, configure lighting rigs, animate turntables, and apply geometry node modifiers.
- Convert between 3D formats (OBJ → Draco-compressed GLTF, FBX → GLB, STL → USDZ) while preserving all materials and UV maps.
- Train, process, and deploy 3D Gaussian Splat models for ultra-fast real-time 3D web viewers.
- Compose rich Three.js / React Three Fiber / WebGPU scenes with PBR materials, post-processing passes, and responsive camera controls.

**Key skills:** `blender-python-automation`, `3d-file-converter`, `gaussian-splatting-3dgs`, `web-3d-scene-composer`, `meshy-3d-agent`, `3d-geometry-processing`, `3d-model-generation`

---

### 02. Audio & Sound Engineering — 51 Skills

**What you can build and automate:**
- Isolate clean vocal and instrumental stems from any mixed audio track using Demucs/Spleeter with phase-cancellation prevention.
- Master podcast episodes to broadcast standards: normalize LUFS, apply multi-band compression, dynamic EQ, and peak limiting.
- Transcribe recordings at word-level timestamps with speaker diarization (who said what, when) in 50+ languages.
- Clone voices, generate expressive TTS narration, create multi-speaker synthetic podcasts, and dub video content into other languages.
- Stream bidirectional live audio for real-time voice agent applications using Azure VoiceLive and WebRTC.

**Key skills:** `audio-cleanup-stems`, `audio-master-engine`, `audio-transcriber`, `ai-voice-studio`, `elevenlabs-text-to-speech`, `elevenlabs-voice-changer`, `ai-podcast-voiceover`, `ai-audiobook-narration`, `whisperx`, `fal-audio`

---

### 03. Autonomous Agents & AI — 218 Skills

**What you can build and automate:**
- Design multi-agent swarms with hub-and-spoke, sequential, or hierarchical communication topologies.
- Build evaluation harnesses that measure task completion rates, hallucination frequency, and performance regression across model upgrades.
- Optimize prompt caching and KV-cache strategies to cut LLM API costs by up to 90% and reduce round-trip latency.
- Implement persistent agent memory: short-term working context, episodic logs, and semantic long-term retrieval over vector stores.
- Harden agent tool execution against prompt injection, credential leaks, and sandbox escapes.

**Key skills:** `agent-creator`, `multi-agent-task-orchestrator`, `agent-eval`, `agent-memory-systems`, `agent-security-hardening`, `llm-prompt-optimizer`, `prompt-caching-strategy`, `crewai`, `langgraph`, `rtk`, `claude-mem`, `anima-memory`, `agentkits-memory`, `muscle-memory`, `mem0-agent`, `headroom`, `caveman`, `awesome-mcp-servers`, `vibe-kanban`, `gstack`

---

### 04. Backend Architecture & APIs — 156 Skills

**What you can build and automate:**
- Scaffold production-grade microservices in Go (Gin/Fiber), Rust (Axum/Actix), Python (FastAPI), Java (Spring Boot), and Node.js (NestJS).
- Design OpenAPI v3 / AsyncAPI specs from scratch and validate request/response schemas with Pydantic, Zod, and Protobuf.
- Implement complete auth flows: OAuth2, OpenID Connect, JWT signing & rotation, session management, RBAC/ABAC.
- Build event-driven systems with Kafka, RabbitMQ, and Redis Streams. Apply CQRS and Event Sourcing patterns.
- Prevent race conditions and deadlocks with optimistic concurrency, distributed row locking, and transactional outboxes.

**Key skills:** `fastapi-pro`, `golang-pro`, `rust-pro`, `api-design-principles`, `auth-implementation-patterns`, `event-sourcing-architect`, `cqrs-implementation`, `api-rate-limit-handler`, `openapi-spec-generator`

---

### 05. Business, Marketing & SEO — 120 Skills

**What you can build and automate:**
- Build programmatic SEO engines generating thousands of optimized landing pages from structured data templates.
- Generate JSON-LD schema markup (Article, FAQ, Product, SoftwareApplication, HowTo, BreadcrumbList) for all page types.
- Optimize content for AI answer engines — Perplexity, ChatGPT Search, Gemini Search — to maximize brand citations and AI citability (GEO/AEO).
- Audit Core Web Vitals (LCP, INP, CLS), identify crawl budget issues, fix canonical loops, and resolve indexing problems.
- Write, detect, and improve AI-generated content to remove robotic tone and pass editorial quality standards.

**Key skills:** `seo-aeo-orchestrator`, `geo-citability`, `programmatic-seo`, `schema-markup-generator`, `page-cro`, `copywriting-psychologist`, `ai-content-detector`, `ai-content-improver`, `writing-guidelines`

---

### 06. Code Quality, Security & Compliance — 164 Skills

**What you can build and automate:**
- Run automated penetration testing workflows for SQLi, XSS, SSRF, IDOR, JWT algorithm confusion, CORS misconfigurations, and race conditions.
- Audit AWS, GCP, and Azure IAM policies for privilege escalation vectors and overly permissive resource access.
- Harden Docker images: distroless base images, non-root execution, read-only root filesystems, dropped Linux capabilities.
- Generate SOC2 Type II, ISO 27001, and GDPR compliance gap reports with automated evidence collection steps.
- Perform deep code reviews checking for memory leaks, deadlocks, silent exception suppression, and unvalidated input paths.

**Key skills:** `hunt-sqli`, `hunt-xss`, `hunt-ssrf`, `hunt-idor`, `hunt-auth-bypass`, `cloud-iam-deep`, `container-hardening`, `linux-hardening`, `soc2-compliance`, `gdpr-compliance`, `code-audit`

---

### 07. Codebase Intelligence & Graphs — 11 Skills

**What you can build and automate:**
- Build an offline knowledge graph of your entire project using Tree-Sitter AST parsers across 28 languages (Graphify). Query it in natural language without re-reading source files every turn.
- Onboard AI agents into unfamiliar monorepos instantly with zero hallucinated file paths or made-up imports.
- Detect architectural boundary violations: presentation layer directly importing database models, circular dependencies, and coupling hotspots.
- Generate full import/export call graphs and calculate cyclomatic complexity, afferent/efferent coupling, and instability index.

**Key skills:** `graphify`, `understand`, `understand-diff`, `understand-knowledge`, `understand-dashboard`, `understand-domain`, `understand-explain`

---

### 08. Databases & Data Engineering — 208 Skills

**What you can build and automate:**
- Tune PostgreSQL query plans with `EXPLAIN ANALYZE`, add missing B-Tree/GIN/BRIN indexes, configure autovacuum, and set up connection pooling.
- Write safe zero-downtime schema migrations: additive columns, backfill batches, constraint swaps, and rollback procedures.
- Build modern data stack pipelines with dbt (BigQuery, Snowflake, Redshift) including incremental models and data quality tests.
- Optimize vector databases (pgvector, Qdrant, Pinecone, Milvus) for high-recall hybrid BM25 + dense embedding search.
- Architect automated backup pipelines, point-in-time recovery (PITR), and cross-region disaster recovery for PostgreSQL, MySQL, and MongoDB.

**Key skills:** `postgres-best-practices`, `postgresql-optimization`, `dbt-transformation-patterns`, `bigquery-optimization`, `database-migrations-sql-migrations`, `vector-database-engineer`, `redis-patterns`, `neon-postgres`, `clickhouse-io`

---

### 09. DevOps, Cloud & Infrastructure — 87 Skills

**What you can build and automate:**
- Provision production-grade AWS, GCP, and Azure infrastructure with reusable Terraform modules including remote state locking and drift detection.
- Build Kubernetes manifests, Helm charts, StatefulSets, Ingress controllers, NetworkPolicies, and Horizontal Pod Autoscalers.
- Create multi-stage GitHub Actions / CircleCI pipelines with artifact caching, matrix builds, container scanning, and automated rollbacks.
- Deploy to Vercel: configure Edge Functions, ISR, middleware, preview deployments, and custom domain routing with zero downtime.
- Identify and clean up orphaned AWS resources (unattached EBS volumes, idle load balancers, forgotten EC2 instances) to reduce cloud spend.

**Key skills:** `kubernetes-architect`, `terraform-specialist`, `terraform-aws`, `github-actions-advanced`, `aws-cost-cleanup`, `service-mesh-expert`, `vercel-deployment`, `vercel-optimize`, `docker-management`, `argocd-gitops`

---

### 10. Frontend, UI/UX & Design Systems — 262 Skills

**What you can build and automate:**
- Scaffold React Server Components (RSC) with streaming SSR, Suspense boundaries, and optimistic UI updates.
- Enforce design token systems (Tailwind CSS, Shadcn/ui, Radix) across dark/light themes, responsive breakpoints, and typography scales.
- Build accessible interfaces meeting WCAG 2.1 AA/AAA: keyboard navigation, ARIA roles, color contrast ratios, and screen reader compatibility.
- Eliminate "AI-generated slop" UIs with high-craft editorial layouts, micro-typography, whitespace discipline, and visual hierarchy rules.
- Create virtualized data tables, complex multi-step forms, real-time dashboards, and drag-and-drop interfaces.

**Key skills:** `react-best-practices`, `nextjs-app-router-patterns`, `tailwind-design-system`, `shadcn`, `ui-a11y`, `better-ui`, `anti-ui-slop`, `zustand-store-ts`, `web-design-guidelines`, `composition-patterns`, `mattpocock-skills`

---

### 11. General Developer Utilities — 2,044 Skills

The massive core of the vault. Contains specialist playbooks for every major programming language, framework, and daily developer workflow.

**Programming Languages (specialist-level playbooks):**

| Language | Skill | Coverage |
|:---|:---|:---|
| Python | `python-pro` | Async patterns, generators, type safety, packaging, testing |
| Go | `golang-pro` | Concurrency, channels, interfaces, standard library patterns |
| Rust | `rust-pro` | Ownership, lifetimes, async Tokio, memory safety, FFI |
| TypeScript | `typescript-pro` | Advanced generics, branded types, module patterns, decorators |
| C++ | `cpp-pro` | RAII, templates, STL, modern C++20/23, memory management |
| Java | `java-pro` | Spring patterns, streams, generics, concurrency, GC tuning |
| Kotlin | `kotlin-patterns` | Coroutines, sealed classes, extension functions, multiplatform |
| C# | `csharp-pro` | LINQ, async/await, records, pattern matching, Blazor |
| PHP | `php-pro` | Generators, SPL, modern OOP, composer, performance |
| Ruby | `ruby-pro` | Metaprogramming, blocks, gems, Rails idioms |
| Elixir | `elixir-pro` | OTP, GenServer, pattern matching, Phoenix LiveView |
| Scala | `scala-pro` | Functional patterns, Akka, type classes, cats |

**Frameworks & Tools:** `django-patterns`, `fastapi-patterns`, `springboot-patterns`, `laravel-expert`, `nestjs-expert`, `rails-patterns`, `bash-pro`, `powershell-windows`, `linux-shell-scripting`, `writing-skills`, `wiki-architect`, `xlsx`, `pdf`, `repomix` and 2,000+ more.

---

### 12. Mobile & Cross-Platform — 51 Skills

**What you can build and automate:**
- Build cross-platform 60 FPS mobile UIs from a single Dart codebase (Flutter) with Bloc or Riverpod state management.
- Implement modern Android UIs using Jetpack Compose, Kotlin Coroutines, Hilt dependency injection, and Room database.
- Develop native iOS apps with Swift 6 strict concurrency, SwiftUI declarative views, Combine, and HealthKit integrations.
- Configure Expo Router, write native modules in Swift/Kotlin for React Native, and set up EAS Build + EAS Submit CI/CD pipelines.
- Handle offline-first sync, background push notifications, biometric authentication, and deep links across all platforms.

**Key skills:** `flutter-expert`, `android-jetpack-compose-expert`, `swiftui-expert-skill`, `react-native-architecture`, `react-native-skills`, `expo-deployment`, `dart-flutter-patterns`

---

### 13. Science, Genomics & Bioinformatics — 39 Skills

**What you can build and automate:**
- Query and analyze data from AlphaFold (protein structure), AlphaGenome (variant impact), UniProt (protein function), ChEMBL (drug compounds), Ensembl (genome assembly), and ClinVar (genetic disease variants).
- Analyze the regulatory and functional consequences of DNA single-nucleotide polymorphisms (SNPs) using AlphaGenome models.
- Visualize biomolecular structures interactively in 3D (PDB files, protein-ligand complexes, binding pockets).
- Perform cheminformatics: parse SMILES strings, generate molecular fingerprints, calculate molecular descriptors with RDKit.
- Synthesize and cross-reference hundreds of academic papers from PubMed, arXiv, Europe PMC, and OpenAlex.

**Key skills:** `alphagenome-single-variant-analysis`, `biomolecular-structure-viewer`, `cheminformatics-core`, `rdkit-general`, `pubmed-database`, `literature-search-arxiv`, `alphafold-database-fetch-and-analyze`

---

### 14. Senior Engineering Best Practices — 25 Skills

**What you can build and automate:**
- Apply defensive minimalism: strip speculative abstractions, eliminate unused dependencies, and prefer standard library patterns (YAGNI/Ponytail).
- Write architecture decision records (ADRs) that capture the trade-offs and rationale behind key technical decisions.
- Manage AI agent context budgets: prevent context pollution, structure compact state handoffs, and enforce working-memory boundaries.
- Conduct systematic, evidence-based root-cause debugging rather than trial-and-error shotgun changes.
- Design systems within explicit resource constraints (memory budgets, latency SLAs, CPU quotas).

**Key skills:** `code-simplification`, `clean-code`, `context-engineering`, `debugging-and-error-recovery`, `architecture-decision-records`, `constraint-driven-development`, `code-review-and-quality`

---

### 15. Spec-Driven Project Management (GSD) — 72 Skills

**The GSD (Get Stuff Done) lifecycle — the structured way to build anything with an AI agent:**

```
  DISCUSS → SPEC → PLAN → EXECUTE → VERIFY → SHIP
     ↑                                         |
     └─────────── Retry if UAT fails ──────────┘
```

**What you can accomplish:**
- Prevent scope creep by scoring ambiguity and requiring explicit specification sign-off before any code is written.
- Break large features into atomic implementation tasks, each committed to Git with descriptive messages.
- Run formal User Acceptance Testing (UAT) comparing what was built against what was specified.
- Archive completed milestones cleanly, generate release changelogs, and prep PR-ready branches.
- Manage multiple parallel workstreams with independent progress tracking across a team.

**Key skills:** `gsd-discuss-phase`, `gsd-spec-phase`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, `gsd-audit-uat`, `gsd-complete-milestone`, `gsd-autonomous`, `gsd-ship`, `gsd-workstreams`

---

### 16. Testing, QA & Debugging — 134 Skills

**What you can build and automate:**
- Author reliable, flake-resistant Playwright E2E test suites with automatic failure screenshots, trace recordings, and network request interception.
- Configure Jest (TypeScript), Pytest (Python), and JUnit 5 (Java) test suites with fixtures, factories, and parameterized test tables.
- Run K6 load tests under realistic ramp-up profiles to find the maximum RPS your system can sustain before degrading.
- Write Pact consumer-driven contract tests to prevent breaking API changes from reaching production.
- Debug production incidents with minimal reproducible examples (MREs), binary search bisection, and structured hypothesis tracking.

**Key skills:** `playwright-skill`, `pytest-skill`, `jest-skill`, `junit-5-skill`, `k6-load-testing`, `systematic-debugging`, `api-contract-testing`, `rtk`

---

### 17. UI Animation & Motion Graphics — 44 Skills

**What you can build and automate:**
- Compose complex, orchestrated GSAP animation timelines with scroll-triggered reveals, text splitting, and SVG morphing.
- Implement React View Transitions for seamless page-to-page navigation animations in Next.js and React Router.
- Design spring-physics-based gesture interactions (swipe, pinch, drag) for mobile and touch-screen interfaces.
- Integrate lightweight Lottie / dotLottie vector animations that run at native FPS with tiny file sizes.
- Audit and fix stuttering animations: eliminate layout thrashing, force GPU compositing layers, and stay in the 60/120 FPS budget.

**Key skills:** `gsap-core`, `gsap-timeline`, `react-view-transitions`, `animation-performance`, `dotlottie-web`, `matter-js-physics`, `tsparticles-engine`, `animejs-animation`

---

### 18. Video, Photo Editing & VFX — 958 Skills

**What you can build and automate:**
- Render personalized programmatic video templates in React using Remotion, with dynamic text, charts, images, and audio — then batch-render to MP4 at scale.
- Build FFmpeg filter graphs: multi-track audio mixing, hardware-accelerated H.264/H.265 transcoding, chroma keying, picture-in-picture, custom LUT color grading, xfade transitions.
- Generate AI UGC (User Generated Content) video ads using Kling, Seedance, Veo 3, and Runway APIs with viral hook formulas and auto-generated animated subtitles.
- Script DaVinci Resolve and After Effects programmatically: create timelines, apply effects, export EDL/XML, and batch-process footage.
- Batch-process photos: background removal, watermarking, color harmonization, super-resolution upscaling, and format conversion.

**Key skills:** `remotion-video-creation`, `ffmpeg-master-engine`, `ai-ugc-ad-video`, `davinci-resolve-mcp`, `after-effects-mcp`, `seedance-2-creative-director`, `image-studio`, `pillow-photo-engine`, `video-editing`

---

## ⚡ Token-Saving Power Tools

These skills are specifically engineered to reduce the AI tokens consumed per coding session, saving you money and making your agent faster:

### 🦀 RTK — Rust Token Killer
**Location:** `03-autonomous-agents-and-ai/rtk/` and `16-testing-qa-and-debugging/rtk/`

RTK is a high-performance Rust CLI proxy that strips verbose output from build tools, test runners, and linters before it reaches the LLM context window.

| Command | What It Strips | Token Savings |
|:---|:---|:---:|
| `rtk test <cmd>` | Passing test output, progress bars, timing data | **60–90%** |
| `rtk diff` | Surrounding context lines, whitespace diffs | **40–70%** |
| `rtk err <cmd>` | Non-error log lines from build output | **50–80%** |
| `rtk gain` | Shows token savings report for your session | — |

### 🕸️ Graphify — AST Knowledge Graph Engine
**Location:** `07-codebase-intelligence-and-graphs/graphify/`

Graphify uses local Tree-Sitter parsers to build an offline semantic graph of your entire project across 28 programming languages. The agent queries the graph instead of re-reading source files on every turn.

| Command | What It Does | Token Savings |
|:---|:---|:---:|
| `graphify update .` | Builds / refreshes the project graph | Setup |
| `graphify explain "<component>"` | Explains a function's callers and callees | **70–85%** |
| `/graphify .` | Loads the graph into the agent context | Per-session |

---

## 🎛️ Universal Orchestration Skills

Located in [`custom-skills/`](./custom-skills/), these three skills work with **every other domain** and should always be installed first.

### `select-skill` — Multi-Domain Task Router
**Trigger:** `/select skill <your task description>`

**How it works:**
1. You describe your task in plain English.
2. The skill analyzes your task and identifies which of the 18 domains are relevant.
3. It selects the single best-matched skill per domain with a justification for why it beats alternatives.
4. It **pauses and shows you the plan** before executing — you confirm or redirect.

**Example:**
```
/select skill Build a secure file upload API in FastAPI with S3 storage and virus scanning
```
→ Agent selects: `fastapi-pro` (Backend) + `aws-s3` (DevOps) + `api-security` (Security)
→ Waits for your confirmation before proceeding.

---

### `ask-question` — Socratic Architecture Engine
**Trigger:** `/ask question <your project idea>`

**How it works:**
1. You describe a project concept or complex problem.
2. The skill generates targeted clarification questions about architecture, data models, edge cases, auth requirements, and UI flow.
3. After you answer, it synthesizes a formal, phased execution blueprint.
4. It automatically hands off to `select-skill` to begin implementation.

**Example:**
```
/ask question I want to build a real-time collaborative drawing app
```
→ Asks: "Should edits sync in <100ms or is eventual consistency OK?", "Will you support undo/redo history?", "Mobile or desktop or both?"
→ Produces: a 5-phase implementation roadmap before writing any code.

---

### `save-token` — Memory-First Multi-Engine Token-Saver & Turn Tracker
**Trigger:** `save token`, `/save token`, `save tokens`, `headroom`, `caveman`

**How it works:**
1. You type `save token` at the start of any message, then describe your task.
2. **Memory Offloading** condenses bloated chat context into compact local state files (`.ai/memory/`, `.planning/`), eliminating 200k+ token history re-transmissions.
3. **Headroom** compresses input context, bloated logs, and trims repetitive conversation turns by 40–70%.
4. **Graphify & Muscle-Memory** query local AST knowledge graphs and replay cached patterns with zero AI tokens.
5. **RTK** wrappers activate: `rtk diff`, `rtk test`, `rtk err`, `rtk git` compress terminal outputs to essential lines before reaching the LLM context.
6. **Ponytail & Caveman** enforce YAGNI minimalism and strip conversational filler, delivering direct, high-density responses.
7. **Turn Tracker & Automated /compact Alerts:** Monitors turns in the current compaction cycle. At Turn 10 (and multiples of 10), prominently alerts you to type `/compact` in the chat box to wipe transcript bloat with zero memory loss.

**Example:**
```
save token. Refactor the auth module to use JWT refresh tokens.
```
→ Agent: engages Headroom + Graphify + RTK + Ponytail + Caveman.
→ Estimated savings: **50–85% fewer tokens** across the entire task.

| Scenario | Token Reduction |
|:---|:---:|
| Reading large codebases | **70–85%** |
| Debugging test failures | **60–80%** |
| Git diff analysis | **60–85%** |
| Writing code & refactoring | **50–70%** |
| General tasks & documentation | **40–60%** |

---

## 🌐 Global Availability & Multi-Account Persistence

All skills in this vault are designed to operate **globally across your operating system** and **persist across Google accounts**:

- **Google Account Agnostic:** In Antigravity IDE and CLI, skills installed in `~/.gemini/skills/` are tied to your local workstation profile, not your Google login. When you switch or rotate Google accounts, all 4,761+ skills remain 100% active, accessible, and intact.
- **Universal Directory Triggering:** You can open a terminal in **any folder or drive** (e.g., `C:\`, `D:\projects\`, nested repos) and trigger any skill via command slash (e.g. `/select-skill`, `/ask-question`, `/save-token`) or natural language. Antigravity discovers and executes them immediately.
- **Cross-Account Token Protection:** The `save-token` orchestrator engages local tools (Ponytail minimalism, Graphify AST analysis, and RTK command compression) that run directly on your hardware without consuming your Google account quota, slashing token burn on every account you use.

---

## 🚀 How to Install

### Prerequisites
- **Python 3.8+** (no extra packages required — uses only the standard library)
- An AI agent environment: Antigravity, Gemini CLI, Claude Code, or Cursor

---

### Option 1: Python Installer (Recommended)

The included `install_skills.py` script copies skills into your global agent directory. It performs a **complete standalone physical copy** — no symlinks, no network calls.

**Step 1 — Clone the repository:**
```bash
# Clone to any temporary location (Downloads, /tmp, etc.)
git clone https://github.com/aniketpal15/Antigravity-skills.git
cd Antigravity-skills
```

**Step 2 — Run the installer:**
```bash
# Install ALL 4,761 skills to ~/.gemini/skills/ (full vault)
python install_skills.py

# OR: Install only the domains you need
python install_skills.py backend        # Backend Architecture (156 skills)
python install_skills.py frontend       # Frontend UI/UX (262 skills)
python install_skills.py security       # Security & Compliance (164 skills)
python install_skills.py database       # Databases (208 skills)
python install_skills.py devops         # DevOps & Cloud (87 skills)
python install_skills.py video          # Video & VFX (958 skills)
python install_skills.py mobile         # Mobile Dev (51 skills)
python install_skills.py testing        # Testing & QA (134 skills)
python install_skills.py gsd            # GSD Workflow (72 skills)
python install_skills.py agents         # AI Agents (214 skills)
python install_skills.py custom         # Orchestration (3 skills)
```

**Step 3 — Verify installation:**
```bash
# Windows
dir "$HOME\.gemini\skills"

# macOS / Linux
ls ~/.gemini/skills
```

You should see your skill folders listed. The agent will automatically index them on the next session start.

**Step 4 — Delete the cloned folder (optional but recommended):**

> [!TIP]
> Once the installer finishes with `Successfully installed XXXX skills to ~/.gemini/skills`, **the cloned folder is no longer needed**. The installer uses `shutil.copytree()` which makes a full, permanent, independent copy of every file. You can safely delete the entire cloned repository from Downloads or wherever you saved it. Your installed skills remain intact in `~/.gemini/skills/` permanently.
>
> To get updates in the future, simply re-clone and re-run the installer — it merges updates with `dirs_exist_ok=True`.

---

### Option 2: Manual Copy

If you prefer not to use Python, copy domain folders directly using your OS tools.

**Windows (PowerShell):**
```powershell
# Always install the orchestration skills first
Copy-Item -Recurse "custom-skills\*" "$HOME\.gemini\skills\"

# Then add any domains you need
Copy-Item -Recurse "04-backend-architecture-and-apis\*" "$HOME\.gemini\skills\"
Copy-Item -Recurse "16-testing-qa-and-debugging\*" "$HOME\.gemini\skills\"
Copy-Item -Recurse "06-code-quality-security-and-compliance\*" "$HOME\.gemini\skills\"
```

**macOS / Linux (bash):**
```bash
# Always install the orchestration skills first
cp -r custom-skills/* ~/.gemini/skills/

# Then add any domains you need
cp -r 04-backend-architecture-and-apis/* ~/.gemini/skills/
cp -r 16-testing-qa-and-debugging/* ~/.gemini/skills/
cp -r 06-code-quality-security-and-compliance/* ~/.gemini/skills/
```

---

### Option 3: Claude Code Setup

Place skills inside `~/.claude/skills/` or your project's `.claude/` directory:

```bash
mkdir -p ~/.claude/skills

# Install orchestration skills
cp -r custom-skills/* ~/.claude/skills/

# Install desired domains
cp -r 15-spec-driven-project-management-gsd/* ~/.claude/skills/
cp -r 14-senior-engineering-best-practices/* ~/.claude/skills/
```

---

### Option 4: Project-Local Setup

Install skills only within a specific project so they apply only to that codebase:

```bash
cd your-project/
mkdir -p .skills

# Copy exactly the skills you want active for this project
cp -r /path/to/Antigravity-skills/04-backend-architecture-and-apis/fastapi-pro .skills/
cp -r /path/to/Antigravity-skills/16-testing-qa-and-debugging/playwright-skill .skills/
cp -r /path/to/Antigravity-skills/08-databases-and-data-engineering/postgres-best-practices .skills/
```

Your agent automatically detects and loads any skills placed in `./.skills/`.

---

## 🧬 Anatomy of a Skill

Every skill in the vault follows the same directory structure so agents load them consistently:

```
skill-name/
├── SKILL.md         ← Primary agent contract: YAML metadata + ordered procedural rules
├── README.md        ← Human-readable documentation with prerequisites and examples
├── references/      ← Deep technical guides, command cheat sheets, and architectural catalogs
│   ├── detailed-guide.md
│   └── patterns.md
├── scripts/         ← Executable helper scripts (Python, Bash, Node.js)
│   └── helper.py
└── tests/           ← Validation suites that verify the skill's own correctness
    └── test_skill.py
```

### Inside `SKILL.md`

Every `SKILL.md` starts with a YAML frontmatter block that tells the agent when and how to activate the skill:

```yaml
---
name: fastapi-pro
description: >
  Production-grade FastAPI architecture: async patterns, Pydantic v2 schemas,
  dependency injection, middleware design, and OpenAPI spec generation.
triggers:
  - "fastapi"
  - "python api"
  - "async backend"
---

# FastAPI Professional Architecture

## Non-Negotiable Rules
1. Never use blocking I/O inside async route handlers — always offload to a thread pool executor.
2. All schemas use Pydantic v2 `BaseModel` with `model_config = ConfigDict(strict=True)`.
3. Business logic lives in domain service classes, never directly inside route handler functions.
4. All external service calls are wrapped in retry logic with exponential backoff and circuit breakers.
...
```

---

## 🤖 Supported AI Agents & Platforms

| Agent / Platform | Skills Directory | Notes |
|:---|:---|:---|
| **Antigravity CLI** | `~/.gemini/skills/` | Full native support, auto-indexed |
| **Gemini CLI** | `~/.gemini/skills/` | Full native support |
| **Claude Code** | `~/.claude/skills/` | Full support via `.claude/` project config |
| **Cursor** | `.cursorrules` / `.cursor/rules/` | Reference `SKILL.md` files directly in rules |
| **CrewAI** | Custom agent tool path | Load `SKILL.md` contents as agent tool descriptions |
| **LangGraph / LangChain** | Custom loader | Embed `SKILL.md` content in system prompts per agent |

---


## 🤝 Contributing

We welcome community contributions. To ensure high quality across the vault, all submissions must follow these standards:

1. **Actionable rules, not vague suggestions.** Every instruction must be an imperative that an agent can execute without ambiguity.
2. **Standard directory layout.** Must include `SKILL.md` with valid YAML frontmatter and at least one entry in `references/`.
3. **Minimal dependencies.** Default to language standard library and platform-native tools. Add external dependencies only when no native equivalent exists.
4. **Cross-platform scripts.** All `scripts/` files must run on Windows (PowerShell/Python), macOS, and Linux without modification.
5. **No duplicate coverage.** Check existing domains before submitting to avoid overlapping with an existing skill.

---

## 📄 License

This collection is distributed under the **MIT License**. Individual skills, reference documents, and scripts may retain their respective upstream licenses as indicated in their folder-level notice files.

---

<p align="center">
  <b>Built for the next generation of autonomous software engineering.</b><br><br>
  ⭐ Star this repository to follow new skill releases and domain expansions!
</p>
