---
name: motion-canvas-engine
description: Motion Canvas programmatic vector animation engine. Use when coding video animations in TypeScript, generating educational and technical explainer videos, animating math/code diagrams, and rendering vector frames directly to MP4.
---

# Motion Canvas Engine

> **Category:** Programmatic Vector Animation  
> **Source Repository:** https://github.com/motion-canvas/motion-canvas  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `motion-canvas-engine` skill gives Antigravity AI agents complete operational mastery over motion canvas engine. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { motion } from "motion";

// Initialize and execute animation timeline
console.log("Initialized motion-canvas-engine");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
