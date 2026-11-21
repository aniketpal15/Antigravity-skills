---
name: omni-video
description: "AI Video Editing & Multi-Modal Generation Framework (Omni-Video 2). Supports instruction-based video editing, video-to-video style transfer, subject replacement, background alteration, inpainting, and camera motion control."
type: video-editing
---

# Omni-Video 2 — AI Video Understanding, Generation & Editing

Omni-Video 2 by Fudan University & Shanghai Academy of AI for Science bridges video understanding, generation, and multi-modal instruction-based editing.

## Core Capabilities
- **Video-to-Video Editing (V2V)**: Modify lighting, appearance, clothes, and environments based on natural language instructions.
- **Subject Replacement & Inpainting**: Replace characters, animals, or objects in source footage while maintaining layout and motion consistency.
- **Camera Control & Perspective Modification**: Alter camera pans, tilts, zooms, and angles across sequential video frames.
- **Style Transfer & Cinematic Atmosphere**: Transform realistic video footage into anime, watercolor, cyberpunk, or historical aesthetics.
- **Text-to-Video Generation (T2V)**: High-resolution temporal DiT generation guided by VLM semantics.

## Quick Usage / Prompts
- *"Use omni-video to edit this clip: replace the background with a futuristic cyberpunk cityscape."*
- *"Use omni-video to change the actor's leather jacket to a white lab coat."*
- *"Perform video inpainting on frame sequence using omni-video."*

## Pipeline Architecture
1. **Vision-Language Model (VLM)** expands concise user edit prompts into explicit temporal-semantic descriptions.
2. **Diffusion Transformer (DiT)** combines source VAE latents with expanded text conditioning via mixed cross-attention.
3. Preserves motion consistency, object spatial trajectories, and identity across all edited frames.
