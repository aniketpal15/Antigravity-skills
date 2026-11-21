---
name: scroll-trigger
description: Advanced scroll-driven animations, horizontal scroll sections, sticky element pinning, scrubbing, and parallax effects using GSAP ScrollTrigger. Use when building interactive scroll experiences, landing page reveals, pinned storytellers, or scroll progress counters.
metadata:
  author: greensock
  version: "3.12.5"
---

# GSAP ScrollTrigger Guide & Patterns

ScrollTrigger enables high-performance, scroll-based animations: scrubbed timelines, pinned sections, horizontal scroll galleries, and scroll-direction reactions.

---

## 1. Setup & Core Syntax

```typescript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
```

### Basic Scroll Trigger
```typescript
gsap.to(".reveal-box", {
  scrollTrigger: {
    trigger: ".reveal-box",
    start: "top 80%", // When top of trigger hits 80% from top of viewport
    end: "top 30%",
    toggleActions: "play none none reverse", // onEnter, onLeave, onEnterBack, onLeaveBack
    markers: false // Set true during development for visual guidelines
  },
  y: 0,
  opacity: 1,
  duration: 1
});
```

---

## 2. Scrubbed Timelines (Animation Bound to Scroll Position)

With `scrub`, the animation advances as the user scrolls forwards and rewinds as they scroll backwards.

```typescript
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".story-container",
    start: "top top",
    end: "+=2000",      // Scroll distance of 2000px
    scrub: 1,           // 1 second smooth catch-up smoothing
    pin: true           // Pin the container during the 2000px scroll
  }
});

tl.from(".chapter-1", { opacity: 0, scale: 0.8 })
  .to(".chapter-1", { opacity: 0, y: -50 }, "+=0.5")
  .from(".chapter-2", { opacity: 0, y: 50 })
  .to(".chapter-2", { opacity: 0, scale: 1.2 }, "+=0.5")
  .from(".chapter-3", { opacity: 0, scale: 0.8 });
```

---

## 3. Pinned Horizontal Scrolling Gallery

Create Apple-style horizontal scrolling sections:

```typescript
const sections = gsap.utils.toArray<HTMLElement>(".panel");

gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: "none", // Must be none for linear scroll scrubbing!
  scrollTrigger: {
    trigger: ".horizontal-wrapper",
    pin: true,
    scrub: 1,
    snap: 1 / (sections.length - 1), // Snap cleanly to each panel
    end: () => "+=" + document.querySelector<HTMLElement>(".horizontal-wrapper")!.offsetWidth
  }
});
```

---

## 4. ScrollTrigger in React / Next.js (`useGSAP`)

```tsx
"use client";

import { useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger);

export function PinnedFeatures() {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    gsap.to(".feature-graphic", {
      rotation: 360,
      scrollTrigger: {
        trigger: containerRef.current,
        start: "top top",
        end: "+=1500",
        scrub: 0.5,
        pin: true
      }
    });
  }, { scope: containerRef });

  return (
    <div ref={containerRef} className="h-screen flex items-center justify-center bg-zinc-900 text-white">
      <div className="feature-graphic w-40 h-40 bg-gradient-to-tr from-cyan-500 to-blue-600 rounded-2xl" />
    </div>
  );
}
```

---

## 5. Responsive Scroll Animations (`ScrollTrigger.matchMedia`)

Never use raw window resize listeners. Use GSAP's built-in media query manager:

```typescript
ScrollTrigger.matchMedia({
  // Desktop
  "(min-width: 800px)": function() {
    gsap.to(".sidebar", {
      scrollTrigger: {
        trigger: ".main-content",
        start: "top top",
        end: "bottom bottom",
        pin: ".sidebar"
      }
    });
  },
  // Mobile (No pinning, simple reveal)
  "(max-width: 799px)": function() {
    gsap.from(".sidebar", {
      scrollTrigger: ".sidebar",
      y: 50,
      opacity: 0
    });
  }
});
```

---

## 6. Debugging & Common Pitfalls

1. **Start & End Guidelines:** Set `markers: true` during development to visualize trigger points (`scroller-start`, `start`, `scroller-end`, `end`).
2. **Dynamic Height Changes:** If images or fonts load asynchronously after page render, call `ScrollTrigger.refresh()` to recalculate trigger positions.
3. **Avoid CSS `overflow: hidden` on Pin Parents:** Applying `overflow: hidden` to parent containers can break scroll calculation for pinned elements.
4. **Scrub Easing:** When using `scrub`, set tween `ease: "none"` unless you explicitly want non-linear scrolling speeds.

