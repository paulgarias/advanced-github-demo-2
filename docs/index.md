# statlite

A small, dependency-free statistics library, and the demo project for the
**Advanced GitHub** workshop.

```python
import statlite

statlite.mean([1, 2, 3, 4])  # 2.5
statlite.percentile([1, 2, 3, 4], 25)  # 1.75
statlite.pearson([1, 2, 3], [2, 4, 6])  # 1.0
```

## Features

- Descriptive statistics: `mean`, `median`, `mode`, `variance`, `stdev`
- Quantiles: `percentile`, `iqr`
- Association: `covariance`, `pearson`
- Fully typed, documented with NumPy-style docstrings, no runtime dependencies

!!! note
    These docs are rebuilt on every merge to `main` (the **dev** version) and
    versioned for every tagged release.
