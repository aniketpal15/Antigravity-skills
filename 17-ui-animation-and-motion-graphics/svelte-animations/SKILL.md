---
name: svelte-animations
description: Svelte port of Aceternity UI, Magic UI, Indie UI, Luxe, and Motion animation components for SvelteKit projects. Use when building animated Svelte components, Svelte landing pages with motion effects, or porting React animation libraries like Aceternity UI and Magic UI into SvelteKit.
metadata:
  author: SikandarJODD
  version: "1.0.0"
---

# Svelte Animations Guide

This library ports popular React animation libraries (Aceternity UI, Magic UI, Indie UI, Luxe) into native Svelte components for SvelteKit projects.

---

## 1. Installation & Setup

```bash
# SvelteKit project
npx sv create my-app --template minimal --types ts

# Install dependencies
npm install clsx tailwind-merge
npm install -D tailwindcss autoprefixer

# Install component dependencies (animation-specific)
npm install @motionone/svelte  # For Motion One animations
```

Add Tailwind utility merger:
```ts
// src/lib/utils.ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

---

## 2. Aceternity UI Svelte Components

### Animated Gradient Hero Text
```svelte
<script lang="ts">
  import { cn } from "$lib/utils";
</script>

<div class="relative flex items-center justify-center min-h-screen">
  <h1
    class={cn(
      "text-6xl font-bold text-center bg-clip-text text-transparent",
      "bg-gradient-to-r from-violet-500 via-pink-500 to-cyan-500",
      "animate-gradient bg-[length:200%_auto]"
    )}
  >
    Build Faster with Svelte
  </h1>
</div>

<style>
  @keyframes gradient {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
  }
  .animate-gradient {
    animation: gradient 3s linear infinite;
  }
</style>
```

### Spotlight Card Effect
```svelte
<script lang="ts">
  let mouseX = $state(0);
  let mouseY = $state(0);

  function handleMouseMove(e: MouseEvent) {
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
  }
</script>

<div
  class="group relative w-72 h-96 rounded-2xl bg-zinc-900 border border-zinc-800 overflow-hidden"
  onmousemove={handleMouseMove}
>
  <!-- Spotlight overlay -->
  <div
    class="pointer-events-none absolute inset-0 opacity-0 group-hover:opacity-100 transition duration-300"
    style="background: radial-gradient(400px circle at {mouseX}px {mouseY}px, rgba(139,92,246,0.15), transparent 60%)"
  />
  <div class="relative z-10 p-6 h-full flex flex-col justify-end">
    <h3 class="text-white text-xl font-semibold">Card Title</h3>
    <p class="text-zinc-400 text-sm mt-1">Hover to see the spotlight effect</p>
  </div>
</div>
```

---

## 3. Magic UI Svelte: Shimmer Button
```svelte
<script lang="ts">
  let { children, class: className = "", onclick } = $props();
</script>

<button
  {onclick}
  class="relative inline-flex overflow-hidden rounded-full p-[1px] focus:outline-none focus:ring-2 focus:ring-violet-500 {className}"
>
  <span class="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#E2CBFF_0%,#393BB2_50%,#E2CBFF_100%)]" />
  <span class="inline-flex h-full w-full cursor-pointer items-center justify-center rounded-full bg-zinc-950 px-6 py-2 text-sm font-medium text-white backdrop-blur-3xl gap-2">
    {@render children?.()}
  </span>
</button>
```

---

## 4. Motion One Svelte Animations

```svelte
<script lang="ts">
  import { animate } from "@motionone/dom";
  import { onMount } from "svelte";

  let cardEl: HTMLDivElement;

  onMount(() => {
    animate(
      cardEl,
      { opacity: [0, 1], y: [30, 0] },
      { duration: 0.6, easing: [0.25, 0.1, 0.25, 1] }
    );
  });
</script>

<div bind:this={cardEl} class="p-6 bg-white rounded-xl shadow-md opacity-0">
  <h2 class="text-xl font-bold">Animated on Mount</h2>
</div>
```

---

## 5. Key Differences from React (Critical Rules)

| React / Framer Motion Pattern | Svelte Equivalent |
|---|---|
| `useState(false)` | `let visible = $state(false)` |
| `useEffect(() => {}, [])` | `onMount(() => {})` |
| `className={cn(...)}` | `class={cn(...)}` |
| `onClick={handler}` | `onclick={handler}` |
| `{children}` prop | `{@render children?.()}` with `$props()` |
| `AnimatePresence` + `motion.div` | CSS transitions + `{#if}` block |

---

## 6. SvelteKit-Specific Best Practices

1. **Use `$state()` rune** for reactive animation state (Svelte 5).
2. **CSS-based animations beat JS** for simple effects — prefer `@keyframes` + Tailwind.
3. **For complex sequences** use Motion One (`@motionone/dom`) over manual CSS.
4. **Transitions on `{#if}` blocks:** Use Svelte's built-in `transition:fade` and `transition:fly` directives for enter/exit:
   ```svelte
   <script>
     import { fade, fly } from "svelte/transition";
   </script>
   {#if visible}
     <div transition:fly={{ y: 20, duration: 300 }}>Animated!</div>
   {/if}
   ```

