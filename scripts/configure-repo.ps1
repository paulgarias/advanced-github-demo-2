<#
.SYNOPSIS
  One-time GitHub repository configuration for the demo (run after the first push).

.DESCRIPTION
  Applies the "protect main" ruleset, creates the testpypi environment, enables
  Pages from the gh-pages branch (after the docs workflow has created it), and
  creates workshop labels. Requires: gh auth with admin rights on the repo.
#>
param(
  [string]$Repo = "paulgarias/advanced-github-demo-2"
)

$ErrorActionPreference = "Stop"

Write-Host "Applying ruleset..."
gh api -X POST "repos/$Repo/rulesets" --input .github/rulesets/protect-main.json

Write-Host "Creating testpypi environment..."
gh api -X PUT "repos/$Repo/environments/testpypi" | Out-Null

Write-Host "Creating labels..."
$labels = @(
  @{ name = "good first issue"; color = "7057ff"; description = "Good for newcomers" },
  @{ name = "workshop"; color = "0e8a16"; description = "Workshop exercise" },
  @{ name = "conflict-demo"; color = "d93f0b"; description = "Branch built to produce a merge conflict" }
)
foreach ($l in $labels) {
  gh label create $l.name --color $l.color --description $l.description --repo $Repo --force
}

Write-Host @"

Manual steps remaining:
  1. After the docs workflow first runs: Settings > Pages > Source: 'Deploy from a branch', branch gh-pages, / (root).
  2. On test.pypi.org: add a Trusted Publisher (owner/repo, workflow 'release.yml', environment 'testpypi').
  3. (Optional) Add CODECOV_TOKEN secret and install the Codecov app.
  4. (Optional) Enable the Zenodo-GitHub integration for DOI minting on release.
"@
