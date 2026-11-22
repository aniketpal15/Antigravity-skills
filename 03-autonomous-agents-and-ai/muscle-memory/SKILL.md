---
name: muscle-memory
description: "Local zero-token code pattern indexing and replay engine for AI assistants. Caches repetitive boilerplate, standard configurations, formatting passes, and common function templates locally so agents can reproduce them with 0 API tokens."
metadata:
  argument-hint: "[cache pattern, replay pattern, list patterns]"
  triggers:
    - "muscle-memory"
    - "muscle memory"
    - "/muscle"
    - "pattern cache"
    - "zero token replay"
---

# Muscle-Memory — Local Zero-Token Pattern Replay Engine

`muscle-memory` acts as a local shortcut dictionary for AI coding agents. When a project uses repeated boilerplate (e.g. Zod validation handlers, CRUD repository methods, Tailwind layout scaffolds), `muscle-memory` caches the template on disk and replays it without invoking multi-turn LLM reasoning.

---

## ⚡ Key Optimizations

1. **Zero-Token Replays**: Emits cached boilerplate directly using local scripts instead of consuming LLM generation quota.
2. **Project Pattern Indexing**: Scans existing codebase for recurring idioms and stores them in `.ai/patterns/`.
3. **Deterministic Consistency**: Guarantees identical coding conventions across the entire project.

---

## 🛠️ Usage
- `"muscle-memory: cache current API route as standard CRUD pattern"`
- `"muscle-memory: replay standard service template for 'ProductService'"`
- `"muscle-memory: list cached project patterns"`
