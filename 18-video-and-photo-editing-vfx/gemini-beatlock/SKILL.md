---
name: gemini-beatlock
description: Extract frame-accurate audio beatmaps, spectral onsets, and retention scene cuts using the librosa-powered analyzer.
---

# Gemini Beatlock Skill

## Usage
Run the beatlock engine against any background track or reference video:
```bash
python3 packages/gemini-audio-beatlock/analyze_media.py input.mp3 --fps 30 -o beatmap.json
```

Use the generated `beat_frames` and `recommended_retention_cuts` to automate Remotion composition cuts and transitions.
