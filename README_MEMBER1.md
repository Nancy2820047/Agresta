# Agresta — Member 1 Phase 1 Delivery

This package is intended to be added on branch `feature/phase1-architecture` in the existing repository. Do **not** replace the repository's root README or existing module folders.

## Files
- `docs/architecture/requirements.md` — use cases, requirements, acceptance criteria.
- `docs/architecture/architecture.md` — architecture diagrams, protocols, dependencies and integration points.
- `docs/architecture/sensor_contract.md` — versioned measurement schema for all sensor owners.
- `docs/architecture/phase1_integration.md` — coordination and demonstration checklist.
- `integration/mock_pipeline.py` — laptop-only, mock sensor threading and data validation.
- `integration/__init__.py` — Python package marker.
- `tests/test_mock_pipeline.py` — standard-library tests.

## Run on laptop
From repository root:
```bash
python -m unittest discover -s tests -v
python -m integration.mock_pipeline
```
Mock data is **not** real Phase 1 sensor demonstration. Member 4 must use the professor's required concurrency template for graded multithreading.

## Mandatory team review before integration
Agree contract names and units with Members 2–5, verify Pi model and GPIO wiring, obtain course template and TA approval, and check Phase 1 demonstration on physical sensors.
