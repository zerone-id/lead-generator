# Implement Phase 2

## Task Title
Implement Phase 2

## Goal
Deliver the first functional lead workflow aligned with `docs/roadmap.md` Phase 2 acceptance criteria.

## Concrete Deliverables
1. **Domain models**
   - Add `src/lead_generator/domain/lead.py` with lead entity and validation rules.
2. **Persistence layer**
   - Add `src/lead_generator/repositories/base.py` for repository interface.
   - Add `src/lead_generator/repositories/in_memory.py` for in-memory implementation.
3. **Application service**
   - Add `src/lead_generator/services/lead_service.py` with create/list operations.
4. **Entrypoint wiring**
   - Update `src/lead_generator/__main__.py` to demonstrate basic workflow invocation.
5. **Tests**
   - Add `tests/test_lead_validation.py` for domain validation behavior.
   - Add `tests/test_lead_service.py` for service and repository interaction.

## Definition of Done
- All new tests pass via `PYTHONPATH=src python -m unittest discover -s tests`.
- Phase 2 acceptance criteria in `docs/roadmap.md` are satisfied.
- Public behavior and module responsibilities are documented in `README.md`.
