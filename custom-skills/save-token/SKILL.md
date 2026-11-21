---
name: save-token
description: >
  Token-Saver Orchestrator — When activated with "save token", "/save token",
  or "use save-token", this skill immediately engages the full Ponytail + Graphify + RTK
  stack to minimize AI token consumption across ALL domains and all task types.
  It runs graphify update (zero-token local AST parse), activates RTK command wrappers
  for every terminal operation, enforces YAGNI minimalism on all code generation,
  and reports token savings at session end. Works globally for any domain:
  code, writing, design, science, business, media — anything.
metadata:
  argument-hint: "[task description] — activates token-saver mode for the described task"
  triggers:
    - "save token"
    - "/save token"
    - "/save-token"
    - "use save-token"
    - "activate save token"
    - "token saver"
    - "enable token saving"
---

# save-token — Universal Token-Saver Orchestrator

## What This Skill Does

`save-token` is a **meta-orchestrator skill** that activates three complementary
token-reduction strategies simultaneously, dramatically cutting the number of AI
tokens consumed per task — across **every domain** (code, writing, design,
research, business, science, media, mobile, 3D, gaming, etc.).

### The Three Pillars

| Pillar | Tool | Token Reduction Mechanism |
|--------|------|--------------------------|
| **Ponytail** | Built-in GSD rule | YAGNI minimalism — write only what is asked; no boilerplate; stdlib-first |
| **Graphify** | `graphify update .` | Local AST knowledge-graph (0 AI tokens); queries the graph instead of re-reading raw files |
| **RTK** | `rtk` CLI binary | Rust-powered terminal compression wrappers — `rtk diff`, `rtk test`, `rtk err`, `rtk git` |

---

## Activation

Type **any** of the following in a prompt or conversation:

```
save token
/save token
/save-token
use save-token
activate save token
token saver
enable token saving
```

The agent will immediately print:

```
🪙 Token-Saver Mode ACTIVE
   ✅ Ponytail (YAGNI minimalism) — engaged
   ✅ Graphify — running update... knowledge graph refreshed
   ✅ RTK — command wrappers active (rtk diff | rtk test | rtk err | rtk git)
   📊 Session token tracking: ON
```

---

## Execution Protocol (What the Agent Does)

### Step 1 — Ponytail Minimalism Gate
Before generating any code, prose, plan, or analysis:
- Apply YAGNI: implement **only** what the user explicitly asked for.
- Use **stdlib / platform-native** features; no extra libraries unless unavoidable.
- Skip all scaffolding, comments, stubs, and examples unless explicitly requested.
- Mark deliberate simplifications with `# ponytail:` inline notes.

### Step 2 — Graphify Knowledge Graph Update
Run the local AST parser immediately on project files (zero AI tokens):
```bash
graphify update .
```
Then query the graph for any context instead of reading raw source files:
```bash
graphify query "function signatures in auth module"
graphify query "what files import database.ts"
```
This replaces expensive file-read + AI-summarization loops with instant
local graph lookups.

### Step 3 — RTK Command Wrapping
Prefix ALL terminal operations with RTK wrappers:
```bash
rtk diff            # compressed git diff (saves reading large diffs)
rtk test            # compressed test output (only failures, not full logs)
rtk err             # compressed error traces (key lines only)
rtk git             # compressed git status/log
rtk gain            # show cumulative tokens saved this session
```

### Step 4 — Session-End Report
At the end of every task or on user request, run:
```bash
rtk gain
```
This prints the estimated token savings for the session.

---

## Domain Coverage

This skill works for **ALL** domains — not just code:

