---
name: save-token
description: >
  ULTRA-HIGH SENSITIVITY TRIGGER. Trigger this skill PROACTIVELY and IMMEDIATELY whenever
  the user writes, mentions, or implies saving tokens, cutting token consumption, reducing AI cost,
  conserving context budget, using RTK, updating Graphify, using Headroom, enabling Caveman mode,
  or activating persistent agent memory (Anima, Claude-Mem, AgentKits, Muscle-Memory).
  Even a casual phrase or keyword (e.g. 'save token', 'save tokens', 'cut tokens', 'reduce tokens',
  'token saver', 'low tokens', 'cheap tokens', 'budget tokens', 'less tokens', 'rtk', 'headroom',
  'caveman', 'memory save') MUST instantly activate this skill.
  Upon activation, it immediately engages the Memory-First Multi-Engine Token Saving Architecture:
  1) Anima & AgentKits Memory (condenses 200k+ chat transcripts into a 400-token file digest),
  2) Headroom (prunes input context and log bloat), 3) Graphify & Muscle-Memory (0-token local AST and pattern replays),
  4) RTK (terminal command compression), and 5) Ponytail & Caveman (ultra-terse, zero-fluff code generation).
  Dramatically slashes token consumption by 70–90% across ALL domains.
  At the very TOP of every response/turn, it MANDATORILY calculates and displays the
  5-Pillar Token Savings Receipt scoreboard before any task output.
metadata:
  argument-hint: "[task description] — activates memory-first token-saver mode with top-of-turn savings receipt"
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
    - "headroom"
    - "caveman"
    - "caveman mode"
    - "anima"
    - "agentkits"
    - "muscle-memory"
    - "claude-mem"
---

# save-token — Memory-First Multi-Engine Token-Saver

`save-token` is an **ultra-sensitive meta-orchestrator skill** that solves the #1 cause of AI quota exhaustion:
**accumulated conversational history (200,000+ tokens)**. By offloading chat context into local structured memory files
and combining it with local zero-token AST code graphs, terminal proxies, and terse generation protocols,
it slashes token consumption by **70% to 90%** across **every single domain**.

## ⚡ Ultra-High Sensitivity Triggering
If the user's prompt contains **ANY** keyword, command, or conversational phrase related to saving or reducing tokens (e.g., `save token`, `save tokens`, `reduce tokens`, `cut tokens`, `token saver`, `low tokens`, `conserve tokens`, `rtk`, `headroom`, `caveman`), the agent **MUST IMMEDIATELY engage this skill without hesitation**.

---

## 🏛️ The Memory-First Token Saving Engine

| Layer | Engines | Token Reduction Mechanism | Typical Savings |
|:---|:---|:---|:---:|
| **1. Memory Offloading** | `anima-memory`, `agentkits-memory`, `claude-mem`, `planning-with-files` | **The History Killer**: Condenses 200k+ chat transcripts into a compact ~400-token file digest (`.ai/memory/state.md`). | **80–95% on History** |
| **2. Context Pruning** | `headroom`, `context-compression` | **Log & Turn Pruner**: Trims bloated test dumps, npm outputs, and redundant turns before sending context to the LLM. | **40–70% on Inputs** |
| **3. Zero-Token Intelligence** | `graphify`, `muscle-memory` | **Offline Tree-Sitter & Pattern Cache**: Queries local code graphs and replays cached boilerplate with 0 API tokens. | **70–85% on Files** |
| **4. Terminal Proxy** | `rtk` (Rust Token Killer) | **CLI Filter**: Intercepts terminal commands, stripping passing tests and unchanged git diff context. | **50–80% on Commands** |
| **5. Dense Generation** | `ponytail`, `caveman` | **Zero-Fluff Code Output**: Delivers pure, dense code and tables without conversational padding. | **40–60% on Outputs** |

---

## 🚀 Activation & Immediate Top-of-Response Output

When triggered, the agent **MUST ALWAYS place the TOKEN SAVINGS RECEIPT at the very TOP of the response**:

```markdown
────────────────────────────────────────────────────────
🪙 TOKEN SAVINGS RECEIPT (This Turn)
• Uncompressed Baseline: ~[Estimated Baseline] tokens
• Actual Consumed:        ~[Actual Consumed] tokens
• Total Tokens Saved:    +[Total Saved] tokens ([Percentage]% Reduction)
  ├─ 🧠 Memory Offloading (Context digest vs 200k+ transcript): +[Memory Saved] tokens
  ├─ 🕸️ Graphify & Muscle (AST lookups & 0-token replays):      +[Graphify Saved] tokens
  ├─ 🗜️ Headroom (Pruned turn bloat & raw log traces):          +[Headroom Saved] tokens
  ├─ 🦀 RTK (Terminal diff/test filter):                         +[RTK Saved] tokens
  └─ 🧵 Ponytail + Caveman (No fluff code generation):           +[Caveman/Ponytail Saved] tokens
────────────────────────────────────────────────────────
```

Followed immediately by active mode status and task execution:

```markdown
🪙 Token-Saver Mode ACTIVE (Memory-First Multi-Engine)
   ✅ 1. Memory Offload (Anima + Claude-Mem) — 200k chat history condensed to 400-token state
   ✅ 2. Graphify & Muscle-Memory — local AST graph & pattern cache active (0 AI tokens)
   ✅ 3. RTK (Rust Token Killer) — terminal wrappers active (rtk diff | rtk test | rtk err)
   ✅ 4. Headroom (Context Pruner) — input logs & turns compressed (40-70% input cut)
   ✅ 5. Ponytail & Caveman — zero conversational fluff, code-first delivery
   📊 Session token tracking: ON
```

---

## 📋 The 5-Step Execution Protocol

### Step 1: Memory Snapshot & Context Offload
Capture active project state, recent user decisions, and immediate next steps into `.ai/memory/session.md` (~400 tokens) to kill context accumulation.

### Step 2: Headroom Input Pruning
Compress bloated terminal dumps, test logs, and remove conversational filler from input context.

### Step 3: Graphify & Muscle-Memory Local Queries
Query local Tree-Sitter AST graphs instead of reading raw files; replay standard boilerplate templates locally.

### Step 4: RTK Command Wrapping
Execute CLI operations using RTK proxies (`rtk diff`, `rtk test`, `rtk err`, `rtk git`).

### Step 5: Ponytail + Caveman Generation
Deliver direct code and technical answers with zero polite filler or essay-style conclusions.
