---
name: theatre-js-motion
description: Theatre.js visual keyframe and motion design editor engine. Use when animating Three.js 3D scenes, HTML5/SVG DOM elements, building complex camera moves, tweening complex properties, and creating cinematic interactive web stories.
---

# Theatre Js Motion

> **Category:** 3D & Web Motion Design  
> **Source Repository:** https://github.com/theatre-js/theatre  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `theatre-js-motion` skill gives Antigravity AI agents complete operational mastery over theatre js motion. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { theatre } from "theatre";

// Initialize and execute animation timeline
console.log("Initialized theatre-js-motion");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
