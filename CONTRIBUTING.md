# Contributing

## Local setup
1. Ensure Python 3.11+ is installed.
2. From repo root, set source path for local runs:
   ```bash
   export PYTHONPATH=src
   ```

## Run the app
```bash
PYTHONPATH=src python -m lead_generator
```

## Run checks and tests locally
Use the following commands before opening a PR:

```bash
PYTHONPATH=src python -m unittest discover -s tests
PYTHONPATH=src python -m compileall src tests
```

## Branching and commits
- Keep changes scoped to one roadmap step when possible.
- Include tests with behavior changes.
- Keep documentation in sync with implementation.
