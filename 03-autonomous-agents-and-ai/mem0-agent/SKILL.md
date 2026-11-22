---
name: mem0-agent
description: "Universal open-source agent memory layer. Automatically extracts user preferences, coding habits, architectural constraints, and evolving facts from natural conversation, storing them in a structured local semantic store for instant recall across chats."
metadata:
  argument-hint: "[extract, recall, update] or [memory query]"
  triggers:
    - "mem0-agent"
    - "mem0"
    - "/mem0"
    - "universal memory"
    - "learn preferences"
---

# Mem0 Agent — Universal Intelligent Memory Layer

`mem0-agent` codifies the Mem0 universal memory architecture. It dynamically analyzes conversation turns, identifies persistent facts (e.g. "user prefers pnpm over npm", "staging database is on port 5433"), and maintains an evolving memory ledger that makes every session smarter without increasing context size.

---

## ⚡ Core Principles

1. **Automatic Fact Extraction**: Extracts durable knowledge without explicit user prompting.
2. **Conflict Resolution**: When a user changes their mind ("actually use Vitest instead of Jest"), Mem0 updates the existing fact rather than storing conflicting rules.
3. **Ultra-Low Footprint**: Injects a clean bullet-point summary of relevant preferences into the prompt header (~150 tokens).

---

## 🛠️ Usage
- `"mem0: extract and store project preferences from this discussion"`
- `"mem0: show everything you know about my coding habits"`
- `"mem0: update preference: switch from npm to bun"`
