# Lead Generator

## Phase 1 Product Scope

### Goals
Phase 1 establishes the product foundation for a lead generation platform by delivering:
- A runnable application skeleton with clear module boundaries.
- Foundational documentation for delivery sequencing.
- A baseline contributor workflow for local checks and tests.

Phase 1 intentionally focuses on structure and delivery readiness instead of production integrations.

### Architecture (Phase 1)
The codebase currently uses a lightweight modular architecture:
- `src/lead_generator/`: Application package.
  - `app.py`: Core bootstrap logic and runtime metadata.
  - `__main__.py`: CLI entrypoint.
- `tests/`: Unit tests validating bootstrap behavior.
- `docs/`: Product planning and roadmap artifacts.

### Technology Stack
- **Language**: Python 3.11+
- **Test Framework**: Python standard library `unittest`
- **Packaging/Execution**: Module execution via `python -m lead_generator`

### Current Status
Phase 1 baseline is in place:
- ✅ Initial project structure created.
- ✅ Runnable entrypoint implemented.
- ✅ Baseline test coverage for startup metadata added.
- ✅ Roadmap and contribution guidance documented.

## Quickstart

```bash
python -m lead_generator
```

Expected output includes current project phase and status text.
