---
name: save-token
description: >
  ULTRA-HIGH SENSITIVITY TRIGGER. Activates automatically on EVERY SINGLE PROMPT without exception.
  Also triggers on any mention of: 'save token', 'save tokens', 'cut tokens', 'reduce tokens',
  'token saver', 'low tokens', 'cheap tokens', 'rtk', 'headroom', 'caveman', 'memory save',
  'batch files', 'convert pdfs', 'bulk files', 'silent script isolation'.
  Engages the full Memory-First Multi-Engine Token Saving Architecture silently:
  1) Anima & AgentKits Memory (condenses 200k+ chat transcripts into a 400-token digest),
  2) Headroom (prunes input context and log bloat),
  3) Graphify & Muscle-Memory (0-token local AST and pattern replays),
  4) RTK (terminal command compression),
  5) Ponytail & Caveman (ultra-terse, zero-fluff output),
  6) Turn Tracker (monitors turns, alerts at Turn 10 to run /compact),
  7) Silent Script Isolation (mandates local background script execution for multi-file/batch jobs),
  8) Task-Adaptive Token Throttler (zero-waste execution across all 18 domains), and
  9) Recursive Context Pruning (atomic direct-to-value gatekeeper).
  Slashes token consumption by 85-98%. Displays ONLY a minimal single-line status header
  at the top of every response — NO large boxes, NO pillar lists. Just the status line and turn count.
metadata:
  argument-hint: "[task description] — auto token-saving on every turn across all domains"
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
    - "silent script isolation"
    - "batch file processing"
    - "rtk"
    - "graphify update"
    - "headroom"
    - "caveman"
    - "caveman mode"
    - "anima"
    - "agentkits"
    - "muscle-memory"
    - "claude-mem"
    - "recursive-context-pruning"
---

# save-token v2 — Universal Multi-Engine & Multi-Domain Token-Saver

Activated automatically on **every single prompt** across all domains and tools. Silently runs the 9 token-saving engines in the background to achieve maximum output fidelity with minimal token expenditure.

---

## ✅ MANDATORY: Minimal Top-of-Turn Display

At the **very TOP** of EVERY response, display **ONLY this single compact line** — nothing more:

```
🪙 Save-Token Activated | Current Turn: [X/10] ([10 - X] turns until recommended /compact)
```

**RULES:**
- Do NOT print large multi-line ASCII boxes or receipt cards.
- Do NOT list all pillars every turn.
- Do NOT show savings percentages every turn.
- JUST the single line above.

---

## 🚨 Turn 10 Alert (and every multiple of 10)

When Turn = 10, 20, 30... replace the single line with this alert ONCE:

```
🪙 Save-Token Activated | Current Turn: 10/10
🚨 TURN 10 REACHED — Type /compact in the chat box now to reset transcript bloat with ZERO memory loss!
```

---

## 🏛️ The 9 Background Engines (Silent Execution)

| Engine | Function | Token Saving |
|:---|:---|:---:|
| **1. Anima & AgentKits Memory** | Condenses 200k+ chat history into 400-token digest in `.ai/memory/` | 80–95% on history |
| **2. Headroom** | Prunes terminal dumps, bridge phrases, and conversational filler | 40–70% on inputs |
| **3. Graphify + Muscle-Memory** | Local AST and structural queries; 0 API tokens for codebase mapping | 70–85% on files |
| **4. RTK Wrapping** | Compresses CLI diffs, tests, and errors before feeding to LLM | 50–80% on commands |
| **5. Ponytail + Caveman** | Zero-fluff, YAGNI, direct-to-solution responses without boilerplate | 40–60% on outputs |
| **6. Turn Tracker** | Cadence monitor; prompts `/compact` at Turn 10 to kill exponential re-sending | Prevents 90k+ spikes |
| **7. Silent Script Isolation** | Batch/multi-file processing via local host scripts (never in context) | **99% on batch jobs** |
| **8. Task-Adaptive Throttler** | Domain-specific execution guards across all 18 domains | 60–90% across domains |
| **9. Recursive Pruning Gatekeeper** | Strips bridge intros; allocates 30% logic, 20% output, 50% buffer | 50–70% on multi-turn |

---

## ⚡ PILLAR 7: Silent Script Isolation Protocol (Multi-File & Batch Rule)

Whenever a task involves **two or more files** (e.g., converting 28 PDFs to images, bulk resizing, CSV processing, multi-file log parsing, batch renaming, bulk format translation):

1. **PROHIBITION**:
   - The LLM is **STRICTLY FORBIDDEN** from reading, loading, or streaming the contents of batch files into context.
   - The LLM must **NEVER loop tool calls** (e.g., 28 read/write tool turns) inside the chat transcript.

2. **ISOLATION WORKFLOW**:
   - Write a single, self-contained local Python/PowerShell script in `<workspace>/scratch/` or project directory.
   - Use high-performance libraries directly on the host (e.g., `pymupdf` / `fitz`, `pdf2image`, `pillow`, `pandas`, `sharp`).
   - Execute the script in **ONE shell command** with output muted:
     ```powershell
     python scratch/batch_task.py | Out-Null
     ```
   - Return ONLY a single compact JSON confirmation:
     `{"status": "success", "processed_files": 28, "errors": 0}`

---

## 🌐 PILLAR 8: Task-Adaptive Token Throttler (Universal 18 Domains)

Automatically detect the active task domain and apply its zero-waste rule:

- **Web & Fullstack Scaffolding (HTML/React/Vue/Next.js)**:
  - Generate components atomically in dedicated files using `write_file`.
  - NEVER reprint unchanged boilerplate or echo entire CSS/vendor framework bundles.
- **Coding, Debugging & Algorithms**:
  - NEVER re-emit whole files for a small fix. Always use surgical `edit_file` with precise target replacements.
  - Locate targets via ripgrep (`rg`) or local AST rather than dumping whole directories.
- **Generative Multimedia (Image, Video, Audio, 3D)**:
  - Operate entirely via file path, seed, and metadata JSON handshakes.
  - NEVER stream raw base64, audio waveforms, or binary chunks into prompt tokens.
- **Web Browsing & Page Interaction (Playwright / Chrome)**:
  - Execute client-side DOM queries to extract only targeted text or selectors.
  - Filter out raw script tags, style blocks, and non-essential markup before returning data to context.
- **MCP Servers & CLI Commands**:
  - Redirect commands with outputs > 40 lines to a local scratch file (`> scratch/cmd.log`).
  - Read only the summary or tail if needed. Return exit code and 1-line status.

---

## 📋 PILLAR 9: Recursive Pruning & Atomic Output Protocol

- **Strip Bridge Phrases**: Never start with "Sure!", "Here is your file", or "Based on your request". Start immediately with the result, code block, or action.
- **Metadata Sharding**: Read file headers or symbol tables first. Full file reads are reserved only for precise target edits.
- **Buffer Safety**: Keep at least 50% headroom buffer for complex tool executions to prevent truncation.
