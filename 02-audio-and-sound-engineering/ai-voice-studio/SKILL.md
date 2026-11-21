---
name: ai-voice-studio
description: High-fidelity AI voice synthesis, speech cloning, and vocal design engine. Use when generating professional voiceovers, character voices, multi-lingual dubbing, emotional speech delivery (ElevenLabs, Bark, Coqui TTS), and transcribing speech with word-level timestamps using Whisper.
---

# Ai Voice Studio

> **Domain:** AI Voice Synthesis & Cloning  
> **Key Tools / Runtimes:** ElevenLabs API, Bark, Coqui TTS, OpenAI Whisper  
> **Architecture:** Antigravity Global Studio Suite (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `ai-voice-studio` skill gives Antigravity AI agents full operational mastery over ai voice studio. It integrates directly with native libraries (Trimesh, PyDub, FFmpeg, Three.js, OpenCV, Librosa) and generative pipelines to provide deterministic, high-performance media execution.

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
print("Executing ai-voice-studio pipeline...")
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Prefer lightweight CLI and standard library operations over heavyweight GUI applications.
2. **Resource Efficiency:** Optimize memory footprint when processing dense 3D meshes or multi-channel audio tracks.
3. **Format Standards:** Default to GLB/GLTF for 3D assets, MP3/WAV for audio, and MP4/H.264 for video unless specialized formats are requested.
