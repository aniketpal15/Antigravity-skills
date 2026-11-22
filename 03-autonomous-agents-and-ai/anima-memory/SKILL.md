---
name: anima-memory
description: "Token-budgeted, impact-tagged long-term memory engine for AI coding agents. Injects compact, high-relevance architectural memories and user decisions at session start, eliminating context bloat and avoiding repetitive onboarding across sessions."
metadata:
  argument-hint: "[memory action: record, recall, budget, prune] or [query]"
  triggers:
    - "anima-memory"
    - "anima memory"
    - "/anima"
    - "token budgeted memory"
    - "session memory"
---

# Anima Memory — Token-Budgeted Agent Memory Architecture

`anima-memory` is a high-efficiency memory injection engine designed for Claude Code and Antigravity. Instead of flooding context with uncompressed chat logs, it organizes memory into impact-tagged tiers (Core Rules, Architecture Decisions, Ephemeral Tasks) and enforces strict token budgets on memory injection (~300–500 tokens max).

---

## ⚡ Core Rules & Memory Tiers

1. **Tier 1: Invariant Identity & Rules (Budget: 100 tokens)**: Core constraints (e.g. strict TypeScript, no inline styles).
2. **Tier 2: Architectural State (Budget: 250 tokens)**: Database schema decisions, active API frameworks, auth mechanics.
3. **Tier 3: Active Task Handoff (Budget: 150 tokens)**: Immediate next steps and recent test results.
4. **Progressive Pruning**: Old ephemeral notes are automatically condensed or archived when the token budget is reached.

---

## 🛠️ Usage
- `"anima: record decision 'Use Redis for rate limiting'"`
- `"anima: summarize active project memory into 300 tokens"`
- `"anima: prune completed task logs"`
