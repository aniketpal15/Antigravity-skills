---
name: cli-anything
description: >-
  Making ALL Software Agent-Native by HKUDS. Autonomous framework that converts
  any desktop GUI application, complex software, API, or library into a clean,
  standardized, agent-executable command-line interface with JSON outputs.
metadata:
  argument-hint: "[software_or_repo] — build agent-native CLI harness"
  triggers:
    - "cli-anything"
    - "agentize software"
    - "build cli harness"
    - "gui to cli"
    - "software agent native"
---

# CLI-Anything (HKUDS)

CLI-Anything is an autonomous agent harness builder created by HKUDS (Hong Kong University Data Intelligence Lab) that makes any software program natively controllable by AI agents through standardized CLI commands.

## Architecture & 7-Phase Methodology

1. **Phase 1: Software Analysis**: Maps the target software's core capabilities, internal APIs, CLI flags, IPC interfaces, and file formats.
2. **Phase 2: Interface Mapping**: Designs deterministic subcommands and parameters corresponding to software features.
3. **Phase 3: Core Implementation**: Builds the Python-based execution bridge using Click/Typer and subprocess handling.
4. **Phase 4: CLI Implementation**: Formats all command responses with clean `--json` outputs for structured agent consumption.
5. **Phase 5: Test Suite Generation**: Writes unit and integration tests with synthetic and real file inputs to verify functionality.
6. **Phase 6: Verification & Validation**: Runs headless execution passes to verify zero hangs, clean exit codes, and reliable stderr capture.
7. **Phase 7: SKILL.md Synthesis**: Auto-generates the canonical agent skill file linking the agent directly to the newly built CLI.

## Usage Guidelines

- Always prefer agent-native CLIs over brittle GUI mouse/keyboard automation.
- Run commands with `--json` to receive structured, machine-parsable dictionaries.
- Use the accompanying `cli-hub` package manager to discover and install existing prebuilt software harnesses.
