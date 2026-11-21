---
name: r3f-3d-web
description: Declarative 3D web graphics, scenes, and interactive experiences in React and Next.js using React Three Fiber (@react-three/fiber) and Drei (@react-three/drei). Use when building 3D product configurators, hero landing page visuals, loading .gltf/.glb models, setting up lighting/cameras, or handling 3D pointer interactions.
metadata:
  author: pmndrs
  version: "8.17.10"
---

# React Three Fiber (R3F) & Drei Guide

React Three Fiber is a React reconciler for Three.js. It lets you build interactive 3D scenes declaratively with re-usable, self-contained components that react to state and user input.

---

## 1. Installation & Dependencies

```bash
npm install three @types/three @react-three/fiber @react-three/drei
# or
pnpm add three @types/three @react-three/fiber @react-three/drei
```

---

## 2. Basic Scene Setup

Every R3F scene starts with a `<Canvas>`. The Canvas takes up the full width and height of its parent container.

```tsx
"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

export function SimpleScene() {
  return (
    <div className="w-full h-[500px] bg-zinc-950 rounded-2xl overflow-hidden">
      <Canvas camera={{ position: [0, 0, 5], fov: 50 }}>
        {/* Lights */}
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} intensity={1} />

        {/* 3D Mesh */}
        <mesh rotation={[0.4, 0.2, 0]}>
          <boxGeometry args={[1.5, 1.5, 1.5]} />
          <meshStandardMaterial color="#6366f1" roughness={0.3} metalness={0.2} />
        </mesh>

        {/* Controls */}
        <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={1.5} />
      </Canvas>
    </div>
  );
}
```

---

## 3. The Animation Loop (`useFrame`)

Never use `setInterval` or React `useEffect` state loops for 3D animations. Use R3F's `useFrame` hook, which runs on every rendered frame before Three.js renders the scene.

```tsx
import { useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import type { Mesh } from "three";

export function SpinningBox() {
  const meshRef = useRef<Mesh>(null);
  const [hovered, setHovered] = useState(false);

  useFrame((state, delta) => {
    if (meshRef.current) {
      // delta ensures smooth speed independent of user monitor refresh rate (60Hz, 120Hz, 144Hz)
      meshRef.current.rotation.x += delta * 0.5;
      meshRef.current.rotation.y += delta * (hovered ? 2 : 0.8);
    }
  });

  return (
    <mesh
      ref={meshRef}
      onPointerOver={() => setHovered(true)}
      onPointerOut={() => setHovered(false)}
      scale={hovered ? 1.2 : 1}
    >
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? "#ec4899" : "#3b82f6"} roughness={0.1} />
    </mesh>
  );
}
```

---

## 4. Loading 3D Models (`.glb` / `.gltf`) with Drei

Use `useGLTF` from `@react-three/drei` with React `<Suspense>`:

```tsx
"use client";

import { Suspense } from "react";
import { Canvas } from "@react-three/fiber";
import { useGLTF, Environment, Float, ContactShadows } from "@react-three/drei";

function Model({ url }: { url: string }) {
  const { scene } = useGLTF(url);
  return <primitive object={scene} scale={2} position={[0, -1, 0]} />;
}

export function ProductShowcase() {
  return (
    <div className="w-full h-screen bg-slate-900">
      <Canvas shadows camera={{ position: [0, 0, 6], fov: 45 }}>
        <ambientLight intensity={0.7} />
        <directionalLight position={[5, 5, 5]} castShadow />

        <Suspense fallback={null}>
          <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
            <Model url="/models/shoe.glb" />
          </Float>
          <Environment preset="city" />
          <ContactShadows position={[0, -1.8, 0]} opacity={0.6} scale={10} blur={2} far={4} />
        </Suspense>
      </Canvas>
    </div>
  );
}

// Preload assets for instant rendering
useGLTF.preload("/models/shoe.glb");
```

---

## 5. Next.js App Router (SSR-Safe Setup)

Three.js and WebGL cannot run on the server. In Next.js:

1. **Always add `"use client"`** to components using Three.js / Canvas.
2. **Dynamic Import with `ssr: false`:**
   ```tsx
   import dynamic from "next/dynamic";

   export const Scene = dynamic(
     () => import("@/components/Scene").then((mod) => mod.Scene),
     { ssr: false, loading: () => <div className="w-full h-96 bg-zinc-900 animate-pulse" /> }
   );
   ```

---

## 6. Performance & Optimization Checklist

1. **Geometry Reuse & Instancing:** When rendering thousands of identical objects (particles, trees, coins), use `<Instances>` and `<Instance>` from `@react-three/drei` instead of individual meshes.
2. **Frame Loop Demand:** For static scenes (only re-rendering on interaction), set `<Canvas frameloop="demand">` to save battery and GPU power.
3. **Model Compression:** Always compress `.gltf` / `.glb` files using Draco compression or `gltf-pipeline`.
4. **Dispose Unused Assets:** R3F handles automatic disposal of geometries and materials on unmount, but textures loaded via standard Three loaders should be explicitly disposed if unmounted.

