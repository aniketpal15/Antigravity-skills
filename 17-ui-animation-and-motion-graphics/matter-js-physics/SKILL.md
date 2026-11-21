---
name: matter-js-physics
description: Matter.js 2D rigid body physics simulation engine for the web. Use when creating physics-driven interactive graphics, gravity simulations, bouncy collision animations, particle systems, ragdoll physics, and constraints in 2D canvas.
---

# Matter Js Physics

> **Category:** 2D Physics & Dynamic Motion  
> **Source Repository:** https://github.com/liabru/matter-js  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `matter-js-physics` skill gives Antigravity AI agents complete operational mastery over matter js physics. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { matter } from "matter";

// Initialize and execute animation timeline
console.log("Initialized matter-js-physics");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
