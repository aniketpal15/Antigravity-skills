---
name: save-token
description: >
  ULTRA-HIGH SENSITIVITY TRIGGER. Trigger this skill PROACTIVELY and IMMEDIATELY whenever
  the user writes, mentions, or implies saving tokens, cutting token consumption, reducing AI cost,
  conserving context budget, using RTK, or updating Graphify. Even a casual phrase or keyword
  (e.g. 'save token', 'save tokens', 'cut tokens', 'reduce tokens', 'token saver', 'low tokens',
  'cheap tokens', 'budget tokens', 'less tokens', 'rtk') MUST instantly activate this skill.
  Upon activation, it immediately engages the full Ponytail + Graphify + RTK stack to minimize
  AI token consumption across ALL domains and all task types. It runs graphify update (zero-token
  local AST parse), activates RTK command wrappers for every terminal operation, enforces YAGNI
  minimalism on all code generation, and reports token savings at session end.
metadata:
  argument-hint: "[task description] — activates token-saver mode for the described task"
  triggers:
    - "save token"
    - "save tokens"
    - "save-token"
    - "save-tokens"
    - "/save token"
    - "/save-token"
    - "/save tokens"
    - "token saver"
    - "token saving"
    - "token savings"
    - "save my tokens"
    - "save our tokens"
    - "reduce tokens"
    - "reduce token"
    - "cut tokens"
    - "cut token"
    - "less tokens"
    - "low tokens"
    - "low token"
    - "cheap tokens"
    - "conserve tokens"
    - "token budget"
    - "token efficiency"
    - "enable token saving"
    - "activate save token"
    - "use save-token"
    - "stop wasting tokens"
    - "minimize tokens"
    - "rtk"
    - "graphify update"
---

# save-token — Universal Token-Saver Orchestrator

## What This Skill Does

`save-token` is an **ultra-sensitive meta-orchestrator skill** that activates three complementary
token-reduction strategies simultaneously, dramatically cutting the number of AI
tokens consumed per task — across **every domain** (code, writing, design,
research, business, science, media, mobile, 3D, gaming, etc.).

## ⚡ Ultra-High Sensitivity Triggering
If the user's prompt contains **ANY** keyword, command, or conversational phrase related to saving or reducing tokens (e.g., `save token`, `save tokens`, `reduce tokens`, `cut tokens`, `token saver`, `low tokens`, `conserve tokens`, `rtk`), the agent **MUST IMMEDIATELY engage this skill without hesitation**.

### The Three Pillars

| Pillar | Tool | Token Reduction Mechanism |
|--------|------|--------------------------|
| **Ponytail** | Built-in GSD rule | YAGNI minimalism — write only what is asked; no boilerplate; stdlib-first |
| **Graphify** | `graphify update .` | Local AST knowledge-graph (0 AI tokens); queries the graph instead of re-reading raw files |
| **RTK** | `rtk` CLI binary | Rust-powered terminal compression wrappers — `rtk diff`, `rtk test`, `rtk err`, `rtk git` |

---

## Activation

Type **any** trigger in a prompt or conversation:

```
save token
/save token
save tokens
cut tokens
reduce tokens
token saver
low tokens
rtk
```

The agent will immediately print:

```
🪙 Token-Saver Mode ACTIVE
   ✅ Ponytail (YAGNI minimalism) — engaged
   ✅ Graphify — running update... knowledge graph refreshed
   ✅ RTK — command wrappers active (rtk diff | rtk test | rtk err | rtk git)
   📊 Session token tracking: ON
```

---

## Execution Protocol (What the Agent Does)

### Step 1 — Ponytail Minimalism Gate
Before generating any code, prose, plan, or analysis:
- Apply YAGNI: implement **only** what the user explicitly asked for.
- Use **stdlib / platform-native** features; no extra libraries unless unavoidable.
- Skip all scaffolding, comments, stubs, and examples unless explicitly requested.
- Mark deliberate simplifications with `# ponytail:` inline notes.

### Step 2 — Graphify Knowledge Graph Update
Run the local AST parser immediately on project files (zero AI tokens):
```bash
graphify update .
```
Then query the graph for any context instead of reading raw source files:
```bash
graphify query "function signatures in auth module"
graphify query "what files import database.ts"
```
This replaces expensive file-read + AI-summarization loops with instant
local graph lookups.

### Step 3 — RTK Command Wrapping
Prefix ALL terminal operations with RTK wrappers:
```bash
rtk diff            # compressed git diff (saves reading large diffs)
rtk test            # compressed test output (only failures, not full logs)
rtk err             # compressed error traces (key lines only)
rtk git             # compressed git status/log
rtk gain            # show cumulative tokens saved this session
```

### Step 4 — Session-End Report
At the end of every task or on user request, run:
```bash
rtk gain
```
This prints the estimated token savings for the session.

---

## Domain Coverage

This skill works for **ALL** domains — not just code:
- Code / Backend
- Frontend / UI
- Writing / Docs
- Design Systems
- Science / Research
- Business / Finance
- Mobile / iOS / Android
- 3D / Game Dev
- DevOps / CI
- Testing / QA
- Video / Media
- Data Science / ML
