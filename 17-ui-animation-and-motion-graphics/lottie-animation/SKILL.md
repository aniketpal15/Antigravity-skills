---
name: lottie-animation
description: Render, control, and interact with After Effects Lottie and DotLottie vector animations in React, Next.js, and web apps using lottie-react and @lottiefiles/dotlottie-react. Use when embedding animated icons, loading spinners, celebratory confetti, interactive hover micro-interactions, or scroll-scrubbed vector animations.
metadata:
  author: LottieFiles
  version: "1.0.0"
---

# Lottie Animation Guide & Patterns (React & Next.js)

Lottie renders lightweight, resolution-independent vector animations exported from Adobe After Effects (via Bodymovin) or the LottieFiles platform.

---

## 1. Packages & Modern Setup

There are two primary modern options in the React ecosystem:

```bash
# Option A: Universal lottie-react (Supports JSON animations + useLottie hook)
npm install lottie-react

# Option B: Official Next-Gen DotLottie (Up to 80% smaller .lottie binary files)
npm install @lottiefiles/dotlottie-react
```

---

## 2. Universal React Pattern (`lottie-react`)

### Basic Component
```tsx
"use client";

import Lottie from "lottie-react";
import successAnimation from "@/public/animations/success.json";

export function SuccessBadge() {
  return (
    <div className="w-32 h-32">
      <Lottie
        animationData={successAnimation}
        loop={false}
        autoplay={true}
        onComplete={() => console.log("Animation finished!")}
      />
    </div>
  );
}
```

### Advanced Control with `useLottie` Hook
The `useLottie` hook provides full programmatic playback, segment playing, and speed control:

```tsx
"use client";

import { useLottie } from "lottie-react";
import loadingAnimation from "@/public/animations/loading.json";

export function InteractiveLoader() {
  const options = {
    animationData: loadingAnimation,
    loop: true,
    autoplay: false,
  };

  const style = {
    height: 200,
    width: 200,
  };

  const { View, play, pause, stop, setSpeed, goToAndPlay } = useLottie(options, style);

  return (
    <div className="flex flex-col items-center gap-4">
      {View}
      <div className="flex gap-2">
        <button onClick={() => play()} className="px-3 py-1 bg-green-500 text-white rounded">
          Play
        </button>
        <button onClick={() => pause()} className="px-3 py-1 bg-yellow-500 text-white rounded">
          Pause
        </button>
        <button onClick={() => setSpeed(2)} className="px-3 py-1 bg-blue-500 text-white rounded">
          2x Speed
        </button>
        <button onClick={() => goToAndPlay(20, true)} className="px-3 py-1 bg-purple-500 text-white rounded">
          Jump to Frame 20
        </button>
      </div>
    </div>
  );
}
```

---

## 3. Micro-Interaction: Play on Hover

Great for interactive navigation icons, heart buttons, or shopping carts:

```tsx
"use client";

import { useRef } from "react";
import Lottie, { LottieRefCurrentProps } from "lottie-react";
import bellAnimation from "@/public/animations/bell.json";

export function NotificationBell() {
  const lottieRef = useRef<LottieRefCurrentProps>(null);

  return (
    <button
      onMouseEnter={() => lottieRef.current?.play()}
      onMouseLeave={() => lottieRef.current?.stop()}
      className="p-3 bg-gray-100 hover:bg-gray-200 rounded-full transition"
    >
      <div className="w-8 h-8">
        <Lottie
          lottieRef={lottieRef}
          animationData={bellAnimation}
          autoplay={false}
          loop={false}
        />
      </div>
    </button>
  );
}
```

---

## 4. Next-Gen DotLottie Pattern (`@lottiefiles/dotlottie-react`)

If using `.lottie` files (smaller, compressed, and faster than raw JSON):

```tsx
"use client";

import { DotLottieReact } from "@lottiefiles/dotlottie-react";

export function RocketBanner() {
  return (
    <DotLottieReact
      src="https://lottie.host/your-animation-id.lottie"
      loop
      autoplay
      className="w-64 h-64 mx-auto"
    />
  );
}
```

---

## 5. Next.js App Router & SSR Safety Checklist

Lottie relies on browser APIs (`window`, `document`, Canvas/SVG DOM). In Next.js App Router:

1. **Always add `"use client"`** at the top of any file rendering a Lottie component.
2. **Dynamic Import with `ssr: false`** (if you encounter hydration warnings):
   ```tsx
   import dynamic from "next/dynamic";

   const Lottie = dynamic(() => import("lottie-react"), { ssr: false });
   ```
3. **Prefer Storing JSON in `/public/animations/`** or fetching remotely to keep JavaScript bundle sizes small.
4. **Clean up memory on unmount:** Lottie instances automatically destroy canvas/SVG listeners when the component unmounts.

