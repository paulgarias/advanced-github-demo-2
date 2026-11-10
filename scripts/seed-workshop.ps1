<#
.SYNOPSIS
  Seeds workshop issues and pushes the prepared demo branches.

.DESCRIPTION
  Run once, after the initial push of main and after configure-repo.ps1.
  Demo branches pushed (never merge these before the workshop):
    feature/geometric-mean, feature/harmonic-mean  -> merge conflict exercise
    demo/failing-ci                                -> CI gating exercise
#>
param(
  [string]$Repo = "quantumdot/advanced-github-demo-2"
)

$ErrorActionPreference = "Stop"

foreach ($b in "feature/geometric-mean", "feature/harmonic-mean", "demo/failing-ci") {
  git push origin $b
}

$criteria = @"

**Acceptance criteria**
- [ ] Implementation with type hints
- [ ] NumPy-style docstring with an example
- [ ] Unit and property-based tests
- [ ] Exported from ``statlite/__init__.py``
- [ ] Entry in ``CHANGELOG.md``
"@

$issues = @(
  @{ title = "Add median absolute deviation (mad)"; labels = "enhancement,workshop,good first issue"
     body = "Add ``mad(data)`` to ``descriptive.py``: the median of absolute deviations from the median." },
  @{ title = "Add z-scores (zscores)"; labels = "enhancement,workshop"
     body = "Add ``zscores(data, ddof=1)`` returning standardized values. Put it in a new ``standardize.py`` module. Note: the ``demo/failing-ci`` branch contains a broken draft; do not reuse it." },
  @{ title = "Add skewness"; labels = "enhancement,workshop"
     body = "Add ``skewness(data)`` (adjusted Fisher-Pearson) to ``descriptive.py``." },
  @{ title = "Add Spearman rank correlation"; labels = "enhancement,workshop"
     body = "Add ``spearman(x, y)`` to ``correlation.py``. Handle tied ranks using average ranks." },
  @{ title = "Add a docs tutorial: working with real data"; labels = "documentation,workshop,good first issue"
     body = "Add ``docs/tutorial.md`` with a worked example, and add it to the nav in ``mkdocs.yml``. ``mkdocs build --strict`` must pass." },
  @{ title = "Resolve the geometric/harmonic mean branch conflict"; labels = "workshop,conflict-demo"
     body = "Branches ``feature/geometric-mean`` and ``feature/harmonic-mean`` edit the same lines in four files. Open PRs for both, merge the first, then resolve the conflicts on the second so that both functions are kept and exported." }
)

foreach ($i in $issues) {
  $body = $i.body
  if ($i.labels -like "*enhancement*") { $body += "`n$criteria" }
  gh issue create --repo $Repo --title $i.title --body $body --label $i.labels
}
