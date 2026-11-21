---
name: tsparticles-engine
description: tsParticles particle animation engine. Use when creating interactive particle backgrounds, confetti celebrations, fireworks, floating stars, smoke, snow, and dynamic canvas particle effects for landing pages and video overlays.
---

# Tsparticles Engine

> **Category:** Particle Systems & Visual FX  
> **Source Repository:** https://github.com/tsparticles/tsparticles  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `tsparticles-engine` skill gives Antigravity AI agents complete operational mastery over tsparticles engine. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { tsparticles } from "tsparticles";

// Initialize and execute animation timeline
console.log("Initialized tsparticles-engine");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
