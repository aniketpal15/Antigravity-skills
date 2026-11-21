# 🌌 Antigravity Skills Vault

[![Total Skills](https://img.shields.io/badge/Total%20Skills-4%2C639%2B-blueviolet?style=for-the-badge&logo=codeforces)](https://github.com/aniketpal15/Antigravity-skills)
[![Domains](https://img.shields.io/badge/Domains-18%20Specialized%20%2B%20Orchestrators-blue?style=for-the-badge&logo=buffer)](https://github.com/aniketpal15/Antigravity-skills)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-orange?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20Code%20%7C%20Gemini%20%7C%20Cursor%20%7C%20CrewAI-red?style=for-the-badge)](https://github.com/aniketpal15/Antigravity-skills)

> **The definitive, battle-tested modular intelligence library for autonomous AI developer assistants, code agents, and modern software engineering swarms.**

The **Antigravity Skills Vault** transforms general-purpose LLMs (Claude 3.7/3.5, Gemini 2.0/Flash, GPT-4o, DeepSeek R1) into domain-expert engineers. Instead of relying on speculative prompt guessing, each skill injects deterministic procedural knowledge, industry best practices, concrete command patterns, scripts, and rigorous validation guardrails directly into your agent's execution context.

---

## 📑 Table of Contents

- [Why Antigravity Skills? (Key Benefits)](#-why-antigravity-skills-key-benefits)
- [Repository Architecture & Domain Inventory](#-repository-architecture--domain-inventory)
- [Universal Custom Orchestration Layer](#-universal-custom-orchestration-layer)
- [Comprehensive Domain Breakdown (01 - 18)](#-comprehensive-domain-breakdown)
  - [01. 3D Modeling and Rendering](#01-3d-modeling-and-rendering)
  - [02. Audio and Sound Engineering](#02-audio-and-sound-engineering)
  - [03. Autonomous Agents and AI Workflows](#03-autonomous-agents-and-ai-workflows)
  - [04. Backend Architecture and APIs](#04-backend-architecture-and-apis)
  - [05. Business, Marketing, and SEO](#05-business-marketing-and-seo)
  - [06. Code Quality, Security, and Compliance](#06-code-quality-security-and-compliance)
  - [07. Codebase Intelligence and Knowledge Graphs](#07-codebase-intelligence-and-knowledge-graphs)
  - [08. Databases and Data Engineering](#08-databases-and-data-engineering)
  - [09. DevOps, Cloud, and Infrastructure](#09-devops-cloud-and-infrastructure)
  - [10. Frontend, UI/UX, and Design Systems](#10-frontend-uiux-and-design-systems)
  - [11. General Developer Utilities](#11-general-developer-utilities)
  - [12. Mobile and Cross-Platform Engineering](#12-mobile-and-cross-platform-engineering)
  - [13. Science, Genomics, and Bioinformatics](#13-science-genomics-and-bioinformatics)
  - [14. Senior Engineering Best Practices](#14-senior-engineering-best-practices)
  - [15. Spec-Driven Project Management (GSD)](#15-spec-driven-project-management-gsd)
  - [16. Testing, QA, and Debugging](#16-testing-qa-and-debugging)
  - [17. UI Animation and Motion Graphics](#17-ui-animation-and-motion-graphics)
  - [18. Video, Photo Editing, and VFX Pipelines](#18-video-photo-editing-and-vfx-pipelines)
- [Installation and Deployment](#-installation-and-deployment)
  - [Universal Python Installer (Recommended)](#1-universal-python-installer-recommended)
  - [Antigravity & Gemini CLI Setup](#2-global-antigravity--gemini-setup)
  - [Claude Code & Cursor Setup](#3-claude-code--cursor-setup)
  - [Project-Local Setup (.skills/)](#4-project-local-setup)
- [Anatomy of a Skill](#-anatomy-of-a-skill)
- [License and Contribution](#-license-and-contribution)

---

## 🎯 Why Antigravity Skills? (Key Benefits)

When software agents fail, they rarely fail due to lack of raw reasoning; they fail due to **lack of domain-specific procedural discipline**. Antigravity Skills solve this by acting as verified expert SOPs (Standard Operating Procedures) designed specifically for code generation environments.

### 🌟 What You Get
1. **Zero-Shot Procedural Mastery:**
   Agents know the exact command flags, idiomatic architectural layouts, security risks, and optimization knobs across 18 specialized technical industries.
2. **Deterministic Security & Compliance:**
   Includes dedicated vulnerability hunters (SQLi, IDOR, SSRF, XSS, Race Conditions, JWT flaws), CIS Linux/Windows hardening recipes, SOC2/ISO27001 checklists, and accessibility audit engines.
3. **Radical Development Speed:**
   Eliminates boilerplate generation. Scaffold production-ready microservices, OpenAPI v3 contracts, Kubernetes deployments, complex GSAP timelines, and Playwright suites in single command cycles.
4. **Autonomous Spec-Driven Quality:**
   Native integration with **GSD (Get Stuff Done)** workflows and **RalphLoop** patterns ensures that agents do not stop at superficial edits; they plan, write atomic tests, execute, verify, and auto-correct until deliverables pass 100% of validation gates.
5. **Full Multimodal Coverage:**
   Bridges code with rich media: automate Blender Python rendering, 3D Gaussian Splatting, stem separation, FFmpeg demuxing/filters, Remotion programmatic video synthesis, and AI UGC video pipelines.

---

## 📊 Repository Architecture & Domain Inventory

The vault contains **4,639 total skills** distributed across 18 specialized technical domains plus a central orchestration gateway:

| Domain Folder | Focus & Category | Skill Count | Primary Toolsets & Frameworks |
| :--- | :--- | :---: | :--- |
| [`custom-skills/`](./custom-skills/) | **Universal Orchestration** | **2** | Socratic interrogation, task deconstruction, multi-domain skill routing |
| [`01-3d-modeling-and-rendering/`](./01-3d-modeling-and-rendering/) | **3D & Spatial Computing** | **7** | Three.js, Blender Python, Gaussian Splatting, GLTF/OBJ/FBX conversions |
| [`02-audio-and-sound-engineering/`](./02-audio-and-sound-engineering/) | **Audio, Voice & Music** | **51** | Stem separation, Foley SFX, ElevenLabs, WhisperX, Audio Mastering |
| [`03-autonomous-agents-and-ai/`](./03-autonomous-agents-and-ai/) | **Agent Systems & LLMs** | **212** | Multi-agent swarms, eval harnesses, LangGraph, prompt caching, memory banks |
| [`04-backend-architecture-and-apis/`](./04-backend-architecture-and-apis/) | **Backend & API Systems** | **156** | REST, GraphQL, gRPC, Go, Rust, Python FastAPI, Java Spring, Auth patterns |
| [`05-business-marketing-and-seo/`](./05-business-marketing-and-seo/) | **Marketing, SEO & Growth** | **119** | Programmatic SEO, schema markup, AI citability (GEO), copy psychology |
| [`06-code-quality-security-and-compliance/`](./06-code-quality-security-and-compliance/) | **Security, SAST & Audits** | **164** | Red teaming, threat modeling, CIS benchmarks, OWASP, ISO27001, SOC2 |
| [`07-codebase-intelligence-and-graphs/`](./07-codebase-intelligence-and-graphs/) | **Knowledge Graphs & AST** | **10** | Understand ASTs, code-to-graph mapping, semantic indexing, architectural layers |
| [`08-databases-and-data-engineering/`](./08-databases-and-data-engineering/) | **Databases & Pipelines** | **208** | PostgreSQL, BigQuery, Redis, MongoDB, ClickHouse, dbt, Spark, Kafka |
| [`09-devops-cloud-and-infrastructure/`](./09-devops-cloud-and-infrastructure/) | **Cloud, K8s & DevOps** | **85** | AWS, Azure, GCP, Docker, Kubernetes, Terraform, ArgoCD, GitHub Actions |
| [`10-frontend-uiux-and-design-systems/`](./10-frontend-uiux-and-design-systems/) | **Frontend & Design Systems** | **261** | React, Vue, Svelte, Tailwind, Shadcn UI, Design Tokens, WCAG Accessibility |
| [`11-general-developer-utilities/`](./11-general-developer-utilities/) | **Languages & Dev Tools** | **2,044** | 20+ languages, runtime patterns, CLI tooling, formatters, developer utilities |
| [`12-mobile-and-cross-platform/`](./12-mobile-and-cross-platform/) | **Mobile Development** | **50** | Flutter, React Native, iOS Swift/SwiftUI, Android Jetpack Compose, Expo |
| [`13-science-and-bioinformatics/`](./13-science-and-bioinformatics/) | **Science & Research** | **39** | AlphaGenome, UniProt, PubMed, ChEMBL, AlphaFold, Biomolecular 3D Viewers |
| [`14-senior-engineering-best-practices/`](./14-senior-engineering-best-practices/) | **Senior Engineering Standards** | **25** | Defensive minimalism (Ponytail), clean architecture, error recovery, ADRs |
| [`15-spec-driven-project-management-gsd/`](./15-spec-driven-project-management-gsd/) | **Spec-Driven GSD Workflows** | **72** | GSD lifecycle (discuss, plan, execute, verify), atomic milestone tracking |
| [`16-testing-qa-and-debugging/`](./16-testing-qa-and-debugging/) | **Testing & QA Verification** | **133** | Playwright E2E, Jest, Pytest, K6 load testing, systemic root-cause debugging |
| [`17-ui-animation-and-motion-graphics/`](./17-ui-animation-and-motion-graphics/) | **Motion & Creative UI** | **43** | GSAP, Framer Motion, Three.js shaders, Lottie, canvas physics, SVG paths |
| [`18-video-and-photo-editing-vfx/`](./18-video-and-photo-editing-vfx/) | **Video, VFX & Media Studio** | **958** | FFmpeg filtering, Remotion code-to-video, AI UGC video generation, DaVinci |
| **Total Across Vault** | | **4,639** | **Complete Full-Stack & Creative Engineering Arsenal** |

---

## 🎛️ Universal Custom Orchestration Layer

Located in [`custom-skills/`](./custom-skills/), these two orchestrator skills act as the central brain of any agent environment:

```
                  ┌─────────────────────────────────┐
                  │          USER PROMPT            │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
             ┌───────────────────────────────────────────┐
             │       custom-skills/ask-question          │
             │   Socratic interrogation & clarification   │
             └─────────────────────┬─────────────────────┘
                                   │
                                   ▼
             ┌───────────────────────────────────────────┐
             │       custom-skills/select-skill          │
             │  Capability router & confirmation gate    │
             └─────────────────────┬─────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [04-Backend]              [10-Frontend]              [06-Security]
  (FastAPI / Go)            (React / Tailwind)         (OWASP / SAST)
```

### 1. `custom-skills/select-skill`
* **Command:** `/select skill <task prompt>`
* **What it does:**
  - Performs intelligent multi-domain task deconstruction.
  - Detects which of the 18 technical domains are required (e.g. Backend + Database + Security).
  - Selects the single best skill per domain and surfaces high-value alternative options.
  - Pauses execution and requests interactive user confirmation before any tool execution begins.
* **Benefits:** Prevents tool runaway, eliminates hallucinated skills, and guarantees the exact toolchain aligns with developer intent.

### 2. `custom-skills/ask-question`
* **Command:** `/ask question <project idea or complex problem>`
* **What it does:**
  - Acts as a Socratic engineering architect.
  - Scrutinizes requirements, identifies ambiguities in data contracts, edge cases, auth models, and UI flow.
  - Asks focused, numbered multi-choice or clarifying questions.
  - Synthesizes findings into a formal, phase-by-phase execution blueprint and delegates directly to `select-skill`.
* **Benefits:** Saves hours of wasted rework by aligning architecture and specifications *before* code is written.

---

## 🔍 Comprehensive Domain Breakdown

Explore the detailed capabilities, representative skills, and real-world tasks for each of the 18 specialized domains:

---

### 01. 3D Modeling and Rendering
**Directory:** [`01-3d-modeling-and-rendering/`](./01-3d-modeling-and-rendering/) | **Skills Count:** 7 Skills

Focuses on programmatic 3D content creation, mesh processing, geometry analysis, headless 3D engine automation, and WebGL rendering.

* **Key Skills:**
  - `blender-python-automation`: Headless script generation for Blender 3.x/4.x (lighting, cameras, animation keyframes, and geometry nodes).
  - `3d-file-converter`: Robust format conversions between GLTF, GLB, OBJ, FBX, STL, and USDZ with material preservation.
  - `gaussian-splatting-3dgs`: Processing, training, and rendering 3D Gaussian Splats for real-time web viewports.
  - `web-3d-scene-composer`: Three.js and WebGPU scene setups with PBR materials, post-processing passes, and camera controls.
  - `meshy-3d-agent` & `3d-model-generation`: AI-driven text-to-3D and image-to-3D pipeline orchestration.
* **Tasks You Can Perform:**
  - Automate 3D product renders and turnarounds via headless Blender Python scripts.
  - Convert heavy CAD/OBJ assets into lightweight, compressed Draco GLTF/GLB files for web deployment.
  - Build interactive 3D web experiences with Three.js, React Three Fiber (R3F), and WebGPU shaders.
  - Integrate 3D Gaussian Splats into standard web viewports with 60 FPS performance budgets.

---

### 02. Audio and Sound Engineering
**Directory:** [`02-audio-and-sound-engineering/`](./02-audio-and-sound-engineering/) | **Skills Count:** 51 Skills

Comprehensive audio processing, speech synthesis, vocal stem isolation, Foley sound design, podcast post-production, and live audio APIs.

* **Key Skills:**
  - `audio-cleanup-stems`: Vocal/instrumental stem separation using Demucs and Spleeter with phase cancellation prevention.
  - `audio-master-engine`: Automated LUFS loudness normalization, multi-band compression, dynamic EQ, and limiter mastering.
  - `audio-transcriber` & `whisperx`: Word-level timestamped transcription, speaker diarization, and multi-language alignment.
  - `ai-voice-studio` & `elevenlabs-voice-*`: Voice cloning, emotional modulation, TTS voiceover generation, and vocal style transfer.
  - `ai-podcast-voiceover` & `ai-audiobook-narration`: Long-form audio synthesis with natural pause structures and chapter marker generation.
* **Tasks You Can Perform:**
  - Automatically master podcasts to broadcast standards (-16 LUFS for stereo, -19 LUFS for mono).
  - Isolate acapella vocals, remove background noise/hum, and extract clean instrumental stems from audio tracks.
  - Generate multi-speaker synthetic podcasts and audiobooks from raw markdown scripts.
  - Integrate live real-time bidirectional audio streaming using Azure VoiceLive and WebRTC.

---

### 03. Autonomous Agents and AI Workflows
**Directory:** [`03-autonomous-agents-and-ai/`](./03-autonomous-agents-and-ai/) | **Skills Count:** 212 Skills

Architectural patterns for autonomous agents, multi-agent swarms, tool-use routing, evaluation benchmarks, and LLM cost optimization.

* **Key Skills:**
  - `agent-creator` & `multi-agent-task-orchestrator`: Design role-based agent squads with communication topologies (hub-and-spoke, sequential, hierarchical).
  - `agent-eval` & `advanced-evaluation`: Rigorous evaluation frameworks measuring task completion, regression drift, and hallucination rates.
  - `agent-memory-systems`: Short-term working context, episodic memory, and persistent semantic retrieval over vector databases.
  - `agent-security-hardening`: Sandboxing agent tool execution, preventing prompt injection, and credential leak containment.
  - `llm-prompt-optimizer` & `prompt-caching-strategy`: Token budgeting, KV-cache optimization, and prompt-cost reduction patterns.
* **Tasks You Can Perform:**
  - Build autonomous agents with self-healing feedback loops and reliable exit criteria.
  - Implement prompt caching strategies that reduce LLM latency by 80% and API costs by 90%.
  - Set up automated eval benchmarks to regression-test agents across model upgrades (e.g. Gemini 1.5 to 2.0).
  - Enforce permission boundaries and human-in-the-loop gates for high-risk agent operations.

---

### 04. Backend Architecture and APIs
**Directory:** [`04-backend-architecture-and-apis/`](./04-backend-architecture-and-apis/) | **Skills Count:** 156 Skills

Enterprise-grade backend design across Go, Rust, Python, Java, Node.js, and .NET. Enforces clean architecture, API contracts, and concurrency safety.

* **Key Skills:**
  - `api-design-principles` & `openapi-spec-generator`: RESTful and RPC API contract design, OpenAPI v3 spec authoring, and schema validation.
  - `fastapi-pro`, `golang-pro`, `rust-pro`: Idiomatic frameworks for high-throughput, low-latency microservices.
  - `auth-implementation-patterns`: OAuth2, OpenID Connect, JWT signing/rotation, session cookies, and RBAC/ABAC authorization.
  - `event-sourcing-architect` & `cqrs-implementation`: Event-driven event-store schemas, projected read models, and message routing.
  - `api-rate-limit-handler`: Distributed token bucket, leaky bucket, and Redis sliding-window rate limiters.
* **Tasks You Can Perform:**
  - Scaffold typed backend services with strict request/response validation (Pydantic, Zod, Protobuf).
  - Implement secure authentication flows including multi-factor auth, token rotation, and fine-grained permissions.
  - Design resilient distributed messaging architectures using Kafka, RabbitMQ, and Redis Pub/Sub.
  - Prevent race conditions and database deadlock issues using optimistic concurrency and transactional outboxes.

---

### 05. Business, Marketing, and SEO
**Directory:** [`05-business-marketing-and-seo/`](./05-business-marketing-and-seo/) | **Skills Count:** 119 Skills

Data-driven growth, programmatic SEO, conversion rate optimization (CRO), search engine indexing, and AI search visibility (GEO).

* **Key Skills:**
  - `seo-aeo-orchestrator` & `geo-citability`: Generative Engine Optimization (GEO) to optimize brand authority and citations in Perplexity, ChatGPT, and Gemini Search.
  - `programmatic-seo`: High-scale landing page generator engines based on structured data and intent-driven dynamic templates.
  - `schema-markup-generator`: JSON-LD structured schema creation (Article, FAQ, Product, SoftwareApplication, Organization).
  - `page-cro` & `copywriting-psychologist`: Conversion funnel audits, psychological hook analysis, and friction reduction.
  - `ai-content-detector` & `ai-content-improver`: Tone normalization, removal of generic AI phrasing, and readability enhancement.
* **Tasks You Can Perform:**
  - Audit websites for technical SEO, crawling issues, canonical loops, and Core Web Vitals bottlenecks.
  - Generate full programmatic SEO clusters with rich schema markup and zero content cannibalization.
  - Optimize content to maximize citations in AI answer engines (Perplexity, SearchGPT).
  - Analyze landing page copy to identify conversion leakages and craft high-converting hero headlines and CTAs.

---

### 06. Code Quality, Security, and Compliance
**Directory:** [`06-code-quality-security-and-compliance/`](./06-code-quality-security-and-compliance/) | **Skills Count:** 164 Skills

Red teaming, defensive engineering, static and dynamic security analysis, vulnerability remediation, and regulatory compliance frameworks.

* **Key Skills:**
  - `hunt-sqli`, `hunt-xss`, `hunt-ssrf`, `hunt-auth-bypass`, `hunt-idor`: Specialized penetration testing playbooks for web vulnerabilities.
  - `cloud-iam-deep` & `saas-security-posture`: Principle-of-least-privilege analysis, IAM permission escalation auditing, and misconfiguration scans.
  - `soc2-compliance`, `iso27001-compliance`, `gdpr-compliance`: Compliance check engines and evidence collection for SOC2, ISO27001, and GDPR.
  - `container-hardening` & `linux-hardening`: CIS benchmark audits, Dockerfile multi-stage minimal builds, and non-root execution rules.
  - `code-audit` & `code-review-excellence`: Deep architectural audits checking for memory leaks, deadlocks, and silent exception suppression.
* **Tasks You Can Perform:**
  - Run comprehensive security vulnerability assessments before merging pull requests.
  - Harden Docker images to reduce attack surfaces (Distroless containers, read-only root filesystems, dropped capabilities).
  - Audit cloud infrastructure access rules for privilege escalation vectors in AWS, GCP, and Azure.
  - Generate compliance gap reports and automated remediation steps for SOC2 and ISO27001 controls.

---

### 07. Codebase Intelligence and Knowledge Graphs
**Directory:** [`07-codebase-intelligence-and-graphs/`](./07-codebase-intelligence-and-graphs/) | **Skills Count:** 10 Skills

Deep structural codebase analysis, Abstract Syntax Tree (AST) inspection, dependency graphs, and architectural layer enforcement.

* **Key Skills:**
  - `understand`: Deep codebase onboarding and architecture mapping tool.
  - `understand-diff`: Structural AST-aware difference analysis that explains architectural implications of code changes.
  - `understand-knowledge`: Extracts domain concepts, entity relationships, and business logic graphs from raw source files.
  - `understand-dashboard`: Visual and tabular codebase health metrics, coupling analysis, and circular dependency detection.
* **Tasks You Can Perform:**
  - Quickly onboard AI agents into unfamiliar multi-million line monorepos with zero hallucinated paths.
  - Detect architectural violations (e.g. presentation layer directly querying database models).
  - Generate comprehensive dependency and call graphs for refactoring initiatives.
  - Calculate structural code metrics: cyclomatic complexity, afferent/efferent coupling, and instability index.

---

### 08. Databases and Data Engineering
**Directory:** [`08-databases-and-data-engineering/`](./08-databases-and-data-engineering/) | **Skills Count:** 208 Skills

Relational, NoSQL, vector, and distributed data systems. Query optimization, schema migrations, ETL pipelines, and disaster recovery.

* **Key Skills:**
  - `postgres-best-practices` & `postgresql-optimization`: Index tuning (B-Tree, GIN, GiST, BRIN), query plan analysis (`EXPLAIN ANALYZE`), and vacuum strategy.
  - `dbt-transformation-patterns` & `bigquery-optimization`: Modern data stack patterns, partition/clustering strategies, and dbt models.
  - `database-migrations-sql-migrations`: Zero-downtime schema migrations, column additions, backfilling, and rollback procedures.
  - `vector-database-engineer` & `vector-database-ops`: Milvus, Qdrant, Pinecone, and pgvector tuning for high-recall cosine/inner-product search.
  - `redis-patterns`: Distributed caching patterns (Cache-Aside, Write-Through), key eviction policies, and pub/sub queues.
* **Tasks You Can Perform:**
  - Identify and fix slow database queries by diagnosing missing indexes and sequential table scans.
  - Write zero-downtime schema migrations for high-traffic production databases.
  - Build and optimize vector indexing pipelines with hybrid BM25 and dense embedding search.
  - Architect automated backup, point-in-time recovery (PITR), and data retention pipelines.

---

### 09. DevOps, Cloud, and Infrastructure
**Directory:** [`09-devops-cloud-and-infrastructure/`](./09-devops-cloud-and-infrastructure/) | **Skills Count:** 85 Skills

Infrastructure as Code (IaC), multi-cloud operations (AWS, GCP, Azure), Kubernetes orchestration, and continuous integration/deployment.

* **Key Skills:**
  - `kubernetes-architect` & `k8s-manifest-generator`: Declarative deployments, StatefulSets, Ingress controllers, NetworkPolicies, and Helm charts.
  - `terraform-specialist` & `terraform-aws`: Reusable, modular Terraform configurations with remote state locking and drift detection.
  - `github-actions-advanced` & `cicd-automation-workflow-automate`: Multi-stage CI/CD pipelines with artifact caching, matrix builds, and security scans.
  - `aws-cost-cleanup` & `aws-cost-optimization`: Automated discovery and termination of orphaned EBS volumes, idle ELBs, and over-provisioned compute.
  - `service-mesh-expert` & `istio-traffic-management`: Envoy/Istio canary deployments, mutual TLS (mTLS), and circuit breaking.
* **Tasks You Can Perform:**
  - Provision complete cloud infrastructures using tested Terraform and OpenTofu blueprints.
  - Containerize complex polyglot applications with minimal Docker images and multi-arch builds.
  - Construct zero-downtime Canary and Blue/Green deployment pipelines on Kubernetes.
  - Reduce monthly cloud bills by identifying idle, unattached, or over-dimensioned infrastructure assets.

---

### 10. Frontend, UI/UX, and Design Systems
**Directory:** [`10-frontend-uiux-and-design-systems/`](./10-frontend-uiux-and-design-systems/) | **Skills Count:** 261 Skills

Modern web interfaces, component architecture (React, Next.js, Vue, Svelte), design tokens, responsive layouts, and WCAG accessibility standards.

* **Key Skills:**
  - `react-best-practices`, `nextjs-app-router-patterns`: Server Components (RSC), suspense boundaries, streaming SSR, and optimistic UI mutations.
  - `tailwind-design-system` & `shadcn`: Token-based design systems, dark/light theme switching, and responsive utility architecture.
  - `better-ui` & `anti-ui-slop`: Elimination of generic AI visual clichés; crafting high-craft, polished, editorial UI typography and layouts.
  - `ui-a11y` & `wcag-audit-patterns`: Automated keyboard navigation testing, ARIA roles, color contrast audits, and screen reader compliance.
  - `state-management` & `zustand-store-ts`: Decoupled, performant client-side state management without unnecessary re-renders.
* **Tasks You Can Perform:**
  - Build responsive, fluid user interfaces following strict design system tokens.
  - Refactor sluggish client components to React Server Components with instant streaming hydration.
  - Guarantee full WCAG 2.1 AA/AAA accessibility compliance across all interactive web elements.
  - Create interactive dashboards, complex data tables with virtualized scrolling, and animated multi-step forms.

---

### 11. General Developer Utilities
**Directory:** [`11-general-developer-utilities/`](./11-general-developer-utilities/) | **Skills Count:** 2,044 Skills

The massive core engine of the vault. Contains exhaustive programming language references, idiomatic patterns, scripts, and developer tools.

* **Key Skills:**
  - **Languages & Frameworks:** Complete specialist playbooks for Python (`python-pro`), Go (`golang-pro`), Rust (`rust-pro`), TypeScript (`typescript-pro`), C++ (`cpp-pro`), Java (`java-pro`), Kotlin (`kotlin-patterns`), C# (`csharp-pro`), PHP (`php-pro`), Ruby (`ruby-pro`), Elixir (`elixir-pro`), and Scala (`scala-pro`).
  - **Frameworks:** `django-patterns`, `fastapi-patterns`, `springboot-patterns`, `laravel-expert`, `nestjs-expert`, `rails-patterns`.
  - **Shell & Systems:** `bash-pro`, `powershell-windows`, `linux-shell-scripting`, `windows-shell-reliability`.
  - **Documentation & Communication:** `writing-skills`, `writing-great-skills`, `wiki-architect`, `write-design-md`, `api-documentation`.
* **Tasks You Can Perform:**
  - Generate idiomatic, high-performance code adhering to official community language standards.
  - Automate tedious developer workflows via robust cross-platform PowerShell and Bash scripts.
  - Produce comprehensive architecture decision records (ADRs), internal developer portals, and user documentation.
  - Parse, transform, and export complex file formats (XLSX, CSV, PDF, XML, Markdown, JSON-LD).

---

### 12. Mobile and Cross-Platform Engineering
**Directory:** [`12-mobile-and-cross-platform/`](./12-mobile-and-cross-platform/) | **Skills Count:** 50 Skills

Native and hybrid mobile app architecture for iOS, Android, Flutter, and React Native.

* **Key Skills:**
  - `flutter-expert` & `dart-flutter-patterns`: Flutter state management (Bloc, Riverpod), responsive layouts, and native platform channels.
  - `android-clean-architecture` & `android-jetpack-compose-expert`: Modern Android development with Compose, Kotlin Coroutines, and Hilt DI.
  - `swiftui-expert-skill` & `swift-concurrency-expert`: Swift 6 concurrency, SwiftUI declarative views, and App Store packaging.
  - `react-native-architecture` & `expo-deployment`: Expo Router, EAS build pipelines, native module bridging, and over-the-air (OTA) updates.
* **Tasks You Can Perform:**
  - Build native-feeling 60 FPS mobile user interfaces across Android and iOS from a single codebase.
  - Handle offline-first data synchronization with SQLite, WatermelonDB, and background push notifications.
  - Configure automated EAS/Fastlane build and submission pipelines to Google Play and Apple App Store.
  - Audit mobile apps for UI jank, memory leaks, battery drain, and excessive startup times.

---

### 13. Science, Genomics, and Bioinformatics
**Directory:** [`13-science-and-bioinformatics/`](./13-science-and-bioinformatics/) | **Skills Count:** 39 Skills

Computational biology, genetics analysis, molecular modeling, and academic literature synthesis.

* **Key Skills:**
  - `alphagenome-single-variant-analysis` & `alphagenome-variant-impact-score`: Functional impact analysis of genetic variants.
  - `biomolecular-structure-viewer`: Interactive 3D molecular inspection (PDB files, protein-ligand binding pockets).
  - `cheminformatics-core` & `rdkit-general`: Chemical structure parsing, SMILES generation, and molecular fingerprint calculation.
  - `literature-search-arxiv`, `literature-search-europepmc`, `pubmed-database`: Automated biomedical and scientific literature synthesis.
* **Tasks You Can Perform:**
  - Query major genetic and protein databases (AlphaFold, UniProt, ChEMBL, ClinVar, Ensembl).
  - Analyze the functional and regulatory consequences of single-nucleotide polymorphisms (SNPs).
  - Visualize complex biomolecular and macromolecular complexes with interactive sidecar viewer links.
  - Perform rigorous, cited literature surveys synthesizing hundreds of academic preprints.

---

### 14. Senior Engineering Best Practices
**Directory:** [`14-senior-engineering-best-practices/`](./14-senior-engineering-best-practices/) | **Skills Count:** 25 Skills

Architectural philosophy, defensive minimalism, complexity reduction, and senior engineering culture.

* **Key Skills:**
  - `code-simplification` & `clean-code`: Aggressive simplification of over-engineered abstractions; eliminating speculative architecture.
  - `context-engineering`: Managing token budgets, preventing context pollution, and structuring multi-turn agent memory.
  - `debugging-and-error-recovery`: Systematic root-cause debugging methodology instead of blind trial-and-error edits.
  - `architecture-decision-records`: Authoring precise, immutable ADRs documenting architectural trade-offs and rationale.
  - `constraint-driven-development`: Designing systems within strict memory, network, and execution-time bounds.
* **Tasks You Can Perform:**
  - Strip away redundant third-party libraries and replace them with standard-library patterns (YAGNI).
  - Prevent context drift in long-running agent conversations by enforcing compact state handoffs.
  - Structure complex cross-team technical initiatives with clear boundaries and interface contracts.
  - Mentor junior developers through clear, actionable, constructive code reviews.

---

### 15. Spec-Driven Project Management (GSD)
**Directory:** [`15-spec-driven-project-management-gsd/`](./15-spec-driven-project-management-gsd/) | **Skills Count:** 72 Skills

The **Get Stuff Done (GSD)** execution methodology. Guarantees that projects move through structured, verifiable phases: Discuss → Spec → Plan → Execute → Verify → Ship.

* **Key Skills:**
  - `gsd-plan-phase` & `gsd-execute-phase`: Turn specifications into discrete, executable task lists with atomic Git commits.
  - `gsd-verify-work` & `gsd-audit-uat`: Formal user acceptance testing (UAT) comparing actual deliverables against the initial specification.
  - `gsd-discuss-phase` & `gsd-spec-phase`: Ambiguity scoring and requirement clarification before a single line of implementation code is written.
  - `gsd-complete-milestone` & `gsd-cleanup`: Archiving completed milestones and prepping clean branches for release.
* **Tasks You Can Perform:**
  - Prevent scope creep by requiring explicit specification approval before coding begins.
  - Execute complex multi-phase software refactorings with guaranteed rollback checkpoints.
  - Automate the creation of PRs, release changelogs, and verification matrices.
  - Run autonomous end-to-end milestone cycles while keeping a persistent progress journal.

---

### 16. Testing, QA, and Debugging
**Directory:** [`16-testing-qa-and-debugging/`](./16-testing-qa-and-debugging/) | **Skills Count:** 133 Skills

Comprehensive test automation across unit, integration, end-to-end (E2E), performance, and exploratory testing.

* **Key Skills:**
  - `playwright-skill` & `playwright-mcp`: Robust browser automation, E2E test authoring, visual regression, and network stubbing.
  - `pytest-skill`, `jest-skill`, `junit-5-skill`: Idiomatic test suite setup, fixtures, parameterized testing, and coverage reports.
  - `k6-load-testing`: High-concurrency performance and stress testing under realistic network profiles.
  - `systematic-debugging`: Reproducible hypothesis-driven debugging strategies with minimal reproducible examples (MREs).
  - `api-contract-testing`: Pact and consumer-driven contract testing preventing breaking changes across microservices.
* **Tasks You Can Perform:**
  - Author flaky-free Playwright E2E test suites with automated failure screenshots and trace recordings.
  - Set up continuous integration test gates with minimum 80%+ branch coverage thresholds.
  - Execute stress and load tests to determine the maximum requests-per-second (RPS) threshold of your APIs.
  - Generate automated mock services and stubs for third-party payment and auth dependencies.

---

### 17. UI Animation and Motion Graphics
**Directory:** [`17-ui-animation-and-motion-graphics/`](./17-ui-animation-and-motion-graphics/) | **Skills Count:** 43 Skills

High-end web motion, physics-based UI transitions, canvas animations, and 60 FPS performance engineering.

* **Key Skills:**
  - `gsap-core`, `gsap-timeline`, `gsap-plugins`: Complex orchestrations, scroll-triggered reveals, and SVG morphing.
  - `animation-performance`: GPU acceleration auditing (`transform`, `opacity`), layout thrashing prevention, and frame-rate budgeting.
  - `dotlottie-web` & `lottie-animation`: Lightweight vector animations integrated into responsive web interfaces.
  - `matter-js-physics` & `tsparticles-engine`: Interactive 2D physics simulations and ambient particle fields.
* **Tasks You Can Perform:**
  - Craft high-end landing page scroll animations without triggering GPU stutter or layout reflows.
  - Design micro-interactions for buttons, toggles, loaders, and notification toasts that feel tactile and responsive.
  - Implement spring-physics-based gestures for mobile and touch-screen devices.
  - Audit and fix stuttering animations by eliminating costly CSS filter recalculations and DOM repaints.

---

### 18. Video, Photo Editing, and VFX Pipelines
**Directory:** [`18-video-and-photo-editing-vfx/`](./18-video-and-photo-editing-vfx/) | **Skills Count:** 958 Skills

Programmatic media creation, code-to-video engines, FFmpeg filter graphs, AI UGC video generation, DaVinci Resolve integration, and visual effects.

* **Key Skills:**
  - `remotion-video-creation`, `remotion-render`: Programmatic video creation in React, dynamic video templates, and automated cloud rendering.
  - `ffmpeg-master-engine` & `ffmpeg-skill`: Complex filter graphs, hardware-accelerated transcoding (NVENC/VAAPI), and multi-stream audio mixing.
  - `ai-ugc-ad-video`, `creative-ad-agent-*`: End-to-end AI UGC video generation, viral hook formulas, and subtitle styling.
  - `davinci-resolve-mcp` & `after-effects-mcp`: Timeline manipulation, EDL/XML export, color grading presets, and motion graphics scripting.
  - `image-studio` & `pillow-photo-engine`: Batch image transformations, background removal, watermarking, and color harmonization.
* **Tasks You Can Perform:**
  - Programmatically render personalized video variations at scale using React code and Remotion.
  - Build automated social media video clips with word-by-word dynamic animated subtitles.
  - Construct complex FFmpeg processing pipelines: split-screens, audio crossfades, chroma-keying, and custom LUT color grading.
  - Script video editing software (DaVinci Resolve, Premiere) directly from agent conversations.

---

## 🚀 Installation and Deployment

You can use the skills globally across your operating system or configure them on a per-project basis.

### 1. Universal Python Installer (Recommended)

A cross-platform Python installer (`install_skills.py`) is provided at the root of the repository:

```bash
# Clone the repository
git clone https://github.com/aniketpal15/Antigravity-skills.git
cd Antigravity-skills

# Install ALL 4,639+ skills globally to ~/.gemini/skills
python install_skills.py

# Or install only a specific domain (e.g. Frontend UI/UX)
python install_skills.py 10-frontend

# Or install Backend + Databases + Security
python install_skills.py 04-backend
python install_skills.py 08-databases
python install_skills.py 06-security
```

---

### 2. Global Antigravity & Gemini Setup

To copy skills directly into your local agent environment:

#### 🪟 Windows (PowerShell)
```powershell
# Create target skills folder
New-Item -ItemType Directory -Force "$HOME\.gemini\skills"

# Copy universal orchestrators
Copy-Item -Recurse "custom-skills\*" "$HOME\.gemini\skills\"

# Copy desired domains (Example: Backend + Testing)
Copy-Item -Recurse "04-backend-architecture-and-apis\*" "$HOME\.gemini\skills\"
Copy-Item -Recurse "16-testing-qa-and-debugging\*" "$HOME\.gemini\skills\"
```

#### 🍏 macOS & 🐧 Linux (Bash)
```bash
# Create target skills folder
mkdir -p ~/.gemini/skills

# Copy universal orchestrators
cp -r custom-skills/* ~/.gemini/skills/

# Copy desired domains (Example: Backend + Testing)
cp -r 04-backend-architecture-and-apis/* ~/.gemini/skills/
cp -r 16-testing-qa-and-debugging/* ~/.gemini/skills/
```

---

### 3. Claude Code & Cursor Setup

To expose skills to Claude Code or Cursor AI:

- **Claude Code:**
  Place the skills inside `~/.claude/skills/` or reference them via your project's `.claude/` directory:
  ```bash
  mkdir -p ~/.claude/skills
  cp -r custom-skills/* ~/.claude/skills/
  cp -r 14-senior-engineering-best-practices/* ~/.claude/skills/
  ```

- **Cursor Rules:**
  You can reference any `SKILL.md` directly inside your `.cursorrules` or `.cursor/rules/` to enforce domain standards across your team.

---

### 4. Project-Local Setup

Keep your repository self-contained by placing skills directly into your project:

```bash
cd your-project/
mkdir -p .skills

# Copy specific capabilities into your project
cp -r /path/to/Antigravity-skills/04-backend-architecture-and-apis/fastapi-pro .skills/
cp -r /path/to/Antigravity-skills/16-testing-qa-and-debugging/playwright-skill .skills/
```

Your agent will automatically detect and load skills located in `./.skills/`.

---

## 🧬 Anatomy of a Skill

Every skill in the vault follows a standardized, modular directory structure:

```
skill-name/
├── SKILL.md            # The primary agent contract (YAML metadata + instructions)
├── README.md           # Human-readable documentation, prerequisites, and examples
├── references/         # Deep technical guides, cheat-sheets, and architectural catalogs
├── scripts/            # Executable Python/Bash/Node scripts used by the skill
└── tests/              # Validation test suites verifying the skill's integrity
```

### The `SKILL.md` Specification
Every `SKILL.md` starts with a parseable YAML header defining when and how the agent should activate the skill:

```yaml
---
name: fastapi-pro
description: Production-grade FastAPI architecture, async patterns, dependency injection, and Pydantic v2 schemas.
triggers:
  - "fastapi"
  - "python backend"
  - "async api"
---

# FastAPI Professional Architecture

## Core Architectural Rules
1. Never perform blocking I/O in async route handlers; always use threadpools or async drivers.
2. Use Pydantic v2 `BaseModel` with strict type annotations and explicit `ConfigDict`.
3. Isolate business logic into domain services; route handlers should only handle HTTP concerns.
...
```

---

## 🤝 Contribution and Guidelines

We welcome community contributions! To ensure high quality across the vault, all new skills must adhere to the following standards:

1. **Deterministic Instructions:** Write actionable, imperative rules rather than open-ended suggestions.
2. **Standard Directory Layout:** Include `SKILL.md` with proper YAML frontmatter and comprehensive `references/`.
3. **No Redundant Dependencies:** Default to language standard libraries and platform-native tools whenever possible.
4. **Tested Scripts:** Any code included in `scripts/` must be cross-platform (Windows/macOS/Linux) and executable.

---

## 📄 License

This collection is distributed under the **MIT License**. Individual skills, reference documents, and scripts retain their respective upstream licenses as indicated in their folder notices.

---

<p align="center">
  <b>Built for the next generation of autonomous engineering.</b><br>
  Star ⭐ this repository to stay up to date with new skill releases!
</p>
