"""Core application bootstrap utilities for Lead Generator."""


def get_app_status() -> dict[str, str]:
    """Return current runtime metadata for the baseline application."""
    return {
        "name": "lead-generator",
        "phase": "Phase 1",
        "status": "baseline-ready",
    }
