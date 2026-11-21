---
name: r3f-shaders-physics
description: Advanced 3D web capabilities including physics simulation with Rapier (@react-three/rapier), custom GLSL shaders (shaderMaterial), and post-processing visual effects (@react-three/postprocessing) in React Three Fiber. Use when creating realistic physical object interactions, custom water/hologram shaders, or cinematic post-processing (Bloom, Depth of Field).
metadata:
  author: pmndrs
  version: "8.17.10"
---

# R3F Shaders, Physics & Post-Processing

Advanced techniques for React Three Fiber to build high-end visual experiences and interactive physics simulations.

---

## 1. Physics with Rapier (`@react-three/rapier`)

Rapier is the fast, WASM-powered physics engine for React Three Fiber.

```bash
npm install @react-three/rapier
```

### Basic Physics World
```tsx
"use client";

import { Canvas } from "@react-three/fiber";
import { Physics, RigidBody } from "@react-three/rapier";

export function BouncingBallsScene() {
  return (
    <Canvas camera={{ position: [0, 5, 10], fov: 50 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 10, 5]} />

      <Physics gravity={[0, -9.81, 0]}>
        {/* Dynamic Falling Sphere */}
        <RigidBody restitution={0.8} colliders="ball">
          <mesh position={[0, 5, 0]}>
            <sphereGeometry args={[0.7, 32, 32]} />
            <meshStandardMaterial color="#f43f5e" roughness={0.2} />
          </mesh>
        </RigidBody>

        {/* Static Ground Floor */}
        <RigidBody type="fixed">
          <mesh position={[0, -2, 0]} rotation={[-Math.PI / 2, 0, 0]}>
            <planeGeometry args={[20, 20]} />
            <meshStandardMaterial color="#1e293b" />
          </mesh>
        </RigidBody>
      </Physics>
    </Canvas>
  );
}
```

---

## 2. Custom GLSL Shaders (`shaderMaterial`)

Drei's `shaderMaterial` makes creating custom GLSL materials declarative:

```tsx
import { shaderMaterial } from "@react-three/drei";
import { extend, useFrame } from "@react-three/fiber";
import { useRef } from "react";
import * as THREE from "three";

// 1. Define Material with Uniforms, Vertex, and Fragment GLSL
const WaveShaderMaterial = shaderMaterial(
  { uTime: 0, uColor: new THREE.Color(0.2, 0.6, 1.0) },
  // Vertex Shader
  `
    varying vec2 vUv;
    uniform float uTime;
    void main() {
      vUv = uv;
      vec3 pos = position;
      pos.z += sin(pos.x * 4.0 + uTime) * 0.2;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
    }
  `,
  // Fragment Shader
  `
    varying vec2 vUv;
    uniform vec3 uColor;
    void main() {
      gl_FragColor = vec4(uColor * vUv.x, 1.0);
    }
  `
);

// 2. Extend into R3F JSX catalog
extend({ WaveShaderMaterial });

// 3. Use in Mesh
export function WavyMesh() {
  const matRef = useRef<any>(null);

  useFrame((_, delta) => {
    if (matRef.current) matRef.current.uTime += delta * 2;
  });

  return (
    <mesh>
      <planeGeometry args={[4, 4, 32, 32]} />
      {/* @ts-ignore JSX extended */}
      <waveShaderMaterial ref={matRef} />
    </mesh>
  );
}
```

---

## 3. Cinematic Post-Processing (`@react-three/postprocessing`)

Add cinematic glow, blur, depth of field, and chromatic aberration:

```bash
npm install @react-three/postprocessing
```

```tsx
import { Canvas } from "@react-three/fiber";
import { EffectComposer, Bloom, Vignette, ChromaticAberration } from "@react-three/postprocessing";

export function GlowScene() {
  return (
    <Canvas>
      {/* 3D Content */}
      <mesh>
        <sphereGeometry />
        {/* High toneMapped: false color values glow with Bloom */}
        <meshBasicMaterial color={[1.5, 3.0, 5.0]} toneMapped={false} />
      </mesh>

      {/* Post Processing Layer */}
      <EffectComposer>
        <Bloom luminanceThreshold={1} luminanceSmoothing={0.9} intensity={1.5} />
        <Vignette eskil={false} offset={0.1} darkness={1.1} />
      </EffectComposer>
    </Canvas>
  );
}
```

