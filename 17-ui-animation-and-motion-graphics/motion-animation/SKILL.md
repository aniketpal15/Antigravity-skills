---
name: motion-animation
description: Comprehensive animation patterns, components, and physics using Motion (formerly Framer Motion) across React, Next.js, Vue, and Vanilla JS. Use when designing animations, page transitions, layout animations (layoutId), scroll-linked effects, gesture interactions, spring physics, or staggered entrances.
metadata:
  author: motiondivision
  version: "12.0.0"
---

# Motion (Framer Motion) Animation Guide & Patterns

Motion (package `motion`) is the modern, production-grade animation library for React, Vue, and vanilla JavaScript. Use this skill whenever implementing UI animations, micro-interactions, layout transitions, scroll effects, or physics-based motion.

---

## 1. Installation & Imports

```bash
# Recommended modern package
npm install motion
# or
pnpm add motion
```

### Import Styles
```tsx
// React / Next.js
import { motion, AnimatePresence, useScroll, useTransform, useSpring } from "motion/react";

// Vanilla JavaScript / TypeScript
import { animate, scroll, timeline, stagger } from "motion";
```

---

## 2. Core Animation Fundamentals (React)

### Basic Motion Component
```tsx
import { motion } from "motion/react";

export function FadeInCard() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.4, ease: [0.25, 0.1, 0.25, 1.0] }}
      className="p-6 bg-white rounded-xl shadow-md"
    >
      <h3>Animated Card</h3>
    </motion.div>
  );
}
```

### Spring Physics vs Easing
Use spring physics for natural, tactile UI interactions (buttons, dialogs, drawers).
```tsx
transition={{
  type: "spring",
  stiffness: 350,
  damping: 25,
  mass: 0.8,
}}
```

---

## 3. Gesture Animations

Motion natively handles hover, tap, drag, and focus states without manual event listeners:

```tsx
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  whileFocus={{ ring: "2px solid #3b82f6" }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
  className="px-4 py-2 bg-blue-600 text-white rounded-lg"
>
  Click Me
</motion.button>
```

### Dragging & Constraints
```tsx
<motion.div
  drag
  dragConstraints={{ left: -100, right: 100, top: -50, bottom: 50 }}
  dragElastic={0.2}
  whileDrag={{ scale: 1.1, cursor: "grabbing" }}
  className="w-24 h-24 bg-indigo-500 rounded-2xl cursor-grab"
/>
```

---

## 4. Exit Animations & Transitions (`AnimatePresence`)

Always wrap conditionally rendered components in `<AnimatePresence>`:

```tsx
import { motion, AnimatePresence } from "motion/react";

export function Modal({ isOpen, onClose, children }) {
  return (
    <AnimatePresence mode="wait">
      {isOpen && (
        <motion.div
          key="modal-backdrop"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center"
          onClick={onClose}
        >
          <motion.div
            key="modal-content"
            initial={{ scale: 0.9, opacity: 0, y: 20 }}
            animate={{ scale: 1, opacity: 1, y: 0 }}
            exit={{ scale: 0.9, opacity: 0, y: 20 }}
            transition={{ type: "spring", damping: 25, stiffness: 300 }}
            onClick={(e) => e.stopPropagation()}
            className="bg-white p-6 rounded-2xl max-w-lg w-full"
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```
> **CRITICAL RULE:** Direct children of `AnimatePresence` **MUST** have a unique `key` prop, or exit animations will fail to trigger.

---

## 5. Layout Animations & Shared Elements (`layout` & `layoutId`)

Motion automatically animates layout changes (e.g., resizing, reordering, tab indicators):

### Shared Layout Indicator (Tabs / Active State)
```tsx
function TabBar({ tabs, activeTab, onSelect }) {
  return (
    <div className="flex gap-2 p-1 bg-gray-100 rounded-lg">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() => onSelect(tab.id)}
          className="relative px-4 py-2 text-sm font-medium"
        >
          {activeTab === tab.id && (
            <motion.div
              layoutId="active-indicator"
              className="absolute inset-0 bg-white rounded-md shadow-sm"
              transition={{ type: "spring", stiffness: 380, damping: 30 }}
            />
          )}
          <span className="relative z-10">{tab.label}</span>
        </button>
      ))}
    </div>
  );
}
```

---

## 6. Scroll-Linked & Scroll-Triggered Animations

### While in View (Reveal on Scroll)
```tsx
<motion.div
  initial={{ opacity: 0, y: 50 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6 }}
>
  <h2>Section Title</h2>
</motion.div>
```

### Scroll Progress Indicator
```tsx
export function ScrollProgressBar() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30 });

  return (
    <motion.div
      style={{ scaleX }}
      className="fixed top-0 left-0 right-0 h-1 bg-blue-600 origin-left z-50"
    />
  );
}
```

---

## 7. Vanilla JavaScript / Framework-Agnostic API

For high performance without React:

```typescript
import { animate, scroll, timeline, stagger } from "motion";

// 1. Basic animate
animate(".box", { x: 100, opacity: 1 }, { duration: 0.8, easing: "ease-out" });

// 2. Staggered list
animate("li", { opacity: [0, 1], y: [20, 0] }, { delay: stagger(0.1) });

// 3. Complex multi-element Timeline
const sequence = [
  [".hero-title", { opacity: [0, 1], y: [30, 0] }, { duration: 0.6 }],
  [".hero-subtitle", { opacity: [0, 1] }, { duration: 0.4, at: "-0.2" }],
  [".cta-btn", { scale: [0.8, 1] }, { duration: 0.5, easing: "spring" }]
];
timeline(sequence);
```

---

## 8. Best Practices & Performance Checklist

1. **Hardware Acceleration:** Prefer animating `transform` (`x`, `y`, `scale`, `rotate`) and `opacity`. Avoid animating expensive layout properties like `width`, `height`, `top`, `left`, `margin`.
2. **`willChange`:** For complex or 3D animations, use CSS `will-change: transform;` or Motion's automatic hardware acceleration.
3. **Accessibility First (`prefers-reduced-motion`):**
   ```tsx
   import { useReducedMotion } from "motion/react";
   const shouldReduceMotion = useReducedMotion();
   const animateProp = shouldReduceMotion ? { opacity: 1 } : { opacity: 1, y: 0 };
   ```
4. **Avoid Stacking Transforms:** Do not mix inline Tailwind `transform -translate-x-1/2` with Motion `x: 50` on the same element — let Motion control the transform matrix.

