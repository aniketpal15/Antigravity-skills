---
name: cli-hub
description: >-
  Package manager and marketplace client for agent-native CLIs by HKUDS.
  Allows agents to autonomously discover, install, inspect, and run prebuilt
  software harnesses from the official CLI-Hub registry.
metadata:
  argument-hint: "[search|install|list|run] — manage agent CLIs"
  triggers:
    - "cli-hub"
    - "cli-hub install"
    - "cli-hub search"
    - "discover clis"
    - "software harness"
---

# CLI-Hub Package Manager (HKUDS)

CLI-Hub is the official package manager for agent-native CLIs. It enables AI agents to dynamically search, install, and execute verified command-line harnesses for professional desktop applications and developer tools.

## Supported Software Ecosystem

Prebuilt harnesses available on CLI-Hub include:
- **Creative & 3D**: Blender, GIMP, Inkscape, Krita, Audacity, Shotcut, Kdenlive, FreeCAD
- **Productivity & Docs**: LibreOffice, Obsidian, Joplin, Zotero, Draw.io, Mermaid
- **Developer Tools**: FFmpeg, LLDB, PM2, Ollama, ChromaDB, CloudCompare, WireMock

## CLI Commands

```bash
# Search for an application harness
cli-hub search blender
cli-hub search gimp

# Install an agent harness directly onto system PATH
cli-hub install blender
cli-hub install gimp

# List all installed agent harnesses
cli-hub list

# Inspect harness details and capabilities
cli-hub info blender

# Uninstall a harness
cli-hub uninstall gimp
```

When an agent needs to automate a piece of software, it can search CLI-Hub first to see if a verified harness already exists before building one from scratch.
