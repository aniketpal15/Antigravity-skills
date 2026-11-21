---
name: p5js-creative-coding
description: p5.js creative coding and algorithmic generative art engine. Use when programming generative visual art, procedural motion patterns, mathematical fractals, noise algorithms (Perlin/Simplex), and audio-reactive canvas animations.
---

# P5Js Creative Coding

> **Category:** Creative Coding & Generative Motion  
> **Source Repository:** https://github.com/processing/p5.js  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `p5js-creative-coding` skill gives Antigravity AI agents complete operational mastery over p5js creative coding. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { p5js } from "p5js";

// Initialize and execute animation timeline
console.log("Initialized p5js-creative-coding");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
