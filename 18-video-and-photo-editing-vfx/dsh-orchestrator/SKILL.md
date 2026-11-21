---
name: dsh-orchestrator
description: Background batch-processing, asset scraping, parallel render orchestration, and harness runner adapted from DeepSeek Harness / Cordis for Antigravity.
---

# DeepSeek Harness Orchestrator (Antigravity Adaptation)

This skill provides an orchestration framework for parallel video rendering, automated asset scraping, and multi-agent task distribution based on patterns from `vendors/deepseek-harness`.

## Core Capabilities

1. **Parallel Render Queue**:
   - Manages render batch queues using Remotion CLI and headless workers.
   - Splits long video sequences into multi-scene chunked renders and joins them via FFmpeg stream concatenation (`-c copy`).
   - Ensures concurrency controls (`--concurrency=2`) to prevent GPU / RAM starvation on local machines.

2. **Automated Asset Extraction & Scraping**:
   - Fetches web assets, SVG brand assets, and product metadata headlessly.
   - Normalizes raster assets into WebP / PNG sequences with optimal DPI.

3. **Background Task Execution**:
   - Leverages Antigravity background task execution (`run_command` with async/background lifecycle) to monitor render jobs without blocking prompt iteration.
   - Provides deterministic state tracking and heartbeat verification.

## Execution Syntax
```bash
# Example parallel render dispatch
npx remotion render src/Root.tsx <CompositionId> renders/<output>.mp4 --concurrency=2
```
