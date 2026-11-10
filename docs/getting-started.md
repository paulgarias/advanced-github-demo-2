# Getting started

## Install

```bash
pip install -i https://test.pypi.org/simple/ statlite
```

## Usage

```python
from statlite import mean, stdev, pearson

heights = [1.62, 1.75, 1.80, 1.68, 1.71]
weights = [58, 72, 80, 63, 68]

print(mean(heights))
print(stdev(heights))  # sample standard deviation (ddof=1)
print(pearson(heights, weights))
```

Every function accepts any iterable of numbers and raises `ValueError` for
invalid input, such as empty data.
