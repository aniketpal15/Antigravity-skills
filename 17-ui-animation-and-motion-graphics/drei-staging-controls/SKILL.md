---
name: drei-staging-controls
description: Staging, studio lighting, camera controls, environment presets, and 3D HTML overlays using @react-three/drei. Use when setting up OrbitControls, ScrollControls (scroll-linked 3D journeys), Environment HDR maps, photorealistic ContactShadows, floating micro-interactions (Float), or embedding HTML/DOM UI inside a 3D scene (Html).
metadata:
  author: pmndrs
  version: "9.117.0"
---

# Drei Staging, Controls & Atmosphere Guide

`@react-three/drei` provides the essential building blocks to stage, illuminate, and interact with 3D scenes in React Three Fiber without hand-rolling Three.js boilerplate.

---

## 1. Installation

```bash
npm install three @react-three/fiber @react-three/drei
```

---

## 2. Camera & Interactive Controls

### OrbitControls (Standard 3D Camera Manipulation)
```tsx
import { OrbitControls } from "@react-three/drei";

<OrbitControls
  enableZoom={true}
  enablePan={false}
  minPolarAngle={Math.PI / 4} // Restrict vertical rotation
  maxPolarAngle={Math.PI / 2}
  autoRotate={true}
  autoRotateSpeed={1.2}
  dampingFactor={0.05} // Smooth inertia
/>
```

### PresentationControls (Spring-Back Product Showcase)
For hero banners where the user can grab and rotate a model, but it snaps back cleanly to center:
```tsx
import { PresentationControls } from "@react-three/drei";

<PresentationControls
  global={true}
  cursor={true}
  snap={true} // Snaps back to initial rotation
  speed={1.5}
  zoom={1}
  rotation={[0, 0, 0]}
  polar={[-Math.PI / 6, Math.PI / 6]}
  azimuth={[-Math.PI / 4, Math.PI / 4]}
>
  <Model />
</PresentationControls>
```

### ScrollControls (Scroll-Driven 3D Experiences)
Create Apple-style 3D journeys where scrolling the webpage drives the camera or model:
```tsx
import { Canvas } from "@react-three/fiber";
import { ScrollControls, Scroll, useScroll } from "@react-three/drei";
import { useFrame } from "@react-three/fiber";
import { useRef } from "react";
import type { Mesh } from "three";

function AnimatedMesh() {
  const meshRef = useRef<Mesh>(null);
  const scroll = useScroll(); // scroll.offset ranges from 0 to 1

  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.y = scroll.offset * Math.PI * 2;
      meshRef.current.position.z = -scroll.offset * 5;
    }
  });

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[2, 2, 2]} />
      <meshStandardMaterial color="#6366f1" />
    </mesh>
  );
}

export function ScrollScene() {
  return (
    <Canvas>
      <ambientLight />
      <ScrollControls pages={3} damping={0.25}>
        {/* 3D Canvas elements */}
        <Scroll>
          <AnimatedMesh />
        </Scroll>

        {/* Regular HTML content synced to 3D scroll */}
        <Scroll html>
          <h1 className="absolute top-[20vh] left-[10vw] text-white text-4xl">Page 1</h1>
          <h1 className="absolute top-[120vh] left-[10vw] text-white text-4xl">Page 2</h1>
          <h1 className="absolute top-[220vh] left-[10vw] text-white text-4xl">Page 3</h1>
        </Scroll>
      </ScrollControls>
    </Canvas>
  );
}
```

---

## 3. Instant Staging & Studio Lighting

### The `<Stage>` Shortcut (Zero Config Studio Setup)
Sets up automatic soft shadows, ambient lighting, studio bounce lights, and centers your model automatically:
```tsx
import { Stage } from "@react-three/drei";

<Canvas>
  <Stage environment="city" intensity={0.6} contactShadow={{ opacity: 0.7, blur: 2 }}>
    <ShoeModel />
  </Stage>
</Canvas>
```

### `<Environment>` (HDR Image Based Lighting)
Provides photorealistic reflections and global illumination using built-in presets:
```tsx
import { Environment } from "@react-three/drei";

// Available presets: "sunset", "dawn", "night", "warehouse", "forest", "apartment", "studio", "city", "park", "lobby"
<Environment preset="studio" background={false} blur={0.8} />
```

### Soft Contact Shadows (`<ContactShadows>`)
High-performance, ground-contact shadows rendered without expensive shadow maps:
```tsx
import { ContactShadows } from "@react-three/drei";

<ContactShadows
  position={[0, -1.5, 0]}
  opacity={0.7}
  scale={10}
  blur={1.5}
  far={4}
  color="#000000"
/>
```

---

## 4. Embedding HTML in 3D (`<Html>`)

Place responsive React DOM components, interactive buttons, or annotations directly onto 3D objects:

```tsx
import { Html } from "@react-three/drei";

<mesh position={[1, 2, 0]}>
  <sphereGeometry args={[0.2]} />
  <meshBasicMaterial color="red" />

  {/* Pinned HTML Tooltip */}
  <Html
    position={[0, 0.3, 0]}
    center
    distanceFactor={10} // Scales HTML with 3D camera distance
    occlude // Hides HTML if a 3D object blocks line-of-sight
  >
    <div className="bg-white/90 backdrop-blur-md px-3 py-1 rounded-lg shadow-lg text-xs font-semibold text-gray-800 pointer-events-none whitespace-nowrap">
      Camera Sensor (48MP)
    </div>
  </Html>
</mesh>
```

---

## 5. Atmosphere: Float, Stars & Sparkles

```tsx
import { Float, Stars, Sparkles } from "@react-three/drei";

// Gentle hovering animation
<Float speed={2} rotationIntensity={0.5} floatIntensity={1} floatingRange={[-0.1, 0.1]}>
  <MyModel />
</Float>

// Night Sky & Particles
<Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
<Sparkles count={50} scale={5} size={3} speed={0.4} color="#fef08a" />
```

