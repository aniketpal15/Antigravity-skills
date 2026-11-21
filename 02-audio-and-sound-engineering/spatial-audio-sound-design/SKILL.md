---
name: spatial-audio-sound-design
description: Binaural spatial audio positioning, 3D sound design, and Foley SFX synthesis engine. Use when placing audio sources in 3D virtual coordinates (x, y, z), rendering Head-Related Transfer Functions (HRTF), and synthesizing procedural sound effects (whooshes, UI clicks, ambient nature, sci-fi lasers).
---

# Spatial Audio Sound Design

> **Domain:** Spatial Audio & SFX Sound Design  
> **Key Tools / Runtimes:** PySofaConventions, Web Audio API Spatial Panner, FFmpeg sofalizer  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `spatial-audio-sound-design` skill gives Antigravity AI agents full operational mastery over spatial audio sound design. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

### Primary Functions:
- **Direct Automation:** Autonomous execution via standard library Python and native CLI binaries.
- **Fail-Fast Validation:** Verifies codecs, sample rates, geometry topologies, and formats before processing.
- **Deterministic Quality:** Maintains 100% precision without lossy unintended re-encoding or vertex degradation.

---

## 2. Standard Usage & Code Recipes

### Execution Pattern:
```python
# ponytail: Clean, minimal execution using standard library
import subprocess

# Invoke native engine with validated parameters
print("Executing spatial-audio-sound-design pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
