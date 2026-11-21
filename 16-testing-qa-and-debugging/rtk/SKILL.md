---
name: rtk
description: "Rust Token Killer (RTK) CLI proxy that reduces LLM token consumption by 60-90% on terminal, test, build, and git commands. Compresses logs, test failures, diffs, and package manager outputs before feeding them to agent context."
metadata:
  argument-hint: "[gain | test | diff | log | git | npm | cargo | run <cmd>]"
---

# RTK — Rust Token Killer (`rtk`)

A high-performance Rust proxy CLI that strips terminal boilerplate, progress bars, verbose stack traces, and noise before command outputs enter the AI agent context window.

---

## When to Use This Skill

- Whenever running verbose terminal commands: test suites (`npm test`, `pytest`, `cargo test`, `playwright test`), linters (`eslint`, `ruff`, `tsc`), build tools (`next build`, `cargo build`), or `git diff` / `git log`.
- To reduce agent token consumption and speed up response times.
- To check cumulative token savings using `rtk gain`.

---

## Key Commands & Usage

Instead of running raw commands, prefix or proxy them through `rtk`:

| Command | What It Does & How It Saves Tokens |
| :--- | :--- |
| `rtk test <cmd>` | Runs tests and prints **only failure assertions**, hiding hundreds of lines of passing boilerplate (up to 95% token savings). |
| `rtk diff` | Ultra-condensed Git diff showing only modified lines without surrounding identical context padding. |
| `rtk log <cmd>` | Deduplicates repeating log lines, trims timestamps, and extracts key error events. |
| `rtk git <cmd>` | Compact git status, log, and branch outputs. |
| `rtk err <cmd>` | Executes any build or CLI tool and suppresses everything except errors and warnings. |
| `rtk gain` | Displays historical token savings and percentage cost reduction. |

---

## Example Comparisons

* **Raw `npm test`:** 3,500 tokens of ASCII tables, passing checkmarks, and dependency paths.
* **`rtk test npm test`:** ~150 tokens showing strictly failed test names and line assertion errors.
