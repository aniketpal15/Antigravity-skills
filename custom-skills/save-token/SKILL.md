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
  4) RTK (terminal command compression), 5) Ponytail & Caveman (ultra-terse, zero-fluff code generation), and
  6) Turn Tracker & Automatic /compact Alert Engine (monitors conversation turns and triggers a prominent
  alert at Turn 10 / multiples of 10 to reset transcript bloat with zero memory loss).
  Dramatically slashes token consumption by 70–95% across ALL domains.
  At the very TOP of every response/turn, it MANDATORILY calculates and displays the
  5-Pillar Token Savings Receipt scoreboard before any task output.
metadata:
  argument-hint: "[task description] — activates memory-first token-saver mode with top-of-turn savings receipt & turn tracker"
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

# save-token — Memory-First Multi-Engine Token-Saver & Turn Tracker

`save-token` is an **ultra-sensitive meta-orchestrator skill** that solves the #1 cause of AI quota exhaustion:
**accumulated conversational history (200,000+ tokens)**. By offloading chat context into local structured memory files,
combining it with local zero-token AST code graphs, terminal proxies, terse generation protocols, and an **automated
turn-tracking `/compact` reminder cadence**, it slashes token consumption by **70% to 95%** across **every single domain**.

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
| **6. Turn Cadence** | `save-token turn-tracker` | **Automated `/compact` Alert**: Prompts user to run `/compact` at Turn 10 to reset transcript size. | **Prevents 90k+ Spikes** |

---

## ⏱️ Turn Tracker & Automated `/compact` Reminder

The agent continuously tracks the conversation turn count within the active compaction cycle:
- **Turns 1 to 9:** Displays current cadence: `Turn [X/10] — [10 - X] turns until recommended /compact`.
- **Turn 10 (and multiples of 10):** Displays the prominent warning banner:

```markdown
================================================================================
🚨 [TURN 10 REACHED — OPTIMAL TIME TO RUN /compact] 🚨
Your conversation transcript has reached 10 turns.
To lock in your token savings and prevent transcript bloat:
👉 Type /compact in the chat box and press Enter.
All memory, project decisions, and files are safely preserved!
================================================================================
```

---

## 🚀 Activation & Immediate Top-of-Response Output

When triggered, the agent **MUST ALWAYS place the TOKEN SAVINGS RECEIPT at the very TOP of the response**:

```markdown
────────────────────────────────────────────────────────
🪙 TOKEN SAVINGS RECEIPT (This Turn)
• Turn Cadence:          Turn [X/10] ([10 - X] turns until recommended /compact)
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
   ✅ 6. Turn Cadence Tracker — Turn [X/10] monitored
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

### Step 5: Ponytail + Caveman Generation & Turn Alert
Deliver direct code and technical answers with zero polite filler. Check turn count: if turn is 10, display the `/compact` reminder banner.
