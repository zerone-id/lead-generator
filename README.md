# Lead Generator

Phase 1 provides a minimal, reviewable scaffold for a lead-generation service.

## Project Layout

- `pyproject.toml`: Python dependency and packaging manifest.
- `src/lead_generator/main.py`: CLI entry point for running the Phase 1 pipeline.
- `src/lead_generator/scoring.py`: Representative domain module for lead qualification logic.
- `src/lead_generator/models.py`: Shared data structures for lead records and results.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
lead-generator
```

## Phase 1 Scope

### Core modules/components

- **Entry point (`main.py`)**: orchestrates a small in-memory pipeline and emits scored lead results.
- **Domain models (`models.py`)**: defines typed dataclasses used across the codebase.
- **Scoring module (`scoring.py`)**: encapsulates the initial qualification heuristic and ranking behavior.

### Expected runtime/dependencies

- **Runtime**: Python 3.11+
- **Dependency management**: `pyproject.toml` with `setuptools` backend
- **Dependencies**: Standard library only in Phase 1 (no third-party runtime packages)

### Current known constraints

- Uses in-memory sample data only; no persistence layer or external CRM integrations.
- Scoring logic is heuristic and intentionally simple; thresholds are not yet calibrated from production data.
- No API/server process yet; current interface is CLI-only for baseline review.
