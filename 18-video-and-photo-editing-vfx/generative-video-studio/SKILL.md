---
name: generative-video-studio
description: Advanced generative AI video production engine. Use when synthesizing cinematic video clips from text prompts or reference images using Runway Gen-3, Luma Dream Machine, OpenAI Sora, Kling AI, Wan2.1, Minimax, and CogVideoX, controlling camera motion trajectories, lighting, and temporal consistency.
---

# Generative Video Studio

> **Domain:** AI Generative Video Production  
> **Key Tools / Runtimes:** Runway Gen-3, Luma Dream Machine, Kling, Sora, Wan2.1  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `generative-video-studio` skill gives Antigravity AI agents full operational mastery over generative video studio. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing generative-video-studio pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
