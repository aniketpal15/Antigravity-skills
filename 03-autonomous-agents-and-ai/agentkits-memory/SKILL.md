---
name: agentkits-memory
description: "Local SQLite vector memory with progressive disclosure for AI assistants. Stores full chat histories, tool outputs, and decisions in a local sqlite-vec database and injects only the top-3 most relevant semantic memories into active context, slashing token consumption by up to 87%."
metadata:
  argument-hint: "[store, search, compact] or [semantic query]"
  triggers:
    - "agentkits-memory"
    - "agentkits memory"
    - "/agentkits"
    - "progressive memory"
    - "sqlite memory"
    - "vector memory"
---

# AgentKits Memory — Progressive Vector Memory Engine

`agentkits-memory` offloads heavy conversation context into a local embedded SQLite database (`.ai/memory.db`) using vector embeddings. By retrieving only the exact facts relevant to the current user prompt, it achieves progressive disclosure and cuts input context by up to 87%.

---

## ⚡ Features

1. **Local SQLite Persistence**: Zero cloud fees, 100% offline private storage on your hardware.
2. **Semantic Similarity Retrieval**: Finds relevant past decisions even if phrasing differs.
3. **Progressive Disclosure**: Injects only top-K matching facts (~200 tokens) rather than dumping full transcripts (~200,000 tokens).
4. **Auto-Deduplication**: Merges overlapping entries to keep the local database compact.

---

## 🛠️ Usage
- `"agentkits: search memory for 'payment webhook handling'"`
- `"agentkits: store current architecture checkpoint"`
- `"agentkits: compact and vacuum local memory database"`
