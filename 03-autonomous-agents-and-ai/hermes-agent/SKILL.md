---
name: hermes-agent
description: >-
  Autonomous problem-solving agent framework by Nous Research. Features
  multi-turn tool execution, self-reflective memory offloading, skill synthesis,
  cross-platform terminal orchestration, and autonomous problem-solving loops.
metadata:
  argument-hint: "[goal_or_task] — execute via Hermes autonomous agent"
  triggers:
    - "hermes-agent"
    - "hermes agent"
    - "run hermes"
    - "hermes reasoning"
    - "nous agent"
---

# Hermes Agent (Nous Research)

Hermes Agent ("The agent that grows with you") is an advanced autonomous agent system developed by Nous Research, engineered for deep problem solving, multi-turn tool calling, and persistent learning across sessions.

## Core Pillars

1. **Self-Reflective Episodic Memory**: Offloads and condenses session histories into dense knowledge fragments, eliminating context bloat while preserving key learnings.
2. **Autonomous Tool & Skill Synthesis**: Dynamically writes, tests, and saves its own reusable tool modules and skills during execution.
3. **Multi-Model Backend Support**: Works seamlessly with open-weight models (Hermes 3, Llama 3, Qwen 2.5, DeepSeek) through local runtimes (vLLM, Ollama, LM Studio) and cloud inference endpoints (OpenRouter, Together, Fireworks, Nous).
4. **Resilient Terminal & Environment Automation**: Executes safe shell tasks with watchdog timeouts, automatic error classification, and state rollback.

## CLI Usage

```bash
# Run Hermes interactive agent shell
hermes

# Execute an autonomous one-shot goal
hermes run "Analyze this repository and generate comprehensive API documentation"

# Run interactive configuration / model provider setup
hermes setup

# Check installed tools, skills, and plugins
hermes plugins list

# Manage session memories and insights
hermes insights --days 7
```

Use Hermes Agent when you need autonomous exploration, complex multi-step reasoning, or an independent agent worker loop capable of self-correction.
