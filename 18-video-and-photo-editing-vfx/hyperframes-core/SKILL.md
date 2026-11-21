---
name: hyperframes-core
description: HyperFrames core video engine: write HTML/CSS/JS, render video. Built for AI agents to generate framerate-locked, multi-track, template-driven MP4 videos from standard web code without native video software.
---

# Hyperframes Core

> **Category:** Web-to-Video Engine  
> **Source Repository:** https://github.com/heygen-com/hyperframes  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `hyperframes-core` skill gives Antigravity AI agents complete operational mastery over hyperframes core. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { hyperframes } from "hyperframes";

// Initialize and execute animation timeline
console.log("Initialized hyperframes-core");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
