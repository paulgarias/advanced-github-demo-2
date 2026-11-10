# statlite

[![CI](https://github.com/quantumdot/advanced-github-demo-2/actions/workflows/ci.yml/badge.svg)](https://github.com/quantumdot/advanced-github-demo-2/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/quantumdot/advanced-github-demo-2/graph/badge.svg)](https://codecov.io/gh/quantumdot/advanced-github-demo-2)
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)](https://quantumdot.github.io/advanced-github-demo-2/)

A small, dependency-free statistics library. It is the demo project for the
**Advanced GitHub** workshop, so it is deliberately simple and is developed
with the practices the workshop teaches: feature branches, pull requests,
automated checks, versioned docs and tagged releases.

```python
>>> import statlite
>>> statlite.mean([1, 2, 3, 4])
2.5
>>> statlite.pearson([1, 2, 3], [2, 4, 6])
1.0
```

## Installation

```bash
pip install -i https://test.pypi.org/simple/ statlite
```

## Development

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows; use `source .venv/bin/activate` elsewhere
pip install -e ".[dev]"
pre-commit install

ruff format --check .         # formatting
ruff check .                  # linting + docstring style
mypy                          # static types
pytest                        # tests, doctests and coverage
mkdocs serve                  # preview the docs
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and pull request workflow.

## Citing

If you use this software, please cite it using [CITATION.cff](CITATION.cff).

## License

[MIT](LICENSE)
