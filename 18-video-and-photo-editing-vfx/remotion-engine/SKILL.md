---
name: remotion-engine
description: React and web-standards programmatic video creation engine. Use when coding videos in React, rendering web components/Three.js/CSS keyframes directly into MP4 frames, data-driven video generation, and creating programmatic SaaS product launch trailers.
---

# Remotion Engine

> **Domain:** Web-Code Video Generation  
> **Key Tools / Runtimes:** Remotion CLI, @remotion/renderer, React  
> **Architecture:** Antigravity Global Media Engine (Ponytail Minimalist Architecture)

---

## 1. Overview & Capabilities
The `remotion-engine` skill equips Antigravity AI agents with complete, self-contained capabilities for remotion engine. It integrates directly with local binaries (FFmpeg, OpenCV, Python PIL, Kinocut, ImageSorcery) to provide deterministic, high-performance media processing without heavy GUI bloat.

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
remotion-engine --input source.ext --output processed.ext
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
