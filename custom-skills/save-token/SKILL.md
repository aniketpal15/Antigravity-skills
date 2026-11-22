---
name: save-token
description: >
  ULTRA-HIGH SENSITIVITY TRIGGER. Trigger this skill PROACTIVELY and IMMEDIATELY whenever
  the user writes, mentions, or implies saving tokens, cutting token consumption, reducing AI cost,
  conserving context budget, using RTK, updating Graphify, using Headroom, or enabling Caveman mode.
  Even a casual phrase or keyword (e.g. 'save token', 'save tokens', 'cut tokens', 'reduce tokens',
  'token saver', 'low tokens', 'cheap tokens', 'budget tokens', 'less tokens', 'rtk', 'headroom',
  'caveman') MUST instantly activate this skill.
  Upon activation, it immediately engages the full 5-Pillar Token-Saving Engine:
  1) Ponytail (YAGNI minimalism), 2) Graphify (zero-token local AST graph), 3) RTK (terminal command compression),
  4) Headroom (input context and log compression), and 5) Caveman (ultra-terse, zero-fluff output protocol).
  Dramatically slashes both input and output token consumption by 50–85% across ALL domains.
metadata:
  argument-hint: "[task description] — activates 5-pillar token-saver mode for the task"
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
---

# save-token — 5-Pillar Universal Token-Saver Mega-Engine

`save-token` is an **ultra-sensitive meta-orchestrator skill** that coordinates five complementary
token-reduction strategies simultaneously, slashing both **input** and **output** tokens by **50% to 85%**
across **every single domain** (code, writing, design, research, business, science, media, mobile, 3D, gaming, DevOps).

## ⚡ Ultra-High Sensitivity Triggering
If the user's prompt contains **ANY** keyword, command, or conversational phrase related to saving or reducing tokens (e.g., `save token`, `save tokens`, `reduce tokens`, `cut tokens`, `token saver`, `low tokens`, `conserve tokens`, `rtk`, `headroom`, `caveman`), the agent **MUST IMMEDIATELY engage this skill without hesitation**.

---

## 🏛️ The 5-Pillar Token-Saving Architecture

| Pillar | Direction | Tool / Protocol | Token Reduction Mechanism | Typical Savings |
|:---:|:---:|:---|:---|:---:|
| **1. Ponytail** | Output | Built-in GSD Rule | **YAGNI Minimalism**: Writes only requested code. No speculative abstractions, scaffolding, or unused imports. | **30–50%** |
| **2. Graphify** | Input | `graphify update .` | **Zero-Token Local AST Graph**: Queries offline Tree-Sitter code graphs instead of repeatedly reading raw files. | **70–85%** |
| **3. RTK** | Input | `rtk` Rust CLI Proxy | **Terminal Output Compression**: Strips passing tests, progress bars, and surrounding diff padding from CLI commands. | **50–80%** |
| **4. Headroom** | Input | `headroom` Context Pruner | **Intelligent Context Compression**: Prunes conversation turn bloat, strips redundant logs, and summarizes file interfaces. | **40–70%** |
| **5. Caveman** | Output | `caveman` Protocol | **Zero-Fluff Dense Output**: Strips polite pleasantries, filler phrases, and repetitive introductions/conclusions. | **40–60%** |

---

## 🚀 Activation & Immediate Agent Response

When triggered by any phrase, the agent immediately outputs:

```markdown
🪙 Token-Saver Mode ACTIVE (5-Pillar Mega-Engine)
   ✅ 1. Ponytail (YAGNI minimalism) — speculative boilerplate eliminated
   ✅ 2. Graphify (Local AST Engine) — knowledge graph active (0 AI tokens)
   ✅ 3. RTK (Rust Token Killer) — terminal wrappers active (rtk diff | rtk test | rtk err)
   ✅ 4. Headroom (Context Pruner) — input logs & turns compressed (40-70% input cut)
   ✅ 5. Caveman (Terse Output Protocol) — zero conversational fluff (40-60% output cut)
   📊 Session token tracking: ON
```

---

## 📋 The 5-Step Execution Protocol

### Step 1: Headroom Input Pruning
Before ingesting context, large files, or error dumps:
- Compress bloated server logs, test histories, and file collections.
- Remove redundant conversational turns and repeated background context.

### Step 2: Graphify Knowledge Graph Lookup
Run the local AST parser immediately on project files (zero AI tokens):
```bash
graphify update .
```
Then query the graph for architecture context instead of reading whole source files:
```bash
graphify query "auth module signatures and imports"
```

### Step 3: RTK Command Wrapping
Wrap all terminal commands to strip verbose noise before it reaches the LLM context:
```bash
rtk diff            # compact git diffs without unchanged lines
rtk test            # only failing assertions, no passing logs
rtk err             # isolated error root-cause line
rtk git             # compact status and history
```

### Step 4: Ponytail + Caveman Code Generation
When generating solutions:
- **Ponytail**: Implement standard library / platform-native features first. No unnecessary packages.
- **Caveman**: Deliver code and technical answers directly. No "Sure! Here is...", no conversational filler, and no repetitive closing summaries.

### Step 5: Session-End Token Savings Report
At the conclusion of the task or upon request, report cumulative token savings:
```bash
rtk gain
```

---

## 📈 Token Saving Potential by Task

| Task Type | Without save-token | With 5-Pillar save-token | Token Reduction |
|:---|:---:|:---:|:---:|
| **Reviewing large codebases** | ~35,000 tokens | ~8,000 tokens | **~77% Savings** |
| **Debugging test suites** | ~20,000 tokens | ~4,500 tokens | **~78% Savings** |
| **Multi-file refactoring** | ~28,000 tokens | ~9,000 tokens | **~68% Savings** |
| **Git diff & commit reviews** | ~15,000 tokens | ~2,500 tokens | **~83% Savings** |
| **Writing code & scripts** | ~8,000 tokens | ~3,200 tokens | **~60% Savings** |

---

## ⚖️ Pros & Cons

### Pros
- ✅ **Cuts both input AND output tokens**: Graphify, RTK, and Headroom compress input; Ponytail and Caveman compress output.
- ✅ **Faster responses**: Fewer tokens generated means much faster generation time.
- ✅ **100% Offline preprocessing**: Graphify, RTK, and Headroom run locally without making external API calls.
- ✅ **Extends rate limits**: Dramatically lowers token consumption against Gemini, Claude, or OpenAI rate limits.

### Cons & Trade-offs
- ⚠️ **Terse style**: Caveman output is direct, compact, and dense; it drops polite conversational prose.
- ⚠️ **Requires local CLI tools**: For full RTK and Graphify acceleration, the local binaries (`rtk`, `graphify`) are used; if absent, Ponytail, Headroom, and Caveman still provide massive savings.
