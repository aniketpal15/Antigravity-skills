---
name: playwright-mcp
description: |
  Microsoft Playwright Model Context Protocol (MCP) server for fast, deterministic
  browser automation via accessibility snapshots, DOM interaction, testing, and
  web scraping. Use when automating web tasks, driving headless browsers,
  taking snapshots, testing web apps, or interacting with live sites.
---

# Playwright‑MCP Skill Documentation

> **TL;DR** – Install the MCP server with a single `npx` command, launch it with
> the flags you need, then drive the browser through a tiny JSON‑over‑HTTP
> protocol that works on **accessibility trees** (no vision model required).  
> The result is deterministic, low‑latency automation that can be used from
> any language or LLM‑agent.

---

## 1. Overview & Architecture

### 1.1 What is MCP?

The **Model Context Protocol (MCP)** is a thin, JSON‑RPC‑style API that sits on
top of **Microsoft Playwright**.  
Instead of sending raw screenshots to a vision model, MCP extracts the **Accessibility
Tree (AT)** from the page and streams it to the client. The AT is a compact,
semantic representation of the UI (roles, names, states, hierarchy) that:

| Benefit | Why it matters |
|---------|----------------|
| **Deterministic** | No pixel‑level noise; the same DOM → same AT. |
| **Fast** | AT payloads are ~10‑100× smaller than images. |
| **Language‑model friendly** | LLMs can reason over a structured tree without OCR. |
| **Privacy‑preserving** | No visual data leaves the host machine. |

MCP adds a **snapshot** layer on top of Playwright’s native APIs:

```
Browser  <-- Playwright -->  MCP Server  <-- JSON RPC -->  Client (LLM, script, etc.)
```

### 1.2 Core Components

| Component | Role |
|-----------|------|
| **Playwright Engine** | Drives Chromium, Firefox, or WebKit (headful/headless). |
| **MCP Server** (`@playwright/mcp`) | Exposes HTTP endpoints (`/command`, `/snapshot`, `/health`). |
| **Accessibility Snapshot Service** | Calls `page.accessibility.snapshot()` on demand, caches per‑frame. |
| **Command Dispatcher** | Maps JSON commands (`navigate`, `click`, `evaluate`, …) to Playwright calls. |
| **Session Manager** | Handles multiple concurrent “contexts” (isolated tabs, incognito). |
| **Ponytail Minimalist Layer** | Enforces a tiny, opinionated API surface (≤ 15 commands) for LLM agents, reducing prompt length and token usage. |

### 1.3 Data Flow Example

1. **Client → MCP**: `POST /command { "action":"navigate", "url":"https://example.com" }`
2. **MCP**: Calls `page.goto(url)`.
3. **MCP**: Immediately after navigation, runs `page.accessibility.snapshot()` and returns:
   ```json
   {
     "snapshotId": "c1a2b3",
     "tree": { "role":"document", "children":[...] }
   }
   ```
4. **Client**: Parses the AT, decides next action (e.g., click a button with name “Login”).
5. **Repeat** – deterministic loop continues until the task finishes.

---

## 2. MCP Server Configuration & Launch Options

### 2.1 Installation (one‑liner)

```bash
npx @playwright/mcp@latest
```

> The package bundles Playwright, so you don’t need a separate `npm i -D playwright`.

### 2.2 CLI Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--port <num>` | HTTP port (default = 3000). | `--port 8080` |
| `--headless` | Run browsers headless (default). | `--headless` |
| `--headful` | Run browsers with UI (useful for debugging). | `--headful` |
| `--browser <name>` | Choose engine: `chromium`, `firefox`, `webkit`. | `--browser chromium` |
| `--output-dir <path>` | Directory where screenshots, HAR, and logs are saved. | `--output-dir ./mcp-data` |
| `--timeout <ms>` | Global command timeout (default = 30000). | `--timeout 60000` |
| `--max-sessions <n>` | Max concurrent browser contexts (default = 5). | `--max-sessions 10` |
| `--log-level <level>` | `debug|info|warn|error`. | `--log-level debug` |
| `--disable-sandbox` | Useful in CI containers without user namespaces. | `--disable-sandbox` |

