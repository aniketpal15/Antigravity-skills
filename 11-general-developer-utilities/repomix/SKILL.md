---
name: repomix
description: "Pack entire codebases and directories into a single AI-friendly formatted file with precise token counts, security secret scrubbing, and customizable file filtering. Perfect for feeding multi-file context into LLMs and code review assistants."
metadata:
  argument-hint: "[repomix path] or [pack repo <options>]"
  triggers:
    - "repomix"
    - "/repomix"
    - "pack repo"
    - "repo to prompt"
    - "codebase packer"
    - "bundle code for ai"
---

# Repomix — Codebase Packing & Token Estimation Engine

`repomix` (formerly Repopack) bundles an entire repository or subset of directories into a single, structured markdown or XML document optimized for ingestion by large language models.

---

## ⚡ Core Features

1. **Single-File AI Ingestion**: Consolidates complex file trees into a unified format with clear file path separators.
2. **Token Count Metrics**: Reports exact token counts using BPE tokenizers so you know if your project fits in a context window.
3. **Secret Scrubbing**: Automatically removes API keys, JWT tokens, private SSH keys, and `.env` credentials before bundling.
4. **Gitignore Awareness**: Respects `.gitignore` and supports custom include/exclude glob patterns.

---

## 🛠️ How to Trigger

```bash
# Bundle entire workspace into repomix-output.xml
npx repomix

# Bundle only source directory in markdown format
npx repomix --style markdown --include "src/**"

# Output token count estimate
npx repomix --token-count
```

- In conversation: `"Use repomix to bundle the backend directory for review"` or `"Pack this repo with repomix and check token count"`.
