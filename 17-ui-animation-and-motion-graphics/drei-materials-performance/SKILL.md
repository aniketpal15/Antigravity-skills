---
name: drei-materials-performance
description: High-end materials (MeshTransmissionMaterial glass, MeshReflectorMaterial, Decals, Portal materials) and performance optimization (BVH raycasting, Instances, AdaptiveDpr, useGLTF) using @react-three/drei. Use when creating frosted glass/acrylic UI, projecting stickers/logos onto 3D models, rendering 3D typography (Text/Text3D), or optimizing frame rates on low-end hardware.
metadata:
  author: pmndrs
  version: "9.117.0"
---

# Drei Materials, Typography & Performance Guide

Advanced materials, asset loaders, and performance optimization tools from `@react-three/drei`.

---

## 1. High-End Materials

### Frosted Glass & Refraction (`MeshTransmissionMaterial`)
Creates realistic physical glass, acrylic, and gemstone refraction:
```tsx
import { MeshTransmissionMaterial } from "@react-three/drei";

<mesh>
  <sphereGeometry args={[1, 32, 32]} />
  <MeshTransmissionMaterial
    backside={false}
    samples={10}
    resolution={512}
    transmission={1}
    roughness={0.15}
    thickness={0.6}
    ior={1.5}             // Index of Refraction (1.5 = Glass, 2.4 = Diamond)
    chromaticAberration={0.06} // Rainbow edge refraction
    anisotropy={0.1}
    distortion={0.2}
    distortionScale={0.3}
    temporalDistortion={0.5}
    color="#ffffff"
  />
</mesh>
```

### Mirror Reflections (`MeshReflectorMaterial`)
Creates reflective ground floors, glossy marble, or wet asphalt:
```tsx
import { MeshReflectorMaterial } from "@react-three/drei";

<mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -1, 0]}>
  <planeGeometry args={[30, 30]} />
  <MeshReflectorMaterial
    blur={[300, 100]}
    resolution={1024}
    mirror={0.7}
    mixBlur={1}
    mixStrength={40}
    roughness={0.4}
    depthScale={1.2}
    minDepthThreshold={0.4}
    maxDepthThreshold={1.4}
    color="#101010"
    metalness={0.5}
  />
</mesh>
```

### Organic Liquid Distortion (`MeshDistortMaterial` & `MeshWobbleMaterial`)
```tsx
import { MeshDistortMaterial } from "@react-three/drei";

<mesh>
  <sphereGeometry args={[1, 64, 64]} />
  <MeshDistortMaterial color="#ec4899" distort={0.4} speed={2} roughness={0.2} />
</mesh>
```

### Projecting Logos & Stickers (`Decal`)
Project a 2D texture directly onto a curved 3D mesh without editing the model's UV map:
```tsx
import { Decal, useTexture } from "@react-three/drei";

function TShirt() {
  const logoTexture = useTexture("/textures/logo.png");

  return (
    <mesh geometry={shirtGeometry}>
      <meshStandardMaterial color="#ffffff" />
      {/* Project logo onto the chest */}
      <Decal
        position={[0, 0.2, 0.15]} // Placement on mesh surface
        rotation={[0, 0, 0]}
        scale={[0.2, 0.2, 0.2]}
        map={logoTexture}
      />
    </mesh>
  );
}
```

---

## 2. 3D Text & Typography

### Flat Vector Typography (`<Text>`)
Crisp, resolution-independent SDF text rendered directly into the 3D scene:
```tsx
import { Text } from "@react-three/drei";

<Text
  fontSize={0.5}
  color="#ffffff"
  anchorX="center"
  anchorY="middle"
  font="/fonts/Inter-Bold.woff"
  maxWidth={4}
  lineHeight={1.2}
>
  Next-Gen Experience
</Text>
```

### Extruded 3D Mesh Text (`<Text3D>`)
Solid 3D extruded geometry using JSON fonts:
```tsx
import { Text3D, Center } from "@react-three/drei";

<Center>
  <Text3D font="/fonts/helvetiker_regular.typeface.json" size={0.75} height={0.2} curveSegments={12}>
    ANTIGRAVITY
    <meshNormalMaterial />
  </Text3D>
</Center>
```

---

## 3. Asset Loading Helpers

### `useGLTF` & `<Clone>`
```tsx
import { useGLTF, Clone } from "@react-three/drei";

function Forest() {
  const { scene } = useGLTF("/models/tree.glb");

  return (
    <>
      <Clone object={scene} position={[-2, 0, 0]} />
      <Clone object={scene} position={[0, 0, -2]} scale={1.2} />
      <Clone object={scene} position={[2, 0, 1]} scale={0.8} />
    </>
  );
}
```

### Loading Screen (`<Loader />`)
Ready-made animated loading progress overlay:
```tsx
import { Loader } from "@react-three/drei";

export default function App() {
  return (
    <>
      <Canvas>...</Canvas>
      <Loader /> {/* Automatically tracks all useGLTF / useTexture loading progress! */}
    </>
  );
}
```

---

## 4. Performance Optimization Toolkit

### 1. Accelerated Raycasting (`<Bvh>`)
Speeds up pointer clicks, hovers, and raycasts by up to 100x on complex meshes:
```tsx
import { Bvh } from "@react-three/drei";

<Bvh firstHitOnly>
  <HeavyCharacterModel onClick={handleClick} />
</Bvh>
```

### 2. High-Density Instancing (`<Instances>`)
Render 10,000+ objects with a single draw call:
```tsx
import { Instances, Instance } from "@react-three/drei";

<Instances range={1000}>
  <boxGeometry />
  <meshStandardMaterial />
  {positions.map((pos, i) => (
    <Instance key={i} position={pos} color={colors[i]} />
  ))}
</Instances>
```

### 3. Adaptive Performance Scaling
Automatically scales resolution down on mobile / low-end GPUs:
```tsx
import { AdaptiveDpr, PerformanceMonitor } from "@react-three/drei";

<Canvas>
  <PerformanceMonitor onDecline={() => console.log("Degrading quality for FPS")} />
  <AdaptiveDpr pixelated />
  {/* Scene Content */}
</Canvas>
```

