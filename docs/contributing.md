# Contributing

## Workflow

1. Pick or open an [issue](https://github.com/paulgarias/advanced-github-demo-2/issues).
2. Create a branch from an up-to-date `main`: `git switch -c feature/<short-name>`.
3. Make small, focused commits with clear messages.
4. Run the checks locally (see below), then push and open a pull request.
5. Address review comments. When CI is green and you have an approval, the PR
   is merged into `main`.

## Local checks

```bash
pip install -e ".[dev]"
pre-commit install

ruff format --check .
ruff check .
mypy
pytest
mkdocs build --strict
```

## Code standards

- Format and lint with **ruff**; all public functions need NumPy-style docstrings
  with an `Examples` section (doctests are run in CI).
- Type annotations are required and checked with `mypy --strict`.
- New behavior needs tests; coverage must stay at or above 90%.
- Add a line to `CHANGELOG.md` under **Unreleased**.

## Releases

Releases are tag-driven. The version is derived from the git tag, so there is
no version number to edit.

```bash
git tag -a v0.2.0 -m "v0.2.0"
git push origin v0.2.0
```
