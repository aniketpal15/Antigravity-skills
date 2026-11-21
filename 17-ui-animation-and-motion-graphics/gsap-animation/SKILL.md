---
name: gsap-animation
description: High-performance animations, choreographed timelines, and physics-driven micro-interactions using GSAP 3 (GreenSock Animation Platform) across React, Next.js, Vue, and Vanilla JS. Use when building complex multi-step timelines, SVG morphing, text effects, stagger animations, or high-framerate interactive canvas/DOM motion.
metadata:
  author: greensock
  version: "3.12.5"
---

# GSAP (GreenSock Animation Platform) Guide & Patterns

GSAP 3 is the industry-standard high-performance animation engine for web development. Use this skill whenever choreographing complex sequenced animations, orchestrating multi-element timelines, animating SVG paths, or implementing high-frequency DOM manipulations.

---

## 1. Installation & Imports

```bash
# Core GSAP + React hook
npm install gsap @gsap/react
# or
pnpm add gsap @gsap/react
```

### Modern Module Imports
```typescript
// Core & Plugins
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Flip } from "gsap/Flip";
import { TextPlugin } from "gsap/TextPlugin";

// Register plugins once
gsap.registerPlugin(ScrollTrigger, Flip, TextPlugin);
```

---

## 2. Core GSAP Methods

### Tweens (`to`, `from`, `fromTo`, `set`)
```typescript
// gsap.to (Animate to destination values)
gsap.to(".card", {
  x: 100,
  opacity: 1,
  duration: 0.8,
  ease: "power2.out",
  stagger: 0.1 // Stagger items
});

// gsap.from (Animate from initial values to current CSS)
gsap.from(".hero-title", {
  y: 60,
  opacity: 0,
  duration: 1.2,
  ease: "power3.out"
});

// gsap.fromTo (Explicit start and end state)
gsap.fromTo(".badge", 
  { scale: 0, opacity: 0 },
  { scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.7)" }
);

// Immediate set without animation
gsap.set(".modal", { autoAlpha: 0 }); // autoAlpha controls both opacity and visibility
```

---

## 3. Timelines: Orchestrated Multi-Step Sequences

Timelines are GSAP's superpower. Avoid messy `setTimeout` chains or manual delay calculations.

```typescript
const tl = gsap.timeline({
  defaults: { duration: 0.6, ease: "power2.out" },
  onComplete: () => console.log("Sequence done!")
});

tl.from(".nav-bar", { y: -50, opacity: 0 })
  .from(".hero-headline", { y: 30, opacity: 0 }, "-=0.2") // Starts 0.2s before nav-bar finishes
  .from(".hero-sub", { y: 20, opacity: 0 }, "<")         // Starts at the exact same time as previous tween
  .from(".cta-button", { scale: 0.8, opacity: 0, ease: "back.out(2)" }, "+=0.1")
  .from(".feature-card", { y: 40, opacity: 0, stagger: 0.15 });
```

### Position Parameter Cheat Sheet:
* `"+=1"` — 1 second after previous animation ends
* `"-=0.5"` — 0.5 seconds before previous animation ends (overlap)
* `"<"` — At the exact same start time as previous animation
* `"<0.2"` — 0.2s after the previous animation starts

---

## 4. GSAP in React & Next.js (`useGSAP`)

Always use `@gsap/react`'s `useGSAP` hook. It handles automatic cleanup (`revert()`), context scoping, and prevents memory leaks / strict-mode double invocation bugs.

```tsx
"use client";

import { useRef } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";

export function HeroSection() {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    // Queries are automatically scoped to containerRef.current!
    // No need for separate refs on every single child element.
    gsap.from(".title", {
      y: 50,
      opacity: 0,
      duration: 1,
      ease: "power3.out"
    });

    gsap.from(".item", {
      scale: 0.9,
      opacity: 0,
      stagger: 0.1,
      delay: 0.3
    });
  }, { scope: containerRef }); // Scope is critical!

  return (
    <div ref={containerRef} className="hero p-10">
      <h1 className="title text-4xl font-bold">Welcome to Next.js</h1>
      <div className="flex gap-4 mt-6">
        <div className="item p-4 bg-white rounded shadow">Feature 1</div>
        <div className="item p-4 bg-white rounded shadow">Feature 2</div>
        <div className="item p-4 bg-white rounded shadow">Feature 3</div>
      </div>
    </div>
  );
}
```

---

## 5. Smooth Layout Morphing with Flip Plugin

Smoothly animate elements changing DOM hierarchy, grid to list layouts, or expanding cards:

```typescript
import { Flip } from "gsap/Flip";
gsap.registerPlugin(Flip);

function toggleLayout() {
  const elements = document.querySelectorAll(".card");
  
  // 1. Capture current position & size
  const state = Flip.getState(elements);
  
  // 2. Make DOM / CSS changes (e.g. toggle grid vs list class)
  container.classList.toggle("list-view");
  
  // 3. Smoothly animate between the two states
  Flip.from(state, {
    duration: 0.7,
    ease: "power2.inOut",
    stagger: 0.05,
    absolute: true // Seamless re-parenting
  });
}
```

---

## 6. Performance & Animation Hygiene

1. **Hardware Acceleration:** Animate `x`, `y`, `scale`, `rotation`, and `autoAlpha`. Never animate `left`, `top`, `width`, or `margin` for movement.
2. **`autoAlpha` instead of `opacity`:** Use `autoAlpha: 0` so GSAP automatically sets `visibility: hidden` when opacity hits 0, preventing ghost clicks on transparent elements.
3. **Always Clean Up in Frameworks:** In React, always use `useGSAP()` or manually call `ctx.revert()` in `useEffect` cleanup.
4. **Use GSAP Context for dynamic elements:**
   ```typescript
   const ctx = gsap.context(() => { ... });
   return () => ctx.revert();
   ```

