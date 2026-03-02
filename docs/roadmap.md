# Product Roadmap

## Phase 1 — Foundation (Current)
**Objective:** Establish a reliable baseline that allows the team to run, test, and extend the product.

### Deliverables
- Project skeleton under `src/`, `tests/`, and `docs/`.
- Runnable application entrypoint.
- Baseline product and contributor documentation.

### Acceptance Criteria
- `python -m lead_generator` runs successfully with `PYTHONPATH=src`.
- `python -m unittest discover -s tests` passes with `PYTHONPATH=src`.
- `README.md` defines Phase 1 scope, architecture, stack, and status.
- `CONTRIBUTING.md` includes local check/test commands.

---

## Phase 2 — Core Domain Workflow
**Objective:** Implement first usable lead intake and qualification workflow.

### Deliverables
- Lead domain model with validation.
- Local persistence abstraction and in-memory implementation.
- Service layer for creating and listing leads.
- Unit tests for validation and service behavior.

### Acceptance Criteria
- Lead creation rejects invalid payloads and accepts valid payloads.
- Lead listing returns deterministic results from storage adapter.
- Tests cover happy path and validation failures.
- Modules are organized and documented for future API integration.

### What “Next Phase” Means
When all Phase 1 acceptance criteria are met, the next phase is **Phase 2** implementation. This means shipping concrete lead-management capabilities in code (not only docs), with tests proving business behavior.

---

## Phase 3 — Integration Surface
**Objective:** Expose lead workflow through a stable interface.

### Deliverables
- API or CLI command set for lead CRUD operations.
- Request/response serialization layer.
- Integration tests for interface contract.

### Acceptance Criteria
- Interface supports create/list/update lead operations.
- Input/output contract is documented and versioned.
- Integration tests validate end-to-end usage through public interface.