#### Example launch

```bash
npx @playwright/mcp@latest \
  --port 4000 \
  --browser firefox \
  --headful \
  --output-dir ./mcp-output \
  --max-sessions 3 \
  --log-level info
```

### 2.3 Environment Variables (alternative to flags)

| Variable | Effect |
|----------|--------|
| `MCP_PORT` | Same as `--port`. |
| `MCP_BROWSER` | Same as `--browser`. |
| `MCP_HEADLESS` | Set to `0` to force headful. |
| `MCP_OUTPUT_DIR` | Same as `--output-dir`. |
| `MCP_TIMEOUT_MS` | Same as `--timeout`. |

### 2.4 Health & Metrics

- **GET** `/health` → `{ "status":"ok", "uptime":12345 }`
- **GET** `/metrics` → Prometheus‑compatible counters (`mcp_requests_total`, `mcp_errors_total`).

---

## 3. Core Capabilities & MCP Tools

> The **Ponytail Minimalist** philosophy limits the public surface to **15** high‑value commands.
> Internally the server supports many more Playwright APIs, but only the listed ones are
> guaranteed stable for LLM consumption.

| Command | Payload (JSON) | Returns | Description |
|---------|----------------|---------|-------------|
| `navigate` | `{ "url":"https://...", "waitUntil":"load|domcontentloaded|networkidle" }` | `{ "snapshotId":"…" }` | Loads a page and returns an AT snapshot. |
| `click` | `{ "selector":"button#login", "button":"left|right", "clickCount":1 }` | `{ "snapshotId":"…" }` | Clicks an element (fallback to AT‑based matching if selector missing). |
| `type` | `{ "selector":"input[name='q']", "text":"Playwright", "delay":50 }` | `{ "snapshotId":"…" }` | Types into a field, character‑by‑character. |
| `fill` | `{ "selector":"input[name='email']", "value":"user@example.com" }` | `{ "snapshotId":"…" }` | Clears + fills in one step. |
| `hover` | `{ "selector":"nav > a[href='/docs']" }` | `{ "snapshotId":"…" }` | Moves mouse over element. |
| `select` | `{ "selector":"select#country", "options":["US","CA"] }` | `{ "snapshotId":"…" }` | Selects one or more `<option>` values. |
| `evaluate` | `{ "script":"() => document.title", "args":[] }` | `{ "result": "…" }` | Executes arbitrary JS in page context (sandboxed). |
| `screenshot` | `{ "path":"login.png", "fullPage":true }` | `{ "file":"login.png" }` | Saves a PNG/JPEG to `output-dir`. |
| `snapshot` | `{ "snapshotId":"c1a2b3" }` | `{ "tree":{…} }` | Retrieves a previously cached AT snapshot (useful for diffing). |
| `tabs` | `{ "action":"list|new|close", "target":"tabId" }` | Varies | Manage multiple pages within a single browser context. |
| `close` | `{ "force":false }` | `{ "closed":true }` | Gracefully shuts down the server (admin only). |
| `waitFor` | `{ "selector":"text=Welcome", "state":"visible|hidden|attached", "timeout":5000 }` | `{ "snapshotId":"…" }` | Waits for a condition before returning. |
| `press` | `{ "selector":"input", "key":"Enter" }` | `{ "snapshotId":"…" }` | Sends a keyboard shortcut. |
| `dragAndDrop` | `{ "source":"#item", "target":"#bin" }` | `{ "snapshotId":"…" }` | Simulates HTML5 drag‑and‑drop. |
| `setViewport` | `{ "width":1280, "height":720 }` | `{ "viewport":{…} }` | Adjusts page size (affects layout & AT). |
| `clearCookies` | `{}` | `{ "cleared":true }` | Clears all cookies for the current context. |

