# Contributing

Thanks for helping! The full guide lives in the docs:
[Contributing](docs/contributing.md).

Quick version:

1. Branch from an up-to-date `main`: `git switch -c feature/<short-name>`.
2. Install and enable the checks: `pip install -e ".[dev]"` then `pre-commit install`.
3. Make focused commits, and run `ruff format .`, `ruff check .`, `mypy` and `pytest`.
4. Update `CHANGELOG.md`, push, and open a pull request using the template.
5. CI must pass and a maintainer must approve before merge.

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).
