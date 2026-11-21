---
name: viral-director
description: High-retention viral video structures, camera grammars, kinetic typography, and pacing curves extracted from top-performing code-driven videos.
---

# Viral Director Reference Guide

This reference library codifies the core visual structures, camera motion grammars, and pacing mechanisms derived from top code-driven viral videos (`vendors/awesome-opus5-5-videos/prompts/` and `data/videos.json`).

## 1. High-Performing Video Architectures

### The 3-Act Micro Structure (Shorts / Reels: 15s - 45s)
1. **Act 1: Visual Hook & Pattern Interrupt (0.0s – 2.5s)**
   - High velocity camera zoom-in (`useCurrentFrame` exponential easing `spring({ damping: 12, mass: 0.5 })`).
   - Dynamic 3D depth-of-field transition or dramatic Chromatic Aberration burst.
   - Punchy single-keyword typography with contrasting background fill.
2. **Act 2: Progressive Information Escalation (2.5s – End minus 3s)**
   - Visual rhythm synced to beat transients (onset strength peaks).
   - Macro view to exploded view transitions (Rapier physics drop or 3D rotation).
   - Micro-events every 2.0 - 3.5 seconds to retain algorithmic interest.
3. **Act 3: Seamless Loop or Climax Drop (Last 3s)**
   - High energy speed ramp leading directly back into frame 0 (for 100%+ retention loop scores).

## 2. Camera Motion & Visual Grammar
- **Handheld Micro-Jitter**: Deterministic pseudo-random noise (`Math.sin(frame * 0.1) * amplitude`) to emulate tactile production without camera shake drift.
- **Parallax Stacking**: Foreground UI / particle layer (PixelFX), Midground 3D subject (Three.js/Rapier), Background atmospheric shader (GLSL/Remotion).
- **Kinetic Typography**: Word-by-word pop (`spring` scale 0.8 -> 1.05 -> 1.0) with highlighted keywords in bright neon hex (`#00F5FF`, `#FF0055`, `#FFE600`).
- **Aspect Ratio Safe-Zones**: Keep all focal content centered, within the vertical 9:16 safe bounds (away from bottom 22% and right 15%).
