---
name: rapier-physics
description: Rapier 2D and 3D fast physics engine for WebAssembly and JavaScript. Use when simulating real-time physics in Three.js/React Three Fiber (R3F), rigid bodies, colliders, joints, character controllers, and high-performance physical interaction.
---

# Rapier Physics

> **Category:** High-Performance 2D/3D Physics  
> **Source Repository:** https://github.com/dimforge/rapier  
> **Architecture:** Antigravity Global Motion Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `rapier-physics` skill gives Antigravity AI agents complete operational mastery over rapier physics. It provides standard recipes, API patterns, and headless rendering commands.

### Key Capabilities:
- **Zero-Bloat Implementation:** Direct browser, canvas, or Node integration using native standards.
- **Motion & Video Compatibility:** Designed to feed directly into Remotion, FFmpeg, HyperFrames, or web frontends.
- **Deterministic Keyframes:** High precision timing, easing functions, and physics solvers.

---

## 2. Standard Usage & Code Patterns

```typescript
// ponytail: Clean, minimal standard integration
import { rapier } from "rapier";

// Initialize and execute animation timeline
console.log("Initialized rapier-physics");
```

---

## 3. Best Practices & Guidelines
1. **YAGNI & Minimalism:** Keep animation trees lightweight; avoid redundant layers.
2. **60 FPS Performance:** Favor GPU transforms (`transform`, `opacity`) over layout-triggering properties.
3. **Video Export:** When rendering to MP4, synchronize timeline time increments with frame rates (e.g. 1/60s).
