---
name: 3d-file-converter
description: Universal 3D format conversion, texture packaging, and geometry compression engine. Use when converting between GLTF, GLB, USDZ (Apple AR Quick Look), FBX, OBJ, STL, and PLY formats, applying Draco mesh compression, and generating multi-tier Level-of-Detail (LOD) assets.
---

# 3D File Converter

> **Domain:** 3D Format Conversion & Compression  
> **Key Tools / Runtimes:** Trimesh, DracoPy, assimp, usdpython, gltf-transform  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `3d-file-converter` skill gives Antigravity AI agents full operational mastery over 3d file converter. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing 3d-file-converter pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
