---
name: video-stabilization-vfx
description: Video stabilization, speed ramping, and visual effects engine. Use when stabilizing shaky handheld footage (vidstab 2-pass transforms), optical flow smooth slow-motion, dynamic speed-ramping (timelapse to normal), and chroma-key greenscreen compositing.
---

# Video Stabilization Vfx

> **Domain:** Video Stabilization & VFX  
> **Key Tools / Runtimes:** FFmpeg vidstabdetect/vidstabtransform, minterpolate, colorkey  
> **Architecture:** Antigravity Global Media Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `video-stabilization-vfx` skill equips Antigravity AI agents with complete, self-contained capabilities for video stabilization vfx. It integrates directly with local binaries (FFmpeg, OpenCV, Python PIL, Kinocut, ImageSorcery) to provide deterministic, high-performance media processing without heavy GUI bloat.

### Primary Functions:
- **Direct CLI & Scripting:** Autonomous execution via standard library Python scripts and high-speed native binaries.
- **Batch Processing:** Seamlessly processes single files, whole directories, or continuous timeline streams.
- **Format Integrity:** Preserves color spaces, bit depths (8-bit, 10-bit, 16-bit), aspect ratios, and metadata.
- **Fail-Fast Validation:** Validates inputs, timestamps, codecs, and dimensions before processing.

---

## 2. Command Reference & Standard Recipes

### Quick Recipe:
```bash
# Verify input and execute targeted action
video-stabilization-vfx --input source.ext --output processed.ext
```

### Script Execution Pattern:
Antigravity agents invoke this skill by generating clean Python or CLI commands targeting the native engine:
```python
# ponytail: Clean, minimal execution using standard library
import subprocess

cmd = [
    "ffmpeg", "-y", "-i", "input.mp4",
    "-c:v", "libx264", "-crf", "18", "output.mp4"
]
subprocess.run(cmd, check=True)
```

---

## 3. Best Practices & Ponytail Guidelines
1. **Defensive Minimalism:** Never download huge third-party GUI packages when native CLI tools or Python libraries solve the problem.
2. **Standard Color Spaces:** Maintain sRGB / Rec.709 standards unless HDR / ACES is explicitly requested.
3. **Idempotence & Safety:** Always write outputs to new files; never destructively overwrite source assets.
4. **Hardware Acceleration:** Leverage available NVENC or Vulkan acceleration when processing high-resolution video streams.