| Domain | How save-token Helps |
|--------|---------------------|
| **Code / Backend** | Graphify graph replaces reading entire codebases; RTK compresses diffs/tests |
| **Frontend / UI** | Ponytail prevents over-engineering components; minimal CSS-first approach |
| **Writing / Docs** | Outputs only the requested section; no filler intros/outros |
| **Design Systems** | Reuses existing tokens/variables from graph; no redundant definitions |
| **Science / Research** | Minimal literature summaries; no padding; graph-indexed datasets |
| **Business / Finance** | Concise reports; no boilerplate executive summaries unless asked |
| **Mobile / iOS / Android** | Native platform APIs first; no extra packages |
| **3D / Game Dev** | Reuses existing asset graphs; minimal shader/script output |
| **DevOps / CI** | RTK git/diff wrappers; minimal YAML; no unused pipeline steps |
| **Testing / QA** | RTK test output; only failing assertions; no verbose logs |
| **Video / Media** | Minimal ffmpeg chains; no intermediate files unless needed |
| **Data Science / ML** | Minimal preprocessing chains; no boilerplate notebooks |

---

## Real Usage Examples

### Example 1 — Code Task
```
User: save token. Now refactor the auth module.

Agent: 🪙 Token-Saver Mode ACTIVE
       Running: graphify update .
       Querying graph for auth module structure...
       [Ponytail: implementing only what's asked — no boilerplate]
       [RTK: rtk diff will show changes]
```

### Example 2 — Writing Task
```
User: save token. Write a product description for my SaaS tool.

Agent: 🪙 Token-Saver Mode ACTIVE
       [Ponytail: 3-sentence output — no filler sections]
       <concise product description>
       [rtk gain: ~400 tokens saved vs. verbose mode]
```

### Example 3 — DevOps Task
```
User: save token. Debug why my CI pipeline is failing.

Agent: 🪙 Token-Saver Mode ACTIVE
       Running: rtk err (compressed error trace)
       Root cause: [single line diagnosis]
       Fix: [minimal change only]
```

---

## How to Use

1. **Start any task with:** `save token` or `/save token`
2. **Describe your task** in the same prompt or the next message.
3. The agent handles everything automatically — Ponytail, Graphify, RTK.
4. At any point type `rtk gain` to see how many tokens you've saved.
5. To disable: `disable save token` or just start a new session.

---

## Pros

- ✅ **Universal** — works on every domain, not just code
- ✅ **Zero extra API calls** — Graphify runs fully locally (Rust binary)
- ✅ **Automatic** — no manual configuration per task
- ✅ **Composable** — stacks with any other skill (GSD, RTK, Ponytail are still active)
- ✅ **Measurable** — `rtk gain` gives real savings data
- ✅ **Minimal prompt overhead** — activation phrase is just 2 words
- ✅ **Cross-platform** — works on Windows, macOS, Linux

## Cons / Limitations

- ⚠️ **Graphify update requires project files** — works best in a code/file-rich workspace; for pure conversation tasks, Graphify step is skipped automatically
- ⚠️ **RTK binary must be installed** — `winget install rtk` or `cargo install rtk`; skill degrades gracefully if not found (Ponytail + Graphify still active)
- ⚠️ **Ponytail may feel "terse"** — intentionally minimal output; ask for elaboration explicitly if needed
- ⚠️ **Token savings are estimates** — `rtk gain` reports compression ratios, not exact model token counts

---

## Token Saving Potential

| Scenario | Estimated Saving |
|----------|-----------------|
| Reviewing large codebases | 40–70% fewer tokens |
| Multi-file refactoring | 30–60% fewer tokens |
| Test output debugging | 50–80% fewer tokens |
| Documentation writing | 20–40% fewer tokens |
| Git diff analysis | 60–85% fewer tokens |

---

## References
- Ponytail: `C:\Users\anike\.gemini\config\plugins\agentic-awesome-skills\skills\ponytail\SKILL.md`
- Graphify: `C:\Users\anike\.gemini\config\plugins\agentic-awesome-skills\skills\graphify\SKILL.md`
- RTK: `C:\Users\anike\.gemini\config\plugins\agentic-awesome-skills\skills\rtk\SKILL.md`
