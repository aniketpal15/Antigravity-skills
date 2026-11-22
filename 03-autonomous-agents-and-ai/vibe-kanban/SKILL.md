---
name: vibe-kanban
description: "AI-native visual task tracking and kanban workflow management for vibe-coding. Organizes rapid agent initiatives into To-Do, In-Progress, Review, and Done columns with real-time markdown board synchronization and atomic progress updates."
metadata:
  argument-hint: "[board action: show, add, move, complete] or [task description]"
  triggers:
    - "vibe-kanban"
    - "vibe kanban"
    - "/kanban"
    - "task board"
    - "vibe board"
    - "track tasks"
---

# Vibe-Kanban — AI-Native Task Board for Vibe-Coding

`vibe-kanban` connects conversational AI development with a lightweight, visual, markdown-backed task board. It enables fast-paced prototyping ("vibe-coding") while maintaining rigorous visibility into what has been built, what is active, and what remains to be done.

---

## ⚡ Features

1. **Markdown-Backed State**: Stores task states directly in `.planning/KANBAN.md` or `TODO.md` inside your repository.
2. **Auto-Advancement**: Automatically moves tasks from `Backlog` → `In Progress` when implementation starts, and to `Done` when tests pass.
3. **WIP Limits**: Prevents agent context overload by limiting active in-flight tasks to 1 or 2 at a time.
4. **Git-Aware**: Attaches commit hashes and file diff links directly to completed task cards.

---

## 🛠️ Usage
- `"vibe-kanban: show current board"`
- `"vibe-kanban: add task 'Implement JWT refresh tokens'"`
- `"vibe-kanban: mark task 3 as done with commit hash"`
