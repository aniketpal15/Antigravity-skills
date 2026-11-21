---
name: leva-controls
description: >
  Floating GUI control panels for React and react-three-fiber scenes using leva.
  Use when debugging 3D scenes, tweaking values live, adding dev control panels,
  creating leva controls, useControls hook, leva GUI, leva panel, leva inputs,
  leva folder, leva button, leva color picker, leva slider, leva vector, leva
  react-three-fiber integration, r3f debug panel, r3f tweakable, dev controls,
  scene inspector, leva schema, leva plugin.
metadata:
  author: pmndrs
  version: "0.9.35"
  source: https://github.com/pmndrs/leva
---

# leva — Floating GUI Control Panels

> **Auto-activates** when you mention: *leva*, *useControls*, *leva panel*, *debug controls*, *GUI controls*, *tweakable values*, *leva inputs*, *r3f debug panel*, *leva folder*, *leva button*.

Leva gives you a floating panel UI for tweaking React state at runtime — perfect for 3D scenes, design prototyping, and dev-only debug panels.

---

## Installation

```bash
npm i leva
# optional plugins
npm i @leva-ui/plugin-bezier @leva-ui/plugin-spring @leva-ui/plugin-plot
```

---

## Quick Start — `useControls`

```jsx
import { useControls } from 'leva'

function Box() {
  const { color, scale, speed } = useControls({
    color: '#ff6080',
    scale: { value: 1, min: 0.1, max: 5, step: 0.1 },
    speed: 2,
  })

  return <mesh scale={scale}><boxGeometry /><meshStandardMaterial color={color} /></mesh>
}
```

The panel appears automatically — no `<Leva />` provider needed unless you want to customize it.

---

## All Input Types

### Number (plain)
```js
const { size } = useControls({ size: 42 })
```

### Range (number + min/max)
```js
const { opacity } = useControls({
  opacity: { value: 1, min: 0, max: 1, step: 0.01 },
})
```

### Color
```js
const { bg, tint } = useControls({
  bg: '#1a1a2e',                              // hex string
  tint: { r: 200, g: 100, b: 50, a: 0.8 },  // rgba object
})
```

### Boolean (toggle)
```js
const { wireframe } = useControls({ wireframe: false })
```

### String
```js
const { label } = useControls({ label: 'Hello World' })
// multi-line
const { notes } = useControls({ notes: { value: 'line1\nline2', rows: 3 } })
```

### Select / Dropdown
```js
const { preset } = useControls({
  preset: {
    value: 'medium',
    options: { Low: 'low', Medium: 'medium', High: 'high' },
  },
})
```

### Vector2
```js
const { pos } = useControls({ pos: { x: 0, y: 0 } })
// or array: { pos: [0, 0] }
```

### Vector3
```js
const { rotation } = useControls({ rotation: { x: 0, y: 0, z: 0 } })
// or array: { rotation: [0, 0, 0] }
```

### Interval
```js
const { range } = useControls({
  range: { value: [2, 8], min: 0, max: 10 },
})
```

### Image Upload
```js
const { texture } = useControls({ texture: { image: undefined } })
// returns data URL or undefined
```

### Button
```js
import { button } from 'leva'

useControls({
  reset: button(() => console.log('reset!')),
  export: button(() => downloadScene(), { disabled: false }),
})
```

---

## Folder Grouping

```js
import { folder } from 'leva'

const { x, y, z, color } = useControls({
  position: folder({
    x: 0, y: 1, z: 0,
  }),
  material: folder({
    color: '#fff',
  }, { collapsed: true }),
})
```

Nested folders are supported.

---

## `<Leva />` Component (optional — for customization)

```jsx
import { Leva } from 'leva'

function App() {
  return (
    <>
      {/* Hide panel in production */}
      <Leva hidden={process.env.NODE_ENV === 'production'} />
      <Canvas>...</Canvas>
    </>
  )
}
```

Props: `hidden`, `theme`, `flat`, `oneLineLabels`, `collapsed`, `titleBar`.

---

## Multiple Independent Panels

```js
import { useControls, useCreateStore, LevaPanel } from 'leva'

// Create a named store
const store = useCreateStore()

function Controls() {
  const { speed } = useControls('myPanel', { speed: 1 }, { store })
  return null
}

function UI() {
  return <LevaPanel store={store} />
}
```

---

## React Three Fiber Integration

```jsx
import { useControls } from 'leva'
import { useFrame } from '@react-three/fiber'
import { useRef } from 'react'

function SpinningBox() {
  const meshRef = useRef()
  const { rotationSpeed, color, scale } = useControls('SpinningBox', {
    rotationSpeed: { value: 1, min: 0, max: 10 },
    color: '#ff6080',
    scale: { value: 1, min: 0.1, max: 3 },
  })

  useFrame((_, delta) => {
    meshRef.current.rotation.y += delta * rotationSpeed
  })

  return (
    <mesh ref={meshRef} scale={scale}>
      <boxGeometry />
      <meshStandardMaterial color={color} />
    </mesh>
  )
}
```

---

## Controlled (Programmatic) Values

```js
import { useControls } from 'leva'

function MyComp() {
  const [{ x }, set] = useControls(() => ({ x: 0 }))

  // Update from outside the panel
  const reset = () => set({ x: 0 })

  return <button onClick={reset}>Reset X ({x})</button>
}
```

---

## Common Options (all inputs)

```js
useControls({
  myInput: {
    value: 42,
    label: 'My Custom Label',  // display name
    hint: 'This controls size', // tooltip
    disabled: false,
    render: (get) => get('someToggle') === true,  // conditional visibility
  },
})
```

---

## Dev-Only Panel Pattern

```jsx
import { Leva } from 'leva'

// Hide in production — zero cost at runtime
<Leva hidden={import.meta.env.PROD} />
```

---

## Theming

```jsx
import { Leva } from 'leva'

<Leva
  theme={{
    colors: {
      elevation1: '#292d39',
      elevation2: '#181c20',
      elevation3: '#373c4b',
      accent1: '#0066dc',
      accent2: '#007bff',
      highlight1: '#535760',
      highlight2: '#8c92a4',
      highlight3: '#fefefe',
    },
    sizes: {
      rootWidth: '280px',
      controlWidth: '160px',
    },
  }}
/>
```

---

## Plugins

```bash
npm i @leva-ui/plugin-bezier
```

```js
import { bezier } from '@leva-ui/plugin-bezier'
import { spring } from '@leva-ui/plugin-spring'

const { curve, springConfig } = useControls({
  curve: bezier([0.25, 0.1, 0.25, 1]),
  springConfig: spring(),
})
```

---

## Best Practices

- **Always hide in production** with `<Leva hidden={isProd} />` — the hook still works, panel just disappears.
- **Name your control groups** via `useControls('ComponentName', {...})` to avoid key collisions across components.
- **Use `folder()` with `collapsed: true`** for dense panels to keep things tidy.
- **Use `button()`** for one-shot actions (export, reset, randomize) instead of wiring extra UI.
- **Pair with react-three/fiber's `useFrame`** to drive animation params live.
- **`useCreateStore` + `LevaPanel`** when you need multiple independent panels side by side.

