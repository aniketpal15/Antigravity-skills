---
name: 3d-model-generation
description: AI 3D mesh and asset generation engine. Use when generating 3D models from text prompts or single images (image-to-3D), orchestrating Trellis, Tripo3D, Meshy, Shap-E, Point-E, InstantMesh, and Hunyuan3D generative pipelines.
---

# 3D Model Generation

> **Domain:** 3D Generation & Modeling  
> **Key Tools / Runtimes:** Shap-E, Point-E, Trellis, InstantMesh, Tripo3D, Meshy API  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `3d-model-generation` skill gives Antigravity AI agents full operational mastery over 3d model generation. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing 3d-model-generation pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
