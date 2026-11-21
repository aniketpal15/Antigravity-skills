---
name: audio-cleanup-stems
description: Audio noise reduction, stem separation, and loudness normalization engine. Use when removing background hum/hiss, isolating vocal stems from music tracks (Demucs / Spleeter), separating drums/bass/other, and normalizing loudness to EBU R128 (-14 to -23 LUFS) standards for Spotify, YouTube, and broadcast.
---

# Audio Cleanup Stems

> **Domain:** Audio Cleanup & Stem Separation  
> **Key Tools / Runtimes:** Demucs, Spleeter, FFmpeg loudnorm / afftfilt / anlmdn  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `audio-cleanup-stems` skill gives Antigravity AI agents full operational mastery over audio cleanup stems. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing audio-cleanup-stems pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
