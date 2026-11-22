---
name: headroom
description: "Intelligent context compressor and token optimization middleware for AI coding agents. Trims bloated system prompts, redundant conversational turns, boilerplate logs, and raw diffs by 40–70% before sending context to LLMs, dramatically lowering API costs and latency."
metadata:
  argument-hint: "[compress context] or [headroom <file/text>]"
  triggers:
    - "headroom"
    - "/headroom"
    - "compress context"
    - "context compression"
    - "trim tokens"
    - "optimize context window"
---

# Headroom — Intelligent AI Context Compression

`headroom` is a high-efficiency context compressor designed to maximize LLM context window utilization and eliminate wasted token spend. It applies semantic pruning, deduplication, and syntax compaction on agent input context.

---

## ⚡ Key Optimizations

1. **Conversational Turn Pruning**: Strips conversational filler ("Sure, I can help with that!") and redundant pleasantries.
2. **Diff & Log Compaction**: Extracts only failing test assertions and changed code hunks while removing unchanged context buffers.
3. **AST Structure Summaries**: Replaces huge raw source files with interface and signature outlines when only contracts are needed.
4. **Token Budget Guarantees**: Ensures prompts stay safely within model token limits without triggering mid-task truncation errors.

---

## 🛠️ Usage & How to Trigger

```bash
# Compress a bloated file or log before ingestion
headroom compress ./logs/test-run.log

# Summarize context with 50% token budget reduction
headroom prune --budget 4000 ./src/components/
```

- In conversation: Simply ask `"headroom: compress this context before analyzing"` or `"use headroom to fit this file in context"`.
