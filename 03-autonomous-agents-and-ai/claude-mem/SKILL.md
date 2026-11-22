---
name: claude-mem
description: "Persistent cross-session memory architecture for AI coding assistants. Automatically records user decisions, project architecture, working agreements, coding preferences, and ongoing tasks into durable memory files, eliminating repetitive onboarding and context resets across sessions."
metadata:
  argument-hint: "[command: record, recall, status, sync] or [natural language memory request]"
  triggers:
    - "claude-mem"
    - "claude mem"
    - "/claude-mem"
    - "agent memory"
    - "persistent memory"
    - "remember this"
    - "recall memory"
---

# Claude-Mem — Persistent Cross-Session Memory Architecture

`claude-mem` gives AI developer agents durable, cross-session working memory. Instead of starting with a blank slate every time a session restarts or a context window compacts, `claude-mem` automatically files key project decisions, architectural constraints, user preferences, and implementation status into a persistent local memory ledger.

---

## ⚡ Core Capabilities

1. **Automatic Decision Logging**: Captures "why we chose X over Y" so future sessions never question or undo past architectural choices.
2. **Context Persistence Across Resets**: Keeps active work items, test results, and next steps organized in durable markdown state.
3. **User Preference Encoding**: Retains developer habits (e.g. strict TypeScript, preferred test framework, formatting rules).
4. **Zero-Token Local Storage**: Operates entirely through local project files (typically `.ai/memory/` or `.planning/memory/`), incurring zero cloud hosting overhead.

---

## 🛠️ Usage & Commands

| Action | How to Trigger | What Happens |
|:---|:---|:---|
| **Remember Decision** | `remember: we are using PostgreSQL with Drizzle ORM` | Appends architectural decision to `.ai/memory/decisions.md` |
| **Recall Memory** | `recall: what did we decide about authentication?` | Queries local memory files and restores context |
| **Active Task Handoff**| `claude-mem sync` | Saves current session progress, passing tests, and next actions |
| **Inspect Memory** | `claude-mem status` | Displays all recorded memory files and active context |

---

## 📋 Best Practices
- Never store API keys, tokens, or credentials in memory files.
- Keep entries atomic, dated, and linked to relevant code files.
