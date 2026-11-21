---
name: gemini-video-director
description: Direct and assemble frame-accurate, monetizable social media videos using Remotion, Three.js, and Gemini 3.8 Flash High.
---

# Gemini Video Director Skill

This skill guides Gemini 3.8 Flash High in constructing end-to-end procedural video compositions within Google Antigravity.

## Instructions
1. When generating or editing video scenes, import components from the local packages:
   - Layout & Aspect: `ResponsiveCineCanvas` from `packages/gemini-cinecode-99`
   - Safe Zones: `SocialSafeZoneOverlay` from `packages/gemini-shotcraft-studio`
   - 3D Physics: `Gemini3DPhysicsStage` from `packages/gemini-3d-physics-stage`
   - Visual FX: `PixelFXOverlay` from `packages/gemini-pixelfx-vfx`
2. Never write non-deterministic animation loops (`requestAnimationFrame`, `Date.now()`). Use `useCurrentFrame()` and `useVideoConfig().fps`.
3. Follow the retention guidelines: trigger visual state shifts every 2.5 to 3.8 seconds, snapped to audio beats.