### 3.1 Command Envelope

All commands are POSTed to **`/command`** with the following envelope:

```json
{
  "sessionId": "optional‑uuid‑if‑multiple‑sessions",
  "command": "navigate",
  "payload": { /* see table above */ }
}
```

If `sessionId` is omitted, MCP creates a **default session** on first request.

### 3.2 Response Envelope

```json
{
  "requestId": "uuid‑mirroring‑client‑id",
  "status": "ok|error",
  "data": { /* command‑specific */ },
  "error": null | { "code":123, "message":"…" }
}
```

---

## 4. Workflows

Below are ready‑to‑copy JSON‑script snippets for the four most common use‑cases.
Each workflow assumes a **single session** (`sessionId` omitted).

### 4.1 Web Testing & Assertion

```json
[
  { "command":"navigate", "payload":{ "url":"https://demo.playwright.dev/todomvc" } },
  { "command":"fill",     "payload":{ "selector":"input.new-todo", "value":"Buy milk" } },
  { "command":"press",    "payload":{ "selector":"input.new-todo", "key":"Enter" } },
  { "command":"snapshot", "payload":{} },
  { "command":"evaluate", "payload":{ "script":"() => document.querySelectorAll('.todo-list li').length", "args":[] } },
  { "command":"assert",   "payload":{ "expected":1, "actualPath":"$.result" } }   // custom LLM‑side assertion
]
```

*Typical LLM loop*: after each `snapshot` the model inspects the AT tree, verifies that a `<li>` with name “Buy milk” exists, then proceeds.

### 4.2 Autonomous UI Interaction (LLM‑driven Agent)

```json
[
  { "command":"navigate", "payload":{ "url":"https://mail.google.com" } },
  { "command":"waitFor",  "payload":{ "selector":"text=Compose", "state":"visible" } },
  { "command":"click",    "payload":{ "selector":"text=Compose" } },
  { "command":"type",     "payload":{ "selector":"textarea[name='to']", "text":"friend@example.com" } },
  { "command":"type",     "payload":{ "selector":"input[name='subject']", "text":"Hello from MCP" } },
  { "command":"type",     "payload":{ "selector":"div[aria-label='Message Body']", "text":"This is an automated email." } },
  { "command":"click",    "payload":{ "selector":"text=Send" } },
  { "command":"snapshot", "payload":{} }
]
```

The LLM can **reason over the returned AT** to confirm the email was sent (look for a toast notification node).

### 4.3 Web Scraping

```json
[
  { "command":"navigate", "payload":{ "url":"https://news.ycombinator.com" } },
  { "command":"snapshot", "payload":{} },
  { "command":"evaluate", "payload":{ "script":"() => Array.from(document.querySelectorAll('.storylink')).map(e=>({title:e.innerText, url:e.href}))", "args":[] } }
]
```

Result `data.result` is a clean JSON array ready for downstream processing—no HTML parsing required.

### 4.4 Visual Regression (Hybrid)

1. **Capture baseline** (run once, store AT + screenshot).

```json
[
  { "command":"navigate", "payload":{ "url":"https://example.com" } },
  { "command":"snapshot", "payload":{} },
  { "command":"screenshot", "payload":{ "path":"baseline.png", "fullPage":true } }
]
```

2. **Compare in CI** – fetch current AT, diff with baseline AT (tree diff libraries) and optionally compare screenshots with a pixel‑diff tool.

```json
[
  { "command":"navigate", "payload":{ "url":"https://example.com" } },
  { "command":"snapshot", "payload":{} },
  { "command":"screenshot", "payload":{ "path":"current.png", "fullPage":true } }
]
```

*Ponytail tip*: keep the AT diff logic inside the LLM prompt; the image diff can be delegated to a CI step.

---

## 5. Best Practices & Ponytail Minimalist Guidelines

###