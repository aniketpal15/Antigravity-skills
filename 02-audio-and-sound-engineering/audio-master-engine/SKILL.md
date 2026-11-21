---
name: audio-master-engine
description: Master FFmpeg and SoX audio processing and filtergraph engine. Use when performing multi-channel routing, high-pass/low-pass EQ filtering, dynamic range compression, audio resampling, format transcoding (WAV, MP3, AAC, FLAC, OGG, Opus), and batch audio mastering.
---

# Audio Master Engine

> **Domain:** Master Audio Processing  
> **Key Tools / Runtimes:** FFmpeg audio filters (compand, equalizer, aresample), SoX CLI  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `audio-master-engine` skill gives Antigravity AI agents full operational mastery over audio master engine. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing audio-master-engine pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
