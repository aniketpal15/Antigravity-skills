---
name: save-token
description: >
  ULTRA-HIGH SENSITIVITY TRIGGER. Activates automatically on EVERY SINGLE PROMPT without exception.
  Also triggers on any mention of: 'save token', 'save tokens', 'cut tokens', 'reduce tokens',
  'token saver', 'low tokens', 'cheap tokens', 'rtk', 'headroom', 'caveman', 'memory save'.
  Engages the full Memory-First Multi-Engine Token Saving Architecture silently:
  1) Anima & AgentKits Memory (condenses 200k+ chat transcripts into a 400-token digest),
  2) Headroom (prunes input context and log bloat),
  3) Graphify & Muscle-Memory (0-token local AST and pattern replays),
  4) RTK (terminal command compression),
  5) Ponytail & Caveman (ultra-terse, zero-fluff output), and
  6) Turn Tracker (monitors turns, alerts at Turn 10 to run /compact).
  Slashes token consumption by 70-95%. Displays ONLY a minimal single-line status header
  at the top of every response — NO large boxes, NO pillar lists. Just the status line and turn count.
metadata:
  argument-hint: "[task description] — auto token-saving on every turn"
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
    - "anima"
    - "agentkits"
    - "muscle-memory"
    - "claude-mem"
---

# save-token — Memory-First Multi-Engine Token-Saver

Activated automatically on **every single prompt**. Silently runs all 6 token-saving engines
(Memory Offloading, Headroom, Graphify, RTK, Ponytail/Caveman, Turn Tracker) in the background.

---

## ✅ MANDATORY: Minimal Top-of-Turn Display

At the **very TOP** of EVERY response, display **ONLY this single compact line** — nothing more:

```
🪙 Save-Token Activated | Current Turn: [X/10] ([10 - X] turns until recommended /compact)
```

**RULES:**
- Do NOT print large multi-line ASCII boxes.
- Do NOT list all pillars every turn.
- Do NOT show savings percentages every turn.
- JUST the single line above. That's it.

---

## 🚨 Turn 10 Alert (and every multiple of 10)

When Turn = 10, 20, 30... replace the single line with this alert ONCE:

```
🪙 Save-Token Activated | Current Turn: 10/10
🚨 TURN 10 REACHED — Type /compact in the chat box now to reset transcript bloat with ZERO memory loss!
```

---

## 🏛️ Background Engines (Silent — Never Displayed Per Turn)

| Engine | Function | Token Saving |
|:---|:---|:---:|
| Anima/AgentKits Memory | Condenses 200k+ chat into 400-token digest | 80–95% on history |
| Headroom | Prunes input logs and bloat | 40–70% on inputs |
| Graphify + Muscle-Memory | Local AST queries, 0 API tokens | 70–85% on files |
| RTK | Terminal command compression | 50–80% on commands |
| Ponytail + Caveman | Zero-fluff terse output | 40–60% on outputs |
| Turn Tracker | /compact alert at Turn 10 | Prevents 90k+ spikes |

---

## 📋 Execution Protocol (Silent Background)

1. **Memory Snapshot:** State saved to `.ai/memory/session.md` (~400 tokens) — kills history snowball.
2. **Headroom Pruning:** Compress terminal dumps and remove conversational filler.
3. **Graphify Queries:** Use local AST graph instead of reading raw files.
4. **RTK Wrapping:** `rtk diff`, `rtk test`, `rtk err` compress CLI outputs.
5. **Ponytail + Caveman:** Direct, dense, zero-filler responses.
6. **Turn Alert:** At Turn 10, display `/compact` alert banner.
